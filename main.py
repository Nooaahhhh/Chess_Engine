import sys
import pygame
from startGUI import menu_gui

pygame.init()

screen = pygame.display.set_mode((1200, 720))

pygame.display.set_caption('Chess Engine')

img = pygame.image.load('contents/chess_piece_knight.png')
pygame.display.set_icon(img)

def mainloop():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        menu_gui()

        pygame.display.update()


if __name__ == '__main__':
    mainloop()
