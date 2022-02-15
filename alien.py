import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien."""

    def __init__(self, ai_game):
        """Initializes the alien and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load an alien image and assigning rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears on the top left screen corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save alien`s accurate horizontal position.
        self.x = float(self.rect.x)
