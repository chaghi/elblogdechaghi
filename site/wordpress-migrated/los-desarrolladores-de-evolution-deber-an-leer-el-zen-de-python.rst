.. title: Los desarrolladores de Evolution deberían leer el Zen de Python
.. slug: los-desarrolladores-de-evolution-deber-an-leer-el-zen-de-python
.. date: 2007-01-26 00:59:29 UTC-03:00
.. tags: GNU/Linux,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Desde que instalé Ubuntu en mi laptop que vengo tratando de hacer que
`Evolution`_ empiece a filtrar correctamente el correo basura. Como me
gusta más `bogofilter`_ que `spamassassin`_ (porque consume MUCHOS
menos recursos), activé el plug-in correspondiente, desactivando el otro
(spamassassin es el default). Además, instalé el paquete bogofilter, y
le di un curso rápido de spam vs. no spam alimentándolo con varios
cientos de mails "buenos" y mails "malos" que tenía guardados. O sea,
hice todos los deberes.

Y sin embargo, nada. Todos los días terminaba con el inbox lleno de
correo basura. Los primeros días no le dí mayor importancia, porque
bogofilter es un filtro estadístico, y necesita aprender. Pero...
después empecé a sospechar, porque primero que aprende RAPIDO, y por
otro lado, yo le había dado un "curso acelerado" de entrada.

Empecé a escarbar, y encontré que la base de datos que se va alimentando
con el correo basura no estaba siendo actualizada. Incluso si yo
manualmente marcaba un mail como spam, la base de datos seguía teniendo
el mismo tamaño, fecha y hora de modificación con los que había quedado
luego de mi importación inicial de mensajes.

Empecé a googlear para tratar de encontrar si a alguien le había pasado
lo mismo, y nada. Hay varios problemas con el filtro de spam en
Evolution, todos relacionados con que suele ser algo que por un motivo u
otro no anda bien de entrada, pero no encontré nada respecto a mi
problema específico.

Hasta que se me ocurrió correr a Evolution desde la línea de comandos,
para poder ver los mensajes que tiraba, si es que tiraba alguno. ¡Bingo!
Cada vez que yo marcaba un mensaje como spam, Evolution decía que no
podía ejecutar el filtro de spam porque no encontraba el programa
/usr/bin/bogofilter

¿Cuál era el problema? Que yo había instalado bogofilter-sqlite, la
versión de bogofilter que usa SQLite como backend para almacenar los
mensajes, en lugar de la versión que usa BerkeleyDB. Y el ejecutable de
esa versión es... /usr/bin/bogofilter-sqlite 

Fácil de arreglar. Solo tuve que crear un link simbólico y listo.
Pero...

No debería haber tenido que correr Evolution desde la línea de comandos
para enterarme que algo estaba fallando "por atrás". Si yo activé un
plug-in, y al disparar en la GUI un comando se ejecuta el plug-in, y el
plug-in falla porque no encuentra un archivo, **YO QUIERO VER UN ALERTA
EN LA GUI**.

`El Zen de Python`_, entre otras cosas dice:

    | Errors should never pass silently.
    | Unless explicitly silenced.

Sabias palabras Mr. Tim Peters. Muy sabias palabras.

(`Launchpad bug: #81581`_) 

.. _Evolution: http://www.gnome.org/projects/evolution/
.. _bogofilter: http://bogofilter.sourceforge.net/
.. _spamassassin: http://spamassassin.apache.org/
.. _El Zen de Python: http://www.python.org/dev/peps/pep-0020/
.. _`Launchpad bug: #81581`: https://launchpad.net/bugs/81581
