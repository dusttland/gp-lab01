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

    def __init__(self, hexagons):
        number_of_hexagons = len(hexagons)
        if not Game.valid_number_of_objects_in_triangle(number_of_hexagons):
            raise ValueError("Invalid number of hexagons.")
        self._hexagons = hexagons

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

    def game_from_complete_list(complete_list):
        """Static factory method to get game instance from complete list."""    
        hexagons = Game.get_hexagons_from_complete_list(complete_list)
        return Game(hexagons)


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
        """Returns all the connections between hexagons in this game.

        Example of connections' structure (numbers are the ids of hexagons):
            
                | 0 |
              | 1 | 2 |

            connections = [
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

                ...
            ]

        The function divides all hexagons into groups of three where all three 
        of them connect. Then it adds all the connections between those three 
        hexagons to the list that is returned."""
        connections = []
        depth = self.depth()

        for current_depth in range(2, depth + 1):
            upper_hexagon_idxs = Game.hexagon_idxs_at_depth(current_depth - 1)
            bottom_hexagon_idxs = Game.hexagon_idxs_at_depth(current_depth)

            for list_idx, upper_hexagon_idx in enumerate(upper_hexagon_idxs):
                top_hexagon_idx = upper_hexagon_idx
                bottom_left_hexagon_idx = bottom_hexagon_idxs[list_idx]
                bottom_right_hexagon_idx = bottom_hexagon_idxs[list_idx + 1]

                connection1 = [
                    [top_hexagon_idx, Hexagon.BOTTOM_LEFT],
                    [bottom_left_hexagon_idx, Hexagon.TOP_RIGHT],
                ]
                connection2 = [
                    [top_hexagon_idx, Hexagon.BOTTOM_RIGHT],
                    [bottom_right_hexagon_idx, Hexagon.TOP_LEFT],
                ]
                connection3 = [
                    [bottom_left_hexagon_idx, Hexagon.MIDDLE_RIGHT],
                    [bottom_right_hexagon_idx, Hexagon.MIDDLE_LEFT],
                ]

                connections.append(connection1)
                connections.append(connection2)
                connections.append(connection3)

        return connections

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

    def number_of_invalid_connections(self):
        """Returns the number of invalid connections."""
        return self.number_of_connections() - self.number_of_valid_connections()

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

    def as_complete_list(self):
        """Returns the game as one complete list containing colors of all 
        hexagons."""
        complete_list = []
        for hexagon in self.hexagos:
            complete_list.append(hexagon.as_list())
        return complete_list

    def solve(self):
        """Solves the game according to current layout."""

        # TODO
        
        print("Solving is not implemented yet...")


    # Utility

    def get_hexagons_from_complete_list(colors_list):
        hexagons = []
        for colors in colors_list:
            hexagons.append(Hexagon(colors))
        return hexagons

    def valid_number_of_objects_in_triangle(number):
        depth = 0
        number_of_objects_in_depth = 0
        while number_of_objects_in_depth < number:
            depth += 1
            number_of_objects_in_depth += depth
            if number_of_objects_in_depth == number:
                return True
        return False

    def hexagon_idxs_at_depth(depth):
        hexagon_idxs = []
        idx = 0
        for current_depth in range(1, depth + 1):
            idx += current_depth - 1
            if current_depth == depth:
                number_of_hexagons_in_depth = current_depth
                hexagon_idxs = Game.sequential_number_list(
                    idx, idx + number_of_hexagons_in_depth)
        return hexagon_idxs

    def sequential_number_list(from_number, to_number):
        number_list = []
        for number in range(from_number, to_number):
            number_list.append(number)
        return number_list