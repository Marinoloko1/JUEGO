import pygame
import constantes
from personaje import Personaje
from weapons import Weapon

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego")

def escalar_img(image, scale):
    h = image.get_height()
    w = image.get_width()
    nueva_imagen = pygame.transform.scale(image, (w * scale, h * scale))
    return nueva_imagen

#Importar imagenes
#Personaje
animaciones = []
for i in range(4):
    img = pygame.image.load(f"assets\\images\\characters\\player\\Player_{i}.png")
    img = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)
    
#Arma
imagen_pistola = pygame.image.load(f"assets\\images\\weapons\\gun.png")
imagen_pistola = escalar_img(imagen_pistola, constantes.SCALA_ARMA)

# Fondo del videojuego
Fondo = pygame.image.load("Fondo.jpg").convert()

#Crear un jugador de la clase personaje
jugador = Personaje(50, 330, animaciones)

#Crear un arma de la clase weapon
pistola = Weapon(imagen_pistola)

# Definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# Controlar el frame rate
reloj = pygame.time.Clock()

run = True

while run:
    # Controlar los fps
    reloj.tick(constantes.FPS)

    # Redibujar el fondo para limpiar la pantalla
    ventana.blit(Fondo, [0, 0])

    # Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0
    
    if mover_derecha:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo:
        delta_y = constantes.VELOCIDAD

    # Eventos de entrada del teclado
    for event in pygame.event.get():
        # Para cerrar el juego
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            # Flechas del teclado
            if event.key == pygame.K_LEFT:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT:
                mover_derecha = True
            if event.key == pygame.K_UP:
                mover_arriba = True
            if event.key == pygame.K_DOWN:
                mover_abajo = True
            
            # Teclas WASD
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
                
        # Cuando se suelte la tecla
        if event.type == pygame.KEYUP:
            # Flechas del teclado
            if event.key == pygame.K_LEFT:
                mover_izquierda = False
            if event.key == pygame.K_RIGHT:
                mover_derecha = False
            if event.key == pygame.K_UP:
                mover_arriba = False
            if event.key == pygame.K_DOWN:
                mover_abajo = False

            # Teclas WASD
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
    
    # Mover al jugador
    jugador.movimiento(delta_x, delta_y)
    
    # Actualiza la animación del jugador
    jugador.update()
    
    #Actualiza el estado del arma
    pistola.update(jugador)
    
    # Dibujar al jugador
    jugador.dibujar(ventana)
    
    #Dibujar el arma
    pistola.dibujar(ventana)

    # Actualizar la pantalla
    pygame.display.update()

pygame.quit()
