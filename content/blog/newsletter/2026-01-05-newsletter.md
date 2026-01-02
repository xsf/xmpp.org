---
title: The XMPP Newsletter December 2025
date: 2026-01-05
categories: ['Newsletter']
summary: "In this issue: Pack your bags and get ready for the XMPP Summit 28, take part on any or all of the 3 XMPP events on Fosdem 26 and the other 2 on the RHL26. Learn about Monal IM internals. Last JMP newsletter of the year. Update your clients with Cheogram, Conversations, Gajim, Kaidan, Monal, Monocles and Quicksy! Update your servers: MoongooseIM 6.0.5, Openfire 5.0.3. and Snikket Server - December 2025. XEP’s news - a proposed XEP, two updated, two new ones, a stable XEP and a last call!"
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of December 2025.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/).

Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors. If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XMPP Summit 28 & FOSDEM 2026

The XSF is planning the [XMPP Summit 28](/2025/11/xmpp-summit-28/), which will take place during Thursday 29th & Friday 30th, January 2026, in Brussels (Belgium, Europe). Following the Summit, the XSF is also planning to be present at [FOSDEM 2026](https://fosdem.org/2026/), which will take place during Saturday, January 31st & Sunday, February 1st, 2026. Find all the details in our [Wiki](https://wiki.xmpp.org/web/Conferences/Summit_28). Please sign-up now if you are planning to attend, since this helps organizing. The event is of course open for everyone interested to participate. Spread the word within your circles!

### XSF Membership

If you are interested in joining the XMPP Standards Foundation as a member, [please apply before February 15th, 2026, 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q1_2026).

### XMPP logo and Font Awesome

The XSF is proud to announce that the official XMPP logo has been [accepted](https://github.com/FortAwesome/Font-Awesome/discussions/21069#discussioncomment-15220358) into [Font Awesome](https://fontawesome.com/start) and will be bundled up in their source tarball starting from their next release!

## XMPP Events

- [XMPP at FOSDEM26](/2025/11/xmpp-at-fosdem-2026/): These are the XMPP related talks that will take place on the [Decentralised Communication](https://fosdem.org/2026/schedule/track/decentralised-communication/) track. This talks will take place in room [AW1.126](https://fosdem.org/2026/schedule/room/aw1126/) on Sunday, January 31st, 2026. You can also [join the conversation](https://chat.fosdem.org/#/room/#2026-decentralised-communication:fosdem.org) or watch the live videos at [aw1126](https://live.fosdem.org/watch/aw1126).
  - [Engineering XMPP Federation: Building Messaging, Voice & Social Features Across Independent Projects](https://fosdem.org/2026/schedule/event/7XJL9E-engineering_xmpp_federation_building_messaging_voice_social_features_across_inde/): The [XSF](https://xmpp.org) is a standards body that sits at the core of a development ecosystem of independent implementations by different individuals and organizations that actually work together, all highly interoperable, shipping new features at a high pace. This talk, by [Jérôme Sautret](https://fosdem.org/2026/schedule/speaker/jerome_sautret/) will share how things work at this scale and will be co-presented by a server and client developer, showing how they work together to fine-tune their implementations. This talk starts at 13:15 and ends at 13:45 hs.
  - [Movim: Building a Decentralized Social Network on XMPP](https://fosdem.org/2026/schedule/event/EVSXLA-movim-building-decentralized-social-network-xmpp/): In this talk, [Timothée Jaussoin](https://fosdem.org/2026/schedule/speaker/timothee_jaussoin/) will present how [Movim](https://movim.eu/) leverages the XMPP standard and its extensions to deliver features users expect from modern social platforms (communities, IM, group chats, video calls, blogging and a complete publishing platform into a unified experience), without giving up your data to a centralized platform, while remaining fully federated, interoperable with other XMPP clients like [Conversations](https://conversations.im/) and [Dino](https://dino.im/), and capable of bridging to centralized platforms like Discord, Telegram, and WhatsApp!. This talk starts at 13:45 and ends at 14:15 hs.
  - [What are you listening to now?: Implementing "Now Playing" feature in modern XMPP](https://fosdem.org/2026/schedule/event/8EDWJT-now-playing-revisited/): In this talk, [Özcan Oğuz](https://fosdem.org/2026/schedule/speaker/ozcan_oguz/) will share the journey on his research on implementing this feature in modern XMPP clients, the protocols of certain operating systems to read the currently playing media, the current status of the support of [XEP-0118](/extensions/xep-0118.html) (User Tune) and the PoC of a modern "Now Playing" feature. This talk starts at 14:15 and ends at 14:45 hs.
- [XMPP at RHL26](https://rencontreshivernalesdulibre.ch/): this french-speaking event for software freedom will take place during January 23-27 in Switzerland and will welcome two conferences about XMPP. [Codimp](https://social.lithio.fr/users/codimp/) will host the ['XMPP ou comment ne pas réinventer la roue : messagerie fédérée et sécurisée en 2026'](https://rencontreshivernalesdulibre.ch/timetable/event/xmpp-ou-comment-ne-pas-reinventer-la-roue-messagerie-federee-et-securisee-en-2026/) presentation about the [improvements to the protocol, servers and clients in last five years](https://social.lithio.fr/notice/B1BfCk6RE0mEj9EMds/), while [neox](https://forge.a-lec.org/neox/) will host the ['L'hébergement éthique comme Commun'](https://rencontreshivernalesdulibre.ch/timetable/event/lhebergement-ethique-comme-commun/) presentation about how the [Libre en Communs non-profit](https://toot.a-lec.org/@a_lec) built its own infrastructure as a [common](https://en.wikipedia.org/wiki/Commons) around fully free software and compatible hardware in order to hosts projects and in particular a public XMPP service, being the communication core to manage this together.
- [XMPP at 39C3 CCC](/2025/12/xmpp-at-chaos-communication-congress-39c3/): the [Critical Decentralisation Cluster (CDC)](https://decentral.community/39C3/) returned to the [39th Chaos Communication Congress](https://events.ccc.de/congress/2025/infos/startpage.html) in Hamburg (Germany) during this last December 27-30 2025. The CDC provided a friendly space for discussions and exchanges on technology and politics with other communities working towards decentralization. The XMPP assembly was part of it thanks to [neox](https://forge.a-lec.org/neox) and [mathieui](https://blog.mathieui.net/en/pages/about.html) active involvement, with the latter being responsible for the sparkly XMPP stickers!!

{{< figure src="/images/newsletter/2026-01-05/stickers_39C3.jpg" caption="Left: the **highly coveted** XMPP sparkly stickers! Right: XMPP assembly at the 39C3 Critical Decentralisation Cluster!" >}}

## Videos and Talks

- [Devuan 6 Excalibur instalamos el cliente xmpp Gajim](https://fediverse.tv/w/gibf1uo3PtNEG2pCNSk1Re) by [gnuxero](@gnuxero@fediverse.tv). [ES]

## XMPP Articles

- [Explorando XMPP e Ejabberd: Um Estudo Profundo](https://blog.dmarkinfo.com.br/post/explorando-xmpp-e-ejabberd-um-estudo-profundo) by [Eduardo Marques](https://www.dmarkinfo.com.br/novosite/) for [DMarkInfo Blog](https://blog.dmarkinfo.com.br/). [PT_BR]
- [Monal Internals - Serializable Promise framework](https://monal-im.org/post/00015-monal-internals-promise-framework/) by Matthew Fennell for the [Monal IM Blog](https://monal-im.org/post/).
- [Movim](https://movim.eu/): Some of you might have experienced [difficulties to open Movim as a Progressive Web App on your Android device](https://mov.im/community/pubsub.movim.eu/Movim/some-of-you-might-have-experienced-difficulties-to-open-movim-as-a-progressive-l3bnom). There is a know issue on Chrome related to that. A workaround has been pushed to master, please clear your application cache to deploy it!
- [Reflecting on 2025: A Year of Growth, Collaboration & Community](https://discourse.igniterealtime.org/t/reflecting-on-2025-a-year-of-growth-collaboration-community/96280) by [guus](https://discourse.igniterealtime.org/u/guus/summary) for the [Ignite Realtime Community](https://discourse.igniterealtime.org/).
- [JMP newsletter - More Cheogram Apps](https://blog.jmp.chat/b/december-newsletter-2025): this latest edition of your pseudo-monthly [JMP](https://jmp.chat/) update brings you news about port-out PIN self-service, data-only registration, a collection of selected recent [Cheogram](https://cheogram.com/) Android changes, a word of advise about some changes to the official distribution mechanism for Cheogram apps and all you need to know about the highly anticipated [Borogove](https://snikket.org//blog/borogove-the-new-snikket-sdk/) based **Cheogram WWW** and **Cheogram iOS** clients!
- The XMPP newsgroup on Usenet: The NNTP protocol is still in use, and there is an active Usenet group about the XMPP/Jabber topic at `alt.chat-programs.jabber`. [NNTP](https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol) is a standard application-level protocol that enables the exchange of messages in distributed systems such as [Usenet](https://en.wikipedia.org/wiki/Usenet) — a protocol worth revisiting. Some free public servers are available; one of them is [Ethernal September](https://www.eternal-september.org), which has open free registration. You may use [Thunderbird](https://www.thunderbird.net/en-US/thunderbird/all/), [PAN](https://gitlab.gnome.org/GNOME/pan/-/blob/master/README.org?ref_type=heads) or [TIN](http://www.tin.org/) as a client.

## XMPP Software News

### XMPP Clients and Applications

- [Cheogram](https://cheogram.com/) has released version [2.19.0-4](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.19.0-4) for Android. A bugfix release that introduces fixes to tablet view, account filters for starting new chat, some crashing bugs, WASM in WebXDC, show an extra piece of context on call status/failure, align message text size with upcoming [Snikket](https://snikket.org/) release, among many others! Make sure to check out the [list of changes](https://git.sr.ht/~singpolyma/cheogram-android/refs) for all the details across releases.
- [Conversations](https://conversations.im/) has released versions [2.19.6](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.6) and [2.19.7](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.7) for Android. This version introduces a setting to always use relays, sends delivery receipts by default and turn setting into "Read receipts" and fixes avatar caching issue and DNS occasionally not resolving when Private DNS is enabled. You can take a look at the [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) for all the details.
- [Gajim](https://gajim.org/) has released version [2.4.1](https://gajim.org/posts/2025-12-13-gajim-2.4.1-released/) of its free and fully featured chat app for XMPP. This release brings previews for GIFs and similar animation file formats, and many smaller changes and bug fixes. Thank you for all your contributions! You can take a look at the [changelog](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) for all the details.

{{< figure src="/images/newsletter/2026-01-05/animated-previews.png" caption="Animated previews in Gajim." >}}

- [Kaidan](https://www.kaidan.im/) has released version [0.14.0](https://www.kaidan.im/2026/01/01/kaidan-0.14.0/) and it includes some great new features and fixes! Advanced media sharing, filtering XMPP providers for account creation, highlighted messages, XMPP URIs, and many other new features and bugfixes! You can find a detailed list of new features, bugfixes and notes in the [changelog](https://invent.kde.org/network/kaidan/-/blob/master/NEWS.md).
- [Monal](https://monal-im.org/) has released versions [6.4.15](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1067) and [6.4.16](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1069) for iOS and macOS.
- [Monocles](https://monocles.eu/more) has released version [2.0.18](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.18) of its chat client for Android. And it comes loaded! It introduces a VCard4 profile editor, a VCard QR code generator to account editor, a drag and drop account reordering, improves input field text color visibility, an option to save media to downloads folder in media viewer, introduces chat history calendar, updates TLSv1.3 setting (Default on), adds wasm extension and application/wasm MIME and more!. Make sure to take a look at the [changelog](https://codeberg.org/monocles/monocles_chat/src/branch/master/fastlane/metadata/android/en-US/changelogs/19504.txt) for all the details!
- [Quicksy](https://quicksy.im/) has released versions [1.17.0](https://github.com/monal-im/Monal/releases/tag/Quicksy_Build_iOS_20) and [1.21.0](https://github.com/monal-im/Monal/releases/tag/Quicksy_Build_iOS_21) for iOS.
- Initial development of [MankalaNextGen](https://invent.kde.org/srisharanvs/mankalanextgen), a graphical user interface to play [Mancala](https://en.wikipedia.org/wiki/Mancala) games was done during Google Summer of Code 2025 by [Srisharan VS](https://srisharanvs.github.io/). The application uses [QXMPP](https://invent.kde.org/libraries/qxmpp) to enable remote play.

### XMPP Servers

- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) has released version [6.5.0](https://github.com/esl/MongooseIM/releases/tag/6.5.0) of its Enterprise Instant Messaging Solution. This release brings new features, changes, various fixes and improvements. For more information, make sure to check out the [changelog](https://github.com/esl/MongooseIM/blob/6.5.0/CHANGELOG.md) and the [documentation](https://esl.github.io/MongooseDocs/6.5.0/).
- The [Ignite Realtime community](https://www.igniterealtime.org/) is happy to announce the release of [Openfire 5.0.3](https://discourse.igniterealtime.org/t/openfire-5-0-3-release/96265)! This release brings a number of stability improvements and bug fixes. Notably, a number of improvements were made to Multi-User Chatroom (MUC). Please refer to the [full changelog](https://download.igniterealtime.org/openfire/docs/latest/changelog.html) for more details.
- [Snikket Server - December 2025 release](https://snikket.org/blog/snikket-server-dec-2025/): Snikket is rounding off the year with another small release of its server software. The main purpose of this release is to fix a couple of small bugs which were discovered and reported after the previous release was announced. Some notable changes include offline message compatibility and web portal debug information.

### XMPP Libraries & Tools

- [go-xmpp](https://github.com/xmppo/go-xmpp/blob/master/README.md) versions [0.3.0](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.0), [0.3.1](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.1) and [0.3.2](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.2) have been released.
- [go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/README.md?ref_type=heads), a tool to send messages to an XMPP contact or MUC inspired by [sendxmpp](https://sendxmpp.hostname.sk/), versions [0.15.2](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.2), [0.15.3](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.3) [0.15.4](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.4) and [0.15.5](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.5) have been released. Full details on the [changelog](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- [nbxmpp-client](https://dev.gajim.org/gajim/nbxmpp-client), a small [GTK](https://www.gtk.org/) test client to test various ways to connect to a server, version [2.0.1](https://dev.gajim.org/gajim/nbxmpp-client/-/tags/v2.0.1) has been released. Full details on the [changelog](https://dev.gajim.org/gajim/nbxmpp-client/-/blob/master/CHANGELOG.md?ref_type=heads).
- [peertube-plugin-livechat](https://github.com/JohnXLivingston/peertube-plugin-livechat/blob/main/README.md), a plugin meant to provide a chat system for [Peertube](https://joinpeertube.org/) videos, version [14.0.2](https://github.com/JohnXLivingston/peertube-plugin-livechat/releases/tag/v14.0.2) has been released.
- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md?ref_type=heads), a Python library that provides a way for Python applications to use the XMPP network, version [7.0.0](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/7.0.0) has been released. Full details on the [changelog](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md?ref_type=heads), the cross-platform C++ XMPP client and server library, version [1.13.0](https://invent.kde.org/libraries/qxmpp/-/tags/v1.13.0) has been released. Full details on the [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- [Slidge](https://slidge.im/) versions [0.3.4](https://codeberg.org/slidge/slidge/releases/tag/v0.3.4) 'Christmas special' and [0.3.5](https://codeberg.org/slidge/slidge/releases/tag/v0.3.5) have been released. This releases incorporates conversion of vector animated stickers in the [lottie](https://lottiefiles.com/) format to webp. [Slidgram](https://codeberg.org/slidge/slidgram/) and [slidcord](https://codeberg.org/slidge/slidcord/) already did such conversion, but now it's done via an optional ("extra") dependency of slidge: [rlottie-python](https://pypi.org/project/rlottie-python/), which makes packaging/distribution easier. And many other features, improvements and bugfixes! You can check the release [changelog](https://codeberg.org/slidge/slidge/releases/tag/v0.3.4) or the intermediate changelogs from [0.3.3 to 0.3.5](https://codeberg.org/slidge/slidge/compare/v0.3.3...v0.3.5) for the full list of changes.
  - [matridge](https://codeberg.org/slidge/matridge#readme), the [Matrix](https://matrix.org/) to XMPP gateway based on Slidge and [nio](https://matrix-nio.readthedocs.io/en/latest/), versions [0.3.2](https://codeberg.org/slidge/matridge/releases/tag/v0.3.2) has been released.
  - [matteridge](https://codeberg.org/slidge/matteridge#readme), the [Mattermost](https://mattermost.com/) to XMPP gateway based on Slidge and [mattermost-api-reference-client](https://git.sr.ht/~nicoco/mattermost-api-reference-client), version [0.3.2](https://codeberg.org/slidge/matteridge/releases/tag/v0.3.2) has been released.
  - [slidcord](https://codeberg.org/slidge/slidcord#readme), the [Discord](https://discord.com/) to XMPP gateway based on Slidge and [discord.py-self](https://discordpy-self.readthedocs.io/en/latest/), version [0.3.1](https://codeberg.org/slidge/slidcord/releases/tag/v0.3.1), has been released.
  - [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp#readme), the [WhatsApp](https://www.whatsapp.com/) to XMPP gateway based on [Slidge](https://slidge.im/) and [whatsmeow](https://github.com/tulir/whatsmeow), version [0.3.9](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.9) has been released.
  - [slidgram](https://codeberg.org/slidge/slidgram#readme), the [Telegram](https://telegram.org/) to XMPP gateway based on Slidge and [Pyrofork](https://pyrofork.wulan17.dev/main/), version [0.3.1](https://codeberg.org/slidge/slidgram/releases/tag/v0.3.1), has been released.
- [xmpp-ap-bridge](https://github.com/Barbapulpe/xmpp-ap-bridge/blob/main/README.md), a lightweight Fediverse to XMPP implementation based on client bots to enable chat-like conversations between any Fediverse application and any XMPP client, from your usual client applications, versions [0.7.3](https://github.com/Barbapulpe/xmpp-ap-bridge/releases/tag/v0.7.3) and [0.7.4](https://github.com/Barbapulpe/xmpp-ap-bridge/releases/tag/v0.7.4) have been released.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- [Initial Authentication Pipelining](/extensions/inbox/iap.html)
  - This specification defines a protocol for discovering if the SASL2 `<authenticate>` can be pipelined safely along with the stream open, and if so allows the client to perform this pipelining safely.

### New

- Version 0.1.0 of [XEP-0508](/extensions/xep-0508.html) (Forums)
  - Accepted as Experimental by council vote (dg)
- Version 0.1.0 of [XEP-0509](/extensions/xep-0509.html) (Initial Authentication Pipelining)
  - Accepted as Experimental by council vote (dg)

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.35.3 of [XEP-0045](/extensions/xep-0045.html) (Multi-User Chat)
  - `muc#roomconfig_allowinvites` doesn't restrict owners but enables additional permissions for members. (spw)
- Version 0.7.0 of [XEP-0353](/extensions/xep-0353.html) (Jingle Message Initiation)
  - Remove local redefinition of jingle `<reason/>` element in XML schema and reference existing.
  - Make usage of `<reason/>` element optional in schema, as specified in the text.
  - Add missing definition of 'empty' type in XML schema. (lnj)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- [Last Call](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/thread/MNUPKCA2NR7ARCOU7MOQVQMTWFG77E3T/) for comments on [XEP-0377](/extensions/xep-0377.html) (Spam Reporting)
  - This Last Call begins on 2025-12-12 and shall end at the close of business on 2026-01-05.

### Stable

- Version 1.0.0 of [XEP-0440](/extensions/xep-0440.html) (SASL Channel-Binding Type Capability)
  - Accept as Stable as per Council Vote from 2025-11-18 (XEP Editor (dg))

### Deprecated

- No XEPs deprecated this month.

### Rejected

- No XEPs rejected this month.

## XMPP Public channels

New rooms and public channels are created on a daily basis on the XMPP network. So, if you are on the look out for new and exciting public channels to join, make sure to check out the [Public Channel Search Engine](https://search.jabber.network/search) to find out groups or communities that share your interests!

- If you want to list all the channels, you can find them [here](https://search.jabber.network).
- If you are interested on something in particular, [look by tag](https://search.jabber.network/tags/)!
- If you only want to list rooms in a particular language just add `lang:xx` in the search box, like in this example for the [Spanish language](https://search.jabber.network/search?q=lang%3Aes&f=y&sinaddr=on&sindescr=on&sinname=on). Just make sure to replace `es` for your desired language (like `lang:fr`, `lang:de`, `lang:pt` and so on).

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp-official.bsky.social)
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
  - To [this issue](/categories/newsletter/): *emus, cal0pteryx, Gonzalo Raúl Nemmi, Adrien 'neox' Bourmault, Ludovic Bocquet, Benson Muite, Mario Sabatino, XSF iTeam*

- Translations:
  - [French](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
  - [German](/categories/newsletter/): *Millesimus*
  - [Italian](/categories/newsletter/): *Mario Sabatino, Roberto Resoli*
  - [Portuguese](/categories/newsletter/): *Paulo*
  
## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). At the end of each month, the pad's content is merged into the [XSF GitHub repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations
- communication via media accounts

## XSF Fiscal Hosting Projects

The XSF offers [fiscal hosting](/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](/2021/09/the-xsf-as-a-fiscal-host/). Current projects you can support:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav](https://opencollective.com/pravapp)
- [diasp.in](https://opencollective.com/diasp-in)

## Unsubscribe from the XMPP Newsletter

For this newsletter either [log in here](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/) and unsubscribe or simply send an email to newsletter-leave@xmpp.org.
(If you have not previously logged in, you may need to set up an account with the appropriate email address.)

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
