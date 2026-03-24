class Renderer:
    """Responsável por desenhar tudo"""

    def __init__(self, screen, settings, ship, entity_manager):
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.entity_manager = entity_manager

    def render(self):
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.entity_manager.bullets.sprites():
            bullet.draw_bullet()

        self.entity_manager.aliens.draw(self.screen)