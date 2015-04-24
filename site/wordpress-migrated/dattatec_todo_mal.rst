.. title: Dattatec. TODO MAL
.. slug: dattatec_todo_mal
.. date: 2006-04-11 01:32:11 UTC-03:00
.. tags: dattatec,General,rant
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

Mi blog está andando cada vez peor. Funciona "de a ratos". Lo vengo
notando desde hace no menos de 3 semanas, y hay gente que visita este
sitio a diario y también lo ha notado. El funcionamiento es errático. Un
rato anda, un rato no. A veces es una cuestión de lentitud. La página no
carga, no carga, no carga... y finalmente el navegador se cansa y tira
un error porque el sitio no está disponible. Pero el error más
frecuente, es más raro: Uno hace click en un link, y vuelve una página
en blanco. O está viendo un artículo del blog, y cuando hace click en el
link de otro, luego de varios segundos de intentar conectarse, vuelve...
¡exactamente la misma página que uno estaba viendo!.

Ese error en particular, me afecta incluso cuando publico las noticias.
Quizás me paso 10 o 15 minutos escribiendo algo, y cuando apreto
"Enviar", no pasa nada. Reintento. Reintento. Si tengo suerte, a la 3ra
o 4ta vez engancha. Pero lo triste, es que los requests "se apilan", y
termino con el artículo duplicado, o triplicado.

El servicio (al igual que a `Facundo`_) me lo brinda `Dattatec`_. Es una
empresa con sede en Rosario. Hasta hace cosa de un año, todo andaba
relativamente bien. Nunca estuve demasiado conforme con el soporte,
porque la única forma de contactar a estos pibes es a través de un
formulario. No hay canales de chat, ni listas de correo, y mucho menos
un número de teléfono. El problema con el soporte, es que cada vez lo
cierran más. Cada vez estructuran más y más el formulario, centrándolo
en los casos típicos (estúpidos) de soporte de lo que supongo será la
mayoría de los usuarios. Y cuando uno tiene un problema EN SERIO, en
general ni siquiera tiene una categoría para describirlo. Y la calidad
de las respuestas es malísima. Siempre cerraron los tickets de soporte
con un "Hemos verificado su sitio y se encuentra perfectamente", sin
mediar ningún otro tipo de explicación. Como si uno fuera estúpido.

Más o menos uno se lo bancaba, porque dentro de todo la cosa funcionaba,
y era algo accesible. Digamos que la relación costo/beneficio terminaba
cerrando. Con algunas bronquitas, pero cerraba.

Desde hace varios meses, la cosa empezó a andar mal. Hace rato, mucho
rato que vengo monitoreando mi sitio, y las caidas son diarias, y por
lapsos de muchos minutos. Incluso horas. Generalmente es de noche, y
como mi blog no es tan popular, probablemente nadie lo note. Pero la
disponibilidad del servicio, viene en picada. Con Facundo hemos
comprobado que el sitio de él está hosteado físicamente en otra máquina.
En general, en cuanto a disponibilidad, parecería que el servidor es es
más estable (pero la realidad no me he puesto a hacer métricas al
respecto).

Sin embargo, `Facundo empezó a tener problemas también`_: Dattatec
decidió, unilaterlamente, instalar un módulo de PHP que supuestamente
incrementa la seguridad del sitio. Pero ese módulo no es del todo
compatible con `LifeType`_ (el software que usamos para generar el
blog), y le trajo varios problemas. El sitio estuvo andando mal durante
días. Nunca obtuvo una respuesta satisfactoria. Y finalmente tuvo que
recurrir a recortar funcionalidad para que más o menos, saliera andando.

Pero bueno, esa es la historia de Facu y le corresponderá a él seguir
ahondando en el tema si quiere :p Volviendo a mi blog, sumado a los
constantes cortes que vengo notando desde hace rato, hace unas semanas
se empezó a dar el problema que comentaba al principio. Al día de hoy,
no tuve una respuesta satisfactoria de soporte. Finalmente hoy me
comentaron que detectaron varios problemas y que tienen que actualizar
el sistema operativo, para que haga un mejor aprovechamiento del
hardware. Eso me sonó raro... así que me puse a ver cual es la
configuración actual. Y me llevé algunas sorpresas:

 

