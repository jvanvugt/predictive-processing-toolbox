from lib_pct_build_network import *
from lib_pct_read_network import *
from lib_pct_inference import *

NN=CreateNetwork();

# WriteNetwork(NN);

AddNode(NodeName="Name1", Probabilities=[0.2,0.8])
AddNode(Outcomes=["yippie","ya","yey"], NodeName="Party", Probabilities=[0.1,0.4,0.5])

SetProbabilities(Probabilities=[0.2,0.2,0.6], NodeName="Party");
#SetOutcomes(NodeName="Party",Outcomes=["1","2","3"]);    #did not work!!

AddArc(StartNode="Name1",GoalNode="Party")

SetProbabilities(Probabilities=[0.2,0.2,0.6,0.3,0.2,0.5], NodeName="Party");

AddNode(NodeName="Hell",Probabilities=[0.2,0.8])

AddArc(StartNode="Party",GoalNode="Hell")

# GetBelieves(NodeName="Name1", NodeEvidence="true");

##print "Nodes: ", NodeNames();


#print "Parents of Party: ", GetParents(NodeName="Party")

##print "Children of Party: ", GetChildren(NodeName="Party")

##AddArc(StartNode="Name1",GoalNode="Hell");

##print "Parents of Hell: ", GetParents(NodeName="Hell")


#print PossibleAlgorithms()

#SetAlgorithm(Algorithm=0);
## SetAlgorithm(Algorithm='aissampling');

#print "Before update"
#GetBelieves(NodeName="Party");

#Update();

#print "After update"
#GetBelieves(NodeName="Party");

#SetEvidence(NodeName="Name1",NodeEvidence="false");

#print "Before update"
#GetBelieves(NodeName="Party");

#Update();

#print "After update"
#GetBelieves(NodeName="Party");
