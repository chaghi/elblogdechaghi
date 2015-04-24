.. title: Probando Beagle
.. slug: probando_beagle
.. date: 2005-10-22 18:29:20 UTC-03:00
.. tags: Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Finalmente, pude instalar y hacer andar `Beagle`_, que vendría a ser
algo similar a `Google Desktop`_, pero para Linux. Si no tienen idea de
que estoy hablando, muy resumidamente digamos que Beagle crea un índice
con toda la información de mi disco rígido, para luego poder realizar
consultas y encontrar rápidamente el documento, mail, conversación de
chat, MP3, imagen, o cualquier cosa que necesito. Pueden ver algunas
demos `entrando acá`_, dentro de la sección "Beagle Demos".

Hace rato que lo quería probar, pero siempre me "asustaba" en cierta
forma la gran cantidad de dependencias y de componentes core de GNOME (y
de Linux) que tenía que reemplazar por versiones más nuevas (menos
estables), y los numerosos reportes de que todavía es software alfa, que
tiene muchos memory-leaks, etc.

Hace unos días, empecé a usar Google Desktop en el laburo, y supongo que
eso me puso pilas para volver a echarle una mirada a Beagle. Y no fue
"tan" difícil. Por una lado, inotify (el componente que permite que
Beagle pueda monitorear los cambios en los archivos ni bien se producen)
es parte oficial del kernel 2.6.13 de Fedora Core 4 (la distro que estoy
usando), hace poco salieron nuevos paquetes de Mono, también para Fedora
Core 4, y Beagle está un poco más maduro.

Eso si: no hubo forma de instalar un RPM. O sea, instalar se instalaba,
pero el servicio de Beagle se iba de paseo, mal, a los pocos minutos de
arrancar, y no volvía. Ya me había rendido otra vez, cuando se me
ocurrió bajar el tarball con los fuentes y compilarlo yo. Y así anduvo
:)

No pude habilitar el servicio web (con lo cual no puedo ver los
resultados de búsqueda en un browser), pero bueno... tiempo al tiempo.

Tiene sus glitches, pero en general, está andando muy bien (convengamos
que Google Desktop está en beta, y también tiene sus glitches...). Me
impactó la velocidad de indexación: No tengo un análisis serio para
justificar lo que estoy diciendo, pero me da la sensación de que Beagle
indexó mucho, pero mucho más rápido mis archivos. Y aún corriendo la
indexación "intensiva", la PC era usable y todo con ese proceso en
background (supongo que esto es más mérito de Linux que de Beagle...).
La cantidad de archivos a indexar en casa es similar (al menos en orden
de magnitud...) a lo que indexé en el laburo, y el hardware también es
similar.

Ooootro tema: ¿Se dieron cuenta que parecidos son los logos de `Google
Desktop`_ y la `Provincia de Santa Cruz`_? Jeje... ¿quién se copió de
quién? :p

.. _Beagle: http://beaglewiki.org/Main_Page
.. _Google Desktop: http://desktop.google.com/es/about.html
.. _entrando acá: http://nat.org/demos/
.. _Provincia de Santa Cruz: http://www.santacruz.gov.ar/
