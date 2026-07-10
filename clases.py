
# creo la clase del tablero, va a estructurar los datos (matriz 2D)
class Board:
          def __init__(self):
                    self.matriz = [ 
                              [Rook("negro","rook"),Knight("negro","knight"),Bishop("negro","bishop"),Queen("negro","queen"),King("negro","king",'no'),Bishop("negro","bishop"),Knight("negro","knight"),Rook("negro","rook")],
                              [Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro")],
                              [None,None,None,None,None,None,None,None],
                              [None,None,None,None,None,None,None,None],
                              [None,None,None,None,None,None,None,None],
                              [None,None,None,None,None,None,None,None],
                              [Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco")],
                              [Rook("blanco","rook"),Knight("blanco","knight"),Bishop("blanco","bishop"),Queen("blanco","queen"),King("blanco","king",'no'),Bishop("blanco","bishop"),Knight("blanco","knight"),Rook("blanco","rook")]
                              ]

          def mostrar (self):
                    for fila in range (len(self.matriz)):
                              for columna in range (len(self.matriz[fila])):
                                        casilla = self.matriz[fila][columna]
                                        print(casilla, end=" ")
                              print()
          def reyEnJaque (self,color_rey):
                    fil_rey = -1 
                    col_rey = -1
                    rey_encontrado = False

                    fil = 0
                    while fil < 8 and rey_encontrado == False:
                              col = 0
                              while col < 8 and rey_encontrado == False:
                                        pieza = self.matriz[fil][col]

                                        if pieza is not None and pieza.tipo == "king" and pieza.color == color_rey:
                                                  fil_rey = fil
                                                  col_rey = col
                                                  rey_encontrado = True
                                        col += 1 
                              fil += 1
                    for fil in range(8):
                              for col in range(8):
                                        enemigo = self.matriz[fil][col]

                                        if enemigo is not None and enemigo.color != color_rey:
                                                  if enemigo.formaDeMoverse(fil,col,fil_rey,col_rey,self.matriz):
                                                            return True
                    return False

          def hayMovimientosPosibles(self,color_jugador):
                    for fil_origen in range(8):
                              for col_origen in range(8):
                                        pieza = self.matriz[fil_origen][col_origen]
                                        if pieza is not None and pieza.color == color_jugador:
                                                  for fil_destino in range(8):
                                                            for col_destino in range(8):
                                                                      
                                                                      if pieza.formaDeMoverse(fil_origen,col_origen,fil_destino,col_destino,self.matriz):
                                                                                pieza_destino_original = self.matriz[fil_destino][col_destino]
                                                                                self.matriz[fil_destino][col_destino] = pieza
                                                                                self.matriz[fil_origen][col_origen] = None

                                                                                rey_amenazado = self.reyEnJaque(color_jugador)

                                                                                self.matriz[fil_origen][col_origen] = pieza
                                                                                self.matriz[fil_destino][col_destino] = pieza_destino_original

                                                                                if rey_amenazado == False:
                                                                                          return True
                    return False



""" 1. validar la forma de moverse de la pieza
2. validar que las coordenadas destino quedendentro de los límites del tablero
3. vlidar colisiones,  comprobar que en la ruta o destino no haya una pieza aliada.
4. validar estado, comprobar que el movimiento no deje en jaque al rey aliado
5. recien ahi, ejecutar el movimiento en la matriz  """

class Piece:
          def __init__ (self,color,tipo):
                    self.color = color
                    self.tipo = tipo
          
          def formaDeMoverse(self,fil_origen,col_origen,fil_destino,col_destino,matriz):
                    pieza_destino = matriz[fil_destino][col_destino]
                    if pieza_destino is not None and pieza_destino.color == self.color:
                              return False
                    else: 
                              return True
          
          def poneEnJaque(self, fil_destino, col_destino, matriz):
        
                    for fil in range(8):
                              for col in range(8):
                                        casilla_objetivo = matriz[fil][col]
                
                                        # si hay una pieza que es rey y es del otro color
                                        if casilla_objetivo is not None and casilla_objetivo.tipo == "king" and casilla_objetivo.color != self.color:
                    
                                                  # veo si mi pieza puede atacarlo
                                                  if self.formaDeMoverse(fil_destino, col_destino, fil, col, matriz):
                                                            casilla_objetivo.enJaque = "si"
                                                            return True
                    return False
          


class Pawn(Piece):
          def __init__(self, color):
                    super().__init__(color, "pawn")


          def formaDeMoverse(self,fila_origen,col_origen,fila_destino,col_destino,matriz):         
                    
                    if self.color == "blanco":
                              direccion = -1
                              fila_inicio = 6
                    else:
                              direccion = 1
                              fila_inicio = 1

                    #avance simple:
                    if col_origen == col_destino and fila_destino == fila_origen + direccion:
                              if matriz[fila_destino][col_destino] is None:
                                        return True
                    
                    #avance doble (solo en posicion de inicio):
                    elif col_origen == col_destino and fila_destino == fila_origen + (direccion *2):
                              if fila_origen == fila_inicio:
                                        #la casilla del medio y la del final deben ser None
                                        casilla_intermedia = fila_origen + direccion
                                        if matriz[casilla_intermedia][col_destino] is None and matriz[fila_destino][col_destino] is None: 
                                                  return True

                    #avance captura: 
                    elif abs(col_origen - col_destino) == 1 and fila_destino == fila_origen + direccion:
                              pieza_destino = matriz[fila_destino][col_destino]
                              #tiene que existir una pieza en destino y debe ser enemiga 
                              if pieza_destino is not None and pieza_destino.color != self.color:
                                        return True
                    
                    return False
                              







class Rook (Piece):
          def __init__(self, color, tipo="rook"):
                    super().__init__(color, tipo)

          def formaDeMoverse(self,fil_origen,col_origen,fil_destino,col_destino,matriz):
                    
                    if super().formaDeMoverse(fil_origen,col_origen,fil_destino,col_destino,matriz) == False:
                              return False
                    
                    if col_origen != col_destino and fil_origen != fil_destino:
                              return False

                    elif col_origen == col_destino: 
                              #se mueve verticalmente
                              if fil_destino > fil_origen:
                                        paso = 1
                              else: 
                                        paso = -1     
                              
                              for casilla in range( fil_origen + paso, fil_destino, paso):
                                        casilla_intermedia = casilla
                                        if matriz[casilla_intermedia][col_destino] is not None: 
                                                  print(f"no se puede mover, existe una pieza en ({casilla_intermedia},{col_destino})")
                                                  return False
                              return True                              

                    elif fil_origen == fil_destino:
                              # se mueve horizontalmente
                              if col_destino > col_origen: 
                                        paso = 1 
                              else: 
                                        paso = -1
                              for casilla in range(col_origen + paso, col_destino, paso):
                                        casilla_intermedia = casilla
                                        if matriz[fil_destino][casilla_intermedia] is not None: 
                                                  print(f'no se puede mover, existe una pieza en ({fil_destino},{casilla_intermedia})')
                                                  return False
                              return True                         


class Knight (Piece):
          def __init__(self, color, tipo="knight"):
                    super().__init__(color, tipo)

          def formaDeMoverse(self,fil_origen,col_origen,fil_destino,col_destino,matriz):
                    if super().formaDeMoverse(fil_origen,col_origen,fil_destino,col_destino,matriz) == False:
                              return False
                    if ((abs(col_origen - col_destino) != 2 * abs(fil_origen - fil_destino)) and abs(fil_origen - fil_destino) != (2 * abs(col_origen - col_destino))) or ((abs(col_origen - col_destino)+ abs(fil_origen - fil_destino) != 3)):
                              return False
                    else:
                              return True


class Bishop (Piece):
          def __init__(self, color, tipo="bishop"):
                    super().__init__(color, tipo)

          def formaDeMoverse(self,fil_origen,col_origen,fil_destino,col_destino,matriz):

                    if super().formaDeMoverse(fil_origen,col_origen,fil_destino,col_destino,matriz) == False:
                              return False

                    if col_origen == col_destino or fil_origen == fil_destino: 
                              return False
                    
                    if (abs(col_origen - col_destino) != abs(fil_origen - fil_destino)):

                              return False

                    if fil_destino > fil_origen:
                              #se mueve hacia abajo
                              paso_y = 1
                    else:
                                        #se mueve hacia arriba
                                        paso_y = -1
                              
                    if col_destino > col_origen: 
                              #se mueve hcia la derecha
                              paso_x = 1
                    else:
                              #se mueve hacia la izquierda
                              paso_x = -1
                    
                    fil_actual = fil_origen + paso_y
                    col_actual = col_origen + paso_x
                    while col_actual != col_destino and fil_actual != fil_destino:
                              pieza_intermedia = matriz[fil_actual][col_actual]
                              if pieza_intermedia is not None:
                                        print(f'no se puede mover, existe una pieza en ({fil_actual},{col_actual})')
                                        return False
                              fil_actual += paso_y
                              col_actual += paso_x

                    return True
                                        



class King(Piece):
          def __init__(self, color, tipo="king", enJaque='no'):
                    super().__init__(color, tipo)
                    self.enJaque = enJaque 
          

          def formaDeMoverse(self,fil_origen, col_origen, fil_destino, col_destino, matriz):
                    
                    if super().formaDeMoverse(fil_origen,col_origen,fil_destino,col_destino,matriz) == False:
                              return False
                             
                    if (abs(fil_origen - fil_destino) > 1 or abs(col_origen - col_destino) > 1 ):
                              return False
                    

                    for fil in range(8):
                              for col in range(8):
                                        enemigo=matriz[fil][col]

                                        if enemigo is not None and enemigo.color != self.color:
                                                  if enemigo.formaDeMoverse(fil,col,fil_destino,col_destino,matriz):
                                                            print("ilegal, estarias en jaque")
                                                            return False
                    return True
                    
class Queen (Piece):
          def __init__(self, color, tipo="queen"):
                    super().__init__(color, tipo)

          def formaDeMoverse(self,fil_origen,col_origen,fil_destino,col_destino,matriz):
                    
                    if super().formaDeMoverse(fil_origen,col_origen,fil_destino,col_destino,matriz) == False:
                              return False

                    #movimiento recto               

                    if col_origen == col_destino: 
                              #se mueve verticalmente
                              if fil_destino > fil_origen:
                                        paso = 1
                              else: 
                                        paso = -1     
                              

                              for casilla in range( fil_origen + paso, fil_destino, paso):
                                        casilla_intermedia = casilla
                                        if matriz[casilla_intermedia][col_destino] is not None: 
                                                  print(f"no se puede mover, existe una pieza en ({casilla_intermedia},{col_destino})")
                                                  return False
                              return True

                              
                    elif fil_origen == fil_destino:
                              # se mueve horizontalmente
                              if col_destino > col_origen: 
                                        paso = 1 
                              else: 
                                        paso = -1
                              for casilla in range(col_origen + paso, col_destino, paso):
                                        casilla_intermedia = casilla
                                        if matriz[fil_destino][casilla_intermedia] is not None: 
                                                  print(f'no se puede mover, existe una pieza en ({fil_destino},{casilla_intermedia})')
                                                  return False
                              return True                      
                    
                    # movimiento diagonal
                    elif (abs(col_origen - col_destino) == abs(fil_origen - fil_destino)):

                              if fil_destino > fil_origen:
                                        #se mueve hacia abajo
                                        paso_y = 1
                              else:
                                                  #se mueve hacia arriba
                                                  paso_y = -1
                                        
                              if col_destino > col_origen: 
                                        #se mueve hcia la derecha
                                        paso_x = 1
                              else:
                                        #se mueve hacia la izquierda
                                        paso_x = -1
                              
                              fil_actual = fil_origen + paso_y
                              col_actual = col_origen + paso_x
                              while col_actual != col_destino and fil_actual != fil_destino:
                                        pieza_intermedia = matriz[fil_actual][col_actual]
                                        if pieza_intermedia is not None:
                                                  print(f'no se puede mover, existe una pieza en ({fil_actual},{col_actual})')
                                                  return False
                                        fil_actual += paso_y
                                        col_actual += paso_x
                              return True
                    return False



