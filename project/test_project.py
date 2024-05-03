import pytest

from project import make_move, check_winner, check_draw


def test_make_move():
    board = [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
    assert make_move(board, 0, 1, 'X') == True
    assert board == [['X', 'X', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
    assert make_move(board, 0, 1, 'O') == False

def test_check_winner():
    board1 = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']]
    assert check_winner(board1) == 'X'
    board2 = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    assert check_winner(board2) == None

def test_check_draw():
    board1 = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    assert check_draw(board1) == True
    board2 = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']]
    assert check_draw(board2) == False
