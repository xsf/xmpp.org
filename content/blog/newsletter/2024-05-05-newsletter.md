---
title: The XMPP Newsletter April 2024
date: 2024-05-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of April 2024.

## XSF Announcements

If you are interested to join the XMPP Standards Foundation as member, [please apply until 19th May 2024!](https://wiki.xmpp.org/web/Membership_Applications_Q2_2024).

### XMPP and Google Summer of Code 2024

The XSF has been accepted as a [hosting organisation at GSoC in 2024](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024) again!
Currently XMPP project mentors are reviewing the proposals.
GSoC project ideas from XMPP-related projects are:

- Monal
  - [Modern Onboarding (90 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Modern_Onboarding)
  - [Media Gallery (90 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
  - [MDM support (175 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/MDM_support)
  - [SiriKit support (350 hours, medium)](https://wiki.xmpp.org/web/Gsoc2024/Monal/SiriKit_support)
- Dino
  - [Inline link preview (175 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Dino/Inline_link_preview)
  - [Rich message support (175 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Dino/Rich_message_support)
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


## Articles


## Software News

### Clients and Applications


### Servers


### Libraries & Tools


## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- [Message Displayed Synchronization](https://xmpp.org/extensions/inbox/xep-mds.html)
  - This specification allows multiple clients of the same user to synchronize the displayed state of their chats.

### New

- Version 0.1.0 of XEP-0485 (PubSub Server Information)
  - Promoted to Experimental. (dg)
- Version 0.1.0 of XEP-0486 (MUC Avatars)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of XEP-0487 (Host Meta 2 - One Method To Rule Them All)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of XEP-0488 (MUC Token Invite)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of XEP-0489 (Reporting Account Affiliations)
  - Promoted to Experimental (XEP Editor: dg)
- Version 0.1.0 of XEP-0490 (Message Displayed Synchronization)
  - Promoted to Experimental (XEP Editor: dg)

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.25.0 of XEP-0001 (XMPP Extension Protocols)
  - Add note that editorial changes do not affect Deferred state (XEP Editor: dg)
- Version 1.26.0 of XEP-0060 (Publish-Subscribe)
  - Add examples for publishing item without ID (melvo)
- Version 1.1.1 of XEP-0313 (Message Archive Management)
  - Add XEP-0136 to superseded specifications (gdk)
- Version 0.5.0 and 0.6.0 of XEP-0333 (Displayed Markers (was: Chat Markers))
  - Remove `<received/>` to not replicate  functionality.
  - Remove `<acknowledged/>` because it was not implemented in the last 10 years and apparently is not needed.
  - Remove Disco feature. Opting in via `<markable/>` is enough (dg)
  - Add Business Rule about opportunistic Displayed Markers in 1:1 chats (dg)
- Version 0.5.0 of XEP-0334 (Message Processing Hints)
  - Incorporate last call feedback from 2017.
  - Differences between this specification and XEP-0079 have been clarified.
  - A note about handling of hints found in error stanzas has been added. (mw)
- Version 0.4.1 of XEP-0388 (Extensible SASL Profile)
  - Add missing elements to XML Schema
  - Add missing XMPP Registrar Considerations (dg)
- Version 0.3.0 of XEP-0398 (User Avatar to vCard-Based Avatars Conversion)
  - Add text to explain that both  and  are valid implementations.
  - Add Security Considerations for both variants (dg)
- Version 0.4.1 of XEP-0424 (Message Retraction)
  - Fix schema.
  - Add missing for attribute in fallback element (Example 4). (nc)
- Version of XEP-0425 (Moderated Message Retraction)
  - Remove the dependency on XEP-0422 Message Fastening
  - Rename to 'Moderated Message Retraction' and focus only on the retraction use-case
  - Ensure compatibility with clients that only implement XEP-0424
  - Clarify the purpose of the `<reason/>` element
- Version 0.3.0 and 0.3.1 of XEP-0447 (Stateless file sharing)
  - Describe how to use for multiple files, with body text, without any source in original message and compatibility with various current deployed protocols. (lmw)
  - Fix example for multiple files. (lmw)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- XEP-0333: Displayed Markers (was: Chat Markers)
- XEP-0334: Message Processing Hints
- XEP-0360: Nonzas (are not Stanzas)
- XEP-0386: Bind 2
- XEP-0388: Extensible SASL Profile
- XEP-0392: Consistent Color Generation

### Stable

- Version 1.0.0 of XEP-0392 (Consistent Color Generation)
  - Accept as Stable as per Council Vote from 2024-03-27. (XEP Editor (dg))

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
  - General contributors: *Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Federico, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, XSF iTeam*
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



