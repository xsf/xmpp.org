---
title: The XMPP Newsletter February 2026
date: 2026-03-05
categories: ['Newsletter']
summary: "In this issue: XMPP material for DI.DAY!. XMPP Sprint in Berlin. Read about Snikket and Prosody IM relationship & goals. Learn about Upcoming changes to Let’s Encrypt and how they affect operators, Running Your Own XMPP Server, and Great Invitations. Update your clients with Conversations, Fluux Messenger, Gajim, Monal, Monocles, Profanity and xmpp-web. Update your servers: ejabberd. Specifications update: a proposed XEP, two new XEP's and three updates!"
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of February 2026.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/).

Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors. If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XMPP logo in Font Awesome

Just as we announced back in our [Newsletter December 2025](/2026/01/the-xmpp-newsletter-december-2025/#xmpp-logo-and-font-awesome) issue, the official XMPP logo now comes bundled up in [Font Awesome](https://fontawesome.com/) since version [7.2.0](https://fontawesome.com/changelog). And it looks [Awesome](https://fontawesome.com/icons/xmpp?f=brands&s=solid)!

## XMPP Events

- [XMPP material for DI.DAY](https://di-day.xmpp.link/): Four [recipes](https://imday.de/en/) to use an open chat protocol at the 'Digital Independence Day' ([DI.DAY](https://di.day/de)) from the XMPP community to enable people to start with independent messaging!

{{< figure src="/images/newsletter/2026-03-05/di-day.png" caption="Four recipes for an open chat protocol at the Digital Independence Day!" >}}

- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2026-06_Berlin) (DE / EN): will take place from June Friday 19th to Sunday 21st 2026, at the [Wikimedia Deutschland e.V.](https://www.openstreetmap.org/node/2551527703#map=19/52.498414/13.381049) offices in Berlin, Germany. If this sounds like the right event for you, come and join us! Just make sure to list yourself [here](https://wiki.xmpp.org/web/Sprints/2026-06_Berlin#Attendees), so we know how many people will attend and we can plan accordingly. If you have any questions or concerns, join us at the chatroom: [sprints@muc.xmpp.org](xmpp:sprints@muc.xmpp.org?join)!

## Videos and Talks

- [Discord Was Never the End Game](https://youtu.be/XwMWUZYUTvM): a quick and painless tutorial on how to install XMPP, and self host an XMPP server on NixOS by [tony-btw](https://www.youtube.com/@tony-btw).
- [[PT-BR] XMPP #engineeringsessions #S06E16](https://youtu.be/dNmUZvM5CUA). [PT-BR]

## XMPP Articles

- [Upcoming changes to Let’s Encrypt and how they affect operators](https://blog.prosody.im/2026-letsencrypt-changes/), by the The Prosody Team for [Prosodical Thoughts](https://blog.prosody.im/).
- [Apprise](https://github.com/caronc/apprise/blob/master/README.md), Push Notifications that work with just about every platform, [_restored_](https://github.com/caronc/apprise/pull/1505) its XMPP support using [Slixmpp](https://codeberg.org/poezio/slixmpp/src/branch/master/README.rst), (after >4 years). ATM no _stable_ [release](https://github.com/caronc/apprise/releases), but it's coming …
- [Bye bye Discord, hello Movim!](https://mov.im/community/pubsub.movim.eu/Movim/bye-bye-discord-hello-movim-FunzTy), by Timothée Jaussoin for the [Movim Blog ](https://mov.im/community/pubsub.movim.eu/Movim).
- [A (big) memory incoming memory optimization in Movim](https://mov.im/community/pubsub.movim.eu/Movim/a-big-memory-incoming-memory-optimization-in-movim-k1GWXd), by Timothée Jaussoin for the [Movim Blog ](https://mov.im/community/pubsub.movim.eu/Movim).
- [Great Invitations](https://joinjabber.org/tutorials/service/great_invitations/), a tutorial that outlines how to create invites for the most popular clients according to [XEP-0401](/extensions/xep-0401.html) (Ad-hoc Account Invitation Generation), from the [tutorials](https://joinjabber.org/tutorials/) section at [joinjabber.org](https://joinjabber.org/).
- [Visite nossa cozinha](https://blog.isacloud.im/visite-nossa-cozinha/), by [Isadora](https://blog.isacloud.im/sobre/) for the [isacloud.im blog](https://blog.isacloud.im/). [PT_BR]
- [About Snikket and Prosody IM: relationship & goals in the XMPP ecosystem](https://news.ycombinator.com/item?id=47034801#47037214), by [MattJ](https://matthewwild.co.uk/about/) on [Hacker News](https://news.ycombinator.com).
- [Running My Own XMPP Server](https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/), by [danny](https://blog.dmcc.io/contact/) for the [dmcc blog](https://blog.dmcc.io/).
- [MembeBot: ohhh I member](https://cyberdelia.com.ar/membebot-ohhh-i-member.html): ¿Listo para implementar tu propio sistema de notificaciones de eventos en calendario sin depender de gigantes tecnológicos? by [TheCoffeMaker](https://rebel.ar/@thecoffemaker) for [Cyberdelia](https://cyberdelia.com.ar/). [ES]
- [Introducing Wimsy](https://github.com/dwd/Wimsy/blob/main/README.md): A cross-platform XMPP client built with Flutter.

## XMPP Software News

### XMPP Clients and Applications

- [Conversations](https://conversations.im/) has released versions [2.19.10](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.10), [2.19.11](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.11) and [2.19.12](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.12) for Android. This version introduces a refactored QR code scanning and URI handling, a fix for rotation issues in tablet mode and also offers to delete messages when banning someone in a public channel among other things. You can take a look at the [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) for all the details.
- [Fluux Messenger](https://github.com/processone/fluux-messenger/blob/main/README.md), a modern, cross-platform XMPP client for communities and organizations, versions [0.11.3](https://github.com/processone/fluux-messenger/releases/tag/v0.11.3), [0.12.0](https://github.com/processone/fluux-messenger/releases/tag/v0.12.0),  [0.12.1](https://github.com/processone/fluux-messenger/releases/tag/v0.12.1), [0.13.0](https://www.process-one.net/blog/fluux-messenger-0-13/), [0.13.1](https://github.com/processone/fluux-messenger/releases/tag/v0.13.1) and [0.13.2](https://github.com/processone/fluux-messenger/releases/tag/v0.13.2) have been released, with a list of additions, new features, improvements and bugfixes that is way longer than what we could ever mention in here! Go straight for the [changelog](https://github.com/processone/fluux-messenger/blob/main/CHANGELOG.md) for all the details!

{{< figure src="/images/newsletter/2026-03-05/fluux-main-console.png" caption="Fluux Messenger main window and XMPP console" >}}

- [Gajim](https://gajim.org/) has released version [2.4.4](https://gajim.org/posts/2026-02-25-gajim-2.4.4-released/) of its free and fully featured chat app for XMPP. This release comes with link previews, many improvements for macOS, and bugfixes. Thank you for all your contributions! You can take a look at the [changelog](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) for all the details.

{{< figure src="/images/newsletter/2026-03-05/gajim-link-previews.png" caption="Link previews in Gajim 2.4.4" >}}

- [Monal](https://monal-im.org/) has released versions [6.4.18](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1077) for iOS and macOS.
- [Monocles](https://monocles.eu/more) has released versions [2.1.2](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.1.2) and [2.1.3](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.1.3) of its chat client for Android. The former release brings fixes for message retraction, images send as link and infinite recursion in `TagEditorView`, adds support for links in posts, disables publish button after click to prevent double posts, refactored message correction UI and a change in the social feed pubsub access model. The latest, adds pause and resume story on delete dialog, fixes for progress bar handling and contact lookup for stories and brings fixes from [Conversations](https://conversations.im/), plus updated translations!. Don't miss it out!
- [Profanity](https://profanity-im.github.io/) has released version [0.16.0](https://github.com/profanity-im/profanity/releases/tag/0.16.0) of its console based XMPP client written in C. This release brings fixes for OTR detection, OMEMO startup, overwriting new accounts when running multiple instances, reconnect when no account has been set up yet, adds a new `/changes` command that allows the user to see the modifications of the runtime configuration vs. the saved configuration among many other fixes and improvements. Make sure to read the [changelog](https://github.com/profanity-im/profanity/blob/master/CHANGELOG) for all the details!
- [xmpp-web](https://github.com/nioc/xmpp-web/blob/master/README.md) has released version [0.11.0](https://github.com/nioc/xmpp-web/releases/tag/0.11.0) of its lightweight web chat client for XMPP server.

{{< figure src="/images/newsletter/2026-03-05/xmpp-web-main.png" caption="XMPP-Web main window" >}}

### XMPP Servers

- [ProcessOne](https://www.process-one.net/) is pleased to announce the bugfix release of [ejabberd 26.02](https://www.process-one.net/blog/ejabberd-26-02/). Make sure to read the [changelog](https://www.process-one.net/blog/ejabberd-26-02/#changelog) for all the details and a complete list of fixes and improvements on this release.

### XMPP Libraries & Tools

- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md?ref_type=heads), a Python library that provides a way for Python applications to use the XMPP network, version [7.1.0](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/7.1.0) has been released. Full details on the [changelog](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md?ref_type=heads), the cross-platform C++ XMPP client and server library, versions [1.13.1](https://invent.kde.org/libraries/qxmpp/-/tags/v1.13.1), [1.14.1](https://invent.kde.org/libraries/qxmpp/-/tags/v1.14.1), [1.14.2](https://invent.kde.org/libraries/qxmpp/-/tags/v1.14.2) and [1.14.3](https://invent.kde.org/libraries/qxmpp/-/tags/v1.14.3) have been released. Full details on the [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- [Siltamesh](https://codeberg.org/tpikonen/siltamesh), a simple bridge between [Meshtastic](https://meshtastic.org/) and XMPP networks, version [0.2.0](https://codeberg.org/tpikonen/siltamesh/src/tag/0.2.0) has been released.
- [Slidge](https://slidge.im/) versions [0.3.7](https://codeberg.org/slidge/slidge/releases/tag/v0.3.7) has been released. You can check the intermediate changelog from [0.3.6 to 0.3.7](https://codeberg.org/slidge/slidge/compare/v0.3.6...v0.3.7) for all the details.
- [Slixmpp](https://codeberg.org/poezio/slixmpp/src/branch/master/README.rst), the MIT licensed XMPP library for Python 3.7+ versions [1.13.0](https://codeberg.org/poezio/slixmpp/releases/tag/slix-1.13.0) and [1.13.2](https://codeberg.org/poezio/slixmpp/releases/tag/slix-1.13.2) have been released. You can read their respective official release announcements [here](https://blog.mathieui.net/slixmpp-1-13.html) and [here](https://blog.mathieui.net/slixmpp-1-13-2.html) for all the details.
- [xmpppy](https://github.com/xmpppy/xmpppy/blob/0.7.2/README.rst), a Python library that is targeted to provide easy scripting with Jabber, version [0.7.3](https://github.com/xmpppy/xmpppy/releases/tag/0.7.3) has been released. Full details on the [changelog](https://github.com/xmpppy/xmpppy/blob/0.7.3/CHANGES.rst).

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- [Link Metadata](/extensions/inbox/link-metadata.html)
  - This specification describes how to attach metadata for links to a message.

### New

- Version 0.1.0 of [XEP-0510](/extensions/xep-0510.html) (End-to-End Encrypted Contacts Metadata)
  - Accepted as Experimental by council vote (dg)
- Version 0.1.0 of [XEP-0511](/extensions/xep-0511.html) (Link Metadata)
  - Accepted as Experimental by council vote (dg)

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.26.0 of [XEP-0001](/extensions/xep-0001.html) (XMPP Extension Protocols)
  - Surface (and correct) the source control information.
  - Surface the publication URL (although I assume anyone reading this has figured that one out by now).
  - Surface the contributor side of things.
  - Add bit about XEP authors making PRs if they don't exist - this is "new" rather than documenting existing practice.
  - Add bit about PRs getting XEP author approval (existing practice hithertofore undocumented).
  - Add bit about Council (etc) adding authors if they drop off (existing practice hithertofore undocumented).
  - Add note to clarify that Retraction doesn't mean Deletion (existing practice, documented, but has been misunderstood before). (dwd)
- Version 1.1.0 of [XEP-0143](/extensions/xep-0143.html) (Guidelines for Authors of XMPP Extension Protocols) 
  - Reflect preference for GitHub pull requests for initial submission, 
  - PRs to contain only one changed XEP. (dwd)
- Version 0.8.0 of [XEP-0353](/extensions/xep-0353.html) (Jingle Message Initiation)
  - Adapt usage of JID types to real-world usage:
    - Send JMI responses to full JID of initiator instead of bare JID
    - Send JMI `<finish/>` element to full JID of both parties (melvo)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No XEPs last calls this month.

### Stable

- No stable XEPs this month.

### Deprecated

- No XEPs deprecated this month.

### Rejected

- No XEPs rejected this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp-official.bsky.social)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers and more languages are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- Contributors:
  - To [this issue](/categories/newsletter/): *emus, cal0pteryx, Gonzalo Raúl Nemmi, Ludovic Bocquet, sokai, XSF iTeam*

- Translations:
  - [French](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
  - [German](/categories/newsletter/): *Millesimus*
  - [Italian](/categories/newsletter/): *Mario Sabatino, Roberto Resoli*
  - [Portuguese](/categories/newsletter/): *Paulo*
  
## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). At the end of each month, the pad's content is merged into the [XSF GitHub repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations
- communication via media accounts

## Unsubscribe from the XMPP Newsletter

For this newsletter either [log in here](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/) and unsubscribe or simply send an email to newsletter-leave@xmpp.org.
(If you have not previously logged in, you may need to set up an account with the appropriate email address.)

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
