---
title: The XMPP Newsletter March 2021
date: 2021-04-05
author: emus
categories: ["Newsletter"]
aliases:
    - "/2021/03/newsletter-03-march/"
---

Welcome to the XMPP newsletter covering the month of March 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom! Other than that - enjoy reading! 

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news.jabberfr.org/category/newsletter/).
- Read the German translation of the [previous month's newsletter](https://anoxinon.de/blog/xmpp_newsletter_februar_2021/)

## XSF Announcements

The XMPP community is now holding regular virtual office hours, short weekly talks, demos, or round table discussions about XMPP or XMPP-adjacent topics! Meeting  details, a list of future talks, and the sign up sheet can be found on the [XMPP Wiki](https://wiki.xmpp.org/web/XMPP_Office_Hours). And we are on [YouTube now](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

## Events

[XMPP Office Hours each week!](https://wiki.xmpp.org/web/XMPP_Office_Hours)

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of every month.

## Articles 

Nicola Fabiano wrote two articles on ["Consciously looking at messaging apps: when users want broad freedom and full control over their data"](https://www.nicfab.it/consciously-looking-at-messaging-apps-when-users-want-broad-freedom-and-full-control-over-their-data/) and ["Aware digital communication respecting privacy and the apps or services you choose"](https://www.nicfab.it/aware-digital-communication-respecting-privacy-and-the-apps-or-services-you-choose/)

Arnaud Joset wrote a small tutorial on [how to use Prosody with a HTTP Reverse Proxy](https://blog.agayon.be/prosody_http.html).

Marek Foss from ProcessOne wrote several articles on ejabberd background and setups:

-   [Starting with MQTT protocol and ejabberd MQTT broker](https://www.process-one.net/blog/starting-with-mqtt-protocol-and-ejabberd-mqtt-broker/)
-   [Install and configure MariaDB with ejabberd](https://www.process-one.net/blog/install-and-configure-mariadb-with-ejabberd/)
-   [Getting started with WebSocket API in ejabberd](https://www.process-one.net/blog/getting-started-with-websocket-api-in-ejabberd/)
-   [Publish-Subscribe pattern and PubSub in ejabberd](https://www.process-one.net/blog/publish-subscribe-pattern-and-pubsub-in-ejabberd/)

Alex Akinbia and Ehizojie Ojieb published ["Forensic analysis of open-source XMPP multi-client social networking apps on iOS devices"](https://www.sciencedirect.com/science/article/pii/S2666281721000196?via%3Dihub). They did their study based on Monal 4.5 and Siskin 5.8.1.

## Software news

### Clients and applications

Conversations [2.9.8](https://github.com/iNPUTmice/Conversations/releases/tag/2.9.8) and [2.9.9](https://github.com/iNPUTmice/Conversations/releases/tag/2.9.9) have been released. These releases bring better compatibility with non-libwebrtc WebRTC implementations, verification of audio and video (A/V) calls with preexisting OMEMO sessions, and better TOR support.

![Conversations verification A/V](/images/newsletter/march2021/conversations.png "Conversations verification A/V")

[Gajim Development News (March)](https://gajim.org/post/2021-03-28-development-news-march/): Gajim’s new main window is coming together step by step while many core functionalities are being rewritten. This month also brought better accessibility for Gajim’s message input and improved status icon behavior. [Gajim 1.3.1 has been released](https://gajim.org/post/2021-03-01-gajim-1.3.1-released/) as well and they added a setting to explicitly enable GSSAPI authentication and improvement changes.

JSXC - the Javascript XMPP Client got a [funding for group chat calls!](https://twitter.com/jsxc_org/status/1366352995508748294)

[Monal is now on Mastodon](https://fosstodon.org/@Monal)! The [second beta release](https://monal.im/blog/monal-5-beta-2-out/) has been published as well, high-way to Monal 5.0! Besides, a setup has been created to [support the vaccination process](https://vaccine.monal.im/) in many US states, but also Puerto Rico. More than one million notifications have been sent already. XMPP is once again supporting in the pandemic crisis. There were [several blog posts in March](https://monal.im/2021/03/) on this topic, you can start with [this selected one](https://monal.im/blog/xmpp-ending-this-pandemic-part-1/). Stay tuned and please support by testing the current beta!

qXMPPconsole is a new [browser based XMPP console](https://github.com/voger/qXMPPconsole). It's main purpose is to aid in learning about the XMPP protocol.

## Servers

No server updates out there :(

## Libraries

[Smack 4.4.2 has been released](https://discourse.igniterealtime.org/t/smack-4-4-2-released/89913), containing mostly bugfixes.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Content Rating Labels](https://xmpp.org/extensions/inbox/content-ratings.html) has been proposed and accepted.

### New

-   Version 0.2.0 of [XEP-0456](https://xmpp.org/extensions/xep-0456.html) (Content Rating Labels)
    -   This specification provides a wire format in the form of a Service Discovery extension to allow services of various kinds to publish information about the kind of content they allow and/or endorse on their platform.
    -   Describe the conversion algorithm. (jsc)

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 1.1 of [XEP-0294](https://xmpp.org/extensions/xep-0294.html) (Jingle RTP Header Extensions Negotiation)
    -   Add mapping for a=extmap-allow-mixed (ph)

-   Version 0.2.0 of [XEP-0408](https://xmpp.org/extensions/xep-0408.html) (Mediated Information eXchange (MIX): Co-existence with MUC)
    -   Fix reference to MIX-CORE namespaces (@mathieui)

-   Version 0.3.0 of [XEP-0406](https://xmpp.org/extensions/xep-0406.html) (Mediated Information eXchange (MIX): MIX Administration)
    -   Fix reference to MIX-CORE namespaces (@mathieui)

-   Version 2.12.0 of [XEP-0004](https://xmpp.org/extensions/xep-0004.html) (Data Forms)
    -    Clarify that the 'reported' element must appear before any 'item' element. (fs, jsc)

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

Thanks to anubis, Bastoon, emus, jeybe, jonas-l, Julien Jorge, Holger, pmaziere, Sam Whited, seveso, vanitasvitae, wurstsalat3000 and Ysabeau for their help in creating it!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

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

