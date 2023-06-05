---
title: The XMPP Newsletter May 2023
date: 2023-06-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of May 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

- If you are interested to become an [XSF member](https://xmpp.org/community/membership/) you can apply during Q3 2023 soon.

### XMPP and Google Summer of Code 2023
The XSF has been [accepted again as hosting organisation at the GSoC 2023 and receive two slots for XMPP Contributors](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/)!

- The GSoC contributor for Moxxy published his [first blog post](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), detailing the plan to implement basic groupchat functionality.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month
- [FOSSY](https://fossy.us) will have an XMPP track at their conference this summer from July 13-16th 2023
- [XMPP Italian happy hour](https://tube.nicfab.eu/w/85RxLsnNTc9FcdFzFgkdsP): monthly Italian XMPP web meeting, starting May 16th and then every third Tuesday of the month at 7:00 PM (online event, with web meeting mode and live streaming).

## Talks

- The developer behind Libervia has scheduled a couple of informative talks in Paris for June. These presentations will delve into various aspects of the Libervia project and XMPP. The first talk is a 20-minute session in English, taking place at 15:00 on Thursday, June 15 at [OW2](https://www.ow2con.org/view/2023/Abstract_Community_Day#15061500). The second talk will be a more in-depth 60-minute discussion in French, scheduled for 17:30 on Friday, June 16 at [Pas Sage En Seine](https://passageenseine.fr/). These sessions provide a great opportunity to gain insights into the Libervia project and to interact with its developer.

## Articles

The German governmental competion authorthy has publish a [study on video and messaging services](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2023/17_05_2023_SU_MD.html) [DE] where the XSF and also several XMPP projects provided statements. Read the [summary](https://www.bundeskartellamt.de/SharedDocs/Publikation/DE/Sektoruntersuchungen/Sektoruntersuchung_MessengerVideoDienste_Zusammfassung.pdf?__blob=publicationFile&v=3) [DE] or the [full document](https://www.bundeskartellamt.de/SharedDocs/Publikation/DE/Sektoruntersuchungen/Sektoruntersuchung_MessengerVideoDienste.pdf?__blob=publicationFile&v=5) [DE].

## Software news
### Clients and applications

- [Gajim 1.8.0](https://gajim.org/post/2023-05-27-gajim-1.8.0-released/) has been released and it comes with integrated OMEMO encryption! Integrating the OMEMO plugin brings tighter integration and better user experience. The chat menu has been rearranged and some quick buttons have been added for convenience. Both Gajim’s message search and conversation view received some important changes and fixes.

{{< figure src="/images/newsletter/2023-06-05/gajim-chat-banner-group-chat.png" caption="Gajim's chat banner in a group chat" >}}

- [Kaidan 0.9 and 0.9.1](https://www.kaidan.im/2023/05/05/kaidan-0.9.0/) have been released! It adds support for OMEMO 2, Automatic Trust Management (ATM), [XMPP Providers](https://providers.xmpp.net/), Message Reactions and much more.

{{< figure src="/images/newsletter/2023-06-05/kaidan-0.9-horizontal.png" caption="Kaidan's chat view" >}}

- Exciting developments are on the horizon for [Libervia](https://libervia.org/). Thanks to a grant from NLnet through the NGI Assure Fund, work on the implementation of A/V calls with Jingle across several frontends is underway. This new feature aims to support both one-on-one and multi-party calls, with plans to even add remote desktop control capabilities. Additionally, the ActivityPub Gateway is currently being stabilised, which will further enhance the functionality of Libervia. For a full rundown of these updates and more, check out the latest progress note on [Goffi's blog](https://www.goffi.org/b/libervia-progress-note-2023-w22-x3Wa).
- JMP lets you send and receive text and picture messages (and calls) through a real phone number right from your computer, tablet, phone, or anything else that has a Jabber client. Jabber-side reactions are now translated where possible into the tapback pseudo-syntax. Read more in the [JMP blog](https://blog.jmp.chat/b/april-newsletter-2023). [Cheogram Android 2.12.1-6](https://git.singpolyma.net/cheogram-android/refs/2.12.1-6) features per-account colours and quiet hours, thumbhash previews for images, and many bug fixes.

### Servers

- [MongooseIM 6.1.0](https://www.erlang-solutions.com/blog/mongooseim-6-1-handle-more-traffic-consume-less-resources/) has been released.
- The Openfire XMPP server had two new releases: [Openfire 4.6.8 (old stable)](https://discourse.igniterealtime.org/t/openfire-4-6-8-release) and [Openfire 4.7.5 (stable)](https://discourse.igniterealtime.org/t/openfire-4-7-5-release). Furthermore a [CVE on Openfire Administration Console authentication bypass has been submitted](https://discourse.igniterealtime.org/t/cve-2023-32315-openfire-administration-console-authentication-bypass/92869).

### Libraries & Tools

- [omemo-dr](https://dev.gajim.org/gajim/omemo-dr/), a new OMEMO crypto library is available. `omemo-dr` is a fork of `python-axolotl`, which is the crypto library used for OMEMO encryption in Gajim. In preparation for future changes (e.g. the next OMEMO version), Gajim developers forked this library.
- [python-nbxmpp 4.3.0 and 4.3.1](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) have been released and bring several bug fixes regarding OMEMO and HTTP handling.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- No XEPs proposed this month.

### New

- [Version 0.1.0 of XEP-0480 (SASL Upgrade Tasks)](https://xmpp.org/extensions/xep-0480.html)
  - This specification provides a way to upgrade to newer SASL mechanisms using SASL2 tasks.
- [Version 0.1.0 of XEP-0482 (Call Invites)](https://xmpp.org/extensions/xep-0482.html)
  - This document defines how to invite someone to a call and how to respond to the invite.
- [Version 0.1.0 of XEP-0481 (Content Types in Messages)](https://xmpp.org/extensions/xep-0481.html)
  - This specification describes a generic method whereby content in messages can be tagged as having a specific Internet Content Type. It also provides a method for sending the same content using different content types, as a fall-back mechanism when communicating between clients having different content type support.
- [Version 0.1.0 of XEP-0478 (Stream Limits Advertisement)](https://xmpp.org/extensions/xep-0478.html)
  - This specification defines a way for an XMPP entity to announce the limits it will enforce for data received on a stream.
- [Version 0.1.0 of XEP-0479 (XMPP Compliance Suites 2023)](https://xmpp.org/extensions/xep-0479.html)
  - This document defines XMPP application categories for different use cases (Core, Web, IM, and Mobile), and specifies the required XEPs that client and server software needs to implement for compliance with the use cases.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- [Version 1.25.0 of XEP-0060 (Publish-Subscribe)](https://xmpp.org/extensions/xep-0060.html)
  - Add data model informational text in Implementation Notes.
  - Provide a way for a PubSub service to tell a client when a node is full.
  - Clarify behaviour and current usage of the 'pubsub#itemreply' option.
  - Fix spec approver
- [Version 1.1.1 of XEP-0223 (Persistent Storage of Private Data via PubSub)](https://xmpp.org/extensions/xep-0223.html)
  - Add notes about checking event origin (in reaction to CVE-2023-28686). (ka)
- [Version 1.1.0 of XEP-0313 (Message Archive Management)](https://xmpp.org/extensions/xep-0313.html)
  - Clarify archive metadata response in the case of an empty archive.
  - Clarify query response in the case of no matching results. (mw)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

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
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), nicola, XSF iTeam**
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
  - Translators: **Jeybe, wh0nix**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: **nicola**
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
