💥 Game2D_Alien — Alien Invasion

**📌 Sobre o Projeto**
Este repositório contém uma versão didática do jogo "Alien Invasion" desenvolvida durante a disciplina de Alta Qualidade de Software. O foco do projeto foi aplicar arquitetura de software, princípios SOLID e boas práticas de código para obter um código organizado, testável e de fácil manutenção.

O jogo foi implementado em Python usando Pygame e apresenta comportamento de frota de inimigos (movimento lateral com descida ao atingir borda) e uma tela de vitória animada exibindo "CONGRATULATIONS" quando todas as naves são eliminadas.

**🎯 Objetivos do Projeto**
- Praticar arquitetura de software e organização em camadas
- Aplicar princípios SOLID (Responsabilidade única, Aberto/Fechado, Liskov, Interface Segregation, Inversão de Dependência)
- Implementar lógica de entidades (nave, projéteis, aliens) com responsabilidade bem definida
- Tratar entrada do usuário e renderização de forma desacoplada
- Fornecer experiência de jogo consistente e previsível

**🚀 Tecnologias Utilizadas**
- Python 3.10+ (ou compatível)
- Pygame
- Git / GitHub

**⚙️ Funcionalidades**
- Movimento da nave controlado pelo jogador (setas esquerda/direita)
- Disparo de projéteis com limite configurável
- Frota de aliens com movimento lateral e descida ao atingir borda
- Tipo de alien mais rápido (`FastAlien`) para variação de comportamento
- Detecção de colisões entre projéteis e aliens
- Tela de vitória animada: "CONGRATULATIONS" com pulso e brilho

**📂 Estrutura do Projeto**
Game2D_Alien/
│
├── images/                       # Imagens do jogo (ship.bmp, alien.bmp)
├── src/
│   ├── alien_invasion.py         # Ponto de entrada do jogo
│   ├── settings.py               # Configurações do jogo
│   ├── core/
│   │   ├── renderer.py           # Responsável pela renderização (HUD, mensagem de vitória)
│   │   ├── event_handler.py      # Tratamento de eventos de entrada
│   │   └── collision_manager.py  # Lógica de colisões
│   ├── managers/
│   │   ├── entity_manager.py     # Atualização e coordenação das entidades (aliens, balas)
│   │   └── fleet_factory.py      # Criação da frota de aliens
│   └── models/
│       ├── ship.py               # Modelo da nave do jogador
│       ├── bullet.py             # Modelo do projétil
│       ├── alien.py              # Modelo base de alien
│       └── fast_alien.py         # Alien com comportamento estendido (mais rápido)
├── .gitignore
└── README.md

**🔄 Fluxo da Aplicação**
1. `alien_invasion.py` inicializa Pygame e cria os componentes principais (Settings, Ship, EntityManager, Renderer, EventHandler, FleetFactory).
2. O loop principal processa eventos, atualiza entidades, trata colisões e renderiza a cena a cada frame.
3. Quando não houver mais aliens, o estado de vitória é ativado e o `Renderer` desenha a mensagem animada "CONGRATULATIONS".

**📐 Arquitetura e Boas Práticas**
- Organização em camadas (entrada/eventos, modelos, gerenciadores, renderização) para separar responsabilidades.
- `EntityManager` concentra a atualização e a orquestração das entidades, mantendo `Renderer` e `EventHandler` desacoplados.
- Princípios SOLID aplicados: classes pequenas com responsabilidade única; fácil extensão (ex.: `FastAlien` estende `Alien`); objetos de configuração (`Settings`) injetados nas dependências.

**▶️ Como executar (Windows)**
1. Crie um ambiente virtual (opcional):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
2. Instale o Pygame:
```powershell
pip install pygame
```
3. Execute o jogo:
```powershell
python src/alien_invasion.py
```

Observação: o repositório foi limpo para manter apenas os arquivos essenciais ao funcionamento após a implementação da animação de vitória.

**📞 Contato**
- Autor: Vinicius Sousa Fernandes
- Email: vinifernandes2005@gmail.com
- GitHub: https://github.com/Vinifernandes05

---
Este projeto foi desenvolvido como exercício de Alta Qualidade de Software, priorizando clareza, modularidade e facilidade de manutenção.