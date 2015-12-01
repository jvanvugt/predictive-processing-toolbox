from lib_pct_read_network import *
from lib_pct_build_network import *
from lib_pct_inference import *

class PCTNetwork(object):
	def __init__(self):
		self.network = create_network()
		
	def load_from_file(self, filename):
		"""
			Load the network from the specified filename
		"""
		load_network(self.network, filename)
	
	def write_to_file(self, filename):
		"""
			Save the network to a file
		"""
		write_network(self.network, filename)
	
	def reload(self, filename):
		"""
			Reload the network from the file
			Call this function when the network file has been modified
		"""
		reload_network(self.network, filename)
	
	def has_node(self, node_name):
		"""
			Return True if node_name is in the network
		"""
		return node_exists(self.network, node_name)
	
	def number_of_nodes(self):
		"""
			Return the number of nodes in the network
		"""
		return number_of_nodes(self.network)
	
	def get_nodes(self):
		"""
			A list of all the names of the nodes in the network
		"""
		return node_names(self.network)
	
	def get_node_outcomes(self, node_name):
		"""
			Return the possible outcomes of the node 
			(e.g. ["true", "false"])
		"""
		if node_name not in self.get_nodes():
			raise ValueError("node %s not in network".format(node_name))
		else:
			return get_outcomes(self.network, node_name)
		
	def get_node_parents(self, node_name):
		"""
			Return a list containing the names of the parents of the node
		"""
		if node_name not in self.get_nodes():
			raise ValueError("node %s not in network".format(node_name))
		else:
			return get_parents(self.network, node_name)
			
	def get_node_children(self, node_name):
		"""
			Return a list containing the names of the children of the node
		"""
		if node_name not in self.get_nodes():
			raise ValueError("node %s not in network".format(node_name))
		else:
			return get_children(self.network, node_name)
			
	def add_node(self, node_name, outcomes=['true', 'false'], probabilities=[0.5, 0.5]):
		"""
			Add a node to the network
		"""
		add_node(self.network, node_name, outcomes, probabilities)
		
	def add_value_node(self, node_name):
		"""
			Add a value node to the network
		"""
		add_value_node(node_name)
		
	def delete_node(self, node_name):
		"""
			Delete the node from the network
		"""
		if node_name not in self.get_nodes():
			raise ValueError("node %s not in network".format(node_name))
		else:
			delete_node(self.network, node_name)
	
	def set_outcomes(self, node_name, outcomes):
		"""
			Set the outcomes of a node
		"""
		if node_name not in self.get_nodes():
			raise ValueError("node %s not in network".format(node_name))
		else:
			set_outcomes(self.network, node_name, outcomes)
			
	def set_probabilities(self, node_name, probabilities):
		"""
			Set the probabilities of a node
		"""
		if node_name not in self.get_nodes():
			raise ValueError("node %s not in network".format(node_name))
		else:
			set_probabilities(self.network, node_name, probabilities)
	
	def add_arc(self, start_node, goal_node):
		"""
			Add an arc from start_node to goal_node
		"""
		if start_node not in self.get_nodes():
			raise ValueError("node %s not in network".format(start_node))
		if goal_node not in self.get_nodes():
			raise ValueError("node %s not in network".format(goal_node))
		else:
			add_arc(self.network, start_node, goal_node)
	