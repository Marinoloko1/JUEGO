import pygame
import constantes
from personaje import Personaje

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego")

def escalar_img(image, scale):
    h = image.get_height()
    w = image.get_width()
    nueva_imagen = pygame.transform.scale(image, (w * scale, h * scale))
    return nueva_imagen

animaciones = []
for i in range(4):
    img = pygame.image.load(f"assets\\images\\characters\\player\\Player_{i}.png")
    img = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)

#Fondo del videojuego.
Fondo = pygame.image.load("Fondo.jpg").convert()

#Imagen del personaje
Player_image = pygame.image.load("assets\\images\\characters\\player\\Player_0.png")
Player_image = escalar_img(Player_image, constantes.SCALA_PERSONAJE)

jugador = Personaje(50, 50, animaciones)

#definir las variables de movimiento del jugador.
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#Controlar los frame rate
reloj = pygame.time.Clock()

run = True
while run == True:
    
    #controlar los fps
    reloj.tick(constantes.FPS)
    
    ventana.blit(Fondo, [0, 0])
    
    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0
    
    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD

    for event in pygame.event.get():
        #para cerrar el juego
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.KSCAN_LEFT:
                mover_izquierda = True
                
        #Cuando se suelte la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
                
        #Mover al jugador
        jugador.movimiento(delta_x, delta_y)
        
        jugador.update()
        
        jugador.dibujar(ventana)

    pygame.display.update()

pygame.quit()