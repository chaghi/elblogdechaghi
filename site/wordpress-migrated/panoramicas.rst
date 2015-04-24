.. title: Panorámicas
.. slug: panoramicas
.. date: 2006-06-13 03:15:12 UTC-03:00
.. tags: Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Después de mucho tiempo, me puse a instalar y probar con paciencia tres
herramientas con las que hacía rato quería experimentar:

-  `autopano-sift`_
-  `hugin`_
-  enblend

Son tres herramientas que se complementan para "pegotear" de una manera
inteligente fotos que están sacadas de forma consecutiva, para formar
una única imagen panorámica. Tenía un par de fotos sacadas así de mis
viajes... pendientes de pegar hasta el día que tuviera tiempo. Alguna
vez investigué un poco, y llegué a la conclusión de que éstas eran las
herramientas adecuadas, pero nunca las probé del todo, porque para
Fedora Core no tenía RPMs disponibles, y compilarlas no era muy sencillo
que digamos. Además, autopano-sift por ejemplo está desarrollado en Mono
(C#), y hasta no hace mucho, el toolchain de Mono no estaba muy maduro
(y menos aún en Fedora Core).

Ahora, con Ubuntu 6.06 LTS, tenía ya los paquetes para autopano-sift y
enblend. Solo tuve que compilar Hugin, lo cual no fue tan complicado.

El proceso funciona más o menos así: Autopano-sift toma las imagenes, y
calcula los puntos en común, guardando esta información en un archivo.
Luego, se carga este archivo en Hugin, se toma la info EXIF de las
imágenes (lo que proporciona metadata sobre lentes, distancia focal,
luz, etc.), se aplican algunos patrones automáticos de alineación, y se
reescriben las imagenes en formato TIFF, ajustadas, y con los datos
necesarios para unirlos. Por último, se usa enblend para hacer el
pegoteo final (Hugin también puede hacer este último paso, pero el
tutorial que seguí decía que enblend lo hace mejor y... ¿por qué no
creerle?)

El tutorial que estuve siguiendo es este: `Create a Panorama`_ (en
inglés), que está redactado por un chabón que a juzgar por los `ejemplos
en su página`_, sabe un rato de panoramas :)

La verdad que estos tres programitas son una masa. Se obtienen
resultados MUY buenos, como la foto que dejo de ejemplo al final de este
artículo, con fotos tomadas el año pasado durante la travesía
Lacar/Lolog. Es una vista del lago Lacar desde el Cerro Colorado. Está
armada uniendo tres fotos. Hagan click sobre la imagen para poder verla
y/o descargarla en tamaño real.

.. thumbnail:: /images/panorama.jpg
   :alt: Lago Lacar
   :align: center

   Lago Lacar

.. _autopano-sift: http://user.cs.tu-berlin.de/~nowozin/autopano-sift/
.. _hugin: http://hugin.sourceforge.net/
.. _Create a Panorama: http://exolucere.ca/articles/create-panorama
.. _ejemplos en su página: http://exolucere.ca/panoramas
