"""
This will be our main driver file. It will be responsible for handling user input and displaying the current GameState
object.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512  # 400 is another option/
DIMENSION = 8  # Dimensions of the chessboard/
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # For animations later on/
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main.
'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # NOTE: We can access an image by calling 'IMAGES('wp')'


'''
The main driver for our code. This will handle user input and updating the graphics.
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # Only do this once, before the while loop/
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for all graphics within the current game state.
'''


def drawGameState(screen, gs):
    drawBoard(screen)  # Draws the squares on the board/
    # Add feature for piece highlighting or move suggestions later/
    drawPieces(screen, gs.board)  # Draws pieces on top of those squares/


'''
Draws the squares on the board. The top left square is light.
'''


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draws the pieces on the board using the current GameState.board
'''


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # Not an empty square/
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
