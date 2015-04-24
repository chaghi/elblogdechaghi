.. title: Nuevo diseño
.. slug: nuevo-dise-o
.. date: 2007-04-30 03:00:45 UTC-03:00
.. tags: General,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Actualización: El diseño del que se habla en este artículo fue cambiado
nuevamente en febrero de 2011, `al migrar a WordPress`_.

Hacía unas cuantas semanas que venía cocinando este, el nuevo diseño del
sitio.

Siempre me faltan "5 pa'l peso", así que no lo instalaba. Durante el
finde hice varios retoques, y si bien las cosas aún no están 100% como
querría, decidí igual instalar el nuevo template. Con un poco de suerte,
usándolo termino de pulir todos los detalles, y los lectores regulares
hacen saltar todos los bugs (sobretodo con MSIE sobre Windows).

Este nuevo layout pretende ser "elástico", en el sentido que no es
"fluído" (como el diseño anterior, que se estiraba a toda la pantalla,
fuera esta lo ancho que fuera), ni tampoco es "fijo". Si tienen una
resolución alta, se va a estirar, pero hasta cierto punto máximo. Y para
abajo, las cosas están pensadas para que se vean (relativamente) bien en
800x600, que sigue siendo una resolución muy usada.

¿Por qué todo esto? Se juntaron 3 cosas: Quería hacer un cambio visual,
meramente desde lo estético. Quería limpiar un poco el layout del diseño
anterior, ya que no andaba muy bien en IE, se "rompía" fácilmente al
insertar imágenes o algún otro contenido sin tener cuidado con los
tamaños, y era un lío a nivel CSS (con un montón de definiciones que no
usaba, ni sabía para que estaban), y a nivel HTML también. Quería
mejorar la usabilidad/legibilidad, y tener un texto "estirado" ocupando
1200 pixels o más no es algo que contribuya a esto (no por nada los
sitios de los diarios meten columnas, como en la edición impresa...)

Estuve investigando bastante, leyendo, probando distintos CSS, buscando
ideas, probando templates de LifeType de distintos autores... y
finalmente, llegué a esto. Es una mezcla del theme de WordPress
`lineSide`_, de Nurdin Jauhari, que migré a LifeType, más algunas ideas
de layouts "elásticos" que fui mezclando (el diseño original de Nurdin
es de ancho fijo), en particular, del blog de `Roger Johansson`_, un
señor que sabe de estas cosas y me cae simpático porque es sueco :)

Y así queda, más o menos. Hay unos cuantos detalles por pulir. Bastante
contenido de la sidebar que saqué, y que todavía tengo que decidir si
reincorporo (banners, links, etc.). Tengo que terminar de experimentar
como se ve en Windows, en particular respecto a las fuentes que estoy
usando. Tengo que implementar un CSS para impresión. Quiero meter algún
"badge" de Flickr con fotos. Y más.

Pero todo eso, lo iré resolviendo de a poco en los próximos días.
Mientras tanto, salimos así, medio en beta. Si encuentran algo
definitivamente roto, o muy feo, avisen. Y obviamente se aceptan
sugerencias / críticas respecto al cambio.

.. _al migrar a WordPress: link://slug/mira-mira-ahora-uso-wordpress
.. _lineSide: http://themes.wordpress.net/testrun/?wptheme=2469
.. _Roger Johansson: http://www.456bereastreet.com/archive/200504/about_fluid_and_fixed_width_layouts/
