import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of screen
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's positioning based on movement flag."""
        # Update ship's center value, not the rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            # self.rect.centerx -= 1

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)
