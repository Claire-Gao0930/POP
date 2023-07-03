def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    import string
    chess_dic = dict(zip(string.ascii_lowercase, range(1,27)))
    a = int(chess_dic[loc[0]])
    b = int(loc[1:])
    return(a,b)


def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    import string
    chess_dic_2 = dict(zip(range(1,27), string.ascii_lowercase))
    a = str(chess_dic_2[x])
    b = str(y)
    return(a+b)


class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_

Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B''' 
    a = []
    for i in B[1]:
        a.append([i.pos_x, i.pos_y])
    if [pos_X, pos_Y] in a:
        return True
    else:
        return False
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for i in B[1]:
        if pos_X == i.pos_x  and pos_Y == i.pos_y:
            return i


class Bishop(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_
	
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this bishop can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''
        
        if is_piece_at(pos_X, pos_Y, B) == True and self.side != piece_at(pos_X, pos_Y, B).side  or is_piece_at(pos_X, pos_Y, B) == False:
            if abs(self.pos_x - pos_X) == abs(self.pos_y - pos_Y):
                return True
            else:
                return False
        else:
            return False

    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this bishop can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        
        Hints:
        - firstly, check [Rule1] and [Rule3] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule4], use is_check on new board
        '''
        if self.can_reach(pos_X, pos_Y, B) == True: 
            selfnum=0
           
            for i in range(len(B[1])): 
                if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                    selfnum = i
 
            if is_piece_at(pos_X, pos_Y, B) == True:
                desnum = 0
                for i in range(len(B[1])): 
                    if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                        desnum = i
                del B[1][selfnum]
                del B[1][desnum]

            else:            
                del B[1][selfnum]

            newPiece = Bishop(pos_X, pos_Y, self.side)
            B[1].append(newPiece)

            if is_check(self.side, B) == False:
                return True
            else:
                return False
        else:
            return False
            
            
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        if self.can_reach(pos_X, pos_Y, B) == True: 
            selfnum=0
           
            for i in range(len(B[1])): 
                if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                    selfnum = i
 
            if is_piece_at(pos_X, pos_Y, B) == True:
                desnum = 0
                for i in range(len(B[1])): 
                    if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                        desnum = i
                del B[1][selfnum]
                del B[1][desnum]

            else:            
                del B[1][selfnum]

            newPiece = Bishop(pos_X, pos_Y, self.side)
            B[1].append(newPiece)

        return B


class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_        

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''
        if is_piece_at(pos_X, pos_Y, B) == True and self.side != piece_at(pos_X, pos_Y, B).side  or is_piece_at(pos_X, pos_Y, B) == False:
            if abs(self.pos_x - pos_X) == 1 and abs(self.pos_y - pos_Y) == 0 or abs(self.pos_x - pos_X) == 0 and abs(self.pos_y - pos_Y) == 1 or abs(self.pos_x - pos_X) == 1 and abs(self.pos_y - pos_Y) == 1:
                return True
            else:
                return False
        else:
            return False         

    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        if self.can_reach(pos_X, pos_Y, B) == True: 
            selfnum=0
           
            for i in range(len(B[1])): 
                if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                    selfnum = i
 
            if is_piece_at(pos_X, pos_Y, B) == True:
                desnum = 0
                for i in range(len(B[1])): 
                    if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                        desnum = i
                del B[1][selfnum]
                del B[1][desnum]

            else:            
                del B[1][selfnum]

            newPiece = King(pos_X, pos_Y, self.side)
            B[1].append(newPiece)

            if is_check(self.side, B) == False:
                return True
            else:
                return False
        else:
            return False
                               

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        if self.can_reach(pos_X, pos_Y, B) == True: 
            selfnum=0
           
            for i in range(len(B[1])): 
                if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                    selfnum = i
 
            if is_piece_at(pos_X, pos_Y, B) == True:
                desnum = 0
                for i in range(len(B[1])): 
                    if B[1][i].pos_x == self.pos_x and B[1][i].pos_y == self.pos_y:
                        desnum = i
                del B[1][selfnum]
                del B[1][desnum]

            else:            
                del B[1][selfnum]

            newPiece = King(pos_X, pos_Y, self.side)
            B[1].append(newPiece)

            if is_check(self.side, B) == False:
                return B
            else:
                return False
        else:
            return False

def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    B1list = []
    B2list = []

    for piece in B[1]:
        if piece.side == side:
            B1list.append(piece)
        else:
            B2list.append(piece)
    B1 =  tuple[B[0], B1list]        
    B2 =  tuple[B[0], B2list]

    for piece in B1list:
        if isinstance(piece,King) == True:
            B1king = piece

    for i in B2list: 
        n = 0
        if i.can_reach(B1king.pos_x, B1king.pos_y, B):
            n += 1

    if n >0:
        return True
    else:
        return False


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_move_to
    '''
    if is_check(side,B) == True:

        B1list = []
        B2list = []

        for piece in B[1]:
            if piece.side == side:
                B1list.append(piece)
            else:
                B2list.append(piece)
        B1 =  tuple[B[0], B1list]        
        B2 =  tuple[B[0], B2list]

        for piece in B1list:
            if isinstance(piece,King) == True:
                B1king = piece

        for piece in B1list:
            if piece.can_move_to(B1king.pos_x, B1king.pos_y, B) == False:
                return True
            else:
                return False
    else:
        return False


def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints: 
    - use is_check
    - use can_move_to 
    '''

    #problem!!!!!!!!!!!!!!!!!!!
    if is_check(side,B) == False:

        B1list = []
        B2list = []

        for piece in B[1]:
            if piece.side == side:
                B1list.append(piece)
            else:
                B2list.append(piece)
        B1 =  tuple[B[0], B1list]        
        B2 =  tuple[B[0], B2list]

        for piece in B1list:
            if isinstance(piece,King) == True:
                B1king = piece

        for piece in B2list:
            if piece.can_move_to(B1king.pos_x, B1king.pos_y, B) == True:
                return True
            else:
                return False
    else:
        return False

       
