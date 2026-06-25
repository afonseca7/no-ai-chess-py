import pygame
from clases import Board, Pawn, Piece


pygame.init()
board=Board()


ancho = 800
alto = 800
size = 100
screen = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('motor grafico')


# imagenes de las piezas con sus respectivos escalados

img_torre_blanca = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_rlt60.png")
img_torre_blanca = pygame.transform.scale(img_torre_blanca, (size, size))

img_torre_negra = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_rdt60.png")
img_torre_negra = pygame.transform.scale(img_torre_negra, (size, size))

img_alfil_blanca = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_blt60.png")
img_alfil_blanca = pygame.transform.scale(img_alfil_blanca, (size, size))

img_alfil_negra = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_bdt60.png")
img_alfil_negra = pygame.transform.scale(img_alfil_negra, (size,size))

img_caballo_blanca = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_nlt60.png")
img_caballo_blanca = pygame.transform.scale(img_caballo_blanca, (size,size))

img_caballo_negra = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_ndt60.png")
img_caballo_negra = pygame.transform.scale(img_caballo_blanca, (size,size))

img_reina_blanca = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_plt60.png")
img_reina_blanca = pygame.transform.scale(img_reina_blanca,(size,size))

img_reina_negra = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_qdt60.png")
img_reina_negra = pygame.transform.scale(img_reina_negra,(size,size))

img_rey_blanca = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_klt60.png")
img_rey_blanca = pygame.transform.scale(img_rey_blanca,(size,size))

img_rey_negra = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_kdt60.png")
img_rey_negra = pygame.transform.scale(img_rey_negra,(size,size))

img_peon_blanca = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_plt60.png")
img_peon_blanca = pygame.transform.scale(img_peon_blanca,(size,size))

img_peon_negra = pygame.image.load(r"C:\Users\Andyf_e5mb545\Documents\proyectos\chessPy\Chess_pdt60.png")
img_peon_negra = pygame.transform.scale(img_peon_negra,(size,size))


seleccionado = None
turno_actual = "blancas"

corriendo = True
while corriendo:

          # escucha eventos (mouse, teclado, cerrar ventana)
          for evento in pygame.event.get():
                    if evento.type == pygame.QUIT: #cerrar ventana
                              corriendo = False

                    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                              pos_x, pos_y = pygame.mouse.get_pos()
                              col_click = pos_x // size
                              fil_click = pos_y // size
                              
                              if seleccionado == None:

                                        if board.matriz[fil_click][col_click] is not None: 
                                                  pieza_a_seleccionar = board.matriz[fil_click][col_click]
                                        #seleccion: 

                                                  if pieza_a_seleccionar.color == turno_actual:
                                                            seleccionado = (fil_click, col_click)
                                                            print(f"Pieza seleccionada en :{seleccionado}") 
                              
                                                  else:
                                                            print("ilegal: no es tu turno")
                              else:  
                                        #movimiento 
                                        #extraigo los indices
                                        fil_origen, col_origen = seleccionado
                                        pieza = board.matriz[fil_origen][col_origen]

                                        #llamo al metodo de validacion
                                        movimiento_legal = pieza.formaDeMoverse(fil_origen,col_origen,fil_click,col_click,board.matriz)
                                        
                                        if movimiento_legal:
                                                  board.matriz[fil_click][col_click] = pieza
                                                  board.matriz[fil_origen][col_origen]= None
                                                  if turno_actual == "blancas":
                                                            turno_actual = "negras"
                                                  else: 
                                                            turno_actual = "blancas"
                                                  print(f"Movimiento ejecutado con éxito. juega: {turno_actual}")
                                        else:
                                                  print("Movimiento ilegal según las reglas de la pieza")
                                        
                                        seleccionado = None

          
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
                                                  
                                                  case "knight":
                                                            if pieza_actual.color == 'blanco':
                                                                      screen.blit(img_caballo_blanca,(coord_x,coord_y))
                                                            else: 
                                                                      screen.blit(img_caballo_negra,(coord_x,coord_y))
                                                  
                                                  case "bishop":
                                                            if pieza_actual.color == "blanco":
                                                                      screen.blit(img_alfil_blanca, (coord_x, coord_y))
                                                            else: 
                                                                      screen.blit(img_alfil_negra,(coord_x,coord_y))
                                                  
                                                  case "queen":
                                                            if pieza_actual.color == 'blanco':
                                                                      screen.blit(img_reina_blanca,(coord_x,coord_y))
                                                            else: 
                                                                      screen.blit(img_reina_negra,(coord_x,coord_y))

                                                  case "king":
                                                            if pieza_actual.color == 'blanco':
                                                                      screen.blit(img_rey_blanca,(coord_x,coord_y))
                                                            else: 
                                                                      screen.blit(img_rey_negra,(coord_x,coord_y))
                                                  
                                                  case "pawn":
                                                            if pieza_actual.color == 'blanco':
                                                                      screen.blit(img_peon_blanca,(coord_x,coord_y))
                                                            else: 
                                                                      screen.blit(img_peon_negra,(coord_x,coord_y))
                                                  



          pygame.display.flip()
#apago
pygame.quit()
