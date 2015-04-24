.. title: Mirá mirá, ahora uso Wordpress!
.. slug: mira-mira-ahora-uso-wordpress
.. date: 2011-02-05 00:25:44 UTC-03:00
.. tags: General,lifetype,wordpress
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Acabo de terminar el "trasplante" de blog, digamos. Para los no
informáticos: le cambié el motor al blog, antes usaba uno de una marca,
y ahora le puse uno de otra. El cambio debería ser transparente, excepto
por las diferencias de diseño, que dicho sea de paso, no son
definitivas. El diseño actual es el que viene por defecto, después con
más tiempo voy a jugar con eso.

Para los informáticos o aquellos que quieran saber algo más: Me estaba
cansando de algunas limitaciones de LifeType (el engine anterior), que
además excepto por algún que otro minor release por temas de seguridad
está virtualmente freezado. La supuesta nueva super versión está
bastante retrasada en el desarrollo, y encima será compatible solo con
PHP>=5 (que mi hosting actual no me da).

Así que me puse a evaluar alternativas. Primero pensé en algo basado en
Python, pero no encontré ningún engine que no me haga caer de nuevo en
un nicho (i.e., un engine usado por muy poca gente, con poca masa
crítica, como el que quería cambiar) o que esté maduro o que... (varias
cosas). Y por otro lado el hosting me limita bastante también en lo que
es Python.

También pensé en migrar el contenido de alguna manera a un servicio como
Tumblr o Posterous, pero la migración no era simple, y si bien me saco
de encima el mantenimiento del blog, también pierdo control. Y corro el
riesgo de quedar "locked-in" en un servicio de estos, y que si después
me quiero ir (y llevarme el 100% de mi contenido, e importarlo en otra
cosa), podría llegar a ser en el mejor de los casos muy complicado (y en
el peor, imposible).

Así que quedaron las opciones obvias: Wordpress, Drupal, MovableType. Y
ganó Wordpress. Y acá estamos.

La migración fue más simple de lo que esperaba. Resulta que Wordpress
tiene herramientas de importación para varias cosas, pero no para
LifeType. Buceando un poco en la red encontré un plugin que alguien
había escrito en la época que LifeType se llamaba pLog, y que migraba de
esa versión (vieja) a Wordpress 2.0 (viejo). Terminé instalando un stack
LAMP en la PC de casa, junto con Wordpress 3.0.4 y un backup de la base
de datos de LifeType, y a toquetear el plugin hasta arreglar algunas
cosas. No fue tan complicado. Lo que más importaba, que son los posts
con sus categorías y comentarios, se importaron perfecto. Tuve problemas
con las categorías de enlaces y los enlaces, pero como en LifeType tenía
definidos muy pocos enlaces (y los que tenía son recontra viejos,
algunos inválidos, e incluso el theme que estaba usando ni los
mostraba), decidí comentar esa parte de la importación. Lo único que no
se importó (porque el plugin ese ni lo contempla, y a mi me dió mucha
fiaca ponerme a investigar como hacerlo) son los trackbacks... una pena,
pero bueno. De todos modos, obvio me queda backup de la base para ver si
en los próximos días invento algo.

¿Y ahora? Ahora nada, me voy a dormir. Ya le dediqué bastantes horas a
todo esto. Por delante queda buscar un theme copado y en español y
gratis (difícil!), instalar varios plugins que me interesan, ver si hay
que hacer alguna magia para evitar el spam y esas cosas, decidir si
vuelvo a meter Google adSense, o si aprovecho la movida y dejo de
molestar con publicidad que no me está dando ningún beneficio.

En una palabra, ahora falta tratar de sacarle el jugo a Wordpress, y ver
si todo esto me ayuda a tener el blog un poco más activo. LifeType se
estaba transformando en una barrera.

El formato de permalinks quedó igual, y como también mejoré el script de
importación para que use el "slug" de LifeType (en lugar de
recalcularlo), los enlaces permanentes de los posts deberían ser
exactamente igual a los de antes. De todas maneras tengo que revisar
algunas reescrituras de URLs que antes hacía en el .htaccess con
mod\_rewrite, que tengo que ver si ahora siguen teniendo sentido o no.

El feed RSS lo manejo con FeedBurner, así que a menos que estés
suscripto directamente al feed que proporcionaba LifeType, esto debería
ser transparente. El feed de los comentarios era directo, y también
cambió, así que si estás suscripto... se rompió :P En los próximos días
probablemente haga alguna magia en el .htaccess para seguir soportando
las URLs viejas, pero igual sería bueno que te re-suscribas a los feeds
nuevos:

-  http://feeds2.feedburner.com/ElBlogDeChaghi (el feed principal)
-  http://chaghi.com.ar/blog/comments/feed/ (el feed de comentarios)

Por favor, si ves algo que no funciona, ¡avisá!
