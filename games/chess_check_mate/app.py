# http://www.codewars.com/kata/52fcc820f7214727bc0004b7/train/python
# {
#   'piece': string, # pawn, rook, knight, bishop, queen or king
#   'owner': int,    # 0 for white or 1 for black
#   'x': int,        # 0-7 where 0 is the leftmost column (or "A")
#   'y': int,        # 0-7 where 0 is the top row (or "8" in the board below)
#   'prevX': int,    # 0-7, presents this piece's previous x, only given if this is the piece that was just moved
#   'prevY': int     # 0-7, presents this piece's previous y, only given if this is the piece that was just moved
# }
WHITE = 0
BLACK = 1

PAWN = 'pawn'
ROOK = 'rook'
KNIGHT = 'knight'
BISHOP = 'bishop'
QUEEN = 'queen'
KING = 'king'


def filter_available_positions(positions, pieces):
    other = [(p.x, p.y) for p in pieces]
    return ((p.x, p.y) for p in positions if (p.x, p.y) not in other)


class Pawn:
    def __init__(self, pos, player, pieces):
        super().__init__()
        self.x, self.y = pos
        self.player = player
        self.pieces = pieces
        self.sign = '+' if self.player == BLACK else '-'

    def eats_positions(self):
        p = [
            eval( '(self.x{sign}1, self.y+1)'.format(sign=self.sign) ),
            eval( '(self.x{sign}1, self.y-1)'.format(sign=self.sign) ),
        ]
        return filter_available_positions(p, self.pieces)

    def can_eat(self, piece):
        return (piece.x, piece.y) in self.eats_positions()


def create_piece(name, pos, player, pieces):
    if name == PAWN:
        return Pawn(pos, player, pieces)


# Returns an array of threats if the arrangement of
# the pieces is a check, otherwise false
def isCheck(pieces, player):
    pass


# Returns true if the arrangement of the
# pieces is a check mate, otherwise false
def isMate(pieces, player):
    pass
