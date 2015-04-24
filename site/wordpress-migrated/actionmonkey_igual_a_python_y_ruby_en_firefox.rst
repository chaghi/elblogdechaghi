.. title: ActionMonkey == Python y Ruby en Firefox
.. slug: actionmonkey_igual_a_python_y_ruby_en_firefox
.. date: 2007-08-01 15:52:13 UTC-03:00
.. tags: Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Acabo de enterarme de un proyecto de Mozilla, `ActionMonkey`_, que
cuenta con el apoyo de Adobe, que es la fusión de otros dos proyectos
que no sabía que estaban en danza: `Tamarin`_ y `SpiderMonkey`_. ¿Y para
qué tantos proyectos y siglas? Para lograr que en un futuro, se pueda
usar IronPython e IronRuby (las implementaciones .NET de Python y Ruby),
de la misma forma que hoy se usa JavaScript.

Es buenísimo. Imaginen poder hacer algo como <script lang="text/python">

Y además, la idea es que esto NO requerirá que el cliente tenga
instalado el runtime de .NET (ni el de Mono, para el caso), ya que se
pretende mapear (traducir) el bytecode de IronPython / IronRuby en el
bytecode de Tamarin.

Tamarin es el plato fuerte de esta ensalada: Es el componente de Firefox
que se encarga de ejecutar el JavaScript, por ejemplo. A futuro, la idea
es transformarlo en una implementación open source de alta performance
de ECMAScript 4. Actualmente los usuarios de Firefox estamos usando una
versión de Tamarin que soporta ECMAScript 3. La siguiente versión,
incorporaría la última especificación de Adobe (que fue "donada" a
Mozilla), y abriría la puerta a hacer esta "traducción" en tiempo de
ejecución de CIL a Tamarin.

Acá hay bastante más información al respecto:

-  `El anuncio de Brendan Eich`_, CTO de Mozilla;
-  `La nota en Ars Technica`_ de la que saqué en principio esta info;
-  `El post de Colins Walters`_ en `Planet GNOME`_ gracias al que llegué
   a todo esto;

Ja! Esto le agrega algo más de significado a aquel slogan inicial de
Firefox que decía "Rediscover the web"... ;)

 

.. _ActionMonkey: http://wiki.mozilla.org/JavaScript:ActionMonkey
.. _Tamarin: http://www.mozilla.org/projects/tamarin/
.. _SpiderMonkey: http://www.mozilla.org/js/spidermonkey/
.. _El anuncio de Brendan Eich: http://weblogs.mozillazine.org/roadmap/archives/2007/07/new_projects.html
.. _La nota en Ars Technica: http://arstechnica.com/journals/linux.ars/2007/07/27/firefox-to-support-scripting-with-ironpython-and-ironruby
.. _El post de Colins Walters: http://cgwalters.livejournal.com/4913.html
.. _Planet GNOME: http://planet.gnome.org/
