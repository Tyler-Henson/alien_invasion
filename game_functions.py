import sys
import pygame


def check_events():
    """Respond to key presses and mouse events"""
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        sys.exit()
        # break
