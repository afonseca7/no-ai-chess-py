#no-ai-chess-py

ajedrez codeado por mí sin usar ia. no por ser negacionista o estar en contra, sino puramente para mejorar mi lógica y medir mis capacidades.

no se nada sobre programacion orientada a objetos en python, asi que voy a ir buscandole la vuelta a medida que avanzo. Seguro termine estando mega hardcodeado, poco optimizado y poco legible peeero espero que algún día funcione.

---

## Sesión 1 — 7/5/26

#### ** 2:13 ** (inicio):  
* Búsqueda simple en documentación sobre clases, herencia, objetos, etc. 
* Mi objetivo ahora es crear algunos objetos y la matriz del tablero.

#### ** 4:32 ** (fin):

* tuve que leer documentación de POO en python, era logico
* crree la clase del tablero con el método para mostrar en terminal y que se inicialice con el método __init__.
* cree la base de las clases para las distintas piezas, pero dudo que este del todo bien. Tengo que verlo dsp.
* tengo que averiguar como crear una interfaz grafica más agradable que la terminal. Poder verlo bien seriviria y motivaria porque me dejaria ver mas cadaa avance.

##### lógica a resolver (Arquitectura de Movimiento)
Tengo que definir la cantidad de métodos "anidados" o secuenciales que necesito para procesar una jugada. El flujo lógico debería ser:

1. validar la forma de moverse de la pieza
2. validar que las coordenadas destino quedendentro de los límites del tablero
3. vlidar colisiones,  comprobar que en la ruta o destino no haya una pieza aliada.
4. validar estado, comprobar que el movimiento no deje en jaque al rey aliado
5. recien ahi, ejecutar el movimiento en la matriz

---

## sesion 2 - 7/5/26

### ** 13:25 ** (inicio):
Mi idea es en intento de una corta sesion poder investigar e implementar una interfaz de tablero, para salir de la interfaz de la terminal

### ** 16:40 ** (fin):
Consegui implementar la cuadricula y peones. Proximo a hacer es hacer visuales las demas piezas

## sesion 3 - 7/5/26

### ** 19:45 ** (inicio):
La idea es meter el resto de piezas con sus respectivas imagenes

## ** 21:20 ** (fin): 
No avance tanto, fue entre clases

---
## sesion 4 - 17/5/26

### ** 12:16 ** (inicio):
Mismo objetivo que sesion 3.

### ** 23:16 ** (fin): 
Tuve un monton de pausa, luego de las 12:16 no hice mas de 12:40, retome a eso de las 22:40.
Puse todas las imagenes e implemente el movimiento de los peones. y lo lleve a la interfaz, con prints de debug para ir viendo que todo funcione OK.
No hay sistemas de turnos (al menos por ahora). 

---
## sesion 5 - 24/6/26
### ** 21:05 ** (inicio):
objetivo de esta sesion es crear el sistema de turnos

### ** 21:32 ** (fin):
Creado con exito, si se intenta mover una pieza que no sea el turno, dice que el movimiento es ilegal porque no es su turno

---
## sesion 6 - 25/6/26
### ** 13:50 ** (inicio):
El objetivo de esta sesion es implementar el movimiento de la torre
### ** 14:01 ** (fin):
por percances personales debo finalizar la sesion antes de tiempo

## sesion 7 - 25/6/26
### ** 18:02 ** (inicio):
voy a continuar con el movimiento de los rooks, me lo imagino asi al aire como: 
si se mueve verticalmente: 
          1. un for desde la fila origen hasta la fila destino
          2. si la casilla no es none, se activa un flag o devuelve false, de esta manera bloquea el movimiento
si se mueve horizontalmente es lo mismo, pero en vez de fila columnas. 
De esta manera consigo checkear que este limpio el camino. 
Lo voy a hacer durante la clase, asi que existe la posibilidad de un avance reducido 

### ** 19:32 ** (fin):
la logica de las torres ya esta implementada.  

##  sesion 8 - 26/6/26
### ** 12:27 ** (inicio):
No tengo tanto tiempo, voy a iniciar con el movimiento de los bishops. Me lo imagino como: 
          1. debe moverse en valor absoluto la misma distancia en filas que en columnas. 
          2. Obtengo la direccion en x y la direccion en y
          3. recorro con un while? sumando la direccion en x y en y segun la direccion hasta llegar al destino. 
          4. si alguna casilla de entremedio no es None, despierta una alerta. 

### ** 13:42 ** (fin):
Empece con la logica del bishop, falta terminar.
Reconoci un bug en una situacion de juego del rook. Corregido. 

## sesion 9 - 26/6/26
### ** 17:51 ** (inicio):
espero poder finalizar con el movimiento del bishop.

### ** 18:31 ** (fin): 
bishop finalizado, intento comenzar con queen, que es la union de bishop con rook.

## sesion 10 - 26/6/2026 
### ** 19:53 ** (inicio):
espero finalizar con la reina. Si lo hago, comenzare con el rey o con el caballo.
### ** 20:25 ** (fin):
reina implementada. Falta el resto

## sesion 11 - 30/6/26
### ** 15:10 ** (inicio):
el objetivo es hacer que funcione el caballo. Supongo que la logica es que se mueva 2 en un eje y 1 en otro.  
 
### ** 15:25 ** (fin):
se que tiene fallos, pero es una prmera idea, tengo que acomodar las leyes de morgan para los != y los or. 
