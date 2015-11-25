from ctypes import *
import numpy
from lib_pct_tools import *

PCTr=CDLL("./LibPCTReadNetwork.so")
#libc = CDLL(ctypes.util.find_library('c'))

DefaultNetworkName="TestNetwork";



def NodeExists(NetworkName=DefaultNetworkName, NodeName="Node"):
	if PCTr.NodeExists(Ending(NetworkName), NodeName) == -2 :
		return False
	else:
		return True


def NodeNumber(NetworkName=DefaultNetworkName):
	return PCTr.NodeNumber(Ending(NetworkName))


def NodeNames(NetworkName=DefaultNetworkName):
	PCTr.NodeNames.restype = POINTER(POINTER(c_char))
	c_names = PCTr.NodeNames(Ending(NetworkName))
	names = [];	name=''; i=0;
	while name!='LISTEND':
		name=string_at(c_names[i]);
		if (name!='LISTEND'):
			names.append(name);
		i+=1;
	return names


def GetOutcomes(NetworkName=DefaultNetworkName, NodeName="Node"):
	PCTr.GetOutcomes.restype = POINTER(POINTER(c_char))
	c_names = PCTr.GetOutcomes(Ending(NetworkName),NodeName)
	names = [];	name=''; i=0;
	while name!='LISTEND':
		name=string_at(c_names[i]);
		if (name!='LISTEND'):
			names.append(name);
		i+=1;
	return names


def GetParents(NetworkName=DefaultNetworkName, NodeName="Node"):
	PCTr.GetParents.restype = POINTER(POINTER(c_char))
	c_names = PCTr.GetParents(Ending(NetworkName),NodeName)
	names = [];	name=''; i=0;
	while name!='LISTEND':
		name=string_at(c_names[i]);
		if (name!='LISTEND'):
			names.append(name);
		i+=1;
	return names


def GetChildren(NetworkName=DefaultNetworkName, NodeName="Node"):
	PCTr.GetChildren.restype = POINTER(POINTER(c_char))
	c_names = PCTr.GetChildren(Ending(NetworkName),NodeName)
	names = [];	name=''; i=0;
	while name!='LISTEND':
		name=string_at(c_names[i]);
		if (name!='LISTEND'):
			names.append(name);
		i+=1;
	return names
	
