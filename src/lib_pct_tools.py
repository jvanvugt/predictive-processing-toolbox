from math import log
from ctypes import string_at

def KL(P,Q, base=2):
	kl = 0;
	for i in range(len(P)):
		kl += P[i]* log( P[i]/Q[i] , base );
	return kl


def ensure_extension(filename, extension):
	"""
		Make sure the filename has the specified extension
		The extension should include the '.'
	"""
	if filename[-len(extension):] == extension:
		return filename
	else:
		return filename + extension
	
def convert_from_genie(network_name):
	f = open(ensure_extension(network_name, '.dsl'))
	contents = f.read(); f.close()
	contents = contents.replace('\r\n', '\n')
	f = open(ensure_extension(network_name, '.dsl'), 'w')
	f.write(contents); f.close()
	
def from_char_p_array(array):
	"""
		Convert a c list of char pointers with last element
		'LISTEND' to a python list
	"""
	result = []
	for element in array:
		string = string_at(element)
		if string == 'LISTEND':
			return result
		result.append(string)