---
title: The XMPP Newsletter October 2022
date: 2022-11-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of October 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **emus, Licaon_Kter, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), wurstsalat, Zash** 
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, Ppjet6**
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
  - Translators: **Jeybe, wh0nix**
- Italian: [nicfab.it](https://www.nicfab.it/)
  - Translators: **nicfab**
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Translators: **daimonduff, TheCoffeMaker**

## XSF Announcements

- The XSF membership application period for the fourth quarter 2022 is currently open. If you are interested in becoming a XSF member then you can [apply for membership](https://wiki.xmpp.org/web/Membership_Applications_Q4_2022). Please submit by November 27, 2022.

### Google Summer of Code 2022

{{< figure src="/images/logos/GSoC_2022_Logo.png" caption="XSF and Google Summer of Code 2022" >}}

The Google Summer of Code 2022 has finished! The two new contributors Patiga and PawBud worked on open-source software projects in the XMPP environment. Read the final collection blog posts:
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
- [Capitole du Libre](https://capitoledulibre.org): Members of the “JabberFR” and “Libre en Communs” associations will be present in Toulouse on the 19-20th of November

## Articles

ejabberd has added [Matrix protocol support](https://www.process-one.net/blog/matrix-protocol-added-to-ejabberd/) bringing their experience of scaling XMPP and MQTT to this new messaging avenue. At first a subset of the protocol will be implemented, acting like a bridge between protocols. Bussiness customers will get a taste of it first and later it will come to the Community Edition.

The [JMP Newsletter](https://blog.jmp.chat/b/october-newsletter-2022) details a big new release of the Cheogram Android client with features including XHTML-IM, Bits of Binary, a form of message retraction, contact tagging, and more.  They also talk about an [XMPP channel integration they have built](https://github.com/chatwoot/chatwoot/pull/5587) for the Chatwoot support software, and offer to let community projects use their instance to try it out. This month they also wrote an article about [SMS Account Verification](https://blog.jmp.chat/b/2022-sms-account-verification) and how it affects the ecosystem.

PGPainless: [Implementing Packet Sequence Validation using Pushdown Automata](https://blog.jabberhead.tk/2022/10/26/implementing-packet-sequence-validation-using-pushdown-automata/)

A new automated testing technique was recently adopted to help the Prosody developers during their daily development work: [Mutation Testing in Prosody](https://blog.prosody.im/mutation-testing-in-prosody/)

Modernization of the authentication protocol is ongoing around the community, keyword "SASL". Multiple hints of the work have been seen in the last two newsletters, in [libs](https://xmpp.org/2022/09/the-xmpp-newsletter-august-2022/#libraries), [XEPs](https://xmpp.org/2022/10/the-xmpp-newsletter-september-2022/#updated) updates and [funding](https://xmpp.org/2022/10/the-xmpp-newsletter-september-2022/#articles) news. It spans multiple clients, multiple platforms and at least one server. Thilo Molitor, the Monal developer, blogged about the current _broken_ state, the ideal properties of the system and [the solutions being worked on](https://monal-im.org/post/00004-sasl/). It's a 30 minutes long read but will sure come handy as more news of the SASL implementations will start to appear from the other involved projects.

## Software news

### Clients and applications

Converse has released [version 10.0.0](https://github.com/conversejs/converse.js/releases/tag/v10.0.0) with a lot of polishing and an updated feature set.

[Dino 0.3.1](https://github.com/dino/dino/releases/tag/v0.3.1) has been released, which is a maintenance release for libsoup3 support and bug fixes.

[Gajim 1.5.2](https://gajim.org/post/2022-10-08-gajim-1.5.2-released/) and [1.5.3](https://gajim.org/post/2022-10-31-gajim-1.5.3-released/) have been released. These releases bring another performance boost, better emojis, selection of multiple messages, and many bug fixes.

{{< figure src="/images/newsletter/2022-11-07/gajim-emoji-shortcodes.png" caption="Gajim emoji shortcodes" >}}

[Profanity 0.13.1](https://github.com/profanity-im/profanity/releases/tag/0.13.1) is out with improved plugins management.

[Psi+ 1.5.1641 (2022-09-24)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) has been released.

Monal 5.3.3 has been [live in the AppStore](https://apps.apple.com/app/id317711500) for a while now, and even if it does not yet bring the SASL improvements mentioned above or the much awaited audio and video calls capabilities [funded last month](https://xmpp.org/2022/10/the-xmpp-newsletter-september-2022/#articles), it does feature several fixes for registrations, screenshots sharing and read markers.

aTalk has been released with [an almost monthly cadence](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt). Each new version brings more polish, like location/map views, calls, libraries updates and keeping up to date on the newer Android requirements. It's biggest adoption impediment unfortunately still stays and stems from an outdated UI that precedes Android 5 Material UI.

### Servers

[ejabberd 22.10](https://www.process-one.net/blog/ejabberd-22-10/) release includes six months of work, over 140 commits, including relevant improvements in MIX, MUC, SQL, and installers, and bug fixes as usual.

[Jackal 0.62.3](https://github.com/ortuman/jackal/releases/tag/v0.62.3) is out bringing 3 fixes for storage/archive and s2s stanzas.

### Libraries & Tools

[python-nbxmpp 3.2.4 and 3.2.5](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) have been released, bringing bug fixes and internal improvements.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

xmpp.org features [a page about XMPP RFCs](https://xmpp.org/rfcs/) as well.

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to 
accept this proposal as an Experimental XEP.

- [PubSub Social Feed](https://xmpp.org/extensions/inbox/pubsub-social-feed.html)
  - This specification defines a way of publishing social content over XMPP.
- [SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/inbox/xep-downgrade-prevention.html)
  - This specification provides a way to secure the SASL and SASL2 handshakes against method and channel-binding downgrades.
- [OpenPGP for XMPP Pubsub](https://xmpp.org/extensions/inbox/pubsub-encryption.html)
  - Specifies an OpenPGP for XMPP (XEP-0373) profile for the pubsub use case.

### New

- No new XEP this month.
  
### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it 
will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- No XEPs updated this month.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

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
