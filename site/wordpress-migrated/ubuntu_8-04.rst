.. title: Ubuntu 8.04
.. slug: ubuntu_8-04
.. date: 2008-04-26 22:12:40 UTC-03:00
.. tags: GNU/Linux,review,Software,ubuntu
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Terminé la migración de la compu y la laptop a Ubuntu 8.04. Esta es la
segunda versión LTS, o Long Time Support. Inicialmente iba a esperar
algunos días más para migrar, pero hoy tenía tiempo, estaba aburrido, y
venía probando los últimos dos betas y el RC sin mayores problemas, así
que me animé.

El mayor miedo era que dejara de andar la placa wi-fi de la laptop, ya
que en los últimos kernels de Linux se viene trabajando en un
refactoring de código importante de la infraestructura de soporte para
los drivers de dispositivos WLAN, que entre otras cosas, obligó a
re-escribir el driver de mi placa (una Intel 3945)... que
paradójicamente era uno de los más maduros, estables, fáciles de hacer
andar. Y su reemplazo tenía un par de bugs que se arreglaron apenas
después de la beta6. De hecho en lo que a mi me concierne sigue habiendo
un bugsito que finalmente no se arregló, y es que con el nuevo driver no
funciona el led que indica si la placa wireless está activada o no.

Volvamos a la actualización: En ambas máquinas el upgrade funcionó sin
novedades. Al igual que las últimas veces, realicé el upgrade con el CD
de instalación "Alternativo", de manera de tener la mayoría de los
paquetes disponibles en CD. Eso acelera mucho el proceso, y lo hace más
inmune a mirrors lentos... que estos días estaban que ardían con todo el
mundo upgradeando. La PC (que actualicé primero), salió andando de una,
sin ningún problema. Supongo que ayuda que hoy se transformó
especialmente en un server y máquina de respaldo, y he desinstalado
parva de cosas, con lo cual hoy por hoy es una configuración sumamente
minimalista y estándar.

Con la laptop tuve un problema complicadito de resolver, culpa de esas
cosas que es imposible probar con el LiveCD, y que hasta que no hacés la
instalación posta no te das cuenta que no andan. Y culpa también de una
configuración bastante particular de mi parte. Resulta que tengo mi HOME
encriptado. Esto es más que nada para que si me chorean o pierdo la
laptop, estar medianamente tranquilo que no desparramo por ahí un montón
de info personal mía, y de amigos y familiares. Pero el approach que usé
para configurar la encriptación no es precisamente el más robusto
(después de todo, la idea no es proteger la info frente a un técnico de
un servicio de inteligencia, sino ante un choro cabeza de mierda de los
que abundan últimamente...), sino el más fácil de configurar. Estoy
usando `EncFS`_, que es un layer de encripción liviano que corre en
user-space por arriba de `FUSE`_. Esto está pensado más que nada para
encriptar directorios y/o archivos individuales, pero yo tengo
encriptado todo mi HOME. Y tengo instalada una magia que a través de
`PAM`_ me da acceso a la info encriptada al iniciar cesión, para que sea
"transparente", y no tener que estar ingresando múltiples passwords. Y
resulta que la versión de libpam-encfs con la que salió Ubuntu 8.04 está
compilada mal, y no se puede cargar.

El efecto fue que al reiniciar la máquina por primera vez luego de la
actualización, y obviamente sin saber nada de todo esto, me encontré con
que ni bien ponía mi nombre de usuario para iniciar cesión, me saltaba
un alerta de "Authentication failed" (sin siquiera pedir el password). Y
no había forma de entrar. Con ningun usuario. Ni desde el session
manager ni desde una consola. Googleando un poco encontré que `el bug
estaba reportado desde hacía ya un tiempito`_, que es una boludez (un
flag de compilación!), que está detectado, y calculo que en los próximos
días saldrá un rebuild oficial del paquete con el fix. Pero mientras
tanto... tuve que encontrar todo esto, bajar el source del paquete, el
patch que incluyen en el bug report, y rearmar el paquete aplicando ese
patch, y reinstalarlo. Todo esto desde una cesión "chrooteada" booteando
con el LiveCD. Una vez detectado el problema fue fácil, pero ciertamente
son esas cosas que uno resuelve por experiencia en la plataforma,
mientras que un usuario final no sabría para donde correr. Aunque
también es cierto que un usuario normal no tendría el setup
pseudo-complicado que tengo yo (de hecho, el reporte de este bug pasó
completamente inadvertido para mí, a pesar de que hacía varias semanas
que venía prestando atención a posibles problemas que podrían
presentarse en un upgrade, y supongo que fue así porque no es un bug que
haya mordido a demasiada gente).

Sorteado ese susto... pude empezar a disfrutar la nueva versión de
Ubuntu. No voy a hablar de cosas nuevas en detalle, porque hay miles de
reportes y blogs y servicios de noticias publicando posts con las
novedades de Ubuntu 8.04 desde hace meses. Pero si quería detenerme un
poquito en `PulseAudio`_, el nuevo sound server. Instalando un par de
aplicaciones de configuración, pude probar los dos features más
interesantes:

-  Controlar en forma individual el volumen de cada cosa que está
   sonando;
-  Publicar en la LAN las placas de sonido, de manera de poder hacer
   cosas como reproducir música en la laptop, pero escucharla por el
   hometheatre conectado a la PC :)

Y lo más lindo es que todo esto se configura con 2 o 3 clics en las
herramientas correspondientes, y Just Works. Y es dinámico. Los servers
se "publican" en la red mediante `Avahi`_, y usan `Zeroconf`_, así que
se auto-descubren, sin configurar IPs, ni puertos ni nada. Y en
cualquier momento, desde el control de volumen, uno puede "transplantar"
un stream de audio de un dispositivo a otro. Impresionante. PulseAudio
es multiplataforma, así que encima esto funciona en una red mixta con
Linux, Solaris, FreeBSD y Windows (sorry Mac... :p)

Otro cambio muy visible, es Firefox 3 (Ubuntu 8.04 instala la beta5).
Para los usuarios de Linux, es realmente bienvenido que los developers
de Mozilla se hayan puesto finalmente las pilas, y hayan hecho que Gecko
use los widgets nativos de la plataforma en los forms, y que Firefox
herede los iconos, colores y demás look&feel de la apariencia general
configurada a nivel global. Así que ahora Firefox dejó de parecer un
alien. Esta fue una de las principales causas de que dejara de usar
Firefox con Gnome, y empezara a usar Epiphany. Además Epiphany es mucho
más liviano. El tema es que ahora Firefox3 (teóricamente...) también
está mejorado en ese aspecto. Pero a su vez Epiphany usa Gecko, y muchas
de las mejoras de Firefox3 son en realidad mejoras de Gecko, con las
cuales las tiene también Epiphany. Conclusión: Voy a tener que probarlos
bastante más codo a codo para determinar si Epiphany continúa siendo una
mejor alternativa (para mí, claro está), o si vuelvo a Firefox.

 

.. _EncFS: http://www.arg0.net/encfs
.. _FUSE: http://fuse.sourceforge.net/
.. _PAM: http://www.kernel.org/pub/linux/libs/pam/whatispam.html
.. _el bug estaba reportado desde hacía ya un tiempito: https://bugs.launchpad.net/ubuntu/+source/libpam-encfs/+bug/205783
.. _PulseAudio: http://www.pulseaudio.org/
.. _Avahi: http://avahi.org/
.. _Zeroconf: http://www.zeroconf.org/
