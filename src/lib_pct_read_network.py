from ctypes import *
import numpy
from lib_pct_tools import *

PCTr=CDLL("./LibPCTReadnetwork.so")

PCTr.Loadnetwork.restype = c_void_p

PCTr.Reloadnetwork.argtypes = [c_void_p, c_char_p]
PCTr.Reloadnetwork.restype = None

PCTr.node_names.argtypes = [c_void_p]
PCTr.node_names.restype = POINTER(POINTER(c_char))

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


default_network_name = "Testnetwork"

def load_network(network, network_name=default_network_name):
	PCTr.Loadnetwork(network, ensure_extension(network_name, '.dsl'))

def reload_network(network, network_name=default_network_name):
	"""
		Reload the network from the file
	"""
	PCTr.Reloadnetwork(network, ensure_extension(network_name, '.dsl'))

def node_exists(network, node_name):
	"""
		Return True if node_name is in the network
	"""
	return PCTr.NodeExists(network, node_name)


def number_of_nodes(network):
	"""
		Return the number of nodes in the network
	"""
	return PCTr.NodeNumber(network)


def node_names(network):
	"""
		Return a list of all the names of the nodes in the network
	"""
	c_names = PCTr.node_names(network)
	return from_char_p_array(c_names)


def get_outcomes(network, node_name):
	"""
		Return the possible outcomes of the node (e.g. ["true", "false"])
	"""
	c_names = PCTr.GetOutcomes(network, node_name)
	return from_char_p_array(c_names)


def get_parents(network, node_name):
	"""
		Return a list containing the names of the parents of the node
	"""
	c_names = PCTr.GetParents(network, node_name)
	return from_char_p_array(c_names)


def get_children(network, node_name):
	"""
		Return a list containing the names of the children of the node
	"""
	c_names = PCTr.GetChildren(network, node_name)
	return from_char_p_array(c_names)
	