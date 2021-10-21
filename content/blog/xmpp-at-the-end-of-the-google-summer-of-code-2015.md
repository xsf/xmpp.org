---
title: XMPP at the end of the Google Summer of Code 2015
date: 2015-12-18
author: Kev
categories: ["Google Summer of Code"]
---

This year we had six students working on disparate projects for GSoC, and we're delighted that all of them were successful! Here we link to a wrapup blog post from each of the students, and a description of their work from their mentors.

We had Adhish Singh working on [Internet of Things implementations](http://www.xmpp-iot.org/gsoc/week-12/). His mentor, Joachim, said:

```
Adhish Singla: [Prototyping tools for IoT](http://www.xmpp-iot.org/gsoc/)

Adhish started from no XMPP experience and have created 2 graphical interfaces to IoT devices supporting xep 323 and xep 325 (experimental). One as a standalone Cordova mobile application and one as part of the converse.js webpage xmpp client. He also implemented a python history client that is instatiated as another resource on a Device IoT JID and polls the device for momentary values and stores history in db or local storage. So when clients ask for historical data it will in parallell with the originating device return the longtime history as part of the XEP323 history part. The javascript parts was done with crafted IQ messaging but will be enhanced with real plugin usage that is now part of the strophe package. python code will be submitted into SleekXMPP distribution. Converse code is running on the [site](http://www.xmpp-iot.org/).
```

We had Andreas Straub working on [end to end encryption in the Conversations client](http://conversationsgsoc2015.blogspot.co.uk/2015/09/omemo.html). His mentor Daniel says:

```
Andreas Straub: Implementing Axolotl over XMPP

In just three month time Andreas managed to basically invent and implement a completely new protocol for multi-end to multi-end encryption. Compared to the commonly used OTR encryption which has  reliability problems in mobile- and multi client setups the new protocol works very well with multiple clients and offline messages while maintaining crypto features such as deniability and forward secrecy. Even after the Google Summer of Code was over Andreas stuck around and created an XEP based on the experienced gather during the implementation. It is currently in the inbox of the XSF and called 'OMEMO Encryption'. A new name was chosen to highlight the fact that - besides using axolotl internally - it is a completely new protocol and incompatible with other implementations that utilize axolotl.
```

We had Daniel Baczynski working on [multi-account support in the Swift client](http://danielbgsoc.blogspot.co.uk/2015/08/polishing-and-fixing-existing-code.html). His mentor, Kev, says:

```
Daniel had a tricky job this summer - to add support for using multiple accounts at once to the Swift client. Rather than being protocol-difficult, as some of the other projects, this one was tricky because of the pervasive nature of and difficult user experience changes needed in the project. Over the course of the summer he made significant progress towards multaccount support, and we hope to have the feature completed for a future release.</blockquote>
```

We had Ishan Khanna working on serverless messaging in the Smack library. His mentor Florian says:

```
Ishan Khanna, Add support for XMPP Serverless Messaging (XEP-174) to Smack

From the very start Ishan was very motivated to add support for
serverless messaging based on DNS-SD and mDNS as described in XEP-147 to
Smack. While the problem description is trivial, the solution involves
many protocols (XMPP, DNS-SD, mDNS, ...), concepts and technology stacks
(Smack, jmdns, ...) that need to be understood in order to be able to
implement XMPP serverless messaging. Ishan implemented a working
solution and and demonstrated how other XMPP clients are able to
discover and exchange messages with the smack serverless implementation.
```

We had Marvin Wißfeld working on [DNSSEC support in the Smack library](http://mar-v-in.github.io/gsoc15/weekly-report/2015/08/21/thanks.html). His mentor Dave says:

```
Marvin W: Adding DNSSEC Support to Smack via miniDNS

A solid implementation of DNSSEC that can span everything from server to mobile would be an accomplishment from any developer - to get this done from scratch in a single summer as a student in GSoC really is amazingly impressive. XMPP relies on DNS for federated service discovery, both from client to server and between servers, and including DNSSEC in this capability gives a huge uplift in security across the board, providing cryptographically assured DNS lookups. Marvin implemented this in miniDNS, and added the needed support to Smack, so this can now be available on Android and desktop clients, and miniDNS can be used by servers as well.
```

We had Tarun Gupta working on [extending the Stroke library with all the features from its Swiften sister-project](http://tarun018.blogspot.co.uk/2015/08/wrap-up.html). His mentor Kev said:

```
Tarun took on a huge project this summer and achieved much more than I would have expected. His project to update Stroke with all the features available in the Swiften library was a great success, and has made Stroke much more useful for developers. Over the course of the summer Tarun touched nearly 600 files, and ported over 35,000 lines of code. A massive achievement.
```

Thanks to all the students for their efforts over the summer, and good luck in their future endeavours (although we hope they'll stick around!).
