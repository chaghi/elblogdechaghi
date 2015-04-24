.. title: Código abierto. Cuando sí, cuando no. Mi visión.
.. slug: codigo_abierto_cuando_si_cuando_no_mi_vision
.. date: 2006-04-06 02:52:50 UTC-03:00
.. tags: Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Lo que sigue es el texto de un e-mail que envié a la lista de correo de
`PyAr`_, a partir de una `discusión`_ que se generó sobre el usar
software libre (`Python`_) para desarrollar software propietario, a
partir de un mensaje que se envió invitando a la presentación de un
producto desarrollado en Python.

Creo que el texto así como está es entendible, pero agrego un poco de
contexto: El núcleo de la discusión era por un lado la postura de que
todo el software tiene que ser libre, y otras opiniones donde la gente
resaltaba el modelo de servicios de Red Hat (y otros) para ejemplificar
como podía ofrecerse sin problema el código fuente, al mismo tiempo que
los ingresos se generaban no por la venta del software en sí, sino por
los servicios anexos al mismo (instalación, configuración, etc.)

Esta fue mi elucubración al respecto:
=====================================

El modelo de código abierto funciona perfecto en determinado software
que o bien se ha "comoditizado", o está camino a comoditizarse, o
*debería* comoditizarse.

Un sistema operativo. Un compilador. Un editor. Una base de datos. Un
servidor web. Un framework... ¿ven el patrón? Las herramientas de base.

Ahí el modelo de código abierto está perfecto, porque esas
aplicaciones son muy valiosas como HERRAMIENTAS para hacer alguna otra
cosa, pero por si solas, no son nada. A nadie le sirve una base de datos
sin datos adentro, por excelente que sea, o el mejor servidor web sin
una aplicación web que lo use.

Y por otro lado, son herramientas muy costosas de desarrollar y
mantener, en tiempo y en recursos. Y entonces el modelo colaborativo del
código abierto está excelente. Para desarrollar software de ese tipo de
forma cerrada, tenés que ser una empresa enorme (Oracle, Microsoft, IBM,
...)

El modelo de servicios de Red Hat, Novell, etc., también es
particular: El producto es estándar (es casi un commodity), muchos de
los recursos de desarrollo no tienen que ponerlos ellos (o los pone un
desarrollador de la comunidad como hobby, o los pone otra empresa (ej.,
Red Hat paga más empleados para laburar en GCC, quizás Canonical tiene
más empleados en GNOME... a la larga, ambas empresas necesitan de los
dos aportes)).

Además, un sistema operativo (que es sobre lo que "venden" servicios),
es algo que cuando se quiere deployar en una empresa, genera una miríada
de costos: de instalación, de capacitación, de certificación, de
integración, de mantenimiento, etc., etc. Si yo tengo una empresa, y
quiero que mis usuarios usen Linux, tengo dos alternativas:

-  Instalo un Debian (por poner un ejemplo de uno libre 100%), y me hago
   cargo yo de todo lo que viene atrás, de buscar ayuda en
   mailing-lists, foros, artículos en slashdot y demás;

-  Instalo un RHEL (por poner un ejemplo de uno pago), y pago una suma
   para siempre tener un 0800-Red Hat que me solucione la vida, me de
   mantenimiento, me de un ciclo de desarrollo predecible sobre los
   cambios que se efectúan en el SO, etc., etc.

Una PyME probablemente pueda usar Debian. Una empresa con 500
empleados, probablemente no.

Brindar ese servicio, no es fácil. No hay muchas empresas del tamaño
de Red Hat y Novell e IBM que puedan darlo. Y cuando un consultor
independiente viene y dice que brinda soporte para Linux, yo lo
invitaría a detenerse a pensar como sería Linux si las grandes empresas
no hubieran invertido tanto en él. ¿Habría soporte para tanto hardware?
¿Tendríamos gestores de paquetes y herramientas de administración
avanzadas? ¿Tendríamos documentación? ¿Tendríamos localización,
internacionalización, subsistemas de soporte para personas con
capacidades reducidas, etc., etc.?

