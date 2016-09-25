# ______________________________________________________________________________


class Hexagon:

    """Class for one hexagon instance."""

    TOP_RIGHT = 0
    MIDDLE_RIGHT = 1
    BOTTOM_RIGHT = 2
    BOTTOM_LEFT = 3
    MIDDLE_LEFT = 4
    TOP_LEFT = 5
    

    def __init__(self, colors):
        if len(colors) == 6:
            self._colors = tuple(colors)
        else:
            raise ValueError("Not a valid hexagon.")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._colors == other._colors
        return False

    def __str__(self):
        return "%s" % str(self._colors)


    # Queries

    def color(self, index):
        """Returns the color on a specified side."""
        return self._colors[index]

    def as_list(self):
        """Returns hexagon as list containing its colors."""
        return list(self._colors)

    def as_tuple(self):
        """Returns hexagon as a tuple."""
        return self._colors


    # Commands

    def rotate(self, step):
        """Rotate clockwise"""
        step = -step % 6
        self._colors = self._colors[step:] + self._colors[:step]

    def rotate_counterclockwise(self, step):
        """Rotate counterclockwise"""
        step = step % 6
        self._colors = self._colors[step:] + self._colors[:step]