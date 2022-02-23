---
title: The XMPP Newsletter September 2021
author: emus
date: 2021-10-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter covering the month of September 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom.

Other than that - enjoy reading!

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- The French translation appears at [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- The German translation appears at [anoxinon.de](https://anoxinon.de/blog/)
- The Italian translation appears at [NicFab.it](https://www.nicfab.it/)

Many thanks to the translators and their work! This is a great help to spread the news! Please join them in their work or start over with another language!

## XSF Announcements

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects now! Please apply via Open Collective. For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/).

The XSF is planning to participate the Google Summer of Code 2022 (GSoC). If you are interested in participating as a student, mentor or as project in general please [add your ideas and reach out to us](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022)!

Furthermore, the [xmpp.org](https://xmpp.org) website received an update. It's now built using [Hugo](https://gohugo.io/) (instead of Pelican) which reduces maintenance effort significantly. The new website is based on Bootstrap 5, and has been developed with simplicity in mind. We also made sure to make contributions as easy as possible. Building the website locally requires a minimum of dependencies, and is possible via Docker and Vagrant as well.

## Events

[XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours) - Also, checkout our new [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of the month.

## Articles

OpenPGP for XMPP (OX) is slowly getting client implementations. In a German blog post, DebXWoody walks us step by step through the process of [enabling OX and using it in Profanity](https://mov.im/?blog/debxwoody%40movim.eu/profanity-und-openpgp-for-xmpp-ox-YRMREh).

The Libervia ActivityPub Gateway work continues, with [a report](https://www.goffi.org/b/libervia-progress-note-2021-w38--flt) about Full-Text Search for PubSub cache and an early, but functional, ActivityPub XMPP Component.

![Libervia](/images/newsletter/september2021/libervia.jpg "Libervia")

Matthew Wild has published a web utility for exploring [XEP-0392 "Consistent Color Generation"](https://xmpp.org/extensions/xep-0392.html). This XEP advises clients on how to colourize a user's contacts (e.g. their nicknames or default avatars) for easier visual identification. The XEP describes a standard algorithm that aims to provide a distinctive colour for any contact, with considerations for colour vision deficiencies, and allowing all of a user's clients to display the same colour for a given contact. Check out the [XEP-0392 colour explorer](https://matthewwild.co.uk/projects/xep0392-web/) and the [Modern XMPP colour guidance](https://docs.modernxmpp.org/client/design/#auto-generated-colors).

Ever wanted a web clients comparison between XMPP and Matrix? You're in luck as [Ade Malsasa Akbar](https://floss.social/@ademalsasa) has written [a simple overview](https://www.ubuntubuzz.com/2021/09/element-and-movim-messengers-comparison-made-simple.html) of two group chat messengers from the decentralization family, Element of Matrix and Movim of XMPP. This is a discussion of usability from an end user perspective without talking about technology stuff like security or protocols.

## Software news

### Clients and applications

[Dino v0.2.2 has been released](https://github.com/dino/dino/releases/tag/v0.2.2). This version is a maintenance release and includes bug fixes.

UWPX [v.0.35.1.0](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.35.1.0) and [v.0.36.0.0](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.36.0.0) have been released. [v.0.35.1.0](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.35.1.0) finally added push support with the [push server](https://github.com/UWPX/UWPX-Push-Server) developed by [COM8](https://github.com/COM8). [v.0.36.0.0](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.36.0.0) of UWPX fixes a bunch of bugs and updated the UI to [WinUI 2.7](https://docs.microsoft.com/en-us/windows/apps/winui/winui2/release-notes/winui-2.7). Besides that, a new [OMEMO status indicator](https://user-images.githubusercontent.com/11741404/135456998-5a0c9e0a-181c-46ab-ae94-3dff8e3b947e.png) got introduced which should help you check if your contacts support the latest OMEMO standard.

[XMPP-DNS](https://salsa.debian.org/mdosch/xmpp-dns), a tool to look up XMPP SRV records and test connectivity, had its initial release of [v0.1.0](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.1.0). The release was directly followed by [v0.2.0](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.2.0), bringing support for the XMPPS-server SRV records and a small bugfix release [v0.2.1](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.2.1).

[Gajim development news](https://gajim.org/post/2021-09-29-development-news-september/): September brought many updates under the hood. With big changes coming up in Gajim 1.4, many parts of the code have to be touched. These changes remain mostly invisible for users, but make Gajim more robust. In some cases, this results in visible improvements as well: Both Add Contact and Start Chat windows are now detecting the type of chat behind an address.

[Go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp), one of various [alternatives](https://wiki.xmpp.org/web/User:MDosch/Sendxmpp_incarnations) to the original [sendxmpp](https://sendxmpp.hostname.sk/), released versions [v0.1.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.1.0) and [v0.1.1](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.1.1).

Conversations and Quicksy got version [2.10.0](https://github.com/iNPUTmice/Conversations/releases/tag/2.10.0) out this month, with a short changelog: black bars on video calls (so you know when "you're holding it wrong"), search performance improvements and a new setting to block app screenshots. Under the hood there was more: two bugs fixed for file attachments (specially for users with a lot of media files), touching the titlebar will open chat details and nested quotes (not yet the default, but you can "copy" and then "paste as quote" to use them).

Converse is going forward after a lot of development. [Version 8 of this JavaScript XMPP chat client that runs in your browser](https://opkode.com/blog/2021-09-13-converse-8/) was released. [JC Brand](https://opkode.com)'s blog post covers the visible changes (message styling, OMEMO encrypted files, URL previews) but also the internal changes (IndexDB by default, web components). [8.0.1](https://github.com/conversejs/converse.js/releases/tag/v8.0.1) followed shortly with bug fixes to the polished product.

![Converse](/images/newsletter/september2021/converse-fullscreen.png "Converse")

Profanity [0.11.1](https://github.com/profanity-im/profanity/releases/tag/0.11.1) has been released improving upon themes, notifications and OMEMO handling.

The Mellium Dev Communiqué for September has been published. It includes minor updates to the [Communiqué TUI client](https://mellium.im/communique/) as well as the [mellium.im/xmpp](https://pkg.go.dev/mellium.im/xmpp) library. Full details in [Dev Communiqué for September 2021](https://opencollective.com/mellium/updates/dev-communique-for-september-2021) on their [Open Collective](https://opencollective.com/mellium) page.

## Servers

No news on XMPP servers have reached us this month. :-(

## Libraries

Mellium has released v0.20.0 of their Go XMPP library. The release announcement can be found on [Open Collective](https://opencollective.com/mellium/updates/release-mellium-im-xmpp). Some of the bigger features include group chat (MUC), chat history (MAM), and ad-hoc command support!

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

-   Version 0.8.0 of [XEP-0384](https://xmpp.org/extensions/xep-0384.html) (OMEMO Encryption)
    -   Update to [XEP-0420](https://xmpp.org/extensions/xep-0420.html) version 0.4.0 and adjust namespace
    -   Replace SCE's old 'content' element by its new 'envelope' element
    -   Replace SCE's old 'payload' element by its new 'content' element
    -   Update SCE's namespace to 'urn:xmpp:sce:1'
    -   Update namespace to 'urn:xmpp:omemo:2' (melvo)

-   Version 0.14.0 of [XEP-0280](https://xmpp.org/extensions/xep-0280.html) (Message Carbons)
    -   Incorporate LC feedback: Remove requirement to remove "private" elements (and add interop note), completely reword mobile considerations to fit modern reality. (gl)

-   Version 1.1 of [XEP-0227](https://xmpp.org/extensions/xep-0227.html) (Portable Import/Export Format for XMPP-IM Servers)
    -   Discourage use of 'password', provide a way to include SCRAM credentials, PEP nodes and message archives. (mw)

-   Version 1.22.0 of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Remove exception for last item when purging a node: all items must be removed. (jp)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   [XEP-0459](https://xmpp.org/extensions/xep-0459.html) XMPP Compliance Suites 2022

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

-   No Stable this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the XMPP community.

Therefore many thanks to Adrien Bourmault (neox), Benoît Sibaud, emus, palm123, Licaon_Kter, MattJ, mdosch, nicola, seveso, Sam Whited, SouL, wurstsalat3000, Ysabeau for their support and help in creation, review and translation!

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
