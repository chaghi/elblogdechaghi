.. title: GMail + OfflineIMAP + Evolution
.. slug: gmail_offlineimap_evolution
.. date: 2009-12-27 11:22:38 UTC-03:00
.. tags: Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Finalmente, después de bastantes experimentos, creo que logré una
configuración de manejo de correo electrónico en la laptop que me
satisface. Y no te dejes engañar por el "Evolution" del título: En
realidad, bastante de la experiencia aplica a cualquier MUA, o a
cualquiera que quiera independizarse del MUA (ver "Bonus track" final),
o simplemente a cualquiera que quiera tener un backup del correo de
GMail local accesible incluso off-line.

Background
----------

Mi cuenta de correo principal, la que más uso, está en GMail. La
aplicación web está excelente, y ahora que me estoy acostumbrando a los
"atajos de teclado" (¿por qué tardé literalmente *años* en tratar de
aprenderlos e incorporarlos a mis dedos?), aún mejor. Pero así y todo,
me gusta sentir que no dependo de una conexión a internet para acceder
al correo histórico, y me gusta tener un backup, con lo cual necesito
que el correo esté bajado en mi disco, para poder accederelo con algún
MUA.

Hasta hace unas semanas, accedía a GMail con Evolution usando POP3.
Desde que empecé a usar GMail que hacía esto. Y tenía múltiples filtros
de correo entrante y saliente que redistribuían los mensajes en N
carpetas de Evolution que, más o menos, equivalen a una etiqueta en
GMail. Por otro lado, tenía (tengo) años de historia de correo
electrónico que no es de GMail, principalmente, de mi vieja, querida y
deprecada cuenta de Sion. Entonces por ejemplo en la carpeta "Amigos",
tengo todo el correo de mis amigos, no solo el de los últimos 3 años en
GMail, sino también el histórico.

El tema es que a medida que empecé a usar más y más GMail, y
especialmente, desde que empecé a usarlo desde distintas computadoras,
en distintos ámbitos, y con diferentes clientes, me choqué contra lo
obvio: POP3... #noescala (chiste interno para los twitteros... je). Leer
una cantidad de correos durante el día, etiquetarlos, acomodarlos, y a
la noche prender la laptop y volver a bajarlos como correo "no leído",
es una porquería. Muchas veces me pasaba que "leer" correo en la laptop
en realidad era ir carpeta por carpeta en Evolution marcando los
mensajes como leídos, sin siquiera abrirlos.

Boludo, ¡usá IMAP!
------------------

Hace bastante GMail habilitó IMAP. Cualquiera diría que es la solución.
Pero... siempre hay un pero (en este caso, varios)

La implementación de IMAP de GMail suckea un poco. Lo de exponer los
labels como folders tiene el inconveniente de que los correos que tienen
N etiquetas, los bajás N veces (¿tantos recursos le sobran a Google que
fue por este camino, en lugar de mapear las etiquetas a IMAP keywords, y
dejar que las carpetas las manejes vos?). Por otro, la filosofía de "no
borres el correo, archivalo", sumado a lo de las etiquetas, hace que
cuando accedés a GMail con IMAP desde un cliente, algunas operaciones no
sean obvias, o no hagan lo que vos pensás que deberían hacer. Aún hoy
estoy tratando de `incorporar algunas de estas cosas`_ de manera
definitiva en mi cerebro.

Así y todo, decidí sacrificar mi estructura histórica de carpetas,
reemplazarla por la estructura "plana" que me da GMail (sí, ya se, si
usara etiquetas con "/" en medio, automáticamente en la interfaz IMAP se
traducen en una jerarquía de carpetas, pero no me gusta), y acceder vía
IMAP.

Ahora, ¿qué hacía con las carpetas con el correo histórico? Vieron que
los MUA en general cuando configuran una cuenta IMAP, como que crean una
sub-estructura de carpetas nuevas, con su propia bandeja de entrada,
papelera, correo enviado, borradores, más las carpetas de esa cuenta.
Así que en cuanto hice el switch, el primer escollo es que en Evolution
pasé a tener 2 grandes nodos: Correo viejo bajado por POP3, de GMail, de
SION y otras cuentas, y el correo nuevo que iba entrando por IMAP. Y
además, había una superposición: Todo el correo de GMail que había
bajado durante años via POP3 estaba también accesible vía IMAP
(repetido).

