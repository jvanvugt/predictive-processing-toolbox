#include <iostream>
#include <sstream>
#include <iomanip>
#include <string.h>
#include <malloc.h>
#define MAX_STRING 80 
using namespace std;

#include "../smile/smile.h"
#include <typeinfo>

extern "C" {
	
  DSL_network* LoadNetwork(DSL_network* network, char* name) {
	network->ReadFile(name, DSL_DSL_FORMAT);
  }
  
  void ReloadNetwork(DSL_network* Network, char* name) {
	  Network->ReadFile(name, DSL_DSL_FORMAT);
  }
  
  bool NodeExists(DSL_network* Network, char* NodeName) {
	return Network->FindNode(NodeName) != DSL_OUT_OF_RANGE;
  };
  
  int NodeNumber(DSL_network* Network) {
	return Network->GetNumberOfNodes();
  };

  char** GetOutcomes(DSL_network* Network, char* NodeName) {
	int Node=Network->FindNode(NodeName);
	DSL_idArray* Outcomes=Network->GetNode(Node)->Definition()->GetOutcomesNames();
	int OutcomeNumber=Network->GetNode(Node)->Definition()->GetNumberOfOutcomes();

	char **Rstr = (char**)malloc(sizeof(char *) * (OutcomeNumber+1));
	for (int i = 0; i < OutcomeNumber; i++){
		Rstr[i] = (char*)malloc(MAX_STRING + 1);
		strncpy(Rstr[i], (*Outcomes)[i], MAX_STRING);
	}
	Rstr[OutcomeNumber] = (char*)malloc(MAX_STRING + 1);
	strncpy(Rstr[OutcomeNumber], "LISTEND", MAX_STRING);  	//Note end of list for processing in python
	return Rstr; 
  };
  
  
  char** NodeNames(DSL_network* Network) {
	int NodeNumber = Network->GetNumberOfNodes();

	char **Rstr = (char**)malloc(sizeof(char *) * (NodeNumber+1));
	for (int i = 0; i < NodeNumber; i++){
		DSL_node* node = Network->GetNode(i); 
		Rstr[i] = (char*)malloc(MAX_STRING + 1);
		strncpy(Rstr[i], (char*)node->Info().Header().GetId(), MAX_STRING);
	}
	strncpy(Rstr[NodeNumber], "LISTEND", MAX_STRING);  	//Note end of list for processing in python
	return Rstr; 
  };

  
  char** GetParents(DSL_network* Network, char* NodeName) {
	int Node=Network->FindNode(NodeName);
	DSL_intArray parents=Network->GetParents(Node);
	int parentnumber=parents.NumItems();

	char **Rstr = (char**)malloc(sizeof(char *) * (parentnumber+1));
	for (int i = 0; i < parentnumber; i++){
		DSL_node* node = Network->GetNode(parents[i]);
		Rstr[i] = (char*)malloc(MAX_STRING + 1);
		strncpy(Rstr[i], (char*)node->Info().Header().GetId(), MAX_STRING);
	}
	Rstr[parentnumber] = (char*)malloc(MAX_STRING + 1);
	strncpy(Rstr[parentnumber], "LISTEND", MAX_STRING);  	//Note end of list for processing in python
	return Rstr; 
  };
  

  char** GetChildren(DSL_network* Network, char* NodeName) {
	int Node=Network->FindNode(NodeName);
	DSL_intArray children=Network->GetChildren(Node);
	int childnumber=children.NumItems();

	char **Rstr = (char**)malloc(sizeof(char *) * (childnumber+1));
	for (int i = 0; i < childnumber; i++){
		DSL_node* node = Network->GetNode(children[i]);
		Rstr[i] = (char*)malloc(MAX_STRING + 1);
		strncpy(Rstr[i], (char*)node->Info().Header().GetId(), MAX_STRING);
	}
	Rstr[childnumber] = (char*)malloc(MAX_STRING + 1);
	strncpy(Rstr[childnumber], "LISTEND", MAX_STRING);  	//Note end of list for processing in python
	return Rstr; 

  };
  
  
}
/* is there an arc between x and y
 * what outcomes does a node have
 * what Probabilities does a node have
 * return ID to a particular name of a node
 */

