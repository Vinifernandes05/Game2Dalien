import pygame
import sys
from models.bullet import Bullet


class EventHandler:
    """Responsável por input"""

    def __init__(self, entity_manager, ship, settings):
        self.entity_manager = entity_manager
        self.ship = ship
        self.settings = settings

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

                elif event.key == pygame.K_SPACE:
                    self.shoot()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def shoot(self):
        if len(self.entity_manager.bullets) < self.settings.bullet_allowed:
            bullet = Bullet(self.entity_manager.screen, self.settings, self.ship)
            self.entity_manager.add_bullet(bullet)