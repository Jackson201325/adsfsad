class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game' settings."""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed_factor = 1.5

        # Lasers Settings
        self.laser_speed_factor = 6
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = 60, 60, 60
        self.lasers_allowed = 7

        # Aliens Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet_direction of 1 represent right; -1 represents left
        self.fleet_direction = 1