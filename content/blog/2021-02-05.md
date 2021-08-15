---
title: The XMPP Newsletter January 2021
date: 2021-01-05
author: emus
categories: ["Newsletter"]
aliases:
    - "/2021/01/newsletter-01-january/"
---

Welcome to the XMPP newsletter covering the month of December 2020 and January 2021.

Happy to have you back reading! We hope this year will be a great one for you, but as well for XMPP!

In December 2020 we discussed the last year of producing and publishing of the XMPP Newsletter, [read the notes here](https://github.com/xsf/xmpp.org/pull/851#issuecomment-754919811)!

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the last year, please consider to say thanks or help these projects!

### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news/jabberfr.org/category/newsletter/).

## XSF Announcement

Regarding the announcement by Let's Encrypt to switch away from their Root CA certificate: Now they are extending their [Android device compatibility of their certificates](https://letsencrypt.org/2020/12/21/extending-android-compatibility.html). [Read their the original post](https://letsencrypt.org/2020/11/06/own-two-feet.html). 

Edward Maurer wrote a commentary blog post regarding on the current situation of instant messaging communication and XMPP: [Instant Messaging: It's not about the app](https://xmpp.org/2021/01/instant-messaging-its-not-about-the-app/). There are also translations in [German](https://xmpp.org/2021/01/instant-messaging-es-geht-nicht-um-die-app/), [French](https://xmpp.org/2021/01/messagerie-instantanee-il-ne-sagit-pas-de-lapplication/), [Spanish](https://xmpp.org/2021/01/mensajeria-instantanea-no-se-trata-de-la-aplicacion/) and [Romanian](https://xmpp.org/2021/01/mesagerie-instantanee-nu-este-vorba-despre-aplicatie/). Thanks to all contributors!

## Events

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of
every month

## Articles 

The developers of the Prosody XMPP server wrote [a recap post of 2020](https://blog.prosody.im/2020-retrospective/) summarizing what happened to the project in the past year. The post contains some nice statistics about how many Prosody deployments are running around the world.

Wolthera wrote another article explaining how to write a [XMPP Client in Godot](https://wolthera.info/2020/12/xmpp-client-in-godot/).

The developers at [blabber.im](https://blabber.im) did a short review of their [2020 statistics](https://blabber.im/en/das-jahr-2020-im-rueckblick/) (DE), giving interesting insights about server traffic, registered users, and more. blabber.im is the new home of Pix-Art Messenger, a Conversations fork which had to [rename itself due to legal issues with a company using a similar sounding name](https://blabber.im/en/wie-pix-art-messenger-aus-dem-google-play-store-verschwand/). Pix-Art Messenger is [now available using the name blabber.im](https://blabber.im/en/blabber-im-v3-0-0-verfuegbar/), offering the same features Pix-Art did.

Paula Kreuzer made a nice [embroidery of the XMPP logo](https://pixelfed.de/p/paulakreuzer/256133901083348992)!

XMPP Refresher: The Open Instant Messaging Protocol Then & Now. XMPP remains a critical framework for chat and messaging applications 20+ years after its launch. [Here’s how it works](https://getstream.io/blog/xmpp-extensible-messaging-presence-protocol/).

In his blog, Dryusdan shares [his recipe](https://dryusdan.space/installer-son-serveur-xmpp-100-conforme-aux-xep/) (FR) for deploying his own XMPP service, with the following main ingredients: Debian or Ubuntu, ejabberd and PostgreSQL. This recipe guarantees a 100% score on the well-known Conversations Compliance test.
 
Nicoco explains [why and how](https://linuxfr.org/users/therealnicoco/journaux/ma-passerelle-xmpp-signal) (FR) he created his own XMPP/signal gateway, called [spectrum2_signald](https://gitlab.com/nicocool84/spectrum2_signald/). Not perfect yet (only one signal account is currently supported) but it is open-source!

MongooseIM published an article on [privacy and security within instant messaging](https://www.erlang-solutions.com/blog/how-to-ensure-your-instant-messaging-solution-offers-users-privacy-and-security/).

Tails ships with an XMPP client which currently is Pidgin. For security reasons [Tails is going to replace it](https://fosstodon.org/@tails/105587047791026258). A new XMPP client that Tails likely is going to install will be either [Dino](https://fosstodon.org/@dino) or [Gajim](https://fosstodon.org/@gajim).

The German newspaper "taz" mentions XMPP in general and Conversations and Quicksy in particular in an [article about alternatives to WhatsApp](https://taz.de/Alternative-Messenger-Dienste/!5743214/).

["XMPP - was ist das?"](https://www.heise.de/tipps-tricks/XMPP-was-ist-das-5006209.html) (DE) article in the German "heise online tipps + tricks" magazine.

Axel Reimer published a startup guide for Siskin IM in his blog. It is available in [English](https://xmppeinrichtung.blogspot.com/2021/01/installation-and-configuration-of.html) and [German](https://xmppeinrichtung.blogspot.com/2021/01/siskin-im-auf-dem-iphone-als-instant.html).

(A little bit too late, but interesting for iOS developer: [Chris Beckstrom explains how he bridged iMessage and XMPP](https://chrisbeckstrom.com/posts/How-I-Bridged-iMessage-and-XMPP/))

## Software news

### Clients and applications

[Conversations 2.9.2 and 2.9.3](https://github.com/iNPUTmice/Conversations/blob/master/CHANGELOG.md) have been released, adding support for SCRAM-SHA-512 authentication, 'Easy Invite' generation on supporting servers, and more. Furthermore, [Conversations 2.9.6](https://github.com/iNPUTmice/Conversations/blob/master/CHANGELOG.md) has been released, bringing minor stability improvements for A/V calls and bug fixes.

Gajim [1.3.0 Beta1](https://gajim.org/post/2021-01-01-gajim-1.3.0-beta-released/) and [1.3.0 Beta2](https://gajim.org/post/2021-01-09-gajim-1.3.0-beta2-released/) have been released. More than four months have passed since the release of Gajim 1.2.2. A lot has happened during this time, including a complete redesign of both Gajim’s Preferences window and configuration backend. Be the first to have a look, and help us ironing out the last issues before the final version arrives. 

Gajim Development News: [In December](https://gajim.org/post/2020-12-28-development-news-december/), the profile window received a complete rework, adding state of the art vCard capabilities and a brand new profile picture selector to Gajim. Furthermore, Chat Markers have been improved and some bugs have been fixed. [In January](https://gajim.org/post/2021-01-28-development-news-january/) a long anticipated feature has been implemented: direct chat messages for private group chats. Also, [@gajim is now on Fosstodon](https://fosstodon.org/@gajim)!

![Gajim has a new profile picture selector](/images/newsletter/january2021/GajimProfile.png "Gajim has a new profile picture selector")

[Kaidan will receive a grant for end-to-end encryption](https://www.kaidan.im/2021/01/07/end-to-end-encryption/): Kaidan will be supported by [NLnet](https://nlnet.nl/foundation/) for adding end-to-end encryption support. We will implement the latest version of the encryption protocol OMEMO and extend it by an easy trust management to solve issues other OMEMO-capable chat apps suffer from.

[MatriX vNext development update](https://www.ag-software.net/2020/12/30/matrix-vnext-development-update/).

[Monal 4.9 for iOS](https://monal.im/blog/ios-4-9-is-out/) has been released, including a complete rewrite of its internal XMPP parser, a complete overhaul of its OMEMO implementation, and many new features (Chat Markers, Nicknames, User Avatars). [Monal 4.9 for MAC](https://monal.im/blog/mac-4-9-beta-out-with-apple-silicon-support/) now supports 'Apple Silicon' and will soon be released. If you like, you can now follow [Monal on Reddit](https://www.reddit.com/r/monal/) as well. [Beta Testers are called to provide active feedback](https://monal.im/blog/wanted-monal-feedback/) from their current experience. Furthermore, the Monal developers also announced an urgent update about a [critical vulnerabitliy](https://monal.im/blog/cve-2020-26547/). Finally, with the announcement [Monal 5.0 will be the last release that supports iOS 12](https://monal.im/blog/monal-5-0-will-be-the-last-version-to-support-ios12/)

![Monal takes care on your privacy](/images/newsletter/january2021/monalproductpagepreview.png "Monal takes care on your privacy")

[Movim is full of new features for 2021](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/movim-is-full-of-new-features-for-2021-oyJ4gu)! Check out the latest blog post to find out what you can expect in the upcoming release and what has been added recently, like URL embedding, picture caching and more. [Movim also had to upgrade their server capacity](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/156c9c91-bbe3-45f0-a5df-1016d641ede6) in order to deal with the sudden subscription of hundreds of new users both on our XMPP #services movim.eu and jappix.com and on #Movim itself. The new official Movim pod is now located at [mov.im](https://mov.im) and the rest of the services (XMPP, Telegram/Slack/IRC bridges…) are now deployed on the new server. A warm welcome to all new users that joined Movim in the past few days!

The Ignite Realtime community [announces the availability of Openfire Pàdé v1.2.2](https://discourse.igniterealtime.org/t/openfire-pade-1-2-0-released/89294) and Openfire [Pàdé v1.3.0](https://discourse.igniterealtime.org/t/openfire-meetings-becomes-pade/89401). This release combines all Openfire Meetings modules (jitsi meet, videobridge, focus and sip gateway) and converse.js into a single plugin called Pàdé and fixes some issues.

[Profanity 0.10.0 has been relased](https://github.com/profanity-im/profanity/releases/tag/0.10.0). The goal for this release was mostly internal cleanup, but there have also been some improvements under the hood for MAM ([XEP-0313](https://xmpp.org/extensions/xep-0313.html)).

[Quicksy.im](https://quicksy.im/), a Conversations Easy Entry and Easy Discovery spin-off, has grown its user count [by more than 30%](https://twitter.com/iNPUTmice/status/1351613901104963592) over the last two weeks. Quicksy 2.9.6 now supports automatic processing of received verification SMS.

[SàT progress note 2020-W53](https://www.goffi.org/b/LFMqr7xC2aNf4MDgkbamBY/progress-note): Full-Text Search in PubSub, easy invitations for sharing files, and more.

[SiskinIM 6.2 has been released](https://mastodon.technology/@tigase/105627824140193490), bringing support for OMEMO encrypted group chats (private group chats only), and fixing issues with VoIP.

[UWPX `v.0.30.0.0`](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.30.0.0) has been released and with it comes a first experimental implementation of [XEP-0313 (MAM)](https://xmpp.org/extensions/xep-0313.html). Besides the introduction of [XEP-0313 (MAM)](https://xmpp.org/extensions/xep-0313.html) to [UWPX](https://uwpx.org/) a bunch of smaller bugs have been fixed and the overall [XEP-0384 (OMEMO Encryption)](https://xmpp.org/extensions/xep-0384.html) experience has been improved. Those were all the features that made it into the current release, but there is far more to come in the future since [COM8](https://github.com/COM8) is working on upgrading his [XEP-0384 (OMEMO Encryption)](https://xmpp.org/extensions/xep-0384.html) to the latest version (`0.7.0 (2020-09-05)`). Besides that a complete database overhaul is also work in progress (switch from [SQLite-net DB](https://github.com/praeclarum/sqlite-net) to the [Entity Framework Core](https://docs.microsoft.com/en-us/ef/core/)).

## Servers

[ejabberd 20.12 has been released](https://www.process-one.net/blog/ejabberd-20-12/), including several new features and many improvements & bugfixes (e.g. new authentification methods, and database drivers).

[Openfire 4.6.1](https://discourse.igniterealtime.org/t/openfire-4-6-1-is-released/89430) has been released. This version is largely a bugfix release. It primarily focuses on improving multi-user chat and pubsub functionality when running an Openfire cluster, but also includes other improvements, such as LDAP/AD performance enhancements. You can find all changes in the changelog, which is denoting 33 issues resolved since 4.6.0.

## Libraries

Gajim’s XMPP library [python-nbxmpp had its 2.0.0 release](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog), adding support for [XEP-0106: JID Escaping](https://xmpp.org/extensions/xep-0106.html), [XEP-0292: vCard4 Over XMPP](https://xmpp.org/extensions/xep-0292.html), and [XEP-0233: XMPP Server Registration for use with Kerberos V5](https://xmpp.org/extensions/xep-0233.html).

[slixmpp 1.6.0 and 1.7.0 have been released](https://lab.louiz.org/poezio/slixmpp/-/releases#slix-1.7.0). Those releases bring support for many new XEPs (including some MIX XEPs), along with fixes, and improvements.

Ignite Realtime developers are [happy to announce Smack 4.4.0](https://discourse.igniterealtime.org/t/smack-4-4-0-released/89283), which is the first major release since the release of Smack 4.3.0 in August 2018 and includes many new features, bug fixes, and improvements.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Service Outage Status](https://xmpp.org/extensions/inbox/service-outage-status.html)
    -   This document defines an XMPP protocol extension that enables a server to communicate issues with the server to all users in a semantic manner.

### New

-   Version 0.1.0 of [XEP-0454](https://xmpp.org/extensions/xep-0454.html) (OMEMO Media sharing)
    -   An informal way of sharing media files despite limitations in the OMEMO encryption
    -   Accepted by vote of Council on 2021-01-13.

-   Version 0.1.0 of [XEP-0453](https://xmpp.org/extensions/xep-0453.html) (DOAP usage in XMPP)
    -   This specification defines how XMPP projects can provide a machine-readable description of their abilities, and how external entities can interact with it.
    -   Accepted by vote of Council on 2021-01-13.

-   Version 0.1.0 of [XEP-0452](https://xmpp.org/extensions/xep-0452.html) (MUC Mention Notifications)
    -   This specification documents how a user may be informed when they're mentioned in a MUC which they're not currently joined to.
    -   Accepted by vote of Council on 2021-01-06.

-   Version 0.1.0 of [XEP-0451](https://xmpp.org/extensions/xep-0451.html) (Stanza Multiplexing)
    -   This spec provides a mechanism for multiplexing multiple virtual hosts over a single XMPP session.
    -   Accepted by vote of Council on 2020-12-09.

-   Version 0.1.0 of [XEP-0450](https://xmpp.org/extensions/xep-0450.html) (Automatic Trust Management (ATM))
    -   This document specifies a way to automatically manage the trust in public long-term keys used by end-to-end encryption protocols.
    -   Accepted by vote of Council on 2020-12-02.

### Deferred

If an experimental XEP is not updated for more than six months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 1.1.0 of [XEP-0393](https://xmpp.org/extensions/xep-0393.html) (Message Styling)
    -   Clarify parsing rules for span directives (sw)

-   Version 1.1 of [XEP-0176](https://xmpp.org/extensions/xep-0176.html) (Jingle ICE-UDP Transport Method)
    -   Make the 'foundation' attribute a string instead of an unsignedByte.
    -   Make the 'network' attribute optional, and add a mapping to SDP. (egp)

-   Version 0.4.0 and 0.5.0 of [XEP-0372](https://xmpp.org/extensions/xep-0372.html) (References)
    -   Specify counting should be of code points. (kis)
    -   Specify that begin is inclusive, starts counting at zero, and that end is exclusive (Dijkstra-based convention) (gh/jcbrand)

-   Version 0.2.0 and 0.3.0 of [XEP-0434](https://xmpp.org/extensions/xep-0434.html) (Trust Messages (TM))
    -   Clarify usage of trust messages by protocols such as Automatic Trust Management (ATM) ([XEP-0450](https://xmpp.org/extensions/xep-0450.html))
    -   Use namespace 'urn:xmpp:atm:0' of Automatic Trust Management (ATM) ([XEP-0450](https://xmpp.org/extensions/xep-0450.html)) as example for 'usage' attribute.
    -   Add section 'Security Considerations'
    -   Improve explanations, descriptions and examples, introduce new attribute and complete all sections:
    -   Remove link to encryption protocol namespaces.
    -   Add short name
    -   Shorten and improve introduction.
    -   Use emphasizing text formatting instead of quotation marks.
    -   Add new section for explaining the core properties of trust messages.
    -   Add examples comparing trust messages to public key certificates.
    -   Improve description of trust message structure.
    -   Introduce 'usage' attribute for 'trust-message' element.
    -   Focus on  and adjust examples accordingly.
    -   Complete sections 'IANA Considerations', 'XMPP Registrar Considerations' and 'XML Schema'. (melvo)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   [XEP-0381](https://xmpp.org/extensions/xep-0381.html) Internet of Things Special Interest Group (IoT SIG)
-   [XEP-0429](https://xmpp.org/extensions/xep-0429.html) Special Interests Group End to End Encryption

### Draft

-   No Drafts this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to Axel Reimer, COM8, deuill, emus, horazont, Licaon_Kter, melvo, pitchum, SamWhited, wurstsalat3000 and zash for their help in creating it!

See you in the next year, stay safe!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

{{< newsletter-subscribe >}}

## Help us to build the newsletter

We started drafting in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days) but also the current new issue in the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3) and we are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. 

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

