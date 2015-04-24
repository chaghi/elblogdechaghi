.. title: Chau Fedora, hola Ubuntu
.. slug: chau_fedora_hola_ubuntu
.. date: 2006-03-25 00:21:17 UTC-03:00
.. tags: fedora,GNU/Linux,ubuntu
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

La migración a `Ubuntu`_ se produjo antes de lo previsto. Ya había
tomado la decisión de que en lugar de instalar `Fedora Core`_ 5, iba a
instalar Ubuntu 6.04. Pero resulta que el lanzamiento de este último se
pospuso unas semanas, salió FC5, no pude contra mi curiosidad, y dije...
¿qué tal darle una mirada antes de despedirnos?

El problema es que como no quería bajar los 5 CDs que componen Fedora,
bajé solo la imagen de inicio, que permite crear un CD (o un miniCD, ya
que apenas mide 8Mb) y arrancar Anaconda (el instalador de Fedora). Mi
idea era hacer un upgrade de Fedora Core 4 (la versión que estaba
usando), mediante la red.

Bueno, haciéndola corta, no anduvo bien. Nunca había hecho esto, y un
enlace ADSL de 256kbps no es la mejor alternativa para hacer un upgrade
de un sistema operativo completo, en línea. A la tercer vez que una
caída de alguno de los mirrors de Fedora (encima, no se me ocurrió nada
mejor que hacer la instalación JUSTO cuando salió FC5, y TODO el mundo
estaba sobrecargando los mirrors...) me abortó la instalación, decidí
que no iba a poder hacer lo que quería.

Así las cosas, tenía 3 alternativas:

-  Bajar los 5 CDs de Fedora 5, y hacer el upgrade desde CD
-  Reinstalar Fedora 4 (los CDs ya los tenía)
-  Instalar Ubuntu 5.10 (también tenía el CD, y es uno solo)

Dejas las cosas como estaban no era una opción: El upgrade había
abortado no una, sino 3 veces, dejando el OS en un estado bastante
inconsitente. No perdí nada de datos (además, tenía un backup), y
arrancaba perfecto, y se podía usar, pero era un híbrido entre Fedora 4
y 5, con librerías mezcladas, que a la larga seguro iba a dar problemas.

Me decidí por Ubuntu. Después de todo, ese era el plan... solo que se
adelantó.

El cambio no es menor. Si bien hay muchas distribuciones de Linux, puede
decirse que que hay dos grandes ramas ancestrales: `Debian`_ y `Red
Hat`_. Si es por historia, también está `Slackware`_ (de hecho, fue la
primera distro), pero —hasta donde se— no hay derivados de Slackware. Y
en algún punto intermedio puede ponerse a `SUSE`_, que si bien creo que
tampoco tiene derivativos, y en sus inicios se basó en Red Hat, es una
distro muy importante. Desde que empecé a usar Linux, siempre usé Red
Hat. Cuando Red Hat creó el proyecto Fedora, empecé a usar Fedora.
Siempre me mantuve en la línea Red Hat.

Ubuntu, es un derivado de Debian. Y si bien en el uso diario, normal,
común, no hay diferencias (las aplicaciones, librerías y la base del
sistema operativo son las mismas), cuando uno empieza a escarbar un poco
la superficie (cosa que a mi me gusta hacer), ahí si aparecen algunas
diferencias. Algún archivo de configuración que se llama distinto,
alguna cosa que está en otro directorio, herramientas de configuración
de bajo nivel diferentes, el sistema de gestión de "paquetes"
(instalación y actualización de software) es diferente, etc. Pero
bueno... pensé que me iba a costar más. Todavía no he jugado demasiado
tiempo como para hacer un juicio definitivo, pero en principio diría que
me voy a adapar mucho más rápido (y fácil) de lo que pensaba.

Ahora si, lo que en algún momento iba a ser el propósito específico de
este post...

¿Por qué el cambio?
-------------------

Fedora es una muy buena distribución, y me ha dado muchas
satisfacciones. Pero en mi humilde opinión, por más que Red Hat haga
ENORMES esfuerzos por desmentirlo, y gritar a los 4 vientos que no, el
desarrollo de Fedora sigue FUERTEMENTE influido por la agenda de Red
Hat, y no por una comunidad de usuarios. Y la agenda de Red Hat es
desarrollar tecnologías nuevas que le permitan vender mejor el producto
enterprise, que es con el que ganan dinero. Y para Red Hat, Fedora es un
"banco de pruebas".

Y acá quiero abrir un paréntesis: Eso no tiene nada de malo *per se*, y
es absolutamente lógico. Quizás lo único que critico es que Red Hat no
sea suficientemente claro al respecto. Supongo que para aquel al que le
interesa meterse de lleno en el desarrollo de nuevas tecnologías, en las
entrañas de proyectos como GNOME, y cosas así, Fedora es una excelente
distro. Red Hat ha aportado y sigue aportando mucho al software libre, y
a Linux y GNOME en particular. Varios de los grandes hackers de la
comunidad son empleados de Red Hat, y muchas tecnologías que hoy son
moneda corriente en GNU/Linux fueron ideadas, desarrolladas o mejoradas
por esta empresa.

