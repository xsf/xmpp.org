---
title: XMPP bites into the apple!
date: 2020-10-06
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/09/newsletter-09-september/"
---

Welcome to the XMPP newsletter covering the month of September 2020.

### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news/jabberfr.org/category/newsletter/)

## XSF Announcements

The XSF started the application period for its annual XSF Board and XSF Council elections. Applicants for the council must be elected XSF members, while board seats are open to everyone. If you are interested to apply for any of those positions please visit the [application page](https://wiki.xmpp.org/web/Board_and_Council_Elections_2020).

The Q4 2020 XSF membership application period is open as well. If you are interested to become an XSF member you can [apply here](https://wiki.xmpp.org/web/Membership_Applications_Q4_2020).

## Articles

The German blog kuketz-blog.de published [part 6 of its messenger series](https://www.kuketz-blog.de/conversations-messaging-ueber-das-xmpp-protokoll-messenger-teil6/) [German] covering the Android client Conversations.

Tigase published an article on the development of their [multiplatform XMPP Library Halcyon](https://tigase.net/halcyon-a-look-at-halcyon/) written in Kotlin. 
In another article later this month they wrote on [publishing and subscribing](https://tigase.net/halcyon-publishing-and-subscribing-with-halcyon/) via [XEP-0060](https://xmpp.org/extensions/xep-0060.html). And to close this article serie, Tigase explains the STUN & TURN setup with their [Tigase XMPP server using XEP-0215](https://tigase.net/tigase-server-with-stun-turn).

## Software news

### Clients and applications

A new major version of Movim is out, with improved notifications, new video-conferencing, chat features and some major performance overhaul. A new version for the Android application is also available to integrate all those features in the Android environment. Discover all the improvements of this new release on the official release note [Movim 0.18 – Oterma](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/11655111-e7ad-4e0c-975c-3c78755d22aa). Have a look at Movim’s improved draw widget:

![Movim](/images/newsletter/september2020/movim.png "Movim")

[Gajim Development News (September)](https://gajim.org/post/2020-09-27-development-news-september/): this month's post marks one year of Gajim Development News! The rework of Gajim’s preferences window has been completed. We improved group chat invitations and made group chat settings easier to access. Also, joining a group chat is now much prettier.

MCabber, the venerable old text UI client, has been released in [version 1.1.1](https://github.com/McKael/mcabber/releases/tag/1.1.1) and [1.1.2](https://github.com/McKael/mcabber/releases/tag/1.1.2). Apart from bugfixes, support for displaying the number of unread messages and refactorization of carbon message handling has been implemented.

The Python SDK for GE WiFi-enabled kitchen appliances, [gekitchen](https://github.com/ajmarks/gekitchen), made its first GitHub release. The primary goal is to use it to power integrations for [Home Assistant](https://www.home-assistant.io/), though that probably needs to wait for some new entity types. It is using XMPP as a mean to authenticate, since it is what the GE SmartHQ app uses to communicate with devices.

XMPP on iOS and Mac is getting traction after all:

- Hello [BeagleIM 4.0 and SiskinIM 6.0](https://tigase.net/beagleim-4.0-and-siskin-6.0-released/)! Their iOS and MacOS clients now speak Mediated Information eXchange (MIX) ([XEP-0369, XMPP’s new group chat protocol](https://xmpp.org/extensions/xep-0369.html)). VoIP connectivity has been improved with Jingle Message Initiation ([XEP-0353](https://xmpp.org/extensions/xep-0353.html)), Last Message Correction ([XEP-0308](https://xmpp.org/extensions/xep-0308.html)) is available for editing messages which were already sent, and other features like Message Retraction ([XEP-0424](https://xmpp.org/extensions/xep-0424.html)) and quick replies for quoting were introduced. Support for CAPTCHA forms has been added as well: Extended In-Band Registration ([XEP-0158](https://xmpp.org/extensions/xep-0158.html)) is invoked for additional verification during account registration. Of course there are many more changes and bugfixes! 

- The iOS and MacOS client Monal got a [new push server](https://monal.im/blog/monal-push-server-upgrade/) and received improvements for Message Archive Management. This is one of the many changes to arrive in future releases. Be prepared and get a glimpse in the [Monal Beta Testflight](https://monal.im/blog/news-betas-up-for-4-8/).

## Servers

No chance for SPAM: Openfire presents their new ['Spam blacklist' plugin](https://discourse.igniterealtime.org/t/new-openfire-plugin-to-help-reduce-spam/88730) which enables reporting for users. Everyone, please report potential spammers!  Openfire’s monitoring plugin has been released in version 2.1.0, featuring full text search for personal archive messages. 

The Prosody XMPP server team has been busy this month with several exciting things. Firstly, the [Prosody 0.11.6 release announcement](https://blog.prosody.im/prosody-0.11.6-released/). They also published a suite of new modules to allow [simple invite-based account registration](https://blog.prosody.im/great-invitations/) which can help guide new users through choosing a suitable client and registering their first XMPP account. Finally, they published a round-up of advice for everyone on how to [help address spam on the XMPP network](https://blog.prosody.im/simple-anti-spam-tips/).

![Prosody](/images/newsletter/september2020/Prosody_invite-flow-manual.png "Prosody")


## Libraries

Libstrophe, a lightweight XMPP client library written in C, released [version 0.10.0](https://github.com/strophe/libstrophe/releases/tag/0.10.0) which, besides bugfixes and a new API, brings new features: SCRAM-SHA-256 and SCRAM-SHA-512 support, c-ares support, LibreSSL support and global timed handlers that fire periodically regardless of connections status

There is a new [beta online for Smack 4.4.0 (Smack 4.4.0-beta2)](https://discourse.igniterealtime.org/t/smack-4-4-0-beta2-released/88804), the Ignite RealTime Java XMPP library.

## Other

Google Summer of Code 2020: Anmol summarized his three months work on In-Band Real Time Texting (RTT) for Dino (XMPP Desktop Client) in a [final blog post](https://wolfieanmol.github.io/gsoc-blog/gsoc-2020-ends/).

The owner of the [joinxmpp.org](https://joinxmpp.org) domain is lacking time for further development of the project. He wrote a short summary describing the original goals and says he is now looking for somebody motivated to take on the project.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html).

### Updated

-   Version 2.11.0 of [XEP-0004](https://xmpp.org/extensions/xep-0004.html) (Data Forms)
    -   Further clarify the presence requirements for the type attribute on fields.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedbacks gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   [XEP-0411](https://xmpp.org/extensions/xep-0411.html) (Bookmarks Conversion)

### Proposed Extensions

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether or not to accept this proposal as an Experimental XEP.

-   [XMPP Compliance Suites 2021](https://xmpp.org/extensions/inbox/cs-2021.html)
    -   This document defines XMPP application categories for different use cases (Core, Web, IM, and Mobile), and specifies the required XEPs that client and server software needs to implement for compliance with the use cases.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to agnauck, emus, mdosch, mwild1, pep., pmaziere, Seve, wurstsalat3000 and zash for their help in creating it!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

## Subscribe to the newsletter

We suggest you [Subscribe](https://tinyletter.com/xmpp) to receive the next editions in your inbox as soon as it is published! 
Promote this newsletter to whoever may be interested.

## Help us to build the newsletter

We started drafting every new issue in the [XSF Github repository](https://github.com/xsf/xmpp.org/pulls) and we are 
always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) 
and thereby help us sustain this as a community effort. 

You have a project and write about it? Please consider sharing your news or events here, and promote it to a large audience! 
Even if you can only spend a few minutes, these would already be helpful!

Tasks which need to be done on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Preparation for media images
- Translations: especially German and Spanish

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
