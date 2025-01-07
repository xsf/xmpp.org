---
title: The XMPP Newsletter March 2022
author: XMPP Communication Team and Contributors
date: 2022-04-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of March 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
- Italian: [nicfab.it](https://www.nicfab.it/)
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)

## XSF Announcements

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

- The XSF has been accepted as hosting organization at [Google Summer of Code 2022 (GSoC)](https://xmpp.org/community/gsoc-2022/). If you are interested in participating as a student, mentor or as a project in general, please [add your ideas and reach out to us](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022). The contributor application period has begun already, so be quick!
- XMPP Newsletter via mail: We migrated to our [own mail-list server](https://mail.jabber.org/mailman/listinfo/newsletter) and stopped using Tinyletter. Its read-only and you will receive the XMPP Newsletter on a monthly basis. It also eliminates the privacy concerns with Tinyletter.

## XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

The Profanity devs posted a quick guide on how to use [OpenPGP for XMPP (OX)](https://profanity-im.github.io/blog/post/openpgp-for-xmpp-ox/).

[JMP's Newsletter](https://blog.jmp.chat/b/march-newsletter-2022) announces a new client for Android (based on Conversations) that has a focus on improving UX for users of standards-compliant gateways.

![JMP Cheogram](/images/newsletter/2022-03/cheogram-screenshot.png "JMP Cheogram")

The [Mellium Dev Communiqué for March 2022](https://opencollective.com/mellium/updates/dev-communique-for-march-20222) has been released! This release includes changes to the sidebar in the Communiqué TUI client and improvements to various packages in the main mellium.im/xmpp module.

## Software news

### Clients and applications

[Gajim development news](https://gajim.org/post/2022-03-24-development-news-march/): March brings a new issue reporting system and many performance improvements for both Gajim and python-nbxmpp. Gajim’s OMEMO plugin comes with some improvements as well. Last but not least, there has been a security issue in python-nbxmpp, which has been fixed in version `2.0.6`.

[Openfire Pàdé `1.5.7` and `1.6.3`](https://discourse.igniterealtime.org/t/openfire-pade-1-6-3-released/91536) and [Openfire Pàdé 1.6.2](https://discourse.igniterealtime.org/t/openfire-pade-1-6-2-released/91424) have been released.

[Profanity `0.12.0`](https://github.com/profanity-im/profanity/releases) has been released, with in-band account registration and user mood support, new theme, improved OX user experience (as the article above shows) and a slew of fixes and polished features.

[Psi+ `1.5.1615` and Psi+ `1.5.1618`](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) have been released.

[Conversations `2.10.5`](https://github.com/iNPUTmice/Conversations/blob/master/CHANGELOG.md) is out, bringing better call reconnections after network switches, showing caller JID and account JID in incoming call screen, adapting the file storage locations per the new Android 11 requirements and a security fix affecting file downloads. Note that the F-Droid version lags behind, due to unrelated issues, but `2.10.2.1` is out and includes only the security fix. Also announced was that accounts on conversations.im are free from now on.

## Servers
[Jackal `0.58.0`](https://github.com/ortuman/jackal/releases/tag/v0.58.0) has been released and added the BoltDB repository type.

After three years of development [Prosody `0.12.0`](https://blog.prosody.im/prosody-0.12.0-released/) has been released. The update covers XMPP Compliance, mobile and connectivity optimizations, updated HTTP file sharing, improved audio/video calling support, Direct TLS and many more - congratulations! 

![Prosody](/images/newsletter/2022-03/grafana-screenshot.png "Prosody")

[Tigase XMPP Server `8.2.0`](https://github.com/tigase/tigase-server/releases/tag/tigase-server-8.2.0) has been released! Biggest feature is the support for MIX protocol, which offers better group chat experience, especially on mobile devices. Group chat (MUC) was not left be and received a lot of fixes as well. In addition we improved server-to-server connectivity, added option to store certificates in the repository (really helpful in cluster deployments) and more!

The Ignite Realtime community is happy to announce the immediate availability of a maintenance release `2.2.3` of the [GoJara plugin for Openfire](https://discourse.igniterealtime.org/t/gojara-plugin-for-openfire-version-2-2-3-release/91505). GoJara provides an implementation of [XEP-0321 “Remote Roster Management”](https://xmpp.org/extensions/xep-0321.html) and helps out with monitoring [Spectrum 2](https://spectrum.im/).

## Libraries

slixmpp version [`1.8.1`](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.8.1) has been released, fixing a compatibility issue with the python standard library due to the defusedxml introduction in the `1.8.0` release.

python-nbxmpp versions [`2.0.5` and `2.0.6`](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/nbxmpp_2.0/ChangeLog) have been released, fixing a security issue in resolving websocket URIs.

[Smack `4.4.5` and `4.5.0-alpha1`](https://discourse.igniterealtime.org/t/smack-4-4-5-and-4-5-0-alpha1-released/91437) has been released.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   No XEPs proposed this month.

### New

-   Version 0.1.0 of [XEP-0462](https://xmpp.org/extensions/xep-0462.html) (PubSub Type Filtering)
    -   Accepted by vote of Council on 2022-02-09.

-   Version 0.1.0 of [XEP-0463](https://xmpp.org/extensions/xep-0463.html) (MUC Affiliations Versioning)
    -   Accepted by vote of Council on 2022-02-16.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 1.6.0 of [XEP-0115](https://xmpp.org/extensions/xep-0115.html) (Entity Capabilities)
    -   Mention preimage attacks explicitly (ssw)

-   Version 1.4.0 of [XEP-0156](https://xmpp.org/extensions/xep-0156.html) (Discovering Alternative XMPP Connection Methods)
    -   Remove DNS `_xmppconnect` method due to security vulnerability. (tjb)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   No Last Call this month.

### Stable (formerly known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

-   No XEPs advanced to Stable this month.

### Deprecated

-   No XEP deprecated this month.

### Obsoleted

-   [XEP-0008](https://xmpp.org/extensions/xep-0008.html) (IQ-Based Avatars)
    -   Obsoleted due to two superseding specifications (egp)

-   [XEP-0038](https://xmpp.org/extensions/xep-0038.html) (Icon Styles)
    -   Obsolete due to the omnipresence of Unicode emoji, as well as Bits of Binary stickers. (egp)

-   [XEP-0051](https://xmpp.org/extensions/xep-0051.html) (Connection Transfer)
    -   Obsolete because this feature has been merged into XMPP core, see RFC6120 section 4.9.3.19, which describes the `<see-other-host/>` stream error. (egp)

-   [XEP-0138](https://xmpp.org/extensions/xep-0138.html) (Stream Compression)
    -   Obsolete due to security vulnerability. (tjb)

-   [XEP-0229](https://xmpp.org/extensions/xep-0229.html) (Stream Compression with LZW)
    -   Obsolete due to security vulnerability. (tjb)

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Spread the news!

Please share the news on other networks:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

Here you can [subscribe via email](https://mail.jabber.org/mailman/listinfo/newsletter). It is read-only and only the Newsletter will be send to you on a monthly basis.

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, MattJ, nicfab, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat, Ysabeau, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

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
