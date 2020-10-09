import planner


default_mode_option = -1
default_mode_domain = r"scenarios\scenario-1\KitchenDomain.pddl"
default_mode_problm = r"scenarios\scenario-1\KitchenProblem.pddl"

scenario1_domain = r"scenarios\scenario-1\KitchenDomain.pddl"
scenario1_problm = r"scenarios\scenario-1\KitchenProblem.pddl"
scenario2_domain = r"scenarios\scenario-2\KitchenDomain.pddl"
scenario2_problm = r"scenarios\scenario-2\KitchenProblem.pddl"
scenario3_domain = r"scenarios\scenario-3\KitchenDomain.pddl"
scenario3_problm = r"scenarios\scenario-3\KitchenProblem.pddl"
scenario4_domain = r"scenarios\scenario-4\KitchenDomain.pddl"
scenario4_problm = r"scenarios\scenario-4\KitchenProblem.pddl"
scenario5_domain = r"scenarios\scenario-5\KitchenDomain.pddl"
scenario5_problm = r"scenarios\scenario-5\KitchenProblem.pddl"
scenario6_domain = r"scenarios\scenario-6\KitchenDomain.pddl"
scenario6_problm = r"scenarios\scenario-6\KitchenProblem.pddl"



# ==========================================
# Main
# ==========================================
if __name__ == '__main__':
    
    # Set default option
    mode = default_mode_option
    target_domain = default_mode_domain
    target_problm = default_mode_problm

    # Get input from user
    try:
        mode = int(input("  <<Launcher Message>> Enter a number to select a scenario: "))
    except ValueError:
        print ("  <<Launcher Message>> No valid input was detected. Default option set.\n\t")

    # Act accoarding to selected options
    if(mode == 0):
        
        domainPath = input("  <<Launcher Message>> Enter the path to the domain file: ")
        problmPath = input("  <<Launcher Message>> Enter the path to the problem file: ")
        if(not path.isfile(domainPath)):
            print("  <<Launcher Message>> The domain path: <",domainPath,"> seems faulty.Check again. Terminating.\n\t")
            exit()
        if(not path.isfile(problmPath)):
            print("  <<Launcher Message>> The problem path: <",problmPath,"> seems faulty.Check again. Terminating.\n\t")
            exit()
        target_domain = domainPath
        target_problm = problmPath
        if(path.isfile(domainPath) and path.isfile(problmPath)):
            print ("  <<Launcher Message>> Scenario initiated:\n\t")
            planner.Planner.Execute_scenario(target_domain ,target_problm)
            target_domain = domainPath
            target_problm = problmPath
    elif(mode == 1):
        print ("  <<Launcher Message>> Scenario 1 initiated:\n\t")
        planner.Planner.Execute_scenario(scenario1_domain ,scenario1_problm)    
    elif(mode == 2):
        print ("  <<Launcher Message>> Scenario 2 initiated:\n\t")
        planner.Planner.Execute_scenario(scenario2_domain ,scenario2_problm)
    elif(mode == 3):
        print ("  <<Launcher Message>> Scenario 3 initiated:\n\t")
        planner.Planner.Execute_scenario(scenario3_domain ,scenario3_problm)
    elif(mode == 4):
        print ("  <<Launcher Message>> Scenario 4 initiated:\n\t")
        planner.Planner.Execute_scenario(scenario4_domain ,scenario4_problm)
    elif(mode == 5):
        print ("  <<Launcher Message>> Scenario 5 initiated:\n\t")
        planner.Planner.Execute_scenario(scenario5_domain ,scenario5_problm)
    elif(mode == 6):
        print ("  <<Launcher Message>> Scenario 6 initiated:\n\t")
        planner.Planner.Execute_scenario(scenario6_domain ,scenario6_problm)
    else:
        print ("  <<Launcher Message>> Default Scenario (Scenario 1) initiated:\n\t")
        planner.Planner.Execute_scenario(target_domain ,target_problm)

    print("  <<Launcher Message>>  Execution Terminated successfully\n")