
# creo la clase del tablero, va a estructurar los datos (matriz 2D)
class Board:
          def __init__(self):
                    self.matriz = [ 
                              [Rook("negro","rook"),Knight("negro","knight"),Bishop("negro","bishop"),Queen("negro","queen"),King("negro","king"),Bishop("negro","bishop"),Knight("negro","knight"),Rook("negro","rook")],
                              [Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro"),Pawn("negro")],
                              [None,None,None,None,None,None,None,None],
                              [None,None,None,None,None,None,None,None],
                              [None,None,None,None,None,None,None,None],
                              [None,None,None,None,None,None,None,None],
                              [Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco"),Pawn("blanco")],
                              [Rook("blanco","rook"),Knight("blanco","knight"),Bishop("blanco","bishop"),Queen("blanco","queen"),King("blanco","king"),Bishop("blanco","bishop"),Knight("blanco","knight"),Rook("blanco","rook")]
                              ]

          def mostrar (self):
                    for fila in range (len(self.matriz)):
                              for columna in range (len(self.matriz[fila])):
                                        casilla = self.matriz[fila][columna]
                                        print(casilla, end=" ")
                              print()


""" 1. validar la forma de moverse de la pieza
2. validar que las coordenadas destino quedendentro de los límites del tablero
3. vlidar colisiones,  comprobar que en la ruta o destino no haya una pieza aliada.
4. validar estado, comprobar que el movimiento no deje en jaque al rey aliado
5. recien ahi, ejecutar el movimiento en la matriz """

class Piece:
          def __init__ (self,color,tipo):
                    self.color = color
                    self.tipo = tipo
          
          def casillaHabilitada():
                    pass

          def CoordsQuedanDentroLim():
                    pass

          def RutaHabilitada():
                    pass

          def DejaEnJaque():
                    pass
          def Mover():
                   if CoordsQuedanDentroLim() & RutaHabilitada() & DejaEnJaque():
                    pass 


class Pawn(Piece):
          def __init__(self, color):
                    super().__init__(color, "pawn")
          
          def conversionMatriz():
                    coord_x, coord_y = pygame.mouse.get_pos()
                    columna_click = coord_x //size
                    fila_click = coord_y //size


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

          def formaDeMoverse():
                    
                    pass

          pass


class Knight (Piece):
          def __init__(self, color, tipo="knight"):
                    super().__init__(color, tipo)

          def formaDeMoverse():
                    
                    pass


          pass



class Bishop (Piece):
          def __init__(self, color, tipo="bishop"):
                    super().__init__(color, tipo)

          def formaDeMoverse():
                    
                    pass

          pass


class King (Piece):
          def __init__(self, color, tipo="king"):
                    super().__init__(color, tipo)

          def formaDeMoverse():
                    
                    pass

          pass


class Queen (Piece):
          def __init__(self, color, tipo="queen"):
                    super().__init__(color, tipo)

          def formaDeMoverse():
                    
                    pass

          pass



