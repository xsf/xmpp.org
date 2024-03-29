---
title: The XMPP Newsletter February 2022
author: emus
date: 2022-03-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of February 2022.

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

- JMP.chat [describes in their blog](http://blog.jmp.chat/b/2022-bidirectional-gateways) why gateways, and especially bidirectional gateways, with XMPP and other protocols, are so useful. [Their Newsletter](http://blog.jmp.chat/b/february-newsletter-2022) also announces the launch of worldwide calling and completion of their rebrand.

![JMP.chat bidirectional gateways](/images/newsletter/2022-02-05/JMP_bidirectional.png "JMP.chat bidirectional gateways")

- Erik Bärwaldt, from the German "Linux Magazin" [evaluated instant messengers including Conversations for XMPP](https://www.linux-magazin.de/ausgaben/2022/02/bitparade/) [DE].

- [Mellium Dev Communiqué](https://opencollective.com/mellium/updates/dev-communique-for-february-2022): This month saw the release of several new packages including integration testing for Slixmpp, support for PEP Native Bookmarks, better support for various cryptographic hashes, and support for entity capabilities.

## Software news

### Clients and applications

[Dino `0.3` has been released](https://dino.im/blog/2022/02/dino-0.3-release/): Video calls and conferences - encrypted and peer-to-peer. Dino now supports calls between two or more people!

![Dino calls](/images/newsletter/2022-02-05/dino_conference_call.png "Dino calls")

[Gajim development news](https://gajim.org/post/2022-02-24-development-news-february/): February brought a unified group chat details window, which offers all the configuration knobs you need. Also this month: less memory leaks and improved OMEMO QR codes.

Monal had a [successful funding campaign](https://monal.im/blog/funding-campaign-mac-mini-for-faster-monal-development/) for a build server, which will significantly reduce build time. [Further insights into Monal development](https://monal.im/blog/insights-into-monal-development/): Monal will drop support for iOS 12 and 13, and for macOS Catalina. Monal's team is searching for a SwiftUI developer, and they need help with building a new and simplified website.

Big news from Movim: [Movim `0.20` "Skiff"](https://mov.im/?node/pubsub.movim.eu/Movim/dd90cd1c-4bcd-45a5-88a3-220fd4280b21) has been released, which features OMEMO support, GUI improvements, and better group chat management.

![Movim GUI update](/images/newsletter/2022-02-05/movim_publish.png "Movim GUI update")

[Psi+ `1.5.1605`](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) has been released with OMEMO fixes.

[Poezio `0.13.2` has been released](https://github.com/poezio/poezio/releases/tag/v0.13.2), this version only fixes the compatibility with the newly released slixmpp `1.8.0`, but a much more interesting release is to come soon.

Profanity developers wrote a [blog post](https://profanity-im.github.io/blog/post/profanity-on-pinephone/) on how to run their client on Pinephones.

Tigase released [BeagleIM `5.1`](https://github.com/tigase/beagle-im/releases/tag/5.1) and [SiskinIM `7.1`](https://github.com/tigase/siskin-im/releases/tag/7.1) featuring improved OMEMO support.

## Servers

[Jackal `0.57.0`](https://github.com/ortuman/jackal/releases/tag/v0.57.0), an XMPP server written in Go has been released.

Openfire announces the release of [Openfire `4.7.1`](https://discourse.igniterealtime.org/t/openfire-4-7-1-released/91365): Notable fixes include security updates to bundled database drivers, logging configuration fixes, and an important fix for users experiencing troubles with users getting booted from group chat rooms. Furthermore, [Openfire Pàdé `1.6.1`](https://discourse.igniterealtime.org/t/openfire-pade-1-6-1-released/91366) has been released. [REST API Openfire plugin `1.7.1`](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-7-1-released/91358) hase been released, too.

Snikket published an important update for users of their [server software on ARM devices, including Raspberry Pi boards](https://snikket.org/blog/server-updates-for-arm/).

[Tigase XMPP Server `8.2.0`](https://github.com/tigase/tigase-server/releases/tag/tigase-server-8.2.0) has been released.

## Libraries

Mellium Co-op has released [`v0.21.0`](https://pkg.go.dev/mellium.im/xmpp@v0.21.0) and [`v0.21.1`](https://pkg.go.dev/mellium.im/xmpp@v0.21.1) of the [melium.im/xmpp](https://mellium.im/xmpp/) library for Go! Highlights for this release include basic support for 
PubSub and PEP as well as In-Band Bytestreams. More information can be found in the [release announcement](https://opencollective.com/mellium/updates/new-release-mellium-im-xmpp-v0-21-0). Version 0.21.1 fixes a security issue that was discovered in the websocket package and should be preferred when updating. For more information see [CVE-2022-24968](https://mellium.im/cve/cve-2022-24968/).

[Slixmpp `1.8.0`](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.8.0) has been released, which adds compatibility with python 3.10, as well as a lot of improvements related to typing and async under the hood.

Tigase had several releases for their products: [Halcyon `0.0.17`](https://github.com/tigase/halcyon/releases/tag/v0.0.17), [JaXMPP `3.5.0`](https://github.com/tigase/jaxmpp/releases/tag/3.5.0), [Tigase Swift `3.1.0`](https://github.com/tigase/tigase-swift/releases/tag/3.1.0), and [Tigase Swift-OMEMO `2.1.0`](https://github.com/tigase/tigase-swift-omemo/releases/tag/2.1.0).

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [PubSub Type Filtering](https://xmpp.org/extensions/inbox/pubsub-filter.html)
    -   This specification provides a way to filter PubSub nodes in a disco query.

-   [MUC Affiliations Versioning](https://xmpp.org/extensions/inbox/muc-affiliations-versioning.html)
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

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), alkino, anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, marevalo, mathieui, MattJ, nicfab, patasca, seveso, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat,xdelatour, Ysabeau** for their support and help in creation, review and translation. Many thanks to all contributors and their continuous support!

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
