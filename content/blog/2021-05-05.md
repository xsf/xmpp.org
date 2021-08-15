---
title: The XMPP Newsletter April 2021
date: 2021-05-05
author: emus
categories: ["Newsletter"]
aliases:
    - "/2021/04/newsletter-04-april/"
---

Welcome to the XMPP Newsletter covering the month of April 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom! Other than that - enjoy reading! 

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news.jabberfr.org/category/newsletter/).
- The German translation currently appears [at anoxinon.de](https://anoxinon.de/blog/)
- The Italian translation of the last newsletter appeared [at NicFab.it](https://www.nicfab.it/la-newsletter-xmpp-di-marzo-2021-versione-italiana/)

## XSF Announcement

The XMPP Standards Foundation is [now on YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)! You can find recordings of conferences, the XMPP Office Hours, and other fun stuff over on the channel.

Have a talk, demo, or roundtable discussion about XMPP or related technologies? XMPP Office Hours are weekly meetings of XMPP enthusiasts for discussion and presentations. For more information, or to sign up, have a look at [the wiki page](https://wiki.xmpp.org/web/XMPP_Office_Hours).

## Events

[XMPP Office Hours each week](https://wiki.xmpp.org/web/XMPP_Office_Hours) - Also, checkout our new [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of every month.

## Articles 

From May 2021, there have been major content updates for [freie-messenger.de](https://www.freie-messenger.de) as well as additions. From now on, the content will be internationalised. As a first step, there is the new [Quick Overview of Messengers](https://www.freie-messenger.de/systemvergleich/#schnellübersicht) in both German and English. Call for supporters!

[Isode presents their military capabilities at DSEI 2021](https://www.isode.com/company/wordpress/dsei-2021-demo/), offering Military Instant Messaging and more.

[Gajim Development News](https://gajim.org/post/2021-04-30-development-news-april/): April brought an all new message styling parser, making Gajim fully compliant with XEP-0393. This post will also give you a sneak peek on some features we’ve been developing for the past months: the new Chat view and Contact Info window.

![Gajim chat view](/images/newsletter/2021-04/gajim_chat-view-april.png "Gajim chat view")

Libervia (formerly Salut à Toi) has been selected for a grant by NLNet/NGI0 Discovery Fund (with financial support from European Commission's Next Generation Internet programme) for an [gateway between XMPP and ActivityPub doubled with Pubsub end-to-end encryption project](https://www.goffi.org/b/activitypub-gateway-and-pubsub-e2ee-QGqK). The gateway will join two major open and decentralised protocols. In practice it will be a XMPP server component (usable with any server), and implement the ActivityPub server to server protocol (or "Federation Protocol"). On XMPP side, it will be mostly a Pubsub service (with some extra, like private messages converted to XMPP message stanza).

[Vaxbot continues to grow](https://monal.im/blog/vaxbot-continues-to-grow/): VaxBot is a free service that helps you find vaccine appointments in your state or country if available. During the last weeks, [Vaxbot](https://vaccine.monal.im) continued to grow. The service just hit 8 million messages sent and it sends around 800,000 messages a day. XMPP and Vaxbot have been on TV news in Las Vegas and South Carolina, the radio in Washington as well newspapers all over the country. 

Refering the Vaxbot news: Georg Lukas, who runs the server behind it, wrote an article regarding the increased subscriptions and how the services have to adapt the infrastructure to [keep up with this new "VaxBot performance challenge"](https://yaxim.org/blog/2021/04/09/vaxbot-performance-challenge/).

![Yaxim server registrations](/images/newsletter/2021-04/yaxim.png "Yaxim server registrations")

Snikket announces that [XMPP Account Portability](https://snikket.org/blog/dapsi-fund-account-portability/) was funded under the [NGI DAPSI](https://dapsi.ngi.eu/) initiative. It will cover the needed standards (beyond older [XEP-0227](https://xmpp.org/extensions/xep-0227.html) and [XEP-0238](https://xmpp.org/extensions/xep-0283.html)), open-source tools and integrating said functionality into Snikket.

Nicola Fabiano published an article titled: [Whatsapp? No thanks, I prefer to have control over my data](https://www.nicfab.it/whatsapp-no-thanks-i-prefer-to-have-control-over-my-data/)

## Software news

### Clients and applications

[Conversation 2.9.11 and 2.9.12 have been released](https://github.com/iNPUTmice/Conversations/blob/master/CHANGELOG.md), fixing 'No Connectivity' issues on Android 7.1 and adding support for roster pre-authentication.

[Gajim 1.3.2 has been released](https://gajim.org/post/2021-04-24-gajim-1.3.2-released/): This release brings back translations for Windows users. It also adds some small fixes and improvements.

[Monal 5 Beta 4 has been released](https://monal.im/blog/monal-5-beta-4/) with lots of updates.

Since there appeared a lot of [sendxmpp](https://sendxmpp.hostname.sk/) alternatives over the last years there is now an work-inprogress overview in the [XSF wiki](https://wiki.xmpp.org/web/User:MDosch/Sendxmpp_incarnations).

[UWPX is replacing the SQLite-net DB backend with a new Entity Framework Core DB](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.31.0.0). This comes with a fix and update of the OMEMO implementation to the latest version of the draft (OMEMO 0.7.0 (2020-09-05)). This version is incompatible with all other previous versions of OMEMO and UWPX allows you now to only exchange OMEMO encrypted messages with contacts that support at least OMEMO 0.7.0 (2020-09-05) draft. Now UWPX can act as a client with a proper one to one OMEMO implementation!

[Spark 3.0.0 Beta](https://discourse.igniterealtime.org/t/spark-3-0-0-beta-released/90084) has been released bringing fixes as usual. Pade Meetings is now integrated (it enables audio and video chat) and all these over a complete UI refresh.

## Servers

[ejabberd 21.04 has been released](https://www.process-one.net/blog/ejabberd-21-04/): The new ejabberd 21.04 release includes many bugfixes and a few improvements. This release includes minor improvements to fully support 
Erlang/OTP 24 and Rebar3. At the same time, it maintains support back to the old Erlang/OTP 19.3 and Rebar2.

[Openfire 4.6.3 has been released](https://discourse.igniterealtime.org/t/openfire-4-6-3-is-released/90062): This release contains a number of bug fixes and denotes the desire to provide stable 4.6.x series releases while development work continues on a 4.7.0 release.

## Libraries

[slixmpp 1.7.1](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.7.1) has been released, which is a bugfix release for a rarely used code path tied to OMEMO.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   No XEPs have been proposed this month.

### New

-   Version 1.0.0 of [XEP-0457](https://xmpp.org/extensions/xep-0457.html) (Message Fancying)
    -   This specification defines a Unicode-formatted fancy text syntax for use in instant messages.
    -   Initial published version. (XEP Editor (jsc))

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 0.4.0 of [XEP-0420](https://xmpp.org/extensions/xep-0420.html) (Stanza Content Encryption)
    -   Use 'envelope' and 'content' consistently by renaming elements Update namespace to  (melvo)

-   Versions 0.4.0 and 0.5.0 of [XEP-0434](https://xmpp.org/extensions/xep-0434.html) (Trust Messages (TM))
    -   Add new section, use more precise sentences, apply consistent formatting:
    -   Add new section for Trust Message URIs
    -   Use 'that' instead of 'which' for restrictive clauses
    -   Apply consistent formatting for paragraphs and revision history
    -   Update to XEP-0420 version 0.4.0 and adapt namespace to shortname
    -   Replace SCE's old 'content' element by its new 'envelope' element
    -   Replace SCE's old 'payload' element by its new 'content' element
    -   Update SCE's namespace to 'urn:xmpp:sce:1'
    -   Change namespace to 'urn:xmpp:tm:0' (melvo)

-   Versions 0.2.0 and 0.3.0 of [XEP-0450](https://xmpp.org/extensions/xep-0450.html) (Automatic Trust Management (ATM)
    -   Add usage of Trust Message URIs, use more precise sentences, apply consistent formatting
    -   Add usage of Trust Message URIs for initial authentications
    -   Use 'that' instead of 'which' for restrictive clauses
    -   Apply consistent formatting for paragraphs and revision history
    -   Update to XEP-0420 version 0.4.0 and XEP-0434 version 0.5.0
    -   Replace SCE's old 'content' element by its new 'envelope' element
    -   Replace SCE's old 'payload' element by its new 'content' element
    -   Update SCE's namespace to 'urn:xmpp:sce:1'
    -   Update TM's namespace to 'urn:xmpp:tm:0'
    -   Update namespace to 'urn:xmpp:atm:1' (melvo)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   [XEP-0280](https://xmpp.org/extensions/xep-0280.html) Message Carbons
-   [XEP-0313](https://xmpp.org/extensions/xep-0313.html) Message Archive Management

### Draft

-   No Drafts this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to alkino, emus, Licaon_Kter, *IM*, Martin, mathieui, MattJ, nicola, peetah, Sam, seveso, therealjeybe, wurstsalat and Ysabeau for their help in creating it!

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

We started drafting in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days) in parallel to our efforts in the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. 

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

