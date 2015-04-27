.. title: No más dual-boot en mi laptop (chau Windows!)
.. slug: no_mas_dual_boot_chau_windows
.. date: 2007-07-08 21:07:56 UTC-03:00
.. tags: dual boot,linux,Software,windows
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Hace unas semanas atrás comentaba que `estaba experimentando con
herramientas de virtualización`_, y que si todo iba bien probablemente
eliminaría la partición física de Windows XP Home, para usarlo solamente
en una máquina virtual. Hoy completé esa movida.

Finalmente, me decidí por VirtualBox. Está andando muy bien; probé
varias herramientas pesadas (SQL Server Express, Visual Studio Express,
...) y no tuve ningún problema. Alguna que otra vez la VM abortó, por
ejemplo, luego de mirar algún trailer en formato QuickTime de los del
sitio de Apple usando Firefox. Pero han sido casos aislados... si bien
la VM no debería abortar así de feo, me ha pasado colgar Windows
"nativo" esporádicamente también, así que no se hasta que punto la falla
es en la VM, o Windows se va al cuerno, y la VM no llega ni a dar un
mensaje de error y aborta. Anyway, no fue motivo suficiente para no
migrar.

Realmente esta configuración es más útil. De hecho, desde que estoy
usando Windows así, lo booteo un poquitín más seguido. Es como que la
barrera de dejar mi entorno de trabajo para iniciar otro OS
desaparece... puedo curiosear algo en Windows, y mientras tanto sigo
usando Ubuntu. E incluso los puedo tener en red, como si fueran dos
equipos. Así que incluso es más fácil compartir recursos entre ambos.
¿Qué pierdo? La aceleración 3D dentro de Windows. Pero como no uso
aplicaciones 3D en Windows, no me afecta. Y es algo en lo que todos los
productos de virtualización están trabajando (de hecho, algunas
versiones de VMWare y Parallels la soportan en ciertas
condiciones/plataformas), así que quien sabe... de acá a que lo necesite
(si es que llego a necesitarlo), quizás esté resuelto y todo. Por lo que
veo, es la única cosa que impide que el tema de la virtualización
despegue del todo fuera del mundo server, sobretodo por los gamers.
Porque por todo lo demás, es mucho más conveniente que un esquema de
dual-boot.

La movida terminó implicando comprar más RAM para la laptop. Si bien no
era imprescindible (con la RAM que tenía las cosas andaban), se notaba
que le estaba robando 512M de memoria al OS para correr otro... y como
la inversión en más RAM es algo que había quedado pendiente, y de todos
modos pensaba hacerla tarde o temprano, aproveché la "excusa". Después
de pedir un presupuesto a Dell (que básicamente me pasó un precio
absolutamente traído de los pelos), evaluar la posibilidad de comprar a
través de internet en el exterior, averiguar un poco en MercadoLibre, y
googlear otro tanto, dí con `Vulcano`_ (aka "Notebook Outlet"). La
experiencia de compra con esta gente resultó EXCELENTE: todo por
internet/e-mail, rápido, automatizado... un lujo. Recomendable. Y
(dentro de Argentina) resultó la alternativa con mejor precio.

Hoy dí el último paso, que fue borrar Windows, y reorganizar las
particiones en disco para que queden más prolijas. Ya había quedado
"rara", producto de que el esquema de particionado de Dell es raro, y yo
lo "manosié" para instalar Ubuntu. Además, con el agregado de RAM me
había quedado corto con la swap (y si bien con 2GB de RAM no swapeo
nunca, es importante para suspender el equipo). Así que me puse a
reorganizar.

El esquema que tenía, es este:

-  Partición primaria de DellUtility (47M)
-  Partición primaria de Windows XP (20G)
-  Partición Extendida (~55G)

   -  Partición boot de Ubuntu (100M)
   -  Swap de Ubuntu (1G)
   -  Volúmen LVM, conteniendo mis filesystems "/", "/home" y "/opt"
      (54G)

... y lo llevé a este:

-  Partición primaria de DellUtility (47M)
-  Partición primaria de boot de Ubuntu (200M)
-  Partición Extendida (~74G)

   -  Swap de Ubuntu (2G)
   -  Volúmen LVM, conteniendo mis filesystems "/", "/home y "/opt"
      (57G)
   -  Algo de espacio libre no asignado...  para pruebas y demás (15G)

A veces hay gente que me dice que tener `LVM`_ en un desktop o laptop es
demasiado... bueno, no. En situaciones como ésta, se paga solo el haber
transitado la (pequeña) curva de aprendizaje de saber manejarlo, y tener
mis datos en volúmenes LVM. Mover el boot y el swap de un Linux es
relativamente sencillo: Solo basta arrancar con algún LiveCD,
reacomodar, reconfigurar el gestor de arranque y listo. Pero mover de
acá-para-allá particiones con datos NO es tan trivial... salvo cuando
usás LVM :)

Si bien el cambio lo tuve que hacer en 4 o 5 etapas, moví TODO sin
perder los datos, sin tener que reinstalar, y sin tener que pasar los
datos transitoriamente a otro disco mientras "reacomodaba" las
particiones.  

Corolario: No más dual-boot, mi Windows XP Home corre virtualizado
dentro de Ubuntu, y ahora tengo suficiente RAM para jugar más cómodo con
esto de la virtualización. Por ejemplo, para cumplir el proyecto
largamente postergado de empezar a probar más temprano en el ciclo de
desarrollo las versiones alfa de Ubuntu, e involucrarme más en la
comunidad.

 

.. _estaba experimentando con herramientas de virtualización: link://slug/mundo_virtual
.. _Vulcano: http://notebookoutlet.com.ar/
.. _LVM: http://es.wikipedia.org/wiki/Logical_Volume_Manager
