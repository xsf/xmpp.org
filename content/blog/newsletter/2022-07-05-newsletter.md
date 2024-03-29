---
title: The XMPP Newsletter June 2022
date: 2022-07-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of June 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
- Italian: [nicfab.it](https://www.nicfab.it/)
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)

## XSF Announcements

- The XSF membership application period for the third quarter 2022 is currently open. If you are interested in becoming a XSF member then you can [apply for membership](https://wiki.xmpp.org/web/Membership_Applications_Q3_2022).

## Google Summer of Code 2022

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

The Google Summer of Code 2022 has lifted off and coding started a while ago! The two new contributors Patiga and PawBud who will work on open-source software projects in the XMPP environment. Read their first blog posts, too.
  - **Patiga** works on [more flexible file transfers in Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ). Mentors are **fiaxh** and **Marvin W.**.
    - [Stateless File Sharing GSoC project](https://dino.im/blog/2022/06/stateless-file-sharing-gsoc-project/)
    - [Project Stateless File Sharing: First Steps](https://dino.im/blog/2022/06/project-stateless-file-sharing-first-steps/)
  - **PawBud** works towards [adding support for A/V communication via Jingle in ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19). Mentors are **JC Brand** and **vanitasvitae**.
    - [On-Boarding Experience with XSF (Converse)](https://xmpp.org/2022/06/on-boarding-experience-with-xsf-converse/)

  Feel free to spread the word via [Mastodon](https://fosstodon.org/@xmpp/108358826402429966) or [Twitter](https://mobile.twitter.com/xmpp/status/1529199174729728000). More details in our [designated page at xmpp.org](https://xmpp.org/community/gsoc-2022/).

## XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

JMP News: [Command UI and better transcriptions coming soon](https://blog.jmp.chat/b/june-newsletter-2022).

Nicola Fabiano wrote the article [To be «IM apps addicted» or not to be, that is the question. Choose to be free: Snikket, the system messaging based on XMPP protocol](https://notes.nicfab.it/en/posts/snikket/) highlighting XMPP as his best solution and [Snikket](https://snikket.org) as his choice. In another article he states his reasons to avoid WhatsApp, also considering the European Commission's actions: [Persisting with Whatsapp use: how to persevere unknowingly. The whys of our «No»](https://notes.nicfab.it/en/posts/nowa/).

Paul Schaub wrote a piece on PGPainless: [Reproducible Builds – Telling of a Debugging Story](https://blog.jabberhead.tk/2022/06/20/reproducible-builds-telling-of-a-debugging-story/). 

Prosody devs got funded by EU’s NGI Assure via the NLnet Foundation to [modernize XMPP authentication and authorization](https://blog.prosody.im/modern-xmpp-auth/) so users can secure their sessions with MFA (multi-factor authentication) and have peace of mind with per session controls.

## Software news

### Clients and applications

Gajim [1.4.3](https://gajim.org/post/2022-06-01-gajim-1.4.3-released/), [1.4.4](https://gajim.org/post/2022-06-18-gajim-1.4.4-released/), and [1.4.5](https://gajim.org/post/2022-06-21-gajim-1.4.5-released/) have been released: Gajim’s new versions come with many improvements: emoji auto-complete, automatic theme switching when your desktop switches from light to dark in the evening, a completely reworked Gajim remote interface, and many bug fixes.

![Gajim emoji auto-complete](/images/newsletter/2022-06-1/gajim-emoji-auto-complete.png "Gajim emoji auto-complete")

### Servers

MongooseIM’s new release 5.1 comes with a [configuration rework](https://www.erlang-solutions.com/blog/mongooseim-5-1-configuration-rework/).

Jackal [0.61.0](https://github.com/ortuman/jackal/releases/tag/v0.61.0) has been released.

ProcessOne announced [ejabberd .deb and .rpm repositories](https://www.process-one.net/blog/announcing-ejabberd-deb-and-rpm-repositories/) for amd64 and arm64 systems.

![ejabberd .deb and .rpm](/images/newsletter/2022-06-1/ejabberd.png "ejabberd .deb and .rpm")

[Prosody 0.12.1](https://blog.prosody.im/prosody-0.12.1-released/) has been released, and it comes with improved compatibility with Jitsi Meet plus bug fixes for its newly-extended [XEP-0227](https://xmpp.org/extensions/xep-0227.html) support.

From the ignite realtime community:

- Smack version 4.4.6 [has been released](https://discourse.igniterealtime.org/t/smack-4-4-6-released/91809).
- Openfire REST API plugin [has been released in version 1.8.1](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-8-1-released/91785).

### Libraries

No news this month.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

By the way, xmpp.org features [a new page about XMPP RFCs](https://xmpp.org/rfcs/).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [WebSocket S2S](https://xmpp.org/extensions/inbox/websocket-s2s.html)
    -   This specification defines a procedure to make s2s XMPP connections over WebSocket.
-   [XMPP over QUIC](https://xmpp.org/extensions/inbox/xmpp-over-quic.html)
    -   This specification defines a procedure to make both c2s and s2s XMPP connections over the QUIC protocol instead of TCP+TLS.   

### New

-   No New XEPs this month

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   No XEPs updated this month.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-  [External Service Discovery](https://xmpp.org/extensions/xep-0215.html)
   -    This document specifies an XMPP protocol extension for discovering services external to the XMPP network. 

### Stable

-   No XEPs advanced to Stable this month.

### Deprecated

-   No XEP deprecated this month.

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

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, guusdk, Holger, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), nicfab, TheCoffeMaker, wh0nix, wurstsalat, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

Each month's newsletter issue is drafted in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
