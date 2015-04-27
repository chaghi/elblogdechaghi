.. title: Configurando Wake on LAN
.. slug: configurando_wake_on_lan
.. date: 2009-03-21 22:50:24 UTC-03:00
.. tags: GNU/Linux,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

En breve me voy por trabajo una temporada a MDQ, y entre todas las cosas
que tengo que hacer, tengo que decidir que cosas dejo operativas en el
depto, y cuales no. La idea es viajar a Baires regularmente (calculo que
cada 20 días), con lo cual no tengo intenciones de hacer un shutdown
*full* de mi casa.

¿Qué hago con la PC? Es un tema. Si bien es normal que esté varios días
encendida, haciendo de file-server o alguna otra huevada, no me gusta
mucho la idea de que esté encendida y desatendida tantos días seguidos.
No le tengo confianza a la fuente, ni a los coolers (ya me pasó una vez
llegar a casa, encontrar la PC apagada, la fuente quemada, y ese
olorcito a "algún aparato se quemó"). Una cosa es que este encendida
permanentemente dejándola sola a lo sumo un par de días, y otra dejarla
encendida sin saber a ciencia cierta cuantas semanas pasarán hasta que
alguien le eche un ojo al depto. La realidad es que hace mucho tiempo
tengo pendiente invertir en una PC más nueva, y de paso prestarle
atención a la alimentación, la refrigeración, el ruido, y el cablerío
infernal que es hoy el escritorio en donde está. Pero eso sigue sin
resolverse, y ya no tengo tiempo de resolverlo antes de la partida.

Mi equipo principal de trabajo hoy es la laptop, no la PC, pero la
verdad me gustaría saber que estando en MDQ puedo contar con la PC. Por
ejemplo, para mantener sincronizados y backupeados regularmente los
datos de la laptop. Para tirar algún proceso largo. Para bajarme algún
album de mi colección de MP3. Whatever. Entonces, no quiero dejar la PC
encendida... pero me gustaría irme a MDQ sabiendo que puedo prenderla en
forma remota si la necesito unas horas. 

Así que me propuse volver a la carga para intentar configurar "WOL", o
Wake-On-LAN, que no es otra cosa que un feature que tiene que estar
soportado por el BIOS, la placa de red, el mother y la fuente, y que
permite mandar un "magic packet" por la red para prender el equipo.

Alguna vez había intentado configurar esto, sin éxito, pero tampoco le
dediqué tiempo. Ahora tenía un motivo para investigar más a fondo, así
que me puse manos a la obra. El desafío tenía 3 partes:

-  dejar de usar la placa de red 3com, y pasar a la nVidia
-  hacer que WOL funcione desde la LAN, o sea, lograr encender la compu
   desde otro equipo que es parte de la red local
-  hacer que WOL funcione desde la WAN (algunos llaman a esto WOW), o
   sea, lograr encender la compu desde internet

Cambiando 3com por nVidia
-------------------------

Mi mother tiene 2 placas de red integradas. La primaria es una placa
nVidia con chipset Realtek, la secundaria es una placa 3com con un
chipset Broadcom. Resulta que había una época, hace muuuuuchos años,
cuando compré la PC, en que el driver "forcedeth" de Linux (el que se
usa para nVidia) no andaba ni pa'tras. Así que hacía rato que usaba la
placa 3com. También había una época en que NetworkManager era bastante
choto en cuanto a configurar una IP fija y/o a levantar la conexión
ANTES de loguearte, así que medio tenía by-passeado a NetworkManager,
con una configuración medio mirame-y-no-me-toques que nunca entendí del
todo, y tampoco quería tocar porque... bueno, para que tocar lo que
anda, ¿no?

Pero resulta que de las dos placas, la que soporta WOL es la nVidia.
Fuck. Así que por eso el primer desafío era cambiar de placa de red. De
paso, si quieren investigar que cosas soporta cierta placa, se lo pueden
preguntar a ethtool:

.. code:: console

   $ sudo ethtool eth0
   Settings for eth0:...  Supports Wake-on: gWake-on: g...

