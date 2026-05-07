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
