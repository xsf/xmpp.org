---
title: The XMPP Newsletter November 2021
author: emus
date: 2021-12-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter covering the month of November 2021 - the last release for this year! After our editorial break we will be back in February 2022!

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

[PeerTube Live Chat is using XMPP](https://joinpeertube.org/news#live-plugin-app): Give your instance's audience the ability to chat during live streams!

Using XMPP instead of ActivityPub? Well, [openEngiadina decided to do so](https://inqlab.net/2021-11-12-openengiadina-from-activitypub-to-xmpp.html)!

Missed for the [September '21](https://xmpp.org/2021/10/the-xmpp-newsletter-september-2021/) newsletter, [Nicholas A. Ferrell](https://emucafe.club/channel/naferrell) has written about their [transition to XMPP for SMS communication](https://thenewleafjournal.com/sending-sms-messages-from-my-computer-with-xmpp-through-jmp/) via [jmp.chat](https://jmp.chat/).

[Nicola Fabiano](https://www.nicfab.it/) is back with another article about why they chose XMPP, and more specifically hosting [Snikket](https://snikket.org/) to have [control over personal information](https://www.nicfab.it/en/xmpp-is-a-solution-that-allows-users-to-have-control-over-their-personal-information-our-choice-snikket/). Article also available in [Italian](https://www.nicfab.it/xmpp-e-una-soluzione-che-permette-agli-utenti-di-avere-il-controllo-sulle-loro-informazioni-personali-la-nostra-scelta-snikket/)

[Take Back Our Tech](https://takebackourtech.org) has started a series of articles (and companion video podcasts) about "XMPP: A Comeback Story". First one is called [A 20 Year Old Messaging Protocol For Robust, Private and Decentralized Communications](https://takebackourtech.org/xmpp-comeback/) and covers the 'ecosystem' of apps and servers with a quick starting guide. The second one continues with [Making Anonymous Phone Calls & Texts With JMP.Chat](https://takebackourtech.org/xmpp-jmp/).

Niklas of [gnulinux.ch](https://gnulinux.ch/) asks (in German) "Is the free software community losing its values?", wondering how come participation in free software discussions can no longer take place without using non-free software. Read [the full article](https://gnulinux.ch/verliert-die-free-software-community-ihre-werte) to find out why this matters and what solution exists already.

The jmp.chat blog had two small updates, a guide on [How to Subscribe Using Movim](https://blog.jmp.chat/b/subscribe-using-movim) and [an update](https://blog.jmp.chat/b/november-newsletter-2021) about the official ways to communicate with the community and about the upcoming app (with dialer integration). 

## Software news

### Clients and applications

[Gajim Development News](https://gajim.org/post/2021-11-29-development-news-november/): Annoyed of spam messages in public channels? Gajim just gained support for Message Moderation. Also this month: better message corrections and improved notifications.

![Gajim Message Moderation](/images/newsletter/november2021/gajim-message-moderation.png "Gajim Message Moderation")

[xmpp-dns](https://salsa.debian.org/mdosch/xmpp-dns) was released in version [`0.2.2`](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.2.2), a minor update that added the possibility to fall back on testing default ports if no XMPP SRV records are provided by the server.

[UWPX](https://uwpx.org) was released in version [`0.38.0.0`](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.38.0.0). This release updates the OMEMO implementation from `0.7.0 (2020-09-05)` to `0.8.1 (2021-10-07)` and includes a bunch of OMEMO related bug fixes.

[SiskinIM](https://siskin.im/) version [`7.0`](https://github.com/tigase/siskin-im/releases/tag/7.0) was released. It's a major release with support for [XEP-0333 Chat Markers](https://xmpp.org/extensions/xep-0333.html), location sharing and improved UI/UX, fetching history, cache handling and push improvements alongside number of bugfixes.

[BeagleIM](https://beagle.im/) version [`5.0`](https://github.com/tigase/beagle-im/releases/tag/5.0) was released. It's a major release with support for [XEP-0333 Chat Markers](https://xmpp.org/extensions/xep-0333.html), screen, voice-messages and location sharing, improved UI/UX, fetching history and much more.

[Libervia (formerly "Salut à Toi") `0.8` "La Cecília" has been released](https://www.goffi.org/b/libervia-v0-8-la-cecilia-BdQ4). Libervia is a multi-frontends client with social features such as blogging, photo albums, events organisation, etc. This release is a big milestone, preparing the field to make Libervia a great fit for family and friends focused social networks.

A new major version of [Converse.js](https://conversejs.org/) is out after three months of development, [version `9.0.0`](https://github.com/conversejs/converse.js/releases/tag/v9.0.0) brings compressed avatars, new media render settings and a lot of bugfixes. Admins should read the release notes and update their deployments.

The new Converse.js version also got updated in the [inVerse plugin version `9.0.0.1`](https://discourse.igniterealtime.org/t/inverse-plugin-for-openfire-version-9-0-0-1-released/91075) for the [Openfire server](https://www.igniterealtime.org/projects/openfire/), and should appear in the instance updates list.

## Servers

The new [Snikket server update](https://snikket.org/blog/nov-2021-server-release/) comes with improvements for the user interaction on iOS, an increased file sharing limit, resource monitoring and better account management!

[MongooseIM 5.0](https://github.com/esl/MongooseIM/releases/tag/5.0.0) was released on 7th October! What's new? Dynamic XMPP domains, improved documentation, multiple bug fixes and more. Virtual hosting XMPP domains was already possible with MongooseIM, but dynamic domains make it possible to add new domains without restarting the server - and to add a lot of them! Load tests with up to 100k users have shown that now there's practically no difference between all the users connecting to a single domain and all of them connecting to 100k domains - that is one domain per user - yes, it's that flexible!

## Libraries

The Mellium [Dev Communiqué for November2021](https://opencollective.com/mellium/updates/dev-communique-for-november-2021) has been released! This month work mostly focused on the [carbons package](https://pkg.go.dev/mellium.im/xmpp/carbons) and on creating a re-usable test suite that other libraries can import to test [message styling](https://pkg.go.dev/mellium.im/xmpp/styling).

Openfire Smack publish [version `4.4.4` as patch level release](https://discourse.igniterealtime.org/t/smack-4-4-4-released/90954)!

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

-   Version 0.2.0 of [XEP-0459](https://xmpp.org/extensions/xep-0459.html) (XMPP Compliance Suites 2022)
    -   Rename Advanced Server and Advanced Client to Server and Client
    -   Add XEP-0455 to Future Development section (sp)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   No Last Call this month.

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

-   Version 1.0.0 of [XEP-0459](https://xmpp.org/extensions/xep-0459.html) (XMPP Compliance Suites 2022)
    -   Advance to Stable as per Council Vote from 2021-11-03. (XEP Editor (jsc))

-   Version 1.0.0 of [XEP-0313](https://xmpp.org/extensions/xep-0313.html) (Message Archive Management)
    -   Advance to Stable as per Council Vote from 2021-10-27. (XEP Editor (jsc))

### Deprecated

-   No XEP deprecated this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the XMPP community.

Therefore many thanks to xdelatour, wurstsalat3000, seveso, palm123, Nicola Fabiano, mdosch, MattJ, Licaon_Kter, Goffi, erszcz, emus, Benoît Sibaud, Anoxinon e.V., Adrien Bourmault (neox) for their support and help in creation, review and translation!

Many thanks to all contributors this year and their continuous support!

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
