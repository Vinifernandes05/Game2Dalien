import pygame
import sys

from settings import Settings
from models.ship import Ship

from core.event_handler import EventHandler
from core.renderer import Renderer
from core.collision_manager import CollisionManager
from managers.entity_manager import EntityManager
from managers.fleet_factory import FleetFactory


class AlienInvasion:
    """Orquestrador do jogo"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.screen, self.settings)

        self.entity_manager = EntityManager(self.screen, self.settings, self.ship)
        self.event_handler = EventHandler(self.entity_manager, self.ship, self.settings)
        self.renderer = Renderer(self.screen, self.settings, self.ship, self.entity_manager)
        self.collision_manager = CollisionManager(self.ship, self.entity_manager)

        self.fleet_factory = FleetFactory(self.screen, self.settings, self.ship)
        self.entity_manager.set_aliens(self.fleet_factory.create_fleet())

    def run_game(self):
        while True:
            self.event_handler.handle_events()
            self.entity_manager.update()
            self.collision_manager.handle_collisions()
            self.renderer.render()
            pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()