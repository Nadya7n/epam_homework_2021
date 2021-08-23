"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
import itertools
from typing import List


def walking(seq):
    counter, who = 1, None
    for index in range(1, len(seq)):
        if seq[index] == seq[index - 1]:
            counter += 1
            who = seq[index]
        else:
            counter = 1
    return counter == 3, who


def do_seq(board):
    len_b = len(board)
    seq_1 = [board[i][i] for i in range(len_b)]
    seq_2 = [board[i][-(i + 1)] for i in range(len_b)]
    seq_3 = [board[i][j] for j in range(len_b) for i in range(len_b)]
    seq_4 = [board[j][i] for j in range(len_b) for i in range(len_b)]
    return list(itertools.chain(seq_1, seq_2, seq_3, seq_4))


def tic_tac_toe_checker(board: List[List]) -> str:
    answer, seq = None, list(do_seq(board))
    if True in walking(seq):
        return f"{walking(seq)[1]} wins!"
    if "-" in seq:
        answer = "unfinished!"
    return answer if answer else "draw!"
