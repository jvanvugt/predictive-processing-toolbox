from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *
from Alarm_base import *



net = create_alarm_network()
print BelieveUpdating(net, TargetNodes=["Alarm", "Smoke"], EvidenceNodes=["Fire", "Tampering"], Evidences=["true", "false"])