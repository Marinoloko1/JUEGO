import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.image = animaciones[self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
        self.moviendo = False  # Nueva variable para controlar si está en movimiento

    def movimiento(self, delta_x, delta_y):
        # Verificar si el personaje se está moviendo
        if delta_x != 0 or delta_y != 0:
            self.moviendo = True
        else:
            self.moviendo = False

        if delta_x < 0:
            self.flip = False
        if delta_x > 0:
            self.flip = True

        self.forma.x += delta_x
        self.forma.y += delta_y

    def update(self):
        # Solo actualizar la animación si el personaje se está moviendo
        if self.moviendo:
            cooldown_animacion = 100  # Tiempo en milisegundos entre frames
            if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
                self.frame_index += 1
                self.update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.animaciones):
                self.frame_index = 0
        # Actualizar la imagen actual
        self.image = self.animaciones[self.frame_index]

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
