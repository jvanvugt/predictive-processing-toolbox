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
  
  int NodeExists(char * NetworkName, char* NodeName) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName,DSL_DSL_FORMAT);
	return theNet.FindNode(NodeName);
  };
  
  int NodeNumber(char * NetworkName) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName,DSL_DSL_FORMAT);
	return theNet.GetNumberOfNodes();
  };

  char** GetOutcomes(char * NetworkName, char* NodeName) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName,DSL_DSL_FORMAT);
	int Node=theNet.FindNode(NodeName);
	DSL_idArray* Outcomes=theNet.GetNode(Node)->Definition()->GetOutcomesNames();
	int OutcomeNumber=theNet.GetNode(Node)->Definition()->GetNumberOfOutcomes();

	char **Rstr = (char**)malloc(sizeof(char *) * (OutcomeNumber+1));
	int ioutcome;
// 	DSL_node* node;
// 	
// // 	if (parentnumber!=0)
// // 		for (int i = 0; i < parentnumber+1; i++){
	for (int i = 0; i < OutcomeNumber; i++){
// 		iparent = parents[i];
// 		if (i<parentnumber)
// 		{ node = theNet.GetNode(iparent); }
		Rstr[i] = (char*)malloc(MAX_STRING + 1);
		strncpy(Rstr[i], (*Outcomes)[i], MAX_STRING);
	}
	Rstr[OutcomeNumber] = (char*)malloc(MAX_STRING + 1);
	strncpy(Rstr[OutcomeNumber], "LISTEND", MAX_STRING);  	//Note end of list for processing in python
	return Rstr; 
  };
  
  
  char** NodeNames(char * NetworkName) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName,DSL_DSL_FORMAT);
	int NodeNumber = theNet.GetNumberOfNodes();

	char **Rstr = (char**)malloc(sizeof(char *) * (NodeNumber+1));
	DSL_node* node;
	for (int i = 0; i < NodeNumber+1; i++){
		if (i<NodeNumber)
		{ node = theNet.GetNode(i); }
		Rstr[i] = (char*)malloc(MAX_STRING + 1);
		strncpy(Rstr[i], (char*)node->Info().Header().GetId(), MAX_STRING);
	}
	strncpy(Rstr[NodeNumber], "LISTEND", MAX_STRING);  	//Note end of list for processing in python
	return Rstr; 
  };

  
  char** GetParents(char * NetworkName, char* NodeName) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName,DSL_DSL_FORMAT);
	int Node=theNet.FindNode(NodeName);
	DSL_intArray parents=theNet.GetParents(Node);
	int parentnumber=parents.NumItems();

	char **Rstr = (char**)malloc(sizeof(char *) * (parentnumber+1));
	int iparent;
	DSL_node* node;
	for (int i = 0; i < parentnumber; i++){
		iparent = parents[i];
		if (i<parentnumber)
		{ node = theNet.GetNode(iparent); }
		Rstr[i] = (char*)malloc(MAX_STRING + 1);
		strncpy(Rstr[i], (char*)node->Info().Header().GetId(), MAX_STRING);
	}
	Rstr[parentnumber] = (char*)malloc(MAX_STRING + 1);
	strncpy(Rstr[parentnumber], "LISTEND", MAX_STRING);  	//Note end of list for processing in python
	return Rstr; 
  };
  

  char** GetChildren(char * NetworkName, char* NodeName) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName,DSL_DSL_FORMAT);
	int Node=theNet.FindNode(NodeName);
	DSL_intArray children=theNet.GetChildren(Node);
	int childnumber=children.NumItems();

	char **Rstr = (char**)malloc(sizeof(char *) * (childnumber+1));
	int ichild;
	DSL_node* node;
	for (int i = 0; i < childnumber; i++){
		ichild = children[i];
		if (i<childnumber)
		{ node = theNet.GetNode(ichild); }
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

