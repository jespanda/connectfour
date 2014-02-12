from collections import namedtuple
from pdb import set_trace

Point = namedtuple("Point", ["x", "y"])

class Board:
    def __init__(self):
        self.size_x = 7
        self.size_y = 6
        self.complete = False
        # Make the key = None and create a board, it starts from 0,0 from upper left and x,x in lower right
        self.board = {key:None for key in [Point(x = x1, y = y1) for x1 in range(0, self.size_x) for y1 in range(0, self.size_y)]}

    def printBoard(self):
        for i in reversed(range(self.size_y)):
            print
            print i,
            for j in range(self.size_x):
                curr_point = self.board.get(Point(x=j, y=i))
                if curr_point == None:
                    print "-",
                else: 
                    print curr_point,
        print 
        print " ",
        for k in range(self.size_x):
            print k,
        print

    def placeMove(self, pos_x, player):
        pos_y = self.checkVert(pos_x)
        curr_point = Point(x=pos_x, y=pos_y)
        if self.isLegal(curr_point):
            self.board[curr_point] = player
            self.printBoard()
            if self.isWin(curr_point, player):
                self.complete = True
                print "Congratulations Player " + player
        else:
            print "Illegal Move"

    def checkVert(self, pos_x):
        for tmp_y in range(self.size_y):
            if self.board.get(Point(x=pos_x, y=tmp_y)) == None:
                return tmp_y
                break
        return None

    def isLegal(self, point):
        if point.y == None:
            return False
        if point.x < 0 or point.x>self.size_x:
            return False
        return True

    def isWin(self, point, player):
        horiz_tally = self.tallyCounter(point, 1, 0, player) +  self.tallyCounter(point, -1, 0, player) - 1
        vert_tally = self.tallyCounter(point, 0, 1, player) + self.tallyCounter(point, 0, -1, player) - 1
        diag_up_tally = self.tallyCounter(point, 1, 1, player) + self.tallyCounter(point, -1, -1, player) - 1
        diag_down_tally = self.tallyCounter(point, -1, 1, player) + self.tallyCounter(point, 1, -1, player) - 1
        max_tally = max(horiz_tally, vert_tally, diag_up_tally, diag_down_tally)
        return max_tally >= 4

    def tallyCounter(self, point, multi_x, multi_y, player):
        tmp_x = point.x
        tmp_y = point.y
        tally = 0
        while self.board.get(Point(x=tmp_x, y=tmp_y)) == player:
            tally += 1
            tmp_x += multi_x
            tmp_y += multi_y
        return tally

