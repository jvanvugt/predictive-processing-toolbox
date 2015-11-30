from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *
from lib_pct_revision import *
from lib_pct_tools import *

ConvertFromGenie("Alarm")

Alarm = CreateNetwork("Alarm")

AddNode(Alarm, "Blackout",Probabilities=[0.002,0.998]);

AddArc(Alarm, "Blackout","Leaving");

SetProbabilities(Alarm, NodeName="Leaving", Probabilities = [0,1,0.88,0.12,0,1,0.001,0.999])


Evidences,Probs =  P(Alarm, TargetNodes = ["Report"], EvidenceNodes = [])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs

Evidences,Probs =  P(Alarm, TargetNodes = ["Report"], EvidenceNodes = ["Blackout"])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs

Evidences,Probs =  P(Alarm, TargetNodes = ["Report"], EvidenceNodes = ["Blackout","Alarm"])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs


print BeliefRevision(Alarm, HypothesisNodes=["Tampering"],PredictionNodes=["Report"], Observations=[0.3,0.7], Method = "Basinhopping")

Evidences,Probs =  P(Alarm, TargetNodes = ["Report"], EvidenceNodes = [])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs




Evidences,Probs =  P(Alarm, TargetNodes = ["Alarm"], EvidenceNodes = [])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs

Evidences,Probs =  P(Alarm, TargetNodes = ["Alarm"], EvidenceNodes = ["Smoke"])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs

Evidences,Probs =  P(Alarm, TargetNodes = ["Alarm"], EvidenceNodes = ["Fire"])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs

Evidences,Probs =  P(Alarm, TargetNodes = ["Alarm"], EvidenceNodes = ["Smoke","Fire"])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; 
print Evidences; print roundProbs


print Check_dependence(Alarm, TargetNodes=["Alarm","Smoke"], EvidenceNodes=[], Disp = True)

print Check_dependence(Alarm, TargetNodes=["Alarm","Smoke"], EvidenceNodes=["Fire"], Disp = True)

print "new"

print Check_dependence(Alarm, TargetNodes=["Tampering","Fire","Leaving"], EvidenceNodes=[], Disp = True)

print Check_dependence(Alarm, TargetNodes=["Tampering","Fire","Leaving"], EvidenceNodes=["Alarm"], Disp = True)

