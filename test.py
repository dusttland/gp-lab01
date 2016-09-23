import unittest

import color
from game import Game
from hexagon import Hexagon

class HexagonTest(unittest.TestCase):

	def setUp(self):
		self.hexagon = Hexagon(['r', 'g', 'g', 'y', 'r', 'y'])

	def test_color(self):
		self.assertEquals('g', self.hexagon.color(2))
		self.assertEquals('y', self.hexagon.color(3))

	def test_as_list(self):
		self.assertEquals(['r', 'g', 'g', 'y', 'r', 'y'], self.hexagon.as_list())

	def test_as_tuple(self):
		self.assertEquals(('r', 'g', 'g', 'y', 'r', 'y'), self.hexagon.as_tuple())

	def test_rotate(self):
		self.hexagon.rotate(1)
		self.assertEquals(['y', 'r', 'g', 'g', 'y', 'r'], self.hexagon.as_list())

	def test_rotate_counterclockwise(self):
		self.hexagon.rotate_counterclockwise(2)
		self.assertEquals(['g', 'y', 'r', 'y', 'r', 'g'], self.hexagon.as_list())



class GameTest(unittest.TestCase):

	def setUp(self):
		self.game = Game.from_list(HEXAGON_COLORS_LIST)

	def test_as_tuple(self):
		self.assertEquals(HEXAGON_COLORS_TUPLE, self.game.as_tuple())



		


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

HEXAGON_COLORS_TUPLE = (
    ( # 1st line
        color.RED, color.GREEN, color.YELLOW,
        color.RED, color.YELLOW, color.GREEN,
    ),

    ( # 2nd line
        color.RED, color.YELLOW, color.BLUE,
        color.YELLOW, color.RED, color.BLUE,
    ),
    (
        color.BLUE, color.GREEN, color.YELLOW,
        color.YELLOW, color.BLUE, color.GREEN,
    ),

    ( # 3rd line
        color.GREEN, color.GREEN, color.BLUE,
        color.YELLOW, color.BLUE, color.YELLOW,
    ),
    (
        color.YELLOW, color.BLUE, color.BLUE,
        color.RED, color.YELLOW, color.RED,
    ),
    (
        color.GREEN, color.BLUE, color.GREEN,
        color.RED, color.BLUE, color.RED,
    ),

    ( # 4th line
        color.BLUE, color.BLUE, color.RED,
        color.YELLOW, color.YELLOW, color.RED,
    ),
    (
        color.BLUE, color.YELLOW, color.YELLOW,
        color.BLUE, color.RED, color.RED,
    ),
    (
        color.BLUE, color.BLUE, color.RED,
        color.RED, color.YELLOW, color.YELLOW,
    ),
    (
        color.YELLOW, color.RED, color.RED,
        color.BLUE, color.BLUE, color.YELLOW,
    ),

    ( # 5th line
        color.BLUE, color.BLUE, color.YELLOW,
        color.GREEN, color.GREEN, color.YELLOW,
    ),
    (
        color.YELLOW, color.RED, color.YELLOW,
        color.BLUE, color.RED, color.BLUE,
    ),
    (
        color.GREEN, color.RED, color.RED,
        color.GREEN, color.YELLOW, color.YELLOW,
    ),
    (
        color.GREEN, color.BLUE, color.BLUE,
        color.YELLOW, color.YELLOW, color.GREEN,
    ),
    (
        color.RED, color.BLUE, color.YELLOW,
        color.YELLOW, color.RED, color.BLUE,
    ),
)

unittest.main()