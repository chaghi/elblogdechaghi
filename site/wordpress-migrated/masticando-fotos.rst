.. title: Masticando fotos
.. slug: masticando-fotos
.. date: 2011-09-04 14:08:00 UTC-03:00
.. tags: exif,flickr,Fotografía,matplotlib,Python
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Estoy en vías de actualizar mi cámara de fotos. Los por qué, y cual es
la cámara que quiero serán materia de otro post (¡suspenso!), ya que la
decisión no fue fácil, y tiene varias aristas. Y además es una excusa
para hacer otro post y hacer de cuenta que tengo un blog y escribo
regularmente (?)

Pero una de las primeras cuestiones con las que me topé, es que si
pretendía ganar en "profesionalismo" de la cámara, iba a tener que
sacrificar zoom. Mi cámara actual, una `Canon PowerShot S5 IS`_, entra
en la categoría bridge/prosumer, pero a su vez, super zoom. Tiene un
zoom de 12X (sí, OK, *hoy* no es tanto para una super zoom, pero cuando
la compré, era una barbaridad).

Y resulta que las cámaras compactas más pro, como las "PowerShot G" de
Canon o las "Coolpix P" de Nikon, tienen bastante menos zoom. Y las
cámaras reflex vienen con un lente estándar con mucho menos zoom, y si
bien se le puede poner el lente zoom que uno quiera, hay que considerar
dos cosas: el precio del lente, y que un lente de más de 300mm (o
incluso menos) para una reflex es un *Señor Lente* (en tamaño y peso),
no muy "trekking friendly". Y lo mismo que aplica a las reflex aplica a
las nuevas mirrorless / EVIL / micro four thirds / etc.

Así que de entrada quedó claro que si iba por una compacta pro (no super
zoom) o por una reflex, iba a sacrificar longitud focal.

Inmediatamente me surgieron un montón de preguntas: ¿cuánto uso el zoom
de mi cámara? ¿qué porcentaje de fotos saco con un zoom óptico mayor a
5X? ¿qué valor tienen para mi las fotos que saqué con un zoom grande,
tipo 10X, 12X? ¿son fotos buenísimas que no querría haberme perdido por
nada del mundo?

Algunas de esas preguntas eran complicadas de responder con certeza,
pero básicamente decidí asumir el riesgo y seguir mi investigación sobre
cámaras bajándole la prioridad al tema zoom. Tenía la impresión
subjetiva de que no era un tema *tan* importante.

En algún momento, ya ni recuerdo como, porque en las últimas semanas he
leído una cantidad escandalosa de reviews, opiniones, blog posts, etc.,
etc. sobre cámaras, caí en este interesante artículo: `Photo Statistics:
Aggregating EXIF data to see how I shoot photos`_. Y eso me abrió el
camino a encontrar una respuesta certera a mis preguntas/dudas sobre
como aprovecho la longitud focal del lente de mi cámara actual. Resulta
que...

-  ... las fotos más importantes / interesantes las tengo subidas a
   `Flickr`_.
-  ... Flickr `expone los datos EXIF`_ de las fotos (a menos que los
   ocultes, cosa que yo no hago).
-  ... Flickr\ `tiene una API`_ que permite acceder por software a la
   información de las fotos, sin necesidad de tener que mirarlas una por
   una en la web
-  ... Python es un lenguaje de programación hermoso y divertido, que
   últimamente tengo medio olvidado, y en el que es realmente muy fácil
   escribir un programita que acceda a mi cuenta de Flickr, y recupere
   la metadata EXIF de todas mis fotos, los mastique, me de las
   respuestas que busco, y encima me las grafique.
-  ... hace rato que busco alguna excusa para volver a escribir algo
   simple en Python, para recordarme a mi mismo que programar puede ser
   muy divertido cuando no tenés que lidiar con problemas boludos de
   clientes idiotas y/o hardware lento y/o restricciones de Microsoft :)

Así que puse manos a la obra, y en un par de horas tenía 80 líneas de
Python que resolvían el tema de bajar los datos de Flickr. Considerando
que hacía rato que no escribía nada en Python desde cero, y que no
conocía las bibliotecas que necesité usar (principalmente, `FlickrAPI`_,
aunque alguna vez, en otra vida, usé ese código como base para armar un
Remember The Milk API), me di por satisfecho.

