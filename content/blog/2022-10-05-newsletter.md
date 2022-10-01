---
title: The XMPP Newsletter September 2022
date: 2022-10-01
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of September 2022.

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

- The XSF Board and Council application period for the next year is currently open. If you are interested in running for the XSF Board or XSF Council then you can [apply here](https://wiki.xmpp.org/web/Board_and_Council_Elections_2022). Please submit by November 6, 2022. Remind that XMPP Council members must be elected members of the XSF; however, there is no such restriction for the Board of Directors.

- Security advisory: libexpat before 2.4.9 is vulnerable to [CVE-2022-40674](https://nvd.nist.gov/vuln/detail/CVE-2022-40674), make sure to update, if you depend on it.

### Google Summer of Code 2022

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

The Google Summer of Code 2022 finished! The two new contributors Patiga and PawBud were working on open-source software projects in the XMPP environment. Read their all their blog posts, too. Thanks everyone for participation!
  - **Patiga** worked on [more flexible file transfers in Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ). Mentors are **fiaxh** and **Marvin W.**.
    - [Stateless File Sharing GSoC project](https://dino.im/blog/2022/06/stateless-file-sharing-gsoc-project/)
    - [Project Stateless File Sharing: First Steps](https://dino.im/blog/2022/06/project-stateless-file-sharing-first-steps/)
    - [Stateless File Sharing: Base implementation](https://dino.im/blog/2022/08/stateless-file-sharing-base-implementation/)
    - [Stateless File Sharing: Sources and Compatibility](https://dino.im/blog/2022/08/stateless-file-sharing-sources-and-compatibility/)
    - [Stateless File Sharing: Async, Metadata with Thumbnails and some UI](https://dino.im/blog/2022/09/stateless-file-sharing-async-metadata-with-thumbnails-and-some-ui/)

  - **PawBud** worked towards [adding support for A/V communication via Jingle in ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19). Mentors are **JC Brand** and **vanitasvitae**.
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
- [Capitole du Libre](https://capitoledulibre.org): Members of the “JabberFR” and “Libre en Communs” associations will be present in Toulouse on the 19-20th of November

## Articles

Congrats to the Monal developers for the new [NLnet Funding](https://monal-im.org/post/00003-nlnet-funding/) that will cover privacy enhancements for the push servers, an explorative audio and video calls implementation, UI updates for MUC and Contact views, and SASL updates.

Paul Schaub wrote a [blog post](https://blog.jabberhead.tk/2022/09/14/using-pushdown-automata-to-verify-packet-sequences/) focused on the technical details of how to check the validity of nested packet sequences using pushdown automata. This technique will be used in a partial rework of PGPainless to validate OpenPGP messages. Earlier this month another post on ["Creating a Web-of-Trust Implementation: Accessing Certificate Stores"](https://blog.jabberhead.tk/2022/09/01/creating-a-web-of-trust-implementation-accessing-certificate-stores/) has been published, too.

![PGPainless to validate OpenPGP messages](/images/newsletter/2022-10-01/OpenPGPMessage.png "PGPainless to validate OpenPGP messages")

jmp.chat brought [voicemail changes and opt-in Jabber ID discoverability](https://blog.jmp.chat/b/september-newsletter-2022) to their service, along with an updated Android app and new custom F-Droid repos for both stable and pre-release versions. Furthermore, they wrote about ["Privacy and Threat Modelling"](https://blog.jmp.chat/b/2022-privacy-threat-modelling) in general.

Arnaud wrote about updates on the [chatty server and HTTPAuthentificationOverXMPP](https://blog.agayon.be/xmpp_auth_update.html).

Anoxinon.media published their blogpost [XMPP - Teil 1 - Messaging mal anders](https://anoxinon.media/blog/xmpp1/) [DE].

## Software news

### Clients and applications

Maintenance release of [Beagle IM 5.3.1](https://github.com/tigase/beagle-im/releases/tag/5.3.1) that fixes sending OMEMO encrypted files and entering password-protected MUC. Besides, Tigase launched a new, simpler website [tigase.org](https://tigase.org/) that makes it easier to access open-source projects created by Tigase.

![New tigase.org](/images/newsletter/2022-10-01/TigaseWebpage.png "New tigase.org")

Gajim 1.5.0 and 1.5.1 [have been released](https://gajim.org/post/2022-09-19-gajim-1.5.0-released/). These releases come with a significant performance boost. Pinned chats can be ordered via drag and drop, message corrections have been improved, and many bugs have been fixed.

[An OMEMO 2 implementation has just been merged ](https://mastodon.social/@Goffi/109053947560868978) to [Libervia](https://salut-a-toi.org), coming with Stanza Content Encryption ([XEP-0420](https://xmpp.org/extensions/xep-0420.html)) support, thanks to the great work of Syndace, author or [python-omemo](https://github.com/Syndace/python-omemo) (which has been updated in the process). One of the major benefits is that other Stanza elements can now be encrypted too, not only the body.
OX ([XEP-0373](https://xmpp.org/extensions/xep-0373.html)/[XEP-0374](https://xmpp.org/extensions/xep-0374.html)) should follow soon, exciting times!

While Monal development is going forward, see the funding news above, and they deployed new Push servers as announced in the [July 2022](https://xmpp.org/2022/08/the-xmpp-newsletter-july-2022/) XMPP Newsletter, users of old Monal versions would need to update, so if you or your contacts didn't already [the developers urge you to do it now](https://fosstodon.org/@Monal/108999198014279513).

Missed in the [August 2022 XMPP Newsletter](https://xmpp.org/2022/09/the-xmpp-newsletter-august-2022/) was a release of UWPX, the XMPP client for UWP (Windows 10) devices. While version v.0.43.0.0 has only a fixup it's unfortunately also the [Final Update](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.43.0.0) as the developer is stepping away from the project. Maintainers to follow-up are welcome to reach out!

Kaidan, a user-friendly and modern chat app for every device, will receive a grant by NLnet for [adding encrypted audio and video calls](https://www.kaidan.im/2022/09/03/audio-video-calls/). Congratulations!

### Servers

Jackal [v0.62.0](https://github.com/ortuman/jackal/releases/tag/v0.62.0) is out bringing [XEP-0313](https://xmpp.org/extensions/xep-0313.html) Message Archive Management support and several enhancements.

Metronome IM 4.0 [has been released](https://metronome.im/changelogs/4_0). This version introduces Lua 5.3 support, a revamped shared API for group chats stanza archiving, MIX Core/PAM experimental support, Message Moderation support and support for containerization.

[Profanity 0.13.0](https://github.com/profanity-im/profanity/releases/tag/0.13.0) has been released.

### Libraries & Tools

python-nbxmpp [3.2.2 and 3.2.3 have been released](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog), adding a stringprep implementation and improvements for detecting broken TCP connections.

The first beta of Slidge (XMPP bridges) is out!: Slidge, supporting Signal, Telegram, Discord, Steam, Mattermost, Facebook and Skype. Currently only direct messages are supported, but development is going further.
Find the article in [English](https://nicoco.fr/blog/2022/09/04/slidge-first-beta/) and [French](https://linuxfr.org/users/therealnicoco/journaux/la-premiere-beta-de-slidge-passerelles-xmpp-est-dehors).

Work on [XMPP ⇔ ActivityPub gateway](https://nlnet.nl/project/Libervia/) (supported by a [NLnel](https://nlnet.nl/) funding) has been achieved. The gateway supports features such as following/followers, favourite/like (or ["noticed" in XMPP terms](https://xmpp.org/extensions/xep-0470.html#noticed-foreword), reactions (compatible with [Pleroma](https://pleroma.social/)), mentions, sharing/reboost and lastly events (compatible with [Mobilizon](https://mobilizon.org)). It has been tested with [Mastodon](https://joinmastodon.org), Pleroma and Mobilizon. It's still considered alpha quality, [a blog post should follow soon to explain in more details](https://www.goffi.org).

Ignite Realtime Community:
  - REST API Openfire plugin 1.10.0 [has been released](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-10-0-released/92108)
  - New Openfire plugin: [Push Server](https://discourse.igniterealtime.org/t/new-openfire-plugin-push-server/92069)

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

xmpp.org features [a page about XMPP RFCs](https://xmpp.org/rfcs/) as well.

### Proposed
The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to 
accept this proposal as an Experimental XEP.

- [Events](https://xmpp.org/extensions/inbox/events.html)
  - This specification describes how to handle calendar events with XMPP

### New

- No new XEP this month.
  
### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it 
will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 0.4.0 of [XEP-0440](https://xmpp.org/extensions/xep-0440.html) (SASL Channel-Binding Type Capability)
  - Make sasl-channel-binding element a top level stream feature (dg)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

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

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, emus, goffi, Jeybe, Licaon_Kter, martin, MattJ, MSavoritias (fae,ve), nicfab, Ppjet6, vanitasvitae, wurstsalat, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

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
