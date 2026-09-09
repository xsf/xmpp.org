---
title: The XMPP Newsletter August 2026
date: 2026-09-09
categories: ['Newsletter']
summary: "In this issue: XMPP at LinuxDays and OmniOpenCon. Quicksy App has been removed. Read about 25 years of XMPP and Slidge.im security audit. New XMPP clients and operators are rising. And updates on four specifications."
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of August 2026.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/) and contributors of the XMPP community.

Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors. If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

## XMPP Events

- The [di.day](https://di.day/en) takes place every [first Sunday of the month](https://fosstodon.org/@xmpp/116867255827209479) where the XMPP community also [promotes their solutions](https://di-day.xmpp.link/)! di.day is a mainly German initiative to help people switch to open-source and privacy-friendly solutions.
- There will be an XMPP stand at the [LinuxDays](https://www.linuxdays.cz/2026/) conference in Prague during the first weekend of October. You can also vote for XMPP-related lectures during the first week of September.
- [XMPP stand at OmniOpenCon](xmpp.org/2026/08/xmpp-stand-at-omniopencon/) in Bucharest, Romania, too. From 16th - 17th October 2026.

## Videos and Talks

- [Quicksy ist aus den App Stores verschwunden... was nun?](https://makertube.net/w/71fFhdnpVHBg5bhchUAs9d), by [eversten.net](https://makertube.net/a/eversten.net/video-channels) for [XMPP Tutorials DE](https://makertube.net/c/xmpp_tutorials_de/videos). [DE]
- [Von Quicksy zu Conversations (Schnellanleitung)](https://makertube.net/w/g6yGQSZvghvHvsLSjzLKpy), by [eversten.net](https://makertube.net/a/eversten.net/video-channels) for [XMPP Tutorials DE](https://makertube.net/c/xmpp_tutorials_de/videos). [DE]

## XMPP Articles

- [Coming home to Jabber](https://www.the-sprawl.blog/2026/08/03/coming-home-to-jabber.html), by [TabTwo](https://fedi.mayer.rocks/@ralph) for [the Sprawl blog](https://www.the-sprawl.blog/).
- [Admin Benachrichtigungen via XMPP](https://blog.dohdom.de/xmpp/prosody-certs/), from [Rainer's Blogseiten](https://blog.dohdom.de/). [DE]
- [Una alternativa fiable a Whastapp para chatear con privacidad](https://www.lentetisquesusa.com/2026/08/06/una-alternativa-fiable-a-whastapp-para-chatear-con-privacidad/), by David Palacios for [Lente Tisquesusa](https://www.lentetisquesusa.com/about/). [ES]
- [Teaching an Old Dog New Tricks: Forgejo + XMPP](https://マリウス.com/teaching-an-old-dog-new-tricks-forgejo-xmpp/), from [マリウス.com](https://マリウス.com/).
- [Eu quero acreditar](https://blog.isacloud.im/eu-quero-acreditar/), by [isadora](https://blog.isacloud.im/author/isadora/) for the [isaCloud diario-de-bordo](https://blog.isacloud.im/category/diario-de-bordo/). [PT_BR]
- [Slidge got a security audit](https://slidge.im/blog/2026/08/20/security-audit/), from [slidge.im blog](https://slidge.im/blog/)
- [Jabber/XMPP: 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/), by [Daniel Gultsch](https://gultsch.de/).
- [XMPP ha 25 anni: perché la messaggistica aperta non è mai davvero morta](https://www.ilsoftware.it/xmpp-compie-25-anni-torna-attuale-messaggistica-aperta/), by [Michele Nasi](https://www.ilsoftware.it/author/michele/) for [ilsoftware.it](https://www.ilsoftware.it/). [IT]
- [Libervia on building an all-in-one communication platform grounded in the right to privacy](https://www.apc.org/en/news/libervia-building-all-one-communication-platform-grounded-right-privacy), by Xavier Coadic for [Association for Progressive Communications (APC)](https://www.apc.org/en).
- [Tubercule](https://tubercule.fr/), a collective of hackers and hackerettes from the Rennes region (France) that wants to be [inclusive and accessible](https://tubercule.fr/objectif-et-code-de-conduite), announced the availability of their [newly implemented XMPP instance](https://toot.aquilenet.fr/@tubercule/117167501923788204) for those of you in Rennes or around! The announcement came along with a really handy [guide](https://tubercule.fr/guide/compte-messagerie-xmpp) (which will evolve over time), that also adds plain and simple instructions on how to get in touch with them and get an account. Have fun! [FR]

## Software news

### Clients and applications

- [aTalk](https://github.com/cmeng-git/atalk-android/blob/master/README.md) has released version [6.5.0](https://github.com/cmeng-git/atalk-android/releases/tag/6.5.0) of its encrypted instant messaging with video call and GPS features for Android. This release brings a lot of improvements, quite a few fixes and some really heavy work 'under the hood'. Please refer to the [release notes](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt) for all the details.
- [Gajim](https://gajim.org/) has released version [2.6.0](https://gajim.org/posts/2026-08-27-gajim-2.6.0-released/) of its free and fully featured chat app for XMPP. Gajim now adapts responsively to window size changes. This release comes with many small improvements and bugfixes. Thank you for all your contributions!
- [Introducing Livewire](https://git.agnos.is/projectmoon/livewire/src/branch/master/README.md): an alpha-quality native XMPP client for [Ubuntu Touch](https://ubports.com/), written in [Rust](https://rust-lang.org/) on top of [tokio-xmpp](https://gitlab.com/xmpp-rs/xmpp-rs/-/blob/main/tokio-xmpp/README.md) and [xmpp-parsers](https://gitlab.com/xmpp-rs/xmpp-rs/-/blob/main/parsers/README.md).
- [Introducing Mynah](https://mynah.starlightnet.work/): an XMPP client using [Python](https://www.python.org/), [GTK](https://gtk.org/), and [slixmpp](https://codeberg.org/poezio/slixmpp). It has a long-term vision of being maximally customisable, user-friendly, and cross-platform (Linux, Windows, macOS).

### Servers

- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) has released versions [6.8.0](https://github.com/esl/MongooseIM/releases/tag/6.8.0) and [6.8.1](https://github.com/esl/MongooseIM/releases/tag/6.8.1) of their enterprise instant messaging solution. You can read all the details in the [changelog](https://github.com/esl/MongooseIM/blob/master/CHANGELOG.md).
- The [Ignite Realtime community](https://www.igniterealtime.org/) is pleased to announce the release of [Openfire 5.1.2](https://discourse.igniterealtime.org/t/openfire-5-1-2-release/96560), a maintenance update to the open-source XMPP real-time communication server. Head over to the [full changelog](https://download.igniterealtime.org/openfire/docs/latest/changelog.html) for all the details!
- The [Prosody App](https://github.com/YunoHost-Apps/prosody_ynh) for [Yunohost](https://yunohost.org/) has been updated to provide a configuration panel, to give an easy access to the most relevant parameters from the web interface!
- Enthousiasts from New Zealand [announced](https://unsociable.lowkey.party/@nigel/statuses/01M0NZRW1ET37YXMH2TTXF5FG5) a new local XMPP server for "Kiwis": [xmpp.nz](https://xmpp.nz/)

### Libraries & Tools

- [Introducing xmpp-translate-bot](https://github.com/Riverfount/xmpp-translate-bot/blob/main/README.md), a translation bot for XMPP (MUC) that makes use of a selfhosted [LibreTranslate](https://libretranslate.com/) instance as a backend for language detection and translation. [PT_BR]
- [jabber.el](https://git.thanosapollo.org/emacs-jabber/about/), the XMPP client for [Emacs](https://www.gnu.org/software/emacs/), versions [0.13.0](https://git.thanosapollo.org/emacs-jabber/tag/?h=0.13.0), [0.13.1](https://git.thanosapollo.org/emacs-jabber/tag/?h=0.13.1) and [0.13.2])(https://git.thanosapollo.org/emacs-jabber/tag/?h=0.13.2) have been released. Full details on the [changelog](https://git.thanosapollo.org/emacs-jabber/tree/CHANGELOG.org).
- [libomemo.js](https://github.com/conversejs/libomemo.js/blob/master/README.md), a [TypeScript](https://www.typescriptlang.org/) implementation of the [OMEMO Multi-End Message and Object Encryption](/extensions/attic/xep-0384-0.3.0.html) protocol for XMPP, version [3.0.0](https://github.com/conversejs/libomemo.js/releases/tag/v3.0.0) has been released. Once again, the list of changes is larger and has more details and notices on breaking changes that what could mention in here. Please refer to the full [changelog](https://github.com/conversejs/libomemo.js/blob/master/CHANGELOG.md) for all the details.
- [matteridge](https://codeberg.org/slidge/matteridge#readme), the [Mattermost](https://mattermost.com/) to XMPP gateway based on [Slidge](https://slidge.im/) and [mattermost-api-reference-client](https://git.sr.ht/~nicoco/mattermost-api-reference-client), version [0.4.1](https://codeberg.org/slidge/matteridge/releases/tag/v0.4.1) has been released. You can check the changelog from [0.4.0 to 0.4.1](https://codeberg.org/slidge/matteridge/compare/v0.4.0...v0.4.1) for all the details.
- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md), a Python library that provides a way for Python applications to use the XMPP network, version [7.4.0](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/7.4.0) has been released. Full details on the [changelog](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- [slidcord](https://codeberg.org/slidge/slidcord#readme), the [Discord](https://discord.com/) to XMPP gateway based on [Slidge](https://slidge.im/) and [discord.py-self](https://discordpy-self.readthedocs.io/en/latest/), version [0.4.1](https://codeberg.org/slidge/slidcord/releases/tag/v0.4.1), has been released. You can check the intermediate changelog from [0.4.0 to 0.4.1](https://codeberg.org/slidge/slidcord/compare/v0.4.0...v0.4.1) for all the details.
- [slidgram](https://codeberg.org/slidge/slidgram#readme), the [Telegram](https://telegram.org/) to XMPP gateway based on [Slidge](https://slidge.im/) and [Pyrofork](https://pyrofork.wulan17.dev/main/), version [0.4.1](https://codeberg.org/slidge/slidgram/releases/tag/v0.4.1), has been released. You can check the changelog from [0.4.0 to 0.4.1](https://codeberg.org/slidge/slidgram/compare/v0.4.0...v0.4.1) for all the details.
- [xmpp-dns](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/README.md), a CLI tool to check XMPP SRV records, version [0.6.4](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.6.4) has been released. Full details on the [changelog](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/CHANGELOG.md).


## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- No proposed XEPs this month.

### New

- Version 0.1.0 of [XEP-0518](/extensions/xep-0518.html) (Payment Required)
  - Accepted as Experimental by council vote on 2026-07-07 (XEP Editor(dg))

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.6 of [XEP-0066](/extensions/xep-0066.html) (Out of Band Data)
  - Twenty years later, strike section 6's SI suggestion (dwd)
- Version 1.1.5 of [XEP-0084](/extensions/xep-0084.html) (User Avatar)
  - Fix inconsistent hash in the example with multiple data sources for the same file. (nc)
- Version 1.1.0 of [XEP-0490](/extensions/xep-0490.html) (Message Displayed Synchronization)
  - Add security consideration for sender verification of PEP notifications. (dg)
- Version 0.1.1 of [XEP-0515](/extensions/xep-0515.html) (TLS Channel-Binding Downgrade Protection)
  - Fixed typo in Bind 2 namespace (XEP Editor (dg))

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No XEPs last calls this month.

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
- [Reddit](https://www.reddit.com/r/xmpp/)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers and more languages are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- Contributors:
  - To [this issue](/categories/newsletter/): *cal0pteryx, emus, Gonzalo Raúl Nemmi, Ludovic Bocquet, poVoq, XSF iTeam*

- Translations:
  - [French](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, seveso, Ysabeau*
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
