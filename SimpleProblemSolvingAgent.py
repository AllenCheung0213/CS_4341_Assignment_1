import queue
from utils import *
from romania_map import *

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
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        if not self.seq:
            if (self.goal!=None and self.state!=None):
                goal = self.goal
                self.seq = self.search(self)
                if not self.seq:
                    return None
            return self.seq.pop(0)
        #return

    def search(self):
        raise NotImplementedError

    graph = [[] for i in romania_map.locations.size]

    def best_first_search(start, target, n):
        visited = [False] * n
        pq = PriorityQueue()
        pq.put((0, start))
        visited[start] = True

        while not pq.empty():
            current = pq.get()[1]
            # Displaying the path having lowest cost
            print(current, end=" ")
            if current == target:
                break

            for city, cost in graph[current]:
                if not visited[city]:
                    visited[city] = True
                    pq.put((cost, city))
        print()

    def astar_search(self, h=None, display=False):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or self.h, 'h')
        return self.best_first_graph_search(self, lambda n: n.path_cost + h(n), display)

