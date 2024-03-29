---
title: The XMPP Newsletter February 2022
author: emus
date: 2022-03-05
categories: ['Newsletter']
---

_¡Este articulo fue traducido por daimonduff, marevalo, patasca y TheCoffeMaker, de la comunidad XMPP!_

Bienvenidos al boletín de noticias de XMPP, ¡es un placer tenerlos aquí de nuevo! Este número cubre el mes de febrero de 2022.

Al igual que este boletín, muchos proyectos y sus esfuerzos en la comunidad XMPP son el resultado del trabajo voluntario de la gente. Si estás contento con los servicios y el software que utilizas, especialmente en la situación actual, ¡considera dar las gracias o ayudar a estos proyectos! ¿Interesado en apoyar al equipo del Boletín? Lee más al respecto al final del boletín de noticias.

### Traducciones del Boletín de Noticias

Este es un esfuerzo comunitario, y nos gustaría agradecer a los traductores sus contribuciones. ¡Los voluntarios son bienvenidos! Las traducciones del boletín XMPP se publicarán aquí (con cierto retraso):

- Francés: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) y [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- Alemán: [xmpp.org/de/blog](https://xmpp.org/de/blog/) y [anoxinon.de](https://anoxinon.de/blog/)
- Italiano: [nicfab.it](https://www.nicfab.it/)
- Español: [xmpp.org/es/blog](https://xmpp.org/es/blog/)

## Anuncios de la XSF

![XSF y Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF y Google Summer of Code 2022")

- La XSF tiene previsto participar en el [Google Summer of Code 2022 (GSoC)](https://xmpp.org/community/gsoc-2022/). Si estás interesado en participar como estudiante, mentor o como proyecto en general, por favor [agrega tus ideas y contactanos](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022).
- Todos los miembros de la XSF son llamados a votar las [solicitudes de membresía](https://wiki.xmpp.org/web/Membership_Applications_Q1_2022) actualmente en curso.

## XSF patrocinando proyectos

La XSF ofrece [patrocinamiento fiscal](https://xmpp.org/community/fiscalhost/) para proyectos de XMPP. Por favor postula a través de [Open Collective](https://opencollective.com/xmpp). Para más información puedes consultar el [anuncio en el blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Proyectos actuales: 

- [Bifrost bridge: Transferencia de mensajes sin conexión entre Matrix y XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Eventos

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): disponible en nuestro [canal de Youtube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remoto)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): encuentro mensual de entusiastas de XMPP en Berlín, todos los segundos miércoles de cada mes.

## Artículos

- JMP.chat [explica en su blog](http://blog.jmp.chat/b/2022-bidirectional-gateways) por qué los gateways, y especialmente los gateways bidireccionales, entre XMPP y otros protocolos son tan útiles. [En su boletín](http://blog.jmp.chat/b/february-newsletter-2022) también anuncia el lanzamiento de llamadas internacionales y la culminación de su renovación de imagen.

![JMP.chat gateways bidireccionales](/images/newsletter/2022-02-05/JMP_bidirectional.png "JMP.chat gateways bidireccionales")

- Erik Bärwaldt, de la alemana "Linux Magazin" [evaluó distintos clientes de mensajería instantánea, entre ellos Conversations para XMPP](https://www.linux-magazin.de/ausgaben/2022/02/bitparade/) [DE]

- [Mellium Dev Communiqué](https://opencollective.com/mellium/updates/dev-communique-for-february-2022): Este mes vio el lanzamiento de diversos nuevos paquetes, incluyendo pruebas de integración para Slixmpp, soporte para PEP Native Bookmarks, mejor soporte para varios hashes de criptografía y soporte para entity capabilites.

## Noticias sobre software 
 
### Clientes y aplicaciones 
 
[Se ha publicado Dino `0.3`](https://dino.im/blog/2022/02/dino-0.3-release/): videollamadas y conferencias, con encriptación y peer-to-peer. ¡Dino ahora soporta llamadas entre dos o más personas! 
 
![Llamadas en Dino](/images/newsletter/2022-02-05/dino_conference_call.png "Llamadas en Dino") 
 
[Noticias sobre el desarrollo de Gajim](https://gajim.org/post/2022-02-24-development-news-february/): Febrero trajo una ventana integrada de detalles de charlas grupales, que ofrece todas las opciones de configuración que necesites. Este mes también: menos fugas de memoria y códigos QR para OMEMO mejorados. 
 
Monal tuvo una [exitosa campaña de recaudación de fondos](https://monal.im/blog/funding-campaign-mac-mini-for-faster-monal-development/) para un servidor de construcción, que reducirá significativamente los tiempos de compilación. [Más información sobre el desarrollo de Monal](https://monal.im/blog/insights-into-monal-development/): Monal dejará de soportar iOS 12 y 13, y macOS Catalina. El equipo de Monal está buscando un desarrollador de SwiftUI, y necesitan ayuda para crear una nueva web más sencilla. 
 
Grandes noticias de Movim: se ha publicado [Movim `0.20` "Skiff"](https://mov.im/?node/pubsub.movim.eu/Movim/dd90cd1c-4bcd-45a5-88a3-220fd4280b21), que incluye  compatibilidad con OMEMO, mejoras en la interfaz gráfica y mejor gestión de salas de charla grupales. 
 
![Mejoras en la interfaz de Movim](/images/newsletter/2022-02-05/movim_publish.png "Mejoras en la interfaz de Movim") 
 
Se ha publicado [Psi+ `1.5.1605`](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) con correcciones para OMEMO. 
 
[Se ha publicado Poezio `0.13.2`](https://github.com/poezio/poezio/releases/tag/v0.13.2). Esta versión solo corrige la compatibilidad con la versión `1.8.0` de slixmpp publicada recientemente, pero una versión mucho más interesante será lanzada pronto. 
 
Los desarrolladores de Profanity escribieron una [entrada en su blog](https://profanity-im.github.io/blog/post/profanity-on-pinephone/) sobre cómo usar su cliente en teléfonos Pinephone. 
 
Tigase publicó [BeagleIM `5.1`](https://github.com/tigase/beagle-im/releases/tag/5.1) y [SiskinIM `7.1`](https://github.com/tigase/siskin-im/releases/tag/7.1) incluyendo mejoras en el soporte de OMEMO. 
 
## Servidores 
 
Se ha lanzado [Jackal `0.57.0`](https://github.com/ortuman/jackal/releases/tag/v0.57.0), servidor XMPP escrito en Go.
 
Openfire anunció el lanzamiento de [Openfire `4.7.1`](https://discourse.igniterealtime.org/t/openfire-4-7-1-released/91365): Correcciones importantes que incluyen actualizaciones de seguridad para los controladores de bases de datos, correcciones de configuración de logging y una corrección importante para usuarios que están experimentando problemas con usuarios que son expulsados de charlas grupales. Además, se han lanzado [Openfire Pàdé `1.6.1`](https://discourse.igniterealtime.org/t/openfire-pade-1-6-1-released/91366) y [REST API Openfire plugin `1.7.1`](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-7-1-released/91358).
 
Snikket publicó una actualización importante para los usuarios de su [servidor para dispositivos ARM, incluyendo las placas Raspberry Pi](https://snikket.org/blog/server-updates-for-arm/). 
 
Se ha publicado [Tigase XMPP Server `8.2.0`](https://github.com/tigase/tigase-server/releases/tag/tigase-server-8.2.0).
 
## Bibliotecas 
 
¡Mellium Co-op ha publicado las versiones [`v0.21.0`](https://pkg.go.dev/mellium.im/xmpp@v0.21.0) y [`v0.21.1`](https://pkg.go.dev/mellium.im/xmpp@v0.21.1) de la biblioteca [melium.im/xmpp](https://mellium.im/xmpp/) para Go! Cabe destacar para esta versión el soporte básico de PubSub y PEP además de flujo binarios dentro de banda (In-Band Bytestreams). Se puede encontrar más información en las [notas de publicación](https://opencollective.com/mellium/updates/new-release-mellium-im-xmpp-v0-21-0). La versión 0.21.1 corrige un problema de seguridad que fue descubierto en el paquete de websockets y es la versión a la que se debería actualizar. Para más información consultar la [CVE-2022-24968](https://mellium.im/cve/cve-2022-24968/). 
 
Se ha lanzado [Slixmpp `1.8.0`](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.8.0), añadiendo compatibilidad con Python 3.10, además de una gran cantidad de mejoras internas relacionadas con el sistema de tipos y async. 
 
Tigase ha hecho varias publicaciones de sus productos: [Halcyon `0.0.17`](https://github.com/tigase/halcyon/releases/tag/v0.0.17), [JaXMPP `3.5.0`](https://github.com/tigase/jaxmpp/releases/tag/3.5.0), [Tigase Swift `3.1.0`](https://github.com/tigase/tigase-swift/releases/tag/3.1.0), y [Tigase Swift-OMEMO `2.1.0`](https://github.com/tigase/tigase-swift-omemo/releases/tag/2.1.0).

## Extensiones y Especificaciones

Desarrolladores y otros expertos en estándares de todo el mundo colaboran en estas extensiones, desarrollando nuevas especificaciones para las prácticas emergentes y perfeccionando las formas existentes de hacer las cosas. Propuestas por cualquiera, las que tienen más éxito acaban siendo definitivas o activas -según su tipo-, mientras que otras se archivan cuidadosamente como diferidas. Este ciclo de vida se describe en [XEP-0001](https://xmpp.org/extensions/xep-0001.html), que contiene las definiciones formales y canónicas de los tipos, estados y procesos. [Más información sobre el proceso de normalización](https://xmpp.org/about/standards-process.html). La comunicación en torno a los estándares y las extensiones tiene lugar en la [Lista de correo de estándares](https://mail.jabber.org/mailman/listinfo/standards) ([archivo en línea](https://mail.jabber.org/pipermail/standards/)).

### Proposed (Propuestas)

El proceso de desarrollo de XEP inicia escribiendo una idea y presentándola en el XMPP Editor. Dentro de las dos semanas, el Consejo decidirá si acepta la propuesta como una XEP Experimental.

-   [PubSub Type Filtering](https://xmpp.org/extensions/inbox/pubsub-filter.html)
    -   Esta especificación proporciona una forma de filtrar los nodos PubSub en una consulta disco.

-   [MUC Affiliations Versioning](https://xmpp.org/extensions/inbox/muc-affiliations)
    -   Esta especificación proporciona una forma de reducir la cantidad de consultas necesarias para estar al día con las afiliaciones en una sala MUC.

### New (Nuevas)

- No hay nuevas XEPs este mes.

### Deferred (Diferidas)

Si una XEP experimental no es actualizada por más de 12 meses, será movida de Experimental a Deferred (Diferida). Si hay alguna actualización, la XEP será puesta nuevamente en Experimental.

- No hay XEPs pospuestas este mes.

### Updated (Actualizadas)

-   Version `2.13.0` de [XEP-0004](https://xmpp.org/extensions/xep-0004.html) (Data Forms)
    -   Añade la gestión de formularios de presentación incompletos (melvo)

-   Version `1.24.1` de [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Añade sugerencias para procesar formularios de presentación incompletos (melvo)

-   Version `1.24.0` de [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Anunciar soporte para publicación de items
    -   Remplaza 'allow' por 'allows' (melvo)

-   Version `1.23.0` de [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Clarifica (redefine) el campo pubsub#type. (edhelas, pep)

### Last Call (Últimos Llamados)

Los Last Call (Últimos Llamados) se emiten una vez que todos parecen estar satisfechos con el estado actual de la XEP. Después de que el Consejo decida si la XEP parece estar lista, el XMPP Editor emite una Última Llamada para recibir comentarios. Los comentarios recogidos durante el Last Call ayudan a mejorar el XEP antes de devolverlo al Consejo para que lo pase a Stable (Estable).

- No hay Last Call este mes.

### Stable (Estable, anteriormente conocido como Draft/Borrador)

Info: La XSF ha decidido cambiar el nombre de "Borrador" a "Estable". [Lee más sobre esto aquí.](https://github.com/xsf/xeps/pull/1100)

- Ningún XEP avanzó a Estable este mes.

### Deprecated

-   No hay XEPs en este estado este mes.

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

Encuentra y publica ofertas de empleo y asesores profesionales en el [XMPP job board](https://xmpp.work/).

{{< newsletter-subscribe >}}

También mira nuestro [feed RSS](https://xmpp.org/feeds/all.atom.xml)!

## Ayúdanos a construir el boletín de noticias

Este boletín XMPP se produce con colaboración de la comunidad XMPP. Por ello, nos gustaría dar las gracias a **Adrien Bourmault (neox), alkino, anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, marevalo, mathieui, MattJ, nicfab, patasca, seveso, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat,xdelatour, Ysabeau** por su apoyo y ayuda en la creación, revisión y traducción. ¡Muchas gracias a todos los colaboradores y a su continuo apoyo!

El número del Boletín de Noticias de cada mes se redacta en este [simple anotador](https://yopad.eu/p/xmpp-newsletter-365days). Al final de cada mes, el contenido del anotador se incorpora al [repositorio Github de XSF](https://github.com/xsf/xmpp.org/milestone/3). Siempre estamos encantados de recibir colaboradores. No dudes en unirte a la discusión en nuestro [chat del grupo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) y así ayudarnos a mantener esto como un esfuerzo comunitario. ¿Tienes un proyecto y escribes sobre él? Considera la posibilidad de compartir tus noticias o eventos aquí, y promuévelos ante una gran audiencia.

Las tareas que realizamos regularmente son, por ejemplo:

- Agregación de noticias en el universo XMPP
- Formulación *breve* de noticias y eventos
- Resumen de la comunicación mensual sobre extensiones (XEP)
- Revisión del borrador del boletín informativo
- Preparación de imágenes para los medios de comunicación
- Traducciones: especialmente al alemán, francés, italiano y español

## Licencia

Este boletín de noticias está publicado bajo [licencia CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
