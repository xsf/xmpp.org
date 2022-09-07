---
title: The XMPP Newsletter August 2022
date: 2022-09-07
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of August 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
- Italian: [nicfab.it](https://www.nicfab.it/)
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)

## XSF Announcements

- The XSF membership application period for the fourth quarter 2022 is currently open. If you are interested in becoming a XSF member then you can [apply for membership](https://wiki.xmpp.org/web/Membership_Applications_Q4_2022). Please submit by November 27, 2022.

### Google Summer of Code 2022

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

The Google Summer of Code 2022 has lifted off and coding started a while ago! The two new contributors Patiga and PawBud who will work on open-source software projects in the XMPP environment. Read their first blog posts, too.
  - **Patiga** works on [more flexible file transfers in Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ). Mentors are **fiaxh** and **Marvin W.**.
    - [Stateless File Sharing GSoC project](https://dino.im/blog/2022/06/stateless-file-sharing-gsoc-project/)
    - [Project Stateless File Sharing: First Steps](https://dino.im/blog/2022/06/project-stateless-file-sharing-first-steps/)
    - [Stateless File Sharing: Base implementation](https://dino.im/blog/2022/08/stateless-file-sharing-base-implementation/)
    - [Stateless File Sharing: Sources and Compatibility](https://dino.im/blog/2022/08/stateless-file-sharing-sources-and-compatibility/)
  - **PawBud** works towards [adding support for A/V communication via Jingle in ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19). Mentors are **JC Brand** and **vanitasvitae**.
    - [On-Boarding Experience with XSF (Converse)](https://xmpp.org/2022/06/on-boarding-experience-with-xsf-converse/)
    - [ConverseJS: An in-depth view into my GSoC'22 project!](https://xmpp.org/2022/07/conversejs-an-in-depth-view-into-my-gsoc22-project/)
    - [Google Summer of Code 2022 at XSF: Converse.js - Mid Term Evaluation Update](https://xmpp.org/2022/08/google-summer-of-code-2022-at-xsf-converse.js-mid-term-evaluation-update/)

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

Prosody's team [announces a rework of their permission system](https://blog.prosody.im/role-auth/) in context of [modernizing XMPP authentication and authorization](https://blog.prosody.im/modern-xmpp-auth/).

[Eversten.net](https://www.eversten.net) published two articles:
- [Snikket: Getting Started (iOS)](https://www.eversten.net/en/blog/snikketmonal/)
- [Snikket: Getting Started (Android)](https://www.eversten.net/en/blog/snikketandroid/)

[JMP newsletter](http://blog.jmp.chat/b/august-newsletter-2022) announces a new major release of the Cheogram Android client, with support for ad-hoc command UI and more, as well as a new multi-account billing feature. They also have an article [showcasing the command UI in pictures](http://blog.jmp.chat/b/signup-with-cheogram-android).

Anoxinon Media published ["XMPP - Teil 1 - Messaging mal anders"](https://anoxinon.media/blog/xmpp1/) [DE]. It is about XMPP - an alternative that stands out from the mass.

Kaidan, the XMPP client for every device, released a [post about its end-to-end encryption trust management](https://www.kaidan.im/2022/08/31/e2ee-trust-management/)
![QR code scan](/images/newsletter/2022-09-05/kaidan-qr-code-scan.svg)

The [Mellium Dev Communiqué for August 2022](https://opencollective.com/mellium/updates/dev-communique-for-august-2022) outlines development for the past month including support for HTTP Upload, RFC 9266, various internal testing changes, and a call for feedback!

[Easy Onboarding with Android Chat App blabber.im via XMPP Providers](https://providers.xmpp.net/blog/2022-08-17-xmpp-providers-and-blabber-im/)! Passwords are generated automatically and XMPP providers are suggested. Those suggestions are based on the [curated list of XMPP Providers project](https://providers.xmpp.net/).

## Software news

### Clients and applications

Conversations [2.10.9](https://github.com/iNPUTmice/Conversations/releases/tag/2.10.9) and [2.10.10](https://github.com/iNPUTmice/Conversations/releases/tag/2.10.10) have finally been released for both Google Play Store and F-Droid. Many people were eagerly waiting for a new Conversations build on F-Droid as there were some issues regarding the usage of WebRTC libraries, for Audio/Video calls. F-Droid users were still on the 2.10.2.1+fcr build but now, after 5 months of waiting, they are using the latest version. These releases improve interactions with Bluetooth output devices so be sure to grant the permission as needed. A note for jmp.chat users, the F-Droid version uses an incompatible WebRTC library, so it's better to switch to the Cheogram app (a fork from the jmp.chat developers) at the moment. The Play Store version does not have this issue.

[Moxxyv2 0.2.0, 0.2.1, 0.2.2, 0.2.3](https://codeberg.org/moxxy/moxxyv2) have been released. A new XMPP client for the Android community is featured in this month's newsletter; it is currently only in the alpha stage. However, the future of the project appears to be pretty promising, and we are pleased to have another XMPP project join the community! The initial version (0.2.0) was made available on July 29th, and the second version (0.2.1) was made 
available on August 14th. This project is the successor of moxxyv1, which was written in React Native and abandoned due to various technical issues.

[Psi+ 1.5.1639 (2022-08-17)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) has been released.

Tigase released [BeagleIM 5.3](https://github.com/tigase/beagle-im/releases/tag/5.3) (macOS) and [SiskimIM7.3](https://github.com/tigase/siskin-im/releases/tag/7.3) (iOS) which contain changes and stability improvements. Note that SiskinIM will need at least iOS 13 from now on.

### Servers

[Openfire 4.7.3](https://discourse.igniterealtime.org/t/openfire-4-7-2-released/91846) has been released, which brings many bug fixes, especially for BOSH.

### Libraries

[libstrophe 0.12.2](https://github.com/strophe/libstrophe/releases/tag/0.12.2) has been released.

[Mellium XMPP 0.21.3](https://github.com/mellium/xmpp/releases/tag/v0.21.3) has been released.

[python-nbxmpp 3.2.0 and 3.2.1](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) have been released, which bring support for Extensible SASL Profile ([XEP-0388](https://xmpp.org/extensions/xep-0388.html)) and bug fixes.

[Tigase Martin 3.2.1](https://github.com/tigase/Martin/releases/tag/3.2.1) has been released.

From the ignite realtime community:
 - REST API Openfire plugin [1.9.0](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-9-0-released/91928/2) and [1.9.1](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-9-1-released/91936) has been released to fix several bugs.
 - [Openfire ThreadDump plugin 1.1.0](https://discourse.igniterealtime.org/t/openfire-threaddump-plugin-1-1-0-released/92030) has been released and add two new evaluators for the TaskEngine and statistics from the database connection pool.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

xmpp.org features [a page about XMPP RFCs](https://xmpp.org/rfcs/) as well.

### Proposed
The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to 
accept this proposal as an Experimental XEP.

- No XEPs proposed this month.

### New

- Version 0.1.0 of [XEP-0469](https://xmpp.org/extensions/xep-0469.html) (Bookmark Pinning)
  - This document defines an XMPP protocol extension to allow users to pin PEP Native Bookmarks.
- Version 0.1.0 of [XEP-0470](https://xmpp.org/extensions/xep-0470.html) (Pubsub Attachments)
  - This specification provides a way to attach elements to a pubsub item.
  
### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it 
will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 0.2.0 of [XEP-0447](https://xmpp.org/extensions/xep-0447.html) (Stateless file sharing)
  - Add disposition attribute to signal when inlining is desired. (lmw)
- Version 0.2.0 of [XEP-0470](https://xmpp.org/extensions/xep-0470.html) (Pubsub Attachments)
  - Update reactions to be similar to  Message Reactions (XEP-0444)
  - Namespace bump (jp)
- Version 1.1 of [XEP-0231](https://xmpp.org/extensions/xep-0231.html) (Bits of Binary)
  - Mention where to get textual names of hash functions. (ssw)
- Version 0.3.0 of [XEP-0440](https://xmpp.org/extensions/xep-0440.html) (SASL Channel-Binding Type Capability)
  - Make implementation of tls-server-end-point a MUST for servers. (tm)
- Version 0.2.0 of [XEP-0446](https://xmpp.org/extensions/xep-0446.html) (File metadata element)
  - Use height/width instead of dimensions (lmw)
- Version 0.2.0 of [XEP-0448](https://xmpp.org/extensions/xep-0448.html) (Encryption for stateless file sharing)
  - Replace the ProtoXEP reference with a reference to the published XEP.
  - Add urn:xmpp:ciphers:aes-256-cbc-pkcs7:0 (same as used in XEP-0384) (lmw)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- Version 1.0.0 of [XEP-0215](https://xmpp.org/extensions/xep-0215.html) (External Service Discovery)
  - Accept as Stable as per Council Vote from 2022-08-03. (XEP Editor (jsc)) 
  
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

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Gooya, Holger, *IM*, Ludovic Bocquet, martin, MattJ, MSavoritias (fae,ve), nicfab, Pierre Jarillon, Sam Whited, TheCoffeMaker, wh0nix, vanitasvitae, wurstsalat, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

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
