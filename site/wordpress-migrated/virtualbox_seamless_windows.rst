.. title: VirtualBox 1.5 - Seamless windows
.. slug: virtualbox_seamless_windows
.. date: 2007-09-01 23:23:52 UTC-03:00
.. tags: GNU/Linux,Software,virtualizacion
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

¿Notan una mezcla rara en este screenshot?

|VirtualBox 1.5 Seamless windows|

:)

Es un nuevo chiche de la versión 1.5 de `VirtualBox`_. La llaman
"Seamless windows", y lo que hace VB en este modo es ocultar el
escritorio del sistema operativo guest (Windows XP Home en este caso),
para lograr una mayor integración con el host.

Por ahora, únicamente funciona para Windows como "guest", y no al revés,
y requiere que sí o sí el sistema operativo virtualizado tenga
instaladas las "guest additions".

Ya había visto (aunque no probado) experimentos similares usando QEMU, y
también pruebas sobre VirtualBox, pero en ambos casos usando un feature
de Windows Terminal 6 (o superior) que permite que el cliente en lugar
de recibir el escritorio completo de Windows pueda recibir solamente la
ventana activa. Entonces, el truco era correr Windows virtualizado en
background, y luego abrir alguna aplicación mediante el cliente Terminal
Server de Linux. Pero esto tiene varios drawbacks:

-  Es bastante complejo de configurar / administrar

-  Funciona únicamente para Windows, y solamente versiones de windows
   que tengan implementado el RDP (Remote Desktop Protocol), lo cual te
   limita a versiones Professional o Enterprise (no Home) de Windows XP
   o superior.

-  Por una limitación de RDP, solo se puede trabajar con una aplicación
   simultánea (aunque creo que algunas versiones de Windows, o con
   configuraciones especiales, esta limitación podía salvarse).

El approach que eligió VirtualBox me gusta más. Si bien por ahora
funciona solo con Windows, funciona en CUALQUIER Windows en el que sean
instalables las Guest Additions. No depende de ninguna configuración de
networking entre host y guest. Puedo abrir todas las ventanas y
aplicaciones que quiera. Y calculo que a futuro implementarán esto
también en las guest additions de Linux y MacOS. Mi impresión personal
es que arrancaron con Windows porque hay más usuarios que corren Windows
sobre Linux que al revés.

Y lo más lindo: Funciona out of the box. No tuve que hacer nada más que
actualizar VirtualBox, arrancar la virtual machine que tiene instalado
Windows, actualizar las Guest Additions también a 1.5... y listo. Con
CTRL-L conmuto entre el modo seamless y el normal.

 

.. _VirtualBox: http://www.virtualbox.org/

.. |VirtualBox 1.5 Seamless windows| image:: https://farm2.static.flickr.com/1174/1298214399_c514b68175.jpg
   :target: https://www.flickr.com/photos/chaghi/1298214399/
