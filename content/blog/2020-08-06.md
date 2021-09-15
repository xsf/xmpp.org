---
title: XMPP Newsletter - Monal update, eturnal and GSoC progress - 6 August 2020
date: 2020-08-06
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/08/newsletter-06-august/"
---

Welcome to the XMPP newsletter covering the month of July 2020.

### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news/jabberfr.org/category/newsletter/)


## XSF Announcements

JC Brand created an [XMPP job board](https://xmpp.work/)! This enables people to review job offers as 
well as advertise XMPP services. Please take a look, post your own offers and recommend it. XMPP works!

![XMPP job board](/images/newsletter/july2020/XMPP_jobs.png "XMPP job board") 

## Articles

Just how scalable is the XMPP server MongooseIM? See how Bartek Górny, one of the MongooseIM team members,
achieved almost 2.5 million connections, passing 45 thousand messages per second.
And, why he thinks 10 million connections is easily achievable. Find out more in
[Scaling a Mongoose](https://www.erlang-solutions.com/blog/scaling-a-mongoose-how-scalable-is-the-mongooseim-xmpp-server.html).

Pep., contributor to the [Poezio XMPP client](https://poez.io) and member of the XSF board, 
[wrote an article](https://bouah.net/2020/07/what-about-design/) detailing his thoughts on XMPP and on the importance of design.

Yarmo Mackenbach wrote [an article](https://yarmo.eu/post/keyoxide-xmpp-omemo) on XMPP and OMEMO integration in [Keyoxide](https://keyoxide.org/), a modern, secure and privacy-friendly platform to establish your decentralized online identity and perform basic cryptographic operations.

## Software news


### Clients and applications

The multi-platform desktop client [Gajim 1.2.1](https://gajim.org/post/2020-07-08-gajim-1.2.1-released/) has been released. Just two weeks after the release of Gajim 1.2, the next update is already there. Gajim 1.2.1 features spam reporting as specified by [XEP-0377](https://xmpp.org/extensions/xep-0377.html), automatic activation of shipped plugins which implies OMEMO available by default, and some bug fixes. Audio/Video calls gain some improvements, but remain highly experimental.
[More development news from July](https://gajim.org/post/2020-07-26-development-news-july/): an automatic update check for Gajim on Windows/MacOS, account password storage enhancements, an OMEMO fix, and many small improvements.

Profanity, the text based user interface client, released version 0.9.5 to fix a potential segmentation fault when using the `/theme properties` command. It is used to display colour settings for the current theme.

Anurodh Pokharel released [Monal 4.7 for iOS and macOS](https://github.com/anurodhp/Monal/releases/tag/Build_iOS_636). Despite the small version number update, this is a large upgrade. Besides the usual UI fixes and stability improvements you'll find: a new in chat title bar (as seen below), support for [XEP-0319](https://xmpp.org/extensions/xep-0319.html) (Last User Interaction in Presence) so you know when your contact was last seen online, support for [XEP-0085](https://xmpp.org/extensions/xep-0085.html) (Chat State Notifications) for those useful typing notifications and support for [XEP-0191](https://xmpp.org/extensions/xep-0191.html) (Blocking Command) for when a spammer comes along.

![Monal navigation bar](/images/newsletter/july2020/Monal_navigation.png "Monal navigation bar") 

The [git repository of Pix-Art Messenger](https://codeberg.org/kriztan/Pix-Art-Messenger/src/branch/master/CHANGELOG.md) has been moved from Github to Codeberg. This migration process is not finished yet. Until then, both repositories will run in parallel.
Concerning the software itself, Pix-Art Messenger versions 2.5.1 and 2.5.2 have been released, highlighting pinned chats in color, improving the video quality, and dynamically optimizing file compression.

Kontalk for Android has released a [new version (4.4.0)](https://github.com/kontalk/androidclient/releases)! Apart from bugfixes and improvements it has now a dark theme, supports sharing to groups, exporting media to storage and deleting media with messages. The settings have been revamped and Android 10 is now supported.

The Android client aTalk released several patches for their 2.3.0 release with [bugfixes and improvements](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt).

### Servers

[MongooseIM 3.7.1 has been released!](https://github.com/esl/MongooseIM/releases/tag/3.7.1)
This one is built on top of the 3.7.0 May release, which introduced support for channel binding to prevent [replay attacks](https://en.wikipedia.org/wiki/Replay_attack) for all methods of [SCRAM](https://en.wikipedia.org/wiki/Salted_Challenge_Response_Authentication_Mechanism "Salted Challenge Response Authentication Mechanism"), a family of modern, password-based challenge–response authentication mechanisms providing authentication of a user to a server. This previous version also provided a range of new SCRAM authentication methods based on different flavors of the [SHA](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms "Secure Hash Algorithms") cryptographic hash functions, the ability to retract messages as specified by [XEP-0424](https://xmpp.org/extensions/xep-0424.html), and support for [Proxy Protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) which safely transports connection information such as a client's address across multiple layers of NAT or TCP proxies. Version 3.7.1 improves on that by speeding up all the SCRAM methods significantly!

[Tigase XMPP Server 8.1.0 General Availability has been released](https://tigase.net/tigase-xmpp-server-8.1.0-ga/) and it is packed with improvements! 
`SASL-EXTERNAL` mechanism defined in [XEP-0178](https://xmpp.org/extensions/xep-0178.html) (Best Practices for Use of SASL EXTERNAL with Certificates) to allow  certificate based authenticated connections was added for server-to-server connections, greatly improving compliance with the XMPP federated network. Depending on support in other servers, it’s possible to use both SASL-EXTERNAL and Dialback, another authentication mechanism defined by [XEP-0220](https://xmpp.org/extensions/xep-0220.html). Set of XMPP extensions were added: 
 - [XEP-0398](https://xmpp.org/extensions/xep-0398.html) (User Avatar to vCard-Based Avatars Conversion)
 - [XEP-0156](https://xmpp.org/extensions/xep-0156.html) (Discovering Alternative XMPP Connection Methods)
 - [XEP-0410](https://xmpp.org/extensions/xep-0410.html) (MUC Self-Ping (Schrödinger’s Chat))
 - [XEP-0153](https://xmpp.org/extensions/xep-0153.html) (vCard-Based Avatars)
 - [XEP-0411](https://xmpp.org/extensions/xep-0411.html) (Bookmarks Conversion)
 - [XEP-0157](https://xmpp.org/extensions/xep-0157.html) (Contact Addresses for XMPP Services)

This version also improves management of multiple domains in virtual hosts and enables by default a new anti-spam plugin.

A new TURN server called [eturnal](https://eturnal.net) has been [published](https://www.process-one.net/blog/eturnal-v1-0-0-say-hello-to-a-new-stun-turn-server/). This is a standalone version of the TURN server part of [ejabberd](https://ejabberd.im/) (with some improvements) and a straightforward alternative to servers such as Coturn which can be used for offering STUN/TURN services to A/V clients using external service discovery as defined by [XEP-0215](https://xmpp.org/extensions/xep-0215.html).


## Libraries

[Tigase JaXMPP 3.3.0 has been released](https://tigase.net/tigase-client-library-v330-released/)!
Main features included in this release are support for OMEMO encryption, making it easier to carry out encrypted conversations, and support for [XEP-0305](https://xmpp.org/extensions/xep-0305.html) (XMPP Quickstart) allowing connections to be established faster. Apart from that, [SCRAM](https://en.wikipedia.org/wiki/Salted_Challenge_Response_Authentication_Mechanism "Salted Challenge Response Authentication Mechanism") support was extended with SCRAM-SHA512 flavour. Service items discovery can now be controlled with [XEP-0059](https://xmpp.org/extensions/xep-0059.html) (Result Set Management). DataForms with multiple items got implemented and MUC message delivery was improved. Last but not least, connectivity with Google's Firebase Cloud Messaging (FCM) was fixed.

Version 1.0.1 of [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp), the library developed for and used by Gajim development team, has been released. This version includes a fix for a bug where messages from ChatSecure could not be decrypted after a longer period of time has passed. It also includes some fixes for Websocket connections.

The Ignite Realtime community is pleased to announce the release of [jXMPP version 1.0.0](https://discourse.igniterealtime.org/t/jxmpp-and-minidns-1-0-0-released/88436)!
jXMPP is a library that provides common functionality required by all sorts of XMPP implementations (servers, clients, components, ...).
Among other things, it provides a sane implementation of JID types.
Check out its [javadoc](https://jxmpp.org/releases/1.0.0/javadoc/) documentation!

## Others

[whatsxmpp](https://git.theta.eu.org/eta/whatsxmpp), the WhatsApp (Web) to XMPP bridge, has seen a variety 
of bugfixes and improvements this month, mainly as a result of various users using the bridge and reporting
errors. The development team switched to using the Nix package manager to build Docker images, resulting in more 
reproducible and faster builds! A stable 0.1 release is getting closer, and the basic functionalities are 
already working and battle-tested. A few more stability improvements are still required and some features, such as proper 
MUC history support and file uploading via native WhatsApp servers, are missing! 
Please do pop by their MUC [whatsxmpp@conf.theta.eu.org](https://join.jabber.network/#whatsxmpp@conf.theta.eu.org?join) if you're interested 
in using or running the bridge.


## Google Summer of Code


Since the beginning of May students all over the world are working on many open-source projects within the Google Summer of Code Season 2020. We would like to introduce the students who work on [GSoC XMPP projects](https://summerofcode.withgoogle.com/organizations/5474262808264704/#6018598289539072) and share their blog posts:

[Aditya Borikar](https://adiaholic.github.io/gsoc2020/2020/05/16/Chapter-0-Introduction.html) is working on WebSocket support for Smack. Blog history:

- [Chapter 1: Handshake](https://adiaholic.github.io/gsoc2020/2020/05/24/Chapter-1-Handshake.html)
- [Chapter 2: Modular Shift](https://adiaholic.github.io/gsoc2020/2020/05/31/Chapter-2-Modular-Shift.html)
- [Chapter 3: SASL Negotiations](https://adiaholic.github.io/gsoc2020/2020/06/07/Chapter-3-sasl-negotiations.html)
- [Chapter 4: Fixing loose endpoints](https://adiaholic.github.io/gsoc2020/2020/06/14/Chapter-4-fix-loose-endpoints.html)
- [Chapter 5: Discrete Http Lookup Method](https://adiaholic.github.io/gsoc2020/2020/06/21/Chapter-5-Discrete-Http-Lookup-Method.html)
- [Chapter 6: A Part Of The Whole, Merged](https://adiaholic.github.io/gsoc2020/2020/06/28/Chapter-6-Part-Of-The-Whole.html)
- [Chapter 7: The Bigger Picture](https://adiaholic.github.io/gsoc2020/2020/07/06/Chapter-7-The-Bigger-Picture.html)
- [Chapter 8: Reworking FSM](https://adiaholic.github.io/gsoc2020/2020/07/12/Chapter-8-Reworking-FSM.html)
- [Chapter 9: Bug Fixation](https://adiaholic.github.io/gsoc2020/2020/07/19/Chapter-9-Fixing-Bugs.html)
- [Chapter 10: End of the second phase](https://adiaholic.github.io/gsoc2020/2020/07/26/Chapter-10-End-of-second-phase.html)

[Anmol (wolfie_anmol)](https://wolfieanmol.github.io/gsoc-blog/) is working on implementing Real Time Texting in Dino ([XEP-0301](https://xmpp.org/extensions/xep-0301.html)). Blog history:

- [GSoC 2020 begins - Introduction to RTT](https://wolfieanmol.github.io/gsoc-blog/introduction/)
- [RTT stanza and message comparision](https://wolfieanmol.github.io/gsoc-blog/rtt-stanza-and-message-comparision/)
- [Receiving Real Time Texts](https://wolfieanmol.github.io/gsoc-blog/receiving-rtt/)
- [User Interface](https://wolfieanmol.github.io/gsoc-blog/ui/)
- [Settings to Enable/Disable RTT](https://wolfieanmol.github.io/gsoc-blog/settings/)
- [Settings Radio Button Menu](https://wolfieanmol.github.io/gsoc-blog/settings-radio-button-menu/)
- [Realistic RTT with wait](https://wolfieanmol.github.io/gsoc-blog/realistic-rtt-with-wait/)

![Enable/Disable RTT in Dino](/images/newsletter/july2020/Dino_RTT_settings.png "Enable/Disable RTT in Dino") 

Thank you for joining GSoC XMPP projects and keep up the good work! To be continued.


## Extensions and specifications

### Updated

- Version 0.7.0 of [XEP-0313](https://xmpp.org/extensions/xep-0313.html) (Message Archive Management)

  TL;DR: add new filtering fields, allow for reversing results order and migrate some information to external documents.
  - Add 'before-id' and 'after-id' fields, flipped pages, single-item retrieval and a new mandatory disco feature
  - Split preferences protocol into a separate document
  - Split the details of pubsub archives into a separate document

- Version 1.0.0 of [XEP-0338](https://xmpp.org/extensions/xep-0338.html) (Jingle Grouping Framework)
  - Advance to Draft as per Council vote from 2020-07-01

- Version 0.3.0 of [XEP-0420](https://xmpp.org/extensions/xep-0420.html) (Stanza Content Encryption)

  TL;DR: some changes concerning elements allowed/denied to be encrypted, and security improvement by increasing the entropy of random padding elements.  
  - Allow origin-id elements, disallow stanza-id and extended stanza addressing elements inside the payload element
  - Clarify wording on stanza processed elements and improve XEP formatting
  - Remove limitation of random padding content to base64 characters alone
  - Chat messages MUST contain message processing store hint
  - Credit where credit is due
  

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to eta, emus, erszcz, Ge0rG, Holger, kriztan, jerome-poisson, jonas', Licaon_Kter, pmaziere, vanitasvitae, wurstsalat, woj-tek, zash for their help in creating it! 

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

## Subscribe to the newsletter

We suggest you [subscribe](https://tinyletter.com/xmpp) to receive the next editions in your inbox as soon as it is published! 
Promote this newsletter to whoever may be interested.

## Help us to build the newsletter

We are always happy to welcome contributors. Find our monthly drafts here in the [XSF Github repository](https://github.com/xsf/xmpp.org/pulls). 
Do not hesitate to join the discussion in our Comm-Team group chat(https://join.jabber.network/#commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. 

You have a project and write about it? Please consider sharing your news or events here, and promote it to a large audience! 
Even if you can only spend a few minutes, these would already be helpful!

Tasks which need to be done on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Translations: especially German and Spanish

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
