---
title: The XMPP Newsletter October 2021
author: emus
date: 2021-11-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter covering the month of October 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom.

Other than that — enjoy reading!

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- The French translation appears at [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- The German translation appears at [anoxinon.de](https://anoxinon.de/blog/)
- The Italian translation appears at [NicFab.it](https://www.nicfab.it/)

Many thanks to the translators and their work! This is a great help to spread the news! Please join them in their work or start over with another language!

## XSF Announcements

- The XSF members have to elect the upcoming XSF Board and Council soon. If you are interested in running for XSF Board (business related) or XSF Council (technical related) for the 2021—2022 term, please [create an appropriate Wiki page by November 7th, 2021 and link it from here](https://wiki.xmpp.org/web/Board_and_Council_Elections_2021)

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

After being featured in the [September 2021](https://xmpp.org/2021/10/the-xmpp-newsletter-september-2021/) newletter with a Movim & Element web client comparison, [Ade Malsasa Akbar](https://floss.social/@ademalsasa) is back with [a short tutorial](https://www.ubuntubuzz.com/2021/10/how-to-voice-video-calls-on-xmpp-and-matrix-made-simple.html) on how to use Audio and Video calls in these clients.

Have you heard about [Bad XMPP](https://badxmpp.eu/)? Well, it is actually good - you can test your clients and servers against a set of intentionally badly configured XMPP services. Happy debugging!

![BadXMPP](/images/newsletter/october2021/bad_xmpp.png "BadXMPP")

The jmp.chat service blog [announced](https://blog.jmp.chat/b/october-newsletter-2021) some changes to the SIP inbound calling feature, so users are advised  to configure it via the new interactive bot. On the iOS side Snikket is now the recommended app as some helpful functions (like calling tones) got sponsored.

Aria Network wrote a follow-up blog post on [UX improvements such as avatars of the Bifrost bridge to Matrix](https://aria-net.org/SitePages/Bifrost-Improvements.aspx). The previous article was ["Conversion of communities to spaces, new Bifrost features"](https://aria-net.org/SitePages/Regarding-spaces-and-Bifrost.aspx).

## Software news

### Clients and applications

Following last month's Conversations and Quicksy releases of 2.10.0, a [2.10.1 point release](https://github.com/iNPUTmice/Conversations/releases/tag/2.10.1) comes with a new internal library for video compression, which allows more devices to send smaller files. Conversations will now be included in Android backups (be it Seedvault or Google's) but only if encrypted. Furthermore, there have been address book fixes so contact addresses are picked up easier. Finally there have been fixes for notifications, which allow to start downloads properly and send MUC PMs to the right contact.

[Gajim 1.3.3 has been released](https://gajim.org/post/2021-10-10-gajim-1.3.3-released/). This release features improved Ad-Hoc Commands and brings back spell checking. Gajim 1.3.3 includes many bug fixes and improvements. Also this month: two years of Gajim Development News! In October, Gajim’s event system received significant changes. These changes lead to improvements in notifications mainly, but also made it possible to display Jingle File Transfers directly in the chat view. Another nice addition: search filters which help narrow down your search.

[Version 2.10.2 of the Snikket Android app has been released](https://fosstodon.org/@snikket_im/107161786225773950)! The main highlight of this release is the new dialpad which allows you to navigate automated call systems when using a Jingle to PSTN bridge.

New beta versions of [Beagle IM and Siskin IM have been released](https://mastodon.technology/@tigase/107161741669699519) for MacOS and iOS with support for location sharing.

![Beagle IM Locations](/images/newsletter/october2021/beagle-location.jpg "Beagle IM Locations")

## Servers

The Openfire plugin for Push Notification got a small bug fix, so server admins are advised to update to [the new 0.9.0 version](https://discourse.igniterealtime.org/t/push-notification-openfire-plugin-0-9-0-released/90934).

## Libraries

Development on [mellium.im/xmpp](https://mellium.im/xmpp) (an XMPP library in Go) has been slower than usual this month. We've primarily been focused on rolling out basic pubsub, PEP, and PEP Native Bookmarks support and the basics are already merged into the main branch. For more information, see the [latest Dev Communiqué](https://opencollective.com/mellium/updates/dev-communique-for-october-2021).

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   No XEPs proposed this month.

### New

-   No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 0.8.0 of [XEP-0392](https://xmpp.org/extensions/xep-0392.html) (Consistent Color Generation)
    -   Remove Color Vision Deficiency correction algorithms and substitute them with a better recommendation. (jsc)

-   Version 0.5 of [XEP-0355](https://xmpp.org/extensions/xep-0355.html) (Namespace Delegation)
    -   delegation of Remaining Discovery Infos
    -   delegation of Bare JID Disco Items
    -   Security Consideration about disco requests
    -   namespace bump
    -   typos (jp)

-   Version 0.8.0 of [XEP-0313](https://xmpp.org/extensions/xep-0313.html) (Message Archive Management)
    -   Update groupchat-messages-in-user-archive advice, introducing fields and disco features to make behaviour explicit in future implementations, in light of Last Call feedback. (ks)

-   Version 0.4.0 of [XEP-0450](https://xmpp.org/extensions/xep-0450.html) (Automatic Trust Management (ATM))
    -   Update to [XEP-0434](https://xmpp.org/extensions/xep-0434.html) version 0.6.0 and [XEP-0384](https://xmpp.org/extensions/xep-0384.html) version 0.8.0
    -   Use Base64-encoded key identifiers in examples
    -   Update TM's namespace to `urn:xmpp:tm:1`
    -   Update OMEMO's namespace to `urn:xmpp:omemo:2` (melvo)

-   Version 0.6.0 of [XEP-0434](https://xmpp.org/extensions/xep-0434.html) (Trust Messages (TM))
    -   Specify key identifier encoding, improve glossary and update to [XEP-0384](https://xmpp.org/extensions/xep-0384.html) version 0.8.0
    -   Specify usage of Base64 encoding for key identifiers within trust messages
    -   Specify usage of Base16 encoding for key identifiers within Trust Message URIs
    -   Use Base64-encoded key identifiers in examples
    -   Add 'hash value' as example of key identifier
    -   Update OMEMO's namespace to `urn:xmpp:omemo:2`
    -   Update namespace to `urn:xmpp:tm:1` (melvo)

-   Version 0.5.0 of [XEP-0401](https://xmpp.org/extensions/xep-0401.html) (Ad-hoc Account Invitation Generation)
    -   Factor out [XEP-0445](https://xmpp.org/extensions/xep-0445.html) (gl)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   [XEP-0379](https://xmpp.org/extensions/xep-0379.html) Pre-Authenticated Roster Subscription
-   [XEP-0401](https://xmpp.org/extensions/xep-0401.html) Ad-hoc Account Invitation Generation
-   [XEP-0445](https://xmpp.org/extensions/xep-0445.html) Pre-Authenticated In-Band Registration

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

-   Version 1.0.0 of [XEP-0280](https://xmpp.org/extensions/xep-0280.html) (Message Carbons)
    -   Advance to Stable as per Council Vote from 2021-09-29. Unbelievable. (jsc (XEP Editor))

### Deprecated

-   Version 1.1.0 of [XEP-0411](https://xmpp.org/extensions/xep-0411.html) (Bookmarks Conversion)
    -   Deprecated by vote of Council on 2020-10-06. (XEP Editor (jsc))

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the XMPP community.

Therefore many thanks to Adrien Bourmault (neox), Anoxinon e.V., Benoît Sibaud, emus, Julien Jorge, Licaon_Kter, MattJ, mdosch, Nicola Fabiano, seveso, Sam Whited, SouL, wojtek, wurstsalat3000, Ysabeau for their support and help in creation, review and translation!

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
