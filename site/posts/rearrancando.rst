.. title: Rearrancando...
.. slug: rearrancando
.. date: 2015-04-26 21:56:41 UTC-03:00
.. tags: nikola,Python,wordpress
.. category: 
.. link: 
.. description: Un intento más (y van...) de revivir el blog 
.. previewimage: https://farm1.staticflickr.com/176/428041211_009f451d70_o.jpg
.. type: text
.. author: cHagHi

.. figure:: https://farm1.staticflickr.com/176/428041211_009f451d70_o.jpg
   :target: https://www.flickr.com/photos/arenamontanus/428041211/
   :class: islink
   :alt: Restart, human!
   :align: right

   Restart, human! por Anders Sandberg

Nueva casa, nueva tecnología, nuevo formato. Todo es nuevo. Menos el
contenido, que está abandonado hace casi un año. Y que ya venía semi
abandonado antes de eso.

Ya ni los ¿clásicos? `posts sobre los viajes <link://tag/viajes>`_
estoy haciendo. Hay por lo menos dos que no están acá. Y es una pena. 
Esto nunca fue muy popular, ni tuvo muchos lectores, pero siempre fue un 
buen ejercicio esto de escribir, y más de una vez fue interesante en lo 
personal volver para atrás y releer algunas cosas. Y eso que he escrito 
cada pelotudez... :p Pero nada, las pelotudeces también son interesantes. 
Es interesante ver como uno cambia, o como el mundo cambia, y contrastar 
lo que pensaba, sentía o vivía mi "yo" de hace X tiempo con mi "yo" actual.

Y cada tanto, cada muy tanto, hasta llegué a escribir algo que le sirvió a
alguien. Y eso también está bueno.

¿Y por qué dejé de hacerlo? No se muy bien, pero en general siento que la
culpa es de Facebook y Twitter. Es mucho más fácil escribir una gilada
de 140 caracteres en Twitter o un par de párrafos en Facebook que ponerlo
en un blog.

----------

Para motivarme un poco, porque uno ante todo es nerd (?), decidí demoler el
blog anterior y armarlo otra vez. Estoy usando `Nikola <http://getnikola.com>`_,
mascota de `Roberto Alsina <http://ralsina.me/weblog/>`_, que resulta que
además de recomendar muy buenos libros, desarrolla muy buenos generadores
de sitios estáticos ;-) (¡gracias Roberto!)

La principal ventaja para mi de haber migrado a Nikola es que ahora el
contenido del blog está en `archivos de texto <./index.rst>`_, en un formato 
que es legible por un humano incluso sin la magia que lo transforma en 
páginas web.

La segunda ventaja es que está desarrollado en Python, que es un lenguaje
de programación que me gusta *hasta el infinito y más allá* más que PHP (que
es lo que usa WordPress), y que me resulta mucho más fácil de entender 
cuando necesito tocar algo, o agregar funcionalidad, o hacer modificaciones.

La tercer ventaja es que Nikola es minimalista. No tiene las decenas de
características que tiene WordPress, ni sus miles y miles de *plugins*. Tiene
lo que necesito. Es más simple. Y cuando uno no necesita la complejidad
extra, *"simple es mejor que complejo"* [*]_.

Migrar de WordPress a Nikola es algo que es más o menos automático en un
75%, pero si sos *obse* como yo y realmente querés emprolijar las cosas,
requiere luego una serie de ajustes que dependen de cuan horrible sea el
formato heredado de WordPress. Para algunos de esos ajustes fui haciendo
reemplazos semi-automáticos con distintas herramientas, para otros tuve 
que ir a mano (y para esos casos, que no fueron taaaaantos, agradecí no haber
estado escribiendo con más frecuencia :p). En todo este proceso me vino de
10 la experiencia previa de
`Humitos <http://elblogdehumitos.com.ar/posts/migrar-post-de-wordpresscom-a-nikola/>`_.

Todavía tengo cosas que ajustar, como los *tags* y *categorías*, o hacer
que el sitio tenga un *look* un poco menos genérico. Y otro gran tema es
encontrar un mecanismo cómodo para poder publicar desde el celu/tablet, o
una compu desde la que no tenga acceso al servidor. Esto es medio una 
desventaja común a todos los generadores de sitios estáticos. Hay varias
opciones, pero todas requieren algún trabajillo extra, todas tienen
algún pero, y va a requerir un poco más de tiempo evaluar que es lo que
más me conviene.

Pero la base está...

----------

Para terminar el revoleo, el blog no está más alojado en un *hosting
compartido*. Me llevé todo a un `VPS <http://www.digitalocean.com/?refcode=11907d74e265>`_.
Y eso también es toda una novedad, y en parte un desafío, porque tengo que 
administrar absolutamente todo yo. Es un arma de doble filo: puedo hacer lo 
que quiera en el servidor, y por lo tanto también puedo romper todo. Y tengo 
que tener un ojo puesto en todo lo que sea configuración, actualizaciones,
seguridad, etc.

Al pasar a un VPS hay una cosa que estaba seguro que **no** quería administrar:
las cuentas de correo de mi dominio. Administrar un servidor de correo propio
es, para mi, "ligas mayores" (para hacerlo razonablemente bien), así que
tuve que encontrar una solución, preferentemente gratuita. En una época la
respuesta obvia a esto era *Google Apps*, pero no es más gratis. Por 
recomendación de Roberto (que además de recomendar buenos libros, y de
desarrollar buenos generadores de sitios estáticos, hace buenas recomendaciones
de servicios en la nube), el correo de mi dominio quedó en `Zoho 
<https://www.zoho.com/>`_, que ofrece un plan gratuito que me alcanza y sobra.

Y acá estamos. Todo nuevito. Ahora solo falta escribir...

----------

.. [*] El Zen de `Python <http://es.wikipedia.org/wiki/Python#Filosof.C3.ADa>`_
