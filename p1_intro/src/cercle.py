import pygame
from src.forme import Forme

class Cercle(Forme):
    rayon = 100

    def __init__(self, couleur):
        Forme.__init__(self, couleur)

    def retournerOriginal(self):
        if self.rayon > 10:
            self.rayon -= 4
        else:
            self.rayon = 10

    def verifierX(self, ecran):
        # ecran.fill((0, 0, 0))
        self.verifierEspace()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            self.rayon += 0.5
        else:
            self.retournerOriginal()
        print(self.rayon)

        pygame.draw.circle(ecran, self.couleur, (200, 200), self.rayon, 0)
