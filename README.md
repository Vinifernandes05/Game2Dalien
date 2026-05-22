# 💥👾 Game2D_Alien — Alien Invasion

## 📌 Sobre o Projeto

Este projeto consiste no desenvolvimento de uma versão didática do jogo **Alien Invasion**, criada durante a disciplina de Alta Qualidade de Software.

O jogo foi desenvolvido em Python utilizando a biblioteca Pygame, com foco em arquitetura de software, organização em camadas, aplicação de princípios SOLID e boas práticas de desenvolvimento.

O sistema apresenta uma estrutura modular, separando responsabilidades entre renderização, gerenciamento de entidades, tratamento de eventos e lógica de colisões, proporcionando um código limpo, reutilizável e de fácil manutenção.

Além disso, o jogo possui sistema de movimentação de inimigos, disparo de projéteis, colisões e uma tela de vitória animada exibindo a mensagem **"CONGRATULATIONS"** ao eliminar todos os aliens da partida.

---

## 🎯 Objetivos do Projeto

- Praticar arquitetura de software  
- Aplicar princípios SOLID  
- Trabalhar com programação orientada a objetos  
- Desenvolver organização modular em Python  
- Criar lógica de movimentação de entidades  
- Implementar sistema de colisões  
- Trabalhar com renderização utilizando Pygame  
- Desenvolver código limpo, reutilizável e escalável  

---

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

### 🔹 Linguagem e Framework
- Python 3  
- Pygame  

### 🔹 Arquitetura e Conceitos
- Programação Orientada a Objetos (POO)  
- Princípios SOLID  
- Arquitetura em camadas  

### 🔹 Outros
- Git  
- GitHub  

---

## ⚙️ Funcionalidades

✔️ Movimentação da nave do jogador  
✔️ Disparo de projéteis  
✔️ Sistema de colisões entre projéteis e aliens  
✔️ Frota de aliens com movimentação lateral e descida automática  
✔️ Alien especial com velocidade aumentada (`FastAlien`)  
✔️ Renderização modular do jogo  
✔️ Tratamento desacoplado de eventos  
✔️ Tela de vitória animada com efeito visual  

---

## 📂 Estrutura do Projeto

```bash
Game2D_Alien
│
├── images
│   ├── ship.bmp
│   └── alien.bmp
│
├── src
│   ├── alien_invasion.py
│   ├── settings.py
│   │
│   ├── core
│   │   ├── renderer.py
│   │   ├── event_handler.py
│   │   └── collision_manager.py
│   │
│   ├── managers
│   │   ├── entity_manager.py
│   │   └── fleet_factory.py
│   │
│   └── models
│       ├── ship.py
│       ├── bullet.py
│       ├── alien.py
│       └── fast_alien.py
│
├── .gitignore
│
└── README.md
```

---

## 🔄 Fluxo da Aplicação

1. O arquivo `alien_invasion.py` inicializa o jogo e os componentes principais  
2. O loop principal processa eventos do teclado e atualiza os estados do jogo  
3. O `EntityManager` coordena entidades como aliens e projéteis  
4. O `CollisionManager` realiza a detecção de colisões  
5. O `Renderer` desenha os elementos da interface e do jogo  
6. Quando todos os aliens são eliminados, a tela de vitória é exibida  

---

## 📐 Arquitetura e Boas Práticas

O projeto foi estruturado utilizando separação de responsabilidades e organização modular.

### 🔹 Organização em Camadas
- Entrada de eventos  
- Modelos das entidades  
- Gerenciamento das entidades  
- Sistema de renderização  

### 🔹 Aplicação dos Princípios SOLID
- Classes com responsabilidade única  
- Facilidade de extensão sem modificar código existente  
- Componentes desacoplados  
- Injeção de dependências através de objetos de configuração  

### 🔹 Estrutura Modular
A organização do projeto facilita:

- Manutenção  
- Testabilidade  
- Escalabilidade  
- Reutilização de código  

---

## ▶️ Como Executar o Projeto

### 1️⃣ Criar Ambiente Virtual (Opcional)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

---

### 2️⃣ Instalar o Pygame

```powershell
pip install pygame
```

---

### 3️⃣ Executar o Jogo

```powershell
python src/alien_invasion.py
```

---

## 📞 Contato

👤 **Vinicius Sousa Fernandes**

- 📧 Email: vinifernandes2005@gmail.com  
- 💼 LinkedIn: https://linkedin.com/in/viniciussousaf  
- 💻 GitHub: https://github.com/Vinifernandes05  

---

Este projeto foi desenvolvido como exercício da disciplina de Alta Qualidade de Software, priorizando clareza, modularidade, arquitetura de software e facilidade de manutenção.
