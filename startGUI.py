import pygame
import sys
import GameState
from buttonClass import Button
from GameState import drawGameState

screen = pygame.display.set_mode((600, 600))


def play():
    gs = GameState.GameState()
    back_button = Button('Back', 200, 50, (975, 25))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # background
        screen.fill((99, 99, 99))
        # chessboard
        drawGameState(screen, gs)
        # back-button

        back_button.draw()
        pygame.draw.rect(screen, (60, 60, 60), [550, 25, 250, 490])
        if back_button.check_click():
            menu_gui()

        pygame.display.update()


def options():
    back_button = Button('Back', 200, 50, (975, 25))

    my_font = pygame.font.SysFont('leelawadeeui', 20)
    color_change_text = my_font.render('Change the color of your Chessboard !', True, (234, 234, 234))

    color_change_button = Button('Change', 300, 50, (450, 430))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((99, 99, 99))
        screen.blit(color_change_text, (440, 395))

        color_change_button.draw()
        if color_change_button.check_click():
            pass


        back_button.draw()
        if back_button.check_click():
            menu_gui()

        pygame.display.update()


def menu_gui():
    # background picture
    BG = pygame.image.load('contents/BG.png')

    pygame.display.set_caption('Chess Engine')

    # Fonts
    my_font = pygame.font.SysFont('georgia', 150)

    # All Buttons
    play_Button = Button('Play', 275, 50, (675, 310))
    options_Button = Button('Options', 275, 50, (675, 390))
    quit_Button = Button('Quit', 275, 50, (675, 470))

    menu_text = my_font.render('CHESS', True, (234, 234, 234))

    while True:

        # Displayed:
        screen.blit(BG, (0, 0))
        # Main menu text
        screen.blit(menu_text, (575, 90))

        # Buttons

        play_Button.draw()
        quit_Button.draw()
        options_Button.draw()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if play_Button.check_click():
            play()

        if options_Button.check_click():
            options()

        if quit_Button.check_click():
            pygame.quit()
            sys.exit()

        pygame.display.update()
