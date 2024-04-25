import pygame

# !!! FEN strings use for pieces on board

width = height = 512
dimension = 8
sq_size = height // dimension
max_fps = 15
images = {}


class GameState:

    def __init__(self):
        # board 8x8 2d list, each element 2 characters
        # first character is color the second is the piece (R, N, B, Q, K, P)
        # -- is empty

        self.board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.whiteToMove = True
        self.moveLog = []


def loadImages():
    # every piece
    pieces = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wp', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bp']
    # loading piece
    for piece in pieces:
        images[piece] = pygame.image.load('contents/ImagesPieces/' + piece + '.png')


def draw_board(screen):
    # color for white and black
    colors = [(222, 184, 135), (139, 69, 19)]
    # rows and colounms
    for r in range(dimension):
        for c in range(dimension):
            # square colors alternating
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


def draw_pieces(screen, board):
    # loading images of pieces
    loadImages()

    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != '--':  # if piece is not empty square
                screen.blit(images[piece], pygame.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


def drawGameState(screen, gs):
    # drawing board
    draw_board(screen)
    # drawing pieces on board
    draw_pieces(screen, gs.board)
