class Piece:
    def __init__(self, piece_type, emoji, pos_x, pos_y, white):
        self.piece_type = piece_type
        self.emoji = emoji
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.white = white

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y

    def is_white(self):
        return self.white

    def __repr__(self):
        #return "Type: " + self.piece_type + " Emoji: " + self.emoji + " Pos X: " + str(self.pos_x) + " Pos Y: " + str(self.pos_y) + " Color: " + "white" if self.white else "black"
        return self.emoji

class Pawn(Piece):
   def __init__(self, white, pos_x):
       super().__init__("pawn", "♟" if white else "♙", pos_x, 6 if white else 1, white)

class King(Piece):
   def __init__(self, white):
       super().__init__("king", "♚" if white else "♔", 4, 7 if white else 0, white)

class Queen(Piece):
   def __init__(self, white):
       super().__init__("queen", "♛" if white else "♕", 3, 7 if white else 0, white)

class Knight(Piece):
   def __init__(self, white, pos_x):
       super().__init__("knight", "♞" if white else "♘", pos_x, 7 if white else 0, white)

class Bishop(Piece):
   def __init__(self, white, pos_x):
       super().__init__("bishop", "♝" if white else "♗", pos_x, 7 if white else 0, white)

class Rook(Piece):
   def __init__(self, white, pos_x):
       super().__init__("rook", "♜" if white else "♖", pos_x, 7 if white else 0, white)

peices = []

peices.append(Pawn(True, 0))
peices.append(Pawn(True, 1))
peices.append(Pawn(True, 2))
peices.append(Pawn(True, 3))
peices.append(Pawn(True, 4))
peices.append(Pawn(True, 5))
peices.append(Pawn(True, 6))
peices.append(Pawn(True, 7))

peices.append(King(True))
peices.append(Queen(True))
peices.append(Knight(True, 2))
peices.append(Knight(True, 5))
peices.append(Bishop(True, 1))
peices.append(Bishop(True, 6))
peices.append(Rook(True, 0))
peices.append(Rook(True, 7))

peices.append(Pawn(False, 0))
peices.append(Pawn(False, 1))
peices.append(Pawn(False, 2))
peices.append(Pawn(False, 3))
peices.append(Pawn(False, 4))
peices.append(Pawn(False, 5))
peices.append(Pawn(False, 6))
peices.append(Pawn(False, 7))

peices.append(King(False))
peices.append(Queen(False))
peices.append(Knight(False, 2))
peices.append(Knight(False, 5))
peices.append(Bishop(False, 1))
peices.append(Bishop(False, 6))
peices.append(Rook(False, 0))
peices.append(Rook(False, 7))

for y in range(8):
    for x in range(8):
        printed = False;
        for peice in peices:
            if peice.get_x() == x and peice.get_y() == y:
                printed = True;
                print(peice, end = ' ')
        if not printed:
            print("*", end = ' ')
    print()

