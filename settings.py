class Settings:
    """A class for storing all game settings."""

    def __init__(self):
        """Initializes the game settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 139)

        # Ship settings.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet parameters.
        self.bullet_speed = 1.4
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (255, 0, 213)
        self.bullets_allowed = 3

        # Alien settings.
        self.alien_speed = 0.6
        self.fleet_drop_speed = 10
        # fleet_direction = 1 (move right), -1 (move left).
        self.fleet_direction = 1
