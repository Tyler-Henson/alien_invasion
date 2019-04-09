"""
Problem 12-4 from Python Crash Course
-Reskin of alien_invasion to make a screen and print the code representing a key press
"""
import sys
import pygame
from settings import Settings


def check_events():
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key)

        elif event.type == pygame.KEYUP:
            print("end")


def check_keydown_events(event, ship):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        # Start moving ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        # Stop moving ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # make the most recently drawn screen visible
    pygame.display.flip()


def key_presses():
    # initialize game and create a screen object.
    pygame.init()  # always use init() since its easier to always have it
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Keys")

    # Main loop of the game
    while True:
        check_events()
        update_screen(ai_settings, screen)


if __name__ == '__main__':
    key_presses()
