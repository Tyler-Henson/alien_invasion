"""
Alien Invasion from Python Crash Course
"""


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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3  # 3 up from 1
        self.bullet_width = 300  # 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 300  # 3

        # Alien settings
        self.alien_speed_factor = 10  # 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
