"""
Alien Invasion from Python Crash Course
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initialize game and create a screen object.
    pygame.init()  # always use init() since its easier to always have it
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # print(ai_settings.bullet_color)
    # Main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
