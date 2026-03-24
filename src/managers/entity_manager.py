import pygame


class EntityManager:
    """Gerencia entidades"""

    def __init__(self, screen, settings, ship):
        self.screen = screen
        self.settings = settings
        self.ship = ship

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def set_aliens(self, aliens):
        self.aliens = aliens

    def add_bullet(self, bullet):
        self.bullets.add(bullet)

    def update(self):
        self.ship.update()
        self.bullets.update()
        self.aliens.update()

        self.remove_offscreen_bullets()

    def remove_offscreen_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)