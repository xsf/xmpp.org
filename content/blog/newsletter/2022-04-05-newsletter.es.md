---
title: The XMPP Newsletter March 2022
author: XMPP Communication Team and Contributors
date: 2022-04-05
categories: ['Newsletter']
---

_¡Este articulo fue traducido por daimonduff y TheCoffeMaker, de la comunidad XMPP!_

Bienvenidos al boletín de Noticias de XMPP, ¡es un placer tenerles aquí de nuevo! Este número cubre el mes de marzo de 2022.

Al igual que este boletín, muchos proyectos y sus esfuerzos en la comunidad XMPP son el resultado del trabajo voluntario de la gente. Si estás contento con los servicios y el software que utilizas, especialmente en la situación actual, ¡considera dar las gracias o ayudar a estos proyectos! ¿Interesado en apoyar al equipo del Boletín? Lee más en la parte inferior.

### Traducciones del Boletín de Noticias

Este es un esfuerzo comunitario, y nos gustaría agradecer a los traductores sus contribuciones. ¡Los voluntarios son bienvenidos! Las traducciones del boletín XMPP se publicarán aquí (con cierto retraso):

- Francés: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) y [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- Alemán: [xmpp.org](https://xmpp.org/categories/newsletter/) y [anoxinon.de](https://anoxinon.de/blog/)
- Italiano: [nicfab.it](https://www.nicfab.it/)
- Español: [xmpp.org](https://xmpp.org/categories/newsletter/)

## Anuncios de la XSF

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

- La XSF ha sido aceptada como organización anfitriona en el [Google Summer of Code 2022 (GSoC)](https://xmpp.org/community/gsoc-2022/). Si estás interesado en participar como estudiante, mentor o como proyecto en general, por favor [añade tus ideas y ponte en contacto con nosotros](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022). El periodo de solicitud de colaboradores ya ha comenzado, ¡así que date prisa!
- Boletín XMPP por correo: Hemos migrado a nuestro [propio servidor de listas de correo](https://mail.jabber.org/mailman/listinfo/newsletter) y hemos dejado de usar Tinyletter. Es de sólo lectura y recibirás el Boletín XMPP mensualmente. También elimina las preocupaciones de privacidad con Tinyletter.

## XSF patrocinando proyectos

La XSF ofrece [patrocinamiento fiscal](https://xmpp.org/community/fiscalhost/) para proyectos de XMPP. Por favor postula a través de [Open Collective](https://opencollective.com/xmpp). Para más información puedes consultar el [anuncio en el blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Proyectos actuales: 

- [Bifrost bridge: Transferencia de mensajes sin conexión entre Matrix y XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Eventos

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): disponible en nuestro [canal de Youtube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remoto)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): encuentro mensual de entusiastas de XMPP en Berlín, todos los segundos miércoles de cada mes.

## Artículos

Los desarrolladores de Profanity publicaron una guía rápida sobre cómo utilizar [OpenPGP para XMPP (OX)](https://profanity-im.github.io/blog/post/openpgp-for-xmpp-ox/).

[JMP's Newsletter](https://blog.jmp.chat/b/march-newsletter-2022) anuncia un nuevo cliente para Android (basado en Conversations) que se centra en la mejora de la experiencia de usuario de los gateways que cumplen con los estándares.

![JMP Cheogram](/images/newsletter/2022-03/cheogram-screenshot.png "JMP Cheogram")

Se ha publicado el [Mellium Dev Communiqué de marzo de 2022](https://opencollective.com/mellium/updates/dev-communique-for-march-20222). Esta versión incluye cambios en la barra lateral del cliente Communiqué TUI y mejoras en varios paquetes del módulo principal mellium.im/xmpp.

## Noticias sobre software 
 
### Clientes y aplicaciones 

[Noticias de desarrollo de Gajim](https://gajim.org/post/2022-03-24-development-news-march/): Marzo trae un nuevo sistema de reporte de problemas y muchas mejoras de rendimiento tanto para Gajim como para python-nbxmpp. El plugin OMEMO de Gajim también viene con algunas mejoras. Por último, pero no menos importante, ha habido un problema de seguridad en python-nbxmpp, que ha sido corregido en la versión `2.0.6`.

Se han publicado [Openfire Pàdé `1.5.7` y `1.6.3`](https://discourse.igniterealtime.org/t/openfire-pade-1-6-3-released/91536) y [Openfire Pàdé 1.6.2](https://discourse.igniterealtime.org/t/openfire-pade-1-6-2-released/91424).

Se ha publicado [Profanity `0.12.0`](https://github.com/profanity-im/profanity/releases), con soporte para el registro de cuentas in-band y estados de ánimo del usuario, nuevo tema, experiencia de usuario OX mejorada (como muestra el artículo anterior) y un montón de correcciones y características pulidas.

Se han publicado [Psi+ `1.5.1615` y Psi+ `1.5.1618`](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/).

[Conversaciones `2.10.5`](https://github.com/iNPUTmice/Conversations/blob/master/CHANGELOG.md) ha salido, trayendo mejores reconexiones de llamadas después de los cambios de red, mostrando el JID de la persona que llama y el JID de la cuenta en la pantalla de llamadas entrantes, adaptando las ubicaciones de almacenamiento de archivos según los nuevos requisitos de Android 11 y una corrección de seguridad que afecta a las descargas de archivos. Hay que tener en cuenta que la versión para F-Droid va con retraso, debido a problemas no relacionados, pero la versión `2.10.2.1` ya está disponible e incluye sólo la corrección de seguridad. También se ha anunciado que las cuentas en conversations.im son gratuitas a partir de ahora.

## Servidores
Se ha publicado [Jackal `0.58.0`](https://github.com/ortuman/jackal/releases/tag/v0.58.0) y se ha añadido el tipo de repositorio BoltDB.

Después de tres años de desarrollo, se ha publicado [Prosody `0.12.0`](https://blog.prosody.im/prosody-0.12.0-released/). La actualización cubre el cumplimiento de XMPP, optimizaciones para móviles y conectividad, intercambio de archivos HTTP actualizado, soporte mejorado para llamadas de audio/vídeo, Direct TLS y mucho más - ¡felicidades! 

![Prosody](/images/newsletter/2022-03/grafana-screenshot.png "Prosody")

¡ [Tigase XMPP Server `8.2.0`](https://github.com/tigase/tigase-server/releases/tag/tigase-server-8.2.0) ha sido lanzado! La característica más importante es el soporte para el protocolo MIX, que ofrece una mejor experiencia de chat de grupo, especialmente en dispositivos móviles. El chat de grupo (MUC) no se ha dejado de lado y también ha recibido muchas correcciones. Además, hemos mejorado la conectividad de servidor a servidor, hemos añadido la opción de almacenar certificados en el repositorio (muy útil en los despliegues de clústeres) y mucho más.

La comunidad Ignite Realtime se complace en anunciar la disponibilidad inmediata de la versión de mantenimiento `2.2.3` del [plugin GoJara para Openfire](https://discourse.igniterealtime.org/t/gojara-plugin-for-openfire-version-2-2-3-release/91505). GoJara proporciona una implementación de [XEP-0321 "Remote Roster Management"](https://xmpp.org/extensions/xep-0321.html) y ayuda a la monitorización de [Spectrum 2](https://spectrum.im/).

## Bibliotecas

Se ha publicado la versión de slixmpp [`1.8.1`](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.8.1), que corrige un problema de compatibilidad con la biblioteca estándar de python debido a la introducción de defusedxml en la versión `1.8.0`.

Se han publicado las versiones de python-nbxmpp [`2.0.5` y `2.0.6``](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/nbxmpp_2.0/ChangeLog), que corrigen un problema de seguridad en la resolución de URIs de websocket.

Se han publicado las versiones [Smack `4.4.5` y `4.5.0-alpha1`](https://discourse.igniterealtime.org/t/smack-4-4-5-and-4-5-0-alpha1-released/91437).

## Extensiones y Especificaciones

Desarrolladores y otros expertos en estándares de todo el mundo colaboran en estas extensiones, desarrollando nuevas especificaciones para las prácticas emergentes y perfeccionando las formas existentes de hacer las cosas. Propuestas por cualquiera, las que tienen más éxito acaban siendo definitivas o activas -según su tipo-, mientras que otras se archivan cuidadosamente como diferidas. Este ciclo de vida se describe en [XEP-0001](https://xmpp.org/extensions/xep-0001.html), que contiene las definiciones formales y canónicas de los tipos, estados y procesos. [Más información sobre el proceso de normalización](https://xmpp.org/about/standards-process.html). La comunicación en torno a los estándares y las extensiones tiene lugar en la [Lista de correo de estándares](https://mail.jabber.org/mailman/listinfo/standards) ([archivo en línea](https://mail.jabber.org/pipermail/standards/)).


### Proposed (Propuestas)

El proceso de desarrollo de XEP inicia escribiendo una idea y presentándola en el XMPP Editor. Dentro de las dos semanas, el Consejo decidirá si acepta la propuesta como una XEP Experimental.

- No hay XEPs propuestas este mes.

### New (Nuevas)

-   Versión 0.1.0 de [XEP-0462](https://xmpp.org/extensions/xep-0462.html) (PubSub Type Filtering)
    -   Aceptado por votación del Consejo el 2022-02-09.

-   Versión 0.1.0 de [XEP-0463](https://xmpp.org/extensions/xep-0463.html) (MUC Affiliations Versioning)
    -   Aceptado por votación del Consejo el 2022-02-16.

### Deferred (Diferidas)

Si una XEP experimental no es actualizada por más de 12 meses, será movida de Experimental a Deferred (Diferida). Si hay alguna actualización, la XEP será puesta nuevamente en Experimental.

- No hay XEPs diferidas este mes.

### Updated (Actualizadas)

-   Versión 1.6.0 de [XEP-0115](https://xmpp.org/extensions/xep-0115.html) (Entity Capabilities)
    -   Menciona explícitamente los ataques de preimagen (ssw)

-   Versión 1.4.0 de [XEP-0156](https://xmpp.org/extensions/xep-0156.html) (Discovering Alternative XMPP Connection Methods)
    -   Elimina el método DNS `_xmppconnect` debido a una vulnerabilidad de seguridad. (tjb)

### Last Call (Últimos Llamados)

Los Last Call (Últimos Llamados) se emiten una vez que todos parecen estar satisfechos con el estado actual de la XEP. Después de que el Consejo decida si la XEP parece estar lista, el XMPP Editor emite una Última Llamada para recibir comentarios. Los comentarios recogidos durante el Last Call ayudan a mejorar el XEP antes de devolverlo al Consejo para que lo pase a Stable (Estable).

- No hay Last Call este mes.

### Stable (Estable, anteriormente conocido como Draft/Borrador)

Info: La XSF ha decidido cambiar el nombre de "Borrador" a "Estable". [Lee más sobre esto aquí.](https://github.com/xsf/xeps/pull/1100)

- Ningún XEP avanzó a Estable este mes.

### Deprecated

-   No hay XEPs en este estado este mes.

### Obsoleted (Obsoletas)

-   [XEP-0008](https://xmpp.org/extensions/xep-0008.html) (IQ-Based Avatars)
    -   Obsoleta debido a dos especificaciones que la sustituyen (egp)

-   [XEP-0038](https://xmpp.org/extensions/xep-0038.html) (Icon Styles)
    -   Obsoleta debido a la omnipresencia de los emoji Unicode, así como de los Bits of Binary stickers. (egp)

-   [XEP-0051](https://xmpp.org/extensions/xep-0051.html) (Connection Transfer)
    -   Obsoleta porque esta característica ha sido fusionada en el núcleo de XMPP, ver RFC6120 sección 4.9.3.19, que describe el error de flujo `<see-other-host/>`. (egp)

-   [XEP-0138](https://xmpp.org/extensions/xep-0138.html) (Stream Compression)
    -   Obsoleta debido a una vulnerabilidad de seguridad. (tjb)

-   [XEP-0229](https://xmpp.org/extensions/xep-0229.html) (Stream Compression with LZW)
    -   Obsoleto debido a una vulnerabilidad de seguridad. (tjb)

### Call for Experience (Llamado a Experiencia)

Un Call for Experience (Llamado a Experiencia), al igual que los “Last Call”, es un llamamiento explícito a comentarios, pero en este caso se dirige principalmente a las personas que han implementado, e idealmente desplegado, la especificación. A continuación, el Consejo vota para pasarla a definitiva.

-   No hubo Call for Experience este mes.

## ¡Difunde la noticia!

Por favor, comparte la noticia a través de otras redes:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

Aquí puede [suscribirse por correo electrónico](https://mail.jabber.org/mailman/listinfo/newsletter). Es de sólo lectura y sólo se le enviará el Boletín Mensual.

¡También puedes consultar nuestro [Feed RSS](https://xmpp.org/feeds/all.atom.xml)!

¿Buscas ofertas de trabajo o quieres contratar a un consultor profesional para tu proyecto XMPP? Visite nuestra [bolsa de trabajo XMPP](https://xmpp.work/).

## Ayúdanos a construir el boletín de noticias

Este boletín XMPP se produce con colaboración de la comunidad XMPP. Por ello, nos gustaría dar las gracias a **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, MattJ, nicfab, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat, Ysabeau, Zash** por su apoyo y ayuda en la creación, revisión y traducción. ¡Muchas gracias a todos los colaboradores y a su continuo apoyo!

EEl número del Boletín de Noticias de cada mes se redacta en este [simple anotador](https://yopad.eu/p/xmpp-newsletter-365days). Al final de cada mes, el contenido del anotador se incorpora al [repositorio Github de XSF](https://github.com/xsf/xmpp.org/milestone/3). Siempre estamos encantados de recibir colaboradores. No dudes en unirte a la discusión en nuestro [chat del grupo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) y así ayudarnos a mantener esto como un esfuerzo comunitario. ¿Tienes un proyecto y escribes sobre él? Considera la posibilidad de compartir tus noticias o eventos aquí, y promuévelos ante una gran audiencia.

Las tareas que realizamos regularmente son, por ejemplo:

- Agregación de noticias en el universo XMPP
- Formulación *breve* de noticias y eventos
- Resumen de la comunicación mensual sobre extensiones (XEP)
- Revisión del borrador del boletín informativo
- Preparación de imágenes para los medios de comunicación
- Traducciones: especialmente al alemán, francés, italiano y español

## Licencia

Este boletín de noticias está publicado bajo [licencia CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).