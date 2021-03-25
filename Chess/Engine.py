#
#   Class to store current game state
#   Determine valid moves
#   Keep move log    
#

class GameState():
    def __init__(self):
        # Chess Board is represented by 2d 8x8 list
        # Each element is two characters:
        #   (b or w) for piece color
        #   (R, N, B, Q, K, P) for piece type
        # "--" is an unoccupied square
            self.board = [
                ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
            ]

            self.whiteMove = True
            self.moveLog = []

            

