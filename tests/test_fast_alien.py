# Importa o pygame (necessário para criar a tela do jogo)
import pygame

# Importa o pytest (framework de testes)
import pytest

# Importa a classe que queremos testar
from models.fast_alien import FastAlien

# Importa as configurações do jogo
from settings import Settings

# 🔧 FIXTURE: prepara o ambiente para os testes
@pytest.fixture
def setup_env():
    # Inicializa o pygame
    pygame.init()

    # Cria uma tela (mesmo que não apareça visualmente)
    screen = pygame.display.set_mode((800, 600))

    # Cria as configurações do jogo
    settings = Settings()

    # Retorna tudo que o teste precisa
    return screen, settings


# 🧪 TESTE: verifica se o FastAlien se move
def test_fast_alien_moves_faster(setup_env):
    
    # Recebe os dados da fixture
    screen, settings = setup_env

    # Cria um alien rápido
    alien = FastAlien(screen, settings)

    # Salva a posição inicial do alien
    posicao_inicial = alien.x

    # Executa o movimento
    alien.update()

    # Verifica se ele andou (posição atual maior que inicial)
    assert alien.x > posicao_inicial