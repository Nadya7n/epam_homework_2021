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
from typing import List


# нелучшее решение, позже напишу покрасивее
def tic_tac_toe_checker(board: List[List]) -> str:
    answer_dict = {}
    answer = {"x": "x wins!", "o": "o wins!", "-": "unfinished!", 0: "draw!"}
    win_combination = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    list_board = [i for element in board for i in element]
    for el in ["x", "o", "-"]:
        list_indexes = [
            index for index in range(len(list_board)) if list_board[index] == el
        ]
        if el in ["x", "o"]:
            if len(list_indexes) == 4:
                if (
                    list_indexes[:3] in win_combination
                    or list_indexes[1:4] in win_combination
                ):
                    answer_dict[el] = "+"
            if len(list_indexes) == 5:
                if (
                    list_indexes[:3] in win_combination
                    or list_indexes[1:4] in win_combination
                    or list_indexes[2:5] in win_combination
                ):
                    answer_dict[el] = "+"
            if len(list_indexes) == 3 and list_indexes in win_combination:
                answer_dict[el] = "+"
        elif el == "-":
            if not answer_dict and "-" in list_board:
                answer_dict[el] = "+"
            if "-" not in list_board:
                answer_dict[0] = "+"

    return [answer[key] for key in answer_dict if key in answer][0]
