.. title: Ubuntu 6.10 en Dell Inspiron 640m
.. slug: ubuntu-6-10-en-dell-inspiron-640m
.. date: 2007-01-20 16:05:02 UTC-03:00
.. tags: dell,GNU/Linux,laptop,Software,ubuntu
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Este es un resumen de la configuración de Ubuntu 6.10 en mi nueva
laptop. Hace unos días había dicho que pretendía instalar Feisty Fawn
(la versión de desarrollo de Ubuntu 7.04, que está en alfa 2), pero un
bug en el actual kernel de esa versión me impidió hacerlo. Probablemente
vuelva a intentar con alguno de los próximos alfas (hay previstos 5,
creo).

Entonces, volviendo al tópico que nos ocupa, vamos a ver como me fue
instalando, en lo que respecta al soporte de hardware. Fue toda una
experiencia: Primera laptop, primera vez que instalo un OS en una
laptop, y atrás, tenía el historial de haber ido siguiendo (en foros,
listas de correo, blogs y demás) la evolución de Linux en este tipo de
hardware... que ha hecho montones de progresos, pero tiene en su haber
algunos capítulos tortuosos :)

En mi caso en particular, decidí usar el CD de instalación
"alternativo", ya que quería absoluto control sobre como particionar el
disco, y además, quería configurar LVM.

Preparación del disco
---------------------

-  Defragmenté la unidad C: de Windows
-  Inicié un Linux reciente desde CD (en mi caso, usé el LiveCD de
   Ubuntu 6.04)
-  Usando el editor de particiones de Gnome, achiqué la partición de
   Windows a 20GB, sin tocar nada más. Mi intención era achicarlo más...
   pero finalmente lo dejé de 20GB por si decido instalar un stack
   completo de desarrollo de .NET. Así todo es un montón de espacio.
-  Reinicié Windows, y dejé que el scandisk chillara e hiciera su
   trabajo al encontrarse con que le habían tocado su disco por afuera.
   ¡Maricón! :p

Una vez que me aseguré que Windows seguía feliz en su casa achicada,
volví a arrancar con Linux, y ahora sí, realicé los otros cambios:

-  Eliminé la partición de Dell MediaDirect;
-  Eliminé la partición de recuperación de Dell;

¿Por qué hice esto en 2 pasos? Porque ajustar una partición NTFS sigue
siendo algo relativamente experimental. Con lo cual, quería tocar lo
menos posible la tabla de particiones antes de dejar que Windows pudiera
verificar su unidad.

Instalación de Ubuntu 6.10
--------------------------

No voy a cubrir el proceso de instalación (menos el del Alternate CD)
acá; solo mencionaré algunos detalles (que no necesariamente son
aplicables a todo el mundo, en particular en cuanto al layout de disco).

-  Use el modo de particionado manual. Creé una partición extendida
   ocupando todo el espacio que quedaba. Dentro de esta, creé una
   partición de 100MB para /boot, y otra de 1GB para swap. En el resto,
   creé un grupo de volúmenes LVM, con 3 volúmenes lógicos: Uno de un
   tamaño inicial de 10GB para /root, otro de 4GB para /home, y el
   último de 20GB para /opt. El resto del disco quedó dentro del volúmen
   físico, pero sin asignar. Eso me permitirá agrandar o achicar las
   particiones de Linux dinámicamente en función del espacio que vaya
   necesitando.
-  Cuando llegó el momento de instalar GRUB (el boot manager), elegí
   instalarlo en la partición /boot, y NO en el MBR. Esto lo hice para
   no correr el riesgo de perder alguna funcionalidad en el arranque
   manejado por Dell. Quizás fui demasiado paranoico. La verdad, no lo
   sé :)

El resto de la instalación... sin novedades.

Configuración del arranque
--------------------------

Si uno instala GRUB en el MBR, listo. Pero si no, se termina con un
Linux instalado pero sin poder arrancarlo. Hay que "enseñarle" a NTLDR
(el boot manager de Windows) a hacerlo. Esto está explicado en miles de
lugares, pero básicamente los pasos son:

-  Iniciar con un Linux desde CD;
-  Copiar el primer sector de la partición de arranque de Linux en un
   archivo;
-  Arrancar Windows;
-  Copiar el archivo que contiene el sector de arranque de Linux en C:,
   y configurar una entrada en el boot.ini haciendo referencia a ese
   archivo;

