---
title: Everyone go for decentralisation! 03 Apr 2020
date: 2020-04-03
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/04/everyone-go-for-decentralisation-03-apr-2020/"
---

## Intro

Welcome to the XMPP newsletter covering the months of February and March 2020.

This is a big one!

Help us sustain this as a community effort, which [process is fully documented](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

Anyway, we are always happy to contributors - just come along and talk to us in the [Comm-Team MUC](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort, which [process is fully documented](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

{{< newsletter-subscribe >}}

#### Newsletter translations

The translations of the XMPP Newsletter will be released here:

- German and Spanish: [https://www.jabber.de/](https://www.jabber.de/)
- French: [https://news.jabberfr.org/category/newsletter/](https://news.jabberfr.org/category/newsletter)

## Articles

A nice and short summary about XMPP - [en español](https://www.altaruru.com/que-es-xmpp/)!

Marvin Schirrmacher [analysed WhatsApp's VoIP protocol](https://medium.com/@schirrmacher/analyzing-whatsapp-calls-176a9e776213).
He extracted cryptographic keys and also showed that code obscurity does not finally protect against attackers.
Further readings on GitHub [here](https://github.com/schirrmacher/files/blob/master/WhatsApp%20VoIP%20Protocol.pdf),
[here](https://github.com/schirrmacher/files/blob/master/WhatsApp) and [here](https://github.com/schirrmacher/files/blob/master/WhatsAppCore).

[Mobile Kommunikation: zeitgemäß und rechtskonform](https://www.behoerden-spiegel.de/2020/02/12/mobile-kommunikation-zeitgemaess-und-rechtskonform/):
A German article about mobile communication in authorities mentioning MOKA/XMPP.

Daniel Gultsch (iNPUTmice) [published several posts](http://nitter.net/iNPUTmice/status/1228950491805167617#m) commenting on the situation on OMEMO initial vectors.

A discussion (Spanish) on Quey compared the [performance of XMPP and Matrix](https://quey.org/@GatoOscuro/103685251805747041). Seems that XMPP outperforms easily!

Liz Flynn scheduled a [notification for IETF-107](https://datatracker.ietf.org/wg/mls/history/) for Messaging Layer Security (MLS). You can read the current architecture draft [here](https://datatracker.ietf.org/doc/draft-ietf-mls-architecture/).

After a recent [secruity flaw in WhatsApp groups](https://www.dw.com/en/whatsapp-security-flaw-over-60000-groups-still-accessible-online/a-52543414), the FSFE recommends XMPP as [decentral and open alternative amd solution](https://fsfe.org/news/2020/news-20200228-01.en.html). The XSF tweeted about this already.

Stefan Kropp (debxwoody) has started to build a [place for German users of XMPP](https://xmpp-messenger.de/index.html) including social media, mailing list, homepage and a blog. He is calling for supporters!

After the Prosody team [released Snikket](https://blog.prosody.im/introducing-snikket/), Alexander Gnauck explains how to run it on your [NAS](https://www.ag-software.net/2020/02/28/run-snikket-on-your-nas/). 

Sam Whited wrote about the [Go XMPP library](https://blog.samwhited.com/2020/02/extensions-in-mellium/).

Turns out [Grindr uses #XMPP for their in-app chat](https://mastodon.xyz/@jcbrand/103757814572529323)

Edward Maurer (emus) created a blog post from his brainstorming and talk on a [vision for XMPP](https://www.jabber.de/guest-article-xmpp-vision/) he created during the Berlin "Online" Sprint.

## Events

After the work from Düsseldorf sprint [OMEMO has been released to version 0.4](https://github.com/xsf/xeps/pull/903 XEP-0384) - Congratulations to the authors! Further readings of their notes on [NEWMEMO](https://hackmd.syndace.com/s/r1fNElZSL) and [OMEMO:1 Requirement](https://hackmd.syndace.com/jG00qKF0SUy_AKUlXJcblQ#). Paul Schaub luckily alo could not refuse to again published his summary: [OMEMO Specification Sprint](https://blog.jabberhead.tk/2020/03/10/omemo-specification-sprint/).

On 1-2 February, [FOSDEM](https://fosdem.org/2020/), was held in Brussels, Belgium. As usual the XMPP community coordinated the Real-Time Lounge, a corner where several open source projects around Real Time Communication can present themselves. At the XMPP booth there were lots of nice conversations with FOSDEM visitors. The easy onboarding of Snikket was one of the eye catchers at the booth. In the Real Time developers room thee was a talk about the [modularity of the XMPP protocol](https://fosdem.org/2020/schedule/event/xmpp/) by Winfried Tilanus.

As usual, before FOSDEM a part of the XMPP community gathered for [XMPP summit 24](https://wiki.xmpp.org/web/Conferences/Summit_24). Over the course of two days many aspects of the XMPP protocol were discussed, including onboarding, 'rich presence', several aspects of encryption, MIX, Bind/SASL, Stickers and rich markup. The attendants regarded this summit as very productive and many of the discussions already resulted in proposed protocol extensions and patches to existing extensions.

The Berlin "Online" Sprint is over! No chance for COVID-19 - it was a non-voluntary situation, but great experience and impressive amount of people attended. Tim Schrock from the DBJR published a [short summary of our virtual sprint](https://www.dbjr.de/en/article/entwicklerinnentreffen-zu-freier-kommunikation/).

## Software releases
          
### Servers 

Jackal (XMPP server written in Go) was [released in version 0.82](https://github.com/ortuman/jackal/releases/tag/v0.8.2).

The Ignite Realtime Community [releases version 4.5.1](https://discourse.igniterealtime.org/t/openfire-4-5-1-is-released/87183) of Openfire with fixes and improvements you can review in their [changelogs](http://download.igniterealtime.org/openfire/docs/latest/changelog.html). REST API Openfire plugin was also released in [version 1.4.0](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-4-0-released/87286).

Erlang Solutions wrote about [improvements of push notifications within MongooseIM](https://www.erlang-solutions.com/blog/improving-push-notifications-with-mongooseim.html).
Mongoose also release MongooseIM [version 3.6.1](https://github.com/esl/MongooseIM/releases/tag/3.6.1) and [MongoosePush version 2.0.1](https://github.com/esl/MongoosePush/releases/tag/2.0.1).

ProcessOne released [go-xmpp in version 0.5.0](https://blog.process-one.net/go-xmpp-v0-5-0/). And on top of that their [xmpp-notifer v1.0.0](https://blog.process-one.net/xmpp-notifer-v1-0-0/) which allows to send notification to XMPP.

During the Berlin Online XMPP Sprint, [version 0.0.4 of sms4you](https://gitlab.com/xamanu/sms4you/-/releases#0.0.4), the personal SMS gateway, has been prepared and released. sms4you forwards text messages to and from XMPP, or alternatively to and from email. It is already in Debian "sid".

### Clients and applications

Tigase has released new [versions of BeagleIM and Siskin](https://tigase.net/beagleim-3.6-and-siskin-5.6-released/).

Goffi has released his SàT [progress note 2020-W08](https://www.goffi.org/b/HsWxUHzXdvsH7Syrx8f6Ne/progress-note).

A bunch of clients have switch OMEMO IV 16 byte to 12 byte. Those were [Conversations](https://github.com/siacs/Conversations/releases/tag/2.7.0), [Gajim](https://dev.gajim.org/gajim/gajim-plugins/commit/25cba9eea702336e82f75faf829873987c72dd33), [Psi](https://github.com/psi-im/plugins/commit/d39789cb986644bcc4c34ca55a20b50357ae342a) and [Profanity](https://github.com/profanity-im/profanity/commit/0089fbcf0a7bf3ba92fa2ba657c5e7d70e395ed7).

Chris Ballinger release version [5.0.1](https://github.com/ChatSecure/ChatSecure-iOS/releases/tag/v5.0.1) of ChatSecure.

The release of Movim 0.17 - Catalina includes [global chatroom search, a night theme, message retractation and UI changes](https://nl.movim.eu/?post/pubsub.movim.eu/Movim/87633da7-3963-4923-aabc-54ac5f6ad1d8).

Pix-Art Messenger will remove its [OTR legacy code by mid of 2020](https://github.com/kriztan/Pix-Art-Messenger/blob/master/docs/encryption.md). Experts on [any future OTRv4 implementation are invited to contribute new code](https://github.com/kriztan/Pix-Art-Messenger/issues/427). 

Profanity has release notes for version [0.8.0](https://github.com/profanity-im/profanity/releases/tag/0.8.0) and [0.8.1](https://github.com/profanity-im/profanity/releases/tag/0.8.1) as well as a [blog post](https://profanity-im.github.io/blog/post/release-080/). Continue reading about their [last message correction](https://profanity-im.github.io/blog/post/lmc/).

Gajim [Development News February 2020](https://gajim.org/post/2020-02-26-development-news-february/): Redesigned invites, color improvements and a new Flatpak Nightly

Gajim [Development News March 2020](https://gajim.org/post/2020-03-30-development-news-march/): New account creation wizard with server suggestions, support for WebSocket and many bugfixes!

Again, this month many changes and [improvements](https://monal.im/blog/mac-and-ips-improving-error-handling/) were implemented into [Monal 4.3](https://monal.im/blog/new-mac-and-ios-builds/) and [4.4](https://monal.im/blog/monal-4-4-for-ios-and-mac-are-out/). The app was refactored on Catalyst with [fixes](https://monal.im/blog/mac-catalyst-delayed-in-the-appstore-its-blocking-the-keychain/), removing of Google Talk, [comeback of the app in France](https://monal.im/blog/monal-4-3-is-coming-out-in-about-a-week-even-in-france/) again and UI changes to name the important blog posts and changes! Monal can now read [OMEMO 12-bytes IV](https://monal.im/blog/omemo-is-broken-in-general-across-the-ecosystem/) but from now limits it to [iOS 12 and 13](https://monal.im/blog/ios-4-3-beta-in-testing/).

[Pàdé 1.6.0](https://discourse.igniterealtime.org/t/pade-1-6-0-released/87226) was release by the Ignite Realtime community.

BeagleIM was released in version 3.7 and SiskinIM in version 5.7. [Improved bookmarks!](https://tigase.net/beagleim-3.7-and-siskin-5.7-released/)

### Libraries

Smack now supports Direct MUC Invitations, Stanza Content Encryption, Message Fastening and Message Retraction. Read Paul Schaub's (vanitasvitae) [blog post](https://blog.jabberhead.tk/2020/02/17/smack-some-more-busy-nights-and-12-bytes-of-iv/) which is also about the recent OMEMO's 12 bytes of IV changes. You want to implement a XEP to Smack? Start reading [here](https://blog.jabberhead.tk/2020/02/25/how-to-implement-a-xep-for-smack/)!

The switch from OMEMO IV 16 byte to 12 byte goes on for [Smack](https://github.com/igniterealtime/Smack/commit/1051cd2640616385f80997cad51bf7411e8e04cc) and [Python](https://github.com/Syndace/python-omemo/commit/45e56db33581c86c7e156115b7714bc32b6e154a).

[XMPP library for Go.](https://pkg.go.dev/mellium.im/xmpp?tab=doc)

### Other

As already previously mentioned: [Snikket](https://blog.prosody.im/introducing-snikket/)!

The title says everything: [A history of end-to-end encryption and the death of PGP](https://www.cryptologie.net/article/487/a-history-of-end-to-end-encryption-and-the-death-of-pgp/)
 
How to setup Conversations - [på svenska](https://hund.linuxkompis.se/2020/02/13/hur-du-kommer-igang-med-xmpp-pa-android.html)!

## Services

[JabberPL.org turns 15](https://twitter.com/jabberpl/status/1231030107273355265) - Congratulations! For their users they also [improved their service](https://twitter.com/jabberpl/status/1231032793968279553). 

## Extensions and specifications

### Updated

- Version 0.3.1 of [XEP-0343 (Signaling WebRTC datachannels in Jingle)](https://xmpp.org/extensions/xep-0343.html) has been released.
Abstract: This specification defines how to use the ICE-UDP Jingle transport
method to send media data using WebRTC DataChannels, so technically
uses DTLS/SCTP on top of the Interactive Connectivity Establishment
(ICE) methodology, which provides robust NAT traversal for media
traffic.

- Version 0.4.0 of [XEP-0384 (OMEMO Encryption)](https://xmpp.org/extensions/xep-0384.html) has been released.
Abstract: This specification defines a protocol for end-to-end encryption in
one-to-one chats, as well as group chats where each participant may
have multiple clients per account.

- Version 1.1.2 of [XEP-0167 (Jingle RTP Sessions)](https://xmpp.org/extensions/xep-0167.html) has been released.
Abstract: This specification defines a Jingle application type for negotiating
one or more sessions that use the Real-time Transport Protocol (RTP)
to exchange media such as voice or video. The application type
includes a straightforward mapping to Session Description Protocol
(SDP) for interworking with SIP media endpoints.

### Miscellaneous

**ProtoXEP**

The XMPP Extensions Editor has received the following proposals:

* [Simple JSON Messaging](https://xmpp.org/extensions/inbox/udt.html):
This specification proposes a simple mechanism by which applications
can transfer data safely, without needing additional protocol design
work. It is intended to provide a protocol that is trivial to
implement and can be driven with a simple API.

* [Extended Channel Search](https://xmpp.org/extensions/inbox/extended-channel-search.html):
This specification provides a standardised protocol to search for
public group chats. In contrast to XEP-0030 (Service Discovery), it
works across multiple domains and in contrast to XEP-0055 (Jabber
Search) it more clearly handles extensibility.

* [Trust Messages](https://xmpp.org/extensions/inbox/trust-messages.html):
This document specifies a way to communicate the trust in public long-
term keys used by end-to-end encryption protocols from one endpoint to
another.

* [MUC Presence Versioning](https://xmpp.org/extensions/inbox/muc-presence-versioning.html):
This specification defines a versioning mechanism which reduces the amount of
presence traffic in a XEP-0045 MUC.

**Experimental**

Version 0.1.0 of [XEP-0434 (Trust Messages)](https://xmpp.org/extensions/xep-0434.html) has been released.
Abstract: This document specifies a way to communicate the trust in public long-
term keys used by end-to-end encryption protocols from one endpoint to
another.
Changelog: Accepted by vote of Council on 2020-02-19. (XEP Editor (jsc))

**Active**

- Version 1.0.0 of [XEP-0345 (Form of Membership Applications)](https://xmpp.org/extensions/xep-0345.html) has been
released.
Abstract: This specification outlines the form and mandatory content of
membership applications.
Changelog: Voted to Active by Board on 2019-03-07. Sorry for the delay in the
editor queue. (XEP Editor (jsc))

**Draft**

- Version 1.0.0 of [XEP-0363 (HTTP File Upload)](https://xmpp.org/extensions/xep-0363.html) has been released.
Abstract: This specification defines a protocol to request permissions from
another entity to upload a file to a specific path on an HTTP server
and at the same time receive a URL from which that file can later be
downloaded again.
Changelog: Accepted as Draft standard by the XMPP Council. Voted on 2020-01-29.
(XEP Editor (jsc))

- Version 1.0.0 of [XEP-0363 (HTTP File Upload)](https://xmpp.org/extensions/xep-0363.html) has been released.
Abstract: This specification defines a protocol to request permissions from
another entity to upload a file to a specific path on an HTTP server
and at the same time receive a URL from which that file can later be
downloaded again.
Changelog: Accepted as Draft standard by the XMPP Council. Voted on 2020-01-29.
(XEP Editor (jsc))

**Call for Experience**

The XEP Editor would like to Call for Experience before
presenting it to the Council for advancing it to Final status.
During the Call for Experience, please answer the following questions each on:

- XEP-0066: [mail.jabber.org/pipermail/standards/2020-February/037071.html](https://mail.jabber.org/pipermail/standards/2020-February/037071.html)
- XEP-0368: [mail.jabber.org/pipermail/standards/2020-February/036992.html](https://mail.jabber.org/pipermail/standards/2020-February/036992.html)
- XEP-0198: [mail.jabber.org/pipermail/standards/2020-February/036986.html](https://mail.jabber.org/pipermail/standards/2020-February/036986.html)
- XEP-0184: [mail.jabber.org/pipermail/standards/2020-March/037107.html](https://mail.jabber.org/pipermail/standards/2020-March/037107.html)

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to Aleja, emus, Licaon_Kter, MDosch, Neustradamus, Nyco, pep, Sven, Vanitasvitae, Winfried, Wurstsalat  for their help in creating it!

Please share the news on "social networks":

* Twitter: [twitter.com/xmpp](https://twitter.com/xmpp)
* Mastodon: [fosstodon.org/@xmpp/](https://fosstodon.org/@xmpp/)
* LinkedIn: [www.linkedin.com/company/xmpp-standards-foundation/](https://www.linkedin.com/company/xmpp-standards-foundation/)
* Facebook: [www.facebook.com/jabber/](https://www.facebook.com/jabber/)
* Reddit: [www.reddit.com/r/xmpp/](https://www.reddit.com/r/xmpp/)

## License

This newsletter is published under CC by-sa license: [creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)
