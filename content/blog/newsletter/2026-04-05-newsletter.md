---
title: The XMPP Newsletter March 2026
date: 2026-04-05
categories: ['Newsletter']
summary: "In this issue: Two XMPP Events, learn about Spaces in XMPP, a new XMPP MUC BanBot, Self-hosting UnifiedPush with Conversations as Distributor, a new member of the Slidge family, and a complete translation of JoinJabber to Portuguese (BR). Specifications update: a proposed XEP, four updated ones, and a Last Call!"
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of March 2026.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/).
Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors. If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XSF Membership

Being an elected member of the XMPP Standards Foundation signals a commitment to open standards and professional engagement in / with the XMPP community. Here, your membership helps position the XSF as a healthy organization, which in itself is valuable. It also grants voting rights on technical and administrative matters within the XSF. The application is a light-weight and free of cost process and you can use your membership to get more involved more easily, too. If you are interested in joining the XMPP Standards Foundation as a member, please apply to our **2nd quarterly** call for members admissions [before May 17th, 2026, 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q2_2026).

## XMPP Events

- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2026-06_Berlin) (DE / EN): will take place in June, from Friday 19th to Sunday 21st 2026, at the [Wikimedia Deutschland e.V.](https://www.openstreetmap.org/node/2551527703#map=19/52.498414/13.381049) offices in Berlin, Germany. If this sounds like the right event for you, come and join us! Just make sure to list yourself [here](https://wiki.xmpp.org/web/Sprints/2026-06_Berlin#Attendees), so we know how many people will attend and we can plan accordingly. If you have any questions or concerns, join us at the chatroom: [sprints@muc.xmpp.org](xmpp:sprints@muc.xmpp.org?join)!
- XMPP at FOSSY 2026: This year's edition of [FOSSY](https://2026.fossy.ca/), the fourth _Free and Open Source Software Yearly_ conference, will take place during the month of August, from Thursday 6th to Sunday 9th 2026 at the [University of British Columbia](https://www.ubc.ca/), Vancouver, Canada. As always, there will be an [XMPP Track](https://2026.fossy.ca/pages/tracks/) and the [call for proposals](https://2026.fossy.ca/call-for-proposals/) is open until May 22, 2026.
Once again, this year [JMP](https://jmp.chat/) is pleased to announce its annual offer for funding to the potential speakers who would like to host a talk on the XMPP track. Please, join them at [discuss@conference.soprani.ca](xmpp:discuss@conference.soprani.ca?join), and don't hesitate to ask for more information!

## Videos and Talks

- [IETF125 Hackathon: XEP-0202 Entity Time](https://gultsch.video/w/8FL21NETdAjnM23hWkYeiZ), by [Daniel Gultsch](https://gultsch.de/).

## XMPP Articles

- [Let's Talk About Spaces in XMPP](https://mov.im/community/pubsub.movim.eu/Movim/fb46d699-adc1-4fda-a76e-71ca1d246b80), by Timothée Jaussoin for the [Movim Blog](https://mov.im/community/pubsub.movim.eu/Movim).
- [Our new XMPP MUC BanBot](https://dan.envs.net/blog/2026/2026-03-05-our-new-xmpp-muc-banbot), by [~dan](https://dan.envs.net/contact) for [~dan's website on envs.net](https://dan.envs.net/).
- [Sending Jabber/XMPP Messages via HTTP](https://gultsch.de/posts/xmpp-via-http/), by [Daniel Gultsch](https://gultsch.de/).
- [Self-hosting UnifiedPush with Conversations as Distributor](https://gultsch.de/posts/self-hosting-up/), by [Daniel Gultsch](https://gultsch.de/).
- [Installing ejabberd](https://the.teabag.ninja/2026/03/14/installing-ejabberd/), by eltheanine for the [The Teabag Ninja](https://the.teabag.ninja/).
- [Fluux Messenger 0.14.0 - Full Room Control & Richer Contact Profiles](https://www.process-one.net/blog/fluux-messenger-0-14-0/), by [Mickaël Rémond](https://www.process-one.net/author/mremond/) for the [ProcessOne Blog](https://www.process-one.net/blog/).
- [My Prosody setup with Docker Compose](https://gsvd.dev/blog/my-prosody-setup-with-docker-compose), by [gsvd.dev](https://gsvd.dev/contact) for the [gsvd.dev blog](https://gsvd.dev/blog).
- [The Slidge family is growing](https://slidge.im/blog/2026/03/14/slidge-family-growing/), from the [slidge.im blog/](https://slidge.im/blog/).
- [JoinJabber](https://joinjabber.org/): thanks to the excellent work done by one of the community members, the whole site is now fully available in [Portuguese (BR)](https://joinjabber.org/pt-br/)! You can check the translation status on their [web translation status page](https://translate.codeberg.org/projects/joinjabber/website/) and help out with other translations!
- [Introducing CLabber](https://github.com/parenworks/CLabber/blob/feature/native-xmpp/README.org): A terminal UI (TUI) XMPP (Jabber) client written in Common Lisp.
- [Upgrade ejabberd on Debian NOW](https://monal-im.org/post/00016-upgrade-ejabberd-on-debian/): Chances might be that you are running a [Debian](https://www.debian.org/) based [ejabberd](https://www.ejabberd.im/) server. Unfortunately push for all your [Monal](https://monal-im.org/) users on that server will break in less than 2 months. And chances are that some of your S2S connections are already failing today. By Thilo Molitor for the [monal-im blog](https://monal-im.org/post/).

## XMPP Software News

### XMPP Clients and Applications

- [aTalk](https://github.com/cmeng-git/atalk-android/blob/master/README.md) has released versions [5.2.0](https://github.com/cmeng-git/atalk-android/releases/tag/5.2.0) and [5.2.1](https://github.com/cmeng-git/atalk-android/releases/tag/5.2.1) of its encrypted instant messaging with video call and GPS features for Android. The former version implements [XEP-0384](/extensions/xep-0384.html) (OMEMO Encryption), decryption of OMEMO messages, upgrades smack to support [XEP-0420](/extensions/xep-0420.html) (Stanza Content Encryption) and other relevant updates and fixes, while the latter introduces a fix for an incorrect fetching. You can check the intermediate changelog from [5.1.0 to 5.2.0](https://github.com/cmeng-git/atalk-android/compare/5.1.0...5.2.0) and [5.2.0 to 5.2.1](https://github.com/cmeng-git/atalk-android/compare/5.2.0...5.2.1) for all the details.
- [Conversations](https://conversations.im/) has released versions [2.19.13](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.13), [2.19.14](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.14) and [2.9.15](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.15) for Android. These releases bring fixes for a crash when changing OMEMO bundle access model, a crash when sharing [Quicksy](https://quicksy.im/) XMPP addresses and a fix for [Quicksy](https://quicksy.im/) registration on older devices, shows `hats` in public conferences where available, shows a warning in the chat if a contact is in different time zone and it is night time for them, a refactored automatic DND handling (based on system DND), and a warning in the chat window if contact is in DND mode. You can take a look at the [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) for all the details or check the intermediate changelogs from [2.19.12 to 2.19.13](https://codeberg.org/iNPUTmice/Conversations/compare/2.19.12...2.19.13), [2.19.13 to 2.19.14](https://codeberg.org/iNPUTmice/Conversations/compare/2.19.13...2.19.14) and/or [2.19.14 to 2.19.15](https://codeberg.org/iNPUTmice/Conversations/compare/2.19.14...2.19.15).

{{< figure src="/images/newsletter/2026-04-05/conversations-contact-time.png" caption="Conversations showing contact's local time in the chat window" >}}

- [Cheogram](https://cheogram.com/) has released version [2.19.0-5](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.19.0-5) for Android. A bugfix release that addresses many crash fixes, never use iterative DNS for DNSSEC, fallback public server is now jabber.fr, merge security fixes from upstream, allow emoji search by emoji (eg for reactions), better isApp logic to default to commands list or not, and fix for channel avatars on some older servers. Make sure to check out the [changelog](https://git.sr.ht/~singpolyma/cheogram-android/refs) for all the details.
- [Fluux Messenger](https://github.com/processone/fluux-messenger/blob/main/README.md) has released versions [0.13.3](https://github.com/processone/fluux-messenger/releases/tag/v0.13.3) and [0.14.0](https://github.com/processone/fluux-messenger/releases/tag/v0.14.0), of its modern, cross-platform XMPP client for communities and organizations, with a list of additions, new features, improvements and bugfixes that is way longer than what we could ever mention in here! You can go straight to the [full changelog](https://github.com/processone/fluux-messenger/blob/main/CHANGELOG.md) or check the intermediate changelogs from [0.13.2 to 0.13.3](https://github.com/processone/fluux-messenger/compare/v0.13.2...v0.13.3) and/or [0.13.3 to 0.14.0](https://github.com/processone/fluux-messenger/compare/v0.13.3...v0.14.0) for all the details!

{{< figure src="/images/newsletter/2026-04-05/fluux-messenger.png" caption="Fluux Messenger team chat" >}}

- [Gajim](https://gajim.org/) has released version [2.4.5](https://gajim.org/posts/2026-03-30-gajim-2.4.5-released/) of its free and fully featured chat app for XMPP. This release lets you know when somebody reacted to one of your messages. It also comes with automatic timezone updates and improvements for macOS, and bugfixes. Thank you for all your contributions! You can take a look at the [changelog](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) for all the details.

{{< figure src="/images/newsletter/2026-04-05/gajim-timezone-update.png" caption="Gajim automatic timezone updates" >}}

- [Monal](https://monal-im.org/) has released version [6.4.19](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1085) for iOS and macOS with a rather large list of fixes.
- [Monocles](https://monocles.eu/more) has released version [2.1.4](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.1.4) of its chat client for Android. This release brings fixes for message moderation, truncated text, link click handling, disappearing reactions popup, MUC destruction, a crash when message body not spannable, allow camera/mic in command UI webview and pick channel binding fallback when server has no [XEP-0440](/extensions/xep-0440.html) (SASL Channel-Binding Type Capability) support.
- [Poezio](https://poez.io/en/) has released version [0.16](https://codeberg.org/poezio/poezio/releases/tag/v0.16) of its console XMPP client. This release implements [XEP-0425](/extensions/xep-0425.html) (Moderated Message Retraction) a receiving side of moderation, [XEP-0424](/extensions/xep-0424.html) (Message Retraction) retraction events, [XEP-0377](/extensions/xep-0377.html) (Blocking Command Reports) a new `/report` plugin to report spam, a new `/tcp-reconnect` to kill TCP connections on faulty networks, a `tls_verify_cert` option that can be set to `false` if the user wishes so, and several fixes. You can find all the details in the [release announcement](https://blog.mathieui.net/en/poezio-0-16.html).

{{< figure src="/images/newsletter/2026-04-05/poezio-moderate.png" caption="Moderated message retraction testing in Poezio" >}}

- [Profanity](https://profanity-im.github.io/) has released version [0.17.0](https://github.com/profanity-im/profanity/releases/tag/0.17.0) of its console based XMPP client written in C. The release announcement for this version is so long that it spans over 200 lines worth of information, which is a lot more than what we could ever list in here, so please make sure to read the [changelog](https://github.com/profanity-im/profanity/blob/master/CHANGELOG) for all the details!
- [Psi+](https://sourceforge.net/projects/psiplus/) has released version [1.5.2132.0 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) of its development branch of the [Psi](https://sourceforge.net/projects/psi/) XMPP client.
- [Wimsy](https://github.com/dwd/Wimsy/blob/main/README.md) has released version [0.0.5](https://github.com/dwd/Wimsy/releases/tag/v0.0.5) of it cross-platform XMPP client built with Flutter.
- [xmpp-web](https://github.com/nioc/xmpp-web/blob/master/README.md) has released version [0.12.0](https://github.com/nioc/xmpp-web/releases/tag/0.12.0) of its lightweight web chat client for XMPP server. You can read the intermediate changelog from [0.11.0 to 0.12.0](https://github.com/nioc/xmpp-web/compare/0.11.0...0.12.0) for all the details.

### XMPP Servers

- The [Ignite Realtime community](https://www.igniterealtime.org/) is happy to announce the release of [Openfire 5.0.4](https://discourse.igniterealtime.org/t/openfire-5-0-4-release/96411). This release continues the efforts to provide a stable 5.0.x series releases whilst they finalize work on the upcoming 5.1.0 release. Please refer to the [full changelog](https://download.igniterealtime.org/openfire/docs/latest/changelog.html) for all the details or to the intermediate changelog for versions [0.5.3 to 0.5.4](https://github.com/igniterealtime/Openfire/compare/v5.0.3...v5.0.4).
- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) has released [MongooseIM 6.6.0](https://github.com/esl/MongooseIM/releases/tag/6.6.0) with more additions, changes and fixes than what we can reasonably list in here! Make sure to read the [changelog](https://github.com/esl/MongooseIM/blob/master/CHANGELOG.md) for all the details!
- [ProcessOne](https://www.process-one.net/) is pleased to announce another bugfix release: [ejabberd 26.03](https://www.process-one.net/blog/ejabberd-26-03/). This brings support for roster pre-approval, and more than 100 commits with bugfixes all around, many of them dedicated to the new mod_invites, including also many security fixes. Make sure to read the [changelog](https://www.process-one.net/blog/ejabberd-26-03/#a-namechangeloga-changelog) for all the details and a complete list of fixes and improvements on this release.

### XMPP Libraries & Tools

- [matridge](https://codeberg.org/slidge/matridge/src/branch/main/README.md), the [Matrix](https://matrix.org/) to XMPP gateway based on [Slidge](https://slidge.im/) and [nio](https://matrix-nio.readthedocs.io/en/latest/), versions [0.3.3](https://codeberg.org/slidge/matridge/releases/tag/v0.3.3) has been released. You can read the intermediate changelog from [0.3.2 to 0.3.3](https://codeberg.org/slidge/matridge/compare/v0.3.2...v0.3.3) for all the details.
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md), the cross-platform C++ XMPP client and server library, versions [1.14.4](https://invent.kde.org/libraries/qxmpp/-/tags/v1.14.4) and [1.14.5](https://invent.kde.org/libraries/qxmpp/-/tags/v1.14.5) have been released. Full details on the [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md).
- [Rusty-Filer](https://codeberg.org/thomas.leister/rusty-filer/src/branch/develop/README.md), an external XMPP file server for HTTP uploads. An alternative to the internal HTTP file servers of Ejabberd and Prosody, written in Rust, version [1.0.0](https://codeberg.org/thomas.leister/rusty-filer/releases/tag/v1.0.0) has been released.
- [Siltamesh](https://codeberg.org/tpikonen/siltamesh/src/branch/main/README.md), a simple bridge between [Meshtastic](https://meshtastic.org/) and XMPP networks, version [0.2.0](https://codeberg.org/tpikonen/siltamesh/src/tag/0.2.0) has been released.
- [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp/src/branch/main/README.md), the [WhatsApp](https://www.whatsapp.com/) to XMPP gateway based on [Slidge](https://slidge.im/) and [whatsmeow](https://github.com/tulir/whatsmeow/blob/main/README.md), version [0.3.11beta1](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.11beta1) has been released. You can read the intermediate changelog from [0.3.10 to 0.3.11beta1](https://codeberg.org/slidge/slidge-whatsapp/compare/v0.3.10...v0.3.11beta1) for all the details.
- [slidgnal](https://codeberg.org/slidge/slidgnal/src/branch/main/README.md), a [feature-rich](https://slidge.im/docs/slidgnal/main/user/features.html) [Signal](https://signal.org/) to XMPP puppeteering [gateway](/extensions/xep-0100.html), based on [slidge](https://slidge.im/) and [signalmeow](https://github.com/mautrix/signal/tree/main/pkg/signalmeow), version [0.3.0beta10](https://codeberg.org/slidge/slidgnal/releases/tag/v0.3.0beta10) has been released. You can read the intermediate changelog from [0.3.0beta9 to 0.3.0beta10](https://codeberg.org/slidge/slidgnal/compare/v0.3.0beta9...v0.3.0beta10) for all the details.
- [Slixmpp](https://codeberg.org/poezio/slixmpp/src/branch/master/README.rst), the MIT licensed XMPP library for Python 3.7+ version [1.14.1](https://codeberg.org/poezio/slixmpp/releases/tag/slix-1.14.1) has been released. You can read the official [release announcement](https://blog.mathieui.net/en/slixmpp-1-14.html) for all the details.
- [Xepher](https://github.com/ekollof/xepher/blob/master/README.md), a plugin written in C++23 that adds full XMPP support to [WeeChat](https://weechat.org/). It targets [XEP-0459](/extensions/xep-0459.html) (XMPP Compliance Suite 2022) and implements a broad set of modern XEPs — including [XEP-0384](/extensions/xep-0384.html) (OMEMO encryption), [XEP-0313](/extensions/xep-0313.html) (Message Archive Management), [XEP-0363](/extensions/xep-0363.html) (HTTP file upload), [XEP-0472](/extensions/xep-0472.html) (Pubsub Social Feed) microblogging via PubSub, and more.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- [Explicit Mentions](/extensions/inbox/explicit-mentions.html)
  - This specification defines a way to explicitly mention a person or groups of people.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 0.2.1 of [XEP-0461](/extensions/xep-0461.html) (Message Replies)
  - Update the example to use the correct fallback namespace. (mye)
- Version 0.1.1 of [XEP-0473](/extensions/xep-0473.html) (OpenPGP for XMPP Pubsub)
  - Fix inconsistency between text and example; it's the `key` attribute that carries the shared secret ID (formerly it was `secret`). (jp)
- Version 0.1.1 of [XEP-0493](/extensions/xep-0493.html) (OAuth Client Login)
  - Fix reference to [RFC 7628](https://datatracker.ietf.org/doc/rfc7628/) for `SASL OAUTHBEARER` (XEP Editor: dg)
- Version 0.1.1 of [XEP-0511](/extensions/xep-0511.html) (Link Metadata)
  - Added security consideration. Added alt text to example. (spw)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- [Last Call](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/thread/4IF5UK2HVQDRUEV4LINWHUQFBRE2C63U/) for comments on [XEP-0377](/extensions/xep-0377.html) (Blocking Command Reports)
  - This Last Call begins on 2026-03-31 and shall end at the close of business on 2026-04-14.

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
  - To [this issue](/categories/newsletter/): *emus, cal0pteryx, Gonzalo Raúl Nemmi, Ludovic Bocquet, Sairam Bisoyi, XSF iTeam*

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
