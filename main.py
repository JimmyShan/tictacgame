class Game:
    WINNING_COMBINATIONS = [(6, 7, 8),
                            (3, 4, 5),
                            (1, 2, 3),
                            (0, 4, 8),
                            (1, 4, 7),
                            (0, 3, 6),
                            (2, 5, 8),
                            (0, 1, 2)]
    def __init__(self):
        self._board = [''] * 9

    _board: 9 element list

    def play_move(self, player, move):
        """Returns a empty slot that player can take"""

    def print_board(self):
        """prints the board in a nice matrix"""


    def find_move_for_player(self, player):
        """return a position for the player"""


    def check(self):
        """Check if the game is over or not"""



