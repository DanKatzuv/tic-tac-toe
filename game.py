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

