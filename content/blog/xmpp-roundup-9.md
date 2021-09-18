---
title: XMPP Roundup 9
date: 2009-05-11
author: Nyco
categories: ["XMPP Roundup"]
---

[Reporters: Nicolas Vérité and Peter Saint-Andre]

Welcome to the 9th edition of the XMPP Roundup, the periodic stream of news and events in the XMPP universe.

**New and updated software**

*Wokkel 0.6.0*

Ralph Meijer has announced [Wokkel 0.6.0](http://wokkel.ik.nu/), a set of XMPP tools on top of the Python Twisted framework.

*PySoy game engine*

[PySoy](http://www.pysoy.org/ "http://www.pysoy.org") is a 3d game engine including networking support being based around XMPP for player chat and server discovering, Jingle ICE-UDP for network games. It is released under the AGPLv3 license.

*XMPPLogger*

[XMPPLogger](http://www.ahzf.de/itstuff/XMPPLogger/) is a small Perl utility written under the BSD license that listens on a FIFO and sends every line to the given XMPP/Jabber account(s).

*Mojo Messaging Service: PubSub by Palm*

[In a article titled "Palm to Introduce Push Services](http://www.precentral.net/palm-introduce-push-services)", [pre central](http://www.precentral.net/) notes:

> When the Mojo SDK is broadly released later this year, it will 
> include a developer-facing offering called the Mojo Messaging Service, 
> an XMPP publish/subscribe service. The Mojo Messaging Service is an
> elegant, standards-based way to exchange information over the 
> Internet. When new information is available, it is “published” to the 
> cloud and all interested parties who are subscribers are notified that 
> new information is available. This will allow developers to push live 
> content to their applications or services. The Mojo Messaging Service 
> initially will have a limited feature set and service level that will 
> evolve over time.

*xBookmarks addon for Firefox*

[xBookmarks](https://addons.mozilla.org/en-US/firefox/addon/9970) stands for "XMPP bookmarks", it is a Firefox extension that implements [XEP-0048](https://xmpp.org/extensions/xep-0048.html) so that a user having an XMPP account can store all of his bookmarks in one place and can retrieve them from anywhere. xBookmarks needs [xmpp4moz](https://addons.mozilla.org/en-US/firefox/addon/3632).

*Babylon*

[Babylon](http://babylon.rubyforge.org/README_rdoc.html) is a Ruby framework for XMPP applications, written under the MIT license and currently available in a "pre-0.1" version.

**Services**

*WordPress.com's firehose*

[WordPress.com](http://wordpress.com/), a hosting service for [WordPress](http://wordpress.org) blogs (this blog is using WordPress), has launched [Firehose](http://en.wordpress.com/firehose/), a private, commercial stream service for blog posts and comments:

> The WordPress.com firehose is designed for partners like search 
> engines and market intelligence providers who would like to ingest a 
> real-time stream of new WordPress.com posts and comments the second 
> they get published. The firehose is XMPP based and can be accessed s2s 
> (server-to-server) or c2s (client-to-server).

*File transfer proxy at jabber.org*

The jabber.org XMPP service has [gained a SOCKS5 file transfer proxy](http://www.jabber.org/index.php/2009/05/new-file-transfer-proxy/), it is located at [proxy.eu.jabber.org](xmpp:proxy.eu.jabber.org).

*WeFeelFine*

[wefeelfine@jabber.spektral.at](xmpp:wefeelfine@jabber.spektral.at) is a Jabber bot that seeks the feeling expressed in blogs worldwide. More information [on the blog post](http://blog.disktree.net/?p=84).

**Articles**

*What Can You Do with XMPP?*

Kathryn Barrett from O'Reilly, [has written a lengthy article](http://fyi.oreilly.com/2009/05/what-can-you-do-with-xmpp.html) on the book XTDG, aka [XMPP: The Definitive Guide](http://oreilly.com/catalog/9780596521264/) by Peter Saint-Andre, Kevin Smith, and Remko Tronçon, detailing a large range of the features and possible applications of XMPP.

**Specifications**

Since the last XMPP Roundup, several specifications published by the XMPP Standards Foundation have evolved:

-   [XEP-0256: Last Activity in Presence](https://xmpp.org/extensions/xep-0256.html) has advanced from Experimental to Draft
-   [XEP-0237: Roster Versioning](https://xmpp.org/extensions/xep-0237.html) has been updated to reflect feedback receiving during Last Call, and a second Last Call has been issued before advancing it from Experimental to
    Draft
-   [XEP-0124: Bidirectional-streams Over Synchronous HTTP](https://xmpp.org/extensions/xep-0124.html) (BOSH) was updated to correct the XML schema and incorporate technical discussions held at [XMPP Summit 6](/2010/08/xmpp-summit-6) in February
-   [XEP-0267: Server Rosters](https://xmpp.org/extensions/xep-0267.html) and [XEP-0268: Incident Reporting](https://xmpp.org/extensions/xep-0268.html) were published, also as a result of discussions held at [XMPP Summit 6](/2010/08/xmpp-summit-6) in February
-   [XEP-0266: Codecs for Jingle RTP Sessions](https://xmpp.org/extensions/xep-0266.html) was updated with information about the [Dirac codec](http://diracvideo.org/) for video
-   [XEP-0238: XMPP Protocol Flows for Inter-Domain Federation](https://xmpp.org/extensions/xep-0238.html) and [XEP-0154: User Profile](https://xmpp.org/extensions/xep-0154.html) have been deferred because of inactivity

**A final word**

XMPP's ubiquity shows even more after months pass.
