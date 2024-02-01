import pygame
import sys
from src.cercle import Cercle

# Constants
WIDTH = 800
HEIGHT = 480

pygame.init()
ecran = pygame.display.set_mode((WIDTH, HEIGHT))

tableSprite = pygame.image.load("images/table.png")
squareSprite = pygame.image.load("images/square.png")

cercle = Cercle((0, 255, 0))

piano = pygame.mixer.Sound("sons/piano.mp3")

def gererFermeture():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while True:
    gererFermeture()

    ecran.blit(tableSprite, (0, 0))
    pygame.draw.rect(ecran, (0, 0, 255), (0,0,100,100))
    pygame.draw.circle(ecran, (255, 0, 0), (50, 50), 10)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LCTRL] and keys[pygame.K_x]:
        ecran.blit(squareSprite, (250, 250))

    if keys[pygame.K_z]:
        piano.play()

    cercle.verifierX(ecran)

    pygame.display.flip()

    # voir la resolution de la fenêtre
    print(ecran)
