---
title: The XMPP Newsletter December 2021 & January 2021
author: emus
date: 2022-02-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter covering the month of December 2021 and January 2021!

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom.

Other than that — enjoy reading!

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- The French translation appears at [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- The German translation appears at [anoxinon.de](https://anoxinon.de/blog/)
- The Italian translation appears at [NicFab.it](https://www.nicfab.it/)

Many thanks to the translators and their work! This is a great help to spread the news! Please join them in their work or start over with any another language!

## XSF Announcements

- The XSF members have to elected their new [XSF Board and XSF Council](https://xmpp.org/about/xmpp-standards-foundation/#council)! Congratulations to everyone!

- The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects now! Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/).

    - Moreover, the XSF has accepted its first project to the fiscal hosting program! A big welcome to the [MAM Plugin for XMPP.js](https://gitlab.com/deblounge/xmppjs-mam-plugin) (note that this is unaffiliated with the upstream [xmpp.js](https://github.com/xmppjs/xmpp.js) project)! They will be working on adding MAM support to xmpp.js with the eventual goal of adding it to the Matrix Bifrost bridge, allowing XMPP users to fetch history from their favorite Matrix channels. You can [donate to the effort here](https://opencollective.com/bifrost-mam).

- The XSF is planning to participate the Google Summer of Code 2022 (GSoC). If you are interested in participating as a student, mentor or as project in general please [add your ideas and reach out to us](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022)!

- Blog and newsletter pages at [xmpp.org/blog](https://xmpp.org/blog) now support multiple languages. We are happy for volunteers to support translating!

## Events

[XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours) - Also, checkout our new [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of the month.

## Videos

Sam Whited gave a [talk for the XMPP Office Hours](https://www.youtube.com/watch?v=lprIwxyPY2E) about the XSF's new fiscal hosting service!

Guest talk at Berlin XMPP Meetup: [Diving deep into Briar at the XMPP Meetup Berlin](https://nico.dorfbrunnen.eu/posts/2021/diving-at-xmpp/)

## Articles

_Please be so kind and write some sentences for the news you place instead of just dropping bare HTTP links - that will help us a lot! <3_

JMP.chat released two blog posts.  [The first](https://blog.jmp.chat/b/2022-jabber-xmpp-from-sms) details a feature of the Soprani.ca project's Cheogram system that allows SMS users to contact (or call!) any XMPP address.  [Their Newsletter](https://blog.jmp.chat/b/january-newsletter-2022) also announces a partnership with Snikket for hosting, as well as a preview of worldwide calling rates as they prepare to launch that feature soon.

## Software news

### Clients and applications

_Please be so kind and write some sentences for the news you place instead of just dropping bare HTTP links - that will help us a lot! <3_

## Servers

_Please be so kind and write some sentences for the news you place instead of just dropping bare HTTP links - that will help us a lot! <3_

## Libraries

_Please be so kind and write some sentences for the news you place instead of just dropping bare HTTP links - that will help us a lot! <3_

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Compatibility Fallbacks](https://xmpp.org/extensions/inbox/compatibility-fallback.html)
    -   This document defines a way to indicate that a specific part of the body only serves as fallback and which specification the fallback is for.

-   [Call Invites](https://xmpp.org/extensions/inbox/call-invites.html)
    -   This document defines how to invite someone to a call and how to respond to the invite.

-   [PubSub Namespaces](https://xmpp.org/extensions/inbox/pubsub-ns.html)
    -   This extension defines a new PubSub node attribute to specify the type of payload.

-   [Message Replies](https://xmpp.org/extensions/inbox/replies.html)
    -   This document defines a way to indicate that a message is a reply to a previous message.

### New

-   No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 1.1.0 of [XEP-0363](https://xmpp.org/extensions/xep-0363.html) (HTTP File Upload)
    -   Filename size in bytes.
    -   Headers MUST be included in the PUT request.
    -   Headers considered opaque.
    -   Servers may want to sign headers, in security implications.
    -   Allow header case insensitivity, multiple times the same header, and preserve the order in the HTTP request. (egp, mb)
    
-   Version 0.4.0 of [XEP-0353](https://xmpp.org/extensions/xep-0353.html) (Jingle Message Initiation)
    -   Rework whole spec, namespace bump
    -   Add new <finish/> message
    -   Add dependency on ,  and
    -   Add <reason/> to some messages (tm)

-   Version 1.1.0 of [XEP-0459](https://xmpp.org/extensions/xep-0459.html) (XMPP Compliance Suites 2022)
    -   Replace deprecated XEP-0411 with XEP-0402 in Advanced Group Chat (egp)

-   Version 0.4.0 of [XEP-0380](https://xmpp.org/extensions/xep-0380.html) (Explicit Message Encryption)
    -   Add new OMEMO namespaces: 'urn:xmpp:omemo:1' for OMEMO versions since 0.4.0, and 'urn:xmpp:omemo:2' for OMEMO versions since 0.8.0 (melvo)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   Last Call for comments on [XEP-0424](https://xmpp.org/extensions/xep-0424.html) (Message Retraction)
-   Last Call for comments on [XEP-0425](https://xmpp.org/extensions/xep-0425.html) (Message Moderation)

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

-   No XEPs advanced to Stable this month.

### Deprecated

-   [XEP-0256](https://xmpp.org/extensions/xep-0256.html) (Last Activity in Presence)

### Obsoleted

-   [XEP-0443](https://xmpp.org/extensions/xep-0443.html) (XMPP Compliance Suites 2021)

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the XMPP community.

Therefore many thanks to xdelatour, wurstsalat3000, seveso, palm123, Nicola Fabiano, mdosch, MattJ, Licaon_Kter, Goffi, erszcz, emus, Benoît Sibaud, Anoxinon e.V., Adrien Bourmault (neox) for their support and help in creation, review and translation!

Many thanks to all contributors and their continuous support!

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

Tasks we do on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Preparation for media images
- Translations: especially German, French, Italian and Spanish

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
