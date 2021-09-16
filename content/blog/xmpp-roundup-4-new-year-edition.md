---
title: "XMPP Roundup 5 'New Year edition'"
date: 2009-01-04
author: Nyco
categories: ["XMPP Roundup"]
aliases:
    - "/2009/01/xmpp-roundup-5-new-year-edition"
---

Welcome to the fifth [roundup](http://blog.xmpp.org/?cat=12) of XMPP activity worldwide. This report is authored by [Nicolas Vérité](http://nyco.wordpress.com/), [Laurent Lathieyre](http://ubikod.com/otmf/) and [Jack Moffitt](http://metajack.im/). This is a very long article since we had a lot of activity these weeks.

Your contributions are welcome for future roundups.

**Software Releases**

In this edition of the XMPP Roundup, we have a lot of software releases: clients, servers, and tools.

***Gajim 0.12***

Astérix aka Yann Leboulanger has [announced on his blog](http://blog.lagaule.org/?p=11) the release of Gajim 0.12. The full [changelog](http://trac.gajim.org/browser/trunk/ChangeLog) since 0.11.4 is loaded with new features: mood, activity, nickname and tunes, encrypted sessions, Kerberos, file transfer over multi-user chat, lots of UI improvements (chat and preference windows, drag'n drop, single window mode, etc.), LaTeX support, and many more.

***Tigase Server 4.1***

[Tigase Server version 4.1](http://www.tigase.org/en/content/tigase-xmppjabber-server-410-b1315) has been released.  New features include virtual hosting, server monitoring, and virtual components.

***BuddyMob***

[Laurent Lathieyre](http://ubikod.com/otmf/) of [Ubikod](http://ubikod.com/), pointed to [BuddyMob](http://www.buddymob.com/), an [Android](http://www.android.com/) application in private beta now, designed and developed by [Ubikod](http://ubikod.com) for [Kiboo.net](http://www.kiboo.net/), a Belgian company. BuddyMob is offering IM, social networking, feeds and geolocation... and it is all based on XMPP.

**Ya Online Mobile**

[Yandex](http://www.yandex.ru/), the giant Russian search engine and web portal, has launched the [mobile version](http://mobile.yandex.ru/online/) (Symbian S60) of its Ya Online client, based on its Jabber/XMPP service.

***Buddycloud***

[Buddycloud](http://www.buddycloud.com/) is a mobile application for Symbian S60, built on XMPP, offering status and location tracking services as well as chat.

***Lampiro***

[Lampiro](http://code.google.com/p/lampiro/), is a mobile open source (GPL licensed) XMPP client developed by [Bluendo](http://www.bluendo.com/). It is written in J2ME, and supports [compression, TLS, group chats, gateways, data forms and touch screens](http://blog.bluendo.com/ff/hooray).

***Prosody***

[Matthew Wild announced](https://mail.jabber.org/pipermail/jdev/2008-December/028640.html) on JDev mailing-list [Prosody 0.1.0](http://prosody.im/) (and [0.2.0](https://mail.jabber.org/pipermail/jdev/2008-December/028715.html) followed in less than a month), a new XMPP server, written in Lua, under the GPL license. It aims to be simple, light, and flexible.

***Sleek Migrate***

[Sleek Migrate](http://github.com/Kev/sleekmigrate/tree/master) is a server migration tool [announced](http://www.kismith.co.uk/wordpress/index.php/2008/11/30/sleek-migrate/) by [Kevin Smith](http://www.kismith.co.uk/), released under GPL license, based on the [SleekXMPP](http://code.google.com/p/sleekxmpp/) library written in Python by [Nathan Fritz](http://nathan.fritzclan.com/).

***Web-Based JavaScript XMPP Clients***

We have a bunch of Web-based JavaScript XMPP clients:

-   [Nounours](http://nounours.txzone.net/trac/) is based on [ExtJS](http://extjs.com) and [JSJaC](http://blog.jwchat.org/jsjac/) using [BOSH](https://xmpp.org/extensions/xep-0124.html), released under the GPL license
-   [iJab](http://code.google.com/p/ijab/) is using [GWT](http://code.google.com/webtoolkit/) and JSJaC, released under
    the GPL license
-   [TrophyIM](http://code.google.com/p/trophyim/) is based on the [Strophe](http://code.stanziq.com/strophe) library, released under the MIT license

***Lime Wire 5.0 alpha***

[Lime Wire](http://www.limewire.com/), the open source P2P software based on the Gnutella network, [integrates Jabber](http://blog.limewire.org/?p=309) in its [5.0 alpha version](http://www.limewire.com/download/alphaversion.php).

**Web-based Services**

***Fire Eagle***

Seth Fitzsimmons [announced](https://mail.jabber.org/pipermail/pubsub/2008-December/000067.html) an XMPP pubsub interface to [Yahoo's FireEagle](http://fireeagle.yahoo.net/).

***Remindr***

[Remindr](http://remindr.info/) sends you reminders via mail, phone or Jabber.

***Chatterous***

[Chatterous](http://www.chatterous.com/) lets you join multi user chats via your web browser, IM client, phone, or e-mail.

**Other News**

Outside of the software releases scope, we have other news:

**Tigase Server virtual hosting**

Above we mentioned the new [virtual hosting](http://www.tigase.org/en/content/virtual-hosts-tigase-server) support in [Tigase Server](http://www.tigase.org/en/project/tigase-server). Artur has also made it configurable [though the Psi XMPP client, with the help of ad-hoc commands](http://www.tigase.org/en/content/managing-virtual-domains-using-psi-client).

**Psi**

With 1,500 downloads per day and 2.4 million downloads overall, the open source Psi XMPP client has [made a long road since its beginning](http://halr9000.com/article/657).

**SAPO Codebits**

[Jack Moffitt](http://metajack.im/)'s talk (51 minutes) at SAPO Codebits is online, both [the video and the slides](http://codebits.sapo.pt/intra/s/speaker/11).

**FLOSS Weekly**

[Peter Saint-Andre](https://stpeter.im/) gave [an interview to FLOSS Weekly](http://twit.tv/floss49):, the audio is available or as an [mp3](http://www.podtrac.com/pts/redirect.mp3/twit.cachefly.net/FLOSS-049.mp3) for download (33 MB, 1h12).

**On the Specifications Front**

The Jingle XEPs for multimedia sessions like voice and video, have entered a LAST CALL:

-   [XEP-0166: Jingle](https://xmpp.org/extensions/xep-0166.html)
-   [XEP-0167: Jingle RTP Sessions](https://xmpp.org/extensions/xep-0167.html)
-   [XEP-0176: Jingle ICE-UDP Transport Method](https://xmpp.org/extensions/xep-0176.html)
-   [XEP-0177: Jingle Raw UDP Transport Method](https://xmpp.org/extensions/xep-0177.html)

As with all Last Calls, please consider the following questions and send your feedback to the [standards@xmpp.org](mailto:standards@xmpp.org) discussion list:

1.  Is this specification needed to fill gaps in the XMPP protocol stack or to clarify an existing protocol?
2.  Does the specification solve the problem stated in the introduction and requirements?
3.  Do you plan to implement this specification in your code? If not, why not?
4.  Do you have any security concerns related to this specification?
5.  Is the specification accurate and clearly written?

Your feedback is appreciated!

Some extensions aka ProtoXEPs have come in:

-   [Message Mine-ing](https://xmpp.org/extensions/inbox/mine.html): In servers that deliver messages sent to the bare JID to all resources, the resource that claims a conversation notifies all of the user's other resources of that claim.

A few XEPs have entered Final status:

-   [XEP-0174: Serverless Messaging:](https://xmpp.org/extensions/xep-0174.html) Communicate over local or wide-area networks using the principles of zero-configuration networking and without the need for servers.
-   [XEP-0085: Chat State Notifications](https://xmpp.org/extensions/xep-0085.html): Communicate the status of a user in a chat session - enaged, composing, gone, etc.
-   [XEP-0012: Last Activity](https://xmpp.org/extensions/xep-0012.html): Communicate information about the last activity of someone.

**XMPP: The Definitive Guide - Rough Cuts edition**

[Peter Saint-Andre](https://stpeter.im/?p=2378), [Remko Tronçon](http://el-tramo.be/blog/xmppbook-roughcuts) and [Kevin Smith](http://www.kismith.co.uk/wordpress/index.php/2008/12/19/xmpptdg-roughcut/) are writing a book on XMPP, for [O'Reilly](http://www.oreilly.com). [The rough cuts are available online](http://oreilly.com/catalog/9780596157197/).

**Conclusion**

The XSF and XMPP community have been quite busy during the final weeks of 2008.  We wish to thank everyone for their efforts, advice, and participation in 2008, and we wish all a happy 2009 filled with similar successes.
