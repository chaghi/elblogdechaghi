.. title: Mundo virtual
.. slug: mundo_virtual
.. date: 2007-05-23 15:33:57 UTC-03:00
.. tags: Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Como parte de los freebies que Lucio y Alecu trajeron de `PyCon 2007`_,
y que repartieron en la `última reunión de PyAr`_, me ligué una licencia
de `VMware Workstation`_ 5.5. Así que hace un par de semanas la instalé
en la laptop, y estuve experimentando un poco.

Tiempo atrás había estado jugando un poco con VMware Player, que es el
producto gratuito, y también con `QEMU`_, una alternativa OpenSource que
funciona bastante bien (y es el core de algunos features nuevos de
virtualización que se están integrando directamente en el kernel de
Linux), pero que realmente carece de herramientas amigables para usarla.
Eso, sumado a las limitaciones de VMware Player, y que mi desktop no es
muy rápido, hicieron que en aquel momento no pueda jugar mucho.

Antes de eso, la última vez que había usado VMware había sido en el
laburo anterior. Hace más de 4 años. Y era tan, pero tan tan tan lento,
que no pasaba de una curiosidad tecnológica.

Hoy, en mi laptop, con un micro más poderoso, y una herramienta de
virtualización más nueva, lo primero que digo es "guau!". Cómo avanzó
esto de la virtualización. Con razón está causando tanto "ruido" en el
mundo de IT como opción para bajar costos, y con razón están surgiendo
tantos proyectos... la performance es casi-nativa. Buenísimo.

Para ampliar el horizonte, quise evaluar también algunas de las
alternativas comparables a VMware en funcionalidad, pero libres. El
candidato número uno era `Xen`_, pero en mi caso no me sirve, porque
depende sí o sí de un micro con las extensiones de virtualización de
Intel o AMD, cosa que yo no tengo. Así que me puse a probar
`VirtualBox`_, que es un producto muy nuevo, de una empresa alemana, que
se basa en parte en QEMU, pero agrega toda (o gran parte de) la
funcionalidad de Vmware Workstation.

En mi situación, donde no necesito sí o sí una herramienta de
virtualización, y las estoy evaluando para "ver que onda", con el
objetivo de máxima de transformar mi Windows XP de la laptop en una
máquina virtual dentro de Linux (para lo poquísimo que uso Windows en
forma personal, hincha bastante las pelotas tener que rebootear cuando
quiero usarlo), la decisión está peleada. En performance son muy
parecidos. VirtualBox viene avanzando rapidísimo. VMware tiene más
pulidas algunas cuestiones, como la integración con herramientas de
desarrollo de software (para hacer cosas como debuggear una aplicación
corriendo en el guest dentro de VMware desde el VisualStudio instalado
en el host), el manejo de snapshots, herramientas para manipular la VM
una vez creada, etc. Pero VirtualBox tiene mejor soporte para algunos
detalles menores (USB me anduvo de una, en VMware no, el sonido en VB me
anduvo de una, en VMware no, el touchpad, el teclado, el driver de
video, me gusta más como funciona en VB, y cosas así).

Y pinta que están pesando más esos detalles menores, ya que las
funcionalidades extra grossas igual no las uso, así que no me importa si
(por ahora) VB no las tiene. Además, *hoy* tengo una licencia "free"
de Workstation... pero ya salió la versión 6, y el upgrade sale USD
100.- que no pienso gastar ni a palos solo "para probar". Y las opciones
gratuitas de VMware son más limitadas que VB. Con lo cual si me caso con
VMware Workstation, me voy a quedar atrás (en la versión 5.x), o tarde o
temprano voy a tener que migrar a una versión superior... y para hacerlo
en forma legítima, tendré que poner bastante dinero. No, gracias.

Así que hoy por hoy la mejor opción de virtualización para alguien que
no necesita soporte de 64 bits, ni tiene un micro con extensiones de
virtualización, que entra en el target de "hobbista", y no quiere gastar
plata, parecería ser VirtualBox.

Veremos si en algunas semanas más este producto se transforma en la
"casa" de mi Windows XP Home.

 

.. _PyCon 2007: http://us.pycon.org/TX2007/HomePage
.. _última reunión de PyAr: http://python.com.ar/moin/Eventos/Reuniones/Reunion22
.. _VMware Workstation: http://www.vmware.com/es/products/desktop/ws_features.html
.. _QEMU: http://fabrice.bellard.free.fr/qemu/
.. _Xen: http://www.xensource.com/
.. _VirtualBox: http://www.virtualbox.org/