ethtool les va a decir varias cosas. En el ejemplo de arriba dejé solo
las salidas relevantes. *Supports Wake-on:...* está seguido de una
seriede flags (letras), indicando todas las opciones de wake up
soportadas por la placa. En mi caso, solo soporta "g", que es WOL usando
un "Magic Packet" (más sobre esto, luego). La línea *Wake-on:...* nos
muestra, dentro de las opciones soportadas, cuales están efectivamente
activas.

Bueno, el tema es que hace una semana hice el cambiazo, y empecé a usar
la placa nVidia. Hice este cambio con tiempo para poder testear que todo
ande bien. La buena noticia es que los años que pasaron desde la última
vez no han sido en vano, y aparentemente el driver forcedeth just works.
Y NetworkManager sigue teniendo sus no pocas mañas, pero al menos ahora
se puede configurar una IP fija y cambiar de una configuración a otra
sin tener que encomendarte a ningún espíritu para que funcione.

So far, so good.

Configurando WOL
----------------

Además de tener una placa que soporte WOL, esta configuración tiene que
estar soportada por el mother y activada en la BIOS. Por defecto, no lo
está. El nombre con el que aparece puede ser bastante críptico, en mi
caso, la configuración está dentro de Power Management, y la opción que
hay que habilitar es "Power Up on PCI Device". Por otro lado, esto tiene
que estar soportado por tu fuente... pero a menos que estemos hablando
de una XT no debería ser problema, ya que me parece que alcanza con que
la fuente sea ATX.

Por último, si la placa de red no está integrada (i.e., no es parte del
motherboard, y es una placa PCI aparte), es muy probable que en algún
lado tenga un conectorsito específico de WOL en el cual habrá que
chantar un cable que en el otro extremo termina en el conectorsito WOL
del motherboard. En mi caso todo esto no existe porque la placa está
integrada al mother.

Hasta ahí estamos con el hardware y la BIOS... el siguiente paso, es
configurar el sistema operativo.

Primer problema: El soporte WOL no está activo por defecto. Si tiráramos
el comando que mostraba más arriba, veríamos el soporte para WOL "g",
pero no lo veríamos activo. Hay que activarlo, y que yo sepa, no hay
otra que hacerlo vía ethtool:

.. code:: console

   $ sudo ethtool -s eth0 wol g

(reemplazando eth0 por el dispositivo de red que se desea configurar si
fuera otro)

Segundo problema: La activación no es persistente. Cada vez que se
reinicia la PC, y el kernel reinicializa el hardware, esa configuración
se pierde. Al menos es así con forcedeth. Así que tuve que crearme un
pequeño servicio para que active WOL en la placa de red cada vez que se
enciende el equipo.

