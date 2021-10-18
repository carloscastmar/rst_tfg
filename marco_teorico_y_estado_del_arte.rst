Marco teórico y estado del arte
===============================

Sistemas en tiempo real
-----------------------

Se dice que un sistema opera en tiempo real cuándo el tiempo que tarda
en efectuarse la salida es significativo. El tiempo de respuesta puede
ser relativamente flexible (tiempo real suave) o más estricto (tiempo
real duro), lo que se denomina software crítico. :cite:`tiempo_real`

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

[1] Libro: Distributed real-time systems. Theory and practice

Sistemas embebidos
++++++++++++++++++

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
+++++++++++++++++++++++++++++++++++

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

.. figure:: Fotos/distributed_real-time_system_structure.png
    :width: 450px
    :align: center
    
    Arquitectura general de un sistema en tiempo real distribuido

En la anterior figura se observa como todos los nodos están conectados
entre sí a través de la red de tiempo real, y a su vez, cada uno está en
contacto con distintas funciones propias que interactúan directamente
con el sistema.

ROS
---

Definición
++++++++++

El ROS o Robot Operating System (sistema operativo de robots), es una
colección de frameworks para el desarrollo de software de robots. Un
framework es un entorno de trabajo tecnológico que se basa en módulos
concretos que sirve de base para la organización y el desarrollo de
software. :cite:`robot_operating_system`

.. figure:: Fotos/ROS.jpg
    :width: 300px
    :align: center
    
    Logotipo de ROS

ROS no llega a ser considerado un sistema operativo como tal, ya que
necesita de un software de nivel superior para ser utilizado. Sin
embargo, ROS provee los servicios básicos de uno, como son la
abstracción del hardware, el control de dispositivos de bajo nivel, la
implementación de funcionalidad de uso común, el paso de mensajes entre
procesos y el mantenimiento de paquetes. :cite:`que-es-ros`

Está basado en una arquitectura de grafos, esto es, una estructura
formada por nodos, o extremos del sistema, y un conjunto de arcos que
establecen las relaciones entre dichos nodos. Estas relaciones se basan
en recibir, mandar y multiplexar mensajes de sensores, control,
periféricos, etc.

La librería está pensada y diseñada para ser utilizada en un sistema
operativo UNIX (base del actual Linux), sin embargo, también se están
lanzando versiones experimentales para otros sistemas operativos muy
comunes como Mac OS X, Debian o Microsoft Windows.

ROS se divide en dos partes básicas. Por un lado, actúa como nexo entre
el usuario y el hardware (más similar a un sistema operativo
convencional) y, por otra parte, se comporta como una batería de
paquetes desarrollados por una comunidad de usuarios. Estos paquetes
implementan numerosas funcionalidades como la localización y el mapeo
simultáneo, la planificación, la percepción, la simulación, etc.

Historia
++++++++

ROS se desarrolló en 2007 bajo el nombre de switchyard por el
Laboratorio de Inteligencia Artificial de Stanford para dar soporte al
proyecto del Robot con Inteligencia Artificial de Stanford (STAIR) y al
programa de robots personales (PR), en los cuales se crearon prototipos
internos de sistemas de software destinados a la robótica. :cite:`ros_history`

.. figure:: Fotos/STAIR.png
    :width: 150px
    :align: center
    
    Robot con Inteligencia Artificial de Stanford (STAIR)

Desde 2008, el proyecto continuó principalmente en Willow Garage, un
instituto de investigación con más de veinte instituciones colaborando
en un modo de desarrollo federado, que proporcionó importantes recursos
para ampliar los conceptos ya creados y crear implementaciones sometidas
a varias pruebas.

El proyecto fue impulsado por una gran cantidad de investigadores con
mucha experiencia en el sector que aportaron numerosas ideas tanto al
núcleo central de ROS como al desarrollo de sus paquetes de software
fundamentales.

En un inicio, el software fue desarrollado utilizando la licencia de
código abierto BSD (Berkeley Software Distribution) y poco a poco se ha
convertido en una plataforma ampliamente utilizada en la comunidad de
investigación robótica.

Desde el principio, ROS ha sido desarrollado en múltiples instituciones
y para numerosos tipos de robots, incluidas aquellas que recibieron los
robots personales (PR2) directamente desde Willow Garage.

Cualquier persona puede iniciar su propio repositorio de código ROS en
sus propios servidores, y mantienen la plena propiedad y control del
mismo; además pueden poner su repositorio a disposición del público y
recibir el reconocimiento y el crédito que merecen por sus logros. De
esta forma también se fomenta la mejora del software ya existente con la
aportación de otros profesionales del sector.

Actualmente, el ecosistema de ROS cuenta con decenas de mies de usuarios
en todo el mundo, que trabajan en ámbitos que van desde proyectos
personales hasta grandes sistemas de automatización industrial.

Algunos de los robots que a día de hoy utilizan ROS son el robot
personal de Ken Salisbury en Stanford (PR1), el robot personal de Willow
Garage (PR2), el Baxter de Rethink Robotics, el Robot de Shadow en el
cual participan universidades españolas o el robot limpiador HERB de
Intel.

Proyección futura
+++++++++++++++++

El sistema operativo de robots ya cuenta hoy en día con una estructura
muy completa que proporciona al usuario múltiples posibilidades. Algunas
de las funcionalidades que engloba este software a día de hoy son la
creación, destrucción y correcta distribución de nodos en la red, la
publicación o suscripción de flujos de datos, la multiplexación de la
información, la modificación de los parámetros del servidor y el testeo
de sistemas.

A pesar de la gran cantidad de servicios que ya ofrece, se espera que en
futuras versiones se incorporen algunas de las siguientes
funcionalidades a las aplicaciones de ROS: identificación y seguimiento
de objetos, reconocimiento facial y de gestos, la comprensión del
movimiento, el agarre y la egomoción, entre muchas otras.

Como se ha podido comprobar, esta tecnología ha avanzado enormemente
durante los últimos años, y se prevé que este auge se maximice en los
próximos años, desempeñando un papel fundamental en la revolución de la
industria 4.0 y el fenómeno conocido como “el internet de las cosas”.
:cite:`ros_rolling`

.. bibliography::
   :style: plain
