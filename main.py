class Game:
    WINNING_COMBINATIONS = [(6, 7, 8),
                            (3, 4, 5),
                            (1, 2, 3),
                            (0, 4, 8),
                            (1, 4, 7),
                            (0, 3, 6),
                            (2, 5, 8),
                            (0, 1, 2)]
    GOOD_MOVES = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

    def __init__(self):
        self._board = [' '] * 9

    def print_board(self):
        """prints the board in a nice matrix"""
        print(' a  b  c')
        for i in range(3):
            print('  -------')
            print(str(i + 1) + ' |' + '|'.join(self._board[i * 3 : i * 3 + 3]) + '|')
        print('  -------')


    def find_move_for_player(self, player):
        """return a position for the player"""
        pass


    def get_opponent_move(self):
        """
        '[abc][012] first column, second row'
        """
        while True:
            print('Your move: ', end='')
            move = input()
            if not move:
                raise SystemExit
            if move not in self.GOOD_MOVES:
                print('Illegal move')
                continue
            pos = self.GOOD_MOVES.index(move)
            if self._board[pos] != ' ':
                print('Illegal move')
            else:
                break

        self._board[pos] = 'X'


    def check(self):
        """Check if the game is over or not"""
        return True


if __name__ == '__main__':
    print("Let's Play!")
    print("You're Xs, I'm Os!")
    game = Game()
    while game.check():
        game.get_opponent_move()
        game.print_board()