Creo que si no fuera por esas empresas (que son ENORMES), Linux no
estaría donde está, y el consultor independiente tendría que dedicarse a
otra cosa.

Y alguien dirá: ¡Red Hat nació con Linux! ¡No siempre fue grande! Es
cierto. Lo mismo que Suse y otros. Pero justamente son fenómenos que se
dieron mientras Linux estaba creciendo. Hoy, ya no es posible para nadie
más ocupar esos lugares. Salvo que seas un Novell, que tengas el cash
para comprar Suse. O que seas un multimillonario africano con muchísima
plata, y seas tan atípico como para querer gastarla en fundar Canonical
(y Ubuntu) y volar por el espacio, en lugar de gastarla en un yate y
acciones de Microsoft.

Si Debian *hoy* quisiera volverse un Red Hat, no podría. Esa ventana
de oportunidad, se cerró.

El asunto es que cuando dejamos de lado las herramientas, el toolchain
de desarrollo, y los frameworks y toolkits de más bajo nivel, llegamos a
las aplicaciones que brindan un servicio agregado. A las verdaderas
"obras de arte" (lo otro, es la pintura, el pincel, el lienzo y la
paleta). Y ahí nos encontramos con tres caminos:

-  Te lo tomás como hobby, y participás de un grupo muy grande de
   desarrolladores que tienen el mismo hobby que vos, y en ratitos
   libres van implementando la aplicación. Sería el ejemplo de Totem,
   Gaim, o cualquier aplicación de las que hoy instalamos sobre Linux.

-  Te lo tomás como laburo, y lo hacés vos solo o con un equipo de gente
   mucho más reducido en una empresa. Como por ejemplo GTalk, Photoshop,
   etc.

-  Le pagás a alguien para que te lo haga.

Si lo hacés como hobby, ¿quién te da de comer? O profesionalmente te
dedicás a otra cosa (no a producir software), o trabajas en una empresa
de software que necesita VENDER para pagarte el sueldo.

¿Y vender qué? Bueno, o es una empresa grande con un producto masivo y
podemos hablar de generar y vender todos los servicios que hay alrededor
del software (sería el caso de Red Hat), o es una empresa chica (o un
producto chico) que no puede darse el lujo de ofrecer el código
abiertamente, porque pierde su única ventaja competitiva, y en
definitiva, todo el fruto de su trabajo, que es el software en sí.

En el caso de que pagues para que te hagan un software a medida,
podrías llegar a exigir como parte de las condiciones que te entreguen
los fuentes. Es algo a medida. Es algo para vos. Tenés que cubrirte si
al desarrollador original le pasa algo. Pero hay una diferencia entre
comprarle a alguien un software "a medida", o comprarle un producto. Hay
una diferencia entre entregarle a alguien el código fuente de algo
hiciste a medida para él (le sirve a él solo, o a poca gente más), o
darle el código fuente de algo que haces para muchos más clientes
potenciales.

La conclusión es (en caso de que alguien siga leyendo todavía :p) que
si TODO el software fuera libre, no habría una industria de software, y
no podríamos vivir de escribir software. Y si no pudiéramos vivir de
escribir software (que asumo que es el trabajo o la industria que nos
gusta), ¿estaríamos motivados para escribirlo? ¿habría llegado el
software hasta donde llegó? ¿estaríamos discutiendo esto?

El concepto de código abierto y software libre está muy bueno.
Podríamos decir incluso que es necesario. Pero, no es el único camino. Y
necesita del software propietario para tener sentido.

.. _PyAr: http://python.com.ar/moin
.. _discusión: http://mx.grulic.org.ar/lurker/message/20060405.162610.bbeaaf4c.es.html
.. _Python: http://www.python.org
