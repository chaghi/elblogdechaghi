.. title: Tercer caso de éxito
.. slug: tercer_caso_de_exito
.. date: 2006-08-19 16:13:55 UTC-03:00
.. tags: GNU/Linux,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

(los dos primeros, `léanlos acá`_)

Además de que nuestro entorno de trabajo nos haga las cosas fáciles, es
bueno saber que, cuando todo se va al carajo, nos puede ayudar a no
perder el trabajo realizado.

Hoy estaba investigando en la web sobre un tema que necesito resolver en
el laburo. Tenía un mail a medio escribir, con varios links y ejemplos
de código copypasteados, que iba creciendo a medida que iba encontrando
información. Y tenía como 6 o 7 páginas web abiertas, en distintas
solapas y ventanas del navegador, de info que había encontrado, y que
aún no había "procesado" (es decir, decidido si me servía o no).

Uno de los links, era un documento de MS Word. Se inició la descarga, y
cuando terminó, empezó a abrirse `OpenOffice`_ (que sigue siendo un
monstruo, por lo pesado...). Y mientras estaba cargando, se colgó todo.
Mal. En forma completa. No más mouse, se congelaron las applets de
Gnome, se congeló el monitor de tráfico de red, dejó de responder el
teclado, no pude conmutar a una ventana de texto, el sistema no
respondió a un CTRL-ALT-BACKSPACE para reiniciar en forma "dura" el
entorno gráfico... nada. Cuelgue total.

Esto es *muy* raro que pase... y como al menos dos de los coolers de
mi gabinete se que no están andando del todo bien, sospecho de un
cuelgue por temperatura... pero también podria haber sido OpenOffice.

El asunto es que no me quedó más remedio que apretar el botón de reset.
Y resignarme a perder el mail que estaba escribiendo, y lo que era peor,
toda la info que había encontrado.

Reinicié la máquina, y al volver a loguearme, obtuve dos agradables
sorpresas:

-  Cuando abrí `Evolution`_, me avisó que tenía un mail a medio
   escribir, y si quería recuperarlo. Le dije que sí, y ahí apareció mi
   e-mail, con el cursor titilando donde lo había dejado, y hasta la
   última letra tecleada. Y esto no es gracias a una función tipo
   "autoguardar" que yo haya activado en las preferencias. No es un
   "snapshot" del mensaje que se toma cada X minutos y se guarda como
   borrador, sino que es la capacidad de Evolution de recuperar en forma
   completa todos los mails que estaban en proceso de edición si se
   produce un cierre anormal de la aplicación.

-  Cuando abrí `Epiphany`_, me dijo si quería recuperar las páginas que
   estaba browseando cuando se produjo el crash. Le dije que sí, y
   recuperó todas las ventanas, con todas sus solapas (el tipo no solo
   "recuerda" que tenía N páginas abiertas, sino que llega al punto de
   saber cuales estaban en solapas en que ventanas, y cuantas ventanas
   abiertas había)

-  Bonus track: La solapa del documento Word no se cargó, y en su lugar,
   apareció un mensaje de Epiphany diciendo que esta ventana no estaba
   totalmente cargada al momento de producirse el crash, con lo cual era
   probable que fuera la causante del problema. En realidad no, porque
   lo que crasheó fue algo de bastante más abajo de Epiphany que colgó
   todo... de hecho pude abrir luego esa ventana sin problemas, y pude
   abrir el documento MS Word con OpenOffice (lo cual refuerza mi
   sospecha de un problema de hardware...). Pero eso no quita que me
   pareció sumamente interesante el approach que tomaron los
   desarrolladores de Epiphany para manejar estos casos: "Mirá, esta
   página no la voy a cargar, porque sospecho que es la que me mató
   antes. Si querés cargarla igual... apretá recargar... bajo tu propia
   responsabilidad". Interesante. Muy.

Conslusión: En un mundo ideal este tipo de cuelgues no deberían darse (y
de hecho son RARÍSIMOS en Linux), pero es bueno saber que el OS y sus
aplicaciones también pueden darnos una mano para no perder el trabajo
realizado cuando todo se fue de control.

.. _léanlos acá: http://www.taniquetil.com.ar/plog/post/1/201
.. _OpenOffice: http://es.openoffice.org/
.. _Evolution: http://es.wikipedia.org/wiki/Evolution
.. _Epiphany: http://es.wikipedia.org/wiki/Epiphany
