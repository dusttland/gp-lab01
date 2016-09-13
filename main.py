import sys
sys.path.insert(0, 'aima-python-master')

import search

import color
from game import Game
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

    [ # 5th line
        color.BLUE, color.BLUE, color.YELLOW,
        color.GREEN, color.GREEN, color.YELLOW,
    ],
    [
        color.YELLOW, color.RED, color.YELLOW,
        color.BLUE, color.RED, color.BLUE,
    ],
    [
        color.GREEN, color.RED, color.RED,
        color.GREEN, color.YELLOW, color.YELLOW,
    ],
    [
        color.GREEN, color.BLUE, color.BLUE,
        color.YELLOW, color.YELLOW, color.GREEN,
    ],
    [
        color.RED, color.BLUE, color.YELLOW,
        color.YELLOW, color.RED, color.BLUE,
    ],
]


def hexagons_from_colors_list(hexagon_colors_list):
    hexagons = []
    for hexagon_colors in hexagon_colors_list:
        hexagons.append(Hexagon(hexagon_colors))
    return hexagons


def main():
    hexagons = hexagons_from_colors_list(HEXAGON_COLORS_LIST)
    game = Game(hexagons)
    game.solve()

    # Test hexagon placement.

    # hexagon_colors = [
    #     color.YELLOW, color.RED, color.BLUE,
    #     color.BLUE, color.YELLOW, color.RED,
    # ]
    # hexagon = Hexagon(hexagon_colors)
    # game.place_hexagon(hexagon, 6)


    # Test hexagon switching.

    # game.switch_hexagons(3, 5)


    # Test hexagon rotation.

    game.hexagon(2).rotate()
    game.hexagon(2).rotate()
    game.hexagon(3).rotate()
    game.hexagon(6).rotate()
    game.hexagon(6).rotate()
    game.hexagon(13).rotate_counterclockwise()
    game.hexagon(14).rotate_counterclockwise()
    game.hexagon(12).rotate()
    game.hexagon(11).rotate()

    print("Game solved: %r" % game.is_solved())
    print("Number of valid connections: %d" % game.number_of_valid_connections())
    

main()