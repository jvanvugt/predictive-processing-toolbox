from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *
from lib_pct_revision import *
from lib_pct_tools import *

def create_alarm_network():
	net = CreateNetwork("Alarm")
	
	P0=0.01
	AddNode(net,"Fire",Probabilities=[P0,1-P0])
	P0=0.02
	AddNode(net, "Tampering",Probabilities=[P0,1-P0])
	AddNode(net,"Smoke")
	AddNode(net,"Alarm")
	AddNode(net,"Leaving")
	AddNode(net,"Report")
	
	AddArc(net,"Fire","Smoke")
	AddArc(net,"Tampering","Alarm")
	AddArc(net,"Fire","Alarm")
	AddArc(net,"Alarm","Leaving")
	AddArc(net,"Leaving","Report")
	
	SetProbabilities(net,"Smoke",[0.9,0.1,0.01,0.99])
	SetProbabilities(net,"Alarm",[0.5,0.5,0.85,0.15,0.99,0.01,0.0001,0.9999])
	SetProbabilities(net,"Leaving",[0.88,0.12,0.001,0.999])
	SetProbabilities(net,"Report",[0.75,0.25,0.01,0.99])
	
	WriteNetwork(net, "Alarm")
	return net