Para resolver eso, me tuve que embarrar las manos. Una solución hubiera
sido escribir un script que leyera las carpetas en formato mbox de Evo y
analizando los headers de los correos los copiara en las carpetas
IMAP... pero no tengo experiencia manipulando correo a bajo nivel, y
tampoco tengo TANTAS carpetas (ni tanto correo, apenas unos cientos de
MBs), así que lo fui haciendo a mano: En cada carpeta de Evo, seteaba un
filtro que básicamente era "mostrame el correo que entre los remitentes
o destintatarios tenga a mi cuenta de sion o la cuenta de mi ex laburo y
no tenga mi cuenta de GMail", y al correo resultante lo arrastraba a la
carpeta (label) correspondiente en la cuenta de GMail.

Esto efectivamente "sube" (o importa) el correo en GMail, así que estuve
un bueeeen rato haciendo esto. Y después me topé con `este bug de
GMail`_: El correo importado desde IMAP queda con la fecha incorrecta
(con la fecha del día que lo importaste) en la interfaz web. Así que
ahora tengo miles de correos en GMail que si los accedo desde la web, o
si los busco, tienen la fecha en que los importé. Como internamente la
fecha está bien (desde cualquier otro cliente se ve la fecha correcta, e
incluso dentro de la interfaz web de GMail, en la vista de
conversaciones se ven bien), supongo que algún día Google lo arreglará
(aunque el tema es un known issue desde hace más de un año...)

Bueno, pero entonces, listo, pasaste a IMAP, y fuiste feliz, ¿no?

No

IMAP en Evolution sucks
-----------------------

Y por lo que leí, IMAP en Thunderbird también, y hasta IMAP en mutt
suckea en algunos aspectos, así que malo por malo, me quedo con el malo
que conozco, que encima es el MUA oficial de Gnome, y por lo menos tiene
resuelta la integración con el desktop de manera decente.

Evo por default baja solo las cabeceras de los mensajes. Así que navegar
por las carpetas se vuelve lentísimo, porque se tiene que conectar al
server a bajar el mensaje. Obvio si el mensaje no está completo, no
tengo un backup en disco. Y tampoco puedo hacer búsquedas locales, ni
acceder al correo viejo si no tengo internet. Se le puede decir a Evo
que baje todo el correo. Y lo hice. Lo dejé una noche haciéndolo. Pero
resulta que el tipo así y todo ¡¡¡NO baja los attachments!!!. E igual,
aunque tenga el correo cacheado en disco, cuando te parás encima del
mensaje el tipo "dialoga" con el server IMAP para ver si el mensaje
sigue existiendo, si le cambió algún flag, etc., o para bajar el
attachment que no bajó. Es *lento*. Navegar por las carpetas de Evo se
vuelve una tortura, y eso que no tengo cientos de miles de correos en
cada carpeta, ni mucho menos. 

La única manera de leer correo sin que sea leeeeeeeento, es decirle a
Evolution que labure "off line". Entonces el tipo se desconecta, no
habla más con el server IMAP, y se deja de joder. Pero... no tengo los
attachments. Y si entra nuevo correo, no me entero. Y si hago cambios
localmente en el correo (los borro, los muevo, etc), no se impactan en
el server hasta que no vuelvo a decirle a Evo que labure on line. Sucks.
Sucks *big time*.

Después de considerar momentáneamente cambiar de MUA, decidí que ese no
era el camino. En múltiples foros me encontré con que Thunderbird tiene
issues también. Y no iba a volver a Thunderbird, cuya integración con
Gnome es *pésima*, para sufrir más o menos lo mismo. Y no iba a
pasarme a un MUA geek de terminal, como `mutt`_ o `SUP`_, no gracias. No
soy *tan* geek. Encima SUP está escrito en Ruby (yikes!).

Enter OfflineIMAP
-----------------

Resulta que hay un programita, hecho en Python (¡Python rocks!), llamado
`OfflineIMAP`_, que básicamente sirve para sincronizar una cuenta IMAP
con un repositorio local en formato `Maildir`_. Puede hacer unas cuantas
cosas más, como sincronizar múltiples cuentas, o sincronizar un IMAP con
otro, y así, pero en esencia, el tipo es eso: un algo que lee un
repositorio remoto (IMAP), y lo sincroniza contra uno local (Maildir u
otro IMAP), y en el medio, podés poner reglas (esto sí, esto no, lo de
esta carpeta pasalo a esta), y esas reglas muchas veces son expresiones
de Python, o invocaciones a funciones de Python que realizan la
conversión :)

Y todos sabemos que *manejar tu correo con Python gives you a warm and
fuzzy feeling* :)

Así que hice eso: Configuré OfflineIMAP, y luego apunté a Evo a la
carpeta raíz de la estructura Maildir, y voilá. *It flies*. Y encima,
el formato Maildir es mucho más robusto que un mbox: tengo un archivo
por correo, así que si por puta se corrompe un archivo, se pierde UN
correo, no mil.

