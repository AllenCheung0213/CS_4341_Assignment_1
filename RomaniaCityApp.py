import SimpleProblemSolvingAgent
import search
from SimpleProblemSolvingAgent import *
from search import romania_map


def start():
    print("Please read the Romania map. The map is stored in romania_map file.")
    print("Please enter any two (different) cities from the map.")
    city1 = input("City 1: ")
    city2 = input("City 2: ")
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
        # RomaniaAgent is a SimpleProblemSolvingAgent
        call = romaniaAgent(city1, city2)
        call()


if __name__ == "__main__":
    main()
