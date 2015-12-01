from ctypes import *
import numpy
from lib_pct_tools import *
from lib_pct_read_network import *

PCTb=CDLL("./LibPCTBuildnetwork.so")

default_network_name = "TestNetwork"


def create_network():
	return PCTb.CreateNetwork();
	
def write_network(network, network_name=default_network_name):
	PCTb.WriteNetwork(network, Ending(networkName))
	
def add_node(network, node_name, outcomes=["true", "false"], probabilities=[0.5, 0.5]):
	if node_exists(network, node_name):
		print "Node %s already exists" % node_name
	
	c_outcomes = (c_char_p * (len(outcomes)) ) ()
	for i in range(len(outcomes)):
		c_outcomes[i] = c_char_p(outcomes[i])

	if len(probabilities)!=len(outcomes): 
		probabilities = numpy.ones(len(outcomes)) / len(outcomes)
	
	# Check values of probabilities
	if sum(probabilities) != 1.0:
		rest = 1 - sum(probabilities[0:len(probabilities) - 1])
		probabilities[-1] = rest
		print "Probabilities do not add to 1, last value has been changed to", rest
	for prob in probabilities:
		if prob > 1 or prob < 0:
			raise ValueError("All Probabilities must be between 0 and 1")

	c_probabilities = (c_double * (len(probabilities)) ) ()
	for i in range(len(probabilities)):
		c_probabilities[i] = c_double(Probabilities[i])

	PCTb.AddNode(network, node_name, c_outcomes, c_probabilities, len(outcomes));
	

def add_value_node(network, node_name="Node"):
	PCTb.AddValueNode(network, node_name)


def delete_node(network, node_name="Node"):
	PCTb.DeleteNode(network, node_name)


def set_outcomes(network, node_name="Node", outcomes=["true","false"]):
	######To check: what happens to the probabilities if the number of outcomes changes
	######To check: if NodeName exists, what to do if not?
	######Only possible to change number of outcomes if node has no children
	c_outcomes = (c_char_p * (len(outcomes)) )
	
	for i in range(len(Outcomes)):
		c_outcomes[i] = c_char_p(outcomes[i])
	PCTb.SetOutcomes(network, node_name, c_outcomes, len(outcomes))


def set_probabilities(network, node_name="Node", probabilities=[0.5,0.5]):
	######To implement: if probabilities are of the wrong number for the Outcomes implemented
	######To check: if NodeName exists, what to do if not?
	###### how to account for conditional probabilities with many incoming arcs?
	c_probabilities =(c_double * (len(probabilities)) ) ()
	for i in range(len(probabilities)):
		c_probabilities[i] = c_double(probabilities[i])
	PCTb.SetProbabilities(network, node_name, c_probabilities, len(probabilities))


def add_arc(network, start_node="Node", goal_node="Node1"):
	######To check: if Nodes exist, what to do if not?
	PCTb.AddArc(network, start_node, goal_node)
	
	