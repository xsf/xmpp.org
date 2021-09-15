---
title: The XMPP Newsletter June 2021
author: emus
date: 2021-07-05
categories: ["Newsletter"]
aliases:
    - "/2021/06/newsletter-06-june/"
---

Welcome to the XMPP Newsletter covering the month of June 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. 
If you are happy with the services and software you may be using, especially throughout the current situation, 
please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom.

Other than that - enjoy reading! 

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- The French translation appears at [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- The German translation appears at [anoxinon.de](https://anoxinon.de/blog/)
- The Italian translation appears at [NicFab.it](https://www.nicfab.it/la-newsletter-xmpp-di-marzo-2021-versione-italiana/)

Many thanks to the translators and their work! This is a great help to spread the news! Please join them in their work or start over with another language!

## XSF Announcement

The XMPP Operators Channel is a place primarily for operators of federated XMPP services, to have civil and low-bar discourse and resolution of interoperability issues. While discussions can get further from on-topic there was no written code of conduct or rules until this month. You can read them [here](https://xmpp.org/community/channels/operators) and join if you find the topic interesting.

## Events

[XMPP Office Hours each week](https://wiki.xmpp.org/web/XMPP_Office_Hours) - Also, checkout our new [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of the month.

## Videos

[Demo: ad-hoc commands and data forms in Mellium](https://www.youtube.com/watch?v=C2oyAfJeqno) - Sam Whited demos the new support for [XEP-0050: Ad-Hoc Commands](https://xmpp.org/extensions/xep-0050.html) and [XEP-0004: Data Forms](https://xmpp.org/extensions/xep-0004.html) in the Mellium XMPP library.

## Articles

Axel Reimer published a short installation and configuration guide for Monal 5.0. It is available in [English](https://eversten.net/en/blog/monal/) and [German](https://eversten.net/blog/monal/).

Ingrid’s Space has thoughts on [why decentralised applications don’t work](https://ingrids.space/posts/why-distributed-systems-dont-work/).

Martin Dosch wrote a short blog post about [how to use the "Jabber-ID" email header with neomutt](https://blog.mdosch.de/2021/06/13/jabber-email-header/) [DE]. The setting of this header is also described in the [xmpp.org wiki](https://wiki.xmpp.org/web/Jabber_Email_Header).

Software freedom conservancy [moved their chat from IRC to XMPP](https://sfconservancy.org/blog/2021/jun/21/xmpp-chat/) using [Snikket](https://snikket.org/).

Vaxbot, the XMPP based vaccine bot [has been featured on Canadian National News](https://monal.im/blog/vaxbot-on-canadian-national-news/).

## Software news

### Clients and applications

Blabber.IM XMPP service has been discontinued and has shut down its server. On June 25, the [blabber.im website](https://blabber.im/) reported that they were discontinuing support for their XMPP server due to personal reasons.

In this respect, [MattJ announced](https://mastodon.technology/@mattj/106517206134989817) created a tool for users to migrate their roster and vcards but also subscriptions to another XMPP account. [Find the XMPP account exporter here](https://migrate.modernxmpp.org/).

[Gajim Development News](https://gajim.org/post/2021-06-27-development-news-june/): This month brought some fixes for themes and spell checking. Development on the new Gajim version made a big step forward: file previews are working again and more important they're now a core integrated feature, they look even better while also being privacy respecting for those anonymous chats.

Monal 5.0 [has been released](https://monal.im/blog/monal-with-group-chat-and-voice-messages/), featuring support for group chats (not yet OMEMO encrypted, will come next) and sending voice messages and videos, but also a lot of internal code refactoring and bug fixes.

![Monal Group Chat (MUC)](/images/newsletter/june2021/MonalGroupChat.png "Monal Group Chat (MUC)")

Profanity, a console-based XMPP client, has implemented [attention flags](https://profanity-im.github.io/blog/post/attention-attention/). Use the shortcut ALT+F to toggle the flag.

UWPX [v.0.33.0.0](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.33.0.0) has been released. It includes support for [XMPP Providers](https://invent.kde.org/melvo/xmpp-providers/-/tree/master) for convenient auto-complete and registration of new accounts to XMPP servers. Besides that, this release fixes a few bugs related to stream close and open message parsing.

![UWPX Server Onboarding](/images/newsletter/june2021/UWPX.png "UWPX Server Onboarding")

## Servers

[Jackal](https://github.com/ortuman/jackal), an XMPP server written in Go, released [version 0.54.0](https://github.com/ortuman/jackal/releases/tag/v0.54.0) with support for [XEP-0198: Stream Management](https://xmpp.org/extensions/xep-0198.html), docker compose support, graphana service dashboard and a new fancy logo:

![New Jackal Logo](/images/newsletter/june2021/jackal.png "New Jackal Logo")

[OpenFire 4.6.4 has been released](https://discourse.igniterealtime.org/t/openfire-4-6-4-is-released/90359), bringing some bug fixes.

## Libraries

Have you heard about [qxbridge a Qt XMPP Bridge for Telegram](https://invent.kde.org/lnj/qxbridge/) based on QXmpp.

There is a new [ProtoXEP for for pre-auth key generation](https://xmpp.org/extensions/inbox/preauth-ibr.html), which would allow for fancy new uses, such as [XMPP Self Provisioning with Mastodon](https://github.com/mellium/fediverse-xmpp-onboarding)


## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Pre-auth Registration Key Generation and Validation](https://xmpp.org/extensions/inbox/preauth-ibr.html)
    -   This specification updates XEP-0401 and XEP-0445 by specifying a shared format for the pre-authenticated registration token.

-   [Moved 2.0](https://xmpp.org/extensions/inbox/moved2.html)
    -   This specification details a way for a user to notify their contacts about an account move.

### New

-   Version 0.1.0 of [XEP-0459](https://xmpp.org/extensions/xep-0459.html) (XMPP Compliance Suites 2022)
    -   Accepted by vote of Council on 2021-05-26.

-   Version 0.1.0 of [XEP-0458](https://xmpp.org/extensions/xep-0458.html) (Community Code of Conduct)
    -   Accept as Experimental after unanimous approval by Board of the ProtoXEP draft for discussion within the community.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEP deferred this month.

### Updated

-   Version 0.2.0 of [XEP-0458](https://xmpp.org/extensions/xep-0458.html) (Community Code of Conduct)
    -   Integrate various comments from various sources (dwd)

-   Version 0.3 of [XEP-0377](https://xmpp.org/extensions/xep-0377.html) (Spam Reporting)
    -   Rework based on list feedback. (ssw)

-   Version 0.11 of [XEP-0292](https://xmpp.org/extensions/xep-0292.html) (vCard4 Over XMPP)
    -   Recommend use of contact bare JIDs for item IDs (ka)

-   Version 1.20.0 of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Add integer-or-max datatype to use with Data Forms Validation. (pep)

### Obsoleted

-   Version 1.0.0 of [XEP-0423](https://xmpp.org/extensions/xep-0423.html) (XMPP Compliance Suites 2020)
    -   Update to Draft as per council vote on 2019/11/07
    -   Successors are XMPP Compliance Suites 2021 ([XEP-0443](https://xmpp.org/extensions/xep-0443.html)) and 2022 ([XEP-0459](https://xmpp.org/extensions/xep-0459.html))

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   No Last Call this month.

### Draft

-   No Draft this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the XMPP community.

Therefore many thanks to Adrien Bourmault, alkino, BAud, emus, Jeybe, nicola, mdosch, Leirda, Licaon_Kter, Pierre Jarillon, pmaziere, seveso, VI, wurstsalat, xdelatour, Ysabeau for their support and help in creation, review and translation!

## Spread the news!

Please share the news on "social networks":

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

## Help us to build the newsletter

We started drafting in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days) in parallel to our efforts in the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. We really need more support!

You have a project and write about it? Please consider sharing your news or events here, and promote it to a large audience! 
And even if you can only spend a few minutes of support, these would already be helpful!

Tasks which need to be done on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Preparation for media images
- Translations: especially German and Spanish

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
