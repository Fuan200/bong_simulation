# Pong Simulación

Este proyecto consiste en la implementación de un juego de Pong en Python utilizando la biblioteca Pygame. Pong es un clásico juego de arcade que simula una partida de ping-pong, donde dos jugadores controlan raquetas y compiten por golpear una pelota de manera que la otra no pueda devolverla. El objetivo de este proyecto es cambiar eso de que sean 2 jugadores y hacer que la máquina juegue sola.

## Requerimientos

1. Contador de Pelotas Perdidas

    * Incrementar en 1 el valor del contador cuando la pelota toque la parte inferior de la pantalla.

2. Contador de Número de Rally

    * Contar la primera colisión de la pelota con la raqueta, tomando en cuenta el contador de pelotas.
    *  Contar solo la primera colisión por cada número diferente en el contador de pelotas.

3. Contador del Largo del Rally

    * Contar cada colisión de la pelota con la raqueta sin aumentar el contador de pelotas.
    * Reiniciar este contador a 0 si el contador de pelotas perdidas aumenta.

4. Movimiento de la Raqueta

    * Permitir que la raqueta se mueva solo en la dirección horizontal `eje x`.

5. Velocidad de la Raqueta

    * Mantener una velocidad uniforme de la raqueta en todo momento.

6. Velocidad de la Pelota

    * Mantener una velocidad uniforme de la pelota en todo momento.

7. Ángulo de Rebote de la Pelota

    * Establecer el ángulo de rebote de la pelota en 45 grados.

8. Efectos de la Raqueta

    * La raqueta tiene 2 efectos al impactar con la pelota.
    * Si la pelota golpea el centro izquierdo de la raqueta, el ángulo es de -45 grados.
    * Si la pelota golpea el centro derecho de la raqueta, el ángulo es de 45 grados.

9. Ángulo de Salida de la Pelota

    * Establecer un ángulo de salida de la pelota de 45 grados al aparecer.
    * La dirección inicial de la pelota es aleatoria (izquierda o derecha).

10. Tamaño de Pantalla

    * La pantalla del programa debe ocupar el 75% x 75% de la pantalla total.

11. Cálculo de Velocidad de la Raqueta

    * La velocidad de la raqueta es igual al tiempo que tarda la pelota desde que aparece hasta que toca el piso, dividido entre dos.
12. Spawn Aleatorio de la Pelota en `x`

    * La posición inicial de aparición de la pelota en el eje x es aleatoria.

13. División en 2 Scripts

    * El programa debe dividirse en dos scripts:
    * Controlar el escenario y la pelota.
    * Controlar la raqueta y enviar instrucciones al primer script para que la raqueta intercepte la pelota.

14. Comunicación entre Scripts

    * Establecer una comunicación entre ambos scripts.

15. Información en el Segundo Script

    * El segundo script solo recibe información sobre la posición en x y el ángulo de la pelota cuando toca el techo y cuando rebota en la raqueta.

16. Tamaño de la Raqueta

    * Establecer el tamaño de la raqueta como 1/12 del ancho de la pantalla del juego.

### Lenguaje de Programación

- [Python3](https://www.python.org/)

### Comunicación entre los Scripts

- [Threads](https://docs.python.org/3/library/threading.html)

- [Sockets](https://docs.python.org/3/library/socket.html)

### Obtención de Números Aleatorios

- [Random](https://docs.python.org/3/library/random.html)

### POO

Si

### Infraestructura para el Juego

- [Pygame](https://www.pygame.org/news)

### Pruebas Unitarias

- [unittest](https://docs.python.org/3/library/unittest.html)

- [pytest](https://docs.pytest.org/en)

- [nose](https://pypi.org/project/nose/)

- [nose2](https://docs.nose2.io/en/latest/)

- [doctest](https://docs.python.org/3/library/doctest.html)

- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

## Fechas de Entrega

* Lunes 13: Saque de pelota y rebote pared.

* Miercoles 15: Movimiento de raqueta (con que se mueva de iz a der) ya con el segundo script y reconocimiento de las paredes.

* Lunes 20: Comunicación entre scripts; la información del saque la reciba el otro script, busqueda de la pelota.

* Miercoles 22: La raqueta debe golpear pelota; conteo de perdidas

* Lunes 27: Contar numero de rallis y largo de rallis

## Prerequisitos

- [Python 3](https://www.python.org/)

- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

- `Requeriments.txt`

## Uso 

1. Clonar el repositorio:

```
$ git clone git@github.com:Fuan200/bong_simulation.git
```

2. Crear un entorno virtual (recomendado, si no pasar al paso número 4), puedes cambiar el segundo `venv` por el nombre que se quiera:

```
$ python -m venv venv
```

3. Activar el entorno virtual:

* En Windows:

```
    venv\Scripts\activate
```

* En macOS and Linux:

```
    . ./bin/activate
```

4. Instalar dependencias:

```
$ pip install -r requeriments.txt
```

5. Para ejecutar el programa:

```
$ python main.py
```

## Autores

:blue_heart: **Denzel Alexander Muñoz Santana** - [Denzypaulito](https://github.com/Denzypaulito)

:blue_heart: **Juan Antonio Díaz Fernández** - [Fuan200](https://github.com/Fuan200)

https://refactoring.guru/design-patterns/observer/