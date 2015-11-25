#include <malloc.h>
#include <string.h>
#define MAX_STRING 80
  
char** NodeNames(char * NetworkName) {
	DSL_network theNet;
	theNet.ReadFile(NetworkName);
	int NodeNumber = theNet.GetNumberOfNodes();
	
	// allocate mem for an array containing pointers to strings
	// needs NodeNumber times the size of a pointer to (char *) bytes
	char **Rstr = malloc(sizeof(char *) * NodeNumber);
	
	for (int i = 0; i < NodeNumber; i++){
		DSL_node *node = theNet.GetNode(i);
		// allocate mem for an array of characters for each node
		Rstr[i] = malloc(MAX_STRING + 1);
		// don't copy the pointers; copy the contents of the strings!
		strncpy(Rstr[i], (char*)node->Info().Header().GetId(), MAX_STRING);
	}
	return Rstr;
};
