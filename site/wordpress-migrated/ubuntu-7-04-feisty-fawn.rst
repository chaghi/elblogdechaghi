.. title: Ubuntu 7.04 - Feisty Fawn
.. slug: ubuntu-7-04-feisty-fawn
.. date: 2007-04-24 17:47:25 UTC-03:00
.. tags: GNU/Linux,review,Software,ubuntu
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Terminé mi serie de upgrades de Ubuntu 6.10 a 7.04, los cuales son
esencialmente 2 :p (mi desktop y mi laptop).

Creo que con este upgrade terminé de aprender, o de convencerme, que una
línea de ADSL 256 **NO** es apta para actualizar un OS completo. Es MUY
lento, y el upgrade es un proceso "atómico", en cuanto implica la
descarga de centenas de archivos, y cuando la ventana de actualización
es de más de 8hs, hay muchas cosas que pueden salir mal. Y el upgrade no
es un proceso que sea cancelable/resumible así nomás.

Con el desktop, me pasó que últimamente vengo con problemas de
temperatura, y se apaga. La semana pasada cambié la fuente, que estaba
andando decididamente mal, y supuse (parecía) arreglado. Bueno, no :( El
sábado a la tarde inicié el proceso de upgrade vía internet, y seguí con
mis cosas. A la noche, cuando volví a casa, seguía descargando. El
domingo a la mañana, la PC estaba apagada. Damn. Y lo que es peor, ya no
booteaba. Se apagó en medio de la instalación, no del download, con lo
cual, mitad de los paquetes estaban actualizados/instalados, mitad
estaban desconfigurados pendientes de instalación, un desastre.

Pero, esto es GNU/Linux, y el upgrade no hace nada de magia negra... tan
solo baja los .deb nuevos, y luego, ejecuta una enooooooorme transacción
de apt que los instala/configura. Así que lo que hice fue iniciar con el
Live CD de Ubuntu 6.04 (Dapper Drake), montar mi partición root de
disco, hacer un chroot, y reiniciar la configuración de paquetes
pendientes. Eso anduvo... a medias. Es que por desconocimiento, no monté
los filesystems ``/proc`` y ``/sys``, y la mitad de los scripts de
post-instalación fallaban por eso. Después de innumerables intentos,
llegué a un entorno chrooteado "sano", y pude terminar.

Si te pasa lo mismo, la secuencia de pasos correcta sería, desde una
consola del LiveCD:

.. code:: console

   $ sudo mkdir /target
   $ sudo mount /dev/mapper/lv_root /target   #reemplazando /dev/mapper... por el dispositivo que contenga el filesystem root 
   $ sudo mount /dev/hda2 /target/boot #opcional, solo si tenés /boot en una partición independiente, y (obviamente) reemplazando /dev/hda2 por lo que corresponda en tu caso
   $ sudo mount -t proc proc /target/proc
   $ sudo mount -t sysfs sysfs /target/sys
   $ sudo modprobe dm-mod # opcional, si tenés un array o usás LVM2
   $ sudo chroot /target

y luego, desde el entorno chroot

.. code:: console

   # dpkg --configure -a # para terminar de configurar los paquetes que estén pendientes
   # aptitude update && aptitude upgrade && aptitude dist-upgrade
   # aptitude dist-upgrade # por las dudas...
   # apt-get -f install # también x las dudas...

y listo.

El otro tema, es que según como tengas la partición\ ``/boot``, desde el
``chroot`` puede verse diferente, con lo cual al instalarse las imágenes
del kernel, el menú del gestor de arranque puede quedar mal configurado.
En mi caso, quedaba con referencias a ``/boot/linux-image-...`` cuando
en realidad es ``/linux-image-...``

Antes de reiniciar por primera vez, conviene verificar en
``/target/boot/grub/menu.lst`` que todo esté ok.

Finalmente, anduvo todo joya. No perdí datos (obvio), y mejor aún, no
perdí configuraciones / customizaciones, y se actualizaron todos los
programas ok. Mi PC había quedado actualizada a Fesity Fawn. Se sigue
apagando después de 6 a 8 hs de funcionamiento continuo... pero por
supuesto eso no es problema de software.

En base a esa experiencia, para la laptop tomé un camino diferente: Bajé
la imagen ISO del CD alternativo de instalación, monté el ISO como si
fuera un CD (jeje... ni siquiera me tomé el laburo de quemar un CD
real), y disparé el Upgrade desde CD. Con eso, TODOS los paquetes base
ya los tenía de una, con lo cual, el instalador solo bajó de internet
las cosas accesorias (así y todo, fueron más de 250Mb de descarga). Pero
fue mucho más rápido / confiable. Y no tuve que embarrarme las manos en
una consola (ok, solo un poquitito, para montar el ISO, pero eso es solo
un comando... casi que no lo contamos, ¿no?)

Tarea cumplida. Mis dos compus están actualizadas a la última versión de
Ubuntu. Todavía no pude apreciar mucho las mejoras, más allá de lo que
es puramente look&feel (el artwork está más pulido).
