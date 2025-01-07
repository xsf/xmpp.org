---
title: The XMPP Newsletter April 2023
date: 2023-05-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of April 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

- xmpp.org got a new software section! Looking for XMPP software, i.e. clients, servers, libraries, components, and tools? Check out [xmpp.org](https://xmpp.org/)'s new [software section](https://xmpp.org/software/), which lets you filter software by your own criteria. Looking for a client which works on Android and supports audio/video calls? Looking for a library that supports [XEP-0461: Message Replies](https://xmpp.org/extensions/xep-0461.html)? Just apply the filter and see what you get!

{{< figure src="/images/newsletter/2023-03-05/xmpp-software-section.png" caption="xmpp.org's new software section" >}}

- If you are interested to become an [XSF member](https://xmpp.org/community/membership/) you can [apply during this quarter until May 21th, 2023, 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q2_2023).

### XMPP and Google Summer of Code 2023
The XSF has been [accepted again as hosting organisation at the GSoC 2023](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/)!

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. We're open for applications via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month
- [FOSSY](https://fossy.us) will have an XMPP track at their conference this summer. Please [submit talk proposals](https://2023.fossy.us/call-for-proposals/) by May 14th. The track organizers offer financial support for presenters, if needed.
- [XMPP Italian happy hour](https://tube.nicfab.eu/w/3KJMxZPYxRXQDAhXySZgLf): monthly Italian XMPP web meeting, starting May 16th and then every third Tuesday of the month at 7:00 PM. Online event, with web meeting mode and live streaming.

## XMPP Sprints

- [Elbe-Sprint Hamburg 2023](https://xmpp.org/2023/04/elbe-sprint-hamburg-2023/): Thursday, 22-06-2023 18:00 CEST — Sunday, 25-06-2023 12:00 CEST.  
This summer, XMPP developers are holding a development sprint in Hamburg, Germany.

## XMPP Videos

- Axel Reimer published German video tutorials in his blog [eversten.net](https://eversten.net/).
    - One [video [DE]](https://www.eversten.net/xmppvideo/) explains some main aspects of XMPP.
    - A series of [four videos [DE]](https://www.eversten.net/blog/monalvideos/) explains how iOS users can start using XMPP by installing and configuring the messenger app Monal.

## Articles

- A draft of the EU chat-control [has been published for download at Netzpolitik.org.](https://cdn.netzpolitik.org/wp-upload/2023/04/2023-04-05_EPRS_CSAM_Complementary-Impact-Assessment_DRAFT.pdf). Those are comment by 
  - [Netzpolitik.org](https://netzpolitik.org/2023/chatkontrolle-studie-zerlegt-plaene-der-eu-kommission/) [DE]
  - [Patrick Beyer (politician)](https://www.patrick-breyer.de/wissenschaftlicher-dienst-des-eu-parlaments-bestaetigt-chatkontrolle-verstoesst-gegen-grundrechte/) [DE]
- Axel Reimer introduced a new German website called [xmpp24.de [DE]](https://xmpp24.de/). This website focuses on helping new XMPP users who want to start using XMPP on their Android or iOS devices. It explains one onboarding flow (as a video tutorial) per operating system.
- The [JMP April Newsletter](http://blog.jmp.chat/b/april-newsletter-2023) talks about several developments, including a new MMS stack in testing, integration with the [Quicksy](https://quicksy.im) directory, the ability to create [Snikket](https://snikket.org) instances from inside a Cheogram Android onboarding flow, and an experimental [WebXDC](https://webxdc.org) prototype.

{{< figure src="/images/newsletter/2023-05-05/JMP_april2023.png" caption="Cheogram onboarding view" >}}

## Software news
### Clients and applications

- [Gajim 1.7.3](https://gajim.org/post/2023-04-04-gajim-1.7.3-released/) has been released. This release enables you to mute notifications for specific contacts and brings some improvements and bug fixes.

### Servers

- [ejabberd 23.04](https://www.process-one.net/blog/ejabberd-23-04/) has been released. This a big new release with many changes including support XEP-0425 (Message moderation), Real-Time Block List for MUC rooms and several SQL improvements.

### Libraries & Tools

- [QXmpp 1.5.4](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.4) and [QXmpp 1.5.5](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.5) have been released! They fix some important bugs.
- [Web Console Chat](https://soft.trung.fun/webcc/webcc.en.html) has been released. This is an installation guide and a collection of patches to make sure existing XMPP console clients are safe enough before serving them to the web with [`ttyd`](https://github.com/tsl0922/ttyd) for your web-chat service.

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

- [Version 0.2.0 of XEP-0472 (Pubsub Social Feed)](https://xmpp.org/extensions/xep-0472.html)
  - Change the pubsub#type to be consistent with other XEPs
  - Add a Discovery section (tj)
- [Version 0.4.1 of XEP-0356 (Privileged Entity)](https://xmpp.org/extensions/xep-0356.html)
  - Fixed some typos (gh/@bodqhrohro)
- [Version 0.2.0 of XEP-0428 (Fallback Indication)](https://xmpp.org/extensions/xep-0428.html)
  - Add 'for' attribute such that entities can discover what the fallback is for.
  - Allow to specify that only one of  or  is meant as a fallback.
  - Allow to specify the part of respective text that is meant as fallback where applicable.
  - Don't use encryption example, which should use XEP-0380 instead. (lmw)
- [Version 0.4.0 of XEP-0388 (Extensible SASL Profile)](https://xmpp.org/extensions/xep-0388.html)
  - Bump namespace
  - Add reference to  and
  - Update security considerations and business rules
  - Clarify `<continue/>` and tasks
  - Add expansion point to inline stream resumption and BIND2 (and possibly others)
  - Add optional `<user-agent/>` element
  - Move from Deferred to Experimental (tm)
- [Version 0.4.0 of XEP-0386 (Bind 2)](https://xmpp.org/extensions/xep-0386.html)
  - Various changes, made in parallel with working client and server implementation experience, and SASL2 updates.
  - More tightly define the integration with XEP-0388 and several session feature XEPs: XEP-0198, XEP-0280, XEP-0352.
  - Replace the custom latest-id element with the new metadata element from XEP-0313, which also provides richer information.
  - Drop unread tracking, as this is a deep topic not directly related to resource binding. Instead the details of integration with other extensions have been better defined and demonstrated, to allow such functionality when it is fully defined and exists.
  - Adjust proposed namespace on aesthetic grounds and consistency with SASL2's approach. As this protocol may become part of the new preferred connection flow for a long time to come, it makes no sense to include the redundant and potentially confusing '2' when there is no conflict without it. Similarly, the '.0' has been dropped from the XEP's title, as it isn't really a version number.
  - Allow the client some influence over the resulting resource identifier, and define a standard format for these combined identifiers.
  - Specify that servers should terminate old sessions from a client when it binds a new resource. (mw)
- [Version 0.7.0 of XEP-0359 (Unique and Stable Stanza IDs)](https://xmpp.org/extensions/xep-0359.html)
  - Add security consideration regarding spoofability and reference example (fs)
- [Version 0.12.0 of XEP-0292 (vCard4 Over XMPP)](https://xmpp.org/extensions/xep-0292.html)
  - Remove raw-IQ mode and specifies the reuse of PEP (spw)

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
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, emus, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), wurstsalat, XSF iTeam**
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
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
