import sys
sys.path.insert(0, 'aima-python-master')

from search import Problem

from game import Game

# ______________________________________________________________________________


class GameProblem(Problem):

    def __init__(self, game):
        self.initial = game.as_tuple()

    def actions(self, state):
        game = Game.game_from_tuple(state)
        return GameProblem.get_all_possible_moves_as_list(game)
        

    def result(self, state, action):
        game = Game.game_from_tuple(state)

        before = game.connection_heuristic()

        if action[0] == "switch":
            game.switch_hexagons(action[1], action[2])
        elif action[0] == "rotate":
            game.hexagon(action[1]).rotate(action[2])
        else:
            print("Failed to choose action.")

        after = game.connection_heuristic()

        print("%d -> %d" % (before, after))

        return game.as_tuple()

    def goal_test(self, state):
        game = Game.game_from_tuple(state)
        return game.is_solved()

    def h(self, node):
        """Heuristic: the less invalid connections, the better."""
        game = Game.game_from_tuple(node.state)
        return game.connection_heuristic()


    # Static methods

    def get_all_possible_moves_as_list(game):
        moves_list = []
        moves_list.extend(GameProblem.get_all_rotate_moves(game))
        moves_list.extend(GameProblem.get_all_switch_moves(game))
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
        """Rotate every rotatation move."""
        rotate_moves = []
        number_of_hexagons = game.number_of_hexagons()
        for i in range(0, number_of_hexagons):
            for j in range(1, 6):
                rotate_moves.append(["rotate", i, j])
        return rotate_moves
