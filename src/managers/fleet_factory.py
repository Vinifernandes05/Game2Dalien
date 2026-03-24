import pygame
from models.alien import Alien
from models.fast_alien import FastAlien


class FleetFactory:
    """Cria a frota de aliens"""

    def __init__(self, screen, settings, ship):
        self.screen = screen
        self.settings = settings
        self.ship = ship

    def create_fleet(self):
        aliens = pygame.sprite.Group()

        # Alien temporário para pegar dimensões
        alien = Alien(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        # Quantidade de aliens por linha
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Quantidade de linhas
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # 🔥 Criação da frota (COM OCP)
        for row in range(number_rows):
            for col in range(number_aliens_x):

                # Alterna tipos de alien (EXTENSÃO do comportamento)
                if row % 2 == 0:
                    alien = Alien(self.screen, self.settings)
                else:
                    alien = FastAlien(self.screen, self.settings)

                # Posicionamento
                alien.x = alien_width + 2 * alien_width * col
                alien.rect.x = alien.x
                alien.rect.y = alien_height + 2 * alien_height * row

                aliens.add(alien)

        return aliens