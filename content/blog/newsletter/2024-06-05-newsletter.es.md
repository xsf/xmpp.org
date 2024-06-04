---
title: The XMPP Newsletter May 2024
date: 2024-06-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

¡Bienvenido al XMPP Newsletter, es un placer tenerlo aquí nuevamente!
Esta edición corresponde al mes de Mayo del 2024.

### XMPP y el "Google Summer of Code 2024"

¡La XSF ha sido aceptada nuevamente como [organización anfitriona en el GSoC 2024](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024) una vez más!
Estos son los proyectos XMPP que fueron seleccionados y sobre los cuales comenzará el trabajo de codificación desde ahora:

- [Monal](https://monal-im.org/)
  - [Media Gallery (90 horas, fácil)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
- [Prav.app](https://prav.app/)
  - [Standards compliant SMS OTP based authentication (350 houras, medio)](https://wiki.xmpp.org/web/Gsoc2024/Prav.app/Standards_compliant_SMS_OTP_based_authentication)

{{< figure src="/images/logos/gsoc2024_logo.svg" caption="XSF and Google Summer of Code 2024" >}}

### Proyecto de Hosting Fiscal XSF

La XSF ofrece [hosting fiscal](https://xmpp.org/community/fiscalhost/) para proyectos XMPP. Por favor envíe su solicitud vía [Open Collective](https://opencollective.com/xmpp). Para más información [vea el post de anuncio en nuestro blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Proyectos actuales que puede apoyar:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Prav iOS](https://opencollective.com/prav-ios)

## Eventos XMPP

- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2024-07_Berlin): del Viernes 12 al Domingo 14 de Julio del 2024.
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) [IT]: XMPP web meeting mensual de la comunidad Italiana cada tercer Lunes del mes a las 7:00 PM hora local (evento online, en modo web meeting y con live streaming).

## Videos sobre XMPP

[Debian and XMPP in Wind and Solar Measurement](https://saimei.ftp.acc.umu.se/pub/debian-meetings/2024/MiniDebConf-Berlin/38-debian-and-xmpp-in-wind-and-solar-measurement.webm) charla en el MiniDebConf, Berlin 2024 (solo disponible en Inglés).

## Artículos sobre XMPP

- En el [JMP Newsletter](http://blog.jmp.chat/b/may-newsletter-2024) se expuso el tema de la censura en las rederes SMS y el trabajo (casi finalizado) que se llevó a cabo para integrar nuevas rutas que reduzcan dramáticamente los niveles de censura. También se anunción que ya se está realizando el testeo interno para adicionar soporte a RCS, y se hizo un repaso sobre las nuevas características de la última versión de [Cheogram 2.15.3-1](https://git.singpolyma.net/cheogram-android/refs/2.15.3-1) para Android.

## Noticias sobre Software XMPP

### Clientes y Aplicaciones XMPP

- [Scaling up with MongooseIM 6.2.1](https://xmpp.org/2024/05/scaling-up-with-mongooseim-6.2.1/)
- [Psi+ 1.5.1844 a 1.5 1930 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) actualización disponible.
- [Psi+ 1.5.1834 a 1.5 1937 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) actualización disponible.

### Servidores XMPP

No hubo novedades relacionadas a los servidores XMPP este mes. :-(

### Librerías y Herramientas XMPP

- QXmpp [1.6.1](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.6.1) (con corrección de errores en el soporte para grupos de chat OMEMO) y [1.7.0](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.7.0) (con [MIX](https://xmpp.org/extensions/xep-0369.html), [SASL2](https://xmpp.org/extensions/xep-0388.html) y actualización [SFS](https://xmpp.org/extensions/xep-0447.html) para compatibilidad con los protocolos implementados) disponible para su descarga.
- [go-xmpp 0.2.1](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.1).
- [go-sendxmpp 0.11.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.11.0).

## Extensiones y especificaciones

En adición a los [XMPP RFCs](https://xmpp.org/rfcs/), la "XMPP Standards Foundation" desarrolla extensiones XMPP a través de su [XEP series](https://xmpp.org/extensions/).

Desarrolladores y otros expertos en estándares de todas partes del mundo colaboran en estas extensiones, desarrollando nuevas
especificaciones para nuevas prácticas emergentes y refinan los métodos actuales que se utilizan para llevar a cabo las tareas existentes. Propuestas por quien quiera hacerlo, las XEP que resultan particularmente exitosas son categorizadas como Final ("Final") o Activa ("Active") - dependiendo de su tipo - mientras que otras son cuidadosamente archivadas como Diferida ("Deferred"). Este ciclo de vida se describe en la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), que contiene las
definiciones formales y canónicas para los tipos, estados y procesos. [Lea más acerca del proceso sobre estándares](https://xmpp.org/about/standards-process.html). Las Comunicaciones acerca de los Estándares y Extensiones ("Standars and Extensiones") tienen lugar en la [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([archivo online](https://mail.jabber.org/pipermail/standards/))

### Propuestas

El proceso de desarrollo de un XEP ("Proposal") comienza con la descripción escrita de una idea y su envío al "XMPP Editor". Dentro del plazo de dos semanas, el Consejo ("Council") decide si acepta la propuesta en carácter de XEP Experimental ("Experimental XEP").

- No hubo nuevos XEPs propuestos este mes.

### Nuevos

- No hubo nuevos XEPs este mes.

### Diferida

Si una XEP experimental ("Experimental XEP") no es actualizada por más de doce meses, perderá su carácter de "Experimental" y será clasificada como Diferida ("Deferred"). Si recibiera una nueva actualización, ésta le devolverá a la XEP carácter de "Experimental".

- No hubo XEPs diferidas ("Deferred") este mes.

### Actualizadas

- Version 2.5.0 de la XEP-0030 (Service Discovery)
  - Add note about some entities not advertising the feature. (pep)
- Version 1.34.6 de la XEP-0045 (Multi-User Chat)
  - Remove contradicting keyword on sending subject in §7.2.2. (pep)

### Últimos llamados

Los “Últimos Llamados” ("Last calls") se emiten una vez que todos parecen estar satisfechos con el estado actual del XEP. Luego de que el "Council" decide si un XEP parece estar listo, el "XMPP Editor" emite un “Último Llamado para comentarios” ("Last Call for comments"). Las devoluciones que se reciben como respuesta los “Últimos Llamados” ("Last calls") pueden ayudar a mejorar el XEP antes de devolverlo al "Council" para que este pueda ser promovido a Estable ("Stable). 


- XEP-0421: Anonymous unique occupant identifiers for MUCs
- XEP-0440: SASL Channel-Binding Type Capability

### Estable

- Version 1.0.0 de la XEP-0398 (User Avatar to vCard-Based Avatars Conversion)
  - Aceptado como "Stable" conforme la votación del Consejo ("Council Vote") del 2024-04-30. (XEP Editor (dg))

### Desechadas

- No hubo XEP's desechadas este mes.

### Rechazadas

- No hubo XEP rechazadas este mes.

## Difunda las noticias

Por favor difunda las noticias en otras redes:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Twitter](https://twitter.com/xmpp)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Recuerde revisar nuestro [Feed RSS](https://xmpp.org/feeds/all.atom.xml)!

¿Buscando ofertas de trabajo o contratar consultoría profesional para su proyecto XMPP? Visite nuestra [Pizarra de trabajo XMPP](https://xmpp.work/).

### Contribuidores y Traductores del Newsletter

Este es un esfuerzo comunitario, y nos gustaría agradecer a nuestros traductores por su contribución. ¡Todos los voluntarios y traductores a nuevos idiomas son bienvenidos! Las traducciones del "XMPP Newsletter" se pondrán a disposición aquí (con cierto retraso):

- Inglés (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Contribuidores asiduos: *Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, XSF iTeam*
- Francés: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) y [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Traductores: *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
- Italiano: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Tranductor: *nicola*
- Español Internacional:
  - *Gonzalo Raúl Nemmi*

## Colabore con la construcción del newsletter

El "XMPP Newsletter" es el resultado del esfuerzo colaborativo de la comunidad XMPP. El Newsletter de cada mes se compone en este [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Al fin de cada mes, el contenido del pad se fusiona en el [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3).

Siempre estamos felices de darle la bienvenida a nuevos contribuidores. No dude en unirse a la discusión en nuestro [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) y de esa forma, ayudarnos a sostener esta esfuerzo
comunitario.

¿Tiene un proyecto y quiere difundir la noticia?. Por favor considere compartir sus noticias o eventos aquí, con nosotros, para
alcanzar así a una mayor audiencia.

Tareas que llevamos a cabo regularmente:

- recolectar noticias acerca en el universo XMPP
- sumarios *cortos* sobre novedades y eventos
`- sumario mensual acerca de comunicaciones sobre extensiones (XEPs)
- revisión del borrador del Newsletter
- preparación de las imágenes
- traducciones
- comunicación a través de cuentas en medios

## Licencia

El presente newsletter se publica bajo los términos de la [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