-  Sistema operativo: Linux
-  Version Sistema Operativo: 2.4.20-43.9.legacysmp
-  Apache: Apache/1.3.31 (Unix)
-  Perl: v5.8.0
-  PHP: 4.3.11
-  MySQL: 4.0.25

 

**La versión del kernel, es VIEJISIMA**. Acaba de cumplir 3 años y
medio. A juzgar por el patchlevel (el 43.9 del final), lo vienen
toqueteando desde hace rato. La versión de MySQL también es muy vieja.
El resto, si bien tiene una antigüedad de 6 meses a un año, digamos que
es entendible. Es un server, tampoco van a estar actualizando todo cada
vez que sale una nueva versión de algo. Lo entiendo y lo comparto. Si
critico por ejemplo la versión de Apache. **Esa versión está por cumplir
dos años**. Y Apache es un componente crítico en el stack de servicios
que le da vida a este sitio web.

¿Será ese el problema? Sinceramente, creo que no. Al menos no en un
100%. Son componentes viejos, pero estables. Versiones que en su momento
estuvieron en producción lo más bien. Obviamente podrían mejorarse las
cosas con versiones más nuevas, pero de nuevo, no creo que eso explique
mi problema. La respuesta que me dieron ("tenemos que actualizar el
sistema operativo"), parece más un intento por hacerme callar la boca
por unos cuantos días, que otra cosa (es como la 4ta vez que reabro el
ticket pidiendo explicaciones, porque lo siguen cerrando sin dar una
buena respuesta).

Yo creo que el problema de Dattatec es que tiene gente incompetente en
el área técnica, y probablmente el nivel medio/alto de la organización
ni se esté enterando de como está decayendo el servicio, porque como
tienen cortado todo mecanismo de recepción de feedback de los clientes,
y no creo que sean adivinos... ¿cómo se van a enterar?

Otra opción es que estén con problemas en su estructura de costos, y que
hayan estado desinvirtiendo (sin embargo, por algo que cuento más abajo,
esto me parece poco probable...)

Más que nada sospecho que el problema de Dattatec es que ha empezado a
apuntar a otra cosa. Está tratando de generar servicios más
"corporativos", más "enterprise" (más rentables...), y los planes
individuales pareciera que ya no le interesan tanto. Además, están
poniendo recursos en otras cosas, que nada tienen que ver con el
mantenimiento de los servicios actuales. Por ejemplo, lanzar toda una
gama de servicios sobre plataforma Windows. Bien por ellos. Pero a mi me
da bronca porque esto no hace más que demostrar que los recursos y las
ganas de hacer cosas nuevas las tienen, solo que las están invirtiendo
en targets más interesantes. Me gustaría que fueran menos caraduras y
más claros al respecto. Nada más.

En fin, no tengo con quien quejarme de estas cosas. No hay un
0-800-Dattatec para llamar y quejarse. Y no voy a volcar todo este rant
en un "ticket de soporte", porque lo más probable es que lo borren. Así
que por lo menos decidí descargar mi bronca escribiendo acá, en mi blog,
en mi página. Como cliente, siento que tengo todo el derecho de hacerlo.

Señores de Dattatec, si alguno lee esto, repito lo que vengo tratando de
decir en todos los últimos tickets de soporte (los invito a consular el
historial...): El servicio viene de mal en peor. El servicio es
inestable. La disponibilidad es cada vez más baja. La performance es
cada vez peor. Ferozo está cada vez más "eye candy" y más inútil. En
lugar de flexibilizar y ampliar los canales de comunicación, cada vez
los cierran más y los hacen más rígidos.

La relación costo/beneficio que hasta ahora me mantenía expectante, ya
no está cerrando.

 

.. _Facundo: http://www.taniquetil.com.ar/plog/
.. _Dattatec: http://www.dattatec.com/sp/inicio.php?Ps=ar
.. _Facundo empezó a tener problemas también: http://www.taniquetil.com.ar/plog/index.php?op=ViewArticle&articleId=170&blogId=1
.. _LifeType: http://www.lifetype.net/
