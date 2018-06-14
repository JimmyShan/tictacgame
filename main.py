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
            def check(self):
        """Check if the game is over or not"""
        ## status is a list of length 9 with each element as either X or O or empty
        ## get the list of indices of X's and O's from the board
        Xs = []
        Xo = []
        for i in range(9):
            if self._board[i] == 'X':
                Xs.append(i)
            elif self._board[i] == 'O':
                Xo.append(i)
            else:
                continue
        
        for winning in WINNING_COMBINATIONS:
            # if winning is a sublist of Xs then Xs wins; if winning is a sublist of Xo then Xo wins; return False
            # otherwise check if there is any empty spot: if ther is empty spot, return true, else return false 
            if all([val in Xs for val in winning]):
                print("A wins!")
                return False
            elif all([val in Xo for val in winning]):
                print("B wins!")
                return False
            else:
                if len(Xs) + len(Xo) < 9:                   # there are empty spots
                    return True
                else:
                    print("No one wins, game ends.")
                    return False
        #return True


if __name__ == '__main__':
    print("Let's Play!")
    print("You're Xs, I'm Os!")
    game = Game()
    while game.check():
        game.get_opponent_move()
        game.print_board()
