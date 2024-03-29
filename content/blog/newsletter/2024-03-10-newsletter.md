---
title: The XMPP Newsletter February 2024
date: 2024-03-24
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of February 2024. Many thanks to all our readers and all Newsletter contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

Welcome to our reapplicants and new members in Q1 2024!
If you are interested to join the XMPP Standards Foundation, [please apply now](https://wiki.xmpp.org/web/Membership_Applications_Q2_2024).

### XMPP and Google Summer of Code 2024

The XSF has been accepted as a hosting organisation at GSoC in 2024 again! [If you are interested, please reach out](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024)!
The GSoC project ideas from XMPP-related organisations are:

- Monal
  - [Modern Onboarding (90 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Modern_Onboarding)
  - [Media Gallery (90 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
  - [MDM support (175 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/MDM_support)
  - [SiriKit support (350 hours, medium)](https://wiki.xmpp.org/web/Gsoc2024/Monal/SiriKit_support)
- Dino
  - [Inline link preview (175 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Dino/Inline_link_preview)
  - [Rich message support	(175 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Dino/Rich_message_support)
- Prav.app
  - [Standards compliant SMS OTP based authentication (350 hours, medium)](https://wiki.xmpp.org/web/Gsoc2024/Prav.app/Standards_compliant_SMS_OTP_based_authentication)

{{< figure src="/images/logos/gsoc2024_logo.svg" caption="XSF and Google Summer of Code 2024" >}}

### XSF Fiscal Hosting Projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects you can support:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Prav iOS](https://opencollective.com/prav-ios)

## XMPP Events

- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) [IT]: monthly Italian XMPP web meeting, every third Monday of the month at 7:00 PM local time (online event, with web meeting mode and live streaming).

## Articles

We are happy [to announce](https://www.xmpp-it.net/2024/03/03/mario/the-xmpp-it-peertube-instance/) the launch of the [XMPP-IT community's PeerTube instance](https://video.xmpp-it.net), a dedicated platform for sharing and discovering videos about the XMPP protocol and its applications. Members of the XMPP community are encouraged to contribute by creating and sharing their own videos. Whether it's tutorials, project showcases, or discussions on XMPP topics, your contributions are welcome.

[JMP turned 7 years old!](https://blog.jmp.chat/b/february-newsletter-2024) Congratulations! Read also about [mobile-friendly gateway to any SIP provider](https://blog.jmp.chat/b/mobile-friendly-sip-gateway).

{{< figure src="/images/newsletter/2024-03-05/jmp-sip-gateway.png" caption="SIP via XMPP" >}}

## Software News

### Clients and Applications

[monocles chat](https://play.google.com/store/apps/details?id=eu.monocles.chat) is available on Google Play. It comes with many updates like a working commands view and better support for [WebXDC](https://webxdc.org/) apps, but also an initial modern integration of stickers.

### Servers

- [ejabberd 24.02](https://www.process-one.net/blog/ejabberd-24-02/) has been released, and it comes with support for TLS 1.3 and advanced SASL2 protocols. This release brings performance enhancements with Bind 2 for faster connection times, which is especially crucial for mobile network users. Support for [XEP-0424: Message Retraction](https://xmpp.org/extensions/xep-0424.html) allows users to manage their message history and remove something they posted by mistake.
 
### Libraries & Tools

- [GitLab XMPP Bot](https://dev.gajim.org/gajim/gitlab-xmpp-bot/-/blob/master/README.md), an XMPP bot that sends messages based on GitLab hooks had its 1.0.0 release. This bot is based on [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp) and it is active in [Gajim's support chat](xmpp:gajim@conference.gajim.org?join).
- [go-xmpp 0.1.0](https://github.com/xmppo/go-xmpp/releases/tag/v0.1.0) has been released.
- [python-nbxmpp 4.5.4](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/4.5.4/ChangeLog) has been released, which fixes some issues around subject changes and date parsing.
- [Slixfeed](https://gitgud.io/sjehuda/slixfeed) is a news bot offered as client and service component; it can handle multiple chats simultaneously and also display media inline, which, in addition of it being intended primarily for private chats, makes it exceptionally useful for groupchats where visual contents are essential.
- [StropheJS 2.0.0](https://github.com/strophe/strophejs/releases/tag/v2.0.0) has been released.
- [xmpp-rs](https://xmpp.rs) has gained a [Code of Conduct](https://gitlab.com/xmpp-rs/xmpp-rs/-/blob/main/CODE_OF_CONDUCT.md) and a [CONTRIBUTING](https://gitlab.com/xmpp-rs/xmpp-rs/-/blob/main/CONTRIBUTING.md) guide. Feel free to come and say hi!

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- No XEPs proposed this month.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- No XEPs updated this month.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No last call this month.

### Stable

- No XEP moved to stable this month.

### Deprecated

- No XEP deprecated this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Twitter](https://twitter.com/xmpp)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Federico, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, XSF iTeam**
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: **nicola**

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

