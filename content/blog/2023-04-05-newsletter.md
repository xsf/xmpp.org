---
title: The XMPP Newsletter March 2023
date: 2023-04-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of March 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

- xmpp.org got a new software section! Looking for XMPP software, i.e. clients, servers, libraries, components, and tools? Check out [xmpp.org](https://xmpp.org/)'s new [software section](https://xmpp.org/software/), which lets you filter software by your own criteria. Looking for a client which works on Android and supports audio/video calls? Looking for a library that supports [XEP-0461: Message Replies](https://xmpp.org/extensions/xep-0461.html)? Just apply the filter and see what you get!

{{< figure src="/images/newsletter/2023-03-05/xmpp-software-section.png" caption="xmpp.org's new software section" >}}

- If you are interested to become an [XSF member](https://xmpp.org/community/membership/) you can [apply during this quarter until May 21th, 2023, 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q2_2023).


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

## Articles

- Debian package maintainers give [a summary](https://xmpp-team.pages.debian.net/blog/2023/03/xmpp-whats-new-in-bookworm.html) of XMPP packages that will be available in the next Debian stable release (Debian 12 "Bookworm").
- Cheogram Android [introduces Stickers](http://blog.jmp.chat/b/cheogram-android-stickers-2023).
- IgniteRealtime: [Translations everywhere!](https://discourse.igniterealtime.org/t/translations-everywhere/92628)
- Carl Schwan writes on the [Digital Market Act workshop in Brussels](https://carlschwan.eu/2023/03/02/digital-market-act-workshop-in-brussels/)
{{< figure src="/images/newsletter/2023-04-05/dma_brussels.jpg" caption="Digital Market Act workshop in Brussels" >}}

- The IETF has approved [publication of Messaging Layer Security (MLS)](https://www.ietf.org/blog/mls-secure-and-usable-end-to-end-encryption/), a new standard for end-to-end security that will make it easy for apps to provide the highest level of security to their users. End-to-end encryption is an increasingly important security feature in Internet applications. It keeps users’ information safe even if the cloud service they’re using has been breached.

## Software news
### Clients and applications

- [Cheogram Android 2.12.1-4](https://git.singpolyma.net/cheogram-android/refs/2.12.1-4) has been released with support for sending message replies and reactions, swipe to reply, "note to self" contact, viewing vcard4 profiles, and occasional MUC pings.
- [Gajim 1.7.2](https://gajim.org/post/2023-03-09-gajim-1.7.2-released/) has been released. This release brings many bug fixes and some useful improvements. Gajim now allows you to delete messages from your local chat history (in case of nasty spam messages). Furthermore, detection of WAV audio files has been improved and you can now click the waveform to skip to a specific timestamp within a voice message.
- [monocles chat 1.6.3](https://codeberg.org/Arne/monocles_chat) received support for message moderation ([XEP-0425](https://xmpp.org/extensions/xep-0425.html)) and will get some new features of Cheogram Android as well.
- [Movim 0.21 "Whipple"](https://mov.im/?node/pubsub.movim.eu/Movim/81f7e9d0-8cb6-47d7-a5d4-f3324c6aa306) has been released, and it comes with a ton of new features. Message Replies, Web Push, voice messages, new emojis, and much more.
- [SiskinIM 7.3.3](https://github.com/tigase/siskin-im/releases/tag/7.3.3) and [BeagleIM 5.3.4](https://github.com/tigase/beagle-im/releases/tag/5.3.4) from [Tigase](https://tigase.org/) have been released.
- [Spark 3.0.2](https://igniterealtime.org/projects/spark/) from [Ignite Realtime](https://igniterealtime.org/) has been released.

{{< figure src="/images/newsletter/2023-04-05/movim_replies.png" caption="Movim supports replies" >}}

### Servers

- Metronome IM [4.0.2](https://github.com/maranda/metronome/releases/tag/v4.0.2) brings some bug fixes.

### Libraries & Tools

- [python-nbxmpp 4.2.1 and 4.2.2](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) have been released, which fix some bugs with python-nbxmpp's HTTP library.
- [QXmpp 1.5.1](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.1) and [QXmpp 1.5.2](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.2) have been released in February and [QXmpp 1.5.3](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.3) in March! They fix some important bugs.
- [xmppbl.org](https://xmppbl.org) provides a Real-Time Block List (RTBL) service for XMPP.
- [XmppDotNet](https://www.ag-software.net/2023/03/22/xmppdotnet-announcement/) is the new name and next generation of the MatriX vNext XMPP library.

From the ignite realtime community:
- [Openfire MUC Real-Time Block List plugin 1.1.0](https://discourse.igniterealtime.org/t/release-v1-1-0-of-the-muc-real-time-block-list-plugin-for-openfire/) has been released.
- [Openfire EXI plugin](https://discourse.igniterealtime.org/t/developing-openfire-efficient-xml-interchange-exi-functionality/) is work in progress.
- [Botz 1.2.0](https://discourse.igniterealtime.org/t/botz-version-1-2-0-release/) has been released.
- [Openfire HTTP File Upload plugin 1.2.2](https://discourse.igniterealtime.org/t/http-file-upload-v1-2-2-released/) has been released.

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

- [Version 0.2.0 of XEP-0444 (Message Reactions)](https://xmpp.org/extensions/xep-0444.html)
  - Add emoji rejection mechanism. (NC)
- [Version 0.7.0 of XEP-0359 (Unique and Stable Stanza IDs)](https://xmpp.org/extensions/xep-0359.html)
  - Add security consideration regarding spoofability and reference example (fs)
- [Version 0.12.0 of XEP-0292 (vCard4 Over XMPP)](https://xmpp.org/extensions/xep-0292.html)
  - Removes raw-IQ mode and specifies the reuse of PEP (spw)
- [Version 0.4.0 of XEP-0388 (Extensible SASL Profile)](https://xmpp.org/extensions/xep-0388.html)
  - Bump namespace
  - Add reference to XEP-0440 and RFC 5802
  - Update security considerations and business rules
  - Clarify `<continue/>` and tasks
  - Add expansion point to inline stream resumption and BIND2 (and possibly others)
  - Add optional `<user-agent/>` element
  - Move from Deferred to Experimental
- [Version 0.4.0 of XEP-0386 (Bind 2)](https://xmpp.org/extensions/xep-0386.html)
  - Various changes, made in parallel with working client and server implementation experience, and SASL2 updates.
  - More tightly define the integration with XEP-0388 and several session feature XEPs: XEP-0198, XEP-0280, XEP-0352.
  - Replace the custom latest-id element with the new metadata element from XEP-0313, which also provides richer information.
  - Drop unread tracking, as this is a deep topic not directly related to resource binding. Instead the details of integration with other extensions have been better defined and demonstrated, to allow such functionality when it is fully defined and exists.
  - Adjust proposed namespace on aesthetic grounds and consistency with SASL2's approach. As this protocol may become part of the new preferred connection flow for a long time to come, it makes no sense to include the redundant and potentially confusing '2' when there is no conflict without it. Similarly, the '.0' has been dropped from the XEP's title, as it isn't really a version number.
  - Allow the client some influence over the resulting resource identifier, and define a standard format for these combined identifiers.
  - Specify that servers should terminate old sessions from a client when it binds a new resource.
- [Version 0.2.0 of XEP-0428 (Fallback Indication)](https://xmpp.org/extensions/xep-0428.html)
  - Add 'for' attribute such that entities can discover what the fallback is for.
  - Allow to specify that only one of `<subject>` or `<body` is meant as a fallback.
  - Allow to specify the part of respective text that is meant as fallback where applicable.
  - Don't use encryption example, which should use XEP-0380 instead.

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
