.. title: A veces no hay nada mejor que un editor "de verdad", como Vim
.. slug: a_veces_no_hay_nada_mejor_que_vim
.. date: 2007-07-06 21:09:23 UTC-03:00
.. tags: Software,vim
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

(Emacs fans: ya sé que `Emacs`_ es también un editor de verdad... pero
el punto de este post no es Vim vs Emacs)

Desarrollar en ASP.NET con C# sin Visual Studio .NET es complicado. O al
menos Microsoft se esfuerza bastante en que así sea. Y cuando uno tiene
que trabajar en equipo, es complicado si cada uno usa su propia
herramienta... así que en el laburo todos usamos VS. Como todo super
IDE, tiene cosas buenísimas, cosas más o menos, y cosas malas. Como
editor de texto... está bastante bien mientras uno hace cosas
estándares. Pero no es la primera vez que me pasa que para hacer una
edición "de verdad", no queda otra que recurrir al viejo y querido
`Vim`_ (que es mi editor de elección en otras plataformas / proyectos
personales / lenguajes).

Imagínense que tienen una clase que expone unas 200 propiedades de este
estilo:

.. code:: csharp

   ///
   /// Kms Extendidos para Traslados
   ///
   public int KmsExtendidosTraslados
   {  
       get
       {
           return ((int)_sesionInfraestructura.ValorParametro("KmsExtendidosTraslados", "Cantidad de Kms a partir de la cual se considera Extendido", "GEN", "E", "50"));
       }
   }

... y tienen que transformarlas a TODAS, siguiendo este estilo:

.. code:: csharp

   ///
   /// Kms Extendidos para Traslados
   ///
   private int? _kmsExtendidosTraslados = null;
   public int KmsExtendidosTraslados
   {  
       get
           {
               if (!_kmsExtendidosTraslados.HasValue)
                   _kmsExtendidosTraslados = (int)_sesionInfraestructura.ValorParametro("KmsExtendidosTraslados", "Cantidad de Kms a partir de la cual se considera Extendido", "GEN", "E", "50");
               return _kmsExtendidosTraslados.Value;
           }
   }

En este momento, no importa demasiado que hace ese código, ni el por qué
del cambio (aunque creo que para más de uno puede ser bastante obvio,
aún fuera de todo contexto...).Lo imporante, es que hay unos cuantos
"desafíos":

-  hay que declarar una variable privada del mismo tipo, pero nullable,
   e inicializada en null;
-  la variable se llama igual que la property, pero en minúscula, y con
   un "_" delante;
-  la invocación al recupero del parámetro queda dentro de un if, que
   controla si el nullable tiene o no valor;
-  la invocación al recupero del parámetro no es más parte del return,
   sino que se asigna a la variable privada;
-  el return devuelve el valor del nullable;

Y todo esto, teniendo en cuenta que:

-  no todas las properties son del mismo tipo de datos;
-  obviamente todas se llaman diferente;

Digamos que no era un trabajo para "copy & paste". Se puede perder buena
parte de un día de trabajo haciendo eso (y lo triste, es que a veces, se
hace!)

¿Solución?

**Enter Vim**

Me llevó unos 15' minutos, haciendo un par de pruebas, grabar una macro
tal que parado en la línea donde arranca la property (el "public int
..."), se re-escribía automagicamente la property al nuevo formato. Y
hacía rato que no hacía estas cosas en Vim, así que no menos de la mitad
de ese tiempo se fué googleando para recordar ciertos comandos de
selección y movimiento relativo.

Una vez escrita la macro, el refactoring de toda esta clase con sus
aproximadamente 200 propiedades no llevó más de 5 minutos (solo había
que hacer un search de las líneas que arrancan con "public", y ejecutar
la macro en cada una).

¿Vim es la única herramienta para hacer cosas así? No, imagino que no.
Nobleza obliga, hay que reconocer que Ezequiel estuvo a un pelito de
hacer algo parecido con `Notepad++`_ (un editor "de verdad" para
Windows, MUY recomendable si no quieren aprender Vim...)

Pero ciertamente es la clase de cosas para las cuales Visual Studio (y
para el caso Sharp Develop, Eclipse, Mono Develop, y cualquier otro
mega-IDE) sencillamente NO SIRVE.

Quizás podría haberse encarado esto mediante algún search&replace usando
expresiones regulares... pero realmente hay que tenerla bastante clara
en expresiones regulares para escribir una que realice ese laburo (y así
y todo tengo mis reparos: hay casos en los que el parámetro es un
string, y su valor por defecto (el último argumento del método
ValorParametro) puede ser por ejemplo una URL, con sus correspondientes
caracteres extraños). No es mi caso. Y si bien Vim tiene su barrera de
entrada para los que no saben usarlo... me parece que es más fácil (y
útil en muchos más escenarios) aprender a usar Vim, que hacer una
maestría en expresiones regulares.

Me parece que en el toolbox de TODO programador que se precie, debería
encontrarse el uso medianamente "avanzado" de algún editor de verdad. Si
nunca te topás con este tipo de refactorings, es que nunca participaste
de un proyecto de desarrollo grande. Y si te topaste y lo resolviste
reescribiendo el código a mano durante todo un día... estás perdiendo tu
preciado tiempo haciendo un laburo repetitivo, aburrido y horrible, con
el correspondiente riesgo a introducir bugs en el camino, solo por no
usar la herramienta correcta.

 

.. _Emacs: http://es.wikipedia.org/wiki/Emacs
.. _Vim: http://es.wikipedia.org/wiki/Vim
.. _Notepad++: http://notepad-plus.sourceforge.net/es/site.htm
