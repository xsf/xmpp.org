---
Title: An Overview of XMPP
Url: about/technology-overview
aliases:
    - "/about/technology-overview.html"
---

XMPP is the Extensible Messaging and Presence Protocol, a set of open technologies for instant messaging, presence, multi-party chat, voice and video calls, collaboration, lightweight middleware, content syndication, and generalized routing of XML data.

XMPP was originally developed in the Jabber open-source community to provide an open, decentralized alternative to the closed instant messaging services at that time. XMPP offers several key advantages over such services:

- **Open** — the XMPP protocols are free, open, public, and easily understandable; in addition, multiple implementations exist in the form of clients, servers, server components, and code libraries.

- **Standard** — the [Internet Engineering Task Force (IETF)](https://www.ietf.org/) has formalized the core XML streaming protocols as an approved instant messaging and presence technology. The XMPP specifications were published as [RFC 3920](/rfcs#3920) and [RFC 3921](/rfcs#3921) in 2004, and the XMPP Standards Foundation continues to publish many [XMPP Extension Protocols](/extensions/). In 2011 the core RFCs were revised, resulting in the most up-to-date specifications ([RFC 6120](/rfcs#6120), [RFC 6121](/rfcs#6121), and [RFC 7622](/rfcs#7622)).

- **Proven** — the first Jabber/XMPP technologies were developed by Jeremie Miller in 1998 and are now quite stable; hundreds of developers are working on these technologies, there are tens of thousands of XMPP servers running on the Internet today, and millions of people use XMPP for instant messaging through various public services and XMPP deployments at organizations worldwide.

- **Decentralized** — the architecture of the XMPP network is similar to email; as a result, anyone can run their own XMPP server, enabling individuals and organizations to take control of their communications experience.

- **Secure** — any XMPP server may be isolated from the public network (e.g., on a company intranet) and robust security using SASL and TLS has been built into the core [XMPP specifications](/rfcs). In addition, the XMPP developer community is actively working on end-to-end encryption to raise the security bar even further.

- **Extensible** — using the power of XML, anyone can build custom functionality on top of the core protocols; to maintain interoperability, common extensions are published in the [XEP series](/extensions), but such publication is not required and organizations can maintain their own private extensions if so desired.

- **Flexible** — XMPP applications beyond IM include network management, content syndication, collaboration tools, file sharing, gaming, remote systems monitoring, web services, lightweight middleware, cloud computing, and much more.

- **Diverse** — a wide range of companies and open-source projects use XMPP to build and deploy real-time applications and services; you will never get “locked in” when you use XMPP technologies.

This page provides an introduction to various XMPP technologies, including links to specifications, implementations, tutorials, and special-purpose discussion venues.

Key XMPP technologies:

- [Core](#core) — information about the core XMPP technologies for XML streaming
- [Jingle](#jingle) — SIP-compatible multimedia signalling for voice, video, file transfer, and other applications
- [Multi-User Chat](#muc) — flexible, multi-party communication
- [PubSub](#pubsub) — alerts and notifications for data syndication, rich presence, and more
- [BOSH](#bosh) — an HTTP binding for XMPP (and other) traffic

Furthermore, we would like to suggest the independent [Modern XMPP project](https://docs.modernxmpp.org/) which attempts to improve the quality of user-to-user messaging applications that use XMPP.

## Core{#core}

At its core, XMPP is a technology for streaming XML over a network. The protocol, which emerged from the Jabber open-source community in 1999, was originally designed to provide an open, secure, decentralized alternative to consumer-oriented instant messaging (IM) services like ICQ, AIM, and MSN. The core technologies were formalized under the name Extensible Messaging and Presence Protocol (XMPP) at the [IETF](https://www.ietf.org/) in 2004. These core technologies include:

- The base XML streaming layer
- Channel encryption using Transport Layer Security (TLS)
- Strong authentication using the Simple Authentication and Security Layer (SASL)
- Use of UTF-8 for complete Unicode support, including fully internationalized addresses
- Built-in information about network availability (“presence”)
- Presence subscriptions for two-way authorization
- Presence-enabled contact lists (“rosters”)

#### Specifications

The core XMPP technologies are defined in two RFCs published by the IETF:

- [RFC 6120: XMPP Core](/rfcs#6120)
- [RFC 6121: XMPP IM](/rfcs#6121)
- [RFC 7622: XMPP Address Format](/rfcs#7622)

The first XMPP RFCs ([RFC 3920](/rfcs#3920) and  [RFC 3921](/rfcs#3921)) were produced by the IETF’s XMPP Working Group in October 2004. In 2011 they were revised, resulting in the current specifications.

#### Implementations

There are [many implementations](/software/) of the core XMPP specifications.

## Jingle{#jingle}

In essence, Jingle provides a way for Jabber clients to set up, manage, and tear down multimedia sessions. Such sessions can support a wide range of application types (such as voice chat, video chat, and file transfer) and use a wide range of media transport methods (such as TCP, UDP, RTP, or even in-band XMPP itself). The signalling to establish a Jingle session is sent over XMPP, and typically the media is sent directly peer-to-peer or through a media relay. Jingle provides a pluggable framework for both application types and media transports; in the case of voice and video chat, a Jingle negotiation usually results in use of the Real-time Transport Protocol (RTP) as the media transport and thus is compatible with existing multimedia technologies such as the Session Initiation Protocol (SIP). Furthermore, the semantics of Jingle signalling was designed to be consistent with both SIP and the Session Description Protocol (SDP), thus making it straightforward to provide signalling gateways between XMPP networks and SIP networks.

#### Specifications

Jingle is defined in a number of specifications:

- [XEP-0166: Jingle](/extensions/xep-0166.html)
- [XEP-0167: Jingle RTP Sessions](/extensions/xep-0167.html)
- [XEP-0176: Jingle ICE-UDP Transport Method](/extensions/xep-0176.html)
- [XEP-0177: Jingle Raw UDP Transport Method](/extensions/xep-0177.html)
- [XEP-0181: Jingle DTMF](/extensions/xep-0181.html)
- [XEP-0234: Jingle File Transfer](/extensions/xep-0234.html)

#### Implementations
_Note: Many of the following implementations support the older Google Talk protocol and are being upgraded to support Jingle as it is defined in the specifications; contact the project developers for details._

__Clients__

- [Gajim](https://gajim.org/)
- [Jitsi](https://jitsi.org/)
- [Movim](https://movim.eu)
- [Pidgin](https://pidgin.im/)
- [Psi](https://psi-im.org/)
- [Telepathy](https://telepathy.freedesktop.org/)
- [YateClient](https://yate.ro/opensource.php?page=yateclient)

__Libraries__

- [libjingle](http://code.google.com/apis/talk/) (C/C++)
- [Smack](http://www.igniterealtime.org/projects/smack/) (Java)
- [Telepathy Gabble](https://telepathy.freedesktop.org/components/telepathy-gabble/) (C)
- [yjingle](https://yate.ro/) (C++)

__Call Managers / VoIP Servers__

- [Asterisk](https://www.asterisk.org/)
- [FreeSWITCH](https://signalwire.com/freeswitch)
- [Yate](https://yate.ro/)


## Multi-User-Chat (MUC){#muc}

MUC is an XMPP extension for multi-party information exchange similar to Internet Relay Chat (IRC), whereby multiple XMPP users can exchange messages in the context of a room or channel. In addition to standard chatroom features such as room topics and invitations, the protocol defines a strong room control model, including the ability to kick and ban users, to name room moderators and administrators, to require membership or passwords in order to join the room, etc. Because MUC rooms are based on XMPP, they can be used to exchange not only plaintext message bodies but a wide variety of XML payloads.

#### Specifications

MUC is defined in one primary specification (XEP-0045) and several ancillary specifications:

- [XEP-0045: Multi-User Chat](https://xmpp.org/extensions/xep-0045.html)
- [XEP-0249: Direct MUC Invitations](https://xmpp.org/extensions/xep-0249.html)
- [XEP-0272: Multiparty Jingle](https://xmpp.org/extensions/xep-0272.html)

#### Implementations

__Servers__ - the following XMPP servers include built-in support for MUC:

- [ejabberd](https://www.ejabberd.im/)
- [Jabber XCP](https://www.cisco.com/)
- [M-Link](https://www.isode.com/product/xmpp-server/)
- [MongooseIM](https://github.com/esl/MongooseIM)
- [Openfire](http://www.igniterealtime.org/projects/openfire/index.jsp)
- [Prosody](https://prosody.im/)
- [Tigase](https://tigase.org/)

__External Components__ - the following standalone components can be used with a wide variety of XMPP servers:

- [mu-conference](https://gna.org/projects/mu-conference/)
- [palaver](https://github.com/twonds/palaver)

__Clients__

- [Adium](https://adium.im/)
- [Gajim](https://gajim.org/)
- [mcabber](https://mcabber.com/)
- [Movim](https://movim.eu)
- [Pidgin](https://pidgin.im/)
- [Psi](https://psi-im.org/)

__Libraries__

- [gloox](https://camaya.net/gloox) (C++)
- [libpurple](https://developer.pidgin.im/wiki/WhatIsLibpurple) (C)
- [Smack](http://www.igniterealtime.org/projects/smack/index.jsp) (Java)
- [XMPP4R](https://xmpp4r.github.io/) (Ruby)

## PubSub{#pubsub}

PubSub is a protocol extension for generic publish-subscribe functionality, specified in XEP-0060. The protocol enables XMPP entities to create nodes (topics) at a pubsub service and publish information at those nodes; an event notification (with or without payload) is then broadcasted to all entities that have subscribed to the node. Pubsub therefore adheres to the classic Observer design pattern and can serve as the foundation for a wide variety of applications, including news feeds, content syndication, rich presence, geolocation, workflow systems, network management systems, and any other application that requires event notifications. The personal eventing protocol (PEP), specified in XEP-0163, provides a presence-aware profile of PubSub that enables every user’s JabberID to function as a virtual pubsub service for rich presence, microblogging, social networking, and real-time interactions.

#### Specifications

PubSub is defined in several specifications:

- [XEP-0060: Publish-Subscribe](https://xmpp.org/extensions/xep-0060.html)
- [XEP-0163: Personal Eventing Protocol](https://xmpp.org/extensions/xep-0163.html)
- [XEP-0248: PubSub Collection Nodes](https://xmpp.org/extensions/xep-0248.html)

#### Payloads
PubSub and PEP are “payload-agnostic” — you can use them as neutral transports for a wide variety of data formats. Some of the more popular payloads are listed below, especially for rich presence related to IM users:

- [Activities](/extensions/xep-0108.html)
- [Atom / RSS Notifications](/internet-drafts/draft-saintandre-atompub-notify-07.html)
- [Avatars](/extensions/xep-0084.html)
- [Chatroom Visits](/extensions/xep-0194.html)
- [Gaming Activities](/extensions/xep-0196.html)
- [Geolocation](/extensions/xep-0080.html)
- [Moods](/extensions/xep-0107.html)
- [Music Tunes](/extensions/xep-0118.html)
- [TV/Video Activities](/extensions/xep-0197.html)
- [Website Visits](/extensions/xep-0195.html)

#### Implementations

__Servers__ - the following XMPP servers include built-in support for PubSub or PEP:

- [ejabberd](https://www.ejabberd.im/)
- [Jabber XCP](https://www.cisco.com/)
- [M-Link](https://www.isode.com/product/xmpp-server/)
- [Openfire](http://www.igniterealtime.org/projects/openfire/index.jsp)
- [Tigase](https://tigase.org/)

__Server Components__

- [Idavoll](https://github.com/ralphm/idavoll)

__Clients__

- [Gajim](https://gajim.org/)
- [Movim](https://movim.eu)
- [Psi](https://psi-im.org/)

__3.4 Libraries__

- [strophe](https://strophe.im/) (C or JavaScript)
- [XMPP4R](https://xmpp4r.github.io/) (Ruby)

## BOSH{#bosh}

BOSH is “Bidirectional-streams Over Synchronous HTTP”, a technology for two-way communication over the Hypertext Transfer Protocol (HTTP). BOSH emulates many of the transport primitives that are familiar from the Transmission Control Protocol (TCP). For applications that require both “push” and “pull” communications, BOSH is significantly more bandwidth-efficient and responsive than most other bidirectional HTTP-based transport protocols and the techniques known as AJAX. BOSH achieves this efficiency and low latency by avoiding HTTP polling, yet it does so without resorting to chunked HTTP responses as is done in the technique known as Comet. To date, BOSH has been used mainly as a transport for traffic exchanged between Jabber/XMPP clients and servers (e.g., to facilitate connections from web clients and from mobile clients on intermittent networks). However, BOSH is not tied solely to XMPP and can be used for other kinds of traffic, as well.

#### Specifications BOSH is defined in two specifications:

- [XEP-0124: Bidirectional-streams Over Synchronous HTTP](https://xmpp.org/extensions/xep-0124.html)
- [XEP-0206: XMPP Over BOSH](https://xmpp.org/extensions/xep-0206.html)

#### Implementations

Servers The following XMPP servers include built-in support for BOSH:

- [ejabberd](https://www.ejabberd.im/)
- [Jabber XCP](https://www.cisco.com/)
- [M-Link](https://www.isode.com/product/xmpp-server/)
- [MongooseIM](https://github.com/esl/MongooseIM)
- [Openfire](http://www.igniterealtime.org/projects/openfire/index.jsp)
- [Prosody](https://prosody.im/)
- [Tigase](https://tigase.org/)

#### Connection Managers

The following standalone XMPP connection managers can be used with a wide variety of XMPP servers:

- [JabberHTTPBind](http://blog.jwchat.org/jhb/)
- [Punjab](https://github.com/twonds/punjab)
- [node-xmpp-bosh](https://github.com/xmppo/node-xmpp-bosh)
- [rhb](http://rubyforge.org/projects/rhb/)

#### Clients

- [Adium](https://adium.im/)
- [Gajim](https://gajim.org/)
- [Pidgin](https://pidgin.im/)
- [Swift](https://swift.im/swift.html)
- [Tigase Messenger](http://www.tigase.org/project/messenger)
- [Tigase Minichat](http://www.tigase.org/project/minichat)

#### Libraries

- [gloox](https://camaya.net/gloox) (C++)
- [strophe](https://strophe.im/) (C or JavaScript)
- [Swiften](https://swift.im/swiften.html) (C++)
- [XMPP4GWT](http://www.tigase.org/project/xmpp4gwt) (gwt)
- [XMPP4R](https://xmpp4r.github.io/) (Ruby)
