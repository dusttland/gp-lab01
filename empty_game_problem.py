import sys
sys.path.insert(0, 'aima-python-master')

from search import Problem

from game import Game

# ______________________________________________________________________________


class EmptyGameProblem(Problem):

    def __init__(self, hexagons):
        self.hexagons = hexagons
        game = Game.empty(len(hexagons))        
        self.initial = game.as_tuple()

    def actions(self, state):
        game = Game.from_tuple(state)
        return self.get_all_moves(game)

    def result(self, state, action):
        game = Game.from_tuple(state)

        if action[0] == "place":
            hexagon_index = action[1]
            hexagon = self.hexagons[hexagon_index]
            game.place_hexagon(hexagon, action[2])
        elif action[0] == "rotate":
            game.hexagon(action[1]).rotate(action[2])
        else:
            print("Failed to choose action.")

        return game.as_tuple()

    def goal_test(self, state):
        return Game.from_tuple(state).is_solved()

    def value(self, state):
        return Game.from_tuple(state).value()

    def h(self, node):
        """Heuristic: the less invalid connections, the better."""
        return Game.from_tuple(node.state).heuristic()


    # Static methods

    def get_all_moves(self, game):
        moves_list = []
        moves_list.extend(self.get_all_rotate_moves(game))
        moves_list.extend(self.get_all_placement_moves(game))
        return moves_list

    def get_all_placement_moves(self, game):
        moves_list = []
        number_of_hexagons = game.number_of_hexagons()
        available_hexagon_indexes = self.get_available_hexagon_indexes(game)
        for index in available_hexagon_indexes:
            for j in range(0, number_of_hexagons):
                if game.hexagon(j) == None:
                    moves_list.append(["place", index, j])
        return moves_list

    def get_all_rotate_moves(self, game):
        rotate_moves = []
        number_of_hexagons = game.number_of_hexagons()
        for i in range(0, number_of_hexagons):
            if game.hexagon(i) != None:
                for j in range(1, 6):
                    rotate_moves.append(["rotate", i, j])
        return rotate_moves

    def get_available_hexagon_indexes(self, game):
        available_hexagon_indexes = []
        used_hexagons = game.hexagons()
        for index, hexagon in enumerate(self.hexagons):
            if hexagon not in used_hexagons:
                available_hexagon_indexes.append(index)
        return available_hexagon_indexes