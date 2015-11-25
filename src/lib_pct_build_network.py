from ctypes import *
import numpy
from lib_pct_tools import *

PCTb=CDLL("./LibPCTBuildNetwork.so")

DefaultNetworkName="TestNetwork";


def CreateNetwork(NetworkName=DefaultNetworkName):
	PCTb.CreateNetwork(Ending(NetworkName));

#def WriteNetwork(NetworkPointer, NetworkName=DefaultNetworkName):
	#PCTb.WriteNetwork(NetworkPointer, NetworkName);
	
	
def AddNode(NetworkName=DefaultNetworkName, NodeName="Node",Outcomes=["true","false"], Probabilities=[0.5,0.5]):
	######To implement: give hint if nodename already exists
	
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
			print "Error: All Probabilities must be between 0 and 1"
			return 0

	c_Probabilities=(c_double * (len(Probabilities)) ) ()
	for i in range(len(Probabilities)):
		c_Probabilities[i] = c_double(Probabilities[i]);

	#print Outcomes, Probabilities
	PCTb.AddNode(Ending(NetworkName), NodeName, c_Outcomes, c_Probabilities, len(Outcomes));
	#return PCTb.AddNode(NetworkPointer, NodeName, c_Outcomes, c_Probabilities, len(Outcomes));
	

def AddValueNode(NetworkName=DefaultNetworkName, NodeName="Node"):
	PCTb.AddValueNode(Ending(NetworkName), NodeName);


def DeleteNode(NetworkName=DefaultNetworkName, NodeName="Node"):
	PCTb.DeleteNode(Ending(NetworkName), NodeName);


def SetOutcomes(NetworkName=DefaultNetworkName, NodeName="Node",Outcomes=["true","false"]):
	######To check: what happens to the probabilities if the number of outcomes changes
	######To check: if NodeName exists, what to do if not?
	######Only possible to change number of outcomes if node has no children
	c_Outcomes=(c_char_p * (len(Outcomes)) ) ()
	# print Outcomes
	for i in range(len(Outcomes)):
		c_Outcomes[i] = c_char_p(Outcomes[i]);
	PCTb.SetOutcomes(Ending(NetworkName), NodeName, c_Outcomes, len(Outcomes));


def SetProbabilities(NetworkName=DefaultNetworkName, NodeName="Node", Probabilities=[0.5,0.5]):
	######To implement: if probabilities are of the wrong number for the Outcomes implemented
	######To check: if NodeName exists, what to do if not?
	###### how to account for conditional probabilities with many incoming arcs?
	
	# Check values of probabilities
#	if sum(Probabilities)!=1:
#		rest = 1-sum(Probabilities[0:len(Probabilities)-1]);
#		Probabilities[len(Probabilities)-1] = rest;
#		print "Probabilities do not add to 1, last value has been changed to", rest
#	for i in range(len(Probabilities)):
#		if Probabilities[i]>1 or Probabilities[i]<0:
#			print "Error: All Probabilities must be between 0 and 1"
#			return 0

	c_Probabilities=(c_double * (len(Probabilities)) ) ()
	for i in range(len(Probabilities)):
		c_Probabilities[i] = c_double(Probabilities[i]);
	PCTb.SetProbabilities(Ending(NetworkName), NodeName, c_Probabilities, len(Probabilities));


def AddArc(NetworkName=DefaultNetworkName, StartNode="Node", GoalNode="Node1"):
	######To check: if Nodes exist, what to do if not?
	PCTb.AddArc(Ending(NetworkName),StartNode, GoalNode);
	
	