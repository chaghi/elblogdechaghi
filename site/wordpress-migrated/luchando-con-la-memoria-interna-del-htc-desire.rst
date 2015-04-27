.. title: Luchando con la memoria interna del HTC Desire
.. slug: luchando-con-la-memoria-interna-del-htc-desire
.. date: 2011-10-25 08:30:41 UTC-03:00
.. tags: android,cache,gingerbread,htc,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Hay dos cosas que no me gustan de `mi HTC Desire`_: una es la autonomía
de la batería, la otra, el espacio de almacenamiento interno.

Bueno, hay tres cosas: La tercera es el GPS, pero no termino de decidir
si lo lento que es el GPS para obtener un lock, y la frecuencia con la
que se desengancha es un problema de software, de hardware, o que... y
no es tan de vida o muerte. Lo puteo ***mucho*** cuando salgo a correr,
pero para lo demás, zafa.

Volvamos a los dos temas originales:

El tema de la batería más o menos quedó aceptablemente resuelto cuando
actualicé a Gingerbread. Estoy usando una ROM custom basada en el build
oficial de Gingerbread liberada por HTC para el Desire, específicamente
`esta`_, que es del mismo desarrollador de la ROM que usaba de Froyo.

Digamos que con esa ROM obtengo unas 8hs de uso intensivo, o unas 24 a
36hs de uso normal (que en mi caso tiende a ser de moderado a bajo). Si
bien está lejos de lo que me gustaría, sirve. Sí, en la práctica implica
que lo tengo que cargar todos los días, pero bueno... ahora con
Gingerbread puedo obtener esa autonomía estando conectado prácticamente
todo el día (con Froyo para lograr eso usaba permanentemente `Green
Power`_ para solo activar la conexión de datos durante 2' cada 30').

Y todavía podría mejorarlo más, si flasheara el "Powersaving Mod" de
esta ROM y/o utilizara alguna aplicación que aprovecha el rooteo del
teléfono para hacer under-clocking cuando la CPU o la pantalla están
idle. Calculo que con eso mejoraría mucho, pero todavía no me puse a
jugar con eso. Y siempre puedo recurrir a Green Power (con Gingerbread
casi no lo estoy usando... pero la opción está). Como decía al
principio, la autonomía que tengo ahora no me vuela la peluca, pero me
alcanza. Es manejable.

Pero queda un tema... y es el espacio de almacenamiento interno. Con
esta ROM que estoy usando, instalé también A2SD+, que básicamente usa
una partición extendida en la SD card, y mueve ahí las aplicaciones y el
caché Dalvik, pero ***no*** los datos de las apps. Eso mejora
***mucho*** la cuestión, pero no alcanza. Hay dos cosas que con el
correr de los días se van descontrolando:

Cache
=====

El caché de algunas aplicaciones crece mucho. Algunas apps tienen el
cache en la memoria interna, otras en la externa, otras en ambas.
Depende. Pero hay ciertas apps que tienen una tendencia a entrar a comer
megas y megas de cache en la memoria interna: Google Reader, Internet,
Facebook, Market, Google Maps.

Para resolver esto, instalé `CacheCleaner NG`_ (requiere root para ser
realmente útil...) Lo que tiene de bueno esta app es que permite ver el
caché usado aplicación por aplicación, interno y externo, y configurar
individualmente cual quiero que borre y cual no, también aplicación por
aplicación. Cada N días, le pego una mirada, y libero unos cuantos megas
(con una semana típica de uso suelo estar con entre 10 y 15MB usados
para cache, que obviamente sigue creciendo si lo dejo). CacheCleaner NG
puede configurarse para iniciarse automáticamente y limpiar con cierta
frecuencia, pero por ahora, lo estoy haciendo manualmente.

ANR_history.txt
===============

Esto es un misterio. Intrigado por saber que otra cosa iba comiendo
espacio sin parar, día a día, casi que hora a hora, sin prisa pero sin
pausa, empecé a prestarle más atención a la info que da `DiskUsage`_. Lo
venía usando hace bastante, pero no me había percatado que, si soy root,
puedo usarlo para analizar la carpeta /data/data, que es donde están los
datos de las aplicaciones. Y ahí me encontré con este señor archivo:

::

    /data/data/com.android.htcprofile/anr_history.txt

Google no me ayudó mucho, pero aparentemente es una especie de log de
errores. De hecho, es un archivo de texto, que tiene stack traces de
aplicaciones con problemas. Aparentemente, "anr" es "application not
responding". Tiene sentido... historial de aplicaciones que no
responden. Lo estuve mirando un poco, y hay errores de java de todo
tipo, de prácticamente todas las aplicaciones. No tengo idea que tiene
que ver con HTC Profile; tampoco tengo muy claro que es HTC Profile. Lo
que si tengo claro, es que si no lo blanqueo cada tanto, crece sin
parar, mal. Y también estoy casi seguro que esto empezó a pasar con la
ROM basada en Gingerbread. ¿Será un bug de la ROM que liberó HTC? ¿Hay
forma de apagar ese log de errores? Como les decía, Google no me fue de
ayuda. Sí encontré un par de foros en los que aclaran que no conviene
borrarlo directamente, porque luego podría tener algún problema de
permisos (¿tal vez alguna aplicación o librería de HTC luego no lo
encuentra y falla?). No comprobé lo de los permisos, pero por las dudas,
no lo borro, lo trunco. Me abro una consola local con `ConnectBot`_, y
hago esto:

.. code:: console

   $ su

   # echo "" > /data/data/com.android.htcprofile/anr_history.txt

... y santo remedio. Por algunos días / semanas.

Odio tener semejante teléfono que me salió unos buenos mangos y tener
que estar haciendo este tipo de chanchadas. Ya decidí que mi próximo
teléfono (si tiene Android) va a tener que tener espacio de
almacenamiento interno de verdad (y no los 140MB que tiene el HTC
Desire, que son un chiste de mal gusto).

.. _mi HTC Desire: link://slug/un-par-de-meses-con-android
.. _esta: http://forum.xda-developers.com/showthread.php?t=1200261
.. _Green Power: https://market.android.com/details?id=org.gpo.greenpower
.. _CacheCleaner NG: https://market.android.com/details?id=org.lsartory.cachecleaner.ng
.. _DiskUsage: https://market.android.com/details?id=com.google.android.diskusage
.. _ConnectBot: https://market.android.com/details?id=org.connectbot
