import pygame

screen = pygame.display.set_mode((600, 600))


class Button:

    def __init__(self, text, width, height, pos):

        # core attributes
        self.pressed = False
        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (0, 0, 0)
        # Text
        gui_font = pygame.font.SysFont('georgia', 30)

        self.text_surf = gui_font.render(text, True, (2, 2, 2))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    # Drawing the Button on screen
    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=8)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    # checking if mouse is hovering over and clicking Button
    def check_click(self):
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # if mouse colliding with button
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (180, 180, 180)

            # if mouse colliding AND pressed
            if pygame.mouse.get_pressed()[0]:
                self.top_color = (198, 198, 198)
                return True

        else:
            self.top_color = (244, 244, 244)

        return False
