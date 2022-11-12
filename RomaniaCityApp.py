from SimpleProblemSolvingAgent import *


def start():
    print("Please enter any two (different) cities from the map.")
    city1 = input("City 1: ")
    city2 = input("City 2: ")
    print("")
    return city1, city2


def main():
    city1, city2 = start()

    city_names = ["Arad",
                  "Bucharest",
                  "Craiova",
                  "Dobreta",
                  "Eforie",
                  "Fagaras",
                  "Giurgiu",
                  "Hirsova",
                  "Iasi",
                  "Lugoj",
                  "Mehadia",
                  "Neamt",
                  "Oradea",
                  "Pitesti",
                  "Rimnicu",
                  "Sibiu",
                  "Timisoara",
                  "Urziceni",
                  "Vaslui",
                  "Zerind"]
    if (city1 == city2) or (city1 not in city_names) or (city2 not in city_names):
        print("Invalid cities, please try again.")
        main()

    else:
        problem = GraphProblem(city1, city2)
        call = SimpleProblemSolvingAgent(problem)
        call()
        print("Would you like to find the optimal path between any two cities again? (yes/no)")
        again_question = input()
        if again_question.lower() == "yes":
            print("")
            main()
        else:
            print("")
            print("Thank You for Using Our App!")


if __name__ == "__main__":
    print("Please read the Romania map. The map is stored in romania_map file.")
    print("")
    main()
