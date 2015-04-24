.. title: Alocado Alocador
.. slug: alocado_alocador
.. date: 2006-06-26 00:08:50 UTC-03:00
.. tags: Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Con algunos miembros de `PyAr`_ (alecu, dave, lucio, facu, nubis y yo)
armamos un equipo para participar del desafío `Pygame.draw`_, organizado
por la misma gente de `PyWeek`_, que básicamente consistía en hacer un
juego en menos de 64Kb de código Python, usando SOLAMENTE pygame y la
librería estándar, sin recursos externos.

El resultado es `Alocado Alocador`_, un juego en el que tenemos que
"administrar" la memoria, ubicando en la misma los bloques de memoria de
los procesos que van apareciendo en una cola. La idea es hacerlo rápido,
porque si se tarda en ubicar los bloques, el sistema se vuelve menos
responsivo, y el usuario va perdiendo la paciencia. Cuando la paciencia
del usuario se agota... perdemos. Hay algunas variables más en el juego
(la verdad, quedó divertido!), pero les propongo bajarlo y enterarse
jugándolo y leyendo la ayuda.

En unos días iremos completando seguramente la página wiki del proyecto
con algo más de info. El juego puede bajarse `acá`_, y necesita
unicamente el intérprete de Python y la librería `pygame`_.

Fue muy divertido participar en este desafío... si bien me faltó tiempo
y recién me pude enganchar a full estos últimos dos días. El finde me la
pasé probando el juego, discutiendo cambios, tocando algo de código, y
sobretodo, "afinando" el mini-sintetizador que hizo alecu para tocar las
melodías, y transcribiendo archivos MIDIs a la notación de ese
sintetizador para ponerle música a la cosa.

Ahora nos queda esperar el resultado de la competencia... estuve jugando
el resto de los juegos enviados, y la verdad... ¡tengo esperanzas!

.. _PyAr: http://www.python.com.ar/moin
.. _Pygame.draw: http://media.pyweek.org/static/pygame.draw-0606.html
.. _PyWeek: http://www.pyweek.org/
.. _Alocado Alocador: http://www.python.com.ar/moin/Proyectos/AlocadoAlocador
.. _acá: https://opensvn.csie.org/PyAr/pydraw2006/release/
.. _pygame: http://www.pygame.org/download.shtml
