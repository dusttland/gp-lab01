import unittest

import color
from game import Game
from hexagon import Hexagon

# ______________________________________________________________________________


class HexagonTest(unittest.TestCase):

    def setUp(self):
        self.hexagon = Hexagon(['r', 'g', 'g', 'y', 'r', 'y'])

    def test_color(self):
        self.assertEqual('g', self.hexagon.color(2))
        self.assertEqual('y', self.hexagon.color(3))

    def test_as_list(self):
        self.assertEqual(
            ['r', 'g', 'g', 'y', 'r', 'y'],
            self.hexagon.as_list()
        )

    def test_as_tuple(self):
        self.assertEqual(
            ('r', 'g', 'g', 'y', 'r', 'y'),
            self.hexagon.as_tuple()
        )

    def test_rotate(self):
        self.hexagon.rotate(1)
        self.assertEqual(
            ['y', 'r', 'g', 'g', 'y', 'r'], 
            self.hexagon.as_list()
        )

    def test_rotate_counterclockwise(self):
        self.hexagon.rotate_counterclockwise(2)
        self.assertEqual(
            ['g', 'y', 'r', 'y', 'r', 'g'], 
            self.hexagon.as_list()
        )

# ______________________________________________________________________________


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game_15 = Game.from_list(HEXAGON_COLORS_LIST_15)
        self.game_10 = Game.from_list(HEXAGON_COLORS_LIST_10)
        self.game_solved = Game.from_tuple(HEXAGON_COLORS_TUPLE_SOLVED)

    def test_as_tuple(self):
        self.assertEqual(HEXAGON_COLORS_TUPLE_15, self.game_15.as_tuple())

    def test_hexagon(self):
        hexagon = Hexagon(HEXAGON_COLORS_LIST_15[3])
        self.assertEqual(hexagon, self.game_15.hexagon(3))

    def test_number_of_hexagons(self):
        self.assertEqual(15, self.game_15.number_of_hexagons())
        self.assertEqual(10, self.game_10.number_of_hexagons())

    def test_is_solved(self):
        self.assertTrue(self.game_solved.is_solved())

    def test_number_of_connections(self):
        self.assertEqual(30, self.game_15.number_of_connections())
        self.assertEqual(18, self.game_10.number_of_connections())

    def test_depth(self):
        self.assertEqual(5, self.game_15.depth())
        self.assertEqual(4, self.game_10.depth())

    def test_connections(self):
        self.assertEqual(CONNECTIONS_15, self.game_15.connections())
        self.assertEqual(CONNECTIONS_10, self.game_10.connections())

    def test_colors_in_connection(self):
        connection = [
            [0, Hexagon.BOTTOM_LEFT],
            [1, Hexagon.TOP_RIGHT],
        ]
        colors = color.RED, color.RED
        colors_in_connection = self.game_15.colors_in_connection(connection)
        self.assertEqual(colors, colors_in_connection)

    def test_is_valid_connection(self):
        connection1 = [
            [0, Hexagon.BOTTOM_LEFT],
            [1, Hexagon.TOP_RIGHT],
        ]
        connection2 = [
            [0, Hexagon.BOTTOM_RIGHT],
            [2, Hexagon.TOP_LEFT],
        ]
        self.assertTrue(self.game_15.is_valid_connection(connection1))
        self.assertFalse(self.game_15.is_valid_connection(connection2))

    def test_number_of_valid_connections(self):
        self.assertEqual(6, self.game_15.number_of_valid_connections())

    def test_connections_of_hexagon(self):
        hexagon_connections = [
            [
                [0, Hexagon.BOTTOM_RIGHT],
                [2, Hexagon.TOP_LEFT],
            ],
            [
                [1, Hexagon.MIDDLE_RIGHT],
                [2, Hexagon.MIDDLE_LEFT],
            ],
            [
                [2, Hexagon.BOTTOM_LEFT],
                [4, Hexagon.TOP_RIGHT],
            ],
            [
                [2, Hexagon.BOTTOM_RIGHT],
                [5, Hexagon.TOP_LEFT],
            ],
        ]
        self.assertEqual(
            hexagon_connections, 
            self.game_15.connections_for_hexagon(2)
        )

    def test_place_hexagon(self):
        hexagon = Hexagon(['r', 'g', 'g', 'y', 'r', 'y'])
        self.game_15.place_hexagon(hexagon, 5)
        self.assertEqual(hexagon, self.game_15.hexagon(5))

    def test_switch_hexagons(self):
        hexagon1 = self.game_15.hexagon(8)
        hexagon2 = self.game_15.hexagon(14)
        self.game_15.switch_hexagons(8, 14)
        self.assertEqual(hexagon1, self.game_15.hexagon(14))
        self.assertEqual(hexagon2, self.game_15.hexagon(8))

