from SimpleProblemSolvingAgent import *
from romania_map import romania_map

def main():
    romania_problem = romaniaAgent("Arad", "Bucharest", romania_map)
    print(romania_problem.best_first_graph_search(romania_problem, 2))

    pass

if __name__ =="__main__":
    main()
