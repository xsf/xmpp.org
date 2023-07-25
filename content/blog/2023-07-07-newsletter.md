---
title: The XMPP Newsletter June 2023
date: 2023-07-07
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of June 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

- If you are interested to become an [XSF member](https://xmpp.org/community/membership/) you can apply during Q3 2023 soon.

### XMPP and Google Summer of Code 2023
The XSF has been [accepted again as hosting organisation at the GSoC 2023 and receive two slots for XMPP Contributors](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/)!

On Dino:
 - [Windows support for Dino](https://hrxi.github.io/gsoc/blog/windows-support-for-dino)

On Moxxy:
- The [first blog post](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), detailing the plan to implement basic groupchat functionality.
- The [second blog post](https://moxxy.org/posts/2023-06-17-XEP-0045-In-Moxxmpp.html), describing the plans to bring a basic implementation of [XEP-0045](https://xmpp.org/extensions/xep-0045.html) into Moxxy’s XMPP library moxxmpp.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month
- [FOSSY](https://fossy.us) will have an XMPP track at their conference this summer from July 13-16th 2023
- [XMPP Italian happy hour](https://tube.nicfab.eu/c/xmpp): monthly Italian XMPP web meeting, starting May 16th and then every third Tuesday of the month at 7:00 PM (online event, with web meeting mode and live streaming).

## Talks

- [Une messagerie instantanée qui respecte vos libertés ?](https://www.a-lec.org/actus/2023-06-23-conference-xmpp-bourbon-archambault/)[FR]: Through a brief history of the web, in order to depict its current centralization centralization and its problems, Adrien Bourmault, member of the XMPP Standards Foundation, will introduce you to the problems problems posed by non-free instant messaging, based on centralized applications and services, and explore the solutions offered by the solutions offered by decentralization and free software with XMPP.

## Articles

No articles have reached us this month. :-(

## Software news
### Clients and applications

- [JMP is launched and out of Beta](https://blog.jmp.chat/b/launch-2023)
- [Cheogram Android version `2.12.1-6`](https://git.singpolyma.net/cheogram-android/refs/2.12.1-6) adds per account colours, per account quiet hours, thumbhash previews of un-downloaded files, and more.
- [Libervia progress note 2023-W22](https://www.goffi.org/b/libervia-progress-note-2023-w22-x3Wa) on A/V Implementation, ActivityPub Gateway and more.

### Servers

No updates on servers have reached us this month. :-(

### Libraries & Tools

- New website and [xmpp.rs version 0.4 release](https://xmpp.rs/blog/release-xmpp-0-4/): After more than 3 years and half since the last release (version 0.3 in septembre 2019), xmpp-rs developers are happy to announce xmpp-rs version 0.4.0. If you don't know about xmpp-rs, those are Rust crates for interoperable and federated instant messaging and other social networking applications.
- The ejabberd [mod_s3_upload](https://github.com/processone/ejabberd-contrib/tree/master/mod_s3_upload) module gained [support for the use of a separate download host](https://github.com/processone/ejabberd-contrib/pull/320). This allows clients to download media content from a statically hosted S3 bucket. This was initially proposed to allow ejabberd to integrate with [Garage](https://garagehq.deuxfleurs.fr/), an open-source distributed object storage service tailored for self-hosting.
- [omemo_dart](https://github.com/PapaTutuWawa/omemo_dart) released [version 0.5.0](https://github.com/PapaTutuWawa/omemo_dart/releases/tag/v0.5.0), which finally allowed Moxxy to establish stable OMEMO:2 sessions between two Moxxy clients.
- [Openfire inVerse plugin v10.1.4-1 release!](https://discourse.igniterealtime.org/t/openfire-inverse-plugin-v10-1-4-1-release/92969)

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

- No Last Call this month.

### Stable

- No XEP moved to stable this month.

### Deprecated

- No XEP deprecated this month.

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

