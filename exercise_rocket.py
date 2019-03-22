import pygame
import sys


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 150, 200)

        # Ship settings
        self.ship_speed_factor = 1.5


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
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's positioning based on movement flag."""
        # Update ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center

        if self.moving_up and self.rect.up > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.left < 800:  # hardcoded limit!!!!
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centery = self.center


    def blitme(self):
        """(Block Image Transfer) Draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)


class Rocket(Ship):

    def update(self):
        """Update the ship's positioning based on movement flag."""
        # Update ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor


def check_events(ship):
    """Respond to key presses and mouse events"""
    # event = pygame.event.wait()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        # Start moving ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        # Stop moving ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make the most recently drawn screen visible
    pygame.display.flip()


def run_game():
    # initialize game and create a screen object.
    pygame.init()  # always use init() since its easier to always have it
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Main loop of the game
    while True:
        check_events(ship)
        ship.update()
        update_screen(ai_settings, screen, ship)


if __name__ == '__main__':
    run_game()
