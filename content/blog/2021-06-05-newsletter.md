---
title: The XMPP Newsletter May 2021
author: emus
date: 2021-06-05
categories: ["Newsletter"]
aliases:
    - "/2021/05/newsletter-05-may/"
---

Welcome to the XMPP Newsletter covering the month of May 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom.

Other than that - enjoy reading! 

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- The French translation appears at [jabberfr.org](https://news.jabberfr.org/category/newsletter/)
- The German translation appears at [anoxinon.de](https://anoxinon.de/blog/)
- The Italian translation appeares at [NicFab.it](https://www.nicfab.it/la-newsletter-xmpp-di-marzo-2021-versione-italiana/)

Many thanks to the translators and their work! This is a great help to spread the news! Please join them in their work or start over with another language!

## XSF Announcement

Voting the membership applications can be done via xmpp:memberbot@xmpp.org (by XSF members only). We will hold a member meeting on June 10th to formally approve the voting results. The meeting particulars are: 

- Date: June 10th, 2021 
- Time: 19:00 UTC 
- Location: xmpp:xsf@muc.xmpp.org
- Further information: https://wiki.xmpp.org/web/Membership_Applications_Q2_2021

## Events

[XMPP Office Hours each week](https://wiki.xmpp.org/web/XMPP_Office_Hours) - Also, checkout our new [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of the month. Next topic will be the [Curated XMPP provider list](https://invent.kde.org/melvo/xmpp-providers) on Wednesday, 2021-06-09 18:00 CEST.

## Videos

[Gajim 1.4 UI/UX Preview](https://www.youtube.com/watch?v=SwZaZY2hYzA) presented by Philipp Hörist.

![Gajim 1.4 UI/UX Preview](/images/newsletter/may2021/gajim_youtube.png "Gajim 1.4 UI/UX Preview")

## Articles

JC Brand, the developer behind [Converse.js](https://conversejs.org/), the web client, blogs about the current development towards version 
8.0.0 in [Mergebounce: Increasing performance by batching IndexedDB writes](https://opkode.com/blog/2021-05-05-mergebounce-indexeddb/).

Ingo Jürgensmann wrote the article [The Fediverse – What About Resources?](https://blog.windfluechter.net/2021/05/01/the-fediverse-what-about-ressources/) on the resources of different messaging technologies. He states that XMPP consumes a lot less hardware resources and thereby energy than comparing services.

Sumit Khanna wrote an article about [moving their phone numbers from Google Hangouts/Voice to a SIP/XMPP Service](https://battlepenguin.com/tech/moving-my-phone-number-from-google-hangouts-voice-to-an-sip-xmpp-service/) by using XMPP and [jmp.chat](https://jmp.chat/).

[jmp.chat](https://jmp.chat/) is also used by [craftyguy](https://blog.craftyguy.net/) to [send test MMS](https://blog.craftyguy.net/sendxmpp-mms/) to himself during [mmsd](https://gitlab.com/kop316/mmsd/) development.

[Vaxbot US has been shutdown](https://monal.im/blog/vaxbot-us-shutting-down/) after change of the situation in the USA. But the service has been deployed for Canada instead. All in all, that was an interesting approach and use of XMPP technology!

## Software news

### Clients and applications

[Video calls in Dino](https://fosstodon.org/web/statuses/106228549009869402) are slowly coming together. Dino's developers are already making 
successful OMEMO encrypted video calls. The feature is included in their nightly builds now, but there's still further work to be done.

![Dino AV calls](/images/newsletter/may2021/Dino_AVcalls.png "Dino AV calls")
 
[Gajim development News](https://gajim.org/post/2021-05-28-development-news-may/): This month brought improved Ad-Hoc commands, fixes for Gajim Portable, 
and new image preview capabilities. Meanwhile, work on Gajim’s next version made some progress: better code block styling, chat filters, note to myself, and much more. Also in Gajim news: [Gajim celebrated its 17th birthday this month](https://gajim.org/post/2021-05-21-gajims-birthday/). Philipp Hörist (lovetox), maintainer of Gajim, [gave a preview of the new Gajim 1.4 User Interface](https://www.youtube.com/watch?v=SwZaZY2hYzA). Gajim is an XMPP client written in Python. It currently receives a big UI overhaul, of which the first results were presented at the [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours).

[Kaidan 0.8](https://www.kaidan.im/2021/05/28/kaidan-0.8.0/) has been released with noteworthy new features, including typing notifications ([Chat State Notifications](https://xmpp.org/extensions/xep-0085.html)) and message history synchronization (using [MAM](https://xmpp.org/extensions/xep-0313.html))!

"Salut à Toi" is now "Libervia". [Read more about the changes behind the curtain.](https://www.goffi.org/b/libervia-progress-note-2021-w18-i4HD)

UWXP, a Microsoft Windows (UWP) client, has been released in [version 0.32.0.0 with focus on MUC and MAM bugfixes](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.32.0.0).

## Servers

ProcessOne published a tutorial on [how to install and configure MariaDB with ejabberd](https://www.process-one.net/blog/install-and-configure-mariadb-with-ejabberd/).

[Prosody 0.11.9 has been released](https://blog.prosody.im/prosody-0.11.9-released/): This release addresses a number of important security issues that 
affect most deployments of Prosody. Full details are available in [a separate security advisory](https://prosody.im/security/advisory_20210512/). We recommend that all deployments upgrade or apply the mitigations described in the advisory.

Snikket [just published their May update](https://snikket.org/blog/may-2021-server-release/) to the Snikket server software. This includes a few security fixes from Prosody, so upgrade soon! It also now allows you to manage user roles and access levels.

## Libraries

No updates on XMPP libraries reach our attention :-(

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [XMPP Compliance Suites 2022](https://xmpp.org/extensions/inbox/cs-2022.html)
    -   This document defines XMPP application categories for different use cases (Core, Web, IM, and Mobile), and specifies the required XEPs that client and server software needs to implement for compliance with the use cases.

### New

-   No new XEP this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEP deferred this month.

### Updated

-   Version 0.7.0 of [XEP-0373](https://xmpp.org/extensions/xep-0373.html) (OpenPGP for XMPP)
    -   Recommend PubSub access model 'open' for public key data node and metadata node. (ps)

-   Version 1.3 of [XEP-0013](https://xmpp.org/extensions/xep-0013.html) (Flexible Offline Message Retrieval)
    -   Deprecate after council vote of 2021-03-31 (XEP Editor (jsc))

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   No Last Call this month.

### Draft

-   No Draft this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Therefore many thanks to emus, Florent Zara, Goffi, jeybe, Licaon_Kter, mdosch, nicola, pmaziere, snark, wurstsalat and Ysabeau for their support and help in creation, review and translation!

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

