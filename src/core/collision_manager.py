import pygame
import sys


class CollisionManager:
    """Responsável por colisões"""

    def __init__(self, ship, entity_manager):
        self.ship = ship
        self.entity_manager = entity_manager

    def handle_collisions(self):
        pygame.sprite.groupcollide(
            self.entity_manager.bullets,
            self.entity_manager.aliens,
            True,
            True,
        )

        if pygame.sprite.spritecollideany(self.ship, self.entity_manager.aliens):
            print("A nave foi atingida!")
            sys.exit()