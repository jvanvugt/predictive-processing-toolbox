from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *
from lib_pct_revision import *
from lib_pct_tools import *

CreateNetwork("Alarm");

P0=0.01;
AddNode("Alarm","Fire",Probabilities=[P0,1-P0]);
P0=0.02;
AddNode("Alarm","Tampering",Probabilities=[P0,1-P0]);
AddNode("Alarm","Smoke");
AddNode("Alarm","Alarm");
AddNode("Alarm","Leaving");
AddNode("Alarm","Report");

AddArc("Alarm","Fire","Smoke");
AddArc("Alarm","Tampering","Alarm");
AddArc("Alarm","Fire","Alarm");
AddArc("Alarm","Alarm","Leaving");
AddArc("Alarm","Leaving","Report");

SetProbabilities("Alarm","Smoke",[0.9,0.1,0.01,0.99])
SetProbabilities("Alarm","Alarm",[0.5,0.5,0.85,0.15,0.99,0.01,0.0001,0.9999])
SetProbabilities("Alarm","Leaving",[0.88,0.12,0.001,0.999])
SetProbabilities("Alarm","Report",[0.75,0.25,0.01,0.99])
