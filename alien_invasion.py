"""
Alien Invasion from Python Crash Course
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
# from alien import Alien
import game_functions as gf


def run_game():
    # initialize game and create a screen object.
    pygame.init()  # always use init() since its easier to always have it
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, group of bullets, group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Get rid of bullets that have disappeared.
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
