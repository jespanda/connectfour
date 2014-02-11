# Run with nosetests nose/  --nocapture -v -a

from nose import with_setup
from pdb import set_trace
from nose.plugins.attrib import attr
from board import Board, Point

# -a **attr**

def setup_func():
    global newGame
    newGame = Board()

@with_setup(setup_func)
def init_board_test():
    assert True

@with_setup(setup_func)
def print_board_test():
    newGame.printBoard()
    assert True

@with_setup(setup_func)
def check_vert_test():
    assert newGame.checkVert(0) == 0

@with_setup(setup_func)
def check_is_legal_test():
    assert not(newGame.isLegal(10, 0) or newGame.isLegal(0, None) or newGame.isLegal(-1, 0))

@with_setup(setup_func)
def check_place_move_test():
    newGame.placeMove(0, "X")
    newGame.placeMove(0, "O")
    assert newGame.board.get(Point(x=0, y=0)) == "X" or newGame.board.get(Point(x=0, y=0)) == "Y"

@with_setup(setup_func)
def check_vert_win_test():
    newGame.placeMove(0, "X")
    newGame.placeMove(0, "X")
    newGame.placeMove(0, "X")
    newGame.placeMove(0, "X")
    assert newGame.complete

@with_setup(setup_func)
def check_horiz_win_test():
    newGame.placeMove(0, "X")
    newGame.placeMove(2, "X")
    newGame.placeMove(3, "X")
    newGame.placeMove(1, "X")
    assert newGame.complete

@with_setup(setup_func)
def check_diag_up_win_test():
    newGame.placeMove(0, "X")
    newGame.placeMove(0, "X")
    newGame.placeMove(1, "O")
    newGame.placeMove(1, "X")
    newGame.placeMove(2, "O")
    newGame.placeMove(2, "X")
    newGame.placeMove(2, "X")
    newGame.placeMove(3, "O")
    newGame.placeMove(3, "O")
    newGame.placeMove(3, "O")
    newGame.placeMove(3, "X")
    assert newGame.complete

@with_setup(setup_func)
def check_diag_down_win_test():
    newGame.placeMove(0, "X")
    newGame.placeMove(0, "O")
    newGame.placeMove(0, "O")
    newGame.placeMove(0, "X")
    newGame.placeMove(1, "O")
    newGame.placeMove(1, "O")
    newGame.placeMove(1, "X")
    newGame.placeMove(2, "O")
    newGame.placeMove(2, "X")
    newGame.placeMove(3, "X")







