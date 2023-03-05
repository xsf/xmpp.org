---
title: The XMPP Newsletter February 2023
date: 2023-03-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of February 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

xmpp.org got a new software section! Looking for XMPP software, i.e. clients, servers, libraries, components, and tools? Check out [xmpp.org](https://xmpp.org/)'s new [software section](https://xmpp.org/software/), which lets you filter software by your own criteria. Looking for a client which works on Android and supports audio/video calls? Looking for a library that supports [XEP-0461: Message Replies](https://xmpp.org/extensions/xep-0461.html)? Just apply the filter and see what you get!

{{< figure src="/images/newsletter/2023-03-05/xmpp-software-section.png" caption="xmpp.org's new software section" >}}

### XMPP and Google Summer of Code 2023
The XSF has been [accepted again as hosting organisation at the GSoC 2023](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/) !

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## XMPP Videos

- Cheogram offers a new [PeerTube channel](https://kumi.tube/c/cheogram) for videos about new features in their XMPP client and gateways. Also available [on YouTube](https://YouTube.com/@cheogram).

## Articles

- [nicfab](https://notes.nicfab.eu) wrote an article about the [Digital Service Act: EU Commission Questions and Answers on identification and counting of active recipients of the service under the DSA](https://notes.nicfab.eu/en/posts/dsa-faq/).
- [Digital Markets Act: the second stakeholders' workshop on the interoperability organized by the EU Commission](https://notes.nicfab.eu/en/posts/dmaworkshop/) an article by nicfab about the recent DMA stakeholder workshop on "Interoperability between messaging services"
- [New Profanity Old System](https://profanity-im.github.io/blog/post/distrobox/) by jubalh: This blog explains how to run latest profanity releases on years old systems properly.
- The [JMP newsletter covering February 2023](https://blog.jmp.chat/b/february-newsletter-2023) has been published. As well as a [post about technical implemetation for stickers](https://blog.jmp.chat/b/cheogram-android-stickers-2023) in Cheogram Android.

## Software news
### Clients and applications

- [Converse 10.1.1](https://github.com/conversejs/converse.js/releases/tag/v10.1.1) and [10.1.2](https://github.com/conversejs/converse.js/releases/tag/v10.1.2) have been released, which both fix some bugs. Converse is a web based XMPP/Jabber chat client.
- [Dino 0.4.0 'Ilulissat'](https://dino.im/blog/2023/02/dino-0.4-release/) and 0.4.1 have been released. The 0.4 release adds support for message reactions and replies. Dino also switched from GTK3 to GTK4 and makes use of libadwaita now.

{{< figure src="/images/newsletter/2023-03-05/dino-reaction.png" caption="Dino 0.4 now supports Message Replies and Message Reactions" >}}

- [Gajim 1.7.0](https://gajim.org/post/2023-02-03-gajim-1.7.0-released/) and [1.7.1](https://gajim.org/post/2023-02-08-gajim-1.7.1-released/) have been released. These releases bring improved KeepassXC integration, better defaults for group chats created with ejabberd, and some important bug fixes.
- [Psi+ 1.5.1645](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) and [1.5.1646](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) have been released.

### Servers

- [Prosody 0.12.3](https://blog.prosody.im/prosody-0.12.3-released/) has been released.
- [Openfire inVerse plugin 10.1.2](https://discourse.igniterealtime.org/t/inverse-openfire-plugin-10-1-2-1-released/92591) has been released.
- A new plugin for Openfire, the [MUC Real-Time Block List plugin](https://discourse.igniterealtime.org/t/new-openfire-muc-real-time-block-list-plugin/92587) has been released. It allows to moderate chat rooms, especially for federated services.
- [Cobalt 1.3](https://www.isode.com/company/wordpress/cobalt-1-3-release-features/) has been released.

### Libraries & Tools

- [nbxmpp 4.2.0](https://dev.gajim.org/gajim/python-nbxmpp) has been released, which brings support for [XEP-0461](https://xmpp.org/extensions/xep-0461.html) Message Replies and a profile for SASLprep.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to 
accept this proposal as an Experimental XEP.

- No XEPs proposed this month.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it 
will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- No XEPs updated this month.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- No XEP moved to stable this month.

### Deprecated

- No XEP deprecated this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Spread the news!

Please share the news on other networks:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [Twitter](https://twitter.com/xmpp)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Lemmy instance](https://community.xmpp.net/)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", emus, Licaon_Kter, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), wurstsalat, Zash**
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, Pierre Jarillon, Ppjet6, Ysabeau**
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
  - Translators: **Jeybe, wh0nix**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: **nicfab**
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Translators: **daimonduff, TheCoffeMaker**

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations
- communication via media accounts

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
