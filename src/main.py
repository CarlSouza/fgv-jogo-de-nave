import pygame

from src.scenes.game import GameScene

# Cria a tela do jogo, com o tamanho de 1200x800
screen = pygame.display.set_mode((1200, 800))

# Cria a cena do jogo
game_scene = GameScene(screen)

# Controle se o jogo está sendo executado ou não
running = True

while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Realiza os cálculos da parte lógica do jogo
    game_scene.step()

    # Desenha na tela
    game_scene.draw()
