import pygame

class Renderer:
    """Responsável por desenhar tudo"""

    def __init__(self, screen, settings, ship, entity_manager):
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.entity_manager = entity_manager
        self.message_font = pygame.font.SysFont(None, 96)
        self.message_text = "CONGRATULATIONS"

    def render(self, victory=False, alpha=255, scale=1.0):
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.entity_manager.bullets.sprites():
            bullet.draw_bullet()

        self.entity_manager.aliens.draw(self.screen)

        if victory:
            self.draw_victory_message(alpha, scale)

    def draw_victory_message(self, alpha, scale):
        text_surface = self.message_font.render(self.message_text, True, (255, 215, 0))
        text_surface = text_surface.convert_alpha()
        text_surface.set_alpha(alpha)

        scaled_surface = pygame.transform.rotozoom(text_surface, 0, scale)
        rect = scaled_surface.get_rect()
        rect.center = self.screen.get_rect().center

        shadow_surface = self.message_font.render(self.message_text, True, (0, 0, 0))
        shadow_surface = pygame.transform.rotozoom(shadow_surface.convert_alpha(), 0, scale)
        shadow_rect = shadow_surface.get_rect()
        shadow_rect.center = (rect.centerx + 4, rect.centery + 4)
        shadow_surface.set_alpha(max(0, alpha - 100))

        self.screen.blit(shadow_surface, shadow_rect)
        self.screen.blit(scaled_surface, rect)