# ______________________________________________________________________________    


HEXAGON_COLORS_LIST_15 = [
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

HEXAGON_COLORS_LIST_10 = [
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
]

HEXAGON_COLORS_TUPLE_15 = (
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

HEXAGON_COLORS_TUPLE_SOLVED = (
    ('y', 'g', 'g', 'b', 'y', 'b'), 
    ('b', 'b', 'r', 'r', 'y', 'y'), 
    ('b', 'g', 'y', 'y', 'b', 'g'), 
    ('r', 'y', 'y', 'r', 'b', 'b'), 
    ('y', 'b', 'b', 'r', 'y', 'r'), 
    ('y', 'b', 'r', 'r', 'b', 'y'), 
    ('r', 'y', 'b', 'y', 'r', 'b'), 
    ('r', 'r', 'b', 'b', 'y', 'y'), 
    ('r', 'g', 'b', 'g', 'r', 'b'), 
    ('g', 'y', 'r', 'y', 'g', 'r')
)

CONNECTIONS_10 = [
    [
        [0, 3], 
        [1, 0]
    ], 
    [
        [0, 2],
        [2, 5]
    ], 
    [
        [1, 1],
        [2, 4]
    ], 
    [
        [1, 3],
        [3, 0]
    ], 
    [
        [1, 2],
        [4, 5]
    ], 
    [
        [3, 1],
        [4, 4]
    ], 
    [
        [2, 3],
        [4, 0]
    ], 
    [
        [2, 2],
        [5, 5]
    ], 
    [
        [4, 1],
        [5, 4]
    ], 
    [
        [3, 3],
        [6, 0]
    ], 
    [
        [3, 2],
        [7, 5]
    ], 
    [
        [6, 1],
        [7, 4]
    ], 
    [
        [4, 3],
        [7, 0]
    ], 
    [
        [4, 2],
        [8, 5]
    ], 
    [
        [7, 1],
        [8, 4]
    ], 
    [
        [5, 3],
        [8, 0]
    ], 
    [
        [5, 2],
        [9, 5]
    ], 
    [
        [8, 1],
        [9, 4]
    ]
]

CONNECTIONS_15 = [    
    [
        [0, 3], [1, 0]
    ], 
    [
        [0, 2], [2, 5]
    ], 
    [
        [1, 1], [2, 4]
    ], 
    [
        [1, 3], [3, 0]
    ], 
    [
        [1, 2], [4, 5]
    ], 
    [
        [3, 1], [4, 4]
    ], 
    [
        [2, 3], [4, 0]
    ], 
    [
        [2, 2], [5, 5]
    ], 
    [
        [4, 1], [5, 4]
    ], 
    [
        [3, 3], [6, 0]
    ], 
    [
        [3, 2], [7, 5]
    ], 
    [
        [6, 1], [7, 4]
    ], 
    [
        [4, 3], [7, 0]
    ], 
    [
        [4, 2], [8, 5]
    ], 
    [
        [7, 1], [8, 4]
    ], 
    [
        [5, 3], [8, 0]
    ], 
    [
        [5, 2], [9, 5]
    ], 
    [
        [8, 1], [9, 4]
    ], 
    [
        [6, 3], [10, 0]
    ], 
    [
        [6, 2], [11, 5]
    ], 
    [
        [10, 1], [11, 4]
    ], 
    [
        [7, 3], [11, 0]
    ], 
    [
        [7, 2], [12, 5]
    ], 
    [
        [11, 1], [12, 4]
    ], 
    [
        [8, 3], [12, 0]
    ], 
    [
        [8, 2], [13, 5]
    ], 
    [
        [12, 1], [13, 4]
    ], 
    [
        [9, 3], [13, 0]
    ], 
    [
        [9, 2], [14, 5]
    ], 
    [
        [13, 1], [14, 4]
    ]
]

unittest.main()