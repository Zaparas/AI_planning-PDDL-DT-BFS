### AI - Planning 
## Keypoints - Keypoints:
  1. Knowledge Base
  2. PDDL
  3. PDDL parser
  4. Descision Trees
  5. Heuristic Algorithm
  6. Breadth First Search (BFS)


## CUDOS TO 
# PDDL Parser [![Build Status](https://travis-ci.org/pucrs-automated-planning/pddl-parser.svg?branch=master)](https://travis-ci.org/pucrs-automated-planning/pddl-parser) [![DOI](https://zenodo.org/badge/42985356.svg)](https://zenodo.org/badge/latestdoi/42985356)
**Planning in Python**



# python version:
  - 3.7

  ## Files
- [action.py](action.py) with an Action class
- [launcher.py](launcher.py) a central execution handler
- [PDDL.py](PDDL.py) with a PDDL parser
- [planner.py](planner.py) with a planner
- [scenarios](scenarios/) folder with PDDL domains:
  - [scenario1](scenarios/scenario1) simple test case scenario.
  - [scenario2](scenarios/scenario2) scenario 1  + 1 command too late to be used vis BFS.
  - [scenario3](scenarios/scenario3) scenario 2  + 1 command early enough to be exploited.
  - [scenario4](scenarios/scenario4) scenario 1  + different starting conditions.
  - [scenario5](scenarios/scenario5) scenario 4  + 1 command late compared to command cook, but still used.
  - [scenario6](scenarios/scenario6) scenario 5  + 1 command earlier compared to command cook, but still used.

  ## Tests
  - python PDDL.py
  - python planner.py
  - python launcher.py
  
  ## Scenario Relative Commands:

    # Scenario 1:
  - python PDDL.py    scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-1\KitchenProblem.pddl
  - python planner.py scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-1\KitchenProblem.pddl
    # Scenario 2:
  - python PDDL.py    scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-2\KitchenProblem.pddl
  - python planner.py scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-2\KitchenProblem.pddl
  	# Scenario 3:
  - python PDDL.py    scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-3\KitchenProblem.pddl
  - python planner.py scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-3\KitchenProblem.pddl

    # Launcher can launch all scenarios
  - python launcher.py

  ## Execution Examples:

  # Scenario 1 Parser example: 

  - Used Command at master directory:
  python PDDL.py scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-1\KitchenProblem.pddl

  - Output:
  -------------------------------------------------------------------------------
        ----------------------------
      ['define',
      ['domain', 'dinner'],
      [':requirements', ':strips'],
      [':predicates', ['clean'], ['dinner'], ['quiet'], ['present'], ['garbage']],
      [':action', 'cook', ':precondition', ['clean'], ':effect', ['dinner']],
      [':action', 'wrap', ':precondition', ['quiet'], ':effect', ['present']],
      [':action',
        'carry',
        ':precondition',
        ['garbage'],
        ':effect',
        ['and', ['not', ['garbage']], ['not', ['clean']]]],
      [':action',
        'dolly',
        ':precondition',
        ['garbage'],
        ':effect',
        ['and', ['not', ['garbage']], ['not', ['quiet']]]]]
      ----------------------------
      ['define',
      ['problem', 'pb1'],
      [':domain', 'dinner'],
      [':init', ['garbage'], ['clean'], ['quiet']],
      [':goal', ['and', ['dinner'], ['present'], ['not', ['garbage']]]]]
      ----------------------------
      Domain name: dinner
      action: cook
        parameters: []
        positive_preconditions: [['clean']]
        negative_preconditions: []
        add_effects: [['dinner']]
        del_effects: []

      action: wrap
        parameters: []
        positive_preconditions: [['quiet']]
        negative_preconditions: []
        add_effects: [['present']]
        del_effects: []

      action: carry
        parameters: []
        positive_preconditions: [['garbage']]
        negative_preconditions: []
        add_effects: []
        del_effects: [['garbage'], ['clean']]

      action: dolly
        parameters: []
        positive_preconditions: [['garbage']]
        negative_preconditions: []
        add_effects: []
        del_effects: [['garbage'], ['quiet']]

      ----------------------------
      Problem name: pb1
      Objects: {}
      State: [['garbage'], ['clean'], ['quiet']]
      Positive goals: [['dinner'], ['present']]
      Negative goals: [['garbage']]


  # Scenario 1 Planner example:

  - Used Command at master directory:
  python planner.py scenarios\Scenario-1\KitchenDomain.pddl scenarios\Scenario-1\KitchenProblem.pddl

  - Output:
  ----------------------------------------------------------------------------------------

      Time: 0.003996372222900391s
    plan:
    action: cook
      parameters: []
      positive_preconditions: [['clean']]
      negative_preconditions: []
      add_effects: [['dinner']]
      del_effects: []

    action: wrap
      parameters: []
      positive_preconditions: [['quiet']]
      negative_preconditions: []
      add_effects: [['present']]
      del_effects: []

    action: carry
      parameters: []
      positive_preconditions: [['garbage']]
      negative_preconditions: []
      add_effects: []
      del_effects: [['garbage'], ['clean']]

# Scenario 1 via launcher example:

  - Used Command at master directory:
  python launcher.py

  - Output:
  ------------------------------------------------------
    <<Launcher Message>> Enter a number to select a scenario: 

    - Given input of 1 
    
    <<Launcher Message>> Scenario 1 initiated:
      
    Time: 0.0050275325775146484s
    plan: {step count: 3 }
    step:  1 
      action: cook
      parameters: []
      positive_preconditions: [['clean']]
      negative_preconditions: []
      add_effects: [['dinner']]
      del_effects: []

    step:  2 
      action: wrap
      parameters: []
      positive_preconditions: [['quiet']]
      negative_preconditions: []
      add_effects: [['present']]
      del_effects: []

    step:  3 
      action: carry
      parameters: []
      positive_preconditions: [['garbage']]
      negative_preconditions: []
      add_effects: []
      del_effects: [['garbage'], ['clean']]

      <<Launcher Message>>  Execution Termianted successfully

