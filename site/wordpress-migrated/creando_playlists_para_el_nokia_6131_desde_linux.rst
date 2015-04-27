.. title: Creando playlists para el Nokia 6131 desde Linux
.. slug: creando_playlists_para_el_nokia_6131_desde_linux
.. date: 2008-05-31 22:45:16 UTC-03:00
.. tags: gnokii,GNU/Linux,linux,nokia,playlists,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

El reproductor de música del Nokia 6131 es bastante pedorro. Básicamente
porque no ofrece una buena interfaz para navegar la colección de música.
Por practicidad, trato de replicar en la MicroSD del celu la misma
estructura de archivos que tengo en la PC y en la laptop, a saber:

::

    /Jukebox
    /Jukebox/Artista 1/
    /Jukebox/Artista 1/Album 1/
    /Jukebox/Artista 1/Album 2/
    /Jukebox/Artista 2/
    /Jukebox/Artista 2/Album 1/

... etc.

Con ese esquema, si le digo al reproductor que tome como carpeta base a
/Jukebox, me "aplana" toda la colección en una lista, ordenada como
puede. Donde el como puede depende de la metadata de los mp3, y del
orden en que se hayan copiado los archivos en la MicroSD.
Particularmente esto último, hace que la lista sea cualquiera,
especialmente si uno arrastra N carpetas con archivos de una al
teléfono, porque el orden en el que se escriben en el filesystem no está
garantizado.

Entonces la opción cuando quiero escuchar el album Foo del artista Bar,
es reconfigurar el reproductor para que tome solo esa carpeta. Pero esto
tampoco está bueno, ni es óptimo, porque:

-  Es lento navegar hasta la carpeta para seleccionarla;
-  Es lento el re-escaneo de los temas, particularmente si hay muchos
   archivos en la MicroSD (y como es de 1GB, normalmente hay muchos...)
-  No me soluciona el problema del orden. La lista me queda
   circunscripta a un artista/album, pero si los archivos que conforman
   el álbum no están en el orden correcto... alpiste.

¿Entonces? De acuerdo al manual del teléfono, y a las opciones que da el
reproductor en los menúes, todo parecía indicar que había \*algún\* tipo
de soporte para playlists. Pero por más que intentaba crearlas, no
encontraba como. Googleando un poco, encontré que sí, que hay soporte de
playlists, pero que no se pueden crear desde el teléfono. Son las
clásicas M3U, así que son fáciles de escribir, pero el teléfono no te
deja ponerlas en cualquier lado (bah, dejar te deja, pero el reproductor
de música no las reconoce). Tienen que estar en una carpeta especial
semi-oculta en la memoria del teléfono... y solo las podés crear con el
Nokia PC Suite, que es un software muy bueno y muy completo, pero del
cual no hay una versión para Linux. Ufa.

Googleando un poco más, terminé dando con varios posts de gente que
había encontrado donde se guardan las playlists, y daba pistas de como
copiarlas al teléfono con `gnokii`_ o gammu.

Resulta que una vez que juntás todas las piezas, no es tan complicado.
Por ejemplo, con gnokii:

-  La memoria del teléfono se accede como drive A:
-  Las playlists se guardan en A:\\predefgallery\\predefplaylist\\
-  La microSD es el drive E: `[1]`_
-  Además, las playlist (archivos .m3u) tienen que estar en formato DOS
   (terminación de línea de DOS)

En general, el soporte out-of-the-box de mi Nokia 6131 en Linux es
bastante decente. Cosas como conectarse via bluetooth, o con el cable
USB en modo "transferencia de datos", enviar y recibir archivos, están
perfectamente integradas y soportadas. Subir música al teléfono es
conectarlo (vía bluetooth o con el cable), y hacer drag&drop. Pero Nokia
con esto de obligar a que la playlist esté en la memoria del teléfono, y
siguiendo sus convenciones absurdas me caga, porque para acceder a la
memoria del teléfono, hay que caer en cosas como gnokii, que es software
hecho por geeks para geeks, y no es muy amigable ni para configurar ni
para usar. :(

Pero una vez configurado, y conociendo dónde y cómo hay que guardar las
listas, es relativamente sencillo, y hasta no debería ser tan complejo
escribir una linda GUI que permita seleccionar archivos en la tarjeta de
memoria, crear una .m3u para los mismos, y subir la lista a su cornudo
directorio-secreto-oh-nokia-eres-tan-brillante.

Hasta que tenga tiempo de encarar la GUI, por ahora me `armé un script
en python`_ que a través de gnokii lista un directorio en particular de
la MicroSD, y escupe por stdout la lista de temas que encuentra en ese
directorio en formato m3u, y ordenada por nombre de archivo.

Ejemplo:

.. code:: console

   $ nokia_m3u.py  "E:/Jukebox/Mikael Bolyos/A Family Affair" > "A Family Affair.m3u"

Y después tengo que subir la playlist a su directorio especial:

.. code:: console

   $ gnokii --putfile "A Family Affair.m3u" "A:/predefgallery/predefplaylist/A Family Affair.m3u"

Es bastante directo, pero si escribiera una GUI para arrastrar los
archivos y grabar la .m3u en el teléfono directamente desde ahí, estaría
mucho mejor. Veremos si invierto tiempo en eso...

[1] Jugando un poco más con gnokii descubrí que la microSD
también puede accederse como drive B: (parecerían ser sinónimos), pero
como Nokia PC Suite crea las .m3u usando E:... decidí respetar eso. Y la
memoria del teléfono también es visible como drive C:

 
.. _gnokii: http://www.gnokii.org/index.shtml
.. _[1]: #update
.. _armé un script en python: /blog/files/nokia_m3u.py
