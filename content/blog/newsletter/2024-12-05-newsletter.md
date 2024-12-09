---
title: The XMPP Newsletter November 2024
date: 2024-12-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of November 2024.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XMPP Summit 27 & FOSDEM 2025
The XSF is planning the XMPP Summit 27, which is to take place on January 30th & 31st 2025 in Brussels (Belgium, Europe). Following the Summit, the XSF is also planning to be present at [FOSDEM 2025](https://fosdem.org/2025/), which takes place on February 1st & 2nd 2025. Find all the details in our [Wiki](https://wiki.xmpp.org/web/Conferences/Summit_27). Please sign-up now if you are planning to attend, since this helps organizing. The event is of course open for everyone interested to participate. Spread the word within your circles!

### XSF Fiscal Hosting Projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects you can support:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav iOS](https://opencollective.com/prav-ios)
- [diasp.in](https://opencollective.com/diasp-in)

## XMPP Events

- [Berlin XMPP Meetup](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) (DE / EN): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month at 6pm local time
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) [IT]: monthly Italian XMPP web meeting, every third Monday of the month at 7:00 PM local time (online event, with web meeting mode and live streaming).

## XMPP Articles

- ProcessOne
  - [Docker: set up ejabberd and keep it updated automagically with Watchtower](https://www.process-one.net/blog/docker-ejabberd-watchtower/)
- Erlang Solution
  - [MongooseIM 6.3: Prometheus, CockroachDB and more](https://www.erlang-solutions.com/blog/mongooseim-6-3-prometheus-cockroachdb-and-more/)
- [XMPP: the forgotten gem of Instant Messaging](https://adele.pages.casa/md/blog/xmpp-the-forgotten-gem-of-instant-messaging.md). A well thoughtout exploration on XMPP, why hasn't it reached widespread adoption, why it remains relevant, and how it might be the best option for those seeking a flexible, secure, and open-source messaging tool.
- [The Quick and Easy Guide to Jabber/XMPP](https://contrapunctus.codeberg.page/the-quick-and-easy-guide-to-xmpp.html)
- [XMPP For Browsers](https://portal.mozz.us/gemini/woodpeckersnest.space/~schapps/journal/2024-11-28-xmpp-for-browsers.gmi): An idea for developing browser software with XMPP [PubSub](https://xmpp.org/extensions/xep-0060.html).
- [Facile guida per chattare con XMPP](https://orgs.noblogs.org/it/post/2024/11/25/facile-guida-per-chattare-con-xmpp/) [IT]: An easy guide on how to chat using XMPP (also available in [English](https://orgs.noblogs.org/post/2024/11/25/easy-guide-for-chatting-with-xmpp/))

## XMPP Software News

### XMPP Clients and Applications

- [Conversations](https://conversations.im/) has released versions [2.17.3](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.17.3) and [2.17.4](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.17.4) for Android.
- [Monocles Chat 2.0.2](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.2) has been released. This version brings MiniDNS, settings export, fixes and more!.
- [Monal](https://monal-im.org/) has released version [6.4.6](https://github.com/monal-im/Monal/releases/tag/Build_iOS_989) for iOS an macOS.
- [Cheogram](https://cheogram.com/) has released version [2.17.2-2](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.17.2-2) for Android. This release brings a chat requests feature to hide possible SPAM, with an option to report all. Additionally, it comes with several improvements and bugfixes. Also worth noting, since this last November, Cheogram is once again available for download from the Google Play Store!

{{< figure src="/images/newsletter/2024-12-05/cheogram.png" caption="Cheogram 2.17.2-2 navigation drawer with account and tag filters and SPAM control, featuring the option report all." >}}

### XMPP Servers

- [Openfire 4.9.1](https://discourse.igniterealtime.org/t/openfire-4-9-1-release/94857) and [4.9.2](https://github.com/igniterealtime/Openfire/releases/tag/v4.9.2) have been released. Version [4.9.1](https://github.com/igniterealtime/Openfire/releases/tag/v4.9.1) is a bugfix and maintenance release, whereas version [4.9.2](https://github.com/igniterealtime/Openfire/releases/tag/v4.9.2) is a bugfix release. You can read the full [changelog](https://download.igniterealtime.org/openfire/docs/latest/changelog.html) for more details.
- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) version [6.3.0](https://github.com/esl/MongooseIM/releases/tag/6.3.0) has been released. The main highlight is the complete instrumentation rework, allowing integration with Prometheus. Additionally, CockroachDB has been added to the list of supported databases for increased scalability. See the [release notes](https://github.com/esl/MongooseIM/releases/tag/6.3.0) for more information.
- The [(non-official) Prosody app](https://github.com/anubister/prosody_ynh) for Yunohost has now reached a beta maturity opening it for everybody to test. This variant aims at providing better XMPP support for Yunohost users. In comparison to official Metronome and Prosody apps, this app enables A/V calls working out of the box. An optional import of rosters, MUCs, and bookmarks from Metronome is also provided. As a reminder, Yunohost is a server distribution based on Debian, which makes it easy to host a lot of services (apps) by yourself. Till the last major release (version 12), Metronome was integrated in the core installation, allowing a lot of people to discover XMPP easier (though with some limitations).

### XMPP Libraries & Tools

- [go-xmpp](https://github.com/xmppo/go-xmpp) versions [0.2.5](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.5), [0.2.6](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.6) and [0.2.7](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.7) have been released.
- [go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp) versions [0.12.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.12.0) and [0.12.1](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.12.1) have been released.
- [QXmpp](https://github.com/qxmpp-project/qxmpp) versions [1.9.0](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.9.0) and [1.9.1](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.9.1) have been released.
- [Slidge](https://sr.ht/~nicoco/slidge/) versions [v0.2.1](https://git.sr.ht/~nicoco/slidge/refs/v0.2.1) and [v0.2.2](https://git.sr.ht/~nicoco/slidge/refs/v0.2.2) have been released, bringing quite a few bugfixes.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- No XEPs Proposed this month.

### New

- Version 0.1.0 of [XEP-0496](https://xmpp.org/extensions/xep-0496.html) (Pubsub Node Relationships)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of [XEP-0497](https://xmpp.org/extensions/xep-0497.html) (Pubsub Extended Subscriptions)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of [XEP-0498](https://xmpp.org/extensions/xep-0498.html) (Pubsub File Sharing)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of [XEP-0499](https://xmpp.org/extensions/xep-0499.html) (Pubsub Extended Discovery)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of [XEP-0500](https://xmpp.org/extensions/xep-0500.html) (MUC Slow Mode)
  - Promoted to Experimental (XEP Editor: dg)

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.0.1 of [XEP-0490](https://xmpp.org/extensions/xep-0490.html) (Message Displayed Synchronization)
  - Fix some examples, and their indentation.
  - Add the XML Schema. (egp)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- Version 1.0.0 of [XEP-0490](https://xmpp.org/extensions/xep-0490.html) (Message Displayed Synchronization)
  - Accept as Stable as per Council Vote from 2024-11-05. (XEP Editor (dg)

### Deprecated

- No XEP deprecated this month.

### Rejected

- No XEP rejected this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Twitter](https://twitter.com/xmpp)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers an more languages are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: *Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Schimon Zachary, Simone Canaletti, singpolyma, XSF iTeam*
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: *nicola*
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/])
  - Translators: *Gonzalo Raúl Nemmi*
- German: [xmpp.org](https://xmpp.org/categories/newsletter/])
  - Translators: *Millesimus*

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations
- communication via media accounts

## Unsubscribe from the XMPP Newsletter
To unsubscribe from this list, [please log in first](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/).
If you have not previously logged in, you may need to set up an account with the appropriate email address.

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