Idealmente, debería haber \*algo\* en la infraestructura de networking
de Linux para configurar esto, y de manera permanente, y los DEs (por
ejemplo, Gnome) deberían brindar alguna GUI para hacer la
configuración... pero por ahora hay que ensuciarse las manos :(

¿Y ahora? Si los planetas están alineados, y apagamos la PC normalmente,
y desde otro equipo dentro de la LAN enviamos un Magic Packet, la PC
debería encenderse.

¿Y qué es eso de un "Magic Packet"? Si quieren detalles pueden leer por
ejemplo `acá`_, o googlear sobre WOL, pero básicamente un Magic Packet
es un datagrama UDP de 102 bytes (pueden ser más si se configura un
password), en el que se envía el byte 0xFF 6 veces, seguido de la MAC
address de la placa de red de destino repetida 16 veces (seguido
opcionalmente de un password). Hay múltiples utilidades para generar ese
tipo de paquetes. Yo me bajé un script en Perl que se llama, en un
derroche de originalidad, "wakeonlan" :p, porque es lo que tenía más a
mano (está en los repos de Ubuntu).

Y este script, en su forma más simple, se usa así:

.. code:: console

   $ wakeonlan xx:xx:xx:xx:xx:xx

donde ``xx:xx:xx:xx:xx:xx`` es la MAC de la placa de red.

Pero resulta que no andaba, no andaba, y no andaba. Después de MUCHO
googlear (no quiero ni sacar la cuenta de las horas que perdí en
esto...), y gracias a un comentario reciente en `este post`_ de hace mil
años de un foro de nVidia, descubrí que forcedeth tenía un bug que hacía
que la MAC se interprete al reves. Supuestamente lo arreglaron, pero
aparentemente en algún punto se rompió otra vez. Así que si tu placa de
red es nVidia, usas forcedeth y un kernel reciente, y tu MAC es
01:02:03:04:05:06, tenés que generar el Magic Packet como si fuera para
la MAC 06:05:04:03:02:01. ¿No era OBVIO? :(

La buena noticia es que... ANDA!

Configurando WOW
----------------

Hasta acá, *debería* ser fácil. Si tu hardware lo soporta, si tu BIOS
está bien configurada, si los drivers de la placa de red del operativo
no fueran una mierda, y si tu SO te facilitara la configuración de esto
(en Windows, por ejemplo, al configuración está un poco escondida, pero
ESTA, y es persistente), deberían ser un par de clics.

Ahora, querer que esto ande desde internet... es otra historia. Porque
ahí tenés que pasar por al menos un router (el tuyo), y si el mismo no
es más o menos "de verdad" y no tiene soporte nativo para WOL, vas a
tener que recurrir a algún "hack" para convencer al router de que cuando
reciba el Magic Packet, se lo pase a la PC.

Mi router es un D-Link DI-524, y es bastante pedorro. No tiene soporte
para WOL. Así que hay que empezar a probar trucos. ¿Dónde está la
complejidad? WOL funciona haciendo un broadcast. Dentro de una LAN eso
está bárbaro, pero desde una WAN, obviamente uno no puede hacer un
broadcast al universo. Básicamente tenés que mandar el Magic Packet a tu
IP pública. A menos que tengas un servicio con IP fija, primero tenés
que resolver como saber en un momento dado que IP te asignó tu ISP. Esa
es una historia que tengo resuelta desde hace rato con `DynDNS`_, así
que hasta ahí, todo OK.

Ahora, el tema es como hacer para que el router retransmita el Magic
Packet, y lo haga llegar a la placa de red de destino. Si el mismo no te
da ninguna solución nativa entre las opciones de configuración, la
solución pasa por configurar un virtual server, y hacer que por ejemplo
los paquetes UDP sobre el puerto 9 (que ese el que se suele usar para
WOL) los envíe a la IP-tal, donde IP-tal es la IP de tu PC. Y acá es
donde las cosas se empiezan a complicar...

Obviamente, el primer paso es que tu PC tenga siempre la misma IP
interna. En mi caso, tengo esto configurado así desde hace rato, así que
vamos bien, pero el tema es que la PC va a estar apagada. Mandamos el
Magic Packet a la IP pública. El router lo recibe. Como está en el
puerto 9, y hay un Virtual Server definido para ese puerto, se encuentra
con que tiene que mandar el paquete a la IP-tal de la LAN. Entonces
manda un request ARP preguntando "¿quién tiene la IP tal?". Y resulta
que la PC está apagada para contestarle :(  Normalmente el router cachea
esta información, así que si uno apaga la PC e intenta un WOL a los
pocos minutos, *puede* que ande. Pero después de un (normalmente) corto
tiempo, ya no.

Si el router fuera más o menos bueno, uno podría cargarle un registro
estático en su tabla ARP, diciéndole que a la IP-tal le corresponde la
MAC-tal, y listo. El router ya no necesita hacer un request ARP para esa
IP. Pero mi router no permite manipular la tabla ARP, así que no es una
opción.

En estos casos, lo que uno puede hacer es configurar el Virtual Server
para que use como IP privada la IP de broadcast de la LAN, entonces,
cuando el router recibe el Magic Packet, lo termina broadcasteando hacia
adentro. Pero... no siempre el router te deja definir como IP privada de
una regla de virtual server a la IP de broadcast. En mi caso, me dejaba
definirla, pero cuando recibía el paquete, se colgaba !!!

A todo esto: Yo no sabía absolutamente NADA de IP broadcasting, tablas
ARP y demás conceptos de ruteo, así que fui sorteando cada nuevo
obstáculo con la ayuda de google y muchos golpes contra la pared. En
particular, `este hilo en este foro`_ está BUENISIMO. Fue gracias a ese
hilo que aprendí un montón de cosas, y que fui dando con las soluciones.
Gracias a la experiencia de otro usuario con mi mismo router, llegué a
la conclusión de que *tal vez* si actualizaba el firmware del router iba
a solucionar el tema del cuelgue del mismo al recibir el paquete.

Generalmente no soy NADA amigo de actualizar el firmware de ningún
equipo, a menos que tenga un problema que sí o sí necesito resolver, y
esté seguro que la nueva versión de firmware lo arregla (y cierta
garantía de que no rompe otras cosas en el proceso...). En este caso, si
bien dejar funcionando WOL no era de vida o muerte, y la única
"evidencia" de que con un firmware más nuevo lo podía arreglar era la
experiencia de UN usuario en UN post de UN foro encotrado al azar en
internet... decidí tirarme a la pileta. Más que nada, por calentura.

Así que algunos minutos después, estaba rebooteando el router con
firmware nuevito. Así y todo... WOL desde internet seguía sin andar. El
avance fue que ya el router no se colgaba (bien!), pero la PC, ni se
inmutaba. Seguía apagadita apagadita. Lo parió.

Después de un rato más de Google y paseo por diversos foros, y cuando ya
casi estaba por mandar todo a la reputamadrequelopario, encontré en
`Ubuntu Forums`_ un flaco que hablaba de `microWOW`_, un MIDlet para
celulares que permite generar paquetes WOW. No le tenía mucha fe, ya que
había probado UN MONTON de servicios web para generar paquetes (además
del script 'wakeonlan' que me había bajado, y además de varias pruebas
armando paquetes "a pedal" con Python), pero perdido por perdido, decidí
probarlo.

Y funcionó! Aún no se por qué, pero so far es la ***única*** alternativa
que me anda fuera de mi LAN.

El por qué es un misterio. Me bajé los fuentes, y constaté que no hace
ninguna magia rara. Es más, me armé una pequeña aplicación de consola en
Java usando el código ese como base, y no me anduvo. Constaté que lo que
hace ese MIDlet aparentemente es lo mismo que hace el script en Perl que
había bajado, y lo mismo que hice con diversos experimentos con Python,
pero la realidad es que TODOS los intentos por generar un Magic Packet
desde internet no me funcionan, excepto si lo genero desde el celular
con microWOW (por otro lado, TODOS los experimentos que hice SI
funcionan desde adentro de la LAN).

Misterio.

Lo bueno es que tengo una alternativa... lo malo es que con tanto tanto
tanto tiempo invertido, me encantaría saber a que le estoy pifiando
cuando genero el Magic Packet con otra herramienta, porque TIENE que ser
una boludez, tiene que ser *algo* que evidentemente Java Micro Edition
hace por default con los sockets, que es diferente de lo que Java
Standard Edition hace, y es diferente de lo que yo hago desde Python, y
lo que wakeonlan hace con Perl.

En un momento se me ocurrió que el problema tal vez era que en
definitiva con mis experimentos el paquete se estaba generando desde
dentro de la LAN, mientras que con microWOW se estaba generando posta
desde afuera (con el celular), pero hice la prueba de mandar un paquete
conectándome vía SSH con otro server fuera de mi LAN, y tampoco anduvo.

Conclusiones
------------

-  mientras tenga mi celular a mano y servicio GPRS, puedo encender la
   compu de casa en cualquier momento
-  configurar WOL no es trivial, hay muchas variables en juego
-  el soporte para WOL en Linux al día de hoy es bastante pedorro, y hay
   que hacer todo a mano y desde una consola
-  configurar WOW es muy complejo a menos que tengas un router de
   verdad, y no uno de los juguetes que uno suele comprarse para la casa
-  aprendí bastante sobre enrutamiento y broadcasting de paquetes...
-  ... pero no lo suficiente como para entender por que el único
   generador de paquetes que me anduvo es microWOW

Si este no es a la fecha el post más largo en este blog (a excepción de
los relatos de viajes), le pega en el palo...

 

.. _acá: http://en.wikipedia.org/wiki/Wake_on_LAN
.. _este post: http://www.nvnews.net/vbulletin/showthread.php?t=70384
.. _DynDNS: http://www.dyndns.com/
.. _este hilo en este foro: http://forums.whirlpool.net.au/forum-replies-archive.cfm/833973.html
.. _Ubuntu Forums: http://ubuntuforums.org/showthread.php?t=913590&page=2
.. _microWOW: http://code.google.com/p/microwow/
