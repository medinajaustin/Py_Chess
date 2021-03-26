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
            
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        
        self.moveLog.append(move) 
        
        # Switch to other player's turn
        self.whiteToMove = not self.whiteMove


#
# Class to control and make moves in the GameState
#
class Move():
    
    # Dictionary to convert rows into chess ranks and columns into files
    rankToRow = {"1": 7, "2": 6, "3": 5, "4": 4, 
                    "5": 3, "6": 2, "7": 1, "8": 0 }
    
    rowToRank = {v: k for k, v in rankToRow.items()}
    
    
    fileToCol = {"a": 0, "b": 1, "c": 2, "d": 3, 
                    "e": 4, "f": 5, "g": 6, "h": 7 }
    
    colToFile = {v: k for k, v in fileToCol.items()}
        
    def __init__(self, start, end, board):
                
        self.startRow = start[0]
        self.startCol = start[1]
        self.endRow = end[0]
        self.endCol = end[1]
        
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        
        
        
                
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        
    def getRankFile(self, row, col):
        return self.colToFile[col] + self.rowToRank[row]

