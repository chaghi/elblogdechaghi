.. title: IronPython con baterías incluídas
.. slug: ironpython_con_bater_as_inclu_das
.. date: 2008-08-08 00:17:00 UTC-03:00
.. tags: ironpython,net,Python,Software
.. category: 
.. link: 
.. description: 
.. type: text
.. author: cHagHi
.. from_wp: True

¡Bien! La beta4 de IronPython 2.0 `va a incluir la librería estándar`_
de Python. En el laburo estamos usando bastante IronPython para algunas
herramientas internas. Y siempre me molestó que por un lado hacían un
laburo realmente MUY BUENO en brindar un runtime de Python perfectamente
integrado con .NET, y por el otro... le sacaban las baterías (para los
no iniciados: solemos decir que "Python viene con las baterías
incluídas", por lo amplia, útil y poderosa que es la librería estándar
que uno obtiene out-of-the-box cuando lo instala).

La realidad es que no van a incluir TODA la stdlib; hay cosas que hoy
por hoy ya se sabe que no funcionan (mayormente, módulos que en todo o
en parte están implementados en C, y para los cuales no se hizo ningún
wrapper "managed" del lado de .NET). Pero es algo.

Otro punto positivo: IronPython 2.0 va a salir con una licencia dual: La
licencia MS-PL de Microsoft, que cubre IronPython, y la Python Software
Foundation License, cubriendo la stdlib. Esto es todo un hito: MS
acepta, y reconoce, la licencia de la PSF. Según comentan en otro blog,
hasta `hubo abogados de por medio`_ para poder dar este paso. Bien por
la PSF, bien por el software libre, y bien MS.

IronPython 2.0 va a ser compatible con Python 2.5, lo cual agregará
varios chiches por sobre 1.1, y probablemente habilitará a que funcionen
algunos módulos de terceros que hoy por hoy no funcionan.

Aún tengo pendiente probar todo esto; en particular, quiero aprovechar
estas últimas betas para verificar que nuestras herramientas funcionen
correctamente con el nuevo runtime.

(gracias `Facu`_ por pasarme la data)

 

.. _va a incluir la librería estándar: http://www.codeplex.com/IronPython/Release/ProjectReleases.aspx?ReleaseId=14353
.. _hubo abogados de por medio: http://devhawk.net/2008/08/06/Including+The+Batteries+In+IronPython.aspx
.. _Facu: http://www.taniquetil.com.ar/plog/
