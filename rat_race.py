def read_maze(maze_file):
    """
    Return the contents of maze_file in a list of list of str,
    where each character is a separate entry in the list.
    """
    pass


class MazeApp(Frame):
    """ The frame for the maze in the window. """

    def __init__(self, parent, maze):
        """
        Set up the window.
        Parent is the root window.
        Maze is the Maze object.
        """
        pass

#   def bind_player_keys(self):
#       """
#       Bind the keys for the players.
#       """
#       pass

    def make_maze_labels(self, maze_frame):
        """
        Make a grid of Labels with backing StringVars to
        update the picture of the maze.
        """
        pass

    def display_score(self, score_frame, score_var, label_text):
        """
        Add a label for the label_text and a label for the score_var to score_frame.
        """
        pass

    def make_label(self, r, c, maze_frame):
        """
        Create a Label and a backing StringVar. Add the StringVar to
        the_maze_vars to change the text of the Label as the players
        move.
        """
        pass

    def redraw(self):
        """
        Reset the StringVars.
        """
        pass

    def find_rats_replace_hallway(maze_list):
        """
        Return the Rats in a list.  Also modify maze_list so that the rat
        chars are replaced with hall chars.
        """
        pass


def main():
    """ Prompt for a maze file, read the maze, and start the game. """
    pass
