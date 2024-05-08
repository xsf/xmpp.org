---
title: The XMPP Newsletter April 2024
date: 2024-05-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of April 2024.

## XSF Announcements

If you are interested to join the XMPP Standards Foundation as a member, [please apply until 19th May 2024!](https://wiki.xmpp.org/web/Membership_Applications_Q2_2024).

### XMPP and Google Summer of Code 2024

The XSF has been accepted as a [hosting organisation at GSoC in 2024](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024) again!
These XMPP projects have received a slot and are in the community bonding phase now:

- [Monal](https://monal-im.org/)
  - [Media Gallery (90 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
- [Prav.app](https://prav.app/)
  - [Standards compliant SMS OTP based authentication (350 hours, medium)](https://wiki.xmpp.org/web/Gsoc2024/Prav.app/Standards_compliant_SMS_OTP_based_authentication)

{{< figure src="/images/logos/gsoc2024_logo.svg" caption="XSF and Google Summer of Code 2024" >}}

### XSF Fiscal Hosting Projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects you can support:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Prav iOS](https://opencollective.com/prav-ios)

## XMPP Events

- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2024-07_Berlin): On Friday, 12th to Sunday, 14th of July 2024.
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) [IT]: monthly Italian XMPP web meeting, every third Monday of the month at 7:00 PM local time (online event, with web meeting mode and live streaming).

## Articles

- Monal:
  - [iOS app banned from Chinese Appstore](https://monal-im.org/post/00010-ios-banned/)
  - [Partial security audit for Monal iOS client](https://monal-im.org/post/00011-security-audit-1/): Radically Open Security (ROS) performed a security audit of some parts of Monal.
- Snikket Android app temporarily [unavailable in Google Play store](https://snikket.org/blog/snikket-google-play-removal) (problem already resolved)

## Software News

### Clients and Applications

- [Monal 6.3.0](https://github.com/monal-im/Monal/releases/tag/Build_iOS_900) has been released, which brings support for [XEP-0425: Moderated Message Retraction](https://xmpp.org/extensions/xep-0425.html) and [XEP-0490: Message Displayed Synchronization](https://xmpp.org/extensions/xep-0490.html).
- [Movim 0.24 "#Mueller"](https://mov.im/node/pubsub.movim.eu/Movim/007843a5-5a44-4710-86a1-70ad7e18bd84) and a [0.24.1 bugfix](https://mov.im/node/pubsub.movim.eu/Movim/d71c1b3a-d36a-4eb4-a6fb-ff245123348f) have been released.
- [Psi+ 1.5.1747 through 1.5.1816 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) and [Psi+ 1.5.1768 through 1.5.1819 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) have been released. Now with Qt6 instead of Qt5.

### Servers

- [MongooseIM 6.2.1](https://github.com/esl/MongooseIM/releases/tag/6.2.1) has been released. Version 1.1.0 of [XEP-0313 Message Archive Management](https://xmpp.org/extensions/xep-0313.html) is now supported. The improved CETS in-memory storage backend allows you to easily deploy, manage and scale your MongooseIM installation in the cloud without the burden of persistent volumes.
- [ejabberd Docs now using MkDocs](https://www.process-one.net/blog/ejabberd-docs-now-using-mkdocs/)

### Libraries & Tools

- [Smack 4.4.8](https://discourse.igniterealtime.org/t/smack-4-4-8-released/93807) has been released
- [Slidge v0.1.0](https://sr.ht/~nicoco/slidge/) Slidge is an XMPP (puppeteer) gateway library in python. It makes writing gateways to other chat networks (legacy modules) as frictionless as possible.
- [go-xmpp 0.2.0](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.0).
- [go-sendxmpp 0.10.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.10.0).

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- No XEP was proposed this month.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 0.7.0 of XEP-0333 (Displayed Markers)
  - Change title to "Displayed Markers"
  - Bring back Service Discovery feature (dg)
- Version 0.4.1 of XEP-0440 (SASL Channel-Binding Type Capability)
  - Recommend the usage of tls-exporter over tls-server-end-point (fs)
- Version 0.2.1 of XEP-0444 (Message Reactions)
  - fix grammar and spelling (wb)
- Version 1.0.1 of XEP-0388 (Extensible SASL Profile)
  - Fixed typos (md)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- XEP-0398: User Avatar to vCard-Based Avatars Conversion

### Stable

- Version 1.0.0 of XEP-0386 (Bind 2)
  - Accept as Stable as per Council Vote from 2024-04-02. (XEP Editor (dg))
- Version 1.0.0 of XEP-0388 (Extensible SASL Profile)
  - Accept as Stable as per Council Vote from 2024-04-02. (XEP Editor (dg))
- Version 1.0.0 of XEP-0333 (Displayed Markers)
  - Accept as Stable as per Council Vote from 2024-04-17. (XEP Editor (dg))
- Version 1.0.0 of XEP-0334 (Message Processing Hints)
  - Accept as Stable as per Council Vote from 2024-04-17 (XEP Editor (dg))

### Deprecated

- No XEP deprecated this month.

### Rejected

- XEP-0360: Nonzas (are not Stanzas)

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

This is a community effort, and we would like to thank translators for their contributions. Volunteers an more languages are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: *Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, XSF iTeam*
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: *nicola*

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



