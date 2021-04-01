from . import home_screen
import pygame
from ..utils.widgets import TextButton
from ..utils import constants as consts


def play():
    running = True

    while running:

        mouse_down = False
        consts.MAIN_DISPLAY.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        font = consts.FONT_MONO_LARGE
        # coins limit reached

        text = font.render('You caught the robber! You get 150 coins!', True, (255, 255, 255))
        w, h = text.get_rect().width, text.get_rect().height
        consts.MAIN_DISPLAY.blit(text, ((800 - w) / 2, ((600 - h) / 2)))

        city_button = TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                   (consts.SCREEN_HEIGHT / 2) + 100),
                                 width=200, height=40, fg_color=(0, 0, 0), bg_color=(255, 0, 0),
                                 font=consts.FONT_MONO_LARGE, text='Home')

        if city_button.hovered:
            city_button.toggle_bg((139, 0, 0))
            if mouse_down:
                city_button.toggle_bg((255, 0, 0))
                return home_screen.play()

        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
