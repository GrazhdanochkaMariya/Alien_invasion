import sys

import pygame


class AlienInvasion:
    """A class for managing resources and game behavior."""

    def __init__(self):
        """Game initializing and making game  resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Assigning a background color.
        self.bg_color = (0, 0, 139)

    def run_game(self):
        """Starting the main game cycle."""
        while True:
            # Tracking keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # The screen is redrawn every time the cycle passes.
            self.screen.fill(self.bg_color)

            # Displaying the last drawn screen.
            pygame.display.flip()


if __name__ == '__main__':
    # Creating an instance and launching the game.
    ai = AlienInvasion()
    ai.run_game()
