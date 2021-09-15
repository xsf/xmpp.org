---
title: Happy new XMPP year! 14 Jan 2020
date: 2020-01-14
author: nyco
categories: ["Newsletter"]
aliases:
    - "/2020/01/newsletter-14-january/"
---

Happy new XMPP year!

Welcome to the XMPP newsletter covering the month of December 2019. Sorry, we are late...

Contribute to the community effort, which [process is fully documented](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## Articles 

[Whatsapp, Matrix or XMPP](https://www.golem.de/news/whatsapp-matrix-oder-xmpp-bmi-sucht-einen-messenger-fuer-bundesbehoerden-1912-145326.html) (german) - The German Federal Ministry of the Interior is looking for a messenger for the federal authorities while the German Federal Police is experimenting with XMPP. They are using an [Open Source Messenger "MOKA" based on Conversations](https://dipbt.bundestag.de/dip21/btd/19/152/1915218.pdf) (german).

Fabian Sauter known as COM8 (and developer of [UWPX](https://uwpx.org/)) has finalised his Bachelor Thesis on "[Smart Building Control with XMPP for IoT](https://home.in.tum.de/~sauterf/html-data/Thesis_Smart_Building_Control_with_XMPP_for_IoT.pdf)". Congratulations! The development will be continued with the goal of an official XEP.

Anoxinon e.V who intend to inform and improve the situation about privacy and free software as well run a XMPP Server are looking for [new board members](https://anoxinon.de/blog/logbuchspezial_zukunftdesvereins/).

Paul Schaub has written two pieces:
* [Pitfalls for OMEMO Implementations – Part 1: Inactive Devices](https://blog.jabberhead.tk/2019/12/13/pitfalls-for-omemo-implementations-part-1-inactive-devices/)
* [Re: The Ecosystem is Moving](https://blog.jabberhead.tk/2019/12/29/re-the-ecosystem-is-moving/) as an answer to Moxie Marlinspike's talk at 36C3 (Moxie is the creator of Signal)

![The Ecosystem is Moving](https://framapic.org/vnIr36vc8UVR/V2BVA5KG8ozl.png)

Alex Gnauck wrote about  [Simpler code in handlers using pattern matching](https://www.ag-software.net/2019/12/30/simpler-code-in-handlers-using-pattern-matching/) in MatriX.

During the 36C3 in December 2019, a bunch of people finalized the idea to form a [SIG dedicated to end-to-end encryption](https://mail.jabber.org/pipermail/standards/2019-December/036769.html).

### Newsletter translations 

* [French](https://linuxfr.org/news/lettre-d-information-xmpp-3-decembre-2019-xmpp-dans-toutes-les-langues)
* [German](https://www.jabber.de/xmpp-newsletter-xmpp-auf-allen-sprachen-03-dez-2019/)
* [Spanish](https://www.jabber.de/es-xmpp-newsletter-xmpp-en-todos-los-idiomas-03-dic-2019/)

## Software releases 

### Servers 

The Ignite Realtime community has released:

* [Openfire 4.5.0 Beta](https://discourse.igniterealtime.org/t/openfire-4-5-0-beta-release/86888)
* [Fastpath Openfire plugin 4.5.0 Beta](https://discourse.igniterealtime.org/t/fastpath-openfire-plugin-4-5-0-beta-release/86895)

### Clients and applications

Anu Pokharel the developer of Monal has made significant changes to its [MUC implementation](https://monal.im/blog/group-chat-improvements/) which improves the situation for iOS ([4.1 and 4.2](https://monal.im/blog/ios-4-1-and-4-2/) and [4.2 final beta](https://monal.im/blog/ios-4-2-final-beta/)) and macOS ([2.5 beta 1](https://monal.im/blog/mac-2-5-beta-1/) [2.5 beta 2](https://monal.im/blog/mac-2-5-beta-2/)) users. Furthermore there has been many [bug fixes](https://monal.im/blog/cve-fixes/), including [HTTP upload](https://monal.im/blog/http-upload/), and [the end of iOS9 support](https://monal.im/blog/the-end-of-ios-9-support/).

![Monal iOS](https://framapic.org/ZyopsYd66GsN/aOp2n1IrXfIy.png)

Gajim has posted their [Development News](https://gajim.org/post/2020-01-07-development-news-december/) for December 2019: old message dialog system, compact tooltip when hovering a group chat in Gajim’s contact list, new assistant for password change and account removal, HTTP File Upload now work asynchronously with the ‘libsoup’ library, bug fixes, plugin updates, and changes in python-nbxmpp.

Tigase has released [BeagleIM 3.4 and Siskin IM 5.4](https://tigase.net/beagleim-3.4-and-siskin-5.4-released/): BeagleIM 3.4 allows you to set MUC room avatar, simplifies MUC room settings, and bug fixes, while SiskinIM 5.4 adds support for setting MUC room avatar.

[Movim 0.16.1](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/cdfc0a4c-3459-4d3b-8c15-08994810d54e) has been released: you can now share posts to your connected chatrooms, communities layout was redesigned, all the messages that you sent in the one to one discussions can now be edited, the videoconferencing feature was heavily refactored, and bugs fixed.

Development versions of [Profanity 0.8.0](https://twitter.com/ProfanityIM/status/1207735919488438273) have been released with consistent color generated nicks (XEP-0392) and a trackbar so you see where you left off reading!

Goffi has published the [SàT progress note 2019-W51](https://www.goffi.org/b/JLPTTHfRnqhxNozHjRz553/progress-note): infinite scroll is now implemented in Cagou, Kivy community extensions used by SàT are now installable like any other Python dependency, e2e encryption with OMEMO, and more.

### Libraries

[gloox 1.0.23 released](https://camaya.net/news/gloox-1-0-23-released/) as a maintenance version.

## GSoC 

Google Summer of Code 2020 has been announced, some XMPP projects have already shown interest to mentor students.

## Extensions and specifications 

### New 

#### XEP-0426: Character counting in message bodies 

Version 0.1.0 of XEP-0426 (Character counting in message bodies) has
been released.

Abstract:
This document describes how to correctly count characters in message
bodies. This is required when referencing a position in the body.

Changelog:
Promote to Experimental as per Council decision. (mb)

URL: https://xmpp.org/extensions/xep-0426.html

### Proposed 

#### Character counting in message bodies 

Title: Character counting in message bodies
Abstract:
This document describes how to correctly count characters in message
bodies. This is required when referencing a position in the body.

URL: https://xmpp.org/extensions/inbox/charcount.html

#### User-defined Data Transfer 

Title: User-defined Data Transfer
Abstract:
This specification proposes a simple mechanism by which applications
can transfer data safely, without needing additional protocol design
work. It is intended to provide a protocol that is trivial to
implement and can be driven with a simple API.

URL: https://xmpp.org/extensions/inbox/udt.html

#### MAM Fastening Collation 

Title: MAM Fastening Collation
Abstract:
This specification proposes a mechanism by which MAM results
containing fastenings can be collated effectively.

URL: https://xmpp.org/extensions/inbox/mamfc.html

#### Fallback Indication 

Title: Fallback Indication
Abstract:
This specification proposes a mechanism by which message bodies can be
marked as being purely for fallback purposes, and therefore to be
ignored by intermediaries and anything that understands the remainder
of the message.

URL: https://xmpp.org/extensions/inbox/fallback.html

#### Special Interests Group End to End Encryption 

Title: Special Interests Group End to End Encryption
Abstract:
This document proposes the formation of a Special Interest Group (SIG)
within the XSF devoted to the development of end-to-end encryption
within the context of XMPP.

URL: https://xmpp.org/extensions/inbox/sige2ee.html

### Updated 

* Version 0.13.2 of XEP-0280 (Message Carbons) has been released.
* Version 0.1.2 of XEP-0284 (Shared XML Editing) has been released.
* Version 0.2.1 of XEP-0328 (JID Preparation and Validation Service) has been released.
* Version 0.1.2 of XEP-0422 (Message Fastening) has been released.

## Thanks all! 

This XMPP Newsletter is produced collaboratively by the community.

Thanks to Wurstsalat, Echolon, Guus, MDosch for their help in creating it!

Please share the news on "social networks":

* Twitter: https://twitter.com/xmpp
* Mastodon: https://fosstodon.org/@xmpp/
* LinkedIn: https://www.linkedin.com/company/xmpp-standards-foundation/
* Facebook: https://www.facebook.com/jabber/
* Reddit: https://www.reddit.com/r/xmpp/

## License 

This newsletter is published under CC by-sa license: https://creativecommons.org/licenses/by-sa/4.0/
