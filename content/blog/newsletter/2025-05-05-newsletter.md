---
title: The XMPP Newsletter April 2025
date: 2025-05-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of April 2025.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XSF Membership
If you are interested in joining the XMPP Standards Foundation as a member, [submissions are open until May 18th, 2025, 00:00 UTC!](https://wiki.xmpp.org/web/Membership_Applications_Q2_2025).

### XSF Fiscal Hosting Projects

The XSF offers [fiscal hosting](/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](/2021/09/the-xsf-as-a-fiscal-host/). Current projects you can support:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav](https://opencollective.com/pravapp)
- [diasp.in](https://opencollective.com/diasp-in)

## XMPP Events

- [Berlin XMPP Meetup](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) [DE / EN]: monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month at 6pm local time.
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) [IT]: monthly Italian XMPP web meeting, every third Monday of the month at 7:00 PM local time (online event, with web meeting mode and live streaming).
- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2025-05_Berlin): On Friday, 23rd, Saturday, 24th, and Sunday, 25th of May 2025.

## XMPP Articles

- [XMPP Foundation Urges Meta to Allow Interoperability Under EU Rules](https://winbuzzer.com/2025/04/02/xmpp-pressures-meta-to-allow-interoperability-under-eu-rules-xcxwbn/) by [Markus Kasanmascheff](https://winbuzzer.com/author/markus/) for [winbuzzer.com](https://winbuzzer.com/)
- [Monocles](https://monocles.eu/more/), the project responsible for the XMPP Monocles chat [Web](https://monocles.chat/login) and [Android](https://f-droid.org/en/packages/de.monocles.chat/) clients, has started a [crowdfunding campaign](https://www.startnext.com/en/monocles). The main goal is to create a platform where privacy, digital sovereignty and sustainability take center stage. Your privacy is non-negotiable. The funding period will span from 03.28.2025 to 06.30.2025.
- [Prav](https://prav.app) has taken its second major step towards forming a cooperative society in India. Their blog post ["Finalising our bye-laws"](https://prav.app/blog/finalising-our-bye-laws/) details the process, including ways you can help out. This is an important step in Prav's mission to implement community-driven decision making for their XMPP apps and services *and* [give legal teeth to that structure](https://prav.app/blog/why-register-a-coop/).

## XMPP Software News

### XMPP Clients and Applications

- [Cheogram](https://cheogram.com/) has released version [2.17.10-1](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.17.10-1) for Android. This version introduces an initial implementation of Spaces ([XEP-503](https://xmpp.org/extensions/xep-0503.html)), among other improvements, bugfixes and more!
- [Conversations](https://conversations.im/) has released versions [2.18.0](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.18.0), [2.18.1](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.18.1) and [2.18.2](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.18.2) for Android. Notable changes include the ability to pick a custom backup location, a prominent backup restore option for [Quicksy](https://quicksy.im/), and improved support for more kinds of URIs. The latter includes `tel` phone numbers, `mailto` email addresses, and more interestingly the `web+ap` scheme for ActivityPub proposed by [Fedi Links](https://fedilinks.org/).
- [Dino](https://dino.im/) has released version [0.5](https://github.com/dino/dino/releases/tag/v0.5.0) featuring OMEMO encryption by default, improved file transfers, image preview and other file details before downloading, and two completely reworked dialogs. See the release [blog post](https://dino.im/blog/2025/04/dino-0.5-release/) for all the details.
  - At the same time, Dino has also [received funding](https://nlnet.nl/news/2025/20250422-announcement-grants-CommonsFund.html) from [NLnet](https://nlnet.nl) to begin development on a slew of new features. This includes message moderation in group chats, local message deletion, modern connection handling with FAST and SASL2, more formatting options with Message Markup, and more! [Visit the project page](https://nlnet.nl/project/Dino-UX/) for all the details.
- [Gajim](https://gajim.org/) has released versions [2.1.0](https://gajim.org/post/2025-04-08-gajim-2.1.0-released/) and [2.1.1](https://gajim.org/post/2025-04-17-gajim-2.1.1-released/) with a new 'Activity feed' page, layout improvements for its 'Start Chat' dialog and support for 'Message Display Synchronisation' ([XEP-0490](https://xmpp.org/extensions/xep-0490.html)) across group chats among other improvements and bugfixes. Head over to their [News](https://gajim.org/post/) section for all the details.

{{< figure src="/images/newsletter/2025-05-05/gajim-activity-feed.png" caption="Activity feed in Gajim 2.1" >}}

{{< figure src="/images/newsletter/2025-05-05/gajim-account-select.png" caption="Account and status selection in Gajim 2.1" >}}

- [Kaidan](https://www.kaidan.im/) has received [NLnet](https://nlnet.nl) funding for [various improvement across the board](https://nlnet.nl/project/Kaidan-MUC/), most notably multi-user chat and support for legacy OMEMO. The second point is significant because while Kaidan is using a newer version of the OMEMO end-to-end encryption protocol, other popular clients including Conversations, Monal, and Dino are still using an older version. Since the two are not compatible, this meant Kaidan users were unable to use OMEMO encryption with users of most other clients. By implementing the older spec as well, Kaidan will help bridge that gap.

- [Monocles Chat 2.0.6](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.6) has been released for Android. This version brings initial support for file captions, the option to pin an unencrypted message to the top of a conversation, providers list support, and the option to register on your own XMPP server, among many other new features and improvements.

{{< figure src="/images/newsletter/2025-05-05/monocles-pin-message.png" caption="Monocles Chat 2.0.6: Initial captions to files and pin message to the top" >}}

{{< figure src="/images/newsletter/2025-05-05/monocles-providers.png" caption="Monocles Chat 2.0.6: Register on your own XMPP server or pick one from the providers list" >}}
 
- [Movim](https://movim.eu/) has released version [0.30](https://mov.im/community/pubsub.movim.eu/Movim/good-news-everyone-movim-0-30-encke-is-there-xMvYPr) (code named "[Encke](https://en.wikipedia.org/wiki/Comet_Encke)"), the biggest Movim evolution in many years! This release brings [multi-participant calls](https://movim.eu/#visio), reactions being displayed in the detailed message view, support for Unicode 15.1 with plenty of new emojis to use, and avatars that change when a contact adds to their [Story](https://movim.eu/#stories).

{{< figure src="/images/newsletter/2025-05-05/movim-visio.jpg" caption="Movim 0.30 (Encke): Multi Participant Calls. Bob Cat looking disgruntled by the presence of the 'Hooman' on the lower right of the screen!" >}}

{{< figure src="/images/newsletter/2025-05-05/movim-visio-phone.jpg" caption="Movim 0.30 (Encke): Meow OwO bedazzled by the looks of Multi Participant Calls on his mobile device!" >}}

  - and following right on its heels, [Movim](https://movim.eu/) also published its first bug-fix release: version [0.30.1](https://mov.im/community/pubsub.movim.eu/Movim/here-comes-the-new-movim-release-encke-0-30-1-ckTLY4), adding animated pictures support in the image proxy and a new Avatar and Banner Configuration Panel, as well as implementing ([XEP-0392](https://xmpp.org/extensions/xep-0392.html)) Consistent Color Generation, among many other improvements and bugfixes. Make sure to check out the official announcements at the [Movim Blog](https://mov.im/community/pubsub.movim.eu/Movim) for all the details!

{{< figure src="/images/newsletter/2025-05-05/movim-avatar-panel.png" caption="Movim 0.30.1: Avatar and banner configuration panel" >}}

- [Prose](https://prose.org/) has released versions [0.8.0](https://github.com/prose-im/prose-app-web/releases/tag/0.8.0), [0.8.1](https://github.com/prose-im/prose-app-web/releases/tag/0.8.1), [0.8.2](https://github.com/prose-im/prose-app-web/releases/tag/0.8.2), [0.8.3](https://github.com/prose-im/prose-app-web/releases/tag/0.8.3), [0.9.0](https://github.com/prose-im/prose-app-web/releases/tag/0.9.0), [0.9.1](https://github.com/prose-im/prose-app-web/releases/tag/0.9.1) and [0.10.0](https://github.com/prose-im/prose-app-web/releases/tag/0.10.0) of its web frontend [prose-web-app](https://github.com/prose-im/prose-app-web).

### XMPP Servers

- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) has released version [6.3.3](https://github.com/esl/MongooseIM/releases/tag/6.3.3) of its Enterprise Instant Messaging Solution. This minor update includes various fixes and improvements. For more information, check out the [documentation](https://esl.github.io/MongooseDocs/6.3.3).
- [ProcessOne](https://www.process-one.net/) has published [ejabberd 25.04](https://www.process-one.net/blog/ejabberd-25-04/). This release brings an important security fix, several bug fixes and a new API command.
- [Prosody IM](https://prosody.im/) is pleased to announce version [13.0.1](https://blog.prosody.im/prosody-13.0.1-released/), a new minor release from the latest stable branch. It fixes some important bugs that were discovered after the latest release. Read all the details on the release [changelog](https://prosody.im/doc/release/13.0.1). As always, detailed download and install instructions are available on the [download page](https://prosody.im/download/) for your convenience.
- The [Prosody app for YunoHost](https://github.com/YunoHost-Apps/prosody_ynh) has been updated to provide a bunch of [supported XEPs](https://raw.githubusercontent.com/YunoHost-Apps/prosody_ynh/refs/heads/master/xmpp_compliance) by default, configured for all YunoHost users in just one click. [YunoHost](https://yunohost.org/) is a set of tools to easily manage your own selfhosted services, and while it used to come bundled with the Prosody fork Metronome by default, it has recently bundled its XMPP functionality into a separate "app" so that people can swap in any other XMPP server of their choice.

### XMPP Libraries & Tools

- [go-xmpp](https://github.com/xmppo/go-xmpp) versions [0.2.13](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.13) and [0.2.14](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.14) has been released.
- [libomemo-c](https://github.com/dino/libomemo-c) version [0.5.1](https://github.com/dino/libomemo-c/releases/tag/v0.5.1) has been released.
- [prose-core-client](https://github.com/prose-im/prose-core-client) versions [0.1.103](https://github.com/prose-im/prose-core-client/releases/tag/0.1.103), [0.1.104](https://github.com/prose-im/prose-core-client/releases/tag/0.1.104) and [0.1.105](https://github.com/prose-im/prose-core-client/releases/tag/0.1.105) have been released.
- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp) versions [6.1.0](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/6.1.0) and [6.1.1](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/6.1.1) have been released.
- [Slidge](https://codeberg.org/slidge/slidge#readme) versions [0.2.9](https://codeberg.org/slidge/slidge/releases/tag/v0.2.9) (codenamed "Trixie <3"), [0.2.10](https://codeberg.org/slidge/slidge/releases/tag/v0.2.10), [0.2.11](https://codeberg.org/slidge/slidge/releases/tag/v0.2.11) and [0.2.12](https://codeberg.org/slidge/slidge/releases/tag/v0.2.12) have been released.
- [Tinder](https://www.igniterealtime.org/projects/tinder/) version [2.1.0](https://github.com/igniterealtime/tinder/releases/tag/tinder_2_1_0) has been released.
- [Whack](https://www.igniterealtime.org/projects/whack/) version [3.0.0](https://github.com/igniterealtime/Whack/releases/tag/v3.0.0) has been released.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- No XEPs proposed this month.

### New

- No New XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 1.1.3 of [XEP-0313](https://xmpp.org/extensions/xep-0313.html) (Message Archive Management)
  - Fixed typo (XEP Editor (dg))
- Version 0.4.0 of [XEP-0377](https://xmpp.org/extensions/xep-0377.html) (Spam Reporting)
  - Add spam report processing opt-in.
  - Add Guus der Kinderen as co-author. (gdk)
- Version 1.0.1 of [XEP-0421](https://xmpp.org/extensions/xep-0421.html) (Occupant identifiers for semi-anonymous MUCs)
  - Fixed typo (XEP Editor (dg))
- Version 0.3.0 of [XEP-0455](https://xmpp.org/extensions/xep-0455.html) (Service Outage Status)
  - Remove all in-band event signaling. (mp)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- No XEPs moved to Stable this month.

### Deprecated

- No XEPs deprecated this month.

### Rejected

- No XEPs rejected this month.

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
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

- English (original): [xmpp.org](/categories/newsletter/)
  - General contributors: *Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, Badri Sunderarajan, Benson Muite, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Schimon Zachary, Simone Canaletti, singpolyma, XSF iTeam*
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: *nicola*
- Spanish: [xmpp.org](/categories/newsletter/)
  - Translators: *Gonzalo Raúl Nemmi*
- German: [xmpp.org](/categories/newsletter/)
  - Translators: *Millesimus*
- Português (BR): [xmpp.org](/categories/newsletter/)
  - Translators: *Paulo*

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
To unsubscribe from this list, [please log in first](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/).
If you have not previously logged in, you may need to set up an account with the appropriate email address.

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
