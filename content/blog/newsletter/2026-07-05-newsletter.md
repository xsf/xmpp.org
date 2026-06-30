---
title: The XMPP Newsletter June 2026
date: 2026-07-05
categories: ['Newsletter']
summary: "In this issue: Fully online 29th XMPP Summit announcement! Full XMPP Track at FOSSY 2026. XMPP Sprint in Berlin, XMPP and DI.DAY, XMPP at PravConf 2026. Read about Openfire, Fluux Messenger, Slidge v0.4.0beta, and Movim last releases! Introducing Tacky and ffetcher. Update your clients with aTalk, Conversations, Converse.js, Fluux Messenger, Gajim, Movim and Profanity. Update your servers: Openfire 5.1.0. Get ready to update your libraries and tools. And our Specifications update: three proposed XEPs, four new ones, and three updated!"
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of June 2026.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/).

Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors. If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XMPP Summit 29

The XMPP Standards Foundation (XSF) is excited to announce the [29th XMPP Summit](/2026/05/xmpp-summit-29/), the first XMPP Summit to take place [fully online](/2026/05/xmpp-summit-29/#the-online-xmpp-summit)! The XMPP Summit will be held from Friday 4th September to Saturday 5th September 2026, both days between 13:00 - 16:00 UTC. The XSF invites everyone interested in development of XMPP technologies to attend, and discuss all things XMPP remotely!

### XSF Membership

Being an elected member of the XMPP Standards Foundation signals a commitment to open standards and professional engagement in / with the XMPP community. Here, your membership helps position the XSF as a healthy organization, which in itself is valuable. It also grants voting rights on technical and administrative matters within the XSF. The application is a light-weight and free of cost process and you can use your membership to get more involved more easily, too. If you are interested in joining the XMPP Standards Foundation as a member, please apply to our **3rd quarterly** call for members admission [before August 16th, 2026 00:00UTC](https://wiki.xmpp.org/web/Membership_Applications_Q3_2026).

## XMPP Events

- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2026-06_Berlin) (DE / EN): during Friday June 19th to Sunday June 21st 2026, various developers had good discussions, tasty food, and did some programming! There was work on message edits in [Conversations](https://conversations.im/), [stateless file sharing](/extensions/xep-0447.html) in [Dino](https://dino.im/), fixes for the next release of [Kaidan](https://www.kaidan.im/), [OMEMO](/extensions/xep-0384.html)+[PubSub](/extensions/xep-0060.html) improvements in [Mellium](https://mellium.im/), a bigger update of [stanza content encryption](/extensions/xep-0420.html) and its [Slixmpp](https://codeberg.org/poezio/slixmpp/src/branch/master/README.rst) implementation, and some fixes on [Debian](https://www.debian.org/) packages. Many thanks to the  [@wikimediaDE](https://social.wikimedia.de/@wikimediaDE) for hosting us, again! Wonderful location, kind people!

- XMPP and DI.DAY: In the frame of the [DI.DAY](https://di.day), a collaborative list of **local**-oriented channels has been started. This list can be accessed as a map on [OpenStreetMap.de](https://umap.openstreetmap.de/de/map/offentliche-gruppenchats_139487) or as a list on [Codeberg](https://codeberg.org/manuu/fosdem-2026-xmpp-diday/wiki/Local-services). Feel free to complete it, or notify new rooms on the dedicated room (xmpp:[mapofchannels@chat.yax.im](xmpp:mapofchannels@chat.yax.im)?join), or via [Mastodon](https://social.anoxinon.de/@eversten/116634419387837338).

- XMPP at PravConf 2026: This year's edition of [PravConf](https://prav.app/conf/2026), a Free Software and XMPP themed conference, is being planned by the [Prav](https://prav.app) community from 4-5 July in Thiruvananthapuram, India. It will be followed by PravCamp on 6-7 July, a Sprint-inspired event where people sit together to work on Prav and other XMPP related things. Both events are held on college campuses and college students will get the chance to learn about XMPP too. Read more about it [on the website](https://prav.app/conf/2026).

- XMPP at FOSSY 2026: [FOSSY](https://2026.fossy.ca/), the fourth _Free and Open Source Software Yearly_ conference, has published the complete list of presentation on the XMPP Track, which will be as follows:
  - On Saturday, August 08, in MCLD 3038:
    - [Encrypted messaging interoperability with hybrid bridges in XMPP](https://2026.fossy.ca/schedule/presentation/374/), by [Marvin W.](https://2026.fossy.ca/speaker/profile/609/) from 2:00 PM to 2:45 PM PDT.
    - [Beyond Chat: Delivering mini "apps" with great UI](https://2026.fossy.ca/schedule/presentation/369/), by [Stephen Paul Weber](https://2026.fossy.ca/speaker/profile/543/) from 3:00 PM to 3:45 PM PDT.
    - ["Beautiful XMPP Testing" revisited -- How to Overcome the Mind-Body Duality by Staring at XML](https://2026.fossy.ca/schedule/presentation/371/), by [Phillip Davis](https://2026.fossy.ca/speaker/profile/552/) from 4:30 PM to 5:15 PM PDT.
  - On Sunday, August 09, in MCLD 3038:
    - [When Data Gets Heavy: Voice and Video for Large Groups](https://2026.fossy.ca/schedule/presentation/370/), by [Christopher Vollick](https://2026.fossy.ca/speaker/profile/625/) from 10:45 AM to 11:30 AM PDT.
    - [UnifiedPush - Push notifications. Decentralized and Open Source](https://2026.fossy.ca/schedule/presentation/372/), by [Daniel Gultsch](https://2026.fossy.ca/speaker/profile/544/) from 11:45 AM to 12:30 PM PDT.
    - [Adventures in Onboarding: Episode V - The Server Goes Down](https://2026.fossy.ca/schedule/presentation/375/), by [Gideon Mayhak](https://2026.fossy.ca/speaker/profile/610/) from 2:00 PM to 2:45 PM PDT.
    - [Snikket: Behind the scenes of our on-demand XMPP server hosting](https://2026.fossy.ca/schedule/presentation/373/), by [Matthew Wild](https://2026.fossy.ca/speaker/profile/579/) from 3:00 PM to 3:45 PM PDT.

## XMPP Articles

- [Openfire 5.1.0 Release!](https://discourse.igniterealtime.org/t/openfire-5-1-0-release/96495), by [guus](https://discourse.igniterealtime.org/u/guus/summary) for the [Ignite Realtime community](https://discourse.igniterealtime.org/).
- [Fluux Messenger 0.16.0: End-to-End Encryption](https://www.process-one.net/blog/fluux-messenger-0-16-0-end-to-end-encryption/), by [Mickaël Rémond](https://www.process-one.net/author/mremond/) for the [ProcessOne Blog](https://www.process-one.net/blog/).
- [Fluux Messenger 0.16.1: fixes and refinements from real-world use](https://www.process-one.net/blog/fluux-messenger-0-16-1-fixes-and-refinements-from-real-world-use/), by [Mickaël Rémond](https://www.process-one.net/author/mremond/) for the [ProcessOne Blog](https://www.process-one.net/blog/).
- [18 meses depois](https://blog.isacloud.im/18-meses-depois/), by [isadora](https://blog.isacloud.im/author/isadora/) for the [isaCloud diario-de-bordo](https://blog.isacloud.im/category/diario-de-bordo/). [PT_BR]
- [Slidge v0.4.0beta "Spaces"](https://slidge.im/blog/2026/06/14/slidge-v0.4.0beta-spaces/), from the [slidge.im blog](https://slidge.im/blog/).
- [Movim 0.34 "Meier" is here! ](https://mov.im/community/pubsub.movim.eu/Movim/30cf568b-49f9-4a59-8168-6f8f1f12164c), by Timothée Jaussoin for the [Movim Blog](https://mov.im/community/pubsub.movim.eu/Movim).
- [Movim 0.31.4 is out, stay safe and upgrade! ](https://mov.im/community/pubsub.movim.eu/Movim/movim-0-31-4-is-out-stay-safe-and-upgrade-cwblXR), by Timothée Jaussoin for the [Movim Blog](https://mov.im/community/pubsub.movim.eu/Movim).
- [Introducing Tacky](https://github.com/pounceandmiss/tacky/blob/main/README.md), a desktop XMPP chat client built with Tcl/Tk for Linux and Windows with support for modern A/V calls and OMEMO e2ee. Still in pre-alpha state.
- [Introducing ffetcher](https://code.woodpeckersnest.space/roughnecks/ffetcher#readme), an XMPP bot that monitors RSS and Atom feeds and posts new articles to one or more MUC rooms. It specializes on fediverse feeds. The code was AI generated and reviewed/tested by the author.

## XMPP Software News

### XMPP Clients and Applications

- [aTalk](https://github.com/cmeng-git/atalk-android/blob/master/README.md) has released versions [6.1.0](https://github.com/cmeng-git/atalk-android/releases/tag/6.1.0), [6.2.0](https://github.com/cmeng-git/atalk-android/releases/tag/6.2.0) and [6.3.0](https://github.com/cmeng-git/atalk-android/releases/tag/6.3.0) of its encrypted instant messaging with video call and GPS features for Android. These versions introduce [message retraction](/extensions/xep-0424.html), remove merging of multiple messages in chat window, extend [last message correction](/extensions/xep-0308.html) support to all other outgoing messages and not just the last sent message, support language translation for sent/received messages in chat/multi-user chat sessions with translation option that can be enabled/disabled per contact chat/multi-user chat session, and also bring improvements, quite a few fixes and lot of 'under the hood' changes. Please refer to the [release notes](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt) for all the details.
- [Conversations](https://conversations.im/) has released version [2.20.1](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.20.1) for Android. This releases adds _Note to self_ as search suggestion and brings in minor bug fixes. Make sure to take a look at the [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) for all the details!
- [Converse.js](https://conversejs.org) has released version [14.0.0](https://github.com/conversejs/converse.js/releases/tag/v14.0.0) of its open-source web-based XMPP chat client. This release adds support for **OMEMO:2 encryption**! It also adds new [pubsub](/extensions/xep-0060.html) API methods to create, subscribe and unsubscribe, [software version](/extensions/xep-0092.html) support and show the server's software version in the profile modal, support for OMEMO 2 (`urn:xmpp:omemo:2`) using [stanza content encryption](/extensions/xep-0420.html), detect omemo:2-only contacts as OMEMO-capable, with a whole lot of fixes and work under the hood!. All this also brings some backwards incompatible changes, so please go straight to the [changelog](https://github.com/conversejs/converse.js/blob/master/CHANGES.md) for all the details!
- [Fluux Messenger](https://github.com/processone/fluux-messenger/blob/main/README.md), has released versions [0.16.0](https://github.com/processone/fluux-messenger/releases/tag/v0.16.0), [0.16.1](https://github.com/processone/fluux-messenger/releases/tag/v0.16.1) and [0.16.2](https://github.com/processone/fluux-messenger/releases/tag/v0.16.2) , of its modern, cross-platform XMPP client for communities and organizations. These versions add [OpenPGP end-to-end encryption](/extensions/xep-0373.html)  — [encrypted 1:1 messaging](/extensions/xep-0374.html) with passphrase-protected key storage and secret-key backup/restore, OpenPGP e2ee support in web version, Multi-TSK (Transferable Secret Key) handling in the backup restore flow for accounts with multiple OpenPGP keys, unread message count badge on avatar, compose messages offline and send on reconnect, support for room private messages ("[whisper](/extensions/xep-0045.html#privatemessage)"), and a whole lot more along with a ton of changes and fixes. Please, go straight to the [fulll changelog](https://github.com/processone/fluux-messenger/blob/main/CHANGELOG.md) for all the details!

{{< figure src="/images/newsletter/2026-07-05/fluux-whisper-dark.png" caption="Fluux Messenger: Private [whisper](/extensions/xep-0045.html#privatemessage) messages to a single room occupant" >}}

- [Gajim](https://gajim.org/) has released version [2.4.7](https://gajim.org/posts/2026-06-18-gajim-2.4.7-released/) of its free and fully featured chat app for XMPP. This release brings support for modern [OpenPGP encryption](/extensions/xep-0374.html), message drafts are now persistent, which means after restarting Gajim, you can continue where you left off, group chats are now named after participants if no other name is available, disabling account while connecting has been fixed, and it also comes with many small improvements and bugfixes. Thank you for all your contributions!

{{< figure src="/images/newsletter/2026-05-05/gajim_mentions.png" caption="Gajim: A message mentioning you" >}}

- [Movim](https://movim.eu/) has released versions [0.34](https://mov.im/community/pubsub.movim.eu/Movim/30cf568b-49f9-4a59-8168-6f8f1f12164c), code named ["Meier"](https://www.rasc.ca/comet-meier-1978f) and [0.34.1](https://mov.im/community/pubsub.movim.eu/Movim/movim-0-31-4-is-out-stay-safe-and-upgrade-cwblXR)! These new Movim milestones stabilize the important work done in the [previous release](https://mov.im/community/pubsub.movim.eu/Movim/a1f5a954-e80c-45bd-911b-62e1bf98f8da) while introducing a completely redesigned conference-call experience. In this version, you can add dedicated conference-call rooms to your Spaces and explore the new video-call interface. Conference calls, rebuilt from the ground up, media renegotiation, new layouts and redesigned interface, new notification sounds, session management, other fixes and more!

{{< figure src="/images/newsletter/2026-07-05/movim-ccis.png" caption="Movim: Conference-Call Rooms in Spaces!" >}}

- [Profanity](https://profanity-im.github.io/) has released version [0.18.2](https://github.com/profanity-im/profanity/releases/tag/0.18.2) of its console based XMPP client. This release brings bug fixes to guard terminal writes while suspended, prevents OTR handshake from leaking presence to strangers, and silence 'no key' error for key transport messages. Please make sure to read the [changelog](https://github.com/profanity-im/profanity/blob/master/CHANGELOG) for all the details!

### XMPP Servers

- The [Ignite Realtime community](https://www.igniterealtime.org/) is pleased to announce the release of [Openfire 5.1.0](https://discourse.igniterealtime.org/t/openfire-5-1-0-release/96495). The highlights of this release include: [SASL channel binding](/extensions/xep-0440.html) (with generous support from the [NLnet Foundation](https://nlnet.nl/), a round of crypto hardening, an O(n²) bug that was causing 2-hour startup times on large deployments (now seconds), Java 25, and new first-class support for [MariaDB](https://mariadb.com/), [Firebird](https://firebirdsql.org/) and [CockroachDB](https://www.cockroachlabs.com/product/overview/). Make sure to read the [full changelog](https://download.igniterealtime.org/openfire/docs/latest/changelog.html) for all the details!

### XMPP Libraries & Tools

- [go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/README.md?ref_type=heads), a tool to send messages to an XMPP contact or MUC inspired by [sendxmpp](https://sendxmpp.hostname.sk/), version [0.16.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.16.0) has been released. Full details on the [changelog](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/CHANGELOG.md).
- [go-xmpp](https://github.com/xmppo/go-xmpp/blob/master/README.md) versions [0.3.5](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.5) and [0.3.6](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.6) have been released.
- [jabber.el](https://codeberg.org/emacs-jabber/emacs-jabber/src/branch/master/README.org), the XMPP client for [Emacs](https://www.gnu.org/software/emacs/), versions [0.11.0](https://codeberg.org/emacs-jabber/emacs-jabber/releases/tag/0.11.0) and [0.11.1](https://codeberg.org/emacs-jabber/emacs-jabber/releases/tag/0.11.1) have been released. Full details on the [changelog](https://codeberg.org/emacs-jabber/emacs-jabber/src/branch/master/CHANGELOG.org).
- [libomemo.js](https://github.com/conversejs/libomemo.js/blob/master/README.md), a [TypeScript](https://www.typescriptlang.org/) implementation of the [OMEMO Multi-End Message and Object Encryption](/extensions/attic/xep-0384-0.3.0.html) protocol for XMPP, versions [1.0.0](https://github.com/conversejs/libomemo.js/releases/tag/v1.0.0), [2.0.0](https://github.com/conversejs/libomemo.js/releases/tag/v2.0.0), [2.0.1](https://github.com/conversejs/libomemo.js/releases/tag/v2.0.1) and [2.0.2](https://github.com/conversejs/libomemo.js/releases/tag/v2.0.2) have been released. The list of changes is larger and has more details and notices on **breaking** changes that what could ever mention in here. Please refer to the full [changelog](https://github.com/conversejs/libomemo.js/blob/master/CHANGELOG.md) for all the details!
- [peertube-plugin-livechat](https://github.com/JohnXLivingston/peertube-plugin-livechat/blob/main/README.md), a plugin meant to provide a chat system for [Peertube](https://joinpeertube.org/) videos, versions [14.0.3](https://github.com/JohnXLivingston/peertube-plugin-livechat/releases/tag/v14.0.3) and [14.0.4](https://github.com/JohnXLivingston/peertube-plugin-livechat/releases/tag/v14.0.4) have been released. You can read all the details in the [changelog](https://github.com/JohnXLivingston/peertube-plugin-livechat/blob/main/CHANGELOG.md)!
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md), the cross-platform C++ XMPP client and server library, versions [1.16.0](https://invent.kde.org/libraries/qxmpp/-/tags/v1.16.0) and [1.16.1](https://invent.kde.org/libraries/qxmpp/-/tags/v1.16.1) have been released. Full details on the [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md).
- [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp/src/branch/main/README.md), the [WhatsApp](https://www.whatsapp.com/) to XMPP gateway based on [Slidge](https://slidge.im/) and [whatsmeow](https://github.com/tulir/whatsmeow/blob/main/README.md), version [0.3.11](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.11) has been released. You can read the intermediate changelog from [ 0.3.11beta1 to 0.3.11](https://codeberg.org/slidge/slidge-whatsapp/compare/v0.3.11beta1...v0.3.11) for all the details.
- [slixmpp](https://codeberg.org/poezio/slixmpp/src/branch/master/README.rst), the MIT licensed XMPP library for Python 3.7+ version [1.16.0](https://codeberg.org/poezio/slixmpp/releases/tag/slix-1.16.0) has been released. This release brings two new XEPs into the fold, and has quite a few internal changes as well. You can read the official [release announcement](https://blog.mathieui.net/en/slixmpp-1-16.html) for all the details. **Breaking**: The `get_certs` method on [XEP-0257](/extensions/xep-0257.html) is now an async function, which breaks compatibility with previous usages.
- [strophejs](https://github.com/strophe/strophejs/blob/master/README.md), a JavaScript library for speaking XMPP via BOSH ([XEP-0124](/extensions/xep-0124.html) and [XEP-0206](/extensions/xep-0206.html)) and [WebSockets](/rfcs/#7395), version [4.0.0](https://github.com/strophe/strophejs/releases/tag/v4.0.0) has been released. You can read the full [changelog](https://github.com/strophe/strophejs/blob/master/CHANGELOG.md) for all the details.
- [xmpp-dns](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/README.md), a CLI tool to check XMPP SRV records, version [0.6.3](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.6.3) has been released. Full details on the [changelog](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/CHANGELOG.md).
- [xmpp-rs](https://gitlab.com/xmpp-rs/xmpp-rs/-/blob/main/README.md), has released:
  - [minidom-0.19.0](https://gitlab.com/xmpp-rs/xmpp-rs/-/tags/minidom-0.19.0), a DOM library quite specific for XMPP.
  - [sasl-0.5.3 ](https://gitlab.com/xmpp-rs/xmpp-rs/-/tags/sasl-0.5.3), handles the SASL protocol.
- [xmpppy](https://github.com/xmpppy/xmpppy/blob/0.7.2/README.rst), a Python library that is targeted to provide easy scripting with Jabber, version [0.7.4](https://github.com/xmpppy/xmpppy/releases/tag/0.7.4) has been released. Full details on the [changelog](https://github.com/xmpppy/xmpppy/blob/master/CHANGES.rst).

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- [Jingle User Location](/extensions/inbox/jingle-geoloc.html)
  - This specification defines a Jingle application extension for negotiating and updating user location inside an active Jingle session using the [XEP-0080](/extensions/xep-0080.html) User Location payload.
- [XMPP Decentralized ID (XID)](/extensions/inbox/xid.html)
  - XMPP Decentralized ID (XID) is a DNS independent XMPP entity identifier. This specification describes how to generate, use, and handle them.
- [Jingle Synchronized Real-Time Text](/extensions/inbox/jingle-rtt-sync.html)
  - This specification defines a Jingle application extension for negotiating real-time text as part of the same conversational session as audio and video.

### New

- Version 0.1.0 of [XEP-0514](/extensions/xep-0514.html) (Emoji Markup)
  - Accepted as Experimental by council vote on 2026-05-12 (XEP Editor(dg))
- Version 0.1.0 of [XEP-0515](/extensions/xep-0515.html) (TLS Channel-Binding Downgrade Protection)
  - Accepted as Experimental by council vote (XEP Editor (dg))
- Version 0.1.0 of [XEP-0516](/extensions/xep-0516.html) (XMPP Decentralized ID (XID))
  - Accepted as Experimental by council vote (XEP Editor (dg))
- Version 0.1.0 of [XEP-0517](/extensions/xep-0517.html) (Jingle Synchronized Real-Time Text)
  - Accepted as Experimental by council vote (XEP Editor (dg))
  
### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.35.5 of [XEP-0045](/extensions/xep-0045.html) (Multi-User Chat)
  - Fix `from` attribute in examples where the room itself sends a message.
  - Fix associated pubsub node field name in disco info example. (nc)
- Version 0.5.0 of [XEP-0420](/extensions/xep-0420.html) (Stanza Content Encryption)
  - The time affix uses the `DateTime` profile of [XEP-0082](/extensions/xep-0082.html)
  - Longer rpads MUST NOT be rejected
  - Add a minimum size target for random padding to add resistance against potential correlation attacks in case of short content and 0-length rpad
  - Removed unhelpful Implementation
  - Note warning about injection of decrypted stanzas
  - Clarify fallback body policy
  - Fix descriptions to apply to all stanzas instead of just messages
  - Remove questionable SHOULD in the time affix handling and clarify the affix'es verification
  - Request the registrar to provide a list of exclusively server-processed elements
  - List XEP dependencies
  - Add XML schema (syndace)
- Version 0.1.1 of [XEP-0514](/extensions/xep-0514.html) (Emoji Markup)
  - Remove outdated reference to BoB (techmetx11)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- No stable XEPs this month.

### Deprecated

- No XEPs deprecated this month.

### Rejected

- No XEPs rejected this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp.org)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers and more languages are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- Contributors:
  - To [this issue](/categories/newsletter/): *emus, cal0pteryx, Gonzalo Raúl Nemmi, Ludovic Bocquet, anubis, Badri (badrihippo), XSF iTeam*

- Translations:
  - [French](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
  - [Italian](/categories/newsletter/): *Mario Sabatino, Roberto Resoli*
  
## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). At the end of each month, the pad's content is merged into the [XSF GitHub repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [XSF Communications Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations
- communication via media accounts

## Unsubscribe from the XMPP Newsletter

For this newsletter either [log in here](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/) and unsubscribe or simply send an email to newsletter-leave@xmpp.org.
(If you have not previously logged in, you may need to set up an account with the appropriate email address.)

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
