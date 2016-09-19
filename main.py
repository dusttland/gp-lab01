import sys
sys.path.insert(0, 'aima-python-master')

import search

import color
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

    # [ # 4th line
    #     color.BLUE, color.BLUE, color.RED,
    #     color.YELLOW, color.YELLOW, color.RED,
    # ],
    # [
    #     color.BLUE, color.YELLOW, color.YELLOW,
    #     color.BLUE, color.RED, color.RED,
    # ],
    # [
    #     color.BLUE, color.BLUE, color.RED,
    #     color.RED, color.YELLOW, color.YELLOW,
    # ],
    # [
    #     color.YELLOW, color.RED, color.RED,
    #     color.BLUE, color.BLUE, color.YELLOW,
    # ],

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


def main():
    game = Game.game_from_list(HEXAGON_COLORS_LIST)
    game_problem = GameProblem(game)
    solution = search.astar_search(game_problem, game_problem.h).solution()
    print(solution)
    

main()