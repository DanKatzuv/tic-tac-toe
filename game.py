from itertools import cycle
from random import randint

from board import Board, FullCellError, OutOfBoundsError


def pvp():
    """
    Function for handling PvP (Player vs Player) game.

    :except: ColumnOutOfBoundsError, FullColumnError, Exception
    :return: when the game has ended
    """
    board = Board()

    for player in cycle(('X', 'O')):
        print(board)
        while True:
            try:
                row, column = cell_input(player)
                if board.move(player, row, column):
                    print(board)
                    print_win(player)
                    return
                break
            except OutOfBoundsError as error:
                print(f'The cell inputted at row {error.row + 1}, column {error.column + 1} is out of bounds.')
            except FullCellError as error:
                print(f'The cell inputted at row {error.row + 1}, column {error.column + 1} is already full.')
            except Exception as error:
                print(error)

        if board.is_full():
            print(board)
            print_game_over()
            return


def random_computer():
    board = Board()
    while True:
        print(board)
        while True:
            try:
                player = 'X'
                row, column = cell_input(player)
                if board.move(player, row, column):
                    print(board)
                    print_win(player)
                    return
                break
            except OutOfBoundsError as error:
                print(f'The cell inputted at row {error.row + 1}, column {error.column + 1} is out of bounds.')
            except FullCellError as error:
                print(f'The cell inputted at row {error.row + 1}, column {error.column + 1} is already full.')
            except Exception as error:
                print(error)

        while True:
            try:
                player = 'O'
                row = randint(0, 2)
                column = randint(0, 2)
                if board.move(player, row, column):
                    print(board)
                    print_win(player)
                    return
                break
            except OutOfBoundsError:
                continue
            except Exception as error:
                print(error)

        if board.is_full():
            print(board)
            print_game_over()
            return


def ai():
    board = Board()

    # first move
    while True:
        try:
            player = 'X'
            row, column = cell_input(player)
            board.move(player, row, column)
            print(board)
            break
        except OutOfBoundsError as error:
            print(f'The cell inputted at row {error.row + 1}, column {error.column + 1} is out of bounds.')
        except Exception as error:
            print(error)

    if row == 2 and column == 2:
        board.move('O', 0, 0)

    if any((row == 0, row == 2 and column == 0, row == 1 and column == 2)):
        board.move('O', 1, 1)

    while True:
        print(board)
        while True:
            try:
                player = 'X'
                row, column = cell_input(player)
                if board.move(player, row, column):
                    print(board)
                    print_win(player)
                    return
                break
            except OutOfBoundsError as error:
                print(f'The cell inputted at row {error.row + 1}, column {error.column + 1} is out of bounds.')
            except FullCellError as error:
                print(f'The cell inputted at row {error.row + 1}, column {error.column + 1} is already full.')
            except Exception as error:
                print(error)

        # The strategy is taken from https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy
        while True:
            player = 'O'
            other = 'X'

            # 1) Win: If the player has two in a row, they can place a third to get three in a row.
            # traverse the main diagonal
            main_diagonal = [board.board[i][i] for i in range(3)]
            if fill_last_empty(board, main_diagonal, player, other, row):
                return

            # traverse the secondary diagonal
            secondary_diagonal = [board.board[i][2 - i] for i in range(3)]
            if fill_last_empty(board, secondary_diagonal, player, other, row):
                return

            for row in board.board:
                # traverse the row
                if row.count(player) == 2 and row.count(other) == 0:
                    if board.move(player, row, row.index(board.EMPTY)):
                        print(board)
                        print_win(player)
                        return

                # traverse the column
                column = [board.board[row] for row in range(3)]
                if column.count(player) == 2 and column.count(other) == 0:
                    if board.move(player, row, column.index(board.EMPTY)):
                        print(board)
                        print_win(player)
                        return

            # 2) Block: If the opponent has two in a row, the player must play the third themselves to block the
            # opponent.
            # traverse the main diagonal
            main_diagonal = [board.board[i][i] for i in range(3)]
            if main_diagonal.count(other) == 2 and main_diagonal.count(player) == 0:
                if board.move(player, row, main_diagonal.index(board.EMPTY)):
                    print(board)
                    print_win(player)
                    return

            # traverse the secondary diagonal
            secondary_diagonal = [board.board[i][2 - i] for i in range(3)]
            if secondary_diagonal.count(other) == 2 and secondary_diagonal.count(player) == 0:
                if board.move(player, row, main_diagonal.index(board.EMPTY)):
                    print(board)
                    print_win(player)
                    return

            for row in board.board:
                # traverse the row
                if row.count(other) == 2 and row.count(player) == 0:
                    if board.move(player, row, row.index(board.EMPTY)):
                        print(board)
                        print_win(player)
                        return

                # traverse the column
                column = [board.board[row] for row in range(3)]
                if column.count(other) == 2 and column.count(player) == 0:
                    board.move(player, row, column.index(board.EMPTY))
                    print(board)
                    print_win(player)
                    return

        if board.is_full():
            print(board)
            print_game_over()
            return


def cell_input(player):
    """
    Input a column number from player.
    :param player: player to ask the input for
    :type player: str
    :return: column number player inputted
    :rtype: int
    """
    row = int(input(f'Player {player}, enter a row number between 1 and 3: ')) - 1
    column = int(input(f'Player {player}, enter a column number between 1 and 3: ')) - 1
    return row, column


def print_win(player):
    """
    Print the winner's sign.
    :param player: the winner
    :type player: str
    """
    'Player {} won! :)'.format(player)

    print(f'Player {player} has won! :)')


def print_game_over():
    """Print that the board is full and the game ended in a tie."""
    print('Board is full, tie.')


def fill_last_empty(board, sequence, player, other, row):
    if sequence.count(player) == 2 and sequence.count(other) == 0:
        if board.move(player, row, sequence.index(board.EMPTY)):
            print(board)
            print_win(player)
            return True


def main():
    """Main function running the game"""
    mode = int(input('Enter 1 for PvP Mode, 2 for Random Computer Mode, and 3 for AI Mode: '))
    if mode == 1:
        pvp()
        return
    if mode == 2:
        random_computer()
        return
    if mode == 3:
        ai()
        return
    raise ValueError('Enter a valid mode number')


if __name__ == '__main__':
    main()
