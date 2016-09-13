
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
            self.colors = colors
        else:
            raise ValueError("Not a valid hexagon.")

    def __str__(self):
        return "%s" % self.colors


    # Queries

    def color(self, index):
        """Returns the color on a specified side."""
        return self.colors[index]


    # Commands

    def rotate(self):
        """Rotate clockwise."""
        old_sixth_color = self.colors[5]
        for i in reversed(range(1, 6)):
            self.colors[i] = self.colors[i-1]
        self.colors[0] = old_sixth_color

    def rotate_counterclockwise(self):
        """Rotate counterclockwise."""
        old_first_color = self.colors[0]
        for i in range(0, 5):
            self.colors[i] = self.colors[i+1]
        self.colors[5] = old_first_color
