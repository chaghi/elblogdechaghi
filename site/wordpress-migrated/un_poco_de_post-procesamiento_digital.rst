.. title: Un poco de post-procesamiento digital
.. slug: un_poco_de_post-procesamiento_digital
.. date: 2010-02-23 23:17:29 UTC-03:00
.. tags: Fotografía
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Últimamente estoy mirando muchas fotos. Principalmente en Flickr. Mirar
fotos de otra gente, especialmente cuando se trata de fotógrafos pro o
semi-pro, es una gran fuente de inspiración. Se pueden obtener muchas
ideas de como tomas que a uno le podrían parecer estúpidas y jamás
harías, en la práctica quedan buenísimas. Y esas son las fotos que decís
"guau!". Mirando y mirando, como que tu ojo y tu cerebro van
incorporando el hábito de mirar distinto cuando uno busca una toma.

También, cuando uno empieza a mirar fotos sacadas por gente que sabe,
empieza a descubrir que más allá de la toma en sí, que es sin dudas lo
más importante, por goleada, generalmente hay un laburo de
post-procesamiento. Puede ser algo mínimo, para mejorar el resultado, o
puede ser algo más agresivo, para obtener una imagen con un toque
artístico, aunque tal vez sacrificando algo de realismo.

De a poquito me fui interesando más en todo esto. Antes tenía muchos
prejuicios respecto al post-procesamiento. En seguida pensaba medio
despectivamente "ah, pero esa foto está *photoshopeada*", como si fuera
un pecado. ¿y saben qué? Como muchos prejuicios, es erróneo. Porque si
sacaste la foto en una condición de luz sub-óptima y estás perdiendo
detalle en las sombras, está bueno ajustar un poco el contraste y
recuperar el detalle oculto, por ejemplo. Si tenías el balance de
blancos en auto, y había una mezcla de luz medio rara, y la cámara le
pifió, está bueno ajustar eso en lugar de tener una foto verdosa, o
azulada, o lo que fuera. O sea, está bueno usar el post-procesamiento
digital para ayudar a que la imagen se acerque más a lo que vos estabas
viendo cuando tomaste la fotografía.

Después de las últimas vacaciones, cuando me puse a hacer la selección
de fotos, le dediqué bastante tiempo a esto. Hay muchas fotos que fueron
levemente retocadas, principalmente en cuanto a contraste, curvas y
niveles. Jugué bastante en el GIMP con la técnica de aplicar una máscara
de contraste. Pueden profundizar el tema `por ejemplo acá`_ (y en mil
lugares más). Básicamente se trata de superponer sobre la imagen
original, la misma imagen pero des-saturada (en B/N), invertida, y
desenfocada. Es una forma más sofisticada/selectiva de ajustar el
contraste de una foto. Es una técnica re-simple, y hace maravillas.

El otro día estuve investigando sobre otras técnicas de
post-procesamiento, específicamente mirando cosas más artísticas. O sea,
no en plan "arreglemos esta foto", sino en plan mostrar algo diferente.

Tone Mapping y Haze removal
---------------------------

Esas dos técnicas quedan buenas aplicadas juntas. Son técnicas de
realce, si se aplican levemente, pueden pasar bastante desapercibidas, y
no necesariamente afectar el realismo de la imagen.

Para hacer tone mapping se puede usar un plugin, pero también se puede
hacer a mano. Yo estuve jugando bien "a pedal", para entender bien el
efecto y experimentar más a conciencia. Básicamente la técnica consiste
en triplicar la imagen obteniendo 3 capas. A la capa superior se la
des-satura, se la desenfoca, se le da algo de transparencia, y se la
combina con la capa del medio. Y luego se toma esta nueva capa y se la
combina con la original en modo "luz tenue". `Acá`_ tienen un ejemplo
explicado. `Y acá`_ uno que muestra lo mismo pero usando un plugin
específico de The GIMP que automatiza el laburo.

Haze removal es una técnica de realce que queda buena sola o como
complemento de la anterior. Se trata simplemente de ajustar los niveles
(algo re-simple de hacer, que el GIMP hasta puede hacer automáticamente,
y muchas veces es un simple click que mejora notablemente una foto...),
y luego se aplica una leve máscara de desenfoque.

Esta es una foto que tiene aplicadas estas dos técnicas:

.. figure:: http://farm5.static.flickr.com/4052/4383751450_c31881f857.jpg
   :target: http://www.flickr.com/photos/chaghi/4383751450/
   :alt: Horses
   :align: center

   Horses

Efecto Orton
------------

Cuando vean el efecto que produce esta técnica, van a decir "si! esto lo
vi aplicado mil veces!". Es una técnica decididamente artística, que
cierto tipo de imágenes (por ejemplo, macros de flores) queda muy
interesante. Esta técnica debe su nombre al tipo que la iventó.
Idealmente, para aplicarla, uno debería tener 2 tomas: Una
sobre-expuesta por 1 stop, y otra sobre-expuesta por 2 stops. Si no se
dispone de esto, lo siguiente recomendable es tener el original en
formato RAW, para hacer la sobre-exposición de manera digital. Y si no
se dispone de eso (como en mi caso), y bueno... se pueden generar estas
sobre-exposiciones usando el JPG original. No es lo ideal, pero anda.

`Acá <http://osp.wikidot.com/orton-technique>`__ hay un ejemplo de como
se aplica la técnica. Ese tutorial parte de la imagen en formato RAW, yo
hice algo similar con el GIMP y un JPG. La técnica en resumen consiste
en tomar la imagen sobre-expuesta por 1 stop, ajustarle los niveles,
abrir la copia sobre-expuesta por 2 stops como una capa sobre la
primera, aplicarle un desenfoque gaussiano (cuanto más agresivo el
desenfoque, más fuerte será el efecto de la técnica), y combinar ambas
capas.

Acá está mi primer experimento con la técnica Orton. Me encanta el
resultado:

.. figure:: http://farm3.static.flickr.com/2719/4383748992_e9f9f42c16.jpg
   :target: http://www.flickr.com/photos/chaghi/4383748992/
   :alt: Lonely notro
   :align: center

   Lonely notro

Si no se abusa, produce un efecto medio etéreo, surrealista, bastante
particular. Y si se abusa... a veces también queda bueno :)

En la página de Flickr de las dos fotos que puse acá está el link a las
que usé como originales. Está bueno ver el antes y el después. Lo iba a
hacer acá en el artículo... pero me dió fiaca, y lo que me importaba más
en este caso era mostrar el resultado final.

Esto son solo dos ejemplos de dos técnicas básicas muy usadas.

Disclaimer para cualquier persona que sepa de post-procesamiento digital
y lea esto: no soy fotógrafo, me gusta la fotografía como hobby; recién
estoy empezando a descubrir el inmenso mundo del post-procesamiento
digital... así que si encontrás alguna barbaridad en lo que escribí,
avisame, así lo arreglo... y de paso aprendo.

 

.. _por ejemplo acá: http://www.gimp.org/tutorials/ContrastMask/
.. _Acá: http://gimpaddict.googlepages.com/tonemapper.html
.. _Y acá: http://osp.wikidot.com/tone-mapping
