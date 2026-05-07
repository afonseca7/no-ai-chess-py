
# creo la clase del tablero, va a estructurar los datos (matriz 2D)
class Tablero:
          def __init__(self):
                    self.matriz = [ 
                              [".", ".", ".", ".", ".", ".", ".", "."],
                              [".", ".", ".", ".", ".", ".", ".", "."],
                              [".", ".", ".", ".", ".", ".", ".", "."],
                              [".", ".", ".", ".", ".", ".", ".", "."],
                              [".", ".", ".", ".", ".", ".", ".", "."],
                              [".", ".", ".", ".", ".", ".", ".", "."],
                              [".", ".", ".", ".", ".", ".", ".", "."],
                              [".", ".", ".", ".", ".", ".", ".", "."]
                              ]

          def mostrar (self):
                    for fila in range (len(self.matriz)):
                              for columna in range (len(self.matriz[fila])):
                                        casilla = self.matriz[fila][columna]
                                        print(casilla, end=" ")
                              print()




class Pieza:
          def __init__(color,x,y):
                    self.color = color
                    self.x = x
                    self.y = y

          def formaDeMoverse():

                    pass
          def Mover():
                    pass
          def puedeMoverse():
                    pass



class Torre (Pieza):

          def formaDeMoverse():
                    
                    pass

          pass


class Caballo (Pieza):

          def formaDeMoverse():
                    
                    pass


          pass



class Alfil (Pieza):

          def formaDeMoverse():
                    
                    pass

          pass


class Rey (Pieza):

          def formaDeMoverse():
                    
                    pass

          pass


class Reina (Pieza):

          def formaDeMoverse():
                    
                    pass

          pass


class Peon (Pieza):

          def formaDeMoverse():
                    
                    pass

          pass