Dejé el script corriendo un largo rato (bajar la info de todas las fotos
no es muy rápido, y encima el script no tiene absolutamente ninguna
optimización, y tampoco estoy seguro de estar usando la API de Flickr
eficientemente y no estar haciendo requests al pedo), y terminé con toda
la data que necesitaba en formato JSON.

El resto fue fácil: levantar esa data, y empezar a obtener las
respuestas que necesitaba (usando Python también, ¡obvio!). Y hoy estuve
jugando un rato con `matplotlib`_ y haciendo algunos dibujitos con la
data.

Pasen y vean que lindas tolderías:

|(gráfico de Apertura vs Longitud Focal)|

Conclusiones sobre fotografía
-----------------------------

No uso mucho el zoom. De un total de 1800 fotos en Flickr tomadas con la
S5 IS, solo un 17% están tomadas con un zoom mayor a 5X. Y si bien
porcentualmente 17% es bastante, una rápida mirada por varias de esas
fotos me confirma que no son obras maestras. Las únicas fotos en las que
el zoom 12X garpó y mucho, fueron en un par de `fotos de la luna`_. Así
que a lo sumo tendré que sacrificar el fotografiar la luna.

Esto es consistente con el tipo de fotos que saco: paisajes, macros,
algún que otro retrato. Todas situaciones en las que el zoom se usa poco
y nada. Las longitudes focales largas están normalmente asociadas con
"action shots", deportes, y fotografía de "vida salvaje", y es un tipo
de fotografía que no practico, o porque no es mi tema, o porque si bien
me alcanzaría el zoom, mi cámara está limitada en otros aspectos que
también son clave en esas situaciones: una buena velocidad de disparo,
una buena velocidad en obtener foco, buena calidad de imagen con ISOs
altos, por ejemplo.

En resumen: creo que podría vivir con un zoom moderado.

Conclusiones sobre programación
-------------------------------

Programar en Python es fácil y divertido. Esto ya lo sabía, pero se me
estaba olvidando.

Programar para resolver algo que te interesa resolver a vos es mucho más
interesante que programar para resolver algo que a otro le interesa que
le resuelvas. Otra cuestión que debería tener más presente, aunque
parezca una verdad de perogrullo.

Programar concentrándote en resolver tu problema, y no en convencer a un
compilador de que estás resolviendo el problema de la manera correcta
(i.e., programar con tipado dinámico vs programar con tipado estático)
permite llegar al resultado mucho más rápido, y podés ocuparte de las
refinaciones después. Otra perogrullada y van...

No voy a publicar el código porque los tres o cuatro scripts que hice
son un asco y me da vergüenza. Tal vez invierta algo de tiempo en
convertirlos en algo que califique de "programa", y no de
revoleo-de-sentencias-de-python, y los suba a algún lado. En algún
momento. Pero no se si vale la pena. Anyway, si estás interesado en
conocer más detalles sobre algo de todo esto, preguntá, y vemos...

.. _Canon PowerShot S5 IS: link://slug/mi_selecci_n_de_camara_digital_bridge
.. _`Photo Statistics: Aggregating EXIF data to see how I shoot photos`: http://www.filosophy.org/2011/06/photo-statistics-aggregating-exif-data-to-see-how-i-shoot-photos/
.. _Flickr: https://www.flickr.com/photos/chaghi/
.. _expone los datos EXIF: https://www.flickr.com/photos/chaghi/6036708189/meta/in/photostream
.. _tiene una API: https://www.flickr.com/services/api/
.. _FlickrAPI: http://stuvel.eu/flickrapi
.. _matplotlib: http://matplotlib.sourceforge.net/
.. _fotos de la luna: https://www.flickr.com/photos/chaghi/4331616464/lightbox/

.. |(gráfico de Apertura vs Longitud Focal)| image:: /blog/wp-content/uploads/2011/09/Aperture-vs-Focal-Length-1024x1024.png
   :target: /blog/wp-content/uploads/2011/09/Aperture-vs-Focal-Length.png
