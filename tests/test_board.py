from pytest import mark
from board import Board


@mark.parametrize('player', ('X', 'O'))
def test_row(player):
    board = Board()
    board._board = [[' ', ' ', ' '],
                    [player, player, player],
                    [' ', ' ', ' ']]

    for column in range(3):
        assert board._has_win_occurred(1, column)
    assert not board._has_win_occurred(2, 0)
    assert not board._has_win_occurred(2, 1)
    assert not board._has_win_occurred(2, 2)


@mark.parametrize('player', ('X', 'O'))
def test_column(player):
    board = Board()
    board._board = [[' ', player, ' '],
                    [' ', player, ' '],
                    [' ', player, ' ']]

    for row in range(3):
        assert board._has_win_occurred(row, 1)
    assert not board._has_win_occurred(0, 2)
    assert not board._has_win_occurred(2, 0)
    assert not board._has_win_occurred(2, 2)


@mark.parametrize('player', ('X', 'O'))
def test_main_diagonal(player):
    board = Board()
    board._board = [[player, ' ', ' '],
                    [' ', player, ' '],
                    [' ', ' ', player]]

    for row in range(3):
        assert board._has_win_occurred(row, row)
    assert not board._has_win_occurred(0, 2)
    assert not board._has_win_occurred(2, 0)
    assert not board._has_win_occurred(2, 1)


@mark.parametrize('player', ('X', 'O'))
def test_secondary_diagonal(player):
    board = Board()
    board._board = [[' ', ' ', player],
                    [' ', player, ' '],
                    [player, ' ', ' ']]

    for row in range(3):
        assert board._has_win_occurred(row, 2 - row)
    assert not board._has_win_occurred(0, 0)
    assert not board._has_win_occurred(2, 2)
    assert not board._has_win_occurred(1, 0)
