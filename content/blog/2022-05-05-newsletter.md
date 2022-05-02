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
- By the way, have you checked our nice [XMPP RFC page](https://xmpp.org/rfcs/)? :-)

## XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- NEW: [Mellium OMEMO encryption project](https://opencollective.com/mellium/projects/omemo)
- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Community Projects

A new community space for XMPP related projects and individuals has been created in the Fediverse! Join us on our new [Lemmy instance](https://community.xmpp.net/) and chat about all XMPP things! 

Are you looking for an XMPP provider that suits you? There is a [new website](https://providers.xmpp.net) based on the data of [XMPP Providers](https://invent.kde.org/melvo/xmpp-providers). XMPP Providers has a curated list of providers and tools for filtering and creating badges for them. The machine-readable list of providers can be [integrated in XMPP clients](https://providers.xmpp.net/apps/) to simplify the registration. You can [help](https://invent.kde.org/melvo/xmpp-providers/-/blob/master/CONTRIBUTING.md) by improving your website (as a provider), by automating the manual tasks (as a developer), by adding new providers to the list (as an interested contributor). Read the [first blog post](https://providers.xmpp.net/blog/2022-04-25-start-of-xmpp-providers-website/)!

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

The [Mellium Dev Communiqué for March 2022](https://opencollective.com/mellium/updates/dev-communique-for-march-20222) has been released! This release includes changes to the sidebar in the Communiqué TUI client and improvements to various packages in the main mellium.im/xmpp module. The Mellium Dev Communiqué for April 2022 has also been released and can be found over on [Open Collective](https://opencollective.com/mellium/updates/dev-communique-for-april-2022).

Maxime “pep.” Buquet wrote some thoughts regarding _"Deal on Digital Markets Act: EU rules to ensure fair competition and more choice for users"_ in his [Interoperability in a “Big Tech” world](https://bouah.net/2022/04/interoperability-in-a-big-tech-world/) article. In a later article he describes [part of his threat model](https://bouah.net/2022/04/an-overview-of-my-threat-model/), detailing how XMPP comes into play and proposing ways it could be improved.

German "Freie Messenger" [shares some thoughts](https://www.freie-messenger.de/en/begriffe/interoperabilitaet/gedanken) on interoperability and the Digital Markets Act (DMA). They also offer [a comparison of "XMPP/Matrix"](https://www.freie-messenger.de/en/systemvergleich/xmpp-matrix)

## Software news

### Clients and applications

[BeagleIM `5.2`](https://github.com/tigase/beagle-im/releases/tag/5.2) and [SiskinIM 7.2](https://github.com/tigase/siskin-im/releases/tag/7.2) just got released with fixes for OMEMO encrypted message in MUC channels, MUC participants disappearing randomly, and issues with VoIP call sending an incorrect payload during call negotiation.

converse.js publishs version `9.1.0`. I comes with a new dark theme, several improvements of encryption (OMEMO), improvement of stanza timeout, font icons, updated translations and enhancement of the IndexedDB. Find the [release notes](https://github.com/conversejs/converse.js/releases/tag/v9.1.0).

[Gajim Development News](https://gajim.org/post/2022-04-30-development-news-april/): This month came with a lot of preparations for the release of Gajim 1.4 🚀 Gajim’s release pipeline has been improved in many ways, allowing us to make releases more frequently. Furthermore, April brought improvements for file previews on Windows.

[Go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp) version [`v0.4.0`](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.4.0) with experimental Ox (OpenPGP for XMPP) support has been released.

JMP offers international call rates based on a [computing trie](https://blog.jmp.chat/b/2022-computing-call-rates). There are also [new commands and team members](https://blog.jmp.chat/b/april-newsletter-2022).

[Monal `5.1` has been released](https://github.com/monal-im/Monal/releases/tag/Build_iOS_780). This release brings OMEMO support in private group chats, communication notifications on iOS 15, and many improvements.

[PravApp project](https://prav.app/) is a plan to get a lot of people from India to invest small amounts to run an interoperable XMPP-based messaging service that is easier to join and discover contacts, similar to the Quicksy app. Prav will be Free Software, which respects users' freedom. The service will be backed by a cooperative society in India to ensure democratic decision making in which users can take part as well. Users will control the privacy policy of the service.

[Psi+ `1.5.1619` (2022-04-09)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) has been released.

[Poezio `0.14`](https://bouah.net/2022/04/updates-from-the-poezio-ecosystem/) has been released alongside with multiple backend libraries. This new 
release brings in lots of bug fixes and small improvements bu doesn't bring in big new features and shows that even if not perfect, poezio reached a point where devs are mostly happy about. Big changes are coming nonetheless, you will find out in the article. Stay tuned.

<!-- https://bouah.net/2022/04/poezio-full.png -->

[UWPX](https://uwpx.org) ships two small pre-release updates concering a [critical fix](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.41.6.0) for a crash that occurs when trying to render an invalid user avatar and issues with the [Windows Store builds](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.41.5.0). Besides that it also got a minor [UI update](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.42.0.0) this month.

## Servers

Ignite Realtime Community:
* Version `9.1.0` release 1 of the Openfire [inVerse plugin](https://discourse.igniterealtime.org/t/inverse-openfire-plugin-9-1-0-1-released/91560) was released which enables deployment of the third-party Converse client 37 in Openfire.
* Version `4.4.0` release 1 of the Openfire [JSXC plugin](https://discourse.igniterealtime.org/t/jsxc-openfire-plugin-4-4-0-1-released/91559) was released which enables deployment the third-party JSXC client 13 in Openfire.
* Version `1.2.3` of the Openfire [Message of the Day plugin](https://discourse.igniterealtime.org/t/openfire-message-of-the-day-motd-plugin-version-1-2-3-released/91556) was released and it ships with the German translation to the admin console
* Version `1.8.0` of the Openfire [REST API plugin](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-8-0-released/91555/3) was released which adds new endpoints for readiness, liveliness and cluster status.

## Libraries

[slixmpp `1.8.2`](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.8.2) has been released. It fixes RFC3920 sessions, improves certificate errors handling, and adds a plugin for XEP-0454 (OMEMO media sharing).

The mellium.im/xmpp library `v0.21.2` has been released! Highlights include support for [PEP Native Bookmarks](https://xmpp.org/extensions/xep-0402.html), and [entity capabilities](https://xmpp.org/extensions/xep-0115.html). For more information, see the [release announcement](https://opencollective.com/mellium/updates/new-release-mellium-im-xmpp-v0-21-2).

The Mellium Dev Communiqué for April 2022 has also been released and can be found over on [Open Collective](https://opencollective.com/mellium/updates/dev-communique-for-april-2022). The big news this month is that the [OMEMO encryption project](https://opencollective.com/mellium/projects/omemo) has received donations totaling over $100!

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

By the way, xmpp.org features [a new page about XMPP RFCs](https://xmpp.org/rfcs/).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Pubsub Public Subscriptions](https://xmpp.org/extensions/inbox/pubsub-public-subscriptions.html)
    -   This specification provides a way to make subscriptions to a node public
-   [Ephemeral Messages](https://xmpp.org/extensions/inbox/ephemeral-messages-v2.html)
    -   This specification encourages a shift in privacy settings wrt. logging policies.

### New

-   No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 0.4 of [XEP-0356](https://xmpp.org/extensions/xep-0356.html) (Privileged Entity)
    -   Add "iq" privilege (necessary to implement XEPs such as ).
    -   Roster pushes are now transmitted to privileged entity with "roster" permission of "get" or "both". This can be disabled.
    -   Reformulate to specify than only initial stanza and "unavailable" stanzas are transmitted with "presence" pemission.
    -   Namespace bump. (jp)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   No Last Call this month.

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here](https://github.com/xsf/xeps/pull/1100).

-   No XEPs advanced to Stable this month.

### Deprecated

-   No XEP deprecated this month.

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

Here you can [subscribe via email](https://mail.jabber.org/mailman/listinfo/newsletter). It is read-only and only the Newsletter will be send to you on a monthly basis. Or simple via:

<head>
    <style>
        body {padding: 2em;}
        h1 a {text-decoration: none;}
        .post-meta {color: gray;}
    </style>
</head>

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, mathieui, MattJ, nicfab, Pierre Jarillon, Ppjet6, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

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
