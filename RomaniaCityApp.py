import SimpleProblemSolvingAgent

def main():
    agent = SimpleProblemSolvingAgent.SimpleProblemSolvingAgentProgram('Arad', 'Bucharest')
    print(agent.best_first_search())
    pass

if __name__ =="__main__":
    main()
