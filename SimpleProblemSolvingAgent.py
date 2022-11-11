import queue
from queue import *
from romania_map import romania_map
from utils import *
from graph import *


class SimpleProblemSolvingAgentProgram:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, initial_state=None, goal=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.goal = goal
        self.state = initial_state
        self.seq = []

    def __call__(self):
        print('hi')
        # """[Figure 3.1] Formulate a goal and problem, then
        # search for a sequence of actions to solve it."""
        # if not self.seq:
        #     if (self.goal!=None and self.state!=None):
        #         goal = self.goal
        #         self.seq = self.search(self)
        #         if not self.seq:
        #             return None
        #     return self.seq.pop(0)
        # #return

    def search(self):
        raise NotImplementedError

    # def best_first_search(self):
    #     start = self.state
    #     target = self.goal
    #     graph = createGraph()

    #     city_names = ["Arad",
    #                   "Bucharest",
    #                   "Craiova",
    #                   "Dobreta",
    #                   "Eforie",
    #                   "Fagaras",
    #                   "Giurgiu",
    #                   "Hirsova",
    #                   "Iasi",
    #                   "Lugoj",
    #                   "Mehadia",
    #                   "Neamt",
    #                   "Oradea",
    #                   "Pitesti",
    #                   "Rimnicu_Vilcea",
    #                   "Sibiu",
    #                   "Timisoara",
    #                   "Urziceni",
    #                   "Vaslui",
    #                   "Zerind"]

    #     visited = {}
    #     for city in city_names:
    #         visited[city] = False

    #     pq = queue.PriorityQueue()
    #     pq.put((0, start))
    #     visited[start] = True

    #     while pq.not_empty:
    #         current = pq.get()[1]
    #         # Displaying the path having lowest cost
    #         #print(current, end=" ")
    #         if current == target:
    #             break

    #         for city, cost in graph[current]:
    #             if not visited[city]:
    #                 visited[city] = True
    #                 pq.put((cost, city))
    #     print(pq.queue)

    def best_first_graph_search(self, f, display=False):
        """Search nodes with minimum f(node) first."""
        node = self
        frontier = PriorityQueue('min', f)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            if self.goal_test(node.state):
                return node
            explored.add(node.state)
            pnode = node.parent
            while pnode:
                if pnode.state == node.state and pnode.path_cost <= node.path_cost:
                    break
                pnode = pnode.parent
            else:
                for child in node.expand(self):
                    if child.state not in explored and child not in frontier:
                        frontier.append(child)
                    elif child in frontier:
                        incumbent = frontier[child]
                        if f(child) < f(incumbent):
                            del frontier[incumbent]
                            frontier.append(child)
        return None

    # Implement the astar search algorithm
    def astar_search(self, problem, h=None):
        """A* search is best-first graph search with f(n) = g(n)+h(n)."""
        h = memoize(h or problem.h, 'h')
        return self.best_first_graph_search(lambda n: n.path_cost + h(n), display=problem.display)
    

    


# def main():
#     agent = SimpleProblemSolvingAgent('Arad', 'Bucharest')
#     # agent.SimpleProblemSolvingAgentProgram.best_first_search()
#     print(agent.state)
#     # print(bfs)
#     print('j')
#
# if __name__ =="__main__":
#     main()
