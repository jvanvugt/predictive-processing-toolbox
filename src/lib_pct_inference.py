from ctypes import *
import numpy
import itertools
from scipy.optimize import minimize, minimize_scalar, brute, basinhopping

from lib_pct_read_network import *

PCTi=CDLL("./LibPCTInference.so")

PCTi.BeliefUpdating.restype = POINTER(c_double)

POSSIBLE_ALGORITHMS = ["Lauritzen", "Henrion", "Pearl", 
    "lsampling", "selfimportance", "backsampling", 
    "aissampling", "epissampling", "lbp", "Lauritzen_old"]
		
def belief_updating(network, algorithm="Lauritzen", target_nodes, evidence_nodes, evidences=["true"]):
	## TODO  check by hand if the joint probability is computed correctly
	if type(algorithm)==str:
		algorithm = POSSIBLE_ALGORITHMS.index(algorithm)
	## Algorithms in the smile libary are indicised as in POSSIBLE_ALGORITHMS.
	###### TODO: if value of NodeEvidence is int, find appropriate NodeEvidence value by getOutcomes

	# Todo: set targets, set evidence, set algorithm, update, return targets
	target_nodes.append('LISTEND')
	c_target_nodes = (c_char_p * (len(target_nodes)) ) ()
	for i in range(len(target_nodes)):
		c_target_nodes[i] = c_char_p(target_nodes[i])
	evidence_nodes.append('LISTEND')
	c_evidence_nodes=(c_char_p * (len(evidence_nodes)) ) ()
	for i in range(len(evidence_nodes)):
		c_evidence_nodes[i] = c_char_p(evidence_nodes[i])
	evidences.append('LISTEND')
	c_evidences = (c_char_p * (len(evidences)) ) ()
	for i in range(len(Evidences)):
		c_evidences[i] = c_char_p(evidences[i])

	c_probs = PCTi.BeliefUpdating(network, algorithm, c_target_nodes, c_evidence_nodes, c_evidences)
	probs = []
	innerprobs = []
	for prob in c_probs:
		if prob == -3:
			break
		elif prob == -2: 
			probs.append(innerprobs)
			innerprobs = []
		else:
			innerprobs.append(prob)
	return probs

def P11(network, target_node, evidence_node): # Probability of one Target given one evidence node
	outcomes = network.get_node_outcomes(evidence_node)
	for outcome in outcomes:
		probs = belief_updating(network, target_node, evidence_node, evidences)	
		print outcome, probs
	
def P1(Network, target_node, evidence_nodes):
	# Probability distribution of one target with multiple evidence nodes
	outcome_lists = []
	for node in evidence_nodes:
		outcome_lists.append(network.get_node_outcomes(node))
	# Generate all possible combinations of the outcomes of the individual nodes
	outcome_combinations = itertools.product(*OutcomeLists)

	return_outcomes = []
	return_probs = []
	for outcome in outcome_combinations:
		probs = belief_updating(network, target_node, evidence_nodes, list(outcome))	
		return_outcomes.append(list(outcome))
		return_probs.append(probs)
	return return_outcomes, return_probs 
    # returns names of outcome and probabilities of outcomes in format of list of distributions. There, distributions are lists with as many entries as outcomes, List of distribution is a list with one entry for any combination of Evidences. If evidences A,B can be both [T,F], then the list has four entries with [TT,TF,FT,FF]. (And a distribution for each entry.)
	
	

def P(network, target_nodes, evidence_nodes):
    # JOINT probability of multiple targets given multiple evidence nodes
	# P(A,B|C,D) = P(A|B,C,D) * P(B|C,D) --> call P1()
	joint_probabilities = []
	for i, target in enumerate(target_nodes):
		pure_outcomes, pure_probs = P1(network, target, target_nodes[i+1:] + evidence_nodes)
		i += 1
		# Reformat output probs
		outcomes = []
        probs = []
		for j in range(len(pure_outcomes)):
			probs = probs + pure_probs[j]
		if len(joint_probabilities)!=0:
			outcome_divider = len(joint_probabilities) / len(probs)
			for j in range(len(joint_probabilities)):
				for k in range(len(joint_probabilities[j])):
					joint_probabilities[j][k] *= probs[j/outcome_divider][k]
		else:
			joint_probabilities = probs
	final_probs = []
	packlength = len(joint_probabilities) / len(pure_outcomes)
	for j in range(len(pure_outcomes)):
		final_probs.append(joint_probabilities[j*packlength:(j+1)*packlength])
	return pure_outcomes, final_probs



def check_dependence2(network, target_nodes, evidence_nodes=[], Disp=False):
	# Returns bool stating if two nodes are dependent.
	A = P(Network, [target_nodes[0]], [target_nodes[1]]+evidence_nodes)[1]
	B = P(Network, [target_nodes[0]], evidence_nodes)[1]
	if A == B * (len(A)/len(B)):
		if Disp: 
            print "Independent: ", target_nodes[0], "and", target_nodes[1], "given", evidence_nodes
		return False
	else:
		if Disp: 
            print "Dependent: ", target_nodes[0], "and", target_nodes[1], "given", evidence_nodes
		return True
	# print P(Network, [target_nodes[0]], evidence_nodes)

def check_dependence(network, target_nodes, evidence_nodes=[], Disp=False):
	dependence_list = []
	for i in range(len(target_nodes) - 1):
		for j in range(i + 1, len(target_nodes)):
			dependence_list.append([target_nodes[i], target_nodes[j], Check_dependence2(network, [target_nodes[i], target_nodes[j]], evidence_nodes, Disp=Disp)])
	return dependence_list
