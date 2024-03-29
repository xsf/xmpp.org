---
title: The XMPP Newsletter July 2022
date: 2022-08-03
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of July 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
- Italian: [nicfab.it](https://www.nicfab.it/)
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)

## XSF Announcements

- The XSF membership application period for the third quarter 2022 is currently open. If you are interested in becoming a XSF member then you can [apply for membership](https://wiki.xmpp.org/web/Membership_Applications_Q3_2022). Please submit by August 25, 2022.

### Google Summer of Code 2022

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

The Google Summer of Code 2022 has lifted off and coding started a while ago! The two new contributors Patiga and PawBud who will work on open-source software projects in the XMPP environment. Read their first blog posts, too.
  - **Patiga** works on [more flexible file transfers in Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ). Mentors are **fiaxh** and **Marvin W.**.
    - [Stateless File Sharing GSoC project](https://dino.im/blog/2022/06/stateless-file-sharing-gsoc-project/)
    - [Project Stateless File Sharing: First Steps](https://dino.im/blog/2022/06/project-stateless-file-sharing-first-steps/)
  - **PawBud** works towards [adding support for A/V communication via Jingle in ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19). Mentors are **JC Brand** and **vanitasvitae**.
    - [On-Boarding Experience with XSF (Converse)](https://xmpp.org/2022/06/on-boarding-experience-with-xsf-converse/)
    - [ConverseJS: An in-depth view into my GSoC'22 project!](https://xmpp.org/2022/07/conversejs-an-in-depth-view-into-my-gsoc22-project/)

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

There are some articles and thoughts on the European Digital Markets Act: 

- [ec.europa.eu](https://ec.europa.eu/info/strategy/priorities-2019-2024/europe-fit-digital-age/digital-markets-act-ensuring-fair-and-open-digital-markets_en)
- [ZDF about interoperatibility](https://www.zdf.de/nachrichten/politik/whatsapp-threema-interoperabilitaet-100.html) [DE]
- German [freie-messenger.de about digital markets act](https://www.freie-messenger.de/en/begriffe/interoperabilitaet/dma)
- German [freie-messenger.de about interoperatibility](https://www.freie-messenger.de/en/begriffe/interoperabilitaet/gedanken)
- [The Digital Markets Act: ensuring fair and open digital markets, European Commission](https://ec.europa.eu/info/strategy/priorities-2019-2024/europe-fit-digital-age/digital-markets-act-ensuring-fair-and-open-digital-markets_en)
- [Interoperability - Digital Markets Act (DMA), freie-messenger.de](https://www.freie-messenger.de/en/begriffe/interoperabilitaet/dma)
- [Interoperability - Thoughts, freie-messenger.de](https://www.freie-messenger.de/en/begriffe/interoperabilitaet/gedanken)
- [WhatsApp muss sich für alle Messenger öffnen, Dominik Rzepka](https://www.zdf.de/nachrichten/politik/whatsapp-threema-interoperabilitaet-100.html) [DE]

The site "Chat standard (XMPP)" with lots of information is available in English now at [freie-messenger.de](https://www.freie-messenger.de/en/sys_xmpp)

Axel from [eversten.net](https://eversten.net/) published an [XMPP Push Notification Test for iOS](https://eversten.net/en/blog/notification/) covering latest Monal, Siskin IM and Snikket versions on different server implementations. A good 15 minutes read for both iOS users and their multi-platforms contacts alike.

JMP now delivers transcribed voicemail in many common languages, not just English. The [voicemail system has also been updated](https://blog.jmp.chat/b/july-newsletter-2022) to source names from more modern XMPP profiles including vCard4 and PEP Nickname.

MoongoseIM 5.1 was released as announced, as announced in the [June 2022 Newsletter](https://xmpp.org/2022/07/the-xmpp-newsletter-june-2022/). In addition to the previously mentioned features, this brought improvements to the Inbox feature. You can now read more about the new Inbox settings and scalability improvements in this [article](https://www.erlang-solutions.com/blog/updates-to-the-mim-inbox-in-version-5-1/).

## Software news

### Clients and applications

[The Mellium Dev Communiqué for July 2022](https://opencollective.com/mellium/updates/dev-communique-for-july-2022) has been published! Important updates this month include an implementation of the new [RFC 9266](https://www.rfc-editor.org/info/rfc9266) and a [new tool](https://mellium.im/checkdoc/) for finding documentation related issues in Go projects. In addition, Mellium has moved to Codeberg! The repositories can now be found at [codeberg.org/mellium](https://codeberg.org/mellium/) and the announcement post can be found on [Lemmy](https://community.xmpp.net/post/34677) or [Open Collective](https://opencollective.com/mellium/updates/mellium-development-has-moved-to-codeberg).

[Conversations 2.10.8](https://conversations.im/), a Jabber/XMPP client for Android, has been released.

[Gajim 1.4.6](https://gajim.org/post/2022-07-07-gajim-1.4.6-released/) and [1.4.7](https://gajim.org/post/2022-07-24-gajim-1.4.7-released/) have been released. These releases bring performance improvements, better file previews, and fix some bugs with the status icon and notifications. Emoji short code detection has been improved as well.

Monal [version 5.2.0](https://github.com/monal-im/Monal/releases/tag/Build_iOS_796) has been released by the Monal development team! This release’s highlights are the new (private) push servers in Europe and the US, display of transferred files in app's documents directory, and several fixes regarding encryption (OMEMO), QR code scanning, and onboarding. Besides, Monal also features a [new webpage](https://www.monal-im.org/).

[Psi+ 11.5.1634 (2022-07-11)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) has been released.

### Servers

[eturnal 1.10.0](https://github.com/processone/eturnal/releases/tag/1.10.0), a STUN / TURN standalone server, has been released.

Openfire version [4.7.2](https://discourse.igniterealtime.org/t/openfire-4-7-2-released/91846) is out, stabilizing and fixing bugs, notably improving BOSH connections under load.

Push Notification Openfire [plugin 0.9.1](https://discourse.igniterealtime.org/t/push-notification-openfire-plugin-0-9-1-released/91832) was released with only one, but an important fix.

[Version 1.8.3](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-8-3-released/91874) of the Openfire REST API plugin is out too, extending MUC search and updating dependencies.

### Libraries

[libstrophe 0.12.1](https://github.com/strophe/libstrophe/releases/tag/0.12.1), a lightweight XMPP client library written in C, has been released.

nbxmpp 3.1.1 [has been released](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog). This version comes with performance improvements and bug fixes.

The [XMPP webhooks component](https://gitlab.com/navlost.eu/xmpp/components/webhooks) has been updated to support more webhooks out of the box. Effectively, this component replaces proprietary tools such as Slack with a better option based on open code and open protocols, fully under control of its users. It now has:
* Richer messages for [GitLab](https://gitlab.com/) events (labels, time spent, etc.)
* Support for [Stripe](https://stripe.com/) events, including optional (but recommended) signature verification.
* Support for [SMS to URL Forwarder](https://github.com/bogkonstantin/android_income_sms_gateway_webhook), a simple but effective SMS forwarder application for Android. This is handy for those with a second or third phone and it's also used to showcase some of the [new features](https://gitlab.com/navlost.eu/xmpp/components/webhooks/-/blob/a6b817012c6c5a0ebf3725cb0bbf5b1120291b6e/README.md#implemented-xeps).
* Integration with [Nextcloud](https://nextcloud.com/) via [Flow Webhooks](https://github.com/kffl/nextcloud-webhooks#flow-based-outgoing-webhooks).

Paul Schaub wrote a [short blog post](https://blog.jabberhead.tk/2022/07/19/creating-a-web-of-trust-implementation-certify-keys-with-pgpainless/) about their recent progress towards adding Web-of-Trust support to PGPainless. With release 1.3.2, the OpenPGP library got support for creating signatures on third-party certificates, which will help users to build their trust network.

xmpp-dns, a tool to check XMPP SRV records, was released in [version 0.3.0](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.3.0), bringing support for DNS over TLS (DoT) and for setting a custom DNS server.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

xmpp.org features [a page about XMPP RFCs](https://xmpp.org/rfcs/) as well.

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Bookmark Pinning](https://xmpp.org/extensions/inbox/bookmark-pinning.html)
    -   This document defines an XMPP protocol extension to allow users to pin PEP Native Bookmarks.
-   [Pubsub Attachments](https://xmpp.org/extensions/inbox/pubsub-attachments.html)
    -   This specification provides a way to attach elements to a pubsub item.  

### New

-   [WebSocket S2S](https://xmpp.org/extensions/xep-0468.html)
    -   This specification defines a procedure to make s2s XMPP connections over WebSocket.
-   [XMPP over QUIC](https://xmpp.org/extensions/xep-0467.html)
    -   This specification defines a procedure to make both c2s and s2s XMPP connections over the QUIC protocol instead of TCP+TLS.

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

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Holger, *IM*, Ludovic Bocquet, martin, MattJ, MSavoritias (fae,ve), nicfab, Pierre Jarillon, Sam Whited, TheCoffeMaker, wh0nix, vanitasvitae, wurstsalat, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

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
