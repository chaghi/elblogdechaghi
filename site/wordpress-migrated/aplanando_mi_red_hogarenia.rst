.. title: "Aplanando" mi red hogareña
.. slug: aplanando_mi_red_hogarenia
.. date: 2007-06-24 19:05:50 UTC-03:00
.. tags: General
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

La Navidad pasada, unos días antes incluso de recibir mi laptop,
mihermano me regaló un router inalámbrico, para que instalara en
eldepto. El router ese no es modem, así que no podía
reemplazardirectamente mi modem/router ADSL, ya que seguía necesitando
la funciónde modem.

Un poco por miedo a no tocar la configuración de mimodem (ya que tuve
bastantes malas experiencias tocando algo, yquedándome sin internet...),
terminé armando una configuración bastantefea, en la cual AMBOS
dispositivos estaban "stackeados" actuando comorouter:

-  El modem establecía el enlace y resolvía el encapsulamiento PPPoE(y
   la autenticación en mi ISP), ruteaba, se ocupaba de la
   actualizaciónde mi IP dinámica en DynDNS.org, y definía algunas
   reglas deNAT/port-forwarding hacia una IP interna...

-  ... que era la IP del router wireless. El router wireless veía aesa
   IP como una IP fija, privada e interna como si fuera la asignadapor
   el proveedor de ISP, definía las reglas de NAT/port-forwardinghacia
   el resto de la red, tenía activo un servidor DHCP (básicamentepor la
   laptop, ya que para el desktop uso una IP interna fija), ygestionaba
   la parte wireless, con su seguridad.

Esto anda. Pero es feo. Es complejo al pedo. Dos routers en cascadapara
una red hogareña con dos equipos siempre me pareció como matar
unmosquito con una bomba atómica. Y además, tenía el problema de que
elmodem/router quedaba "oculto" hacia la red interna, con lo cual
cuandoquería tocar algo de su configuración, tenía que desconectar
elrouter/wireless, conectar la PC directamente al modem, cambiar
laconfiguración de red para poder verlo, configurarlo, y luego,
volvertodo otra vez a su lugar. Quizás, si supiera algo más de redes,
podríahaber configurado alguna regla de ruteo o alguna cosa que me
permitiera"ver" (y administrar) el modem... pero no sé, nunca busqué
demasiado alrespecto, e igualmente, me seguía resultando una
configuración muycompleja.

El otro día, de casualidad, encontré que mi routerwireless puede
funcionar solo como "punto de acceso". El truco es, enlugar de conectar
la salida del modem al puerto WAN del wireless, hayque conectarlo a uno
de los 4 ports ethernet internos. De esa forma,toda la configuración de
WAN, NAT, ruteo y demás queda sin efecto(porque no se usa), y el
router/wireless deja de actuar como router...para ser solo una especie
de hub wireless, o más precisamente, un"access point". Y lo bueno es que
podía acceder y administrar a los dosequipos, al modem y al wireless,
via sus interfaces web.

Probéesa configuración, y anduvo. Pero empecé a notar lentitud en la
red,más que nada en la resolución de DNS. Tardaba a veces varios
segundos.No tengo ninguna medición precisa, pero era apreciable. Muy.
Hicealgunas pruebas, pero no llegué a encontrar el problema. No se dónde
nipor qué los paquetes se quedaban "rebotando" y haciendo
carambolasdentro de la LAN antes de salir... pero lo hacían. Y además,
empezarona pasar cosas raras. Por ejemplo, el "bridge" entre mi placa
wireless yla placa "virtual" que uso cuando booteo Windows en una
virtual machinedejó de andar. Y peor: Cuando levantaba ese bridge, me
quedaba sinconectividad en la laptop, mal, al punto que (gracias a mi
ignoranciapara revertirlo), tenía que reiniciar la laptop para que se
arregle elmoco que se armaba. Feo. Horrible.

Investigando un poco más, encontré que:

-  El modem/router podía configurarse como "bridge", con lo cual
   establece el enlace con el ISP, pero NADA más;

-  El router/wireless podía configurarse para hacer el encapsulamiento
   PPPoE... bien!

Así que probé esa alternativa: Pasé toda la configuración de PPPoEal
wireless, ajusté las reglas de NAT, le pasé la configuración deDynDNS
también a este equipo, y configuré al modem/router para que hagasolo de
bridge y deje de ser router, actuando solo como modem.

Perfecto.Ahora el modem es solamente un modem. También queda oculto como
alprincipio para la LAN (con lo cual no puedo administrarlo), pero
ahorano importa, porque básicamente no hay nada para configurar... o
sea, siel enlace se cae al punto que el modem no anda, es que se rompió
algoen Telefónica, o en mi ISP.

Y el router/wireless hace todo elresto: Encapsula PPPoE, rutea, hace NAT
y port-forwarding, define lasreglas del firewall, DHCP, seguridad, y
demás. Con lo cual, tengo unsolo equipo para administrar o para mirar
los logs cuando algo nofunciona. La red volvió a la normalidad (no tengo
"lags" extraños), yel bridge cuando configuro una red virtual sigue
andando.

Así queahora tengo una configuración más simple, más normal (parecida a
la deun usuario de cablemodem, digamos, pero con ADSL).

Y todo elexperimento me demostró que realmente se MUY POCO de ruteo,
briding,masquerading y encapsulamiento. Porque realmente me gustaría
saber cualera el problema con la configuración intermedia (la que usaba
elwireless solo como Access Point).
