.. title: Aprendiendo erlang
.. slug: aprendiendo_erlang
.. date: 2007-09-15 13:24:11 UTC-03:00
.. tags: erlang,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Hace un par de semanas atrás, empecé a leer un poco documentación y
tutorials de `erlang`_. Instalé en mi laptop la `implementación open
source`_, y estuve practicando.

Nada fancy, nada útil per-se. Estoy apenas escarbando la superficie,
para ver algo concreto de programación funcional (algo que tenía
pendiente hace rato). Y elegí erlang porque dentro de los otros
lenguajes funcionales (o pseudo-funcionales) que miré encontré que tiene
una sintaxis clara. Y tiene algunos pythonismos:

-  tiene un intérprete interactivo (tener un intérprete interactivo es
   LO MAS!)

-  tipado dinámico

-  evaluación estricta

-  asignación única (esto para mí era importante, porque realmente
   quiero probar como es programar SIN depender de cambios de estado
   para expresar la lógica (creo que es el click-mental más costoso para
   pasar a hacer algo funcional...))

Por otro lado, si bien es relativamente "viejo" (si se puede decir viejo
sobre un lenguaje de programación...), últimamente viene ganando
terreno. Quizás porque algunas singularidades son más útiles o fáciles
de explotar ahora. Y esas singularidades de erlang también ayudaron a
que terminara siendo "el elegido" para esta prueba: El lenguaje
incorpora en sí mismo todo lo necesario para programación concurrente,
ejecución en paralelo, ejecución distribuida, pasaje de mensajes, rule
matching, de una manera sumamente simple y completamente integrada al
core del lenguaje.

Hasta ahora me viene resultando un experimento interesante, sobretodo
porque acostumbrado a lenguajes procedurales y orientados a objetos, es
un desafío a veces expresar las cosas más sencillas cuando el paradigma
es funcional.

Con todo esto ni quiero decir que me vaya a dedicar a desarrollar en
erlang ni mucho menos... pasa que la "pata" de paradigma funcional me
está faltando, y me parece que la mejor forma de incorporarla es jugar
un rato con un lenguaje 100% funcional. Después, es más fácil volver a
otros lenguajes y aplicar esas "lecciones aprendidas" a la resolución de
los problemas, aún en casos en que el lenguaje en sí no soporte el
paradigma. Se trata solamente de poder incorporar otro enfoque, otro
punto de vista, que a veces es más eficiente / útil.

Y calculo que una vez que tenga más en la cabeza estas cosas a partir de
elrang, va a ser más fácil echarle una mirada a otras opciones (como por
ejemplo, `Haskell`_) de las que huí despavorido por su horripilante
sintaxis (ok, no le puse mucho esfuerzo de mi parte en darle una
oportunidad, pero... ¿para qué el masoquismo, teniendo erlang?)

Algunos links que me resultaron útiles al principio:

-  `An introduction to erlang`_: Este está recién salido del horno, pero
   lo pongo primero porque lo leí ayer y es un excelente paneo de las
   cosas más significativas

-  `Quick start`_ 

-  `Curso en 5 módulos`_: Lo acabo de empezar, bajando el `pdf`_.

 

.. _erlang: http://es.wikipedia.org/wiki/Erlang
.. _implementación open source: http://www.erlang.org/
.. _Haskell: http://es.wikipedia.org/wiki/Haskell
.. _An introduction to erlang: http://www.onlamp.com/pub/a/onlamp/2007/09/13/introduction-to-erlang.html
.. _Quick start: http://www.erlang.org/faq/quick_start.html
.. _Curso en 5 módulos: http://www.erlang.org/course/course.html
.. _pdf: http://www.erlang.org/download/course.pdf
