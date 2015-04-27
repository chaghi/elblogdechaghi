.. title: Y seguimos con Dattatec...
.. slug: y_seguimos_con_dattatec
.. date: 2006-04-18 22:56:21 UTC-03:00
.. tags: dattatec,General,rant
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Lamento que mi blog se haya transformado en el lugar para ventilar mi
indignación con esta empresa. Probablemente a la gente que lee el blog
regularmente no le importe. Esté aburrida de este tema. Pero, ¿saben
cuál es el objetivo? Básicamente que esto no se pierda. Que los spiders
de Google y Yahoo! lo indexen. Y que alguna vez, alguien que se pregunte
"¿cómo será el servicio y el soporte de Dattatec?", pueda caer en este
artículo, leerlo, y sacar su propia conclusión.

La "interacción" con Dattatec del fin de semana acaba de convertirse
para mí en la PEOR experiencia de atención al cliente. La PEOR. Y miren
que estamos en Argentina, así que cuando hablamos de un mal servicio al
cliente, sabemos de que hablamos, ¿no?

Voy a describir el problema que se presentó, y luego voy a reproducir
el texto de los diferentes reclamos que nos cruzamos con soporte técnico
a causa de este problema, en orden cronológico. Faltan mis primeras
respuestas, porque hoy, armando esto, me dí cuenta (para aumentar más mi
indignación) que Dattatec se dedicó a BORRAR del sistema de reclamos las
primeras consultas. Cuando lean como se fue dando todo... saquen Uds.
las conclusiones de por qué lo habrán hecho.

Bueno, el asunto es que las respuestas de Dattatec las tengo todas,
porque me llegan por e-mail. Pero mis primeras consultas (a excepción de
la inicial que "abre" el reclamo, que también llega por e-mail) fueron
borradas. Así que en lugar de poner el texto de la consulta (que no
tengo...), trataré de resumir que fué lo que dije. Me hubiera gustado
tener el 100% de la info textual, para que esto sea más transparente...
pero bueno, Dattatec ni siquiera me dejó esa alternativa.

Por último, al final de todo, algunas conclusiones sobre como termina
esto.

El Problema
===========

El sábado a la mañana, me dí cuenta que mi sitio estaba andando mal.
Ok, venía andando mal desde hacía varias semanas (vean los posts
anteriores...), pero en particular el sábado directamente se había
"roto" completamente algo: Los links no funcionaban. Al hacer click en
los títulos de los artículos, o en las categorías, o en el historial,
obtenía un mensaje de error de que la página no existía.

Resulta que yo estaba absolutamente seguro de que hasta el viernes a
la noche todo andaba Ok. Y como Dattatec supuestamente estaba tratando
de arreglar mis otros problemas, y esto que me pasó, `ya le había pasado
a Facundo`_, obviamente estaba claro que Dattatec se había mandado una
de las suyas.

Y así empezó esta conversación con soporte técnico, vía el sistema de
"tickets"

Parte I: Diálogo de sordos
==========================

yo, el sábado 15/04 a las 09:21
-------------------------------

Mi sitio dejó de andar correctamente. Las páginas de mi blog dan error
"404".

Por favor, noten que NO son páginas estáticas, con lo cual el problema
NO es que la página no exista, sino alguna configuración que supongo
habrá cambiado en el servidor a nivel de PHP.

