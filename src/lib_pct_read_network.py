from ctypes import *
import numpy
from lib_pct_tools import *

PCTr=CDLL("./LibPCTReadNetwork.so")

PCTr.LoadNetwork.restype = c_void_p

PCTr.ReloadNetwork.argtypes = [c_void_p, c_char_p]
PCTr.ReloadNetwork.restype = None

PCTr.NodeNames.argtypes = [c_void_p]
PCTr.NodeNames.restype = POINTER(POINTER(c_char))

PCTr.NodeNumber.argtypes = [c_void_p]
PCTr.NodeNumber.restype = c_int

PCTr.GetOutcomes.restype = POINTER(POINTER(c_char))
PCTr.GetOutcomes.argtypes = [c_void_p, c_char_p]

PCTr.GetParents.restype = POINTER(POINTER(c_char))
PCTr.GetParents.argtypes = [c_void_p, c_char_p]

PCTr.GetChildren.restype = POINTER(POINTER(c_char))
PCTr.GetChildren.argtypes = [c_void_p, c_char_p]

PCTr.NodeExists.restype = c_bool
PCTr.NodeExists.argtypes = [c_void_p, c_char_p]


DefaultNetworkName = "TestNetwork"

def LoadNetwork(NetworkName=DefaultNetworkName):
	return PCTr.LoadNetwork(Ending(NetworkName))

def ReloadNetwork(Network, NetworkName=DefaultNetworkName):
	PCTr.ReloadNetwork(Network, NetworkName)

def NodeExists(Network, NodeName):
	return PCTr.NodeExists(Network, NodeName)


def NodeNumber(Network):
	return PCTr.NodeNumber(Network)


def NodeNames(Network):
	c_names = PCTr.NodeNames(Network)
	return from_c_array(c_names)


def GetOutcomes(Network, NodeName):
	c_names = PCTr.GetOutcomes(Network, NodeName)
	return from_c_array(c_names)


def GetParents(Network, NodeName):
	c_names = PCTr.GetParents(Network, NodeName)
	return from_c_array(c_names)


def GetChildren(Network, NodeName):
	c_names = PCTr.GetChildren(Network, NodeName)
	return from_c_array(c_names)
	
def from_c_array(array):
	result = []
	for element in array:
		string = string_at(element)
		if string == 'LISTEND':
			return result
		result.append(string)