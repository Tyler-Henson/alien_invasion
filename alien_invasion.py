import sys
import pygame
from settings import Settings


def run_game():
    # initialize game and create a screen object.
    pygame.init()  # always use init() since its easier to always have it
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Main loop of the game
    while True:
        # Watch for keyboard or mouse events
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()
            # break

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
