---
title: The XMPP Newsletter March 2022
author: emus
date: 2022-04-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of March 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- German: [xmpp.org/de/blog](https://xmpp.org/de/blog/) and [anoxinon.de](https://anoxinon.de/blog/)
- Italian: [nicfab.it](https://www.nicfab.it/)
- Spanish: [xmpp.org/es/blog](https://xmpp.org/es/blog/)

## XSF Announcements

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

- The XSF is planning to participate in [Google Summer of Code 2022 (GSoC)](https://xmpp.org/community/gsoc-2022/). If you are interested in participating as a student, mentor or as a project in general, please [add your ideas and reach out to us](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022).
- All XSF members are called to vote in the currently on-going [member applications](https://wiki.xmpp.org/web/Membership_Applications_Q1_2022).

## XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

## Software news

### Clients and applications

``` ![Dino calls](/images/newsletter/2022-02-05/dino_conference_call.png "Dino calls")```

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

## Servers

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

## Libraries

_Please do not simply drop links, rather try to make a short (<5 lines) and decent formulated description of what is the main outcome of your source. This will help us a lot! You do not need to use a hard, formal tone, be passionate about why this motivates you or what you work on!_

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [PubSub Type Filtering](https://xmpp.org/extensions/inbox/pubsub-filter.html)
    -   This specification provides a way to filter PubSub nodes in a disco query.

-   [MUC Affiliations Versioning](https://xmpp.org/extensions/inbox/muc-affiliations)
    -   This specification provides a way to reduce the amount of queries necessary to stay up-to-date with affiliations in a MUC room.

### New

-   No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version `2.13.0` of [XEP-0004](https://xmpp.org/extensions/xep-0004.html) (Data Forms)
    -   Add incomplete submission form handling (melvo)

-   Version `1.24.1` of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Add hint for processing incomplete submission forms (melvo)

-   Version `1.24.0` of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Advertise support for publishing items
    -   Replace 'allow' with 'allows' (melvo)

-   Version `1.23.0` of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Clarify (redefine) pubsub#type field. (edhelas, pep)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   No Last Call this month.

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

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

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), alkino, anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, marevalo, mathieui, MattJ, nicfab, seveso, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat,xdelatour, Ysabeau** for their support and help in creation, review and translation. Many thanks to all contributors and their continuous support!

Each months's newsletter issue is drafted in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
