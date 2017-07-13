.. title: Primeras horas con WordPress
.. slug: primeras-horas-con-wordpress
.. date: 2011-02-06 17:48:30 UTC-03:00
.. tags: General,plugins,themes,wordpress
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

|Writing por jjpacres|

Bueno, follow-up sobre la `migración a WordPress`_: So far, so good,
aunque algunas cosas no me sorprenden tan positivamente como hubiera
esperado.

Customizar algunas cosas y volver a incorporar información que tenía en
la barra lateral fue MUY fácil. Realmente el sistema de widgets de
WordPress brilla en este aspecto. Así que si no fuera porque me puse
quisquilloso con algunos detallecitos, ni hubiera tenido que tocar
código y salir del panel de administración de WP para hacer esto. La
cantidad de plugins existentes es astronómica, así que no tuve que
codear (casi) nada.

Volví a poner la info de licencia, la política de privacidad (por ser
purista y cumplir con los Términos y Condiciones de adSense, aunque
todavía no volví a activar adSense), el link a los albums en Flickr, la
sección "Hace un año..." (aunque no de la forma que la tenía, en cada
post, sino en la barra lateral), los tweets recientes, los comentarios
recientes, ... blah, blah.

Lo complicado a veces es encontrar el plugin correcto. Hay muchísima
funcionalidad solapada, mucha porquería, mucho plugin para versiones
viejas de WordPress, mucha metadata incorrecta (i.e., el plugin fue
probado por última vez con WP 2.7, ponele, pero sigue andando en 3.0.4).
Pero en general luego de unas cuantas búsquedas le vas tomando la mano.
De todas maneras, el repositorio central de WordPress en ese sentido es
mejorable: Mínimo estaría bueno poder decirle "tengo WP x, MySQL y, PHP
z", y que aplique un primer filtro descartando lo que (teóricamente,
siempre que la metadata sea correcta) no te sirve. Esto es algo que no
es sencillo, lo entiendo. Mozilla por ejemplo tuvo que rever varias
veces el sistema de aprobación/inclusión de extensiones en el sitio
oficial. Tener una comunidad enorme y alentar que cualquiera contribuya
plugins es buenísimo para el ecosistema, pero también te pone una enorme
carga administrativa, y te abre brechas de seguridad, mala calidad,
bugs, etc.

Lo otro malo de muchos plugins es que no están pensados para ser
traducidos. O sea, no solo están únicamente en inglés, sino que todos
los strings están hardcodeados en inglés. Esto es tristísimo, dada la
popularidad global de WordPress como plataforma.

Anyway, las cosas que quería las encontré. Como features nuevos del
blog, agregué los clásicos botonitos para compartir en otras redes
sociales, y me registré en `BackType`_ para poder hacer tracking de los
comentarios, tweets, etc sobre los posts, importándolos automáticamente
como comentarios. No me gusta mucho que importe esta info como
comentarios directamente en la base de datos, pero no encontré nada
intermedio. No se si va a quedar... lo voy a ir testeando.

¿Y qué quedaba? ¡El Theme! Y esta es la parte que aún no pude resolver.
La situación con los themes es más triste que con los plugins. Primero,
hay bocha de sitios basura que pretenden hacer plata ofreciendo "Free
Wordpress Themes". Y son un rejunte de porquerías tan grande, que es
complicadísimo encontrar entre toda la porquería algo decente. También
me enteré gracias a un `comentario de Marcos`_ que encima muchos de
estos themes `vienen con sorpresita`_... patético :(

Con un poco más de cuidado, llegás a sitios bastante más piolas, con
cosas decentes. Los reconocés porque suelen ser empresas que ofrecen
themes "Premium" o meta-themes para escribir tus propios themes, y que
tienen una oferta limitada de algunos temas free. Normalmente tienen un
portfolio de 10, 15 temas gratis de calidad (y no 15.326.178 como los
sitios que mencionaba antes). Pero acá me encontré con otro problema:
Muchos de estos themes a pesar de su calidad no están traducidos al
español (aunque sí están preparados para ello), o son lindos pero muy
pesados, con demasiados chiches, o muy orientados a lo multimedia, pero
por sobre todo, la gran mayoría requiere PHP 5. Encontré varios que me
hubiera gustado ensayar en el blog, pero no pude por esto último.

Así que... volvimos a las bases. Creé un "child theme" de *Twenty Ten*
(el tema por defecto de WP 3.0.x), le toqué 2 o 3 giladas de CSS por
compatibilidad con el contenido que importé de LifeType, le customicé la
cabecera usando una foto tomada por mí, y listo... por ahora.

Realmente me gustaría cambiar el theme, pero encontrar algo que te
guste, que funcione bien, que no tenga sorpresas, que sea localizable (e
idealmente que ya esté traducido al español), que se ajuste a mi tipo de
blog, que sea mínimamente customizable para darle un toque personal, que
funcione con PHP4, que no sea muy pesado y que encima sea libre y
gratis, va a llevar bastante más tiempo...

.. _migración a WordPress: link://slug/mira-mira-ahora-uso-wordpress
.. _BackType: http://www.backtype.com/home
.. _comentario de Marcos: ../mira-mira-ahora-uso-wordpress/#comment-600
.. _vienen con sorpresita: http://wpmu.org/why-you-should-never-search-for-free-wordpress-themes-in-google-or-anywhere-else/

.. |Writing por jjpacres| image:: https://farm4.static.flickr.com/3447/3293117576_05f43d8305.jpg
   :target: https://www.flickr.com/photos/jjpacres/3293117576/
