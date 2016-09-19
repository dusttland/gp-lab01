import sys
sys.path.insert(0, 'aima-python-master')

import search

from game import Game

# ______________________________________________________________________________


class GameProblem(search.Problem):

    def __init__(self, initial):
        self.initial = tuple(initial)

    def actions(self, state):
        # if state.index(0) == 0:
        #     return ["right", "down"]
        # elif state.index(0) == 1:
        #     return ["left", "right", "down"]
        #
        # ...
        

    def result(self, state, action):
        # new_state = list(state)
        # if action == "left":
        #     blank = state.index(0)
        #     tile = state[state.index(0) - 1]
        #     new_state[blank] = tile
        #     new_state[blank-1] = 0
        #     return tuple(new_state)
        # elif action == "right":
        #     blank = state.index(0)
        #
        # ...
        

    def goal_test(self, state):
        complete_list = list(state)
        game = Game.game_from_complete_list(complete_list)
        return game.is_solved()

    def h(self, node):
        """Misplaced tiles of heuristic"""
        complete_list = list(node.state)
        game = Game.game_from_complete_list(complete_list)
        return game.number_of_invalid_connections()
