from game import Game
from players import (AI, Human, RandomComputer)


def main():
    """Main function running the game."""
    while True:
        print('Welcome to the Tic Tac Toe game!')
        game = Game(player_type_chooser(True), player_type_chooser(False))
        game.play()
        if input("Would you like to play again? Enter 'Y' if yes, anything else if not: ").upper() != 'Y':
            print('Thanks for playing! Hope you enjoyed, see you next time :-)')
            exit()


def player_type_chooser(is_first):
    """
    Return the type of a player.

    :param is_first: whether the current player whose type is chosed is the first player (player X) or the second one (player O)
    :type is_first: bool
    :return: the type chosen of a player
    :rtype: Player
    """
    while True:
        player_x = input(f'''Enter the type of the {'first' if is_first else 'second'} player (player {'X' if is_first else 'O'});
        1 for Human, 2 for RandomComputer or 3 for AI: ''')
        if player_x == '1':
            return Human
        if player_x == '2':
            return RandomComputer
        if player_x == '3':
            return AI
        else:
            print('You did not enter a valid number')


if __name__ == '__main__':
    main()
