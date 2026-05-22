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
        self.check_fleet_edges()
        self.aliens.update()

        self.remove_offscreen_bullets()

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def remove_offscreen_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)