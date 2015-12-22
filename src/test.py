from pct_network import PCTNetwork
from lib_pct_inference import *
from lib_pct_revision import *

convert_from_genie("new")

net = PCTNetwork()
net.load_from_file("new.dsl")
print belief_revision(net, ["BIN_1"], ["COLOR"], [0.3719,0.1344,0.2720,0.2217])