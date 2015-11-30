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

 node Fire
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Fire;
     NAME = "Fire";
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
     PROBABILITIES = (0.01000000, 0.99000000);
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

 node Tampering
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Tampering;
     NAME = "Tampering";
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
     PROBABILITIES = (0.02000000, 0.98000000);
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

 node Smoke
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Smoke;
     NAME = "Smoke";
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
   PARENTS = (Fire);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.90000000, 0.10000000, 0.01000000, 0.99000000);
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

 node Alarm
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Alarm;
     NAME = "Alarm";
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
   PARENTS = (Tampering, Fire);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.50000000, 0.50000000, 0.85000000, 0.15000000, 
     0.99000000, 0.01000000, 0.00010000, 0.99990000);
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

 node Leaving
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Leaving;
     NAME = "Leaving";
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
   PARENTS = (Alarm);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.88000000, 0.12000000, 0.00100000, 0.99900000);
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

 node Report
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Report;
     NAME = "Report";
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
   PARENTS = (Leaving);
   DEFINITION = 
    {
     NAMESTATES = (true, false);
     PROBABILITIES = (0.75000000, 0.25000000, 0.01000000, 0.99000000);
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

   node Fire
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Tampering
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Smoke
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Alarm
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Leaving
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };

   node Report
    {
     PARENTS = ();
     COSTS = (0.00000000);
    };
  };
};
