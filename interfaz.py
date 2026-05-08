import pygame
from clases import Board, Pawn, Piece


pygame.init()
board=Board()


ancho = 800
alto = 800
size = 100
screen = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('motor grafico')
img_torre_blanca = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_rlt60.png")
img_torre_blanca = pygame.transform.scale(img_torre_blanca, (size, size))
img_torre_negra = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_rdt60.png")
img_torre_negra = pygame.transform.scale(img_torre_negra, (size, size))
img_alfil_blanca = pygame.iamge.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_blt60.png",(size,size))
im_alfil_blanca = pygame.transform.scale
corriendo = True
while corriendo:

          # escucha eventos (mouse, teclado, cerrar ventana)
          for evento in pygame.event.get():
                    if evento.type == pygame.QUIT: #cerrar ventana
                              corriendo = False
          
          # actualizar logica

          # dibujar

          screen.fill((0,0,0)) # el fondo va a ser negro

          # rectangulos
          for col in range(8):
                    for fil in range(8): 
                              par_o_impar = col + fil
                              coord_x = col * size
                              coord_y = fil * size
                              
                              #dibujo cuadricula
                              if (par_o_impar) % 2 == 0 :
                                        pygame.draw.rect(screen, (253, 241, 219), (coord_x, coord_y, size, size))
                              else:
                                        pygame.draw.rect(screen, (181, 149, 110), (coord_x, coord_y, size, size))
                              
                              #guarod la pieza actual en una variable
                              pieza_actual = board.matriz[fil][col]

                              #valido que haya una pieza
                              if pieza_actual is not None:
                                        #definicion del texto de color a rgb
                                        
                                        
                                        #render de la pieza ya con el color que le toca
                                       match pieza_actual.tipo:
                                                  case "rook":
                                                            if pieza_actual.color == "blanco":
                                                                      screen.blit(img_torre_blanca, (coord_x, coord_y)) #proyecto la imagen
                                                            else:
                                                                      screen.blit(img_torre_negra, (coord_x,coord_y))
                                                  case "bishop":
                                                            if pieza_actual.color == "blanco":
                                                                      screen.blit(img_alfil_blanca

          pygame.display.flip()
#apago
pygame.quit()
