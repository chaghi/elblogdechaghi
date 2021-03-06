.. title: Haciendo que Ubuntu 7.10 se despierte bien
.. slug: haciendo_que_ubuntu_7-10_se_despierte_bien
.. date: 2008-02-10 01:00:39 UTC-03:00
.. tags: GNU/Linux,Software,ubuntu
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Hacía rato que tenía problemas con Ubuntu en la laptop con el soporte de
"Suspend to RAM".

Suspender, suspendía. El problema era al despertar. Pasaban 3 cosas:

-  La pantalla no se encendía. 

-  Me quedaba sin sonido. El control de volumen maestro quedaba
   silenciado, y además, se bajaba completamente el volumen PCM.

-  Me quedaba sin wifi. Mal. El dispositivo desaparecía, el led de la
   laptop quedaba apagado y no respondía a la combinación de teclas
   Fn+F2 para encenderlo, y NetworkManager determinaba que estaba solo
   en el mundo, sin ningún dispositivo que atender.

Lo de la pantalla tenía un workarround: apretar CTRL-ALT-F1 y luego
ALT-F7, o sea, conmutar a modo texto y volver a modo gráfico. Eso
terminaba de despertar al video. Feo, pero eran dos golpes de tecla. 

El tema del sonido, también tenía un workarround: Des-silenciar el
master, abrir el control de volumen, y volver a subir el volumen PCM. Me
hinchaba las pelotas, sí, pero se arreglaba con algunos clics del mouse.

El tema de la red wifi tenía un workarround HORRIBLE: reiniciar :(

Hace unos días me puse a investigar más a fondo. El objetivo primario
era hacer que funcione ok (i.e., que al despertar la laptop tuviera red
otra vez automáticamente); el premio consuelo que estaba dispuesto a
aceptar era encontrar que servicios reiniciar (y en que orden) para que
volviera a funcionar, y al menos no caer en reiniciar la máquina (que es
la salida típica en Windows, pero NO en Linux). 

Después de googlear bastante, la primera conclusión a la que llegué es
que todo "debería" funcionar bien; los problemas que estaba
experimentando eran típicos de hace un par de versiones atrás, pero no
de Ubuntu 7.10. Si bien no era el único que tenía estos problemas,
también era mucha la gente que reportaba que todo le funcionaba perfecto
"out of the box".

¿Entonces? Empecé a bucear en decenas de bug reports y threads en foros
y demás, probando tocar un archivo u otro (casi siempre,
``/etc/default/acpi-support``), para comentar una línea o descomentar
otra, o cambiar cierto parámetro... pero nada. El tema no se arreglabla.
Finalmente, terminé encontrando un post en un foro donde un usuario daba
la siguiente receta, al iniciar luego de un suspend:

-  parar el servicio de networking;
-  parar NetworkManager;
-  forzar la descarga del módulo del kernel correspondiente a tu placa
   wifi (en mi caso, ipw3945); 
-  volver a cargar el módulo;
-  iniciar networking;
-  iniciar NetworkManager;

Voilá!. Andaba. Y era suficientemente sencillo como para armar un
pequeño script que automatizara eso, cosa que terminé haciendo. Cada
vez que la laptop salía de un suspend, corría el script, y volvía a
tener red. Además, claro, tenía que seguir despertando "a mano" el video
y el sonido. Feo. Pero ya había dado un paso: No reiniciar.

Pero todo esto me dejó pensando... si todo se limitaba a reiniciar
servicios, ¿entonces por qué no andaba? ¿Por qué hay N personas a las
que no les andaba, y M personas a las que sí? Y entonces empecé a
confirmar la sospecha de que al fin y al cabo todo era producto de los
upgrades sucesivos de una versión de Ubuntu a la siguiente. Este tema
(el power management) hace un año y pico atrás tenía problemas. Ahora
estaban resueltos. Pero probablemente algo (vaya uno a saber qué...) no
había sido correctamente pisado, reconfigurado o reemplazado en alguno
de los upgrades, y por eso me seguía funcionando a medias.

Y decidí probar lo siguiente: La mayoría de las recetas para arreglar
estos problemas implicaban modificar el archivo
``/etc/default/acpi-support``. ¿Qué pasaría si eliminara COMPLETAMENTE
(incluyendo la configuración) el paquete "dueño" de ese archivo, y lo
reinstalara?

Ejecuté un

.. code:: console

   $ dpkg -S /etc/default/acpi-support

y me enteré que el archivo es parte del paquete ``acpi-support``. Probé
desinstalarlo, y APT me dijo "no! no podés desinstalar eso, porque el
paquete ``powermanagement-interface`` depende de ``acpi-support``".
Igual, decidí forzar la desinstalación ignorando las dependencias
(total, pretendía reinstalarlo inmediatamente después, con lo cual no
iba a quedar nada roto), pero ya que estaba metí en el trámite también a
ese otro paquete:

.. code:: console

   $ sudo dpkg --purge --force-depends acpi-support
   $ sudo dpkg --purge --force-depends powermanagement-interface

Listo. Con el ``--purge`` me aseguraba de haber eliminado también
toooooodos los archivos de configuración, y que por lo tanto al
reinstalarlos, se configurara todo de cero. A reinstalar:

.. code:: console

   $ sudo aptitude install acpi-support powermanagement-interface

Y listo! ¿Adivinen qué? Ahora anda todo 100% Ok. La laptop suspende
perfecto, y se despierta perfecto, con video, sonido y wifi.

Algunas moralejas de esta historia:

-  Por maravilloso que sea actualizar el sistema operativo "on the fly",
   de una versión a otra, es muy complicado que el proceso cubra el 100%
   de los detalles. Y esto se potencia cuando las actualizaciones se
   acumulan (yo ya voy por el 3er upgrade, y en un par de meses sale
   Hardy, e iremos por el 4to...)

-  Si algo no te anda, y a otras personas sí, y tu instalación no fue
   hecha desde cero, empezá a sospechar de que algo haya quedado mal por
   ese lado.

-  Si empezás a tocar acá y allá, y no obtenés resultados, y a la larga
   lo que estás buscando es la configuración "por defecto" en la que
   todo debería andar, empezá a preguntarte si no es mejor purgar
   completamente el componente de software en cuestión, y reinstalarlo
   para que se autoconfigure solito.

-  APT (el sistema de paquetes) es una joyita. Es fantástico poder
   llegar de un archivo a un paquete, poder desinstalarlo COMPLETAMENTE,
   incluyendo a la configuración, y que la reinstalación se ocupe de
   auto-configurar todo nuevamente.

-  Linux es fantástico por su modularización, y por permitir estas
   cosas. Ok, en un mundo ideal esto no debería pasar, y tampoco la
   solución es para cualquiera (no la veo a mi vieja por ejemplo
   siguiendo estos pasos), pero una vez ante el problema, prefiero mil
   veces lidiar con algo así en Linux, al que le puedo preguntar donde
   le duele (¡y me responde y todo!), que en Windows, donde no queda
   otra que recurrir a la `magia negra`_... o reinstalar TODO,
   ABSOLUTAMENTE TODO.

 

.. _magia negra: link://slug/magia_negra_con_el_regedit
