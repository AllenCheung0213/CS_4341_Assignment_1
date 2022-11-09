import SimpleProblemSolvingAgent
from SimpleProblemSolvingAgent import SimpleProblemSolvingAgentProgram
from romania_map import romania_map

def main():
    agent = SimpleProblemSolvingAgent.SimpleProblemSolvingAgentProgram('Arad', 'Bucharest')
    print(agent.best_first_search())
    print('j')
    pass

if __name__ =="__main__":
    main()
