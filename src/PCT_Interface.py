from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *
from lib_pct_revision import *
from lib_pct_tools import *
import random

from matplotlib.pyplot import show
from time import time

CreateNetwork();

N = 10 # Number of nodes 
p = 0.3 # sparseness of the network


for i in range(N):
	NodeName="Node_"+str(i);
	P0 = random.random();
	AddNode(NodeName=NodeName, Probabilities=[P0,1-P0]);
	if i==5 or i==0:
		SetOutcomes(NodeName="Node_"+str(i),Outcomes=["true","false","maybe"]);
		SetProbabilities(NodeName="Node_"+str(i), Probabilities=[P0/2,P0/2,1-P0])

for i in range(N):
	for j in range(i+1,N):
		if (random.random()<p) and (j>1) and (i<N-1):
			AddArc(StartNode="Node_"+str(i), GoalNode="Node_"+str(j))

for i in range(N):
	Parents=GetParents(NodeName="Node_"+str(i));
	dims=1;
	for Par in Parents:
		dims *= len(GetOutcomes(NodeName=Par));
	Prob=[];
	for ip in range(dims):
		o = len(GetOutcomes(NodeName="Node_"+str(i)));
		totprob=0;
		for io in range(o-1):
			P0 = random.random();
			Prob.append((1-totprob)*P0);
			totprob+=(1-totprob)*P0;
		Prob.append(1-totprob);
	SetProbabilities(NodeName="Node_"+str(i), Probabilities=Prob);


# print BelieveUpdating(TargetNodes = ["Node_5"], EvidenceNodes=["Node_2","Node_4","Node_8"],Evidences=["true","true","false"])

# print P1(TargetNode="Node_8", EvidenceNodes=["Node_5","Node_3"])
# P11("Node_3","Node_5")

# Outcomes, Probs = P(TargetNodes=["Node_8","Node_6","Node_2"], EvidenceNodes=["Node_3","Node_5"])

# print KL(Probs[1],Probs[2])

#DeleteNode(NodeName="Node_2");

#print GetParents(NodeName="Node_1");
#print GetChildren(NodeName="Node_8");
## BeliefRevision(HypothesisNodes=["Node_0","Node_1"], PredictionNodes=["Node_8"]);
#P(TargetNodes=["Node_1","Node_5"], EvidenceNodes=[]);

#t0=time()
#print BeliefRevision(HypothesisNodes=["Node_0"],PredictionNodes=["Node_5"], Observations=[0.3,0.5,0.2],Method=0)
#print time()-t0

#t0=time()
#print BeliefRevision(HypothesisNodes=["Node_0"],PredictionNodes=["Node_5"], Observations=[0.3,0.5,0.2],Method=1)
#print time()-t0

#print Check_dependence(TargetNodes=["Node_0","Node_1","Node_5","Node_9"], EvidenceNodes=["Node_2","Node_3","Node_3"], Disp = True)
#print Check_dependence(TargetNodes=["Node_0","Node_1","Node_5","Node_9"], EvidenceNodes=[], Disp = True)

#t0=time()
#print BeliefRevision(HypothesisNodes=["Node_0"],PredictionNodes=["Node_5"], Observations=[0.3,0.5,0.2],Method=2, Searchgrid=3)
#print time()-t0

#t0=time()
#print AddObservation(HypothesisNodes=["Node_0","Node_1"],PredictionNodes=["Node_5"], ObservableNodes=["Node_3","Node_2"], PredObservations=[0.98,0.01,0.01], FullOutput=True)
#print time()-t0

#t0=time()
#print Intervention(HypothesisNodes=["Node_0","Node_1"],PredictionNodes=["Node_5"], InterventionNodes=["Node_3","Node_2"], PredObservations=[0.3,0.5,0.2])
#print time()-t0

#t0=time()
#print ModelRevision(HypothesisNodes=["Node_0","Node_1"],PredictionNodes=["Node_5"], RevisionNodes=["Node_2"], Observations=[0.3,0.5,0.2],Method=0, Searchgrid=3)
#print time()-t0

#t0=time()
#print ModelRevision(HypothesisNodes=["Node_0","Node_1"],PredictionNodes=["Node_5"], RevisionNodes=["Node_2"], Observations=[0.3,0.5,0.2],Method=1, Searchgrid=3)
#print time()-t0

#t0=time()
#print ModelRevision(HypothesisNodes=["Node_0","Node_1"],PredictionNodes=["Node_5"], RevisionNodes=["Node_2","Node_3"], Observations=[0.3,0.5,0.2],Method=2, Searchgrid=3)
#print time()-t0

Evidences,Probs = P(TargetNodes=["Node_5"], EvidenceNodes=[])
roundProbs = [[ '%.2f' % prob for prob in probdist] for probdist in Probs]; #rounds entries of Probs to two digits
print ["Node_0","Node_2"]; print Evidences; print roundProbs

show()