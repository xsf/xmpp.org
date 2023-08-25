---
title: The XMPP Newsletter August 2023
date: 2023-09-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of August 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

### XMPP and Google Summer of Code 2023

The XSF has been [accepted again as hosting organisation at the GSoC 2023 and receive two slots for XMPP Contributors](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/)!

On Dino:

- [Windows support for Dino](https://hrxi.github.io/gsoc/blog/windows-support-for-dino)
- [Windows woes](https://hrxi.github.io/gsoc/blog/windows-woes)

On Moxxy:

- The [first blog post](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), detailing the plan to implement basic group chat functionality.
- The [second blog post](https://moxxy.org/posts/2023-06-17-XEP-0045-In-Moxxmpp.html), describing the plans to bring a basic implementation of [XEP-0045](https://xmpp.org/extensions/xep-0045.html) into Moxxy’s XMPP library moxxmpp.
- The [third blog post](https://moxxy.org/posts/2023-07-24-Join-MUC-With-Moxxy.html), sketching the frontend implementation plan.
- The [fourth blog post](https://moxxy.org/posts/2023-08-20-Moxxy-MUC-GSoC-Final-Report.html), concluding with Moxxy's completed MUC support.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month
- [XMPP Italian happy hour](https://tube.nicfab.eu/c/xmpp): monthly Italian XMPP web meeting, starting May 16th and then every third Tuesday of the month at 7:00 PM (online event, with web meeting mode and live streaming).
- [TroLUG XMPP Workshop](http://trolug.de/termine.html) The TroLUG organizes the second workshop on XMPP in German language on 2023-09-07. It takes place as audio conference via BBB. All nice people are invited to join the workshop.

## Videos

There has been an XMPP track at [FOSSY2023](https://2023.fossy.us/schedule/) with many talks:

- [XMPP Connectivity & Security](https://archive.org/details/fossy2023_XMPP_Connectivity__Security) is an introduction about XMPP connectivity XEPs like XEP-0368 (Direct TLS), XEP-0467 (QUIC), XEP-0468 (WebSocket S2s) and the internals of xmpp-proxy, a forward+reverse proxy, and others.
- [XMPP Introduction and Overview](https://archive.org/details/fossy2023_XMPP_Introduction_and_Overview) is a brief history and introduction to the XMPP protocol for people with small background in programming.
- [My XMPP Past, Present, and Future](https://archive.org/details/fossy2023_My_XMPP_Past_Present_and_Futur) is a point-of-view journey through the evolution of the XMPP ecosystem from 2004. It explains how it was affected by major events such as the decline of traditional IM services, the beginning of the smartphone era and new chat services, and more.
- [Building open standards-based ecosystems](https://archive.org/details/fossy2023_Building_open_standardsbased_e) is a talk about how XMPP as both a community and a protocol adapted to change, and the role that the XSF played in its continuity, but also a general discussion about sustainability of open ecosystems and open networks.

## Articles

- No articles this month.

## Software news

### Clients and applications

- [Converse 10.1.6](https://github.com/conversejs/converse.js/releases/tag/v10.1.6) has been published. It fixes two graphical bugs.
- [Gajim 1.8.1](https://dev.gajim.org/gajim/gajim/-/releases/1.8.1) is available with many bugfixes. Note that Gajim's OMEMO plugin was integrated into Gajim's core with Gajim 1.8.0. You don't need the plugin anymore.
- [monocles chat 1.7.3](https://codeberg.org/Arne/monocles_chat/releases/tag/v1.7.3) is available on f-droid with some fixes and many new features from Cheogram.
- [Profanity 0.14.0](https://github.com/profanity-im/profanity/releases/tag/0.14.0) has been released.
- [State of Snikket 2023: The Apps](https://snikket.org/blog/state-of-snikket-2023-the-apps/).

{{< figure src="/images/newsletter/2023-09-05/snikket-logo.png" caption="Snikket - Chat that is simple, secure, and private" width="200" alt="Snikket Logo" >}}

### Servers

- [Metronome IM 4.0.3](https://github.com/maranda/metronome/releases/tag/v4.0.3) has been released.

### Libraries & Tools

- [libstrophe 0.12.3](https://github.com/strophe/libstrophe/releases/tag/0.12.3) has been released.
- [python-nbxmpp 4.3.2](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/4.3.2) and [4.3.3](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/4.3.3) have been released and come with bug fixes.
- [XMPP Providers](https://providers.xmpp.net) got a new [web bot](https://fosstodon.org/@xmpp_providers/110802431627220360) and an [XMPP bot](https://fosstodon.org/@xmpp_providers/110968568856872183) keeping several provider properties up-to-date.

{{< figure src="/images/newsletter/2023-09-05/xmpp-providers-logo.png" caption="XMPP Providers - Which XMPP provider suits you best? It’s your choice." width="150" alt="XMPP Providers Logo" >}}

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- [MUC Token Invite](https://xmpp.org/extensions/inbox/muc-token-invite.html)
  - This specification provides a way to generate tokens to invite users to a MUC room.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- [Version 0.2.1 of XEP-0458 (Community Code of Conduct)](https://xmpp.org/extensions/xep-0458.html)
  - Add anchors to every section, for easier linking.  Also fix a typo. (egp)
- [Version 0.4.1 of XEP-0333 (Chat Markers)](https://xmpp.org/extensions/xep-0333.html)
  - Changed discovery example to use client JIDs. (gdk)
- [Version 1.1.0 of XEP-0459 (XMPP Compliance Suites 2022)](https://xmpp.org/extensions/xep-0459.html)
  - Replace deprecated XEP-0411 with XEP-0402 in Advanced Group Chat. (egp)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- No XEP moved to stable this month.

### Deprecated

- No XEP deprecated this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Twitter](https://twitter.com/xmpp)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance](https://community.xmpp.net/)
- [Reddit](https://www.reddit.com/r/xmpp/)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Jonas Stein, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), nicola, XSF iTeam**
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
