#include <iostream>
#include <sstream>
#include <iomanip>
using namespace std;

#include "../smile/smile.h"
#include <typeinfo>

extern "C" {
  
  void CreateNetwork(char* NetworkName) {
    DSL_network theNet;
//     theNet.WriteFile(NetworkName);
//     theNet.WriteFile(strcat(NetworkName, ".dsl"));
    theNet.WriteFile(NetworkName,DSL_DSL_FORMAT);
    cout << NetworkName << endl;
  };
  
//   void WriteNetwork(void* NetworkPointer, char* NetworkName) {
//     DSL_network* theNet = (DSL_network*)NetworkPointer;
//     theNet->WriteFile(strcat(NetworkName, ".dsl"),DSL_XDSL_FORMAT);
//   };
  
  void AddNode(char * NetworkName, char* NodeName, char * Outcomes[], double Probabilities[], int OutcomeNumber) {
    DSL_network theNet;
    //strcat(NetworkName, ".dsl");
    theNet.ReadFile(NetworkName);
    int NewNode = theNet.AddNode(DSL_CPT,NodeName);

    DSL_idArray NodeOutcomes;
    for (int i=0; i<OutcomeNumber; i++) { NodeOutcomes.Add(Outcomes[i]);}
    theNet.GetNode(NewNode)->Definition()->SetNumberOfOutcomes(NodeOutcomes);  
    NodeOutcomes.Flush();

    DSL_doubleArray NodeProbabilities;
    NodeProbabilities.SetSize(OutcomeNumber); // it has to be an array
    for (int i=0; i<OutcomeNumber; i++) { NodeProbabilities[i] = Probabilities[i];}
    theNet.GetNode(NewNode)->Definition()->SetDefinition(NodeProbabilities);
    
    theNet.WriteFile(NetworkName);
  };

  void AddValueNode(char * NetworkName, char* NodeName) {
    DSL_network theNet;
    theNet.ReadFile(NetworkName);
    int NewNode = theNet.AddNode(DSL_MAU,NodeName);

//     DSL_idArray NodeOutcomes;
//     for (int i=0; i<OutcomeNumber; i++) { NodeOutcomes.Add(Outcomes[i]);}
//     theNet.GetNode(NewNode)->Definition()->SetNumberOfOutcomes(NodeOutcomes);  
//     NodeOutcomes.Flush();
// 
//     DSL_doubleArray NodeProbabilities;
//     NodeProbabilities.SetSize(OutcomeNumber); // it has to be an array
//     for (int i=0; i<OutcomeNumber; i++) { NodeProbabilities[i] = Probabilities[i];}
//     theNet.GetNode(NewNode)->Definition()->SetDefinition(NodeProbabilities);
    
    theNet.WriteFile(NetworkName);
  };

  void DeleteNode(char * NetworkName, char* NodeName) {
    DSL_network theNet;
    //strcat(NetworkName, ".dsl");
    theNet.ReadFile(NetworkName);
    
    theNet.DeleteNode(theNet.FindNode(NodeName));
        
    theNet.WriteFile(NetworkName);
  };

  void SetOutcomes(char * NetworkName, char* NodeName, char * Outcomes[], int OutcomeNumber) {
    DSL_network theNet;
    theNet.ReadFile(NetworkName);
    int Node=theNet.FindNode(NodeName);
    DSL_idArray NodeOutcomes;
    for (int i=0; i<OutcomeNumber; i++) { NodeOutcomes.Add(Outcomes[i]);}
    theNet.GetNode(Node)->Definition()->SetNumberOfOutcomes(NodeOutcomes);
        
    NodeOutcomes.Flush();
    
    theNet.WriteFile(NetworkName);
  };

  void SetProbabilities(char * NetworkName, char* NodeName, double Probabilities[], int OutcomeNumber) {
    DSL_network theNet;
    theNet.ReadFile(NetworkName);
    int Node=theNet.FindNode(NodeName);
    
    DSL_doubleArray NodeProbabilities;
    NodeProbabilities.SetSize(OutcomeNumber); // it has to be an array
    for (int i=0; i<OutcomeNumber; i++) { NodeProbabilities[i] = Probabilities[i];}
    theNet.GetNode(Node)->Definition()->SetDefinition(NodeProbabilities);
    
    theNet.WriteFile(NetworkName);
  };

  void AddArc(char* NetworkName, char* StartNodeName, char* GoalNodeName){
    DSL_network theNet;
    theNet.ReadFile(NetworkName);
    int StartNode=theNet.FindNode(StartNodeName);
    int GoalNode=theNet.FindNode(GoalNodeName);
    
    theNet.AddArc(StartNode,GoalNode);
    
    //DSL_sysCoordinates theCoordinates (*theNet.GetNode(GoalNode)->Definition());
    //theCoordinates.UncheckedValue() = 0.4;
    /*theCoordinates.Next();
    theCoordinates.UncheckedValue() = 0.4;
    theCoordinates.Next();
    theCoordinates.UncheckedValue() = 0.2;
    theCoordinates.Next();
    theCoordinates.UncheckedValue() = 0.1;
    theCoordinates.Next();
    theCoordinates.UncheckedValue() = 0.3;
    theCoordinates.Next();
    theCoordinates.UncheckedValue() = 0.6; */


    theNet.WriteFile(NetworkName);
  };
}
