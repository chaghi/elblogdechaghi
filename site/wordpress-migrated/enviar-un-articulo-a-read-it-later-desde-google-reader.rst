.. title: Enviar un artículo a Read It Later desde Google Reader
.. slug: enviar-un-articulo-a-read-it-later-desde-google-reader
.. date: 2011-11-22 19:58:37 UTC-03:00
.. tags: bookmarklet,firefox,google,google reader,read it later,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Mi servicio preferido para llevar un registro de "cosas que encontré en
la web y que me quiero acordar de leer" es `Read It Later`_. Antes usaba
Instapaper, pero más que nada por un tema de soporte oficial en
celulares con Android, hace unos meses me cambié a Read It Later.

Hace rato que tengo configurado en la barra de marcadores de Firefox un
`bookmarklet`_ que me permite enviar a Read It Later la página que estoy
leyendo, y en general es lo que uso. El tema es que cuando estoy leyendo
un artículo en Google Reader, tengo que abrir el artículo en una
solapa/ventana nueva (para ir a la fuente original), y de ahí hacer el
envío.

Si bien Google hizo muchas cagadas con el rediseño de Reader de hace
unas semanas, hasta que le encuentre un reemplazo, lo sigo usando. Y
resulta que han hecho algunas cosas buenas. Por ejemplo: al pie de cada
artículo hay una opción de "Send to" que permite enviar la nota a
diferentes servicios. Desde la configuración de Google Reader se pueden
habilitar y deshabilitar que servicios queremos ver. Están los clásicos:
Twitter, Facebook, Tumblr, Digg... hasta está Instapaper, pero no está
Read It Later.

Si miran en la configuración al pie de los servicios disponibles, verán
que no todo está perdido. Google previó crear "sitios personalizados",
con lo cual es posible definir nuevos servicios. Y resulta que la gente
de Read It Later ya documentó como hacer para agregar su servicio a la
lista.

Hay que crear un enlace personalizado con la siguiente información:

::

    Name: Read It Later

    URL: https://readitlaterlist.com/save?url=${url}&title=${title}

    Icon Url: http://readitlaterlist.com/favicon.ico

... y listo, con eso aparece Read It Later como "sitio destino" dentro
de Google Reader, y se pueden enviar los artículos sin necesidad de
abrir la fuente original primero.

|Read It Later dentro de Google Reader|\ Fuente: `Add Read It Later to
Google Reader’s Send To Dropdown`_

Sí, ya se: hay una `extensión oficial para Firefox`_ que integra Read It
Later con el browser, pero, cuestión de gustos, personalmente prefiero
el bookmarklet antes que una extensión...

.. _Read It Later: http://readitlaterlist.com
.. _bookmarklet: http://readitlaterlist.com/bookmarklets
.. _Add Read It Later to Google Reader’s Send To Dropdown: http://readitlaterlist.com/blog/2009/08/add-read-it-later-to-google-readers-send-to-dropdown/
.. _extensión oficial para Firefox: http://readitlaterlist.com/firefox/

.. |Read It Later dentro de Google Reader| image:: /blog/wp-content/uploads/2011/11/readitlater-googlereader.png
