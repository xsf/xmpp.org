---
title: The 19th XMPP Summit and FOSDEM 2016
date: 2016-02-08
authors: Tobi; Nyco
categories: ["XMPP Summit", "FOSDEM"]
aliases:
    - "/2016/02/the-19th-xmpp-summit-and-fosdem-2016/"
---

## 19th XMPP Summit

In late January 2016, from the 28th to the 29th, the XSF held its XMPP Summit in Brussels, Belgium. It was the 19th meeting by XMPP standards writers, implementers, and enthusiasts since the first XMPP Summit in July 2006.
Among the topics we discussed were MIX, efficient reconnections and, as always, end-to-end security.

[XSF at work at XMPP Summit](https://twitter.com/nyconyco/status/692734779809251329)

MIX, defined in [XEP-0369: Mediated Information Exchange](//xmpp.org/extensions/xep-0369.html), is a replacement for the current multi-user chat standard ([XEP-0045](//xmpp.org/extensions/xep-0045.html)). Classic MUC was first standardized 14 years ago. While it has received some updates and fixes over the years, it still has severe issues considering modern usage scenarios: like mobile devices without a permanent connection and on low bandwith, or rich-media applications with images, movies and voice/video conversations.

MIX is a new protocol aiming to solve these issues and provide a clean solution, based on [Publish-Subscribe](//xmpp.org/extensions/xep-0060.html) allowing independent distribution of messages, configuration, presence and more, and [Message Archive Management](//xmpp.org/extensions/xep-0313.html) for chat history. 

MIX related topics like mentioning others in a chat room, conversation threading and bookmarks have also been discussed and to some extent already standarized shortly after the summit. MIX will enable the implementation of modern group-chat applications with a good user experience in an easier fashion compared to classic MUC.

Simple and efficient reconnection was another large topic discussed at the XMPP Summit. The protocol for a full connection of modern XMPP clients has become more complex and extensive over the years as features have been added. This includes stuff like TLS negotiation, synchronization of contact lists, feature discovery and more.

We collectively analyzed the protocol a modern feature-full XMPP client uses to login, and highlighted opportunities to reduce traffic, round trips and latency. An efficient reconnection is becoming more important as more and more chat applications run on a mobile device and reconnect quite often. A writeup of our findings and directions to possible optimizations will soon follow in the form of an informational XEP.

Finally, end-to-end security between XMPP clients was shortly discussed. The current ideas mainly evolve around [fixing OpenPGP usage in XMPP](http://geekplace.eu/xeps/xep-openpgp/xep-openpgp.html) and the Axolotl-based [OMEMO proposal](https://conversations.im/omemo/). Here, our discussion mainly focused on current issues around the OMEMO proposal like missing support for full-stanza encryption and the threat model OMEMO is designed to protect against.

On the evening of the 28th, we also had our traditional XSF Dinner with interesting discussions and delicious food.

[XSF Dinner](https://twitter.com/DwdDave/status/692837510498504704)

[XSF Dinner](https://twitter.com/JBinary/status/693001521382973440)

We would like to thank the summit's sponsors, [AG-Software](http://www.ag-software.net/), [Cisco](http://www.cisco.com/) and [Surevine](http://www.surevine.com), for enabling this great meetup and the XSF Dinner.

##FOSDEM 2016

In the [Real Time devroom](https://fosdem.org/2016/schedule/track/real_time/), there has been a lot happening around the SIP and WebRTC protocols & ecosystems, but also around XMPP.

Panagiotis Stathopoulos presented ["Sharp.Xmpp, a multiplatform .NET XMPP client library and Android"](https://fosdem.org/2016/schedule/event/sharpxmpp/) with some real world return of experience around battery and bandwidth efficiency.

Nicolas (Nÿco) Vérité presented ["The state of XMPP and instant messaging, The awakening"](https://fosdem.org/2016/schedule/event/state_of_xmpp/) introducing the 3 generations of Instant Messaging, the trough of disillusionment, and consequently the necessary cleanup yet to be accomplished.

[The state of XMPP and instant messaging](https://twitter.com/nyconyco/status/693449757155577856)

Dave Cridland talked about ["Reigniting Openfire: A tale of birth, death, zombies, and resurrection"](https://fosdem.org/2016/schedule/event/openfire/) (with a lie about zombies), showing the history of the [Openfire](http://www.igniterealtime.org/projects/openfire/) XMPP server.

Matthew Wild talked about ["XMPP: Beyond standards, Exploring the non-technical requirements of open communication"](https://fosdem.org/2016/schedule/event/xmpp_beyond_standards/) which echoes the need to focus less on lower layers, but more in the user space.

[Matthew Wild presenting XMPP 2016](https://twitter.com/zooldk/status/693456193189232641)

Jérôme Poisson (Goffi) presented ["How we built a decentralized blogging engine with XMPP"](https://fosdem.org/2016/schedule/event/decentralized_blogging_with_xmpp/) in Libervia (Salut à Toi), demonstrating the capacities of XMPP outside of chat.

The Real Time lounge was a booth where people could sit in large cushions, to openly discuss about Real Time Communications.

[Setting up at FOSDEM](https://twitter.com/DwdDave/status/693352392914530304)

In the Main Track, beyond the scope of only Real Time Communications, Daniel Pocock presented ["Free communications with Free Software is there any credible way to build a trustworthy communications platform without using free software?"](https://fosdem.org/2016/schedule/event/free_communications/).

[Daniel Pocock introducing humourously 'Free comms with free software'](https://twitter.com/nyconyco/status/693721422523437056)

Overall, the participants were [all](https://twitter.com/michalwski/status/695155070246215681) [quite](https://twitter.com/winfriedtilanus/status/693890533442392064) [satisfied](https://twitter.com/iNPUTmice/status/693822618735108096) with what they achieved and we are looking forward to our next XMPP Summit.
