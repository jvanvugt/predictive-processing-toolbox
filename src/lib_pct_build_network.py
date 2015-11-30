from ctypes import *
import numpy
from lib_pct_tools import *
from lib_pct_read_network import *

PCTb=CDLL("./LibPCTBuildNetwork.so")

DefaultNetworkName="TestNetwork";


def CreateNetwork(NetworkName=DefaultNetworkName):
	return PCTb.CreateNetwork(Ending(NetworkName));
	
def WriteNetwork(Network, NetworkName=DefaultNetworkName):
	PCTb.WriteNetwork(Network, Ending(NetworkName))
	
def AddNode(Network, NodeName, Outcomes=["true","false"], Probabilities=[0.5, 0.5]):
	if NodeExists(Network, NodeName):
		print "Node %s already exists" % NodeName
	
	c_Outcomes=(c_char_p * (len(Outcomes)) ) ()
	for i in range(len(Outcomes)):
		c_Outcomes[i] = c_char_p(Outcomes[i]);

	if len(Probabilities)!=len(Outcomes): Probabilities=numpy.ones(len(Outcomes))/len(Outcomes)
	
	# Check values of probabilities
	if sum(Probabilities)!=1.0:
		rest = 1-sum(Probabilities[0:len(Probabilities)-1]);
		Probabilities[len(Probabilities)-1] = rest;
		print "Probabilities do not add to 1, last value has been changed to", rest
	for i in range(len(Probabilities)):
		if Probabilities[i]>1 or Probabilities[i]<0:
			raise ValueError("All Probabilities must be between 0 and 1")

	c_Probabilities=(c_double * (len(Probabilities)) ) ()
	for i in range(len(Probabilities)):
		c_Probabilities[i] = c_double(Probabilities[i]);

	PCTb.AddNode(Network, NodeName, c_Outcomes, c_Probabilities, len(Outcomes));
	

def AddValueNode(Network, NodeName="Node"):
	PCTb.AddValueNode(Network, NodeName);


def DeleteNode(Network, NodeName="Node"):
	PCTb.DeleteNode(Network, NodeName);


def SetOutcomes(Network, NodeName="Node",Outcomes=["true","false"]):
	######To check: what happens to the probabilities if the number of outcomes changes
	######To check: if NodeName exists, what to do if not?
	######Only possible to change number of outcomes if node has no children
	c_Outcomes=(c_char_p * (len(Outcomes)) )
	
	for i in range(len(Outcomes)):
		c_Outcomes[i] = c_char_p(Outcomes[i]);
	PCTb.SetOutcomes(Network, NodeName, c_Outcomes, len(Outcomes));


def SetProbabilities(Network, NodeName="Node", Probabilities=[0.5,0.5]):
	######To implement: if probabilities are of the wrong number for the Outcomes implemented
	######To check: if NodeName exists, what to do if not?
	###### how to account for conditional probabilities with many incoming arcs?
	c_Probabilities=(c_double * (len(Probabilities)) ) ()
	for i in range(len(Probabilities)):
		c_Probabilities[i] = c_double(Probabilities[i]);
	PCTb.SetProbabilities(Network, NodeName, c_Probabilities, len(Probabilities));


def AddArc(Network, StartNode="Node", GoalNode="Node1"):
	######To check: if Nodes exist, what to do if not?
	PCTb.AddArc(Network,StartNode, GoalNode);
	
	