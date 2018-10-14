# Tic-tac-toe

A Python implementation of a tic-tac-toe game with three types of players: human, random computer and smart computer.


## Getting Started
Download the game.exe file and run it. (Your operating system or browser might warn you from using the exe file, do not fear it 😀).
You can also download the [zip folder](https://github.com/DanKatzuv/tic-tac-toe/archive/master.zip) of this repository
and run the [main.py](main.py) file.

### Prerequisites
You will need Python 3.6 or above. You can download it [here](https://python.org/downloads). If you do not wish to download Python, you can
run the game.exe file as mentioned above.

### Tests
To run the tests, you will need [pytest](https://pytest.org). You can install it via `pip install pytest`.


## Running the tests
Install [pytest](https://pytest.org) via `pip install pytest`. To run the tests, download the [zip folder](https://github.com/DanKatzuv/tic-tac-toe/archive/master.zip) of this repository
open Cmd or PowerShell, change to the directory of the game files, and run `pytest` in Cmd or PowerShell.

There are tests for almost every class in this game. However, the most interesting ones are the tests for the [smart player class](tests/ai.py). They check every step the computer does.
For example, [this](https://github.com/DanKatzuv/tic-tac-toe/blob/master/tests/test_ai.py#L55-L77) method checks whether the computer fills a row of two:
```python
@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_win(player_mark):
    ai = AI(player_mark)
    board = Board()
    board._rows = [[player_mark, ' ', player_mark],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    assert ai.turn(board.representation()) == (0, 1)

    board._rows = [[' ', player_mark, ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', ' ']]
    assert ai.turn(board.representation()) == (2, 1)

    board._rows = [[' ', ' ', ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', player_mark]]
    assert ai.turn(board.representation()) == (0, 0)

    board._rows = [[' ', ' ', player_mark],
                   [' ', ' ', ' '],
                   [player_mark, ' ', ' ']]
    assert ai.turn(board.representation()) == (1, 1)
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
