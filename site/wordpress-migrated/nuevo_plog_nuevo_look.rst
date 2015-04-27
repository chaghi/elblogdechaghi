.. title: Nuevo pLog, nuevo look
.. slug: nuevo_plog_nuevo_look
.. date: 2005-04-09 19:23:25 UTC-03:00
.. tags: General,plog,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Para festejar la `migración a pLog 1.0`_, decidí cambiar de look. Como
el estilo transitorio que estuvo funcionando luego del cambio
(Mac-Stripe) me gustó bastante, decidí usarlo como base... y ver que
salía.

Y salió esto. Lo más visible es el cambio de grises a azules y celestes.
Pero a su vez: reordené el panel lateral izquierdo, moví el form de
búsqueda (una nueva feature de pLog) a la cabecera, quité el calendario
(¿a alguien le sirve? ¿por qué todos los creadores de templates se
emperran en ponerlo?), agregué la sección de posts recientes, agregué mi
referrer de Firefox (pero pasándolo casi abajo de todo... pasado el
furor del lanzamiento de la versión 1.0, ya no tenía sentido un lugar
"tan" privilegiado como el que tenía antes) y el Emblema Hacker. En
cuanto a los posts, saqué el enlace "permanente", e hice que el título
de cada post lo fuera (como antes), agregué la hora, y reinstalé el
plug-in que permite generar la versión "printer-friendly" (que ya fue
portado a 1.0). Todo el grupete de links relacionados con el post lo
ubiqué debajo del título, y no al final del post, a excepción del link
de "Comentarios" (que me parece mucho más natural que esté ubicado
debajo).

El template Mac-Stripe no validaba como XHTML Strict, así que estuve un
buen rato ajustando eso (jeje... ¿fanático yo?).

Otro cambio visible, y a su vez también nuevo feature de pLog 1.0, son
las "URL Personales". Con esa funcionalidad, ahora los links a la
información publicada son mucho más naturales, quedando algo tipo

-  ``http://www.chaghi.com.ar/blog/post/2005/02/28/fin_de_semana_de_cine``
   en lugar de algo como

-  ``http://chaghi.com.ar/blog/post/1/28``
   o peor aún,

-  ``http://chaghi.com.ar/blog/index.php?op=ViewArticle&articleId=28&blogId=1``

Finalmente, apliqué dos pequeños patches a pLog, ya que las "URL
Personales" de las galerías y el archivo histórico no estaban
funcionando.

Creo que ahora sí funciona todo. A lo mejor todavía realice algún que
otro cambio estético más, pero en general, estoy conforme con el estilo
"minimalista" que quedó, así que por lo menos hasta que me aburra, no me
voy a alejar demasiado de este look.

.. _migración a pLog 1.0: link://slug/actualizando_plog
