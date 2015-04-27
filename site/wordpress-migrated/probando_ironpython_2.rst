.. title: Probando IronPython 2
.. slug: probando_ironpython_2
.. date: 2009-03-01 13:11:08 UTC-03:00
.. tags: ironpython,net,Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Hace un tiempo vengo haciendo diversas pruebas con IronPython 2,
principalmente por sus mejoras en compatibilidad con CPython, y sus
mejores opciones de integración con VS (en particular VS 2008).

A partir de aquel `experimento que alguna vez comenté`_, en el laburo
decidimos usar `Cheetah`_ e `IronPython`_ como núcleo de nuestro
generador de código. Hace un tiempo había empezado a experimentar con
IronPython 2, y me dí contra la pared cuando descubrí que Cheetah (en su
momento el único *template engine* que encontré que andaba con
IronPython) ya no funcionaba del todo bien, y que además, era
*lentísimo*. Oportunamente reporté esto en `CodePlex`_, pero
básicamente parecía haber quedado en el olvido.

Los problemas de Cheetah en el peor de los casos podían salvarse con un
par de workarounds, pero implicaba tocar bastante código de nuestro
lado, y además caer en cosas no recomendadas por la doc de Cheetah. Así
que no era lindo. Pero además, lo de la performance era... intolerable.
Simplemente intolerable.

Así que seguimos usando IPy 1.1.

En los últimos días me hice de algo de tiempo para probar IPy 2.0.1, la
última release estable de IronPython. Y me encontré con 2 gratas
sorpresas:

-  Cheetah funciona otra vez *as expected*;
-  *parte* de los problemas de performance están resueltos;

Eso último, parcialmente: Lo que encontré es que usando IPy 2.0.1, el
generador de código funciona perfecto, y descontando la inicialización
de Cheetah, incluso es por lo menos un 30% más rápido que IPy 1.1. ¿Lo
malo? La inicialización de Cheetah es PATETICAMENTE lenta.

¿A qué le llamo "inicializar Cheetah"? A un simple

.. code:: python

   from Cheetah.Template import Template

Eso en CPython es *instantáneo*. En IPy 1.1 tarda *segundos* (más de 5",
y a veces hasta 10"), y en IPy 2.0.1 tarda el triple que en IPy 1.1 :(

¿Es un problema de Cheetah? No. Es un issue conocido en IronPython que
los module imports son lentísimos, y que a veces muchas de las mejoras
de performance de IronPython sobre CPython a nivel runtime se pierden
porque de pronto en medio de tu código tenés un inocente import que se
lleva el 80% del tiempo de ejecución. Una reverenda cagada. Mal.

IPy 1.1 tenía una opción *SaveAssemblies* que permitía guardar las DLL
que generaba el intérprete. Eso ayudaba un poco, aunque no mucho en el
caso de los imports. El tema es que esa opción no existe más en IPy 2.x.
Supuestamente, para IPy 2.x se estuvo trabajando en una precompilación
similar a la de CPython (algo parecido a la generación de .pyc), y por
más que el tema está mencionado en las release notes y todo, no logro
encontrar como cuerno se activa y/o usa y/o implementa eso. De todos
modos no tengo muchas esperanzas, porque leí en varios lugares que de
nuevo, en el caso de los imports, esta precompilación no aporta mucho,
pero en nuestro caso algo es algo, y me gustaría probarlo.

Dear lazy web, does anybody know how to test the "precompile" feature of
IronPython 2.x?

 

.. _experimento que alguna vez comenté: link://slug/exoditus_en_python
.. _Cheetah: http://www.cheetahtemplate.org/
.. _IronPython: http://www.codeplex.com/IronPython
.. _CodePlex: http://ironpython.codeplex.com/WorkItem/View.aspx?WorkItemId=17753
