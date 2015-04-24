.. title: Exoditus en Python
.. slug: exoditus_en_python
.. date: 2007-09-30 18:32:57 UTC-03:00
.. tags: Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

En varios posts anteriores creo haber mencionado (a veces al pasar, y a
veces no tanto), al generador de código que usamos en el laburo en los
desarrollos .NET, a quien su autor, `Darío`_, denominó Exodus. No, el
nombre no es arbitrario... pero en todo caso le tocará a Darío algún día
escribir sobre ello en su propio blog... :)

Sin entrar en detalles (je! a ver si avivamos giles y perdemos la
ventaja competitiva que nos da!), digamos que es una herramienta
mediante la cual se define el "dominio" de una aplicación, generalmente
haciendo algo de introspección sobre el modelo de datos (o sea, sobre la
base de datos a usar), y genera automáticamente un montón de código
boilerplate: el mapeo entre el ORM y la base de datos, "finders" para
recuperar datos, consultas y ABMs estándares (al estilo de las que
genera por ejemplo Django), las `fachadas`_ y `business delegates`_ (en
el laburo, a pesar de usar .NET, usamos muchos de los patrones
arquitectónicos de J2EE) y un sinfín de cosas más.

La herramienta es fantástica, e imprescindible: Creo que sería imposible
desarrollar sistemas del tamaño de los que estamos generando, si
tuviéramos que escribir todo eso a mano, cada vez (y si cada vez que
tocáramos el modelo de datos, tuviéramos que ir manualmente a reajustar
TODOS los lugares en los que pega). A pesar de todo, desde el comienzo
que hay algo que me "molesta" (muy entre comillas, porque en definitiva,
FUNCIONA, y bien), y es que internamente, el core de Exodus no deja de
ser un template engine, que toma una descripción del dominio de la
aplicación, y una serie de plantillas, y escupe código (o más
académicamente hablando, "text artifacts" (¿ahí les gusta más?)). Y el
problema es que usa un template engine custom, y peor, ese template
engine usa un lenguaje scripting custom, que tiene varias limitaciones
(se han tenido que hacer cosas "raras" en las plantillas, y en el código
generado, por limitaciones en los tipos de datos que maneja este
lenguaje, por ejemplo). Y sobre todo, es LENTO. Esto hasta ahora no era
un problema, pero en el proyecto en el que estoy trabajando desde hace
varios meses, que es MUY MUY grande, regenerar código lleva más de 10
minutos.

Ninguna de las dos cosas constituyen una limitación "insalvable". De
nuevo, funciona, funciona ok, el código no se regenera a cada rato, no
todos los proyectos son tan grandes, y cada vez que nos topamos con
alguna limitación a nivel de templates... Darío encontró un workarround.

Pero la cuestión es que a mí el tema me seguía dando vueltas en la
cabeza... y siempre tenía en la cabeza una vocesita diciendo "que bien
que vendría Python y alguno de los tantos templates engines que tiene
acá..."  Encima, Exodus desde hace un tiempo atrás tiene embebida una
consola de IronPython, que sirve para levantar "on-the-fly" el modelo
antes de generar código, y jugar un poquito. Todavía no le hemos dado
mucho vuelo... pero es cool :)

Hace unos meses atrás, mejorando el esquema de remoting estándar que
usan nuestras aplicaciones, se presentó un problema "recursivo": Ciertos
Business Delegates dependían del código escrito por nosotros (no del
auto-generado), con lo cual en principio no se podían generar con
Exodus... y ahí nació "Exoditus", que no es más que un hook de
post-compilación de parte del proyecto que levanta el core de Exodus,
levanta el assembly recién compilado con la lógica de negocios, mediante
reflection extrae algunas propiedades, genera código adicional, y sigue
compilando. Nice.

Este fin de semana, decidí poner manos a la obra, y ver si podía, como
experimento y prueba de concepto, re-escribir Exoditus en IronPython.
Elegí Exoditus porque es lo más fácil de reemplazar. Hoy por hoy, aunque
la idea funcione, reescribir todos los templates y modificar Exodus para
que "dialogue" con este esquema ya no es tan trivial (aunque tampoco lo
veo como algo muy complejo). En cambio Exoditus bien puede no depender
para nada de Exodus; es un paso intermedio en la compilación. Nada más.
Y solo UN template.

Bueno, el experimento funcionó. La parte más compleja, fue encontrar un
template engine que funcionara BIEN en IronPyhon. Los template engines
que hay suelen (todos) hacer uso de mucha magia negra y de features de
CPython que aún no funcionan en IronPython. Luego de algunas pruebas, y
con la ayuda de Google, el candidato elegido fue `Cheetah`_. Buenísimo.
Quizás no sea el ciudadano más ilustre por estos días, con todo el buzz
alrededor de Django, TurboGears y cía., y los template engines
orientados al desarrollo web. Pero es un producto maduro, estable, en
producción, rápido... y MUY poderoso.

Así que prueba superada: pyExoditus se compone de +/-90 líneas de
código, de los cuales el 70% se va en dos métodos que realizan
introspección sobre un assembly que recibe como parámetro, para extraer
nombres de clases y métodos que cumplen ciertos patrones, un template,
Cheetah, y unos 32 módulos de la stdlib de Python (me tomé el laburo de
identificar uno a uno cuales eran, para poder armar un "paquete"
autocontenido con todo lo necesario que no requiera tener CPython
instalado para andar). La buena noticia: No solo anda, sino que anda
sensiblemente más rápido :)

No se si terminará metido o no en nuestro estándar de desarrollo... pero
en cualquier caso, fue divertido y productivo. Y si termina metido,
quizás sea el primer paso para apuntar a otro objetivo: Darío está en
estos momentos escribiendo la versión 2.0 de Exodus, con muchas mejoras
y cambios estructurales... quizás... solo quizás, Exodus 2.0 podría usar
como template engine a Cheetah, y como scripting language a Python...

 

.. _Darío: http://kblok.blogspot.com/
.. _fachadas: http://java.sun.com/blueprints/corej2eepatterns/Patterns/SessionFacade.html
.. _business delegates: http://java.sun.com/blueprints/corej2eepatterns/Patterns/BusinessDelegate.html
.. _Cheetah: http://www.cheetahtemplate.org/