def read_board(filename: str) :
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''

    try:
        chess = []
        chesslist = []
        infile = open(filename, "r")
        lines = infile.readlines()
        for line in lines:
            a = line.rstrip().split(", ")
            chess.append(a)
        whitepiece = chess[1]
        for white in whitepiece:
            if white[0] == "B":
                White = Bishop(location2index(white[1:])[0], location2index(white[1:])[1], True)
            else:
                White = King(location2index(white[1:])[0], location2index(white[1:])[1], True)
            chesslist.append(White)

        blackpiece = chess[2]
        for black in blackpiece:
            if black[0] == "B":
                Black = Bishop(location2index(black[1:])[0], location2index(black[1:])[1], False)
            else:
                Black = King(location2index(black[1:])[0], location2index(black[1:])[1], False)
            chesslist.append(Black)
        Board = tuple()
        Board =(int(chess[0][0]),chesslist)
        return Board
        print(Board)

    except IOError:
        print("This is not a valid file. File name for initial configuration: ")

    
#def test_read_board1():
   #  pass


def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    whitelist = []
    blacklist = []
    for piece in B[1]:
        if piece.side == True:
            whitelist.append(piece_mark(piece))
        else:
            blacklist.append(piece_mark(piece))
    data = [B[0], whitelist, blacklist]
    with open(filename, "w") as f:
        for line in data:
            f.write("%s\n" % line)

def piece_mark(piece: Piece):     
    if isinstance(piece, Bishop):
        a =  "B"
    else:
        a =  "K"
    b = index2location(piece.pos_x, piece.pos_y)
    return (a+b) 


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''
    import random

    blackpiece = []
    coorlist = []
    i = 0

    for piece in B[1]:
        if piece.side == False:
            blackpiece.append(piece)
            random.shuffle(blackpiece)
    
    for i in range(1,B[0]):
        for j in range(1,B[0]):
            coorlist.append([i,j])
    coor = random.choice(coorlist)

    for piece in blackpiece:
        if piece.can_move_to(coor[0], coor[1], B) == True:
            i += 1

    return(tuple[piece, coor[0], coor[1]])


def conf2unicode(B: Board) -> str: 
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    unicode_map = {'wk': '\u2654', 'wb': '\u2657', 'bk': '\u265A', 'bb': '\u265D', 'sp': '\u2001'}
    w = int(B[0])
    Matrix = [['' for x in range(w)] for y in range(w)]   
    for piece in B[1]:
        if piece.side == True:
            if isinstance(piece, Bishop):
                Matrix[piece.pos_x - 1][piece.pos_y - 1] += '\u2657'
            if isinstance(piece, King):
                Matrix[piece.pos_x - 1][piece.pos_y - 1] += '\u2654' 
        if piece.side == False:
            if isinstance(piece, Bishop):
                Matrix[piece.pos_x - 1][piece.pos_y - 1] += '\u265D'
            if isinstance(piece, King):
                Matrix[piece.pos_x - 1][piece.pos_y - 1] += '\u265A'    
       
    print(Matrix)


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''   
    filename = input("File name for initial configuration: ") 
    Board = read_board(filename)
    conf2unicode(Board)
    move_str = input("Next move of White: ")

    if move_str != "QUIT":
        Piece = piece_at(location2index(move_str[:2])[0], location2index(move_str[:2])[1], Board)
        if Piece.can_move_to(location2index(move_str[3:])[0], location2index(move_str[3:])[1], Board) == True:
            Board = Piece.move_to(location2index(move_str[3:])[0], location2index(move_str[3:])[1], Board)
            print("The configuration after White's move is:", conf2unicode(Board))

            if is_checkmate(False, Board) == True:
                print("Game over. White wins.")
                return

            if is_stalemate(False, Board) == True:
                print("Game over. Stalemate.")
                return

            else:
                find_black_move(Board)
                blackpiece = find_black_move(Board)[0]
                x = find_black_move(Board)[1]
                y = find_black_move(Board)[2]
                Board = blackpiece.move_to(x, y, Board)

                st1 = index2location(blackpiece.pos_x, blackpiece.pos_y)
                st2 = index2location(x, y)
                location = st1 + st2

                print("Next move of Black is", location, ". The configuration after Black's move is:", conf2unicode(Board))
       
                if is_checkmate(True, Board) == True:
                    print("Game over. Black wins.")
                    return

                if is_stalemate(True, Board) == True:
                    print("Game over. Stalemate.")
                    return

                else:
                    move_str = input("Next move of White: ")

        else:
            print("This is not a valid move. Next move of White:")

    else:
        savename = input("File name to store the configuration: ") 
        save_board(savename, Board)
        print("The game configuration saved.")
        return

if __name__ == '__main__': #keep this in
   main()
