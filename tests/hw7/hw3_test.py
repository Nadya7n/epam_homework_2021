import pytest

from homework7.hw3 import tic_tac_toe_checker


@pytest.mark.parametrize("board", [[["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]])
def test_tic_tac_toe_when_x_wins(board):
    """
    Testing
    :param board:
    :return:
    """
    result = tic_tac_toe_checker(board)
    assert result == "x wins!"


@pytest.mark.parametrize("board", [[["-", "-", "o"], ["-", "x", "x"], ["o", "o", "o"]]])
def test_tic_tac_toe_when_o_wins(board):
    """
     Testing
    :param board:
    :return:
    """
    result = tic_tac_toe_checker(board)
    assert result == "o wins!"


@pytest.mark.parametrize("board", [[["-", "-", "o"], ["-", "x", "x"], ["o", "x", "o"]]])
def test_tic_tac_toe_when_unfinished_game(board):
    """
     Testing
    :param board:
    :return:
    """
    result = tic_tac_toe_checker(board)
    assert result == "unfinished!"


@pytest.mark.parametrize("board", [[["x", "o", "o"], ["o", "x", "x"], ["o", "x", "o"]]])
def test_tic_tac_toe_when_draw(board):
    """
     Testing
    :param board:
    :return:
    """
    result = tic_tac_toe_checker(board)
    assert result == "draw!"
