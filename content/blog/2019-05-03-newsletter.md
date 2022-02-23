---
title: The XMPP Newsletter, 3 May 2019
date: 2019-05-03
author: jcbrand
categories: ["Newsletter"]
aliases:
    - "/2019/05/newsletter-3-may/"
---

Welcome to the XMPP newsletter.

If you have an article, tutorial or blog post you'd like us to include in the
newsletter, please [submit it on the XMPP wiki](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## News

Rafał Leśniak published an interesting write-up about the challenges faced by a
Forward Health, a UK based messaging platform for healthcare, which [migrated from
a third party chat solution to a custom XMPP-based one](https://medium.com/miquido/successful-migration-to-a-custom-xmpp-solution-76fcdecb0928).
It's an interesting read with insights into how XMPP is perceived by newcomers to the protocol.

An academic paper (in PDF format) appeared about
[using XMPP to control robotic telescopes](http://www.astroscu.unam.mx/rmaa/RMxAC..51/PDF/RMxAC..51_articulo06.pdf).

Jérôme Poisson is writing regular [progress notes](https://www.goffi.org/b/EMqk8vCvdPMMjXQzZWbSc3/progress-note)
about his work on various parts of the Salut à Toi project, which includes frontends for the desktop, Android
and the web. He's been working on the XMPP-based [file sharing service](https://www.goffi.org/b/LdJWYpoF2gznf3NWgCWKba/progress-note).
Starting with the incoming version 0.7 [SàT can be used as a component, and file sharing is the first one](https://www.goffi.org/b/dbK4eHGoCeWDz2NWTjSjR2/progress-note)
although he's still making further [fixes to file sharing in the context of photo albums](https://www.goffi.org/b/iEh8ZAoD3yu4fCgxxecoME/progress-note).

{{< newsletter-subscribe >}}

Paul Schaub has been writing a series of blogs posts about the cryptographic
building blocks of OMEMO, an end-to-end encryption protocol for XMPP based on
the Signal Protocol. In the first one he explains how with the Signal Protocol you can
[start an encrypted chat with another user even if they are offline](https://blog.jabberhead.tk/2019/04/04/shaking-hands-with-omemo-x3dh).
In his second post, he takes a [closer look at the double ratchet](https://blog.jabberhead.tk/2019/04/15/closer-look-at-the-double-ratchet)
which protects the secrecy of past and future chat sessions if a
particular session was compromised.

Isode has published a [whitepaper on interoperability between IRC and XMPP](https://isode.com/whitepapers/interconnecting-xmpp-and-irc.html).
One key takeaway is that with their approach, when all users have migrated to XMPP
the IRC channel is no longer needed and can be removed, which is not the case with
other gateway approaches.

In the beginning of April an XMPP sprint was held in Berlin, sponsored by
the German Federal Youth Council (_Deutsche Bundesjugendring_). On their website is a
[retrospective on the sprint](https://tooldoku.dbjr.de/2019/04/rueckblick-auf-den-xmpp-sprint/) in German.
Here's the [Google translated version](https://translate.google.com/translate?sl=de&tl=en&u=https%3A%2F%2Ftooldoku.dbjr.de%2F2019%2F04%2Frueckblick-auf-den-xmpp-sprint%2F).
They've now also [announced their own public XMPP server at yochat.eu](https://tooldoku.dbjr.de/2019/04/yochat-eu-willkommen-beim-offenen-chatserver-fuer-die-jugendarbeit/).
Here again the [Google translated version](https://translate.google.com/translate?sl=de&tl=en&u=https%3A%2F%2Ftooldoku.dbjr.de%2F2019%2F04%2Fyochat-eu-willkommen-beim-offenen-chatserver-fuer-die-jugendarbeit%2F).

The 2019 [XMPP Compliance Suites](https://xmpp.org/extensions/xep-0412.html) XEP has been advanced to Draft status and Jonas Schäfer
has updated the CSS stylesheets of the XEPs so that they now have a handy fixed table of contents.


## Software releases

The upcoming release of Monal will support [AESGCM:// links](https://monal.im/blog/aesgcm-links/), 
include an [unread message indicator](https://monal.im/blog/unread-message-indicator) and
[include some OMEMO fixes](https://monal.im/blog/ios-updates/).

### Clients

- Converse.js [4.2.0](https://github.com/conversejs/converse.js/releases/tag/v4.2.0)
- Gajim [1.1.3](https://dev.gajim.org/gajim/gajim/blob/gajim-1.1.3/ChangeLog)

### Plugins

- Hazelcast for Openfire [2.4.2](https://discourse.igniterealtime.org/t/hazelcast-openfire-plugin-2-4-2-released/84966)
- Search for Openfire [1.7.2](https://discourse.igniterealtime.org/t/search-openfire-plugin-1-7-2-released/84819)
- Bookmarks for Openfire [1.0.3](https://discourse.igniterealtime.org/t/bookmarks-openfire-plugin-1-0-3-released/84760)