No voy a exponer acá un tutorial detallado de como configurar
OfflineIMAP (hay *mil* recetas en la web), pero si voy a dar algunos
tips que me resultaron interesantes, o que descubrí a fuerza de darme
algún palo:

Muchos tutoriales te dicen que para configurar OfflineIMAP para GMail y
luego accederlo con Evo tenés que mover ciertas carpetas a un nodo
"root", porque si no Evo no entiende bien la estructura Maildir. Esto es
parcialmente falso. La única carpeta problemática es el INBOX, que tiene
que ser la raíz de la estructura Maildir, y GMail la expone como
"/INBOX", no como "/". Esto se resuelve así en tu .offlineimaprc:

.. code:: python

   nametrans = lambda foldername: re.sub('^INBOX', '.', foldername)

Puede que NO quieras bajar la carpeta "Spam" de GMail, ni la carpeta
"All Mail". La última es un tema... en mi caso, como soy bastante
histérico con el etiquetado de correo en GMail, es raro que un mensaje
quede sin etiquetar. Si está etiquetado, lo tengo en por lo menos una
carpeta IMAP (y si tiene N etiquetas, en las N carpetas); si no está
etiquetado, en general no es importante. Anyway, la forma de exluir una
o más carpetas de la sincronización es la siguiente:

.. code:: python

   folderfilter = lambda foldername: foldername not in ['[Gmail]/Spam', '[Gmail]/All Mail',]

Dejarlas afuera tiene los siguientes caveats:

-  No hay forma de reportar un correo como SPAM desde tu estructura
   Maildir. La forma de decirle a GMail desde IMAP que un correo es Spam
   es moverlo a dicha carpeta, pero como no la estás sincronizando...
-  No hay forma de "desetiquetar" por completo un mensaje. La forma de
   hacerlo es mover el mensaje a la carpeta "All Mail", pero como no la
   estás sincronizando...

De nuevo, eso último es personal. A mi, me sirve así.

Ya que hablamos de carpetas, `no dejen de leer estos tips de Google`_.
Básicamente:

-  **No** mapeen la carpeta "Correo enviado" de su MUA a la carpeta
   Sent. Google copia automáticamente los mensajes que salen por su SMTP
   a la carpeta Sent.
-  **No** mapeen la "Papelera" de su MUA con la carpeta Trash de GMail,
   a menos que quieran efectivamente *borrar* el mensaje en lugar de
   archivarlo. Google recomienda lo último (archivar). La manera de
   borrar sería arrastrar el correo a la carpeta trash. Si atan la
   papelera de su cliente con el Trash de Gmail, no tienen forma de
   hacer el equivalente al "Archive" de GMail desde el cliente... a
   menos que también estén sincronizando la carpeta "All Mail", en cuyo
   caso, el Archive sería mover el correo a la carpeta All Mail.
-  **Sí** mapeen la carpeta "Borradores" de su MUA con la Draft de
   GMail, así los tienen sincronizados.

Por último, un detalle: No me gustaba mucho tener la clave de GMail
volcada textualmente en un archivo de configuración. Pero resulta que
OfflineIMAP puede invocar a una función de Python que le devuelva
algunos settings, entre ellos, la password y el usuario de la cuenta
IMAP (o de GMail). Así que pensé, ¿no podré tener la password en el
keyring de Gnome, hacer un script de Python que lo recupere, y decirle a
OfflineIMAP que use eso? Si, puedo. Y alguien ya lo había hecho :)
`Miren acá`_.

Bonus track
-----------

Lo bueno de tener a OfflineIMAP en el medio volcando tu correo en un
Maildir estándar, es que ahora mi copia local del correo es
independiente del MUA :)

Si mañana me canso de Evolution, solo tengo que poner el MUA que quiera
apuntando a mi repo local, y ya está. Y si quiero probar un MUA nuevo,
no necesito hacer NADA. Hasta puedo usar diferentes MUAs
simultáneamente.

 

 

.. _incorporar algunas de estas cosas: http://mail.google.com/support/bin/answer.py?hl=en&answer=77657
.. _este bug de GMail: http://mail.google.com/support/bin/answer.py?answer=82365&topic=12922
.. _mutt: http://www.mutt.org/
.. _SUP: http://sup.rubyforge.org/
.. _OfflineIMAP: http://software.complete.org/software/wiki/32
.. _Maildir: http://es.wikipedia.org/wiki/Maildir
.. _no dejen de leer estos tips de Google: http://mail.google.com/support/bin/answer.py?answer=78892&cbid=-1d485khlyyj17&src=cb&lev=answer
.. _Miren acá: http://www.clasohm.com/blog/one-entry?entry_id=90957
