
from hexagon import Hexagon

# ______________________________________________________________________________


class Game:

    """Instance of the game.

               | 0 |
             | 1 | 2 |
           | 3 | 4 | 5 |
         | 6 | 7 | 8 | 9 |
       |10 |11 |12 |13 |14 |

    """

    def __init__(self, hexagon_color_lists):
        number_of_hexagons = len(hexagon_color_lists)
        if not Game.valid_number_of_objects_in_triangle(number_of_hexagons):
            raise ValueError("Invalid number of hexagons.")

        self._hexagons = []
        for colors in hexagon_color_lists:
            self._hexagons.append(Hexagon(colors))

    def __str__(self):
        string = ""
        depth = 0
        number_of_objects_in_depth = 0

        for idx, hexagon in enumerate(self._hexagons):
            if idx >= number_of_objects_in_depth:
                depth += 1
                number_of_objects_in_depth += depth
                string += "\n"
            string += "%s" % hexagon

        return string[1:]


    # Queries

    def hexagon(self, index):
        """Returns the hexagon at the specific index."""
        return self._hexagons[index]

    def number_of_hexagons(self):
        """Returns the number of hexagons in the game."""
        return len(self._hexagons)

    def is_solved(self):
        """Returns true if game is solved."""
        connections = self.connections()
        for connection in connections:       
            if not self.is_valid_connection(connection):
                return False
        return True

    def number_of_connections(self):
        """Returns the total number of connections for the given game."""
        connections = 0
        for objects_in_depth_minus_one in range(0, self.depth()):
            connections += objects_in_depth_minus_one * 3
        return connections

    def depth(self):
        depth = 0
        number_of_objects_in_depth = 0
        while number_of_objects_in_depth < self.number_of_hexagons():
            depth += 1
            number_of_objects_in_depth += depth
            if number_of_objects_in_depth == self.number_of_hexagons():
                return depth
        return None

    def connections(self):
        """Returns all the connections between hexagons in THIS game."""
        number_of_connections = self.number_of_connections()
        return Game.CONNECTIONS[:number_of_connections]

    def colors_in_connection(self, connection):
        """Returns the colors siding the given connection."""
        color1 = self.hexagon(connection[0][0]).color(connection[0][1])
        color2 = self.hexagon(connection[1][0]).color(connection[1][1])
        return color1, color2

    def is_valid_connection(self, connection):
        color1, color2 = self.colors_in_connection(connection)
        if color1 == color2:
            return True
        return False

    def number_of_valid_connections(self):
        """Returns the number of valid connections for the given game."""
        connections = self.connections()
        number_of_valid_connections = 0
        for connection in connections:
            if self.is_valid_connection(connection):
                number_of_valid_connections += 1
        return number_of_valid_connections

    def valid_connections(self):
        """Returns all valid connections as a list."""
        connections = self.connections()
        valid_connections = []
        for connection in connections:
            if self.is_valid_connection(connection):
                valid_connections.append(connection)
        return valid_connections
        

    # Commands

    def place_hexagon(self, hexagon, hexagon_index):
        """Places a new hexagon to the given location. If a hexagon exists
        in the indexed position, it will be replaced by the new one."""
        self._hexagons[hexagon_index] = hexagon

    def switch_hexagons(self, hexagon_index1, hexagon_index2):
        """Switch hexagons' positions with each other. Inputs are hexagon 
        indexes."""
        temp_hexagon = self._hexagons[hexagon_index1]
        self._hexagons[hexagon_index1] = self._hexagons[hexagon_index2]
        self._hexagons[hexagon_index2] = temp_hexagon

    def solve(self):
        """Solves the game according to current layout."""

        # TODO
        
        print("Solving is not implemented yet...")


    # Utility

    def valid_number_of_objects_in_triangle(number):
        depth = 0
        number_of_objects_in_depth = 0
        while number_of_objects_in_depth < number:
            depth += 1
            number_of_objects_in_depth += depth
            if number_of_objects_in_depth == number:
                return True
        return False


    # Connections should be got mathematically

    CONNECTIONS = [
        [
            [0, Hexagon.BOTTOM_LEFT],
            [1, Hexagon.TOP_RIGHT],
        ],
        [
            [0, Hexagon.BOTTOM_RIGHT],
            [2, Hexagon.TOP_LEFT],
        ],
        [
            [1, Hexagon.MIDDLE_RIGHT],
            [2, Hexagon.MIDDLE_LEFT],
        ],


        [
            [1, Hexagon.BOTTOM_LEFT],
            [3, Hexagon.TOP_RIGHT],
        ],
        [
            [1, Hexagon.BOTTOM_RIGHT],
            [4, Hexagon.TOP_LEFT],
        ],
        [
            [3, Hexagon.MIDDLE_RIGHT],
            [4, Hexagon.MIDDLE_LEFT],
        ],

        [
            [2, Hexagon.BOTTOM_LEFT],
            [4, Hexagon.TOP_RIGHT],
        ],
        [
            [2, Hexagon.BOTTOM_RIGHT],
            [5, Hexagon.TOP_LEFT],
        ],
        [
            [4, Hexagon.MIDDLE_RIGHT],
            [5, Hexagon.MIDDLE_LEFT],
        ],


        [
            [3, Hexagon.BOTTOM_LEFT],
            [6, Hexagon.TOP_RIGHT],
        ],
        [
            [3, Hexagon.BOTTOM_RIGHT],
            [7, Hexagon.TOP_LEFT],
        ],
        [
            [6, Hexagon.MIDDLE_RIGHT],
            [7, Hexagon.MIDDLE_LEFT],
        ],

        [
            [4, Hexagon.BOTTOM_LEFT],
            [7, Hexagon.TOP_RIGHT],
        ],
        [
            [4, Hexagon.BOTTOM_RIGHT],
            [8, Hexagon.TOP_LEFT],
        ],
        [
            [7, Hexagon.MIDDLE_RIGHT],
            [8, Hexagon.MIDDLE_LEFT],
        ],

        [
            [5, Hexagon.BOTTOM_LEFT],
            [8, Hexagon.TOP_RIGHT],
        ],
        [
            [5, Hexagon.BOTTOM_RIGHT],
            [9, Hexagon.TOP_LEFT],
        ],
        [
            [8, Hexagon.MIDDLE_RIGHT],
            [9, Hexagon.MIDDLE_LEFT],
        ],


        [
            [6, Hexagon.BOTTOM_LEFT],
            [10, Hexagon.TOP_RIGHT],
        ],
        [
            [6, Hexagon.BOTTOM_RIGHT],
            [11, Hexagon.TOP_LEFT],
        ],
        [
            [10, Hexagon.MIDDLE_RIGHT],
            [11, Hexagon.MIDDLE_LEFT],
        ],

        [
            [7, Hexagon.BOTTOM_LEFT],
            [11, Hexagon.TOP_RIGHT],
        ],
        [
            [7, Hexagon.BOTTOM_RIGHT],
            [12, Hexagon.TOP_LEFT],
        ],
        [
            [11, Hexagon.MIDDLE_RIGHT],
            [12, Hexagon.MIDDLE_LEFT],
        ],

        [
            [8, Hexagon.BOTTOM_LEFT],
            [12, Hexagon.TOP_RIGHT],
        ],
        [
            [8, Hexagon.BOTTOM_RIGHT],
            [13, Hexagon.TOP_LEFT],
        ],
        [
            [12, Hexagon.MIDDLE_RIGHT],
            [13, Hexagon.MIDDLE_LEFT],
        ],

        [
            [9, Hexagon.BOTTOM_LEFT],
            [13, Hexagon.TOP_RIGHT],
        ],
        [
            [9, Hexagon.BOTTOM_RIGHT],
            [14, Hexagon.TOP_LEFT],
        ],
        [
            [13, Hexagon.MIDDLE_RIGHT],
            [14, Hexagon.MIDDLE_LEFT],
        ],
    ]