.. title: SiGeFi otra vez...
.. slug: sigefi_otra_vez
.. date: 2006-02-11 20:59:31 UTC-03:00
.. tags: Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Después de varios meses, hoy hice otra vez un par de *commits* en
`sigefi`_. Tras haber estado hiper-activamente involucrado en el
proyecto desde su inicio, y durante **todo** el desarrollo del core de
la aplicación, resultó que las múltiples complicaciones inútiles de
`wxWidgets`_ (el toolkit que elegimos para desarrollar la interfaz
gráfica) terminaron inclinando la balanza para el otro lado: de pronto
era mayor el tiempo que perdíamos luchando contra una estupidez, que el
tiempo que invertíamos logrando un resultado CONCRETO, visible, en la
aplicación.

Mi historia con wxWidgets es larga, y quizás algún día escriba sobre
ella, no lo sé. La cuestión es que `Facundo`_ quedó virtualmente solo en
el desarrollo, porque yo nunca más junté motivación suficiente para
tocar una sola línea de código. El core estaba hecho, y básicamente todo
el trabajo se limitaba a pelear con wxWidgets.

Por suerte, Facundo tiene **mucha** más paciencia que yo, y el proyecto
siguió adelante.

Ahora que la GUI está más madura, otra vez empiezan a aparecer
oportunidades de hacer cosas divertidas (al menos, divertidas para mí).
y entre ayer y hoy, romí el hielo arreglando dos pequeñísimos bugs,
retocando un detalle mínimo de la configuración, y... [trompetas] ¡hasta
volví a bucear por la documentación de wxWidgets! ¡y logré hacer lo que
yo quería!

Como siempre pasa con wxWidgets, perdí 3hs tratando de encontrar como
hacer lo que yo quería. Tres horas. Tres preciosas horas. Lo que yo
quería hacer, se resolvía con UNA miserable línea de código. Pero
wxWidgets tiene esas cosas: Al menos que ya seas un experto en el
toolkit, pareciera que la idea de sus desarrolladores es que pierdas tu
tiempo buscando en Google, en lugar de desarrollando. En fin.

Nada. Una mínima contribución a SiGeFi otra vez. Espero ir recuperando
la motivación, como para contribuir más seguido.

.. _sigefi: http://sourceforge.net/projects/sigefi
.. _wxWidgets: http://wxwidgets.org/
.. _Facundo: http://www.taniquetil.com.ar/plog/
