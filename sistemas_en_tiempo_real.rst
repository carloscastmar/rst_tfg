Sistemas en tiempo real
=======================

Se dice que un sistema opera en tiempo real cuándo el tiempo que tarda
en efectuarse la salida es significativo. El tiempo de respuesta puede
ser relativamente flexible (tiempo real suave) o más estricto (tiempo
real duro), lo que se denomina software crítico.

La falta de respuesta en el tiempo establecido puede ocasionar graves
consecuencias para el entorno del sistema, llegando a producir daños a
la vida y a la propiedad.

Es por ello por lo que un sistema en tiempo real se diseña
específicamente para la tarea que ha de acometer, utilizando un hardware
y software dedicados.

El software empleado en sistemas de tiempo real cuenta con una serie de
características propias que garantizan el correcto funcionamiento del
sistema:

-  Sistema operativo en tiempo real: Los sistemas operativos en general
   tienen dos principales funciones, gestionar bien los recursos que
   proporciona el hardware y facilitar el uso del mismo al usuario. En
   este caso, los objetivos del sistema operativo en tiempo real son los
   mismos pero enfocados a las restricciones de tiempo y ocupar un
   tamaño reducido para que pueda aplicarse a sistemas embebidos.

-  Lenguaje de programación en tiempo real: Proporciona esquemas básicos
   como la comunicación y la sincronización entre tareas, el manejo de
   errores y la programación de funciones a realizar en tiempo real. El
   lenguaje C se ha utilizado ampliamente para este tipo de tareas
   debido a su facilidad de uso e interacción con el hardware. Sin
   embargo, otros lenguajes como Ada o Java se han desarrollado
   específicamente para este tipo de uso y cada vez tienen más peso en
   el sector.

-  Una red en tiempo real: Un sistema en tiempo real necesita una red
   que sea puntual y fiable en la transferencia de mensajes, para ello
   cuentan con un protocolo específico para trabajar en tiempo real
   proporciona una entrega puntual y garantizada de los mensajes a
   través de la red.

Las características principales de los sistemas en tiempo real son las
siguientes:

-  Cumplimiento en los plazos de ejecución: Es lo que distingue a este
   tipo de sistemas respecto al resto de sistemas informáticos.

-  Gran tamaño: Suelen ocupar mucho espacio tanto hablando de hardware
   como de software, cuyas librerías suelen estar formadas por una gran
   cantidad de lineas de código.

-  Previsibilidad: Han de ser capaces de prever cualquier tipo de orden
   que pueda ocurrir posteriormente para estar preparado y que no haya
   fallos en los tiempos de ejecución.

-  Seguridad y fiabilidad: Muchos sistemas de este tipo se encargan de
   controlar otros sistemas peligrosos en los que es de vital
   importancia la precisión, ya no solo en el tiempo de la ejecución
   sino en los movimientos del sistema.

-  Tolerancia a los fallos: Debido a la importancia del correcto
   funcionamiento de estos sistemas, deben estar diseñados para que un
   fallo en el propio hardware o software del mismo no repercuta
   drásticamente en el resto de componentes y operaciones que ejecute el
   sistema.

-  Concurrencia: El sistema tiene que ser capaz de cooperar con otros
   sistemas que estén operando en el mismo entorno y, en determinadas
   ocasiones, incluso utilizar el hardware o software de dichos
   sistemas.

Sistemas embebidos
------------------

La mayoría de sistemas utilizados en tiempo real son sistemas embebidos.
Estos son aquellos en los que el computador se encuentra integrado en el
sistema. Se caracterizan por no ser sistemas informáticos generales que
se programan para distintas tareas, sino que están diseñados para
cumplir un objetivo en concreto. Generalmente, un sistema embebido está
constituido por un microcontrolador y una infraestructura diseñada para
el propósito para el que está diseñado. El microcontrolador está
constituido por una unidad central (CPU), que se encarga de realizar la
mayoría de procesos, una memoria, que almacena las instrucciones y otro
tipo de datos que aseguran el correcto funcionamiento del sistema; y un
subsistema de entrada y salida, que suele contar con temporizadores,
convertidores de señales analógicas y digitales, y canales de
comunicación en serie.

Sistemas en tiempo real distribuido
-----------------------------------

Un sistema que trabaja en tiempo real distribuido está formado por unos
nodos autónomos que se comunican entre sí a través de una red que
trabaja en tiempo real y que cooperan para lograr unos objetivos comunes
en unos plazos determinados.

Estos sistemas son fundamentales debido a varias razones. En primer
lugar, la computación en tiempo real es esencialmente distribuida, ya
que se basa en la transferencia de información entre dos extremos
(nodos) a realizar en un tiempo determinado.

Seguidamente, la comunicación en tiempo real distribuido permite aislar
las partes del sistema e identificar fallos en el mismo evaluando los
nodos de la operación por separado. El cálculo realizado en cada nodo
debe cumplir con las restricciones de tiempo de las tareas, y la red
debe proporcionar un procesamiento en tiempo real con retrasos limitados
en los mensajes.

Además de esto, un equilibrio entre los distintos nodos del sistema
mejora el rendimiento del mismo.

Existen varios tipos de sistemas en tiempo real distribuido, sin
embargo, la arquitectura general de todos ellos es similar a la
siguiente:

|image0|

En la anterior figura se observa como todos los nodos están conectados
entre sí a través de la red de tiempo real, y a su vez, cada uno está en
contacto con distintas funciones propias que interactúan directamente
con el sistema.

.. |image0| image:: Pictures/1000020100000286000001DB702089A5741AD863.png
   :width: 4.2957in
   :height: 3.1917in
