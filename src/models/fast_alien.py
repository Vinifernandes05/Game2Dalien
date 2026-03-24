# Muda o comportamento do movivmento do alien, herdando todas as caracteristicas de Alien

from models.alien import Alien

class FastAlien(Alien):
    """Alien mais rápido"""

    def update(self):
        # Movimento mais rápido que o alien padrão
        self.x += 2 * self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x