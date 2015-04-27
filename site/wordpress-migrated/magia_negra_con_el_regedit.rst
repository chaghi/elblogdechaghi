.. title: Magia Negra con el Regedit
.. slug: magia_negra_con_el_regedit
.. date: 2004-11-27 16:43:07 UTC-03:00
.. tags: GNU/Linux
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Algunos amigos que solo tienen experiencia en ambientes Windows, se
sorprenden cuando yo estoy trabajando con Linux, abro una ventana de
comandos (¡sacrilegio! ¡no uso GUI!), y tiro algún comando como:

.. code:: console

   $ find . -name "struts*" | grep bin

... el cual podría llegar a parecerle mágico a alguien, pero es
perfectamente explicable:

-  ``find`` : encontrar
-  ``.`` : desde el directorio en el que me encuentro
-  ``-name "struts*"`` : aquellos archivos cuyo nombre comienza con
   'struts'
-  ``|`` : "conectar" la salida del comando anterior (su resultado) como
   entrada del siguiente
-  ``grep bin`` : filtrar el resultado y quedarse solo con las líneas que
   contienen la cadena 'bin'

Lo anterior puede parcer complejo, pero en cuanto uno utiliza unos
cuantos comandos de Unix/Linux, enseguida se encuentra un patrón, la
idea siempre es la misma, y se puede comenzar a apreciar el poder que
tiene a veces la CLI (command line interpreter) frente a una GUI
(graphical user interface)

Anoche un amigo llamó desesperado por teléfono porque había instalado el
Service Pack 2 de Windows XP, y al reiniciar la PC, descubrió que no
tenía mas unidad de CD-ROM (Windows le decía que el driver se había
cargado correctamente, pero que no podría encontrar el hardware).
Después de probar las soluciones "típicas" (ejemplo, borrar la unidad
con el Panel de Control y reiniciar para que el sistema Plug&Play
redetecte el hardware) sin poder solucionar el problema, recurrimos a
Google. Enseguida encontramos un link, que proponía lo siguiente:

-  Abrir el Editor del Registro (regedit)
-  Navegar hasta HKEY_LOCAL_MACHINE / System / CurrentControlSet /
   Control / Class / {4D36E965-E325-11CE-BFC1-08002BE10318}
-  Eliminar las claves "Upperfilters" y "Lowerfilters"
-  Reiniciar la PC

El artículo del foro terminaba diciendo que el truco podría funcionar...
o no. Por suerte, para el caso de mi amigo, el truco funcionó, y la
unidad de CD-ROM reapareció.

Ahora bien, que alguien por favor me explique, que tiene de "intuitivo"
o "amigable" la solución propuesta. ¿Acaso hay que considerarlo amigable
porque tengo una GUI (regedit) para navegar hasta esa cadena
indescifrable de letras y números, que milagrosamente vaya uno a saber
por qué hechizo vodoo controlan la visibilidad del CD-ROM luego de
instalar un Servce Pack oficial, en un Windows legítimo, instalado por
Compaq en una PC de escritorio legítima? ¿Y eso dónde está documentado?

Lo lamento. Para lidiar con la configuración de hardware, o de algún
servicio del SO, prefiero mi Linux: abro una línea de comandos (¡otra
vez! ¡sacrilegio!), voy al directorio /etc (o /proc), donde tengo
archivos planos, de texto, comentados, con nombres intuitivos, que se
vienen usando desde hace años, que puedo editar con cualquier editor de
texto.

Ah! Y por supuesto... nada me impide ir hasta ese directorio con
Nautilus, o Konqueror, o el navegador de archivos gráfico de mi
preferencia, y hacer doble click sobre el archivo que quiera para
editarlo con mi editor preferido (¡ups! ¡ni siquiera tuve que abrir la
línea de comandos!)

Nota: El título del artículo y la referencia al hechizo vodoo fue
inspirado por Facundo
