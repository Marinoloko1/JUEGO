import pygame
import math

class Weapon():
    def __init__(self, image):
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje):
        # Centrar el arma con el personaje
        self.forma.center = personaje.forma.center

        # Obtener la posicion del raton
        mouse_pos = pygame.mouse.get_pos()

        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)  

        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

        if personaje.flip:
            self.forma.x = self.forma.x + personaje.forma.width / 2
            self.rotar_arma(flip=False)
        else:
            self.forma.x = self.forma.x - personaje.forma.width / 2
            self.rotar_arma(flip=True)

    def rotar_arma(self, flip):
        if flip:
            imagen_flip = pygame.transform.flip(self.imagen_original, False, True)
        else:
            imagen_flip = self.imagen_original

        self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

        self.forma = self.imagen.get_rect(center=self.forma.center)

    def dibujar(self, interfaz):
        interfaz.blit(self.imagen, self.forma)
