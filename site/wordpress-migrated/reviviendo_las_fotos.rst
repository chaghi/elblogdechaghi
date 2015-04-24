.. title: Reviviendo las fotos
.. slug: reviviendo_las_fotos
.. date: 2005-09-16 03:19:57 UTC-03:00
.. tags: Software,Viajes
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Cuando migré a `pLog`_ 1.0, en mi capricho de explotar a fondo las
"friendly URLs" (eso que hace que la URL permanente de los posts sea
algo como post/fecha/título), dejaron de andar los álbumes de fotos
integrados de pLog. No terminé de encontrar nunca el problema, se que es
algo mal configurado, pero no pude resolverlo. Ni me interesó demasiado,
porque el gestor de galerías que viene con pLog no me gusta \*nada\*.

Como directamente ahora las fotos no podían verse de ninguna manera, me
puse las pilas para encontrar otra solución.

Instalé `MG2`_, por un lado porque es una de las alternativas que me da
el proveedor del servicio de hosting, pero principalmente porque me
gustó: es chiquita, configurable, "skineable", fácil de usar, no
necesita una base de datos, se ve bien... ¡y funciona en "PHP safe
mode"! (que es la configuración que muchos servicios de hosting —y el
mío no es la excepción— usan para aumentar la seguridad).

Primero la instalé desde DattaPanel, la herramienta de administración de
mi proveedor. Pero los permisos quedaban mal, y además era una versión
vieja. Así que instalé a mano la última versión. Fácil, muy fácil... por
suerte, porque si hay algo que le falta a MG2, es documentación. A full.

Luego, vino la tarea de migrar las fotos. La interfaz administrativa de
MG2 me facilitó mucho la tarea. Permite subir todas las fotos de una vez
e "importarlas", sin obligar al usuario a usar una interfaz web lenta
para hacer los uploads. Lo tedioso, fue pasar las descripciones de las
fotos. No quería perderlos, y no había una manera automática de hacerlo
(¿ven? Acá falta un estándar. Cada software almacena esta "metadata" a
su manera...). Como eran solo 4 álbumes, decidí que iba a ser más rápido
tipearlos otra vez que ponerme a bucear en las tablas de MySQL de pLog y
hacer algún script. Así que me pasé un buen rato reescribiendo los
detalles en cada foto... fue divertido, porque rememoré muchos gratos
momentos :) Otra vez, la interfaz de MG2 me facilitó las cosas. Por
ejemplo, luego de editar una foto, automáticamente salta a la edición de
la siguiente. Es una boludez, pero ahorra un montón de tiempo.

En resumen, si bien no está probado a fondo, hasta ahora, estoy muy
contento con MG2. Seguro es muy superior a la alternativa de pLog.

Ya está todo migrado. El link del menú apunta a la nueva ubicación de
las galerías. Y para ahorrarles arrastre de mouse `les dejo también el
link acá`_ :p

Fíjense que les parece. Si encuentran algún problema, por favor chiflen.
Voy a dejar pasar unos días, y después de eso, voy a borrar
definitivamente las galerías viejas.

.. _pLog: http://www.plogworld.net/
.. _MG2: http://www.minigal.dk/
.. _les dejo también el link acá: http://chaghi.com.ar/albums/
