import sys
sys.path.insert(0, 'aima-python-master')

from search import Problem

from game import Game

# ______________________________________________________________________________


class GameProblem(Problem):

    def __init__(self, initial):
        self.initial = tuple_it(initial)

    def actions(self, state):
        game = Game.game_from_complete_list(list_it(state))
        return GameProblem.get_all_possible_moves_as_list(game)
        

    def result(self, state, action):
        game = Game.game_from_complete_list(list_it(state))

        if action[0] == "switch":
            game.switch_hexagons(action[1], action[2])
        elif action[0] == "rotate":
            game.hexagon(action[1]).rotate(1)
        else:
            print("Failed to choose action.")

        return tuple_it(game.as_complete_list())

    def goal_test(self, state):
        complete_list = list_it(state)
        game = Game.game_from_complete_list(complete_list)
        return game.is_solved()

    def h(self, node):
        """Heuristic: the less invalid connections, the better."""
        complete_list = list_it(node.state)
        game = Game.game_from_complete_list(complete_list)
        return game.number_of_invalid_connections()


    # Static methods

    def get_all_possible_moves_as_list(game):
        moves_list = []
        moves_list.extend(GameProblem.get_all_switch_moves(game))
        moves_list.extend(GameProblem.get_all_rotate_moves(game))
        return moves_list

    def get_all_switch_moves(game):
        """Get all possible hexagon pairs without doubling."""
        switch_moves = []
        number_of_hexagons = game.number_of_hexagons()
        for i in range(0, number_of_hexagons):
            for j in range(i, number_of_hexagons):
                if i != j:
                    switch_moves.append(["switch", i, j])
        return switch_moves

    def get_all_rotate_moves(game):
        """Rotate every hexagon once."""
        rotate_moves = []
        number_of_hexagons = game.number_of_hexagons()
        for i in range(0, number_of_hexagons):
            rotate_moves.append(["rotate", i])
        return rotate_moves



def tuple_it(nested_list):
    return tuple([tuple(l) for l in nested_list])

def list_it(nested_tuple):
    return list(map(list_it, nested_tuple)) if isinstance(nested_tuple, (list, tuple)) else nested_tuple
