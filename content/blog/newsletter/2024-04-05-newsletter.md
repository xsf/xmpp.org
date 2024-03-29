---
title: The XMPP Newsletter March 2024
date: 2024-04-05
categories: ['Newsletter']
---

# The 50th release of the XMPP Newsletter!

This is the 50th release of the XMPP Newsletter since it started in February 2019.
At the Summit at Brussels JC Brand, Nicolas Vérité (Nyco) and Severino Ferrer (S0ul) proposed and initialed the XMPP Newsletter and since then we had almost every month a release of the news in the XMPP universe.
We think it is worth to celebrate this achievement and say thanks to all the contributors as well as all our readers!
We are looking forward to the next releases and invite you to participate! We would love to see more contributors as well as more translations.

So, welcome to the 50th edition of the XMPP Newsletter, great to have you here again!
This issue covers the month of March 2024.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

Welcome to our reapplicants and new members in Q1 2024!
If you are interested to join the XMPP Standards Foundation as member, [please apply now](https://wiki.xmpp.org/web/Membership_Applications_Q2_2024).

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

## Talks

- Last November the [Linux Inlaws Podcast](https://linuxinlaws.eu/#episodes) hosted Edward and Matt from the XSF Board 2024.
The episode has been published recently and can be accessed via [archive.org](https://archive.org/download/LI_S02E06_XMPP__EA30/LI_S02E06_XMPP_.mp3).

## Articles

Axel Reimer published an XMPP app decision table. It compares typical instant messaging features of popular XMPP apps and might be a guideline for new users who want to try an XMPP app.
The table is available in [English](https://apps.xmpp24.de/english/) and [German](https://apps.xmpp24.de/deutsch/).

You can now ask all your questions about [XMPP Providers](https://providers.xmpp.net) in the **new** [support chat](https://providers.xmpp.net/blog/2024-03-11-xmpp-providers-chat/).
That chat is hosted on an own XMPP server which is set up with the **new** [XMPP Providers Server](https://providers.xmpp.net/blog/2024-03-28-xmpp-providers-server/) project.
It is a simple, Ansible-based all-in-one server setup that can be used for *your* own XMPP server as well.

[Snikket Hosting is now publicly available!](https://snikket.org/blog/snikket-hosting-launched/) The launch is about providing new ways to get started with Snikket, not replacing
the options that are already available. If you are already self-hosting Snikket, or planning to, nothing is changing for you.
Though please do [donate to support](https://snikket.org/donate/) the project, even a little helps!

{{< figure src="/images/newsletter/2024-03-05/jmp-sip-gateway.png" caption="SIP via XMPP" >}}

## Software News

### Clients and Applications

- The [JMP newsletter introduces the JMP eSIM Adapter](https://blog.jmp.chat/b/march-newsletter-2024), allowing users to use eSIMs from any provider in any device. It explains how to download and write eSIMs to the adapter, including using an open source Android app or PC/SC reader. Cheogram Android also receives an update with new features and a visual refresh. There's a clarification on contact integration, with Google now requiring the app claim to upload the contacts even though it does not.
- [Converse 10.1.7](https://github.com/conversejs/converse.js/releases/tag/v10.1.7) with StropheJS fix for [XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.html).
- [Psi+ 1.5.1716](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/), [Psi+ 1.5.1682](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/),
[Psi+ 1.5.1669](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) have been released.

### Servers

- Openfire has been released in [version 4.8.1](https://discourse.igniterealtime.org/t/openfire-4-8-1-release/93681).
  - Openfire inVerse plugin [version 10.1.7.1 has been released](https://discourse.igniterealtime.org/t/openfire-inverse-plugin-version-10-1-7-1-released/93740).
  - Openfire [PionTurn plugin](https://discourse.igniterealtime.org/t/pionturn-plugin-1-0-0-released/93757) 1.0.0 released! It creates a TURN/STUN server for Openfire.

### Libraries & Tools

- A new release of [go-xmpp 0.1.4](https://github.com/xmppo/go-xmpp/releases/tag/v0.1.4).
- A new release of [go-sendxmpp 0.9.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.9.0).

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


