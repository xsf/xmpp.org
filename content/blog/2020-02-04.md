---
title: Full speed XMPP universe! 04 Feb 2020
date: 2020-02-04
author: nyco
categories: ["Newsletter"]
aliases:
    - "/2020/02/newsletter-04-february/"
---

## Intro

Welcome to the XMPP newsletter covering the month of January 2020, which has seen a lot of activity!

Please help us on this community effort, which [process is fully transparent and adaptable](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## Articles 

Ingo Jürgensmann has written two interesting articles:

* [XMPP - Prosody & Ejabberd](https://blog.windfluechter.net/content/blog/2020/01/07/1754-xmpp-prosody-ejabberd)
* [XMPP - Fun with Clients](https://blog.windfluechter.net/content/blog/2020/01/18/1755-xmpp-fun-clients)

David Wong wrote an insightful point by point piece: [A history of end-to-end encryption and the death of PGP](https://www.cryptologie.net/article/487/a-history-of-end-to-end-encryption-and-the-death-of-pgp/)

This Twitter thread started by Thierry Stoehr shows [various use cases of XMPP in Instant Messaging](https://twitter.com/ThierryStoehr/status/1202978443048235009): healthcare, miltary, police and law enforcement, municipal services, intelligence agencies, in-games chat... Please "Like" and "Share", and even add the use cases you have seen in action.

Mike Kuketz started of a series about different messengers including XMPP: [Die verrückte Welt der Messenger – Messenger Teil1](https://www.kuketz-blog.de/die-verrueckte-welt-der-messenger-messenger-teil1/) (German).

![Federation](https://media.kuketz.de/blog/artikel/2020/welt-der-messenger/federation.png)

### XMPP Newsletter translations

This month, the [French version is available](https://linuxfr.org/news/bonne-annee-xmpp-14-janvier-2020) on LinuxFr.org.

## Events

As usual in this period of the year, the community of protocol makers united in the XMPP Summit. Two days of sharing and building the future of XMPP. This year has been productive, we covered various subjects such as:

* XMPP Shortage Audit
* Easy Passwordless Onboarding and Account Management
* Account Rich Presence in PEP
* MLS
* End-to-End Encryption Key Management
* Palaver IM Client
* Why Push Notifications are not good enough?
* MIX when?
* IM-NG
* commTeam ("Lightning talk")
* Inbox / Unread / Bind2
* XMPP as mandatory standard? (Lightning talk)
* Stickers
* XHTML-IM2 / Rich markup

vanitasvitae has written a huge live thread on Mastodon:

* [Day 1](https://fosstodon.org/@vanitasvitae/103571845414141817)
* [Day 2](https://fosstodon.org/@vanitasvitae/103577121536634734)

We will probably cover all these in more depth next month.

## Software releases 
          
### Servers 

The Ignite Realtime community has announced a series of updates:

* [Hazelcast Openfire plugin 2.5.0](https://discourse.igniterealtime.org/t/hazelcast-openfire-plugin-2-5-0-released/86961)
* [Openfire 4.5.0](https://discourse.igniterealtime.org/t/openfire-4-5-0-is-released/87004)
* [XML Debugger Openfire plugin 1.7.3](https://discourse.igniterealtime.org/t/xml-debugger-openfire-plugin-1-7-3-released/87006)
* [Monitoring Openfire plugin 2.0.0](https://discourse.igniterealtime.org/t/monitoring-openfire-plugin-2-0-0-released/87153)

[Prosody 0.11.4](https://blog.prosody.im/prosody-0.11.4-released/) has been released.

Erlang Solutions has released [MongooseIM 3.6.0](https://github.com/esl/MongooseIM/releases/tag/3.6.0) and [MongoosePush 2.0.0](https://github.com/esl/MongoosePush/releases/tag/2.0.0).

Process One has published [ejabberd 20.01](https://blog.process-one.net/ejabberd-20-01/).

### Clients and applications 

The Dino team has announced [version 0.1](https://dino.im/blog/2020/01/dino-0.1-release/), with a "development process that started three years ago and already combined work of 30 contributors, including 4 summer of code students and multiple development sprints". The news has even been covered by [Hacker News](https://news.ycombinator.com/item?id=22185693) and [LinuxFr.org](https://linuxfr.org/news/sortie-de-dino-0-1)

![Dino](https://dino.im/blog/2020/01/dino-0.1-release/main_window.png)

Tigase has released [BeagleIM 3.5 and SiskinIM 5.5](https://tigase.net/beagleim-3.5-and-siskin-5.5-released/), respectively for macOS and iOS.

![Beagle IM](https://tigase.net/static/28fe03d4f74066874cfcf0ca8f5b7732/fcda8/beagle-chat.png)

JC Brand has announced the release of [Converse.js 6.0.0](https://github.com/conversejs/converse.js/releases/tag/v6.0.0).

Georg Lukas has released  [yaxim 0.9.9 - FOSDEM Edition](http://yaxim.org/blog/2020/01/31/yaxim-0-dot-9-9-fosdem-edition/).

In the latest newsletter, we wrongly announced the release of profanity 0.8.0 due to a misunderstanding. Please be aware that [profanity 0.8.0 has been released](https://github.com/profanity-im/profanity/releases/tag/0.8.0) on the 3rd of February. Also, [a new blog has opened](https://profanity-im.github.io/blog/index.html).

Monal has seen [a lot of news in January](https://monal.im/2020/01/), among which Catalyst progress, iOS [4.2.1](https://monal.im/blog/monal-ios-4-2-1-released/) and [4.2.2](https://monal.im/blog/catalyst-and-ios-4-2-2/), and 4.2.3 releases to Testflight, [UI progress](https://monal.im/blog/mam-and-rethinking-the-ui/) in upcoming 4.3.

Please also follow progress:

* [Gajim development news January 2020](https://gajim.org/post/2020-01-27-development-news-january/)
* [SàT progress note 2020-W01](https://www.goffi.org/b/66adNNNbFp84CWFzyvGpmK/progress-note)
* zatrox, jbb & melvo, from the Kaidan team, explain their upcoming [streamlined registration process](https://www.kaidan.im/2020/01/08/Easy-Registration/) in the next Kaidan 0.5.0.

### Libraries 

Remi Corniere has released [go-xmpp v0.4.0](https://blog.process-one.net/go-xmpp-v0-4-0/).

Tigase has just introduced [halcyon](https://github.com/tigase/halcyon), a Kotlin multiplatform XMPP client library.

## Other 

Mastodon is getting [support for XMPP URIs](https://github.com/tootsuite/mastodon/issues/9776).

The EU H2020 [CPSwarm](https://www.cpswarm.eu/) project has produced as one of its main outcome the [CPSwarm Workbench](https://www.cpswarm.eu/index.php/cpswarm-workbench/), a toolchain to model, optimize, simulate and deploy a swarm of Cyber Physical Systems. One of its opensource components [released on Github](https://github.com/cpswarm), is the [Simulation and Optimization Environment](https://github.com/cpswarm/SimulationOrchestrator/wiki/Simulation-and-Optimization-Environment), which is used to evaluate the performance of a swarm solution. This environment has a distributed architecture based on XMPP, allowing to execute in parallel simulations on simulators deployed on distributed machines.

## Services 

Tigase has upgraded their public servers [xmpp.cloud](https://xmpp.cloud) with [SASL-EXTERNAL for federation, and MUC avatars](https://mastodon.technology/@tigase/103488503676998610).

Jonas Schäfer has described the [first update on search.jabber.network in 2020](https://sotecware.net/first-update-on-searchjabbernetwork-in-2020.html).

## Extensions and specifications

### Deferred 

* XEP-0283 (Moved)
* XEP-0313 (Message Archive Management)
* XEP-0335 (JSON Containers)
* XEP-0357 (Push Notifications)
* XEP-0359 (Unique and Stable Stanza IDs)
* XEP-0367 (Message Attaching)
* XEP-0373 (OpenPGP for XMPP)
* XEP-0384 (OMEMO Encryption)
* XEP-0385 (Stateless Inline Media Sharing (SIMS))
* XEP-0391 (Jingle Encrypted Transports)
* XEP-0397 (Instant Stream Resumption)
* XEP-0398 (User Avatar to vCard-Based Avatars Conversion)
* XEP-0399 (Client Key Support)
* XEP-0400 (Multi-Factor Authentication with TOTP)
* XEP-0403 (Mediated Information eXchange (MIX): Presence Support.)
* XEP-0404 (Mediated Information eXchange (MIX): JID Hidden Channels.)
* XEP-0406 (Mediated Information eXchange (MIX): MIX Administration)
* XEP-0407 (Mediated Information eXchange (MIX): Miscellaneous Capabilities)
* XEP-0408 (Mediated Information eXchange (MIX): Co-existence with MUC)
* XEP-0409 (IM Routing-NG)
* XEP-0411 (Bookmarks Conversion)

### Proposed 

* Title: Inbox
  * Abstract: This specification proposes a mechanism by which clients can find a list of ongoing conversations and their state.
  * URL: https://xmpp.org/extensions/inbox/inbox.html
* Title: Full Text Search in MAM
  * Abstract: This specification proposes a field in the MAM form for full text searching.
  * URL: https://xmpp.org/extensions/inbox/fulltext.html

### New 

* Version 0.1.0 of XEP-0427 (MAM Fastening Collation) has been released.
  * Abstract: This specification proposes a mechanism by which MAM results containing fastenings can be collated effectively.
  * URL: https://xmpp.org/extensions/xep-0427.html
* Version 0.1.0 of XEP-0428 (Fallback Indication) has been released.
  * Abstract: This specification proposes a mechanism by which message bodies can be marked as being purely for fallback purposes, and therefore to be ignored by intermediaries and anything that understands the remainder of the message.
  * URL: https://xmpp.org/extensions/xep-0428.html
* Version 0.1.0 of XEP-0429 (Special Interests Group End to End Encryption) has been released.
  * Abstract: This document proposes the formation of a Special Interest Group (SIG) within the XSF devoted to the development of end-to-end encryption within the context of XMPP.
  * URL: https://xmpp.org/extensions/xep-0429.html
* Version 0.1.0 of XEP-0431 (Full Text Search in MAM) has been released.
  * Abstract: This specification proposes a field in the MAM form for full text searching.
  * URL: https://xmpp.org/extensions/xep-0431.html
* Version 0.1.0 of XEP-0430 (Inbox) has been released.
  * Abstract: This specification proposes a mechanism by which clients can find a list of ongoing conversations and their state.
  * URL: https://xmpp.org/extensions/xep-0430.html

### Updated 

* Version 0.3.0 of XEP-0401 (Easy User Onboarding)
* Version 0.2.0 of XEP-0426 (Character counting in message bodies)
* Version 0.2.1 of XEP-0393 (Message Styling)
* Version 0.10.0 of XEP-0363 (HTTP File Upload)
* Version 0.2.1 of XEP-0425 (Message Moderation)
* Version 0.2.0 of XEP-0429 (Special Interests Group End to End Encryption)
* Version 0.2.0 of XEP-0431 (Full Text Search in MAM)

### Obsoleted 

* Version 1.0.1 of XEP-0412 (XMPP Compliance Suites 2019)
  * URL: https://xmpp.org/extensions/xep-0412.html

### Last Call 

* This message constitutes notice of a Last Call for comments on XEP-0363. The Last Call was restarted after the Council election, because the previous Council did not vote on the ongoing LC.
  * Title: HTTP File Upload
  * Abstract: This specification defines a protocol to request permissions from another entity to upload a file to a specific path on an HTTP server and at the same time receive a URL from which that file can later be downloaded again.
  * URL: https://xmpp.org/extensions/xep-0363.html
  * This Last Call begins today and shall end at the close of business on 2020-01-28.
* This message constitutes notice of a Last Call for comments on XEP-0402.
  * Title: Bookmarks 2 (This Time it's Serious)
  * Abstract: This specification defines a syntax and storage profile for keeping a list of chatroom bookmarks on the server.
  * URL: https://xmpp.org/extensions/xep-0402.html
  * This Last Call begins today and shall end at the close of business on 2020-02-12.

## Thanks all! 

This XMPP Newsletter is produced collaboratively by the community.

Thanks to MDosch, Vanitasvitae, Wurstsalat, Neustradamus, Jwi, geOrg, licaon-kter, guus, horazont for their help in creating it!

Please share the news on "social networks":

* Twitter: https://twitter.com/xmpp
* Mastodon: https://fosstodon.org/@xmpp/
* LinkedIn: https://www.linkedin.com/company/xmpp-standards-foundation/
* Facebook: https://www.facebook.com/jabber/
* Reddit: https://www.reddit.com/r/xmpp/

## License 

This newsletter is published under CC by-sa license: https://creativecommons.org/licenses/by-sa/4.0/
