.. title: Ubuntu 9.04 - Jaunty Jackalope
.. slug: ubuntu_9-04_-_jaunty_jackalope
.. date: 2009-04-25 15:56:28 UTC-03:00
.. tags: GNU/Linux,review,Software,ubuntu
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Terminé de migrar a `Jaunty`_. Esta vez, fue una experiencia diferente.
Tenía intenciones de hacer un clean-install, manteniendo mi $HOME y mi
/opt, que están en particiones independientes. Siempre termino usando el
CD "alternativo", porque mis particiones están sobre `LVM2`_, y
`Ubiquity`_, el instalador de la versión Desktop no lo soporta.

Resulta que anoche iba a quemar el .iso... y me encuentro con que no
tenía ni un CD virgen. Últimamente estoy volviendo a micro-blogguear
bastante en `Twitter`_, y desde hace poquito también en `Identi.ca`_, y
cuando postié "`Iba a aprovechar el release de Jaunty para hacer un
clean install, y me acabo de dar cuenta que no tengo ni un CD para
quemar el .iso`_\ ", bugabundo, alguien que ni conozco y que no es un
follower directo mío en identi.ca me respondió "`@chaghi do you have a
USB stick? you can use that!`_\ ".

Eso motivó un par de intercambios en identi.ca con este flaco, con un
poco de google en paralelo, y un ratito después había aprendido lo
siguiente:

-  Hay *algo* en identi.ca que evidentemente permite que pongas en tu
   "radar" determinadas keywords o tags o algo y eso hace que te enteres
   de determinados posts aunque no seas suscriptor del usuario. Hay todo
   un manejo de tags y grupos en identi.ca sobre el que tengo que
   investigar un toque;

-  *La herramienta Sistema -> Administración -> Creador de discos de
   arranque USB* que Ubuntu tiene desde hace un par de versiones te
   automatiza el proceso de hacer booteable un USB, y meterle el
   contenido de un .iso (normalmente, correspondiente al CD de
   instalación de Ubuntu) para poder arrancar, instalar, o probar desde
   ahí. Es automágico, no es destructivo (i.e., no te borra lo que ya
   tengas en el pendrive), y hasta te sugiere reservar una especie de
   micro-partición en el USB para hacer persistentes los cambios, onda
   que luego si arrancás con el pendrive, y guardas un archivo en tu
   Escritorio, por ejemplo, lo estás persistiendo en el USB, y no en RAM
   como sucede normalmente con el LiveCD.

-  El Desktop CD tiene *algo* de soporte para LVM. En particular, la
   herramienta de particionado manual de Ubiquity NO puede crear
   volumenes LVM nuevos, ni te deja tocarlos mucho, pero si está
   preparada para reconocer a los que existan, y usarlos en la
   instalación.

Así que por primera vez en la vida, decidí bajar el Desktop CD en lugar
del Alternativo, e instalar con Ubiquity. En mi caso, y por este tema de
tener LVM en el medio, hay dos detalles a tener en cuenta:

No puedo arrancar el instalador directo desde el menú de arranque. Tengo
que bootear la version Live de Ubuntu, instalar lvm2 (¿que les costará
meterlo por defecto en el CD?), activar mis volumenes LVM, lanzar
Ubiquity, instalar seleccionando particionado manual, y a lo último NO
REINICIAR. Antes, debo hacer un chroot a la instalación en disco, e
instalar lvm2 también ahí, ya que Ubiquity NO lo instala.

Es un poco tricky, no es algo que le recomendaría a mi madre, pero
digamos que si estoy usando LVM2 es porque no soy precisamente un
newbie, así que el workarround tampoco es terrible.

Después de todo eso, llegué a las siguientes conclusiones:

-  Realmente no tiene sentido hacer el "Upgrade" de una versión a otra.
   El Upgrade tarda muchísimo más que una instalación limpia, aún
   tomando los paquetes base desde el CD. Mucho más. Un Upgrade es un
   proceso de un par de horas, a veces más, mientras que instalar Ubuntu
   con Ubiquity lleva algo así como 20'/30'. Nada que ver. Ok, parte del
   tiempo del upgrade es tiempo que con un clean install perdés después
   bajando soft adicional (más sobre esto luego)... pero igual.

-  El Upgrade tiene la ventaja de que preserva los datos, pero teniendo
   particiones independientes... es lo mismo. Usás la misma partición
   para tu $HOME, le decís al instalador que no la formatee, y ya. La
   otra ventaja del Upgrade es que tiene cierta heurística de migración
   que hace que si algún default cambió, y vos tenés todavía el default
   anterior (y no un setting custom), te pone el nuevo default. Al hacer
   un clean-install eso no lo tenés, y a veces tenés que luego jugar un
   poco con las configuraciones para activar un feature nuevo que de
   otro modo no ves porque está "tapado" por una configuración legacy,
   digamos, pre-existente en tu $HOME.

-  El Upgrade no solo preserva datos en tu $HOME, sino system-wide, con
   lo cual cualquier cosa que hayas toqueteado en por ejemplo /etc,
   también se mantiene. Pero hacer un backup de /etc es trivial, y pisar
   luego en la instalación nueva los 2, 3 o 4 archivos que al menos en
   mi caso podés llegar a tener con configuraciones extra, es también
   trivial. Si fuera un server sería más complejo, obvio, pero al menos
   en la laptop... hacer rato que me vengo apegando a las
   configuraciones por defecto, y de última a centralizar cualquier cosa
   custom dentro de mi $HOME, y no como algo global.

-  Por último, el Upgrade preserva todo tu software extra, y te lo
   actualiza, mientras que si hacés un clean-install, todo lo que no
   provee el CD y tenías instalado, tenés que volver a bajarlo. Pero no
   me jode. El tiempo de downloading a la larga es el mismo, y a su vez
   ayuda a cada 6 meses PENSAR si vale la pena volver a instalar ese
   programa que habías instalado para probar algo, y lo ejecutaste solo
   una vez ese día y nunca más...

¿Conclusión? Dudo mucho que vuelva a usar el Update Manager de Ubuntu
para hacer una actualización completa de la distribución. Me parece que
me acabo de hacer fan de los clean-installs.

Ahora, respecto a Jaunty:

Arranca notablemente más rápido que Intrepid y las versiones anteriores.
Parece un sistema operativo del siglo XXI corriendo en hardware
medianamente nuevo y todo :) ¡Bien ahí! Parece una boludez, pero una de
las cosas que más me estaba hinchando las pelotas de Intrepid es que el
arranque se tomaba un minuto o más hasta el login screen, y luego otro
tanto para levantar Gnome. Ahora en menos de un minuto ya estoy
laburando.

Tengo una relación de amor-odio con el nuevo Notify-OSD. Si, es sleek.
Se ve re-lindo. Pero las notificaciones desaparecen rapidísimo, a veces
te las perdés, no todo el soft está usando ese esquema.

El OS en general se nota mejor en performance, excepto en la parte de
video, por ciertas regresiones en los drivers de Intel. La verdad se
notan. Hay algunos workarrounds experimentales para eso (como habilitar
UXA), pero dicen que es a costa de estabilidad... así que ni probé.

El look-and-feel de Ubuntu la verdad ya me aburrió. Los community-themes
que ahora se incluyen como alternativas (Dust, Dust-Sand, etc) están
buenos, pero tienen muchos detalles. Cositas acá y allá que no se ven
bien, o aplicaciones a las que no les gusta y cosas así. Y sí, hay BOCHA
de themes para Gnome, pero la verdad... todos tienen detalles, y encima,
todos tienden a copiar a Vista, o a copiar a OS X. A la larga, el más
pulido es el default, así que volví a Human. Pero estoy aburrido de
Human. Espero que para Karmic hagan algo piola y DIFERENTE. Realmente
espero que Canonical le pague a un grupo de designers profesionales para
que hagan algo lindo, usable, pulido, pero que a su vez se vea como
Ubuntu, tenga identidad propia, y no parezca un clon barato de Vista u
OS X.

Jaunty ya tiene soporte para ext4. Aún no es el filesystem por defecto,
pero ya que estaba reformateando la partición root, esta quedó en ext4.
Cero problema. Y quizás eso esté contribuyendo en parte a las mejoras en
el booteo.

El tiempo de inicialización de Gnome se arregló. No se que tenía mi
profile, que tardaba un montón. Y si me logueaba con otro usuario con un
$HOME "limpio", era mucho más rápido. Por un lado le sospechaba a la
encripción; por otro, a algún software adicional. Pero el tema es que no
toqué mi $HOME, reinstalé básicamente el mismo soft que tenía (al menos
en cuanto a los que están colgados del inicio de sesión de Gnome), y
mantuve exactamente la encripción, y sin embargo los 30"/45" que después
del login se perdían con el disco andando a full haciendo vaya uno a
saber que cosa que nunca pude identificar, hasta que aparecían los
paneles, se fue. ¡Bien!

All in all, so far I'm a happy Jaunty Jackalope user.

 

.. _Jaunty: http://www.ubuntu.com/products/whatisubuntu/904features/
.. _LVM2: http://es.wikipedia.org/wiki/LVM
.. _Ubiquity: https://launchpad.net/ubiquity
.. _Twitter: http://twitter.com/chaghi
.. _Identi.ca: http://identi.ca/chaghi/all
.. _Iba a aprovechar el release de Jaunty para hacer un clean install, y me acabo de dar cuenta que no tengo ni un CD para quemar el .iso: http://identi.ca/notice/3689643
.. _@chaghi do you have a USB stick? you can use that!: http://identi.ca/notice/3689660
