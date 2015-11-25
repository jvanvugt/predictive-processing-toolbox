from ctypes import *
import numpy
import itertools
from scipy.optimize import minimize, minimize_scalar, brute, basinhopping

PCTi=CDLL("./LibPCTInference.so")
from lib_pct_read_network import *

DefaultNetworkName="TestNetwork";


def PossibleAlgorithms():
	return ["Lauritzen","Henrion","Pearl","lsampling","selfimportance","backsampling","aissampling","epissampling","lbp","Lauritzen_old"];
		
def BelieveUpdating(NetworkName=DefaultNetworkName, Algorithm=0, TargetNodes=["Node"], EvidenceNodes=["Node"], Evidences=["true"]):
	## TODO  check by hand if the joint probability is computed correctly
	if type(Algorithm)==str:
		Algorithm=PossibleAlgorithms().index(Algorithm);
	## Algorithms in the smile libary are indicised as in the PossibleAlgorithms function.
	###### TODO: if value of NodeEvidence is int, find appropriate NodeEvidence value by getOutcomes

	# Todo: set targets, set evidence, set algorithm, update, return targets
	TargetNodes.append('LISTEND');
	c_TargetNodes=(c_char_p * (len(TargetNodes)) ) ()
	for i in range(len(TargetNodes)):
		c_TargetNodes[i] = c_char_p(TargetNodes[i]);
	EvidenceNodes.append('LISTEND');
	c_EvidenceNodes=(c_char_p * (len(EvidenceNodes)) ) ()
	for i in range(len(EvidenceNodes)):
		c_EvidenceNodes[i] = c_char_p(EvidenceNodes[i]);
	Evidences.append('LISTEND');
	c_Evidences=(c_char_p * (len(Evidences)) ) ()
	for i in range(len(Evidences)):
		c_Evidences[i] = c_char_p(Evidences[i]);

	PCTi.BelieveUpdating.restype = POINTER(c_double);
	c_probs = PCTi.BelieveUpdating(Ending(NetworkName), Algorithm, c_TargetNodes, c_EvidenceNodes, c_Evidences);
	probs = [];	prob=0; i=0;
	while prob!=-3:
		prob=c_probs[i];
		if (prob!=-3):
			probs.append(prob);
		i+=1;
	return probs

def P11(TargetNode="Node", EvidenceNode="Node"): # Probability of one Target given one evidence node
	Outcomes = GetOutcomes(NodeName=EvidenceNode);
	for outcome in Outcomes:
		probs=BelieveUpdating(TargetNodes=[TargetNode], EvidenceNodes=[EvidenceNode], Evidences=[outcome])	
		print outcome, probs
	
def P1(NetworkName=DefaultNetworkName, TargetNode="Node", EvidenceNodes=["Node"]):# Probability distribution of one target with multiple evidence nodes
	OutcomeLists=[];
	for node in EvidenceNodes:
		OutcomeLists.append(GetOutcomes(NetworkName=NetworkName, NodeName=node));
	OutcomeCombinations = itertools.product(*OutcomeLists); # generates all possible combinations of the outcomes of the individual nodes

	ReturnOutcomes=[];
	ReturnProbs=[];
	for outcome in OutcomeCombinations:
		probs=BelieveUpdating(NetworkName=NetworkName, TargetNodes=[TargetNode], EvidenceNodes=EvidenceNodes, Evidences=list(outcome))	
		ReturnOutcomes.append(list(outcome));
		ReturnProbs.append(probs[0:len(probs)-1])
	return [ReturnOutcomes,ReturnProbs]; # returns names of outcome and probabilities of outcomes in format of list of distributions. There, distributions are lists with as many entries as outcomes, List of distribution is a list with one entry for any combination of Evidences. If evidences A,B can be both [T,F], then the list has four entries with [TT,TF,FT,FF]. (And a distribution for each entry.)
	
	

def P(NetworkName=DefaultNetworkName, TargetNodes=["Node"], EvidenceNodes=["Node"]):# JOINT probability of multiple targets given multiple evidence nodes
	# P(A,B|C,D) = P(A|B,C,D) * P(B|C,D) --> call P1()
	i=0;
	JointProbabilities=[];
	OutcomeDevider=1;
	for target in TargetNodes:
		PureOutcomes, PureProbs = P1(NetworkName=NetworkName, TargetNode=target, EvidenceNodes=TargetNodes[i+1:] + EvidenceNodes)
		i+=1;
		# Reformat output probs
		Outcomes=[]; Probs=[];
		for j in range(len(PureOutcomes)):
			Probs = Probs + PureProbs[j];
		if len(JointProbabilities)!=0:
			OutcomeDevider=len(JointProbabilities)/len(Probs);
			for j in range(len(JointProbabilities)):
				JointProbabilities[j] *= Probs[j/OutcomeDevider];
		else:
			JointProbabilities = Probs;
	FinalProbs = [];
	packlength = len(JointProbabilities)/len(PureOutcomes);
	for j in range(len(PureOutcomes)):
		FinalProbs.append(JointProbabilities[j*packlength:(j+1)*packlength]);
	return PureOutcomes,FinalProbs;



def Check_dependence2(NetworkName=DefaultNetworkName, TargetNodes=["Node_1","Node_2"], EvidenceNodes=[], Disp = True):
	# Returns bool stating if two nodes are dependent.
	comparecounter = 0;
	#for i in range(len(GetOutcomes(NetworkName, NodeName = TargetNodes[1]))-1):
		# print P(NetworkName, [TargetNodes[0]], [TargetNodes[1]]+EvidenceNodes)[1][i]
		#if P(NetworkName, [TargetNodes[0]], [TargetNodes[1]]+EvidenceNodes)[1][i] != P(NetworkName, [TargetNodes[0]], [TargetNodes[1]]+EvidenceNodes)[1][i+1]:
			#comparecounter += 1;
	#if comparecounter == 0:
		#if Disp: print "Independent: ", TargetNodes[0], "and", TargetNodes[1]
		#return False
	#else:
		#if Disp: print "Dependent: ", TargetNodes[0], "and", TargetNodes[1]
		#return True
	A = P(NetworkName, [TargetNodes[0]], [TargetNodes[1]]+EvidenceNodes)[1]
	B = P(NetworkName, [TargetNodes[0]], EvidenceNodes)[1]
	if A == B * (len(A)/len(B)):
		if Disp: print "Independent: ", TargetNodes[0], "and", TargetNodes[1], "given", EvidenceNodes
		return False
	else:
		if Disp: print "Dependent: ", TargetNodes[0], "and", TargetNodes[1], "given", EvidenceNodes
		return True
	# print P(NetworkName, [TargetNodes[0]], EvidenceNodes)

def Check_dependence(NetworkName=DefaultNetworkName, TargetNodes=["Node_1","Node_2"], EvidenceNodes=[], Disp = False):
	DependenceList = [];
	for i in range(len(TargetNodes)-1):
		for j in range(i+1,len(TargetNodes)):
			DependenceList.append([TargetNodes[i],TargetNodes[j], Check_dependence2(NetworkName,[TargetNodes[i],TargetNodes[j]],EvidenceNodes,Disp=Disp)]);
	return DependenceList
