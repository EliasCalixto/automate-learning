import pygame
import sys

#definir colores

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FLOOR1 = (120, 50, 20)
FLOOR2 = (80, 20, 20)

pygame.init()

size = (800, 500)

#crear ventana

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # color de fondo
    screen.fill(BLACK)
    #--- zona de dibujo ---

    for i in range(0, 800, 30):
        pygame.draw.rect(screen, FLOOR1, (i, 450, 15, 300))
    for x in range(15, 800, 30):
        pygame.draw.rect(screen, FLOOR2, (x, 450, 15, 300))


    #--- zona de dibujo ---
    # actualizar pantalla
    pygame.display.flip()


