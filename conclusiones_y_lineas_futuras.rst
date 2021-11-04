Conclusiones y líneas futuras
=============================

Conclusiones
------------

Tras varios meses realizando el trabajo se han obtenido numerosas
conclusiones, tanto durante en el proceso de aprendizaje como
en el momento de la realización de análisis y la discusión de los
resultados.

Lo primero que resulta llamativo a la hora de introducirse en la
programación de sistemas que operen en tiempo real es la complejidad
que conlleva diseñar un software de este tipo. A la hora de diseñar la
arquitectura del sistema, es crucial que los componentes del
software mantengan una comunicación fiable que no se vea afectada
en gran medida por las perturbaciones que puedan existir en el
entorno del sistema y que la transmisión de información se ejecute
de una manera regular. Esto se consigue dividiendo la arquitectura
general en distintos niveles que se encargan del funcionamiento
de una sección específica de la comunicación.

En este sentido, ROS consigue unificar todas las partes que tratan
la información en un solo software para permitir al usuario centrarse
en el desarrollo de aplicaciones.

Por otro lado es reseñable la evolución que ha experimentado este
sector en los últimos años. Su comienzo se dio hace poco más de
una década y durante este tiempo se han realizado numerosos proyectos y
se ha locgrado desarrollar una segunda versión que incorpora una
gran cantidad de mejoras y que se actualiza constantemente con
nuevas distribuciones.

Esto muestra claramente el apoyo que existe hacia el sector y
las enormes previsiones que este posee de cara a un futuro
cercano.

En este sentido micro-ROS supone un gran avance para el sector. El desarrollo
de una variante del sistema operativo de robots que permite operar con dispositivos
de tan reducido coste se traduce en oportunidades para permitir que cualquier
persona pueda introducirse en el mundo de la programación de robots sin
necesidad de un gran presupuesto. Así mismo, resulta fascinante el modo en el
que, a pesar de no existir aún una gran cantidad de información en la web sobre el
desarrollo de aplicaciones en micro-ROS, este cuenta con una comunidad muy activa
que favorece a los usuarios menos experimentados. Durante la realización del
trabajo han ocurrido situaciones de bloqueo en las que ha sido necesario
utilizar información que apenas llevaba horas publicada en la red. Esto muestra
una idea del potencial y del margen de mejora que tiene a día de hoy.

En cuanto a la actuación del software, ha resultado muy interesante el hecho
de poder obtener unos resultados tan concluyentes empleando una aplicación
relativamente sencilla y una placa que actúa con unos recursos tan limitados.

De este modo, los análisis que se han discutido previamente muestran
una idea general del alcance de este software. Es cierto que numéricamente
hablando, pueda parecer que no cuenta con la potencia necesaria para
soportar aplicaciones que vayan a ser realizadas por robots en tiempo real.

Sin embargo, el gran potencial de estos sistemas no es el poder desarrollar
complejas aplicaciones para la monitorización de un gran robot, sino la facilidad
de poder fragmentar un gran sistema en distintos apartados que estén
controlados por dispositivos más modestos que sean diseñados específicamente
para la tarea que vayan a desempeñar.

Teniendo esto en cuenta, el proyecto realizado muestra unos resultados satisfactorios
que se resumen en como la complejidad de una tecnología tan avanzada se consigue
simplificar de tal forma, manteniendo unas prestaciones más que suficientes
para los objetivos para los que están diseñados la mayoría de microcontroladores.

Lineas futuras
--------------

Para los análisis que se han realizado en este trabajo se han seleccionado unos
parámetros y distintos escenarios. Estos nos muestran una idea bastante acertada
de como se comporta la placa. Sin embargo, existen muchos otras variables que no
se han medido que aportarían bastante información, como puede ser la latencia que
se produce en el transporte del mensaje desde el cliente al agente, la CPU que se
emplea en el proceso, etc.

Asimismo, sería muy interesante repetir los experimentos que se han realizado
teniendo varias placas conectadas como suscriptoras del topic. De este modo
se podría comprobar las características de la conexión en un entorno más
cercano a un posible escenario de la vida real.

Otro posible análisis podría centrarse en la comparación de resultados entre distintos
tipos de hardware o distintos RTOS. Esto resultaría muy útil a la hora de escoger
tanto la placa como el sistema operativo que la soporta.

Finalmente, cabe recordar que la ciencia que se ha estudiado está en pleno desarrollo
y sufre cambios constantemente, por lo que no sería de extrañar que de aquí a unos
pocos años, o incluso meses, se optimice la calidad de la conexión tanto de algunos
de los componentes que forman tanto el software como el hardware. En cualquier caso, es
muy probable que en un breve espacio de tiempo surjan numerosas mejoras. 