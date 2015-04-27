.. title: Cómo tener una consola de IronPython decente en Linux
.. slug: como_tener_una_consola_de_ironpython_decente_en_linux
.. date: 2007-09-30 22:39:18 UTC-03:00
.. tags: ironpython,linux,net,Python
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

IronPython, como buena implementación de Python, provee una consola
interactiva.

Tiene un gran problema: En linux, anda MUY mal. Al menos en Ubuntu,
desde gnome-terminal, suckea. Mucho. Pero que mucho. En Windows, anda un
poquitín mejor. Por ejemplo, uno puede apretar backspace y sucede esa
cosa mágica de borrar el caracter a la izquierda del cursor y todo!!! En
linux, por default, ni eso.

Este finde estuve por primera vez en varios meses usando en serio
IronPython, y si bien los ajustes finales de `este mini-proyecto`_ los
terminé sobre .NET en Windows, arranqué trabajando con Mono en Linux. Y
trabajar con Python con una consola que NO funciona, es desesperante. Me
cansé de googlear buscando soluciones... y no encontré nada. Mi última
búsqueda fue "ironpython console on linux sucks". Y para mi sorpresa, no
arrojó resultados significativos. Porque IT REALLY SUCKS! Al toque
empecé con mis teorías conspirativas, en la línea "claro, ahora que es
un proyecto de Microsoft, no nos importa como anda en Linux". Pero no
tenía sentido... porque debería haber una legión de usuarios de
Linux/Mono descontentos. Y si Google no los encontraba, ¿dónde estaban?
No cerraba. Evidentemente \*yo\* estaba haciendo algo mal.

Y ahí fue cuando entre tantas vueltas, descubrí que la consola de
IronPython se puede iniciar con una serie de opciones... y al toque 3
llamaron poderosamente mi atención:

::

   -X:AutoIndent        Automatically insert indentation 
   -X:ColorfulConsole   Enable ColorfulConsole 
   -X:TabCompletion     Enable TabCompletion mode

Si bien a priori no tenían que ver con mi problema (que es un manejo
absolutamente BROKEN de las secuencias de escape, movimiento del cursor
y demás), decidí probar. Y para mi sorpresa... no solo gané color,
tab-completion (bastante similar a la que ofrece `iPython`_) y
auto-indent... sino que con esas opciones se resuelven los demás
problemas!!! Fantástico. No se cual de las 3 hace la magia (sinceramente
no lo probé... se los dejo como tarea para el hogar) pero sospecho que
la opción salvadora debe ser -X:ColorfulConsole, que para manejar el
color debe usar otra librería para interactuar con la consola.

Así que ahora tengo en mi .bash\_aliases lo siguiente:

.. code:: bash

   alias ipy='ipy -X:AutoIndent -X:ColorfulConsole -X:TabCompletion'

... de manera que cuando ejecuto 'ipy' (el intérprete de IronPython), lo
hago con las opciones correctas. Y me pregunto por qué mierda esas
opciones no están activas por default, y/o por qué Ubuntu no las activa
por default. Porque la diferencia es ABISMAL.

Bonus-track: Esas opciones son también útiles en Windows. 

 

.. _este mini-proyecto: http://chaghi.com.ar/blog/post/2007/09/30/exoditus_en_python
.. _iPython: http://ipython.scipy.org/moin/About
