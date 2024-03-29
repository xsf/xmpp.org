---
title: The XMPP Newsletter November 2023
date: 2023-12-10
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of November 2023 and will be the last publication for 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcments

### New XSF Board and Council

The XSF members have [voted for a new XSF Board and XSF Council](https://wiki.xmpp.org/web/Meeting-Minutes-2023-11-23). Congratulations to the new Board members Nicola Fabiano, Edward Maurer, Ralph Meijer, Peter Saint-Andre and Matthew Wild. And congratulations to the new Council members Travis Burtrum, Dan Caseley, Daniel Gultsch, Stephen Paul Weber and Marvin Wissfeld.

Please welcome the members to their [new or continuing role](https://xmpp.org/about/xmpp-standards-foundation/)!

### XMPP Summit 26 & FOSDEM 2024

The XSF is planning the XMPP Summit 26, which is to take place on February 1st & 2nd 2024 in Brussels (Belgium, Europe). Following the Summit, the XSF is also planning to be present at FOSDEM 2024, which takes place on February 3rd & 4th 2024. Find all the details in our [Wiki](https://wiki.xmpp.org/web/Conferences/Summit_26). Please sign-up now if you are planning to attend, since this helps organizing. The event is of course open for everyone interested to participate. [Spread the word](https://fosstodon.org/@xmpp/111313123888872184) within your circles!

### XMPP and Google Summer of Code 2023

The XSF [has been a hosting organisation at GSoC in 2023 again, and manages two successful slots for XMPP Contributors](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/). Find the projects for ["Windows Support for Dino"](https://summerofcode.withgoogle.com/programs/2023/projects/ygGSIiHc) and ["Implement group chats in Moxxy"](https://summerofcode.withgoogle.com/programs/2023/projects/UK3oE0f9).

We are planning to participate the next year. The time to reach out to the XMPP community is now :-)

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### XSF Fiscal Hosting Projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month
- [XMPP Italian happy hour](https://tube.nicfab.eu/c/xmpp): monthly Italian XMPP web meeting, starting May 16th and then every third Tuesday of the month at 7:00 PM (online event, with web meeting mode and live streaming).

## Talks

- XMPP Italian Happy Hour Podcast: Dive into the world of XMPP with the Italian Happy Hour podcast, a monthly event derived from recorded video sessions. Each episode is dedicated to the XMPP protocol, offering insights and discussions from enthusiasts and professionals within the community. Whether you're commuting, working out, or simply seeking to listen to interesting conversation, this podcast delivers the essence of Italian XMPP gatherings directly to your ears. Tune in at XMPP Italian Happy Hour Podcast or subscribe to the RSS feed to never miss an episode. Find the [link to podcast](https://open.audio/channels/xmpphappyhour/) and the [link to RSS feed to subscribe the podcast](https://open.audio/api/v1/channels/xmpphappyhour/rss). Plus, join the conversation and keep up with updates by following the podcast page in the Fediverse: @xmpphappyhour@open.audio. The podcast is in Italian but but there may be contributions in English.

## Articles

- [Automating the automatable](https://providers.xmpp.net/blog/2023-11-22-xmpp-providers-automation/): During the past year, the team behind the [XMPP Providers project](https://providers.xmpp.net/) worked on automating the process of gathering data about XMPP providers. Automating this process reduces manual work significantly (for example, checking websites by hand, verifying information, listing sources, etc.) and helps to sustain the team’s efforts. Automation also enables the project to be up to date - every day! A [suite of tools](https://invent.kde.org/melvo/xmpp-providers/-/blob/master/TOOLS.md#automation) has been developed since, providing the ability to query properties via XMPP and through the web. All of these tools are working together in a GitLab pipeline, which runs every night to keep the data up to date.
- [Planned downtime + Happy 10th anniversary, yax.im!](https://yaxim.org/blog/2023/11/27/happy-10th-yax_im/) by Georg Lukas, discussing about the last ten years evolution of yaxim and what's next.
- [Automatic schema update in ejabberd](https://www.process-one.net/blog/automatic-schema-update-in-ejabberd/) by Jérôme Sautret: Previously, if you were using ejabberd with an external relational database, you might have to manually apply some schema changes that come with new features when you upgrade to a new ejabberd release. ejabberd can now handle this schema upgrade automatically. This articles discuss about this feature.
- [Software is Political](https://blog.samwhited.com/2023/11/software-is-political/) by SamWhited: adapted from closing remarks of an XMPP talk at FOSSY, this article discuss about why SamWhited thinks to use as a universal standardized chat protocol is the correct choice.
- [The Power of Green Coding: Erlang and Elixir Leading the Charge](https://www.erlang-solutions.com/blog/the-power-of-green-coding/) by Simon El Nahas: In the era of the green revolution, Erlang and Elixir languages are helping industries reduce server consumption and minimise environmental impact. Here are some industry examples demonstrating this.
- Italian XMPP-IT Community - they have a website now: [www.xmpp-it.net](https://www.xmpp-it.net), a group chat: [xmpp-it@conference.xmpp-it.net](xmpp:xmpp-it@conference.xmpp-it.net?join), they also have a Git to share, create and develop software, configurations and documents concerning the XMPP protocol: [git.xmpp-it.net](https://git.xmpp-it.net), and finally created a wiki for documentation in Italian: [wiki.xmpp-it.net](https://wiki.xmpp-it.net). There is a first translated  [guide](https://www.xmpp-it.net/2023/11/11/roughnecks/xmpp-snikket/) in Snikket.

## Software News

### Clients and Applications

- [Gajim 1.8.3](https://gajim.org/post/2023-11-06-gajim-1.8.3-released/) and [1.8.4](https://gajim.org/post/2023-11-26-gajim-1.8.4-released/) have been released. These releases come with improvements for the profile window, fail-safes for anonymous accounts, usability improvements, and several fixes.
- [Psi+ 1.5.1653](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) has been released.
- [Libervia](https://libervia.org) has received new funding from NLnet/NGI0 for the development of an email-XMPP gateway. This project will enable the conversion of email messages to XMPP and vice versa, including the transformation of mailing lists into pubsub-based forums. Enhancements in Libervia will include UI/UX improvements, end-to-end encryption, and advanced handling of attachments. More details on the project are available [here](https://nlnet.nl/project/EmailXMPPgateway/).
- [monocles chat 1.7.7.5](https://f-droid.org/en/packages/de.monocles.chat/) has been released and got several fixes and improvements like the re-implementation of stickers or a DNSSEC and DANE check shown in the interface. Also an option to enforce DANE and further improvements in the latest Beta [1.7.8](https://codeberg.org/monocles/monocles_chat/releases/tag/Codeberg-beta-v1.7.8).

### Servers

- [Openfire 4.8.0 Beta](https://discourse.igniterealtime.org/t/openfire-4-8-0-beta-release/93338) with a lot of security improvements...
- [Openfire plugin maintenance release galore!](https://discourse.igniterealtime.org/t/openfire-plugin-maintenance-release-galore/93347)
- [New Openfire plugin: Reporting Account Affiliations](https://discourse.igniterealtime.org/t/new-openfire-plugin-reporting-account-affiliations/93360)
- [More Openfire plugin maintenance releases!](https://discourse.igniterealtime.org/t/more-openfire-plugin-maintenance-releases/93369)
- [External Service Discovery plugin 1.0.2 released!](https://discourse.igniterealtime.org/t/external-service-discovery-plugin-1-0-2-released/93351)
- [REST API Openfire plugin 1.10.2 released!](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-10-2-released/93343)

### Libraries & Tools

- [nbxmpp 4.5.1](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/4.5.1), [4.5.2](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/4.5.2) and [4.5.3](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/4.5.3) have been released and come with bug fixes.
- [Smack 4.4.7](https://discourse.igniterealtime.org/t/smack-4-4-7-released/93357) has been released

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- No XEPs proposed this month.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- No XEPs updated this month.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- [Community Code of Conduct](https://xmpp.org/extensions/xep-0458.html)
  - This document describes the XMPP Standard Foundation's Code of Conduct. This Last Call begins today and shall end at the close of business on 2023-11-30.

### Stable

- No XEP moved to stable this month.

### Deprecated

- No XEP deprecated this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Twitter](https://twitter.com/xmpp)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Federico, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, XSF iTeam**
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
  - Translators: **Jeybe, wh0nix**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: **nicola**
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Translators: **daimonduff, TheCoffeMaker**

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

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
