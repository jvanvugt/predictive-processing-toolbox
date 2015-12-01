#include <iostream>
#include <sstream>
#include <iomanip>
using namespace std;

#include "../smile/smile.h"
#include <typeinfo>

extern "C" {
  
  DSL_network* CreateNetwork() {
    DSL_network* network = new DSL_network();
    return network;
  };
  
  void AddNode(DSL_network* Network, char* NodeName, char* Outcomes[], double Probabilities[], int OutcomeNumber) {
    int NewNode = Network->AddNode(DSL_CPT,NodeName);

    DSL_idArray NodeOutcomes;
    for (int i=0; i<OutcomeNumber; i++) { 
      NodeOutcomes.Add(Outcomes[i]);
    }
    Network->GetNode(NewNode)->Definition()->SetNumberOfOutcomes(NodeOutcomes);  
    NodeOutcomes.Flush();

    DSL_doubleArray NodeProbabilities;
    NodeProbabilities.SetSize(OutcomeNumber); // it has to be an array
    for (int i=0; i<OutcomeNumber; i++) {
      NodeProbabilities[i] = Probabilities[i];
    }
    Network->GetNode(NewNode)->Definition()->SetDefinition(NodeProbabilities);
  };
  
  void WriteNetwork(DSL_network* Network, char* NetworkName) {
    Network->WriteFile(NetworkName, DSL_DSL_FORMAT);
  }

  void AddValueNode(DSL_network* Network, char* NodeName) {
    Network->AddNode(DSL_MAU, NodeName);
  };

  void DeleteNode(DSL_network* Network, char* NodeName) {
    Network->DeleteNode(Network->FindNode(NodeName));
  };

  void SetOutcomes(DSL_network* Network, char* NodeName, char* Outcomes[], int OutcomeNumber) {
    int Node=Network->FindNode(NodeName);
    DSL_idArray NodeOutcomes;
    for (int i=0; i<OutcomeNumber; i++) { 
      NodeOutcomes.Add(Outcomes[i]);
    }
    Network->GetNode(Node)->Definition()->SetNumberOfOutcomes(NodeOutcomes);
        
    NodeOutcomes.Flush();
  };

  void SetProbabilities(DSL_network* Network, char* NodeName, double Probabilities[], int OutcomeNumber) {
    int Node=Network->FindNode(NodeName);
    
    DSL_doubleArray NodeProbabilities;
    NodeProbabilities.SetSize(OutcomeNumber); // it has to be an array
    for (int i=0; i<OutcomeNumber; i++) { NodeProbabilities[i] = Probabilities[i];}
    Network->GetNode(Node)->Definition()->SetDefinition(NodeProbabilities);
  };

  void AddArc(DSL_network* Network, char* StartNodeName, char* GoalNodeName){
    int StartNode=Network->FindNode(StartNodeName);
    int GoalNode=Network->FindNode(GoalNodeName);
    Network->AddArc(StartNode,GoalNode);
  };
}
