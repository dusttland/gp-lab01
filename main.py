import sys
sys.path.insert(0, 'aima-python-master')

import search
import time

import color
from empty_game_problem import EmptyGameProblem
from game import Game
from game_problem import GameProblem
from hexagon import Hexagon

# ______________________________________________________________________________


# Hexagons provided in the example that is in the PDF file.

HEXAGON_COLORS_LIST = [
    [ # 1st line
        color.RED, color.GREEN, color.YELLOW,
        color.RED, color.YELLOW, color.GREEN,
    ],

    [ # 2nd line
        color.RED, color.YELLOW, color.BLUE,
        color.YELLOW, color.RED, color.BLUE,
    ],
    [
        color.BLUE, color.GREEN, color.YELLOW,
        color.YELLOW, color.BLUE, color.GREEN,
    ],

    [ # 3rd line
        color.GREEN, color.GREEN, color.BLUE,
        color.YELLOW, color.BLUE, color.YELLOW,
    ],
    [
        color.YELLOW, color.BLUE, color.BLUE,
        color.RED, color.YELLOW, color.RED,
    ],
    [
        color.GREEN, color.BLUE, color.GREEN,
        color.RED, color.BLUE, color.RED,
    ],

    [ # 4th line
        color.BLUE, color.BLUE, color.RED,
        color.YELLOW, color.YELLOW, color.RED,
    ],
    [
        color.BLUE, color.YELLOW, color.YELLOW,
        color.BLUE, color.RED, color.RED,
    ],
    [
        color.BLUE, color.BLUE, color.RED,
        color.RED, color.YELLOW, color.YELLOW,
    ],
    [
        color.YELLOW, color.RED, color.RED,
        color.BLUE, color.BLUE, color.YELLOW,
    ],

    # [ # 5th line
    #     color.BLUE, color.BLUE, color.YELLOW,
    #     color.GREEN, color.GREEN, color.YELLOW,
    # ],
    # [
    #     color.YELLOW, color.RED, color.YELLOW,
    #     color.BLUE, color.RED, color.BLUE,
    # ],
    # [
    #     color.GREEN, color.RED, color.RED,
    #     color.GREEN, color.YELLOW, color.YELLOW,
    # ],
    # [
    #     color.GREEN, color.BLUE, color.BLUE,
    #     color.YELLOW, color.YELLOW, color.GREEN,
    # ],
    # [
    #     color.RED, color.BLUE, color.YELLOW,
    #     color.YELLOW, color.RED, color.BLUE,
    # ],
]

def get_hexagons(colors_list):
    hexagons = []
    for colors in colors_list:
        hexagons.append(Hexagon(colors))
    return hexagons

def main():
    hexagons = get_hexagons(HEXAGON_COLORS_LIST)
    empty_game_problem = EmptyGameProblem(hexagons)
    start = time.time()
    state = search.hill_climbing(empty_game_problem)
    game = Game.from_tuple(state)
    game_problem = GameProblem(game)
    node = search.astar_search(game_problem, game_problem.h)
    end = time.time()
    print(node.state)
    print("Duration: %f" % (end - start))
    

main()