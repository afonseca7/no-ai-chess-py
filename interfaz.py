import pygame
from clases import Tablero,Peon,Pieza


pygame.init()
tablero=Tablero()


ancho = 800
alto = 800
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('motor grafico')

corriendo = True
while corriendo:

          # escucha eventos (mouse, teclado, cerrar ventana)
          for evento in pygame.event.get():
                    if evento.type == pygame.QUIT: #cerrar ventana
                              corriendo = False
          
          # actualizar logica

          # dibujar

          pantalla.fill((0,0,0)) # el fondo va a ser negro

          #rectangulos
          # rectangulos
          size = 100
          for col in range(8):
                    for fil in range(8): 
                              par_o_impar = col + fil
                              coord_x = col * size
                              coord_y = fil * size
                              
                              #dibujo cuadricula
                              if (par_o_impar) % 2 == 0 :
                                        pygame.draw.rect(pantalla, (255, 255, 255), (coord_x, coord_y, size, size))
                              else:
                                        pygame.draw.rect(pantalla, (0, 0, 0), (coord_x, coord_y, size, size))
                              
                              #guarod la pieza actual en una variable
                              pieza_actual = tablero.matriz[fil][col]

                              #valido que haya una pieza
                              if pieza_actual is not None:
                                        
                                        #definicion del texto de color a rgb
                                        if pieza_actual.color == "blanco":
                                                  color_visual = (200, 200, 200)
                                        else: 
                                                  color_visual = (50, 50, 50)
                                        
                                        #render de la pieza ya con el color que le toca
                                        pygame.draw.circle(pantalla, color_visual, (coord_x + (size / 2), coord_y + (size / 2)), 30)

                              
          
          pygame.display.flip() # actualizo la pantalla


#apago
pygame.quit()
