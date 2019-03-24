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
