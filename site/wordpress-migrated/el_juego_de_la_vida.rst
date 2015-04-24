.. title: El Juego de la Vida
.. slug: el_juego_de_la_vida
.. date: 2004-10-31 02:36:43 UTC-03:00
.. tags: General
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

.. image:: /images/glider.png
   :alt: Emblema Hacker
   :align: center

Verán que en el panel de la derecha de la página, debajo de los links a
los validadores del `W3C`_, he colocado el emblema que encabeza este
artículo, el cual fue elegido por `Eric S. Raymond`_ para representar a
la `comunidad hacker`_. Antes de seguir, vale aclarar dos cosas:

-  El título de `hacker`_ se gana haciendo mérito en la comunidad, no es
   algo que uno adopte. Con lo cual, no me considero tal, no
   necesariamente pretendo serlo... aunque sí comparto muchos de sus
   valores (y por eso decidí incluir el símbolo en mi blog). En la
   página del emblema EsR comenta algo al respecto; y en este `how-to`_
   hay más información.
-  Ser hacker no es algo malo, ser hacker no implica cometer sabotajes
   informáticos, ni nada por el estilo. Sería muy largo explicar acá
   todo lo que significa ser hacker. Si estás interesado, leé el
   `how-to`_, consultá `The Jargon FIle`_, o leé los dos primeros
   capítulos del libro `The Art of Unix Programming`_.

Volviendo al tema que nos ocupa: El emblema representa a uno de los
patrones del `Juego de la Vida de John Conway`_ llamado glider. No tenía
idea lo que era, así que los últimos días estuve investigando al
respecto. El juego, extremadamente relacionado con conceptos de IA,
premite simular mediante reglas muy sencillas el ciclo de vida e
interacción de un conjunto de células. Es muy interesante. Nace por allá
por el '70, junto con Unix y la comunidad hacker, y aparentemente más de
un fanático se pasaba horas corriendo simulaciones, intentando descubrir
patrones especiales (y hablamos de la época en la que para sentarse
delante de una minicomputadora había que sacar turno). Todo este
contexto es el que llevó a EsR a pensar que el glider del Juego de la
Vida era un buen emblema para los hackers.

El juego (que formalmente es un `autómata celular`_ (el más famoso)),
fue ideado por el matemático británico `John Conway`_, y permite
apreciar como pueden generarse patrones muy complejos a partir de reglas
sumamente sencillas.

¿Y qué son los dichosos patrones? Resulta que hay agrupamientos
iniciales de células, que por su cantidad, disposición y las reglas
ideadas por Conway se comportan de una manera particular: Se deslizan,
'evolucionan' generando determinada figura, y muchas veces llegan a una
condición de equilibrio en la que el sistema queda estático: no nacen ni
mueren mas células. Glider es uno de los más sencillos, se desliza por
el ecosistema (tablero) al mismo tiempo que va mutando, y tiene la
particularidad de volver a su forma original cada 4 generaciones.

Como parte de la investigación, encontré un sitio donde se puede 'jugar'
on-line mediante un applet Java. La verdad que encontré varios sitios
parecidos, pero en particular me gustó éste porque están predefinidos
varios de los patrones iniciales mas interesantes (incluyendo el
glider). Además están explicadas las relgas por las que se rige el
comportamiento de las células. Si les interesa probarlo, entren a `John
Conway's Game of Life`_ (requiere Java).

Este post es un brevísimo resumen. En el texto desparramé links
suficientes como para que aquel que se sienta interesado, pueda buscar
información por su cuenta. Y nunca olviden que `Google`_ es su amigo ;)

¡Ah! Me olvidaba: EsR menciona que la idea de usar patrones de Vida como
emblema fue semi-anticipada por algunos hackers Argentinos :) (y pone
`esta imagen`_ de una remera como ejemplo).

.. _W3C: http://www.w3c.org/
.. _Eric S. Raymond: http://www.catb.org/~esr/
.. _comunidad hacker: http://www.catb.org/hacker-emblem/
.. _hacker: http://www.catb.org/~esr/jargon/html/H/hacker.html
.. _how-to: http://www.catb.org/~esr/faqs/hacker-howto.html
.. _The Jargon FIle: http://www.catb.org/~esr/jargon/html/online-preface.html
.. _The Art of Unix Programming: http://www.catb.org/~esr/writings/taoup/
.. _Juego de la Vida de John Conway: http://en.wikipedia.org/wiki/Conway's_Game_of_Life
.. _autómata celular: http://en.wikipedia.org/wiki/Cellular_automaton
.. _John Conway: http://en.wikipedia.org/wiki/John_Conway
.. _John Conway's Game of Life: http://www.bitstorm.org/gameoflife/
.. _Google: http://www.google.es/search?q=juego+de+la+vida+de+conway&start=0&start=0&ie=utf-8&oe=utf-8&client=firefox-a&rls=org.mozilla:es-ES:official
.. _esta imagen: http://swain.webframe.org/tshirts/conway_life_zoom.jpg
