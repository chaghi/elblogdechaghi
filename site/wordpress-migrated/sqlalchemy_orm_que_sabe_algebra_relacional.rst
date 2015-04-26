.. title: SQLAlchemy: Un ORM que sabe de álgebra relacional
.. slug: sqlalchemy_orm_que_sabe_algebra_relacional
.. date: 2007-09-02 17:15:15 UTC-03:00
.. tags: orm,Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Hace algunas semanas que estoy leyendo la doc y haciendo algunos
experimentos "caseros" (descolgados, sin ningún propósito concreto de
momento) con `SQLAlchemy`_.

SQLAlchemy es, al mismo tiempo, un set de herramientas de acceso a SQL 
**y** un ORM. Y resalto el "y". Es la primera herramienta de estas
características que veo que implementa este concepto de separar
claramente, e incluso como cosas usables de manera independiente, las
dos caras de la moneda: El "lidiar" con SQL desde una aplicación
(sobretodo para consultas), y el mapear un modelo de objetos a una base
de datos.

Traducción libre de la página principal del sitio:

    Las bases de datos SQL se alejan más del comportamiento de una
    colección de objetos a medida que la performance y el tamaño de la
    base de datos se vuelve más importante; las colecciones de objetos
    se alejan más de conceptos como tablas y filas conforme la
    abstracción se vuelve más importante. SQLAlchemy intenta acomodar
    simultáneamente estos principios.

    SQLAlchemy no ve a las bases de datos sólo como una colección de
    tablas; las ve como motores de álgebra relacional. Su ORM permite
    mapear clases contra una base de datos de varias formas distintas.
    Las sentencias SQL no solamente consultan tablas—es posible realizar
    consultas de joins, subqueries y uniones. Así, las relaciones de la
    base de datos y el modelo de objetos se desacoplan desde el
    principio, permitiendo que los dos conceptos se exploten a su máximo
    potencial.

Realmente esto no es marketing, cuando uno empieza a usar la herramienta
y analizar los ejemplos en la `documentación`_, se ve claramente que
esta filosofía se aplica... y da frutos. De todos los ORM existentes
para Python, creo que SQLAlchemy es el único considerado "de verdad", es
decir, que podría usarse en escenarios más complejos de la simple
aplicación web con 3 o 4 ABMs que normalmente se desarrollan con
`Django`_ o `TurboGears`_. Es a su vez uno de los más nuevos, pero ha
tomado la comunidad "por asalto", y me atrevo a especular que es por
lejos el que más rápidamente ha avanzado (y continúa avanzando...)

SQLAlchemy escala hacia arriba... y hacia abajo. Por ejemplo, está
creciendo bastante también un proyecto, `Elixir`_, que implementa una
capa "declarativa" sobre SQLAlchemy que resuelve de una manera sencilla
e intuitiva (muy al estilo del `Active Record`_ de `Ruby on Rails`_) los
casos más comunes.

Por último (y esto no es exclusivo de SQLAlchemy, sino extensivo a todos
los otros ORMs para Python): Cuánto más "lindo" es un ORM con un
lenguaje dinámico. Cuando hay que acercar los mundos de SQL y OOP en
Java o C#, se nota mucho el overhead de jerarquías de clases y
abstracciones e interfaces que se "apilan" para lograr algo extensible y
robusto... y que adhiera a las restricciones del tipado estático. Con
Python (o Ruby), se puede crear el puente, igualmente extensible y
robusto, de una manera mucho más directa. Gracias a 
`Darío`_ en el laburo tenemos un excelente generador de código que nos
resuelve automágicamente toda la parafernalia de código extra... si no
lo tuviéramos, calculo que estaría pidiendo a gritos que laburemos con
otra cosa... jeje.

 

.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _documentación: http://www.sqlalchemy.org/docs/04/
.. _Django: http://www.djangoproject.com/
.. _TurboGears: http://turbogears.org/
.. _Elixir: http://elixir.ematia.de/
.. _Active Record: http://ar.rubyonrails.com/
.. _Ruby on Rails: http://rubyonrails.com/
.. _Darío: http://kblok.blogspot.com/
