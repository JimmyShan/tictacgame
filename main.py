import cmd


class Shell(cmd.Cmd):
    pass

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

    def play_move(self, player, move):
        """Returns a empty slot that player can take"""
        pass

    def print_board(self):
        """prints the board in a nice matrix"""
        for i in range(3):
            print '-------'
            print '| | | |'


    def find_move_for_player(self, player):
        """return a position for the player"""
        pass


    def check(self):
        """Check if the game is over or not"""
        pass



