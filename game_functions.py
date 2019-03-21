import sys
import pygame


def check_events():
    """Respond to key presses and mouse events"""
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        sys.exit()
        # break


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make the most recently drawn screen visible
    pygame.display.flip()
