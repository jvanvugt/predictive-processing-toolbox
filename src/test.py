from pct_network import PCTNetwork
from lib_pct_inference import *

net = PCTNetwork()
net.load_from_file("Alarm")
# print BelieveUpdating(net.network, 0, ["Alarm", "Leaving"], ["Fire", "Smoke"], ["true", "true"])
# P11(net.network, "Alarm", "Smoke")
# print len(P1(net.network, "Alarm", ["Smoke", "Fire"]))
print P(net.network, ["Alarm"], ["Smoke", "Fire"])