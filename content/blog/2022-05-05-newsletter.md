---
title: The XMPP Newsletter April 2022
author: XMPP Communication Team and Contributors
date: 2022-05-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of April 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
- Italian: [nicfab.it](https://www.nicfab.it/)
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)

## XSF Announcements

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

- The XSF has been accepted as hosting organization at [Google Summer of Code 2022 (GSoC)](https://xmpp.org/community/gsoc-2022/).
- XMPP Newsletter via mail: We migrated to our [own mail-list server](https://mail.jabber.org/mailman/listinfo/newsletter) and stopped using Tinyletter. Its read-only and you will receive the XMPP Newsletter on a monthly basis. It also eliminates the privacy concerns with Tinyletter.

## XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

The [Mellium Dev Communiqué for March 2022](https://opencollective.com/mellium/updates/dev-communique-for-march-20222) has been released! This release includes changes to the sidebar in the Communiqué TUI client and improvements to various packages in the main mellium.im/xmpp module.

## Software news

### Clients and applications

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

[Go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp) version [v0.4.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.4.0) with experimental Ox (OpenPGP for XMPP) support has been released.

## Servers

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

## Libraries

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   No XEPs proposed this month.

### New

-   Version 0.1.0 of [XEP-0462](https://xmpp.org/extensions/xep-0462.html) (PubSub Type Filtering)
    -   Accepted by vote of Council on 2022-02-09.

-   Version 0.1.0 of [XEP-0463](https://xmpp.org/extensions/xep-0463.html) (MUC Affiliations Versioning)
    -   Accepted by vote of Council on 2022-02-16.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 1.6.0 of [XEP-0115](https://xmpp.org/extensions/xep-0115.html) (Entity Capabilities)
    -   Mention preimage attacks explicitly (ssw)

-   Version 1.4.0 of [XEP-0156](https://xmpp.org/extensions/xep-0156.html) (Discovering Alternative XMPP Connection Methods)
    -   Remove DNS `_xmppconnect` method due to security vulnerability. (tjb)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   No Last Call this month.

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

-   No XEPs advanced to Stable this month.

### Deprecated

-   No XEP deprecated this month.

### Obsoleted

-   [XEP-0008](https://xmpp.org/extensions/xep-0008.html) (IQ-Based Avatars)
    -   Obsoleted due to two superseding specifications (egp)

-   [XEP-0038](https://xmpp.org/extensions/xep-0038.html) (Icon Styles)
    -   Obsolete due to the omnipresence of Unicode emoji, as well as Bits of Binary stickers. (egp)

-   [XEP-0051](https://xmpp.org/extensions/xep-0051.html) (Connection Transfer)
    -   Obsolete because this feature has been merged into XMPP core, see RFC6120 section 4.9.3.19, which describes the <see-other-host/> stream error. (egp)

-   [XEP-0138](https://xmpp.org/extensions/xep-0138.html) (Stream Compression)
    -   Obsolete due to security vulnerability. (tjb)

-   [XEP-0229](https://xmpp.org/extensions/xep-0229.html) (Stream Compression with LZW)
    -   Obsolete due to security vulnerability. (tjb)

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Spread the news!

Please share the news on other networks:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

Here you can [subscribe via email](https://mail.jabber.org/mailman/listinfo/newsletter). It is read-only and only the Newsletter will be send to you on a monthly basis.

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, MattJ, nicfab, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat, Ysabeau, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

Each month's newsletter issue is drafted in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
