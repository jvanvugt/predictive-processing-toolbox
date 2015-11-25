from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *
from lib_pct_revision import *
from lib_pct_tools import *
import random

CreateNetwork(NetworkName="He");

AddNode(NetworkName="He", NodeName="N0");

print NodeNumber(NetworkName="He.dsl");#, NodeName="0");

print "say what?"