---
title: The XMPP Newsletter September 2023
date: 2023-10-07
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of September 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

### XMPP and Google Summer of Code 2023

The XSF has been [accepted again as hosting organisation at the GSoC 2023 and receive two slots for XMPP Contributors](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/)!

On Dino:

- [Windows support for Dino](https://hrxi.github.io/gsoc/blog/windows-support-for-dino)
- [Windows woes](https://hrxi.github.io/gsoc/blog/windows-woes)

On Moxxy:

- The [first blog post](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), detailing the plan to implement basic group chat functionality.
- The [second blog post](https://moxxy.org/posts/2023-06-17-XEP-0045-In-Moxxmpp.html), describing the plans to bring a basic implementation of [XEP-0045](https://xmpp.org/extensions/xep-0045.html) into Moxxy’s XMPP library moxxmpp.
- The [third blog post](https://moxxy.org/posts/2023-07-24-Join-MUC-With-Moxxy.html), sketching the frontend implementation plan.
- The [fourth blog post](https://moxxy.org/posts/2023-08-20-Moxxy-MUC-GSoC-Final-Report.html), concluding with Moxxy's completed MUC support.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month
- [XMPP Italian happy hour](https://tube.nicfab.eu/c/xmpp): monthly Italian XMPP web meeting, starting May 16th and then every third Tuesday of the month at 7:00 PM (online event, with web meeting mode and live streaming).
- [TroLUG XMPP Workshop](http://trolug.de/termine.html) The TroLUG organizes the second workshop on XMPP in German language on 2023-09-07. It takes place as audio conference via BBB. All nice people are invited to join the workshop.

- The GSoC Organisation Administrator will participate this year's Google Mentor Summit in Sunnyvale!

## Videos

There has been an XMPP track at [FOSSY2023](https://2023.fossy.us/schedule/) with many talks:

- [XMPP Connectivity & Security](https://archive.org/details/fossy2023_XMPP_Connectivity__Security) is an introduction about XMPP connectivity XEPs like XEP-0368 (Direct TLS), XEP-0467 (QUIC), XEP-0468 (WebSocket S2s) and the internals of xmpp-proxy, a forward+reverse proxy, and others.
- [XMPP Introduction and Overview](https://archive.org/details/fossy2023_XMPP_Introduction_and_Overview) is a brief history and introduction to the XMPP protocol for people with small background in programming.
- [My XMPP Past, Present, and Future](https://archive.org/details/fossy2023_My_XMPP_Past_Present_and_Futur) is a point-of-view journey through the evolution of the XMPP ecosystem from 2004. It explains how it was affected by major events such as the decline of traditional IM services, the beginning of the smartphone era and new chat services, and more.
- [Building open standards-based ecosystems](https://archive.org/details/fossy2023_Building_open_standardsbased_e) is a talk about how XMPP as both a community and a protocol adapted to change, and the role that the XSF played in its continuity, but also a general discussion about sustainability of open ecosystems and open networks.

## Articles

- [JMP Newsletter: Summer in Review](https://blog.jmp.chat/blog/view/blog.jmp.chat/@/id/septermber-newsletter-2023). JMP lets you send and receive text and picture messages (and calls) through a real phone number right from your computer, tablet, phone, or anything else that has a Jabber client.  Among other things, JMP has these features: Your phone number on every device; Multiple phone numbers, one app; Free as in Freedom; Share one number with multiple people.
- [State of Snikket 2023: Funding](https://snikket.org/blog/snikket-2023-funding/). This post in the series is covering financial topics of the project.

## Software news

### Clients and applications

- [Moxxy 0.5.0](https://codeberg.org/moxxy/moxxy/releases/tag/v0.5.0) has been released. This release brings improved notifications, image picking, and translations. Initial work on groupchats has been started, thanks to the Google Summer of Code 2023.

{{< figure src="/images/newsletter/2023-10-05/moxxy-muc-demo.gif" caption="Moxxy Group Chat (MUC) Demo" >}}

### Servers

- [Prosody 0.12.4](https://blog.prosody.im/prosody-0.12.4-released/) has been released.

### Libraries & Tools

- [XMPP Account Exporter](https://migrate.modernxmpp.org/) received an update, which brings many layout improvements and support for exporting bookmarks.
- [Ejabberd auth script for Lemmy](https://f-hub.org/Solarpunk/ejabberd-auth-lemmy), to bring secure chat to the users of your [federated Reddit alternative](https://join-lemmy.org/). This extends a collection of Fediverse [integrations on JoinJabber.org](https://joinjabber.org/tutorials/integration/).

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

- No XEPs update this month.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

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

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), nicola, XSF iTeam**
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
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
