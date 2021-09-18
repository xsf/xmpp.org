---
title: "Last Call: Link-Local Messaging"
date: 2007-03-01
author: stpeter
categories: ["Miscellaneous"]
---

At the XMPP Summit on Monday we held a rare in-person meeting of the [XMPP Council](https://xmpp.org/council/), since we had four of the five Council members in attendance. Among other things the Council issued a [Last Call](https://mail.jabber.org/pipermail/standards/2007-February/014012.html) for comments on [XEP-0174: Link-Local Messaging](https://xmpp.org/extensions/xep-0174.html).

This technology, which enables real-time messaging in the absence of a server, was pioneered by Apple in an early version of their [iChat](http://www.apple.com/ichat/) client. It has since been adopted in several open-source instant messaging clients and is now also widely used in the [One Laptop Per Child](http://www.laptop.org/) project.

Although this serverless mode is not precisely an XMPP extension since XMPP as defined in [RFC 3920](https://datatracker.ietf.org/doc/html/rfc3929) requires a server for authentication and network access, it does re-use XMPP's XML streams for peer-to-peer communication in a local mesh, so it seemed appropriate to standardize its usage through the XMPP Standards Foundation. The spec has been stable for some time and now appears mature enough to advance to Draft within our standards process. 

The Last Call ends on 2007-03-13, so if you have comments send them as always to our open [standards discussion list](https://mail.jabber.org/mailman/listinfo/standards).
