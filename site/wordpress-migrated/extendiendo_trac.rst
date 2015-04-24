.. title: Extendiendo Trac
.. slug: extendiendo_trac
.. date: 2007-11-13 23:08:19 UTC-03:00
.. tags: Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

En el trabajo ya hace bastante tiempo estamos usando `Trac`_, con
bastante éxito. Tiene sus limitaciones, ya que manejamos muchos
proyectos, y sobretodo para la gente que tiene que coordinar más de un
proyecto, se vuelve muy tediosa la falta de una "vista consolidada" que
permita consultar y administrar al conjunto de proyectos como un todo.
Por ejemplo, responder la pregunta "¿cuántos tickets tiene asignados
fulano en TODOS los proyectos en los que está?" es complicado.

Esa parte la resolvió Diego exportando cada N tiempo cada una de las
bases de datos SQLite de cada proyecto a una base de datos dentro de
SQLServer, y ahora se están desarrollando varios reportes usando las
herramientas estándares de la consultora. La desventaja es que la
información es un snapshot (i.e., no tenemos la info en tiempo real,
actualizada al instante), la enorme ventaja es que estamos pudiendo
explotar la info de Trac de una manera mucho más rica, a la vez que nos
permite una integración mucho más fuerte con nuestras otras
herramientas. En cuanto a esta parte del dilema (consolidación de la
información), la pata que está faltando es interactuar con Trac, es
decir, no solo consultar la info, sino por ejemplo hacer operaciones
masivas, del estilo seleccionar N tickets de X proyectos que cumplen tal
criteria y cerrarlos. Diego está experimentando con una especie de RPC
casero haciendo POSTs a Trac, yo tengo pendiente instalar en un entorno
de prueba el `XmlRpcPlugin`_ y ver si nos da alguna ventaja.

Otro problema que teníamos era la consistencia entre proyectos en cuanto
a "Prioridades", "Tipos de tickets", "Severidades", etc., etc., más
cuestiones como definir que componentes por defecto están activos, que
usuarios tienen que permisos, etc. Eso lo resolvimos haciendo un wrapper
alrededor de `TracAdmin`_. Pero no "trac-admin" el comando, sino
TracAdmin a nivel de componente. Este wrapper puede usarse por línea de
comandos o como un servicio web (que invocamos por ejemplo desde una
página de creación de proyectos), y "sabe" hacer un initenv usando todos
nuestros defaults: borra las cosas que no necesitamos, agrega las que
sí, setea defaults y permisos, etc. Así cualquiera puede inicializar un
nuevo proyecto en Trac con total confianza de no olvidarse ningún paso,
y de que va a cumplir con nuestro estándar interno. Y el 99% de las
cosas que hace este wrapper están definidas en un archivo externo de
configuración, con lo cual es simple modificar / extender lo que hace.

Sacando esos dos grandes temas, aún tenemos pendientes varios detalles
mas finitos, varios de los cuales son candidatos a o bien encontrar un
plug-in en `Trac Hacks`_ que nos de la funcionalidad requerida, o
implementar nuestro propio plug-in. Uno de esos temas tiene que ver con
que Trac 0.10 no maneja workflows, la versión 0.11 se sigue demorando...
y demoraaaaaaando, y estábamos necesitando empezar a validar ciertas
cosas, en particular, de consistencia de valores de algunos campos al
cerrar un ticket. Así que con un poco de expermientación del finde, más
un ratito hoy en el trabajo para afinar detalles, me largué a escribir
mi primer plugin para Trac.

Es realmente MUY fácil. La mayor parte del tiempo la invertí
investigando de cual de tooooooooodos los puntos de extensión que expone
Trac tenía que colgarme para hacer lo que yo quería. Una vez descubierto
eso, fue muy sencillo. Quería validar el ticket al grabar cambios. La
interfaz a implementar resultó ser ITicketManipulator. Macheteandome un
poco en el código `SpamFilterPlugin`_, y leyendo la MUY buena doc de
Trac, el resto fue coser y cantar.

No publico el código completo porque está muy pegado a lo que hacemos
internamente en el trabajo, pero en esencia, el core del plug-in es algo
así:

.. code:: python

   from trac.core import *
   from trac.ticket import ITicketManipulator, TicketSystem
   
   class RechazarTicket(TracError):
       """Excepcion a generar si el ticket es inválido."""
       
   class MiValidator(Component):
       implements(ITicketManipulator)
       
       # Métodos de ITicketManipulator
       
       def prepare_ticket(self, req, ticket, fields, actions):    
           pass  

       def validate_ticket(self, req, ticket):
           if 'preview' in req.args:
               # Si es un preview, y no estamos grabando, no validamos nada      
               return [] 
           if ticket['status'] != 'closed':
               if ticket['version'] in ('XXX', 'YYY'):
                   raise RechazarTicket('La versión %s solo es válida si el ticket está cerrado.' % ticket['version'])
               # El ticket aún no está cerrado: No validamos nada más
               return []
               
           # Recuperamos todos los campos que NO son de texto
           fields = [f['name'] for f in TicketSystem(self.env).get_ticket_fields() if f['type'] not in ('textarea', 'text')]
           for field in fields:
               # Acá implemento las validaciones que quiera...      
               # "field" tiene el nombre del campo (ej., "version", "status", etc.)      
               # puedo acceder al valor haciendo      
               #    ticket[field]      
               # y puedo ver el valor anterior (para ver si se está modificando) haciendo      
               #    ticket._old[field]      
               # Si alguna de mis validaciones custom no se cumple, se hace un      
               # raise de RechazarTicket... y listo.    
           return []

Como ven, muy fácil. Ahora entiendo un poco más por qué en Trac Hacks
hay TANTAS cosas... es que realmente es simple extender Trac. Ahora que
rompimos el hielo con este primer plugin... probablemente se vengan más
a futuro.

 

.. _Trac: http://trac.edgewall.org/
.. _XmlRpcPlugin: http://trac-hacks.org/wiki/XmlRpcPlugin
.. _TracAdmin: http://trac.edgewall.org/wiki/TracAdmin
.. _Trac Hacks: http://trac-hacks.org/
.. _SpamFilterPlugin: http://trac.edgewall.org/wiki/SpamFilter
