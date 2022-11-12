from queue import *
from search import *
from utils import *


class SimpleProblemSolvingAgentProgram:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, initial_state=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state, percept):
        raise NotImplementedError

    def formulate_goal(self, state):
        raise NotImplementedError

    def formulate_problem(self, state, goal):
        raise NotImplementedError

    def search(self, problem):
        raise NotImplementedError

    def astar_search(self, h=None, display=False):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or self.h, 'h')
        return self.best_first_graph_search(self, lambda n: n.path_cost + h(n), display)


class romaniaAgent(SimpleProblemSolvingAgentProgram):
    def __init__(self, initial, goal):
        self.graph = romania_map
        self.state = initial
        self.goal = goal
        self.seq = []

    def __call__(self):
        romania_problem = GraphProblem(self.state, self.goal, self.graph)
        final_path = best_first_graph_search(romania_problem, lambda n: n.state).solution()
        final_path.insert(0, self.state)
        print("Best first graph search path: ", final_path)
        print("Best first graph search cost:", best_first_graph_search(romania_problem, lambda n: n.state).path_cost)


    def update_state(self, state, percept):
        return percept

    def formulate_goal(self, state):
        goal = self.goal
        return goal

    def formulate_problem(self, state, goal):
        problem = state
        return problem

    def best_first_graph_search(problem, f, display=False):
        f = memoize(f, 'f')
        node = Node(problem.initial)
        frontier = PriorityQueue('min', f)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    if f(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)
        return None

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or np.inf)
