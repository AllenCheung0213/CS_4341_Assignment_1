import functools
from queue import PriorityQueue

import romania_map
from queue import *
from romania_map import romania_map


# def memoize(fn, slot=None, maxsize=32):
#     """Memoize fn: make it remember the computed value for any argument list.
#     If slot is specified, store result in that slot of first argument.
#     If slot is false, use lru_cache for caching the values."""
#     if slot:
#         def memoized_fn(obj, *args):
#             if hasattr(obj, slot):
#                 return getattr(obj, slot)
#             else:
#                 val = fn(obj, *args)
#                 setattr(obj, slot, val)
#                 return val
#     else:
#         @functools.lru_cache(maxsize=maxsize)
#         def memoized_fn(*args):
#             return fn(*args)
#
#     return memoized_fn

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
        problem = Problem('Arad', 'Bucharest')
        self.best_first_graph_search(problem)
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

    def best_first_search(self):

        graph = romania_map

        start = self.state #node
        goal = self.goal
        pq = PriorityQueue() #frontier
        pq.put((0, start)) #put initial state into priority queue

        #create a dictionary to keep track of which cities have been visited
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
        visited = {}
        for city in city_names:
            visited[city] = False

        #set the initial city for visited --> True
        visited[start] = True

        stack = []
        while pq.not_empty:
            current = pq.get()[1]
            # Displaying the path having lowest cost
            print(current, end=" ")
            # Displaying the path with the lowest cost
            if current == goal:
                break

            for neighbor in graph.find_neighbors(current):
                city = neighbor[0]
                cost = neighbor[1]
                if not visited[city]:
                    visited[city] = True
                    pq.put((cost, city))

        print(pq.get())
        print("ss")


    # def best_first_graph_search(self, problem, display=False):
    #     """Search the nodes with the lowest f scores first.
    #     You specify the function f(node) that you want to minimize; for example,
    #     if f is a heuristic estimate to the goal, then we have greedy best
    #     first search; if f is node.depth then we have breadth-first search.
    #     There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    #     values will be cached on the nodes as they are computed. So after doing
    #     a best first search you can examine the f values of the path returned."""
    #     # f = memoize(f, 'f')
    #     node = Node(problem.initial)
    #     # frontier = PriorityQueue('min', f)
    #     frontier = PriorityQueue()
    #     frontier.put(node)
    #     explored = set()
    #     while frontier:
    #         node = frontier.get()
    #         if problem.goal_test(node.state):
    #             if display:
    #                 print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
    #             return node
    #         explored.add(node.state)
    #         for child in node.expand(problem):
    #             if child.state not in explored and not any(child in item for item in frontier.queue):
    #                 frontier.put(child)
    #             elif any(child in item for item in frontier.queue):
    #                 # if f(child) < frontier[child]:
    #                 #     del frontier[child]
    #                 #     frontier.append(child)
    #                 break
    #     return None

    def astar_search(self, h=None, display=False):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or self.h, 'h')
        return self.best_first_graph_search(self, lambda n: n.path_cost + h(n), display)