La cuestión es que me fui dando cuenta que yo no encajo en el target de
usuarios al que Fedora —explícitamente o no— está apuntando. Soy un
"power user", me gusta programar, me gusta experimentar, me gusta tener
una distro de Linux con los últimos avances... pero a su vez quiero algo
pulido, quiero un Desktop en el que pueda trabajar.

Y básicamente Fedora tiene una historia de haber descuidado algunos
aspectos para el usuario final, en favor de hacer a tiempo a incluir
determinada tecnología "enterprise". Primero fue `SELinux`_, ahora es
`XEN`_. Y si bien (al igual que Ubuntu) saca una nueva versión cada 6
meses, Fedora se caracteriza por meter como updates estables MUCHAS más
actualizaciones que Ubuntu. Y esto cada vez me va gustando menos: Todas
las semanas hay decenas de megas de actualizaciones para bajar, y la
calidad final del producto se resiente, porque no todo está debidamente
testeado. Hay cosas que se rompen, y permanecen rotas por semanas o
meses.

Así que decidí migrar a Ubuntu por eso. Porque creo que Ubuntu está
claramente más orientado al desktop. Por eso, por ejemplo, se distribuye
en un solo CD: Porque hay miríada de cosas que no se instalan (aunque
están disponibles para instalar desde internet, con un par de clicks).
Con Ubuntu, uno obtiene un desktop moderno y estable, sincronizado
también con GNOME. Yo soy libre de instalar todo el resto. Hay
actualizaciones frecuentes, pero por lo que estuve averiguando, no tanto
como Fedora, y el resultado final es más estable, más pulido. El tiempo
dirá si estoy en lo cierto.

Y si bien atrás de Ubuntu también hay una empresa, `Canonical Ltd.`_,
sus objetivos respecto a Ubuntu (al menos por ahora) están más claros
que los de Red Hat respecto a Fedora. Ubuntu ha hecho ENORMES progresos
en su corta vida. Y la comunidad está mucho más integrada al proceso de
desarrollo. La agenda y los objetivos son mucho más abiertos. No hay
"secretos". No hay mensajes en la lista de correo del estilo "Por
razones fuera de nuestro control el lanzamiendo de próxima versión se va
a demorar 15 días" (como en Fedora), sino un mensaje público dando los
motivos por los que se DESEA (no "decide") postergar el lanzamiento, e
invitando a todos los interesados a debatirlo en un chat abierto, en dos
horarios diferentes (hasta eso cuidan: que mientras una mitad del
planeta trabaja, la otra está durmiendo). Creo que ese tipo de cosas
(podría tirar un par de ejemplos más de ese estilo) resumen las
diferencias entre un proyecto y otro.

Canonical se apoyó en Debian, que, por lejos, representa la comunidad
más fuerte, y con mayor tradición de manejarse bajo las reglas del
sofware libre y de código abierto. Y Ubuntu heredó mucho de eso. Ubuntu
es el producto final de Canonical.

Red Hat apunta a las empresas Fortune 500. Red Hat necesita vender
contratos de soporte y mantenimiento de Red Hat Enterprise Linux. Red
Hat no está del todo dispuesto a dejar que una comunidad de usuarios y
desarrolladores externos le maneje la agenda. Fedora representa una cama
de pruebas para Red Hat. Fedora no es el producto final de Red Hat.
Fedora es (como mínimo) un "Release Candidate" —por no decir beta...— de
las tecnologías y mejoras a introducir en Red Hat Enterprise Linux.

Como alguna vez Facundo me dijo, "esa es la diferencia entre trabajar
CON la comunidad, o pretender que la comunidad trabaje PARA vos".

Veremos como me va con Ubuntu. Después de todo, tampoco estoy cerrando
todas las puertas. Como dije al principio, Fedora me parece una de las
mejores distros gratuitas que hay disponibles. Y si Ubuntu me
decepcionara... supongo que volvería a Fedora. Hoy por hoy, no veo otra
alternativa que me guste más.

 

 

.. _Ubuntu: http://www.ubuntu.com
.. _Fedora Core: http://fedoraproject.org/wiki/
.. _Debian: http://www.us.debian.org/
.. _Red Hat: http://www.redhat.com/
.. _Slackware: http://slackware.com/
.. _SUSE: http://www.novell.com/linux/
.. _SELinux: http://www.nsa.gov/selinux/
.. _XEN: http://www.cl.cam.ac.uk/Research/SRG/netos/xen/
.. _Canonical Ltd.: http://www.canonical.com/
