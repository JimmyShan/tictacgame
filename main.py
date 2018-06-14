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
        self._board = [' '] * 9

    def play_move(self, player, move):
        """Returns a empty slot that player can take"""
        pass

    def print_board(self):
        """prints the board in a nice matrix"""
        for i in range(3):
            print('-------')
            print('|' + '|'.join(self._board[i * 3 : i * 3 + 3]) + '|')
        print('-------')


    def find_move_for_player(self, player):
        """return a position for the player"""
        pass


    def parse_move(self):
        """
        '[abc][012] first column, second row'
        """
        move = input()
        if not move:
            raise SystemExit
        print(move)

    def check(self):
        """Check if the game is over or not"""
        return True


if __name__ == '__main__':
    print("Let's Play!")
    print("You're Xs, I'm Os!")
    game = Game()
    while game.check():
        print('Your move: ', end='')
        move = game.parse_move()
        game.play_move('x', move)
        game.print_board()
