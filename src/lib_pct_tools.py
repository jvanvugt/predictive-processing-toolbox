# from ctypes import *
# import numpy
from math import log
# import itertools
# PCTi=CDLL("/home/marvin/Coding/StudentAssistantship/bridepythonC/Predictive Coding Toolbox/LibPCTInference.so")
# from lib_pct_read_network import *

# DefaultNetworkName="TestNetwork";


def KL(P,Q, base=2):
	kl = 0;
	for i in range(len(P)):
		kl += P[i]* log( P[i]/Q[i] , base );
	return kl


def Ending(NetworkName):
	if NetworkName[-4:] == ".dsl":
		return NetworkName
	else:
		return NetworkName+".dsl"
	

def ConvertFromGenie(NetworkName):
	f = open(Ending(NetworkName))
	contents = f.read(); f.close()
	contents = contents.replace('\r\n', '\n')
	f = open(Ending(NetworkName), 'w')
	f.write(contents); f.close()
	
