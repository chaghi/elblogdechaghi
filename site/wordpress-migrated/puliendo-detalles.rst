.. title: Puliendo detalles
.. slug: puliendo-detalles
.. date: 2006-11-04 17:40:28 UTC-03:00
.. tags: General,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

El plugin tagcloud que se menciona en este artículo fue desactivado el
23/11/06 hasta nuevo aviso. Permanentemente tenía que agregar a la lista
negra palabras que son frecuentes en lo que escribo pero que no tienen
relevancia semántica como "tag", y por otro lado, no funciona
correctamente con caracteres acentuados.

Continuando con las pilas renovadas por el cambio de hosting, estuve
haciendo algunos cambios adicionales a los que comentaba `acá`_.

Por un lado, pulí un poco más el nuevo sidebar para mostrar los últimos
comentarios. Ahora es más visible el nombre o nick de la persona que lo
hizo.

Además, agregué un nuevo plugin, `tagcloud`_, el cual podrán ver en
acción también en el panel de la izquierda, en la nueva sección **¿De
qué hablo?**. Fue divertido ponerlo a funcionar. Este bicho funciona
contando las palabras más frecuentes en los últimos N posts, las ordena
alfabéticamente, y a cada palabra le da un tamaño proporcional a su
frecuencia. Es como una especie de categoría virtual. Además de la
cantidad de palabras a mostrar, uno puede controlar: la longitud mínima
que una palabra tiene que tener para que la contemple, cuántos posts
tiene que evaluar, y además hay una lista de palabras a omitir.

El plugin viene con esa lista preconfigurada para inglés. Lo primero que
hice, fue agregar todas las preposiciones del castellano. Y así y todo,
estuve jugando como una hora, agregando los verbos comunes del español
en varias de sus conjugaciones más comunes. El idioma español es mucho
más rico y expresivo que el inglés; cuando hay que hacer estas cosas, se
nota. Anyway, ahora muestra resultados más o menos relevantes. Costó,
pero salió. ¿Acaso los sorprende ver cuales son las palabras (temas) más
frecuentes en mi blog? ;) Bueno... a mí no, pero me sorprendió un poco
que Python y PyAr no ranquearan mejor.

Cada palabra es un link a una búsqueda dentro del blog que retorna los
artículos que contienen esa palabra. 

Y mientras estaba en eso... decidí hacer algo similar para las
categorías. No pude encontrar publicado ningún plugin que lo hiciera,
así que juntando mi experiencia de la semana pasada escribiendo
`ayearago`_, y robando MUCHAS ideas del plugin *tagcloud*, escribí
`categorycloud`_. Me encanta esa idea de ponderar una lista de palabras
usando una "nube".

Hay un problema que me molesta bastante y todavía no pude resolver que
tiene que ver con la hora en que quedan registrados los artículos y los
comentarios. Pasa que arreglarlo implica reconfigurar algo en LifeType,
pero al mismo tiempo, tocar a mano directamente en la base de datos la
información de fecha/hora para los artículos y comentarios viejos. Algo
que no pienso hacer hasta tanto no instale en mi máquina una instancia
de MySQL en la que pueda bajar un backup de la base de datos del blog
para probar el update tranquilo.

Sé que Facundo tiene en su lista de 10 cosas pendientes con su blog este
tema también. Quien les dice... como últimamente está con pilas para
`Taniquetil`_, quizás me gana y hace ese ajuste primero, y después me
pasa el script.

 

.. _acá: http://chaghi.com.ar/blog/post/2006/11/01/Nos-mudamos
.. _tagcloud: http://wiki.lifetype.net/index.php/Plugin_tagcloud
.. _ayearago: http://wiki.lifetype.net/index.php/Plugin_ayearago
.. _categorycloud: http://wiki.lifetype.net/index.php/Plugin_categorycloud
.. _Taniquetil: http://www.taniquetil.com.ar/plog/
