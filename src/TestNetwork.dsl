net Unnamed
{
 HEADER = 
  {
   ID = Unnamed;
   NAME = "Unnamed";
  };
 CREATION = 
  {
  };
 NUMSAMPLES = 1000;
 SCREEN = 
  {
   POSITION = 
    {
     CENTER_X = 0;
     CENTER_Y = 0;
     WIDTH = 76;
     HEIGHT = 36;
    };
   COLOR = 16250597;
   SELCOLOR = 12303291;
   FONT = 1;
   FONTCOLOR = 0;
   BORDERTHICKNESS = 3;
   BORDERCOLOR = 12255232;
  };
 WINDOWPOSITION = 
  {
   CENTER_X = 0;
   CENTER_Y = 0;
   WIDTH = 0;
   HEIGHT = 0;
  };
 BKCOLOR = 16777215;
 USER_PROPERTIES = 
  {
  };
 DOCUMENTATION = 
  {
  };
 SHOWAS = 3;

 node Node_0
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_0;
     NAME = "Node_0";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = ();
   DEFINITION = 
    {
     NAMESTATES = (true, false, maybe);
     PROBABILITIES = (0.57533168, 0.05382179, 0.37084653);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0, 0);
     FAULT_NAMES = ("", "", "");
     FAULT_LABELS = ("", "", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "", "");
     STATEREPAIRINFO = ("", "", "");
     QUESTION = "";
    };
  };

 node Node_1
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_1;
     NAME = "Node_1";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = ();
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.84114685, 0.15885315);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };

 node Node_2
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_2;
     NAME = "Node_2";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = (Node_0);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.18394873, 0.81605127, 0.26499752, 0.73500248, 
     0.17135187, 0.82864813);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };

 node Node_3
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_3;
     NAME = "Node_3";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = ();
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.41562572, 0.58437428);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };

 node Node_4
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_4;
     NAME = "Node_4";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = ();
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.54616639, 0.45383361);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };

 node Node_5
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_5;
     NAME = "Node_5";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = (Node_0, Node_1, Node_2);
   DEFINITION = 
    {
     NAMESTATES = (true, false, maybe);
     PROBABILITIES = (0.28811099, 0.11153913, 0.60034988, 0.44177452, 
     0.23647879, 0.32174669, 0.46282422, 0.09789097, 0.43928481, 
     0.55594013, 0.04641644, 0.39764343, 0.02613813, 0.86804561, 
     0.10581626, 0.64961543, 0.22688357, 0.12350100, 0.88612785, 
     0.06184361, 0.05202855, 0.30023507, 0.56044966, 0.13931526, 
     0.29487927, 0.13878709, 0.56633364, 0.56380864, 0.20527773, 
     0.23091363, 0.99457887, 0.00051979, 0.00490134, 0.78223613, 
     0.12149095, 0.09627292);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0, 0);
     FAULT_NAMES = ("", "", "");
     FAULT_LABELS = ("", "", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "", "");
     STATEREPAIRINFO = ("", "", "");
     QUESTION = "";
    };
  };

 node Node_6
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_6;
     NAME = "Node_6";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = (Node_1, Node_3, Node_4);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.14261976, 0.85738024, 0.28187752, 0.71812248, 
     0.54680423, 0.45319577, 0.30905832, 0.69094168, 0.47293875, 
     0.52706125, 0.50661117, 0.49338883, 0.01485398, 0.98514602, 
     0.65279620, 0.34720380);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };

 node Node_7
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_7;
     NAME = "Node_7";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = (Node_2, Node_4, Node_5);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.92391104, 0.07608896, 0.65343720, 0.34656280, 
     0.88420558, 0.11579442, 0.45987248, 0.54012752, 0.16555579, 
     0.83444421, 0.27914387, 0.72085613, 0.87004027, 0.12995973, 
     0.28898047, 0.71101953, 0.45999539, 0.54000461, 0.86052253, 
     0.13947747, 0.02156695, 0.97843305, 0.39603276, 0.60396724);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };

 node Node_8
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_8;
     NAME = "Node_8";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = (Node_1, Node_4, Node_5);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.67071101, 0.32928899, 0.62768397, 0.37231603, 
     0.31195320, 0.68804680, 0.79311488, 0.20688512, 0.47267525, 
     0.52732475, 0.24611103, 0.75388897, 0.27838818, 0.72161182, 
     0.01951365, 0.98048635, 0.34286550, 0.65713450, 0.92488425, 
     0.07511575, 0.40002278, 0.59997722, 0.56066692, 0.43933308);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };

 node Node_9
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Node_9;
     NAME = "Node_9";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 0;
       CENTER_Y = 0;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   USER_PROPERTIES = 
    {
    };
   DOCUMENTATION = 
    {
    };
   PARENTS = (Node_0);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.77989981, 0.22010019, 0.23839692, 0.76160308, 
     0.89441586, 0.10558414);
    };
   EXTRA_DEFINITION = 
    {
     DIAGNOSIS_TYPE = AUXILIARY;
     RANKED = FALSE;
     MANDATORY = FALSE;
     SETASDEFAULT = FALSE;
     SHOWAS = 4;
     FAULT_STATES = (0, 0);
     FAULT_NAMES = ("", "");
     FAULT_LABELS = ("", "");
     DEFAULT_STATE = 0;
     DOCUMENTATION = 
      {
      };
     DOCUMENTATION = 
      {
      };
     STATECOMMENTS = ("", "");
     STATEREPAIRINFO = ("", "");
     QUESTION = "";
    };
  };
 OBSERVATION_COST = 
  {

   node Node_0
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_1
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_2
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_3
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_4
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_5
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_6
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_7
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_8
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Node_9
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };
  };
};
