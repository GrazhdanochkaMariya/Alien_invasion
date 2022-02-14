import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing bullets fired by a ship."""

    def __init__(self, ai_game):
        """Creates a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creating a bullet at position (0, 0) and assigning the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position is stored as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Moves bullet to the top of the screen."""
        # Bullet position update as a float.
        self.y -= self.settings.bullet_speed
        # Rectangle position update.
        self.rect.y = self.y

    def draw_bullet(self):
        """Bullet output on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
