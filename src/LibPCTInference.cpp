#include <iostream>
#include <sstream>
#include <iomanip>
using namespace std;

#include "../smile/smile.h"
#include <typeinfo>

extern "C" {
  
  void SetAlgorithm (char* NetworkName, int AlgorithmIndex) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName);
		/*
		1 DSL_ALG_BN_LAURITZEN;
		2 DSL_ALG_BN_HENRION ;
		3 DSL_ALG_BN_PEARL;
		4 DSL_ALG_BN_LSAMPLING ;
		5 DSL_ALG_BN_SELFIMPORTANCE;
		6 DSL_ALG_BN_BACKSAMPLING;
		7 DSL_ALG_BN_AISSAMPLING;
		8 DSL_ALG_BN_EPISSAMPLING;
		9 DSL_ALG_BN_LBP ;
		10 DSL_ALG_BN_LAURITZEN_OLD;
		*/
	theNet.SetDefaultBNAlgorithm(AlgorithmIndex);
	theNet.WriteFile(NetworkName);
  };
  
  
  
  double* BelieveUpdating(char * NetworkName, int AlgorithmIndex, char * TargetNodes[], char * EvidenceNodes[], char* Evidences[]){
	DSL_network theNet;
	theNet.ReadFile(NetworkName);
	// DSL_node* node
  
	// Set Algorithm
	theNet.SetDefaultBNAlgorithm(AlgorithmIndex);
    
	// Set Evidences
	int i=0;
	while (strcmp(EvidenceNodes[i],"LISTEND")!=0)
	{
		DSL_node* node = theNet.GetNode(theNet.FindNode(EvidenceNodes[i]));
		int EvidenceId = node->Definition()->GetOutcomesNames()->FindPosition(Evidences[i]);
		node->Value()->SetEvidence(EvidenceId);
		i++;
	}
	
	//Set TargetNodes
	i=0;
	while (strcmp(TargetNodes[i],"LISTEND")!=0)
	{
		theNet.SetTarget(theNet.FindNode(TargetNodes[i]));
		i++;
	}
	
	//Update
	theNet.UpdateBeliefs();
	
	//Read target probabilities
	int NodeNumber = theNet.GetNumberOfNodes();
	
	int TotalOutcomeNumber;
	for (int i=0; i<NodeNumber; i++)
	{
		TotalOutcomeNumber+=(theNet.GetNode(i)->Definition()->GetNumberOfOutcomes())+1;
	}

	double* Rdouble = (double*)malloc(sizeof(double) * (NodeNumber+1)*(2+1)+1);

	
	DSL_Dmatrix* Values;
	i=0;
	int iout=0;
	while (strcmp(TargetNodes[i],"LISTEND")!=0)
	{
		DSL_node* node = theNet.GetNode(theNet.FindNode(TargetNodes[i]));
		Values = node->Value()->GetMatrix();
// 		cout << ((char*)node->Info().Header().GetId()) << endl;
// 		cout << "Dimensionsize = " << Values->GetSizeOfDimension(0) << endl;
		for (int j=0; j<Values->GetSizeOfDimension(0);j++)
		{
			DSL_intArray Coords;
			Coords.Add(j);
// 			cout << Values->Subscript(Coords)<< endl;
			Rdouble[iout]=Values->Subscript(Coords);iout++;
		}
		Rdouble[iout]=-2;iout++;
		i++;
	}
	if (i!=0)
	{
		Rdouble[iout]=-3;iout++;
		return  Rdouble;
	}
	else
	{
		for (int i=0; i<NodeNumber; i++)
		{
			DSL_node* node = theNet.GetNode(i);
			Values = node->Value()->GetMatrix();
// 			cout << ((char*)node->Info().Header().GetId()) << endl;
// 			cout << "Dimensionsize = " << Values->GetSizeOfDimension(0) << endl;
			for (int j=0; j<Values->GetSizeOfDimension(0);j++)
			{
				DSL_intArray Coords;
				Coords.Add(j);
// 				cout << Values->Subscript(Coords)<< endl;
				Rdouble[iout]=Values->Subscript(Coords);iout++;
			}
			Rdouble[iout]=-2;iout++;
		}
		Rdouble[iout]=-3;iout++;
		return  Rdouble;
	}
  };
}
