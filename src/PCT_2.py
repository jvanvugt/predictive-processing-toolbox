from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *
from lib_pct_revision import *
from lib_pct_tools import *
import random

ConvertFromGenie("He")

AddNode("He","N5")

print NodeNames(NetworkName="He.dsl");#, NodeName="1")

#print GetChildren("He","Node3")

#print GetParents("He","Node2")