Probando Ubuntu. Ajuste fino
----------------------------

Listo. Solo faltó arrancar Ubuntu, y entrar a probar. Anduvo
prácticamente todo "out-of-the-box":

-  Touchpad;
-  Notificación de estado de la batería;
-  Ajuste dinámico del brillo de la pantalla al (des)enchufar la laptop;
-  Hibernación;
-  Suspend;
-  Detección del cierre de la tapa;
-  Teclas especiales de la laptop;
-  Manejo de la frecuencia de clock de la CPU en función de la demanda;
-  Placa de red;
-  Lector de tarjetas;
-  ... en fin, todo. O casi todo.

¿Entonces...?

¿Qué no anduvo, o no anduvo bien?
---------------------------------

Básicamente 3 cosas:

-  Resolución correcta del LCD (en formato wide). Tuve que instalar el
   paquete "915resolution", reiniciar el modo gráfico, y salió andando.
   Hay reportes de que en las últimas versiones de Xorg, si cambio el
   driver "i810" (que es el default para la placa integrada Intel 950)
   por "intel", no hace falta el 915 resolution, pero no lo probé.
   Primero quiero investigar que otras diferencias tiene un driver
   respecto del otro.
-  Placa de red inalámbrica. Acá el problema es que no se instalaron los
   módulos restringidos del kernel. Solo tuve que instalar el paquete
   "linux-restricted-modules-generic", y reiniciar. Y listo. A partir de
   ahí, anduvo todo, hasta la autenticación WPA (yo tuve que pelearme un
   rato con eso, pero por ignorancia mía...)
-  Ajuste del brillo de la pantalla "a mano", usando el teclado.
   Aparentemente es un bug del módulo de gestión de energía del kernel
   que se disparó partir de cierta versión de BIOS de Dell (en laptops
   con BIOS anteriores funciona ok). Acá es donde tuve que hacer magia
   negra: agregar el módulo "video" a la lista negra de módulos en
   /etc/modprobe.d/blacklist. No entiendo muy bien por qué, ni que otro
   efecto colateral tiene eso (si tiene alguno, no lo he notado), y no
   deja de ser un workaround feo, pero anda. Ahora puedo apretar Fn+Up o
   Fn+Down y manejar el brillo de la pantalla sin problemas.

¿Conclusión? Una maravilla. 100% del hardware autodetectado, configurado
y funcionando correctamente, con solo 3 ajustes manuales.

Incluso activé AIGLX en la configuración gráfica, e instalé Compiz.
Funciona perfecto. Efectitos 3D, transparencia, blah, blah. Todo el
eye-candy de moda. Tengo algunos glitches con la hibernación y el
suspend (no funcionan 100% ok el 100% de las veces), pero dejando de
lado eso, está todo super estable. Ningún cuelgue, ningún error crítico.
Nada.

Y estoy absolutamente maravillado con la performance de este bichito, a
pesar de que el gestor de energía del kernel me pone los dos cores al
50% de su velocidad la mayor parte del tiempo. Tengo que hacer algo muy
muy pesado para que el kernel diga "ok, necesitás más procesador, te voy
a dejar usar el 100% de lo que compraste" :p Y en ningún momento tuve
problemas de performance. La ventaja de dejar que el kernel haga su
laburo a demanda, es que como consecuencia de tener los cores de la CPU
laburando al 50%, el equipo trabaja re-silencioso (casi nunca se
encienden los ventiladores), y apenas tibio. No calienta prácticamente
nada.

.. figure:: http://farm1.static.flickr.com/154/363692900_2282fa52f8.jpg
   :target: http://farm1.static.flickr.com/154/363692900_2282fa52f8_o.png
   :alt: Ubuntu 6.10 en Dell Inspiron 640m
   :align: center

   Ubuntu 6.10 en Dell Inspiron 640m

Por último, hay algunas cosas que aún no probé (algunas ni siquiera en
Windows), y no se si funcionan ok o no:

-  Modem
-  El slot ExpressCard (no tengo con qué...)
-  La salida DVI
-  La salida VGA
-  La grabación de CDs/DVDs (la reproducción anda perfecto; la grabación
   de CDs la probé en Windows; la grabación de DVDs no la probé en
   absoluto)
-  La entrada de micrófono

