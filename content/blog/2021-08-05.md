---
title: The XMPP Newsletter July 2021
author: emus
date: 2021-08-05
categories: ["Newsletter"]
aliases:
    "/2021/07/newsletter-07-july/"
---

Welcome to the XMPP Newsletter covering the month of July 2021.

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

Currently, the XSF members are voting on [new members and reapplying members](https://wiki.xmpp.org/web/Membership_Applications_Q3_2021). The member meeting will be hold on August 19th 2021, 19:00 UTC to formally approve the voting results. [XSF group chat (MUC)](xmpp:xsf@muc.xmpp.org?join)
If you are interested to joining the XSF you can [apply beginning of Q4 2021](https://xmpp.org/community/membership.html), too!

Since this month a new sub-domain is also available at xmpp.net: data.xmpp.net. Many thanks to MattJ! The first data project being hosted here for everyones access are the [providers lists (JSON format)](https://data.xmpp.net/providers/v1/providers-A.json) from the [XMPP Providers project](https://invent.kde.org/melvo/xmpp-providers). There are already first client implementation using these - please review the [criteria](https://invent.kde.org/melvo/xmpp-providers/-/blob/master/README.md) and add you service as well via the Gitlab repository! Feedback welcome!

## Events

[XMPP Office Hours each week](https://wiki.xmpp.org/web/XMPP_Office_Hours) - Also, checkout our new [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of the month.

## Videos

XMPP Office Hours: [Building a Chat Bot on Ad Hoc Commands](https://www.youtube.com/watch?v=e1-hpsQ9OZE)

## Articles

With the very first article we would like to bring attention to a general serious topic: [Burnout in open-source communities](https://opensource.com/article/21/7/burnout-open-source). Please take care of yourself, seek help and also have an eye even on your virtual colleagues! Searching for help in your current location may be more satisfying, however this could be a start:
- [Psychology Today](https://www.psychologytoday.com/intl/basics/therapy/finding-help-others)
- [How to find therapy](https://www.thecut.com/article/how-to-find-a-therapist.html)

The Debian XMPP Team blog [announced all the goodies](https://xmpp-team.pages.debian.net/blog/2021/07/xmpp-novelties-in-debian-11-bullseye.html) the soon to be released Debian 11 will bring. While these might not be 'new' for newsletter readers, they'll improve the experience for users of Debian Stable significantly.

Seth Kenlon, from Red Hat, published two articles on the XML markup language (a quite important thing in the XMPP world ;) ) at [opensource.com](https://opensource.com). Starting with [What is XML?](https://opensource.com/article/21/7/what-xml) and following up by [Use XMLStarlet to parse XML in the Linux terminal](https://opensource.com/article/21/7/parse-xml-linux).

## Software news

### Clients and applications

[Gajim News](https://gajim.org/post/2021-07-28-development-news-july/): Development on the new Gajim version continued in July, bringing many fixes and improvements. Also this month: WebSocket improvements and a new python-nbxmpp release.

Profanity [0.11.0](https://github.com/profanity-im/profanity/releases/tag/0.11.0) is out, bringing six months of polishing to 0.10.0. This includes message archive management (MAM) support (still experimental), support for changing the password, abilities in group chats (MUC) like voice and registration, OMEMO trust mode, private messages (MUC-PM) in public channels, spam reporting, server contact discovery, and much more.

[Jan-Philipp Litza](https://github.com/jplitza) built an XMPP feed integration for the German official warning app NINA: [Find the Github repository here](https://github.com/jplitza/nina-xmpp). One can simply [add the bot and register coordinates of interest](https://github.com/jplitza/nina-xmpp/blob/master/README.md). May it never contact you!

UWPX [v.0.34.0.0](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.34.0.0) has been released. This release mostly focuses on bug fixes for the first beta release of UWPX with an ETA of 01.09.2021 and proper push support even if the app is not running. For this [COM8](https://github.com/COM8) has been working on its C++ [push server](https://github.com/UWPX/UWPX-Push-Server) for the last couple of months and it is finally up and running. Besides that, this release also includes XEP-0085 (Chat State Notifications) improvements with a proper [typing indicator](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.34.0.0) and status messages.

## Servers

ejabberd 21.07 has been [released](https://www.process-one.net/blog/ejabberd-21-07/) with a plethora of fixes and improvements, so be sure to read the changelog if you're using shared groups and MySQL. Big changes have been implemented pertaining to the build system, as ejabberd can now be built using [rebar3](https://rebar3.org/) and [Elixir Mix](https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html).

For OpenFire an update for the [plugin 'inVerse' has been published](https://discourse.igniterealtime.org/t/inverse-plugin-for-openfire-reaches-7-0-6-2/90440) and it makes the [Converse.js web client](https://conversejs.org/) available for its users.

## Libraries

[python-nbxmpp 2.0.3](https://gajim.org/post/2021-07-28-development-news-july/) has been released.

[Mellium Dev Communiqué](https://opencollective.com/mellium/updates/dev-communique-for-july-2021): Development continued apace this month and included the usual assortment of bug fixes and improvements. In addition, carbons, MUC, and Roster Versioning were all implemented!

Smack, a Java XMPP client library has been [released in version 4.4.3](https://discourse.igniterealtime.org/t/smack-4-4-3-released/90436) with mostly bugfixes.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Disco Feature Attachment](https://xmpp.org/extensions/inbox/disco-feature-attachment.html)
    -   This specification provides a way to indicate that a feature is implemented for a specific namespace

-   [Pubsub Caching Hints](https://xmpp.org/extensions/inbox/pubsub-caching-hints.html)
    -   This specification provides a way to get caching information from a Pubsub node

### New

-   No new XEP this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   [XEP-0328](https://xmpp.org/extensions/xep-0328.html) (JID Preparation and Validation Service)
-   [XEP-0333](https://xmpp.org/extensions/xep-0333.html) (Chat Markers)
-   [XEP-0357](https://xmpp.org/extensions/xep-0357.html) (Push Notifications)
-   [XEP-0380](https://xmpp.org/extensions/xep-0380.html) (Explicit Message Encryption)
-   [XEP-0392](https://xmpp.org/extensions/xep-0392.html) (Consistent Color Generation)
-   [XEP-0398](https://xmpp.org/extensions/xep-0398.html) (User Avatar to vCard-Based Avatars Conversion)
-   [XEP-0401](https://xmpp.org/extensions/xep-0401.html) (Easy User Onboarding)
-   [XEP-0413](https://xmpp.org/extensions/xep-0413.html) (Order-By)
-   [XEP-0414](https://xmpp.org/extensions/xep-0414.html) (Cryptographic Hash Function Recommendations for XMPP)
-   [XEP-0415](https://xmpp.org/extensions/xep-0415.html) (XMPP Over RELOAD (XOR))
-   [XEP-0416](https://xmpp.org/extensions/xep-0416.html) (E2E Authentication in XMPP)
-   [XEP-0417](https://xmpp.org/extensions/xep-0417.html) (E2E Authentication in XMPP: Certificate Issuance and Revocation)
-   [XEP-0418](https://xmpp.org/extensions/xep-0418.html) (DNS Queries over XMPP (DoX))
-   [XEP-0421](https://xmpp.org/extensions/xep-0421.html) (Anonymous unique occupant identifiers for MUCs)
-   [XEP-0422](https://xmpp.org/extensions/xep-0422.html) (Message Fastening)
-   [XEP-0424](https://xmpp.org/extensions/xep-0424.html) (Message Retraction)
-   [XEP-0425](https://xmpp.org/extensions/xep-0425.html) (Message Moderation)
-   [XEP-0426](https://xmpp.org/extensions/xep-0426.html) (Character counting in message bodies)
-   [XEP-0427](https://xmpp.org/extensions/xep-0427.html) (MAM Fastening Collation)
-   [XEP-0428](https://xmpp.org/extensions/xep-0428.html) (Fallback Indication)
-   [XEP-0430](https://xmpp.org/extensions/xep-0430.html) (Inbox)
-   [XEP-0431](https://xmpp.org/extensions/xep-0431.html) (Full Text Search in MAM)
-   [XEP-0432](https://xmpp.org/extensions/xep-0432.html) (Simple JSON Messaging)
-   [XEP-0433](https://xmpp.org/extensions/xep-0433.html) (Extended Channel Search)
-   [XEP-0435](https://xmpp.org/extensions/xep-0435.html) (Reminders)
-   [XEP-0436](https://xmpp.org/extensions/xep-0436.html) (MUC presence versioning)
-   [XEP-0437](https://xmpp.org/extensions/xep-0437.html) (Room Activity Indicators)
-   [XEP-0439](https://xmpp.org/extensions/xep-0439.html) (Quick Response)

### Updated

-   Version 1.0.0 of [XEP-0429](https://xmpp.org/extensions/xep-0429.html) (Special Interests Group End to End Encryption)
    -   Accepted by Council (XEP Editor: jsc)

-   Version 0.2 of [XEP-0413](https://xmpp.org/extensions/xep-0413.html) (Order-By)
    -   Add a way to discover on which protocols Order-By applies
    -   Remove references to SQL (except in implementation notes)
    -   Specify that order-by operate on the whole item set and inside a RSM result set
    -   Explicitly says that creation and modification dates are set by Pubsub service itself
    -   Specify that Clark notation should be used for extensions
    -   Add a full example with Pubsub and RSM
    -   Add hint for SQL based implementations removed [XEP-0060](https://xmpp.org/extensions/xep-0060.html) and [XEP-0313](https://xmpp.org/extensions/xep-0313.html) as dependencies, they are mentioned as use cases, but are not mandatory
    -   Better wording following feedback
    -   Namespace bump (jp)

-   Version 1.0.0 of [XEP-0381](https://xmpp.org/extensions/xep-0381.html) (Internet of Things Special Interest Group (IoT SIG))
    -   Accepted by Council (XEP Editor: jsc)

-   Version 0.2.0 of [XEP-0383](https://xmpp.org/extensions/xep-0383.html) (Burner JIDs)
    -   Improve security considerations and add listing JIDs. (ssw)

-   Version 0.2.0 of [XEP-0458](https://xmpp.org/extensions/xep-0458.html) (Community Code of Conduct)
    -   Integrate various comments from various sources (dwd)

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

Therefore many thanks to Adrien Bourmault, Benoît Sibaud, DebXwoody, COM8, emus, mattJ, neox, Licaon_Kter, pmaziere, raspbeguy, wurstsalat3000, Ysabeau for their support and help in creation, review and translation!

## Spread the news!

Please share the news via other networks:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

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
