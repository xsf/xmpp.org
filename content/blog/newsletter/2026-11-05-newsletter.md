---
title: The XMPP Newsletter October 2026
date: 2026-11-05
categories: ['Newsletter']
summary: "Call for Papers for FOSDEM 2027 devroom as well as upcoming XMPP Sprint in London! NLnet supports XMPP software again, many client and gateway updates. Consider to apply for XSF Board, Council as well as general XSF membership."
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of October 2026.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/) and contributors of the XMPP community.

Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors.
If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)?
Read more [at the bottom](#help-us-to-build-the-newsletter).

## Events

- [See below the Call for Papers](#FOSDEM-2027-Decentralised-Messaging-devroom) of the Devroom at FOSDEM 2027!
- [XMPP Sprint London](https://xmpp.org/2026/09/xmpp-sprint-london/): There will be an XMPP Sprint in London from the 6th to the 8th of November at The Mitre in Greenwich.
- The [di.day](https://di.day/en) takes place every [first Sunday of the month](https://fosstodon.org/@xmpp/116867255827209479) where the XMPP community also [promotes their solutions](https://di-day.xmpp.link/)! di.day is a mainly German initiative to help people switch to open-source and privacy-friendly solutions.

See also the [XMPP Events page](/community/events/).

## Videos and Talks

- [Daniel Gultsch − Jabber/XMPP: 25 Years of Digital Independence](https://gultsch.video/w/mHRCPQ3SYTUio8bC7cdhaj) at [LinuxDays](https://www.linuxdays.cz/2026/)
- [Messenger Monopolists hate this trick!](https://makertube.net/w/8Dpe5YJayrKu1KoDnmFJdh) - An XMPP promotion video by Axel Reimer (eversten.net), subtitles [EN]/[FR]
- [Gibt es gute Messenger? (NET⫽SPLIT #2)](https://gultsch.video/w/pAoKnpBVCY3pRt6YhnV32h) - In dieser Folge von NET⫽SPLIT stellt Ückück Daniel Fragen zu XMPP, Matrix, Message Deletion und Messengern im Allgemeinen. [DE]
- [XMPP Speedrun unter Android](https://makertube.net/w/vpuePWVjVq9AY8P24do4Lg) - A short video by Axel Reimer (eversten.net) showing how short it takes to create a new XMPP account using Android (Conversations) [DE]

## Articles

- [NLnet](https://nlnet.nl/): [47 Open Source Projects Receive NLnet Grants to Boost Digital Autonomy](https://nlnet.nl/news/2026/20261015-47-new-projects.html) which also includes [Gajim Audio and Video Calls](https://nlnet.nl/project/Gajim-AV/). This project aims to extend Gajim's text and rich-media messaging by implementing encrypted audio and video calls, ensuring interoperability with other XMPP clients by relying on the same standard protocols based on Jingle and WebRTC ([Jingle RTP Sessions - XEP-0167](/extensions/xep-0167.html), [Jingle ICE-UDP Transport Method - XEP-0176](/extensions/xep-0176.html), [Jingle Raw UDP Transport Method XEP-0177](/extensions/xep-0177.html), [Jingle Message Initiation - XEP-0353](/extensions/xep-0353.html)).
- [Nspawn - Build A Tor-only XMPP Server In Containers](https://silentarchitect.org/articles/2026/10/tor-only-xmpp-in-containers.html), by [DeadSwitch](https://silentarchitect.org/static/pages/about.html) for [The Silent Architect's Whispers](https://silentarchitect.org/index.html).
- [Una presentazione su XMPP al Linux Day 2026](https://www.cuche.cc/una-presentazione-su-xmpp-al-linux-day-2026.html) from [cuche.cc](https://www.cuche.cc/). [IT]
- On [Channel Binding](https://blog.prosody.im/channel-binding/), by The Prosody Team from [Prosodical Toughts](https://blog.prosody.im/).

- [Review blog post](https://xmpp.org/2026/10/xmpp-stand/talk-at-omniopencon-2026-review/) on the XMPP Stand/Talk at OmniOpenCon 2026 by Polarian.
- [XMPP Providers Support in Converse.js & More Automation!](https://providers.xmpp.net/blog/2026-10-28-xmpp-providers-support-in-converse-js-more-automation/) Since earlier this year [Converse.js](https://conversejs.org/) suggests an XMPP provider and allows to select one during account registration. XMPP Providers also accelerated its inclusion process.

{{< figure src="/images/newsletter/2026-11-05/xmpp-providers-converse-integration.png‎" caption="Converse.js suggests an XMPP provider and allows to select one during account registration based on the data from XMPP Providers." >}}

## Software news

### Clients and applications

- [anotherim-js](https://dev.another.im/another-im/anotherim-js/releases) (a new XMPP client written using libtacky and Tauri.rs) has its first public release (version 0.7). Chats, MUCs, OMEMO (both versions), A/V calls (webrtc and libdatachannel backends are available), Push notifications (apushd required for correct work) among with exclusive libtacky features, such as chat state sync (drafts etc) are waiting for your feedback.
- [aTalk](https://github.com/cmeng-git/atalk-android/blob/master/README.md) has released version [6.5.2](https://github.com/cmeng-git/atalk-android/releases/tag/6.5.2) of its encrypted instant messaging with video call and GPS features for Android. This release brings many improvements, quite a few fixes and some really heavy work 'under the hood'. Please refer to the [release notes](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt) for all the details.
- [Conversations](https://conversations.im/) has released version [2.21.0](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.21.0) for Android. This release disables the eMudhra root certificates, even if your Android distribution still includes them. It also enables Channel Binding by default, a method to detect machine-in-the-middle attacks like the one enabled by the eMudhra situation or the one that happened to jabber.ru three years ago. Make sure to take a look at the [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) for all the details.
- [Converse.js](https://conversejs.org) has released version [14.0.1](https://github.com/conversejs/converse.js/releases/tag/v14.0.1) of its open-source web-based XMPP chat client. This is a minor release that brings fixes for OMEMO:2, reactions, notifications and some other small fixes.
- [fluux Messenger](https://www.process-one.net/fluux-messenger/), has released new versions of its modern, cross-platform XMPP client for communities and organizations with smoother history, clearer unread counts, and better sharing ([0.18.0](https://github.com/processone/fluux-messenger/releases/tag/v0.18.0) and [0.18.1](https://github.com/processone/fluux-messenger/releases/tag/v0.18.1), [Full changelog](https://github.com/processone/fluux-messenger/blob/main/CHANGELOG.md)).

{{< figure src="/images/newsletter/2026-11-05/fluux-messenger-0.18.0-2.png" caption="fluux messenger with improved conversation functions like unread messages counts as well as experimental iOS support." >}}

- [Monal](https://monal-im.org/) has released versions [6.4.23](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1098) and [6.4.24](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1101) for iOS and macOS. This version increased sync speed considerably, doesn't show the login view anymore if all configured accounts are disabled and adds other improvements.
- [Monocles](https://monocles.eu/more) has released versions [2.3.1](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.3.1) of its chat client for Android. This versions introduces an improved PQ OMEMO2 rollout, UI redesign of floating bars, separate contacts and groups, updated MiniDNS and add DoT option, allow importing Conversations and Quicksy backups and many fixes and hardenings! This update introduces a needed wire break of the PQ OMEMO2 encryption for further hardening. You may need to reset the OMEMO identities when using PQ OMEMO2. Note: due to some delays with the [Android Play Store](https://play.google.com/store/games) updates, this releases may only be available through [F-droid](https://f-droid.org/en/packages/de.monocles.chat/) at the time of reading.
- [Profanity](https://profanity-im.github.io/) has released version [0.19.0](https://github.com/profanity-im/profanity/releases/tag/0.19.0) of its console based XMPP client. This release brings a list of features, bug fixes, refactorings, and other improvements that is way longer than what it could mention in here. Please make sure to read the [changelog](https://github.com/profanity-im/profanity/blob/master/CHANGELOG) for all the details. Also worth checking out: [Fresh Look For The Website](https://profanity-im.github.io/blog/post/fresh-look-for-the-website.html)!

{{< figure src="/images/newsletter/2026-11-05/profanity-update.png‎" caption="Screenshot of the new Profanity messenger website describing the client purpose and technology." >}}

- [Psi+ 1.5.2202 through 1.6.1.44 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) have been released.

Find more [XMPP Clients](/software/?category=clients).

### Servers

- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) has released versions [6.10.0](https://github.com/esl/MongooseIM/releases/tag/6.10.0) of their enterprise instant messaging solution. You can read all the details in the [changelog](https://github.com/esl/MongooseIM/blob/master/CHANGELOG.md).
- [Security Advisory: eMudhra Intermediate CA Compromise and ejabberd](https://www.process-one.net/blog/security-advisory-emudhra-intermediate-ca-compromise-and-ejabberd/)

Find more [XMPP Servers](/software/?category=servers).

### Libraries & Tools

- [apushd](https://dev.another.im/another-im/apushd) is a fork of Monal's fpush (XEP-0357) with extra features like payload encryption and optional server-side filtering (supported only in clients built on libtacky) and [mod_apush](https://dev.another.im/another-im/anotherim-server/src/branch/master/ejabberd/modules/mod_apush) for ejabberd.
- [ffetcher](https://code.woodpeckersnest.space/roughnecks/ffetcher), an XMPP bot that monitors [RSS](https://www.rssboard.org/rss-specification) and [Atom](https://www.ietf.org/rfc/rfc4287.txt) feeds and posts new articles to one or more MUC rooms, versions [4.1.0](https://code.woodpeckersnest.space/roughnecks/ffetcher/releases/tag/4.1.0) and [4.1.1](https://code.woodpeckersnest.space/roughnecks/ffetcher/releases/tag/4.1.1) have been released.
- [go-xmpp](https://github.com/xmppo/go-xmpp/blob/master/README.md), a Go XMPP library, versions [0.4.9](https://github.com/xmppo/go-xmpp/releases/tag/v0.4.0) and [0.4.1](https://github.com/xmppo/go-xmpp/releases/tag/v0.4.1) have been released.
- [go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/README.md), a tool to send messages to an XMPP contact or MUC inspired by [sendxmpp](https://sendxmpp.hostname.sk/), version [0.17.1+build2](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.17.1+build2) has been released. Full details on the [changelog](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/CHANGELOG.md).
- [jabber.el](https://git.thanosapollo.org/emacs-jabber/about/), the XMPP client for [Emacs](https://www.gnu.org/software/emacs/), versions [0.15.0](https://git.thanosapollo.org/emacs-jabber/tag/?h=0.15.0) and [0.15.1](https://git.thanosapollo.org/emacs-jabber/tag/?h=0.15.1) have been released. Full details on the [changelog](https://git.thanosapollo.org/emacs-jabber/tree/CHANGELOG.org).
- [Koishi](https://github.com/jjj333-p/koishi/blob/main/README.md), a [Matrix](https://matrix.org/) room <-> XMPP MUC bridge, picking up where [Parsee Bridge](https://gitfield.org/kappachat/Parsee) left off, version [0.1.0](https://github.com/jjj333-p/koishi/releases/tag/v0.1.0) has been released.
- [libtacky 1.1](https://dev.another.im/another-im/libtacky) first public release of cross-platform high-level library for building XMPP clients, written in Rust and Tcl. The author claims this library is an XMPP equivalent of Telegram's tdlib. [List of supported XEPs](https://dev.another.im/another-im/libtacky/src/branch/develop/docs/features.md)
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md), the cross-platform C++ XMPP client and server library, version [1.17.0](https://invent.kde.org/libraries/qxmpp/-/tags/v1.17.0) has been released. Full details on the [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md).
- [Slidge](https://slidge.im/), a software library, built in Python, for creating gateways from XMPP to other networks, such as [Telegram](https://telegram.org/), [Discord](https://discord.com/), or [WhatsApp](https://www.whatsapp.com/), versions [0.5.3](https://codeberg.org/slidge/slidge/releases/tag/v0.5.3) and [0.5.4](https://codeberg.org/slidge/slidge/releases/tag/v0.5.4) have been released. You can check the intermediate changelog from [0.5.2 to 0.5.4](https://codeberg.org/slidge/slidge/compare/v0.5.2...v0.5.4) for all the details.
  - [matridge](https://codeberg.org/slidge/matridge#readme), the [Matrix](https://matrix.org/) to XMPP gateway based on [Slidge](https://slidge.im/) and [nio](https://matrix-nio.readthedocs.io/en/latest/), version [0.5.1](https://codeberg.org/slidge/matridge/releases/tag/v0.5.1), has been released.
  - [slidcord](https://codeberg.org/slidge/slidcord#readme), the [Discord](https://discord.com/) to XMPP gateway based on [Slidge](https://slidge.im/) and [discord.py-self](https://discordpy-self.readthedocs.io/en/latest/), version [0.5.1](https://codeberg.org/slidge/slidcord/releases/tag/v0.5.1), has been released.
  - [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp/src/branch/main/README.md), the [WhatsApp](https://www.whatsapp.com/) to XMPP gateway based on [Slidge](https://slidge.im/) and [whatsmeow](https://github.com/tulir/whatsmeow/blob/main/README.md), version [0.5.1](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.5.1) has been released.
  - [slidgnal](https://codeberg.org/slidge/slidgnal/src/branch/main/README.md), a [feature-rich](https://slidge.im/docs/slidgnal/main/user/features.html) [Signal](https://signal.org/) to XMPP puppeteering [gateway](/extensions/xep-0100.html), based on [slidge](https://slidge.im/) and [signalmeow](https://github.com/mautrix/signal/tree/main/pkg/signalmeow), version [0.5.1](https://codeberg.org/slidge/slidgnal/releases/tag/v0.5.1) has been released.
  - [slidgram](https://codeberg.org/slidge/slidgram#readme), the [Telegram](https://telegram.org/) to XMPP gateway based on [Slidge](https://slidge.im/) and [Pyrofork](https://pyrofork.wulan17.dev/main/), version [0.5.1](https://codeberg.org/slidge/slidgram/releases/tag/v0.5.1), has been released.
- [Smack](https://www.igniterealtime.org/projects/smack/), a modular and portable XMPP client library for Android and Java has been published in [version 4.5.0](https://discourse.igniterealtime.org/t/smack-4-5-0-release/96599).
- [tackygram](https://dev.another.im/another-im/tackygram) is an experimental Telegram gateway built using libtacky and gotd with A/V calls support and secret chats (supported only in clients built on libtacky)

Find more [XMPP Libraries & Tools](/software/?category=libraries).

---

## XSF Announcements

#### FOSDEM 2027 Decentralised Messaging devroom
The XMPP Standards Foundation (XSF), together with our friends from the Matrix and Delta Chat communities, is organising a [Decentralised Messaging devroom at FOSDEM 2027](https://xmpp.org/2026/10/fosdem-2027-decentralised-messaging-devroom/), and we are looking for speakers. [Submission](https://fosdem.org/submit) deadline for talks is Friday, November 20, 2026!

#### Board and Council Elections 2026

The [XMPP Standards Foundation](/about/xmpp-standards-foundation/) is calling for individuals to compose the [Board of Directors](/about/xmpp-standards-foundation/#board) and members to serve on the [XMPP Council](/about/xmpp-standards-foundation/#council) for the 2026/2027 period. If you are interested in running for the Board of Directors or the XMPP Council, please add a [wiki page](https://wiki.xmpp.org/web/Main_Page) about your candidacy to one or both of the aforementioned sections [before November 8, 2026, 00:00 UTC](https://wiki.xmpp.org/web/Board_and_Council_Elections_2026). Get involved in the XMPP Standards Foundation organization decisions and with the specifications we publish. Note: XMPP Council members must be [elected members](/about/xsf/members/) of the XSF; however, there is no such restriction for the Board of Directors.

#### Membership

Being an elected member of the XMPP Standards Foundation signals a commitment to open standards and professional engagement in / with the XMPP community. Here, your membership helps position the XSF as a healthy organization, which in itself is valuable. It also grants voting rights on technical and administrative matters within the XSF. The application is a light-weight and free of cost process and you can use your membership to get more involved more easily, too. If you are interested in joining the XMPP Standards Foundation as a member, please apply to our **4th quarterly** call for members admission [before November 29, 2026, 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q4_2026).

---

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/).
Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things.
Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred.
This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes.
[Read more about the standards process](/about/standards-process.html).
Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/).
Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- [MUC is ready](/extensions/inbox/muc-ready.html)
  - This specification provides a way for MUC components to inform clients that a room is ready to be re-joined.
- [Portable Import/Export Format for XMPP Components](/extensions/inbox/pie-components.html)
  - This document specifies a file format for importing and exporting component data to and from XMPP software.
- [Bookmark last known name](/extensions/inbox/bookmark-last-known-name.html)
  - This document defines an XMPP protocol extension to allow users to pin PEP Native Bookmarks.
- [Bookmarks hierarchy](/extensions/inbox/bookmarks-hierarchy.html)
  - This specification provides a way to organise bookmarks.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.0.3 of [XEP-0070](/extensions/xep-0070.html) (Verifying HTTP Requests via XMPP)
  - Fix namespaces in examples (spw)
- Version 0.12.1 of [XEP-0292](/extensions/xep-0292.html) (vCard4 Over XMPP)
  - Fix examples for gender and pref vcard fields (ph)
- Version 0.12.2 of [XEP-0292](/extensions/xep-0292.html) (vCard4 Over XMPP)
  -  Fix automated entity example for removal of raw-IQ mode (ka)
- Version 0.3.1 of [XEP-0425](/extensions/xep-0425.html) (Moderated Message Retraction)
  - Clarify that the tombstone of a retracted XEP-0308 correction keeps its `<replace/>` element (jcb)
- Version 0.1.4 of [XEP-0491](/extensions/xep-0491.html) (WebXDC)
  - Support realtime channels (spw)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status.
After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments.
The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No last call this month.

### Stable

- No XEP moved to stable this month.

### Deprecated

- No XEPs deprecated this month.

### Rejected

- No XEPs rejected this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp.org)
- [Reddit](https://www.reddit.com/r/xmpp/)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project?
Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions.
Volunteers and more languages are welcome!
Translations of the XMPP Newsletter will be released here (with some delay).
Consider to donate to the individuals that spend their time creating this edition:

- Contributors:
  - To [this issue](/categories/newsletter/): *Adrien 'neox' Bourmault, [cal0pteryx](https://liberapay.com/cal0pteryx/), [emus](https://liberapay.com/Echolon/), Gonzalo Raúl Nemmi, Ludovic Bocquet, [XSF Infrastructure Team](https://xmpp.org/about/xsf/infrastructure-team/)*

- Translations:
  - [French](https://linuxfr.org/tags/xmpp/public): *Adrien 'neox' Bourmault, seveso, anubis, BAud, impromptux, Benoit Sibaud, Ysabeau and Pierre Jarillon.
  
## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community.
Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung).
At the end of each month, the pad's content is merged into the [XSF GitHub repository](https://github.com/xsf/xmpp.org/milestone/3).
We are always happy to welcome contributors.
Do not hesitate to join the discussion in our [XSF Communications Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort.
You have a project and want to spread the news?
Please consider sharing your news or events here, and promote it to a large audience.

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

