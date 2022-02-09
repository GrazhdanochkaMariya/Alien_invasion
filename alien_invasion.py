import sys

import pygame

from settings import Settings

from ship import Ship


class AlienInvasion:
    """A class for managing resources and game behavior."""

    def __init__(self):
        """Game initializing and making game  resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Assigning a background color.
        self.bg_color = (0, 0, 139)

    def run_game(self):
        """Starting the main game cycle."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Tracking keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Updates the images on the screen and displays a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Creating an instance and launching the game.
    ai = AlienInvasion()
    ai.run_game()
