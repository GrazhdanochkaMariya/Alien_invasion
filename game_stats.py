class GameStats():
    """Statistic tracking for game Alien Invasion."""

    def __init__(self, ai_game):
        """Statistic initializer."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initializes statistics dynamics."""
        self.ships_left = self.settings.ship_limit
