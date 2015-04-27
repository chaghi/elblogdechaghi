.. title: IronPython pyc
.. slug: ironpython_pyc
.. date: 2009-03-08 18:21:47 UTC-03:00
.. tags: ironpython,net,Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Estuve investigando el supuesto camino de pre-compilar módulos para ver
si lograba resolver los problemas de performance que `mencioné hace unos
días`_.

Resulta que la punta del iceberg estaba escondida en el pack de
`ejemplos`_ de IronPython, que se descarga aparte. En ese paquete está,
entre otras cosas, el famoso pyc.py, parte de cuyo README nos cuenta:

    This sample demonstrates the use of the Python Hosting APIs to
    compile Python files into .NET executables.  The behavior of the
    generated files is actually quite similar to that of CPython files
    with the ".pyc" file extension.

Bueno, ni tanto. El script de ejemplo solo es un programita de consola
para compilar en bloque una serie de módulos, y generar un assembly.
Básicamente, es una interfaz al nuevo método CompileModules del CLR, y
hay una explicación bastante detallada de como funciona todo esto
`acá`_.

A menos que me esté perdiendo de algo, sinceramente no entiendo de donde
sacan que el funcionamiento de todo esto es "similar al de los archivos
CPython de extensión .pyc".

Veamos por que:

-  Explícitamente tengo que compilar los módulos. En CPython, esto es
   transparente.
-  Explícitamente tengo que indicar cual es el módulo que actuará como
   "entry point". En CPython, esto no es necesario.
-  Si compilo varios módulos, termino con un único assembly con todo. En
   CPython, cada .py genera su propio .pyc.
-  Pero lo más importante: Para usar el módulo compilado, tengo que
   cambiar los fuentes que lo consumen (importan). En CPython, el uso de
   los .pyc por parte del intérprete es completamente transparente.

El último punto es re-importante, y es la diferencia más grave. En
CPython, si tengo un módulo foo, en el archivo foo.py, lo importo así:

.. code:: python

   import foo

... y resulta que si ese módulo está pre-compilado en foo.pyc, es lo
mismo. Para mí no cambia nada. El intérprete agarra el .pyc. Y es más:
El intérprete se ocupa de determinar si el .py cambió (es decir, si el
.pyc ya no es válido).

En IronPython, al usar la compilación de módulos, y asumiendo que ya me
haya tomado el trabajo de generar foo.dll (lo que me están vendiendo
como "equivalente a un .pyc", para usar el assembly tengo que hacer
esto:

.. code:: python

   clr.AddReference("foo.dll")
   import foo

Y eso tiene varios problemas:

-  El código dejó de ser compatible con CPython (por el uso de clr)
-  Si alguien borra el assembly, el código pincha
-  Si foo.py sufre algún cambio, y nadie lo recompila, sigo levantando
   la foo.dll con el código viejo, y capaz ni me entero

Todo es más o menos workarroundeable: Podría tener un módulo clr "dummy"
que no haga nada en CPython, podría meter el AddReference en un
try/catch, podría crearme un modulito genérico que generalice toda esta
magia, e incluso se ocupe de verificar si el assembly debe ser
recompilado... pero no es el punto. Esto NO es lo mismo que un .pyc.

Anyway, estuve jugando con el esquema. Aplicarlo a algo como Cheetah es
muy complejo, porque está compuesto por muchísimos módulos. ¿Cuáles
compilo? ¿Todos? ¿Algunos? ¿Genero un solo assembly? ¿Genero un assembly
por cada módulo? ¿Cuál es la diferencia? La documentación oficial sobre
todo lo que tenga que ver con la compilación estática de scripts es
sumamente escasa, por no decir inexistente.

Lamentablemente, no llegué a ningún resultado útil. Si compilo Cheetah,
igual sigue tardando una bocha en importarse, y lo que es peor: ¡Después
no anda! Se importa aparentemente ok (tardando...), pero luego al usarlo
empiezan a producirse errores extraños, inesperados.

También noté que si compilo un programa de consola, tengo problemas por
ejemplo con sys.argv. En la versión compilada, pierdo los parámetros
(sys.argv es siempre ['']).

Conclusión: El esquema de compilación estática no es transparente, no
funciona igual que los .pyc de CPython, es más engorroso de usar, obliga
a cambiar el código fuente, no acelera la importación, e introduce
side-effects y errores inesperados.

Me parece que el equipo de desarrollo de IronPython debería volver a
leer el Zen de Python...

Mientras tanto, este esquema a nosotros no nos sirve. No solo no nos
resuelve la performance, sino que nos obliga a armar toda una magia para
implementarlo, y encima, después funciona a medias, o directamente no
funciona.

.. _mencioné hace unos días: link://slug/probando_ironpython_2
.. _ejemplos: http://ironpython.codeplex.com/Wiki/View.aspx?title=Samples
.. _acá: http://blogs.msdn.com/srivatsn/archive/2008/08/06/static-compilation-of-ironpython-scripts.aspx