Me pregunto si Uds. habrán decidido cambiar algo, como siempre, sin
avisar, y sin cuidar la compatibilidad de los cambios con las
aplicaciones existentes de sus clientes :(

Por otro lado, esto teniendo un problema de permisos en el directorio::

    /home/gechaghi/public_html/blog/tmp/1

Yo NO modifiqué permisos ni configuraciones de mi sitio en el día de
ayer u hoy, y hasta ayer funcionaba, así que insisto en que esto se debe
a algún cambio en el servidor.

Les pido por favor lo verifiquen y me informen que es lo que está
pasando.

Estos son ejemplos de links que no están andando (devuelven error 404)
y eran funcionales hasta el día de ayer:::

    http://chaghi.com.ar/blog/post/2006/03/25/windows_vista_innovacion
    http://chaghi.com.ar/blog/category/software

Soporte técnico, el 15/04 a las 10:11
-------------------------------------

Sr Mariano,

El error que nos detalla en su ticket fué causado al utilizar Front
Page para publicar y/o actualizar su sitio, debido a la gran cantidad de
inconvenientes que posee este software, el cual cambia los permisos y
propietarios de sus archivos y carpetas sin consultar (por ej
``/home/gechaghi/public_html/blog/tmp/1``); le sugerimos utilizar un
cliente ftp para subir sus archivos. (Cute o Nicoftp, por ejemplo).

Por otra parte le comunicamos que el error que visualizó en su panel
de control (dpanel) fué debido a que los permisos , propietarios y
grupos de los archivos de configuración de dpanel que se encuentran en
su carpeta etc, fueron dañados por el mismo FP; hemos corregido esos
archivos.

yo, el 15/04, algunos minutos después
-------------------------------------

El texto original fue borrado por Dattatec. Mi respuesta fue que yo
jamás había usado Front Page, que manejaba los archivos de mi sitio
desde Linux, con un cliente de FTP estándar de dicho sistema operativo.
Que hasta el viernes todo había funcionado bien, y que yo no había
tocado NADA desde entonces, y que los permisos no podían cambiarse
"solos". Y que mi sitio seguía andando mal.

Soporte técnico, el 15/04 a las 14:15
-------------------------------------

Estimado usuario: Le informamos que el inconveniente respecto al blog
ha sido generado al eliminar archivos de su sitio mediante FTP,
adjuntamos log FTP:::

    Mon Mar 6 20:07:58 2006 0 200.69.49.135 1508 /home/gechaghi/public_html/blog/templates/chaghi/commentform.template b _ o r gechaghi ftp 0 * c
    Mon Mar 6 20:10:26 2006 0 200.69.49.135 1547 /home/gechaghi/public_html/blog/templates/chaghi/commentform.template b _ i r gechaghi ftp 0 * c
    Tue Mar 7 15:23:52 2006 0 200.68.82.145 3437 /home/gechaghi/public_html/blog/templates/chaghi/footer.template a _ o r gechaghi ftp 0 * c
    Tue Mar 7 15:26:10 2006 0 200.68.82.145 3712 /home/gechaghi/public_html/blog/templates/chaghi/footer.template a _ i r gechaghi ftp 0 * c
    Sat Mar 11 17:56:36 2006 0 200.69.49.116 4091 /home/gechaghi/public_html/blog/.htaccess b _ o r gechaghi ftp 0 * c
    Tue Apr 11 22:25:38 2006 0 200.69.49.49 18230 /home/gechaghi/public_html/blog/class/net/customrequestgenerator.class.php b _ o r gechaghi ftp 0 * c
    Tue Apr 11 22:36:23 2006 0 200.69.49.49 1859 /home/gechaghi/public_html/blog/templates/chaghi/postandcomments.template b _ o r gechaghi ftp 0 * c
    Sat Apr 15 16:09:17 2006 0 201.250.96.4 4091 /home/gechaghi/public_html/blog/.htaccess a _ o r gechaghi ftp 0 * c

Saludos cordiales.

yo, el 15/04, algunos minutos después
-------------------------------------

El texto original fue borrado por Dattatec. Respondí MUCHO más
indignado, y quizás en un tono no del todo apropiado, porque sentí que
me estaban tomando de idiota.

El log de FTP que adjuntan como prueba, habla de ACCESOS a los
archivos, no eliminaciones. Además, todas las entradas (menos la última)
son de varios días (¡y hasta semanas!) antes de que se produjera el
problema, con lo cual, es absolutamente irrelevante.

Respondí muy enojado, porque realmente no entendía la insistencia de
Dattatec en tratar de "forzar" la realidad, y buscar la manera de
culparme por algo que yo no había hecho.

Soporte técnico, el 15/04 a las 16:10
-------------------------------------

Estimado usuario: El archivo que ha eliminado y no deberia haberlo
hecho es ``/home/gechaghi/public_html/blog/class/net/customrequestgenerator.class.php`` ,
dirijase por favor con respeto a nuestro soporte o no atenderemos su consulta.

Saludos cordiales.

yo, el 15/04, algunos minutos después
-------------------------------------

El texto original fue borrado por Dattatec. Esta respuesta terminó de
indignarme, porque el archivo mencionado NO estaba borrado. Y es más, no
se modificaba desde el 31 de marzo del 2005, ¡hace más de un año!

Como no quería darles la excusa fácil de ignorarme por no ser
"educado", conté hasta 10.000 antes de responder, y muy a mi pesar,
cambié el tono.

Como supuse que evidentemente no estaban dispuestos a salir de su
política de acusarme, en lugar de investigar realmente el problema, les
comenté en mi respuesta que yo sabía de al menos dos clientes de ellos
que semanas atrás habían experimentado problemas similares cuando
Dattatec decidió instalar suPHP. Y que por favor, les rogaba que dejaran
de acusarme y de responder con información abosultamente irrelevante y
falsa, y se dedicaran a buscar el problema (y la solución).

Soporte técnico, el 15/04 a las 17:59
-------------------------------------

Estimado usuario:

Le informamos que en la busqueda de las causas que pudieron haber
producido este inconveniente hemos verificado ya que no sea a causa de
permisos en los archivos y carpetas, los archivos PHP deben tener 644
mientras las carpetas 755, sin excepción para funcionar.

En cuanto a la suposicion de front page esto fue debido a que a
sucedido muchas veces y a que en su hosting existen carpetas como
``_private`` provias de estas extensiones.

En el caso de los logs, le pedimos disculpas ya que este si fue error
nuestro por una mala interpretacion de los mismos.

En todo caso, nosotros hemos realizado una actualizacion de suPHP en
el servidor en las ultimas 48 horas y es por ello que los permisos no
deben ser mas de los señalados en primera instancia.

Saludos cordiales

yo, el 15/04, algunos minutos después
-------------------------------------

El texto original fue borrado por Dattatec. La cosa parecía que
(tibiamente) comenzaba a encaminarse: Reconocían que habían estado
hablando estupideces, y reconocían que tal vez el problema se debiera
efectivamente a lo que YO les había sugerido. Sin embargo, mi sitio
seguía sin andar.

Ingresé al "DattaControl" para verificar los permisos, y me encontré
con el mismo error de licencia vencida o inválida de hacía un par de
días atrás.

Así que les respondí que todo seguía igual, y que encima, otra vez no
me funcionaba DattaControl. Y que si ellos habían actualizado suPHP,
necesitaba que encontraran el problema, y me dieran una solución.

Soporte técnico, el 15/04 a las 19:28
-------------------------------------

Estimado Mariano

Le informamos que en estos momentos se esta llevando a cabo la
migracion de su cuenta a otro servidor para solucionar estos problemas,
en unas horas mas cuando culmine este proceso todo quedara solucionado,
cualquier inconveniente seguiremos trabajando para que su sitio funcione
de manera correcta. Saluda a Usted Cordialmente.

**- - - - -**

Y ahí terminó el diálogo de sordos. Esperé algunas horas, y volví a
probar. El problema de acceso a DattaControl estaba resuelto, pero mi
sitio, seguía andando mal. Para esto, ya era domingo de Pascuas a la
madrugada. El domingo a mediodía volví a conectarme para ver el estado
del ticket, y avisarles que todo seguía andando mal. Durante todo el
domingo, sin embargo, no tuve respuesta. A última hora recibí la
confirmación de que el tema estaba en "espera", y lo estaban evaluando.

Y así pasamos a la parte II, que abre con una respuesta de Dattatec,
incidentalmente, la primera que figura en el sistema de tickets si
entramos hoy y lo consultamos, ya que todas las anteriores, como ya
dije, fueron sospechosamente eliminadas.

A partir de acá, entonces, leerán las respuestas de Dattatec
intercaladas con las respuestas mías, tal cual como fueron redactadas.

Parte II: Estimado cliente, nosotros lo rompemos. Ud. arréglelo
===============================================================

Soporte técnico, el 17/04 a las 08:22
-------------------------------------

Sr,

el inconveniente en su sitio se debe a directivas de apache alojadas
en su archivo .htaccess, como RewriteEngine on, la cual se encuentra
activada a nivel servidor y por ello deberá quitarla.

De todas maneras le sugerimos replantear la programación e su blog

yo, el 17/04 a las 08:39
------------------------

Las directivas de Apache que mencionan están funcionando desde hace
meses. No entiendo por que ahora, sin previo aviso, dejaron de hacerlo.

Por otro lado, todas las directivas del .htaccess en este momento
están comentadas (supongo las habrán comentado Uds. para probar), y sin
embargo, mi sitio SIGUE SIN FUNCIONAR CORRECTAMENTE.

Yo NO programé mi blog; es un producto estándar, LifeType (antes
"pLog") que incluso Uds. ofrecián con el pack "Amigo".

Mi blog funcionaba perfectamente hasta el día viernes por la noche.
Por favor, no pueden obligarme a "replantear la programación de mi
blog", de un día para otro, sin aviso, y sin ninguna explicación técnica
coherente de que es exactamente lo que no está andando, y por qué.

La regla de RewriteEngine que ahora Uds. comentaron, no tiene nada que
ver con mi problema. *esa* parte, hasta ayer, estaba funcionando de
manera correcta.

Por favor, sean un poco más específicos respecto a que es lo que está
causando conflictos. Entiendan que esto estuvo funcionando durante más
de un año, hasta el día viernes.

Soporte Técnico, el 17/04 a las 20:04
-------------------------------------

Estimado Mariano:

Le informo que deberá desactivar los permalinks de su weblog, ya que
son incompatibles con nuestra configuración actual de PHP.

yo, el 17/04 a las 20:21
------------------------

Quiero manifestar que estoy en absoluto desacuerdo a que Dattatec
cambie arbitrariamente de un día para otro, sin avisar, la configuración
de PHP, provoque el mal funcionamiento de algo que estuvo andando
perfectamente bien durante más de un año de la forma que está, y que
luego de casi 48hs de tratar constantemente a través de este medio de
"echarme la culpa" imputándome modificaciones que yo nunca hice, ahora
me digan que tengo que deshabilitar y/o limitar la funcionalidad de mi
sitio, tan solo poroque a Uds. se les ocurre que a si sea.

Me parece una total falta de respeto hacia mi persona, una total falta
de consideración hacia el cliente.

La respuesta es ABSOLUTAMENTE arbitraria. No entiendo por qué
decidieron deshabilitar el uso de ForceType (o cualquier otra directiva
de Apache en la que se estaba basando el software que tenía corriendo),
cuando en nada afecta la seguridad.

Están recortando funciones. Y encima, haciéndolo sin previo aviso, sin
asesorar antes a los clientes, y sin brindarme ninguna solución
altenativa.

Soporte Técnico, el 17/04 a las 21:16
-------------------------------------

Estimado Mariano:

Le comunico que ForceType obviamente no representa ningun peligro de
seguridad, lo que nosortros hemos implementado es una restriccion de
seguridad al server web que afecta el funcionamiento de algunas de estas
directivas, no por capricho nuestro sino porque asi funciona, por otra
parte cada ves que aplicamos restricciones de seguridad no podemos
informar a cada uno de nuestros clientes, debe comprender que estamos
hablando de seguridad, no de actitudes caprichosas por parte de
dattatec.com, si usted posee una queja o sugerencia debe completar el
formulario de testimonios en nuestro sitio o en el buzon de sugerencias
que se encuentra en su acceso a soporte.

Conclusiones
============

Me aburrí de discutir. Realmente siento que no vale la pena, porque la
impresión que me dejaron es que no tienen la más puta idea de que es lo
que está mal, y lo que es más grave, no les importa.

Estuve intercambiando algunas opiniones con la gente que desarrolla
LifeType, y uno de los core developers me dijo que esto debe estarles
causando problemas no solo con LifeType, sino con múltiples clientes,
así que debería estar en su mayor interés arreglarlo, ya que además
seguramente se trataba de algo trivial.

Bueno, no es el caso de Dattatec. A ellos, aparentemente, no les
importa. Y decidieron que si cambian la configuración, y se vuelve
incompatible con mis aplicaciones, pues nada. No importa que es lo que
no anda, ni por qué, ni si tiene arreglo, ni si antes andaba. La
solución es que yo me arregle a partir de ahora prescindiendo de lo que
no anda.

Al carajo. Está decidido que en cuanto pueda, mudo mi sitio a un
proveedor que me respete.

Mientras tanto, investigando un poco en internet, encontré una manera
transitoria de hacer andar los links. La solución no es prolija, e
invalida muchas estadísticas de acceso a mi sitio (porque la solución
genera datos incorrectos), pero funciona.

Así que ahí tienen. Si alguna vez deciden ser clientes de Dattatec,
estén preparados para vivir experiencias emocionantes como las que acabo
de contarles.

.. _ya le había pasado a Facundo: http://www.taniquetil.com.ar/plog/index.php?op=ViewArticle&articleId=170&blogId=1
