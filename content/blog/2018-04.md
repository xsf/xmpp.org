---
title: The XMPP Newsletter, 3 May 2018
date: 2018-05-03
author: jcbrand
categories: ["Newsletter"]
aliases:
  - "/2018/05/the-xmpp-newsletter-3-may-2018/"
---

Welcome to the 3rd edition of the XMPP newsletter.

Jeff Becker has written a howto called
[New life for XMPP. Build your own decentralized messenger!](https://i2p.rocks/blog/new-life-for-xmpp-build-your-own-decentralized-messenger.html)
which focuses on using the [I2P](https://geti2p.net/en/) anonymous network layer instead of using a registered domain name.

Peter Waher has published his book _"Mastering Internet of Things"_, available from [Packt](https://www.packtpub.com/networking-and-servers/mastering-internet-things)
and [Amazon](https://www.packtpub.com/networking-and-servers/mastering-internet-things).

Georg Lukas has written a post [Freedom and Anonymity on XMPP](https://github.com/ge0rg/jabber-spam-fighting-manifesto/blob/master/Freedom-and-Anonymity.md)
in which he addresses concerns around his [Jabber Spam Fighting Manifesto](https://github.com/ge0rg/jabber-spam-fighting-manifesto)
and its possible effects on issues of privacy and free speech.

The USA's National Institute of Standards and Technology (NIST) released a [draft report on cybersecurity or the Internet of Things (IoT)](https://csrc.nist.gov/CSRC/media/Publications/nistir/8200/draft/documents/nistir8200-draft.pdf). Daniel Wisnewski from Tigase has written an [analysis with focus on using XMPP for IoT](https://tigase.net/article/nist-releases-iot-draft-standards).

Tigase recently moved their `xmpp.cloud` service to Amazon Web Services and Daniel wrote an article on
[how using AWS helped them optimize memory usage in the Tigase HTTP API](https://tigase.net/blog-entry/how-aws-helped-us-optimize-memory-usage-tigase-http-api).

## Software releases

### Servers

* [Ejabberd 18.04](https://blog.process-one.net/ejabberd-18-04/) has been released, it includes bugfixes and a few improvements.

* Less than a month after MetronomeIM 3.8, [versions 3.8.1, 3.8.2, and 3.8.3 have followed](https://metronome.im/Tags/releases),
  bringing improvements such as MAM, SIFT, avatars and GDPR.

* Erlang Solutions made a new [2.2 release of MongooseIM](https://www.erlang-solutions.com/blog/mongooseim-2-2-the-global-server.html),
  subtitled _The Global Server_, as it supports certificate based authentication ([XEP-0178](https://xmpp.org/extensions/xep-0178.html)),
  stable _Global Distribution_ that connects multiple servers/clusters worldwide under the same domain name,
  a Jingle/SIP proxy, an important security fix, hidden components and more.

### Clients

* Less than a month after the symbolic version 1.0.0, [Gajim 1.0.1 and Gajim 1.0.2](https://gajim.org/) have been released.
  Version 1.0.1 improves MAM support, adds image previews in the file chooser dialog and includes many smaller fixes and improvements.
  Version 1.0.2 correctly reloads plugins, saves history export with utf8 encoding, doesnt allow plain BOSH by default, and fixes many bugs.

* ChatSecure releases [version 4.3.0](https://chatsecure.org/blog/chatsecure-v43-omemo-group-chat-preview/),
  which is able to catch up on discussions that happened while it was offline and supports #OMEMO encryption.

* In its on-going series of concise blog posts, [Monal IM](https://monal.im/) developer follows up on MAM development,
  as well as announces a future implementation of XEP-0184: Message Delivery Receipts.

### Libraries

* [Smack 4.2.4](https://discourse.igniterealtime.org/t/smack-4-2-4-released/81404) has been released,
   adding support for XEP-0394: Message Markup, XEP-0382: Spoiler messages, XEP-0372: References, XEP-0392: Consistent Color Generation, and bringing even more fixes and improvements. 

* [MatriX vNext version 2.0](https://www.ag-software.net/2018/04/30/matrix-vnext-2-0-released/) has been released.
  It is a cross platform XMPP SDK for the full .NET Framework, .NET Core and Mono.

##  XMPP videos:

Daniel Gakwaya has been making various XMPP-related videos the last while, some of them we've linked to in previous newsletters.

* [XMPP Core Explained: Introduction](https://www.youtube.com/watch?v=O0gZSd_oW1g)
* [XMPP Core Explained : XMPP Architecture](https://www.youtube.com/watch?v=gbeS8BwwM-M&t=1s)
* [XMPP Tutorial: The Friendly Introduction](https://www.youtube.com/watch?v=6YhMOFS04kA)
* [XMPP Android Chat App Tutorial Step by step](https://www.youtube.com/watch?v=BheBPoBR_5s)
* [XMPP WhatsApp like Android Chat App With Smack](https://www.youtube.com/watch?v=97-XjxcBXOk)

