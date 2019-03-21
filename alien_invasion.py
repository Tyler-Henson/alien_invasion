import pygame
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
    ship = Ship(screen)

    # Main loop of the game
    while True:
        # Watch for keyboard or mouse events
        gf.check_events()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
