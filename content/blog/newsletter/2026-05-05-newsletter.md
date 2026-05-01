---
title: The XMPP Newsletter April 2026
date: 2026-05-05
categories: ['Newsletter']
summary: "In this issue: 2nd quarterly call for XSF members admissions. XMPP at FOSSY 2026. XMPP Sprint in Berlin. Two new NLnet grants. Experimenting with MariaDB, Firebird and CockroachDB Support in Openfire, bringing jabber.el back from the dead, Fluux Messenger 0.15 and beyond, Libervia progress notes, Matridge spaces with NLNet, and a lot more! Update your clients with aTalk, Fluux Messenger, Gajim, Monal, Monocles, Movim, Poezio and Profanity. Update your servers: ejabberd 26.04 and Prosody IM 13.0.5. Specifications update: six proposed XEP's, two new XEP's, and five updated ones!"
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of April 2026.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/).

Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors. If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XSF Membership

Being an elected member of the XMPP Standards Foundation signals a commitment to open standards and professional engagement in / with the XMPP community. Here, your membership helps position the XSF as a healthy organization, which in itself is valuable. It also grants voting rights on technical and administrative matters within the XSF. The application is a light-weight and free of cost process and you can use your membership to get more involved more easily, too. If you are interested in joining the XMPP Standards Foundation as a member, please apply to our **2nd quarterly** call for members admissions [before May 17th, 2026, 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q2_2026).

## XMPP Events

- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2026-06_Berlin) (DE / EN): will take place in June, from Friday 19th to Sunday 21st 2026, at the [Wikimedia Deutschland e.V.](https://www.openstreetmap.org/node/2551527703#map=19/52.498414/13.381049) offices in Berlin, Germany. If this sounds like the right event for you, come and join us! Just make sure to list yourself [here](https://wiki.xmpp.org/web/Sprints/2026-06_Berlin#Attendees), so we know how many people will attend and we can plan accordingly. If you have any questions or concerns, join us at the chatroom: [sprints@muc.xmpp.org](xmpp:sprints@muc.xmpp.org?join)!
- XMPP at FOSSY 2026: This year's edition of [FOSSY](https://2026.fossy.ca/), the fourth _Free and Open Source Software Yearly_ conference, will take place during the month of August, from Thursday 6th to Sunday 9th 2026 at the [University of British Columbia](https://www.ubc.ca/), Vancouver, Canada. As always, there will be an [XMPP Track](https://2026.fossy.ca/pages/tracks/). The [call for proposals](https://2026.fossy.ca/call-for-proposals/) closed on April 30th, 2026. Once again, this year [JMP](https://jmp.chat/) was pleased to do its annual offer for funding to the potential speakers who would like to host a talk on the XMPP track.

## Videos and Talks

- [Mensajería instantánea: por qué recomiendo XMPP](https://creators.spotify.com/pod/profile/dmurana/episodes/Mensajera-instantnea-por-qu-recomiendo-XMPP-e3iat5d), a podcast by [Damián Muraña](https://damian.murana.uy/acerca-de/) for [Cosas de Damián](https://damian.murana.uy/podcast/). [ES]
- [Conversations (XMPP): Feature-Preview](https://makertube.net/w/pnjU56zj83eE2Ys2Av22Wm), by [eversten.net](https://makertube.net/a/eversten.net/video-channels) for [XMPP Tutorials DE](https://makertube.net/c/xmpp_tutorials_de/videos). [DE] [[EN](https://makertube.net/w/g41J1Bcvf3Mjk6h9H1kt2N)]
- [XMPP: Instant Messaging that works like email](https://pt.gogreenit.net/w/7YzvYkDJVM1e5FcmnCpqkj) by Polarian and [Chewie](https://mammut.gogreenit.net/@chewie) at [oggcamp 2026](https://www.oggcamp.org/).

## XMPP Articles

- [NLnet](https://nlnet.nl/): [57 Projects Receive NGI Zero Grants to Fix the Internet](https://nlnet.nl/news/2026/20260409-announce-commons-fund.html)
  - [OpenPGP refresh for Conversations](https://nlnet.nl/project/Conversations-OpenPGP-refresh/): This project aims to modernize PGP encryption within [Conversations](https://conversations.im/), a Jabber/XMPP client, by integrating cryptographic operations and adopting updated messaging standards. Furthermore, the project will implement and update the modern [OpenPGP](https://www.openpgp.org/) standards for XMPP ([XEP-0373](/extensions/xep-0373.html) and [XEP-0374](/extensions/xep-0374.html)) by making use of Stanza Content Encryption (SCE). This transition not only benefits users who prefer PGP-based encryption but also serves as a critical building block for the development of OMEMOv2.
  - [Matridge spaces](https://nlnet.nl/project/Matridge/): [Matridge](https://codeberg.org/slidge/matridge/src/branch/main/README.md) is a gateway for XMPP users to transparently chat in [Matrix]() rooms. It is an XMPP server-side component that acts as a [Matrix](https://matrix.org/) client and makes it possible to pilot a Matrix client from any XMPP client. It implements modern instant messaging features such as rich replies, spaces, attachments, emoji reactions and threads. It is self-hosting friendly, community-lead, written in python and based on slidge, an XMPP gateway library.
- [Experimenting with MariaDB, Firebird and CockroachDB Support in Openfire](https://discourse.igniterealtime.org/t/experimenting-with-mariadb-firebird-and-cockroachdb-support-in-openfire/96434), by [guus](https://discourse.igniterealtime.org/u/guus/summary) for the [Ignite Realtime community](https://discourse.igniterealtime.org/).
- [Bringing jabber.el Back From the Dead](https://thanosapollo.org/posts/emacs-jabber-revival/), by [Thanos Apollo](https://thanosapollo.org/about/) from the [thanosapollo posts](https://thanosapollo.org/posts/).
- [Fluux Messenger 0.15: Search, Themes, Polls, and a Whole Lot More](https://www.process-one.net/blog/fluux-messenger-0-15/), by [Mickaël Rémond](https://www.process-one.net/author/mremond/) for the [ProcessOne blog](https://www.process-one.net/blog/).
- [Full Text Search with IndexedDB](https://blog.jmp.chat/b/2026-full-text-search-indexeddb), by singpolyma for the [JMP blog](https://blog.jmp.chat/).
- [Fluux Messenger 0.15.2: RTL Support, Faster Reconnection, and a Pile of Reliability Fixes](https://www.process-one.net/blog/fluux-messenger-0-15-2-rtl-support-faster-reconnection-and-a-pile-of-reliability-fixes/) by [Mickaël Rémond](https://www.process-one.net/author/mremond/) for the [ProcessOne blog](https://www.process-one.net/blog/).
- [Libervia progress note 2026-W16](https://www.goffi.org/id/libervia-progress-note-2026-w16-ooph): a complete and comprehensive blog post about the Audio/Video implementation, email gateway, work on installation/configuration simplification and the new forge, focus on web frontend and redesign and work done with current metadata reduction and serverless XMPP (Tor, contacts e2ee, new pubsub implementation) by [Goffi](https://mastodon.social/@Goffi).
- [Movim 0.33 "Halley" is Out!](https://mov.im/community/pubsub.movim.eu/Movim/a1f5a954-e80c-45bd-911b-62e1bf98f8da), by Timothée Jaussoin for the [Movim Blog](https://mov.im/community/pubsub.movim.eu/Movim).
- [XMPP – The Middle Ground Of Instant Messaging](https://tomsitcafe.com/2026/04/24/xmpp-the-middle-ground-of-instant-messaging/): XMPP or Extensible Messaging and Presence Protocol is an open communication protocol. In this article you will learn to install a private, non-federated XMPP server. By [Tom's IT Cafe](https://mastodon.social/@TomsITCafe) for the [Tom's IT Cafe blog](https://tomsitcafe.com/).
- [XMPP como alternativa a Whatsapp](https://onlykievvv.bearblog.dev/xmpp-como-alternativa-a-whatsapp/), by [Runforrest](https://onlykievvv.bearblog.dev/acerca-de-mi/) for [Runforrest World blog](https://onlykievvv.bearblog.dev/). [ES]
- [XMPP: mensajería instantánea libre y federada](https://damian.murana.uy/xmpp-mensajeria-instantanea-libre-y-federada/), by [Damián Muraña](https://damian.murana.uy/acerca-de/) for [Damián Muraña blog](https://damian.murana.uy/posts/). [ES]
- [Matridge spaces with NLNet](https://slidge.im/blog/2026/04/28/nlnet-spaces-kickoff/), from the [slidge.im blog](https://slidge.im/blog/).

## XMPP Software News

### XMPP Clients and Applications

- [aTalk](https://github.com/cmeng-git/atalk-android/blob/master/README.md) has released versions [5.2.2](https://github.com/cmeng-git/atalk-android/releases/tag/5.2.2) and [5.3.0](https://github.com/cmeng-git/atalk-android/releases/tag/5.3.0) of its encrypted instant messaging with video call and GPS features for Android. Both versions bring a lot of 'under the hood' changes. Please refer to the [release notes](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt) or check out the intermediate changelog from [5.2.1 to 5.3.0](https://github.com/cmeng-git/atalk-android/compare/5.2.1...5.3.0) for all the details.
- [Fluux Messenger](https://github.com/processone/fluux-messenger/blob/main/README.md), has released versions [0.15.0](https://github.com/processone/fluux-messenger/releases/tag/v0.15.0), [0.15.1](https://github.com/processone/fluux-messenger/releases/tag/v0.15.1) and [0.15.2](https://github.com/processone/fluux-messenger/releases/tag/v0.15.2), of its modern, cross-platform XMPP client for communities and organizations. These versions introduce a large list of additions and new features like [12 built-in themes](https://github.com/processone/fluux-messenger/blob/main/screenshots/OVERVIEW.md#theme-showcase), reaction-based polls for MUC rooms with deadlines, full-text message search across all conversations and rooms, font size adjustment buttons, activity log events are clickable and allow you to navigate to the relevant conversation and message, and the ability to disable push notifications just to name a few of them! The list also expands to improvements, bugfixes and it's way longer than what we can mention in here! Please, go straight to the [fulll changelog](https://github.com/processone/fluux-messenger/blob/main/CHANGELOG.md) for all the details, because there are a lot of them!

{{< figure src="/images/newsletter/2026-05-05/fluux_chat_rose_pine.png" caption="Fluux Messenger Rose Pine theme." >}}

- [Gajim](https://gajim.org/) has released version [2.4.6](https://gajim.org/posts/2026-04-19-gajim-2.4.6-released/) of its free and fully featured chat app for XMPP. This release can now give you a clue if it's night for your contacts and comes with improvements for the activity feed, better display of mentions, fixed message scrolling, and many bugfixes. Thank you for all your contributions! You can take a look at the [changelog](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) for all the details.

{{< figure src="/images/newsletter/2026-05-05/gajim_mentions.png" caption="Gajim: A message mentioning you" >}}

- [Monal](https://monal-im.org/) has released version [6.4.20](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1090) for iOS and macOS with a rather large list of fixes.
- [Monocles](https://monocles.eu/more) has released version [2.1.5](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.1.5) of its chat client for Android. This release brings fixes on import settings and hide offline. It implements swipe to previous or next media in preview, clear push notification configuration values, and work on UnifiedPush to add support for link activity among other niceties!
- [Movim](https://movim.eu/) has released version [0.33](https://mov.im/community/pubsub.movim.eu/Movim/a1f5a954-e80c-45bd-911b-62e1bf98f8da), code named [Halley](https://en.wikipedia.org/wiki/Halley%27s_Comet)! After months of work and hundreds of commits, this is the biggest Movim release ever made. This release massively scales up Movim's architecture while introducing long-awaited, and exclusive, new features like spaces, shorcuts, hats, swipe to reply, videoconference, audio and screen sharing, categorizing content during calls, refactored notifications, new administration tools and accessiblity improvements, a big Funding Campaign for 2026, and even two new mascots: Miho and Stash! A lot of work was also done to improve accessibility thanks to [NLnet](https://nlnet.nl/) funding. Head over the [official release announcement](https://mov.im/community/pubsub.movim.eu/Movim/a1f5a954-e80c-45bd-911b-62e1bf98f8da) and dive directly into the exciting things you can find in this release!

{{< figure src="/images/newsletter/2026-05-05/movim_spaces.png" caption="Movim: Spaces; already compatible with ejabberd. Prosody support coming very soon!" >}}

- [Poezio](https://poez.io/en/) has released versions [0.16.1](https://blog.mathieui.net/poezio-0-16-1.html) and [0.17](https://blog.mathieui.net/en/poezio-0-17.html) of its console XMPP client. The former is a bugfix release that brings mostly fixes and internal stuff, but also adds the ability to see redacted/moderated messages if you wish so, particularly useful if you are the one moderating. The latter is a small release focused on receiving and sending message reactions! You can find all the details in their respective links.

{{< figure src="/images/newsletter/2026-05-05/poezio_react.png" caption="Poezio: receiving message reactions" >}}

{{< figure src="/images/newsletter/2026-05-05/poezio_react_cmd.png" caption="Poezio: sending message reactions" >}}

- [Profanity](https://profanity-im.github.io/) has released version [0.18.0](https://github.com/profanity-im/profanity/releases/tag/0.18.0) of its console based XMPP client written in C. This release adds spellcheck highlighting support and implements asynchronous external editor support while introducing quite a few bugfixes. Please make sure to read the [changelog](https://github.com/profanity-im/profanity/blob/master/CHANGELOG) for all the details!

### XMPP Servers

- [ProcessOne](https://www.process-one.net/) has released [ejabberd 26.04](https://www.process-one.net/blog/ejabberd-26-04/). This security release [includes options to limit XML parser](https://www.process-one.net/blog/ejabberd-26-04/#parser), and other minor bugfixes. It is strongly encouraged that you update ejabberd as soon as possible. Make sure to read the [changelog](https://www.process-one.net/blog/ejabberd-26-04/#a-namechangelogachangelog) for all the details and a complete list of fixes and improvements on this release.
- [Prosody IM](https://prosody.im/) is pleased to announce version [13.0.5](https://blog.prosody.im/prosody-13.0.5-released/), a new minor release from the stable branch. This is a security release for the Prosody 13.0.x stable series. It fixes multiple security issues, some memory leaks, some smaller bugs and changes which have been implemented since the previous release. Full details about the security vulnerabilities can be found in the [security advisory](https://prosody.im/security/advisory_735dd9d3/). All Prosody operators on 13.0.4 or earlier are encouraged to upgrade to 13.0.5 as soon as possible, or to review the advisory and implement appropriate mitigations. Read [changelog](https://prosody.im/doc/release/13.0.5) for all the details, and as always, detailed download and install instructions are available on the [download page](https://prosody.im/download/) for your convenience.

### XMPP Libraries & Tools

- [jabber.el](https://codeberg.org/emacs-jabber/emacs-jabber/src/branch/master/README.org), the XMPP client for [Emacs](https://www.gnu.org/software/emacs/), versions [0.10.0](https://codeberg.org/emacs-jabber/emacs-jabber/releases/tag/0.10.0) to [0.10.6](https://codeberg.org/emacs-jabber/emacs-jabber/releases/tag/0.10.6) have been released. Full details on all the releases in the [changelog](https://codeberg.org/emacs-jabber/emacs-jabber/src/branch/master/CHANGELOG.org).
- [librssguard-xmpp](https://github.com/martinrotter/rssguard/tree/master/src/librssguard-xmpp), a [plugin](https://rssguard.readthedocs.io/en/latest/features/xmpp.html) for the [RSS Guard](https://github.com/martinrotter/rssguard/blob/master/README.md) desktop feed reader that offers basic XMPP support to fetch real-time (push) ATOM/PubSub entries and single/multi user chat messages.
- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md), a Python library that provides a way for Python applications to use the XMPP network, version [7.2.0](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/7.2.0) has been released. Full details on the [changelog](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md), the cross-platform C++ XMPP client and server library, versions [1.14.6](https://invent.kde.org/libraries/qxmpp/-/tags/v1.14.6), [1.14.7](https://invent.kde.org/libraries/qxmpp/-/tags/v1.14.7), [1.15.0](https://invent.kde.org/libraries/qxmpp/-/tags/v1.15.0) and [1.15.1](https://invent.kde.org/libraries/qxmpp/-/tags/v1.15.1) have been released. Full details on the [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md).
- [Slidge](https://slidge.im/) versions [0.3.8](https://codeberg.org/slidge/slidge/releases/tag/v0.3.8) and [0.3.9](https://codeberg.org/slidge/slidge/releases/tag/v0.3.9) have been released. The former comes with the usual bug fixes and introduces image link previews and contact- and room-specific commands along with a lot of internal changes to improve the code maintainability. The latter is a bugfix release, notably for a crash triggered by using chat commands introduced by a refactor of the commands system in the previous release. You can check the intermediate changelog from [0.3.7 to 0.3.9](https://codeberg.org/slidge/slidge/compare/v0.3.7...v0.3.9) for all the details.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- [Message Archive Management: Trim Command](/extensions/inbox/xep-mam-trimming.html)
  - This specification describes how a client can request "trimming" of an archive.
- [Group Chat Reporting](/extensions/inbox/xep-gc-reporting.html)
  - This specification describes how a client can report abuse and spam in a MUC or other group chat context.
- [Occupant Mute Synchronization](/extensions/inbox/xep-occupant-mute-sync.html)
  - Allows synchronizing a list of muted group chat participants between multiple clients.
- [New MUC](/extensions/inbox/new-muc.html)
  - This document specifies an enhanced Multi-User Chat protocol that is broadly backwards compatible with that of [XEP-0045](/extensions/xep-0045.html)(Multi-User Chat), but adds a number of key improvements.
- [Payment Required](/extensions/inbox/payment-required.html)
  - This specification defines an XMPP protocol extension that enables services to require payment before granting access to a resource. It provides a payment-system neutral invoice format supporting multiple concurrent payment options, including bank transfers (SEPA, IBAN, UPI) and instant-settlement networks (Lightning Network), and integrates with the existing CAPTCHA challenge mechanism defined in [XEP-0158](/extensions/xep-0158.html) (CAPTCHA Forms).
- [Emoji Markup](/extensions/inbox/emoji-markup.html)
  - This specification leverages Message Markup and Stateless file sharing or Stateless Inline Media Sharing (SIMS) to send custom emojis.

### New

- Version 5.6.7.8 of [XEP-0512](/extensions/xep-0512.html) (XMPP as Interpretive Dance)
  - Initial published version. (gdk)
- Version 0.1.0 of [XEP-0513](/extensions/xep-0513.html) (Explicit Mentions)
  - Accepted as Experimental by council vote on 2026-03-31 (dg)

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated
- Version 1.35.4 of [XEP-0045](/extensions/xep-0045.html) (Multi-User Chat)
  - Add clarification how to unset a reserved nickname when modifying the member list.
  - Split passage which defines how to modify the member list into multiple sentences to improve readability. (ph)
- Version 1.1.0 of [XEP-0345](/extensions/xep-0345.html) (Form of Membership Applications)
  - Apply policy changes after Board vote on 2026-04-16.
  - Allow Legal Name to be provided privately to the Secretary instead of published.
  - Add support for alternative public identifiers.
  - Clarify handling of private information and alignment with XSF disclosure policy. (gdk)
- Version 0.9.1 of [XEP-0384](/extensions/xep-0384.html) (OMEMO Encryption)
  - Fix using `id=0` in examples. Spec requires positive numbers. (XEP Editor: dg)
- Version 0.2.1 of [XEP-0413](/extensions/xep-0413.html) (Order-By)
  - Replace old namespace use in examples. (jp)
- Version 0.2.0 of [XEP-0509](/extensions/xep-0509.html) (Initial Authentication Pipelining)
  - Updates based on implementation. (dwd)

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
  - To [this issue](/categories/newsletter/): *emus, cal0pteryx, Gonzalo Raúl Nemmi, Ludovic Bocquet, XSF iTeam*

- Translations:
  - [French](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
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

## Unsubscribe from the XMPP Newsletter

For this newsletter either [log in here](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/) and unsubscribe or simply send an email to newsletter-leave@xmpp.org.
(If you have not previously logged in, you may need to set up an account with the appropriate email address.)

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
