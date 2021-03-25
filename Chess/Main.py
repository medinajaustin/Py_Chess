# Driver File
# Handle User Input
# Display GameState objects

import pygame as p
import Engine

# Resolution is 512x512
# Dimension is 8x8
width = height = 512
dimension = 8

# Size of each square
squareSize = height // dimension

# Max FPS
fps = 15

# Dictionary of images, will be initialized by loadImages()
images = {}

# Initialize global images dict 
def loadImages():
    
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("../images/" + piece + ".png"), (squareSize, squareSize))
    


# Main Driver
# User Input
# Graphics Handler
def main():
    
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    
    gs = Engine.GameState()
    loadImages()
    
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        
        drawGameState(screen, gs)        
        clock.tick(fps)
        p.display.flip()
    

# Draw graphics for current GameState  
def drawGameState(scr, state):
    drawBoard(scr)
    # add in piece highlighting, move suggest
    drawPieces(scr, state.board)

# Draw the squares
def drawBoard(scr):
    # Top left square is always a light square
    
    colors = [p.Color("white"), p.Color("dark green")]
    
    for row in range(dimension):
        for col in range (dimension):
            if ((row + col ) % 2 ) == 0: # Light Square
                p.draw.rect(scr, colors[0], p.Rect(col*squareSize, row*squareSize, squareSize, squareSize))
            else: # Dark Square
                p.draw.rect(scr, colors[1], p.Rect(col*squareSize, row*squareSize, squareSize, squareSize))
    
# Draw the pieces    
def drawPieces(scr, board):
    for row in range(dimension):
        for col in range(dimension):
            piece = board[row][col]
            if board[row][col] != '--':
                scr.blit(images[piece], p.Rect(col*squareSize, row*squareSize, squareSize, squareSize))
             


    
if __name__ == "__main__":  
    main()