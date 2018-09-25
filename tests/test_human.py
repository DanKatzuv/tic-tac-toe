from pytest import mark
from players import Human


@mark.parametrize('mark', ('X', 'O'))
def test_human_init(mark):
    human = Human(mark)
    assert human.mark == mark


@mark.parametrize('cell_input,turn', ((1, 1), (2, 2)))
def test_turn(cell_input, turn):
    assert cell_input == turn
