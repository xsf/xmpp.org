---
title: The XMPP Newsletter September 2025
date: 2025-10-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Welcome to the XMPP Newsletter, great to have you here again!
This issue covers the month of September 2025.

The [XMPP Newsletter](/categories/newsletter/) is brought to you by the [XSF Communication Team](/about/xsf/comm-team/).

Just like any other product or project by the XSF, the Newsletter is the result of the voluntary work of its members and contributors. If you are happy with the services and software you may be using, please consider saying thanks or help these projects!

Interested in contributing to the [XSF Communication Team](/about/xsf/comm-team/)? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

### XSF Membership

If you are interested in joining the XMPP Standards Foundation as a member, [please apply before November 23th, 2025, 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q4_2025).

### XSF Board and Council Elections 2025

The [XMPP Standards Foundation](/about/xmpp-standards-foundation/) is calling for individuals to compose the [Board of Directors](/about/xmpp-standards-foundation/#board) and members to serve on the [XMPP Council](/about/xmpp-standards-foundation/#council) for the 2025/2026 period. If you are interested in running for the Board of Directors or the XMPP Council, please add a [wiki page](https://wiki.xmpp.org/web/Main_Page) about your candidacy to one or both of the aforementioned sections [before November 2nd, 2025, 00:00 UTC](https://wiki.xmpp.org/web/Board_and_Council_Elections_2025).

Get involved in the XMPP Standards Foundation organization decisions and with the specifications we publish!

**Note**: XMPP Council members must be [elected members](/about/xsf/members/) of the XSF; however, there is no such restriction for the Board of Directors.

## Videos and Talks
- [XMPP Tutorials DE](https://makertube.net/c/xmpp_tutorials_de/videos) by [eversten.net](https://makertube.net/a/eversten.net/video-channels). 
  - [Conversations (XMPP) - Verbindungsproblem nach Update beheben](https://makertube.net/w/8yXjHWpVd77tz5vRySpJeH). [DE]
  - [Quicksy - Der einfachste Einstieg in XMPP (iOS-Version)](https://makertube.net/w/7osSvECKBQvFPTYkjP9kz5). [DE]
- [UnifiedPush](https://gultsch.video/w/85UeGATR1i13E7j6eKzq2r): a [lecture](https://talks.datenspuren.de/ds25/talk/3783DB/) by [Daniel Gultsch](https://gultsch.de/) at the [Datenspuren 2025](https://www.datenspuren.de/2025/). [DE]

## XMPP Articles

- [ProcessOne ](https://www.process-one.net/)
  - [Why Europe's 'Chat Control' Proposal Will Cripple European Communication Industry While Failing to Protect Children](https://www.process-one.net/blog/chat-control-2025/) by [Mickaël Rémond ](https://www.process-one.net/author/mremond/) for the [ProcessOne Blog](https://www.process-one.net/blog/).
- [XMPP Interop Testing](https://xmpp-interop-testing.github.io/)
  - [Lots More Options!](https://xmpp-interop-testing.github.io/2025/09/14/lots-more-options.html): A slew of new CI systems have been added. This time the target was freedom-respecting, open source CI systems for your open source projects ( including [Jenkins](https://www.jenkins.io/), [Drone](https://www.drone.io/), [Harness](https://www.harness.io/) and [Woodpecker](https://woodpecker-ci.org/) ). This brings the total number of CI systems in which you can run XMPP interop tests up to a whopping ELEVEN, plus anywhere else you can run containers. If there’s a CI system that you’re using and you’d like to see supported, or if it's already supported but you’re struggling, [please join their MUC](xmpp:interop@conference.igniterealtime.org?join), or [open an issue on GitHub](https://github.com/XMPP-Interop-Testing/smack-sint-server-extensions). By [Dan Caseley](https://xmpp-interop-testing.github.io/contact) for the [XMPP Interop Testing Blog](https://xmpp-interop-testing.github.io/blog).
  - [Two New Features for Clearer Testing](https://xmpp-interop-testing.github.io/2025/09/26/new-features-for-clearer-testing.html): Has released version 1.7.1 of all of its test runners. This release adds two improvements to make interop testing both stricter and easier to set up! Now you can configure the suite to treat impossible tests as failures, ensuring that a green run really means every configured test executed and passed. You can now choose from three provisioning methods:
    - Admin Account using [XEP-0133](/extensions/xep-0133.html) (Service Administration) to create test accounts.
    - Explicit Test Accounts you configure up front.
    - In-Band Registration via [XEP-0077](/extensions/xep-0077.html) (In-Band Registration).
    Pick the approach that fits your setup best. There is [documentation](https://xmpp-interop-testing.github.io/documentation/provisioning-accounts) available for you to review the finer details!
- [Libervia CLI tips](https://mastodon.social/@Goffi/tagged/tips): Did you know that [Liverbia](https://libervia.org/) has a [CLI](https://libervia.org/__b/doc/backend/libervia-cli/) that you can use to do nearly everything with? Well, that's right, and [Goffi](https://mastodon.social/@Goffi), its author, has been steadily publishing a series of Mastodon toots to help you make the most out of it! Share files, publish blog posts, send encrypted messages, make audio/video calls, encrypt a pubsub node, automate tasks with ad-hoc commands, etc; everything from the comfort of your terminal!
- [FastCGI Authorizer](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/#fastcgi-authorizer-implementing-xep_0070-xmpp-confirmation) implementing [XEP-0070](/extensions/xep-0070.html) (Verifying HTTP Requests via XMPP) XMPP confirmation by [PulkoMandy](https://mastodon.tetaneutral.net/@pulkomandy) for [pulkomandy.tk Git repositories](https://pulkomandy.tk/gerrit/plugins/gitiles/?format=HTML). [[FR](https://linuxfr.org/users/pulkomandy/journaux/authentifiez-vous-sans-mot-de-passe-grace-a-xmpp-10-ans-plus-tard)]
- [Montando un WhatsApp gateway desde XMPP con Slidge](https://portal.mozz.us/gemini/z3r0.maverick-hq.org/gemlog/montando-un-whatsapp-gateway-desde-xmpp-con-slidge.gmi) by [z3r0](https://gts.maverick-hq.org/@z3r0) via [SMOLNET PORTAL](https://portal.mozz.us/about). [ES]
- [Modern messaging: Running your own XMPP server](https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server/) by [Holger](https://hachyderm.io/@theaitch) for [codedge](https://www.codedge.de/).
- [Install Slidgram in NetBSD](https://eugene-andrienko.com/it/2025/09/20/slidgram-netbsd-install-howto.html) by [Eugene](https://eugene-andrienko.com/about.html) for [Dragon's notes](https://eugene-andrienko.com/).
- XMPP Brasil [celebrates its first anniversary](https://mastodon.social/@xmppbrasil/115232713992094928) providing free accounts for the Brasilian community and its new status as a [Category Provider A](https://providers.xmpp.net/provider/xmpp.eco.br/) by [XMPP Providers](https://providers.xmpp.net/). [PT]

## XMPP Software News

### XMPP Clients and Applications

- [Cheogram](https://cheogram.com/) has released version [2.19.0-2](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.19.0-2) for Android. A bugfix release that addresses issues with registration and discovery (fixes options to block) on [Snikket](https://snikket.org/) instances, fix more insets on latest Android, and scrolling 'Manage Accounts' with many accounts, among other things. Make sure to check out the [changelog](https://git.sr.ht/~singpolyma/cheogram-android/tree/master/item/CHANGELOG.md) for all the details.
- [Conversations](https://conversations.im/) has released version [2.19.5](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.5) for Android, with **improved error message for servers that do not support TLS 1.3** and fixed issues with device rotation among many other [fixes and improvements](https://codeberg.org/iNPUTmice/Conversations/compare/2.19.4...2.19.5). You can take a look at the [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) for all the details.
- [Convo](https://git.disroot.org/badrihippo/convo) XMPP client for [KaiOS](https://www.kaiostech.com/) has released version [0.2.0](https://git.disroot.org/badrihippo/convo/releases/tag/0.2.0) codenamed "Eyes Only" with support for OMEMO powered end-to-end encryption! This is the first time XMPP with OMEMO is available on a button phone. You can find all the announcements [on the release page](https://git.disroot.org/badrihippo/convo/releases/).

{{< figure src="/images/newsletter/2025-10-05/convo.png" caption="Convo 0.2.0: Support for end-to-end encryption with OMEMO." >}}

- [Gajim](https://gajim.org/) has released versions [2.3.5](https://gajim.org/posts/2025-09-11-gajim-2.3.5-released/) and [2.3.6](https://gajim.org/posts/2025-09-30-gajim-2.3.6-released/) of its free and fully featured chat app for XMPP. This release brings reorganized account settings, a brand new shortcuts manager, more contact info, video previews, performance improvements, and many bugfixes. The latest update fixes some issues with video previews and preview generation as well as some issues around loading icons. You can take a look at the [changelog](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) for all the details. Thank you for all your contributions!

{{< figure src="/images/newsletter/2025-10-05/main-window.png" caption="Gajim 2.3.5 bundles preferences and account settings!" >}}

- [Kaidan](https://www.kaidan.im/) has released version [0.13.0](https://www.kaidan.im/2025/09/21/kaidan-0.13.0/) of its user-friendly and modern chat app for XMPP. This new release brings support for using multiple accounts simultaneously, enable/disable accounts, message forwarding, apply consistent criteria for all message correction, secure passwords storage, try all providers on connection error during automatic registration and many other new features and bugfixes! You can find a detailed list of new features, bugfixes and notes in the [changelog](https://invent.kde.org/network/kaidan/-/blob/Kaidan/0.13/NEWS.md?ref_type=heads).

{{< figure src="/images/newsletter/2025-10-05/kaidan.png" caption="Kaidan 0.13.0: Multi-Account support with enable/disable toggle switch." >}}

- [Monocles](https://monocles.eu/) has released versions [2.0.14](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.14) and [2.0.15](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.15) of its chat client for Android. This updates bring in the ability to pin images and files to the top of the chat window, support for geo URI in pinned messages and reply previews, enable video preview for pinned messages and show audio file icon for pinned audio messages among other 'pinning related' improvements. They also allow replies to yourself, sending replies with OMEMO and jump to message on tap on reply with new scroll to reply, among many other features and a lot of fixes. Make sure to take a look at the [changelog](https://codeberg.org/monocles/monocles_chat/src/branch/master/fastlane/metadata/android/en-US/changelogs/19101.txt) for all the details!
- [Psi+](https://sourceforge.net/projects/psiplus/) has released version [1.5.2117 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) of its development branch of the [Psi](https://sourceforge.net/projects/psi/), the cross-platform XMPP client designed for experienced users.
- [Renga](http://pulkomandy.tk/projects/renga) XMPP client for [Haiku](https://www.haiku-os.org/) has released version 1.28, with some improvements to MUC support, and an implementation of [XEP-0070](/extensions/xep-0070.html) (Verifying HTTP Requests via XMPP) for HTTP authentication using XMPP. You can read all the details about this release on the [latest news](https://pulkomandy.tk/projects/renga#Latestnews) about it.
- [xmpp-web](https://github.com/nioc/xmpp-web/blob/master/README.md) has released version [0.10.7](https://github.com/nioc/xmpp-web/releases/tag/0.10.7) of its lightweight web chat client for XMPP server.
- [XOWS](https://github.com/iquercorb/xows/blob/main/README.md) has released version [0.9.9c](https://github.com/iquercorb/xows/releases/tag/0.9.9c) of its XMPP Over WebSocket web client, with refactored avatar fetch routines, some browser DOM refresh optimizations, fixes to account registration process crash and MUC occupant that may be duplicated.

### XMPP Servers

- The [Ignite Realtime community](https://www.igniterealtime.org/) is happy to announce the release of [Openfire 5.0.2](https://discourse.igniterealtime.org/t/openfire-5-0-2-release/95982)! This release addresses a recently identified security vulnerability ([CVE-2025-59154](https://github.com/igniterealtime/Openfire/security/advisories/GHSA-w252-645g-87mp)). The issue allowed for potential identity spoofing via unsafe Common Name attribute parsing. Please read the full [security advisory](https://github.com/igniterealtime/Openfire/security/advisories/GHSA-w252-645g-87mp) for more information. This release also improves the SystemD-based scripts, removing a few annoyances introduced in Openfire 5.0.1. Please refer to the [full changelog](https://download.igniterealtime.org/openfire/docs/latest/changelog.html) for more details.

### XMPP Libraries & Tools

- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md?ref_type=heads) version [6.3.1](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/6.3.1) has been released. Full details on the [changelog](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md?ref_type=heads) version [1.11.2](https://invent.kde.org/libraries/qxmpp/-/tags/v1.11.2) has been released. Full the details on the [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- [Slidge](https://slidge.im/) versions [0.3.0](https://codeberg.org/slidge/slidge/releases/tag/v0.3.0) and [0.3.1](https://codeberg.org/slidge/slidge/releases/tag/v0.3.1) have been released. **Migration from the 0.2 series is not supported, the slidge home dir has to be deleted and users have to register again**. New features and improvements were introduced, mainly: support for (optional) reaction fallbacks (for older XMPP clients not supporting reactions), a lot of gateway-wide settings have been moved to user-specific settings, check the "preferences" command (adhoc or chatbot-style) and support for pronouns in VCards. You can check the intermediate changelogs from [0.2.12 to 0.3.0](https://codeberg.org/slidge/slidge/compare/v0.2.12...v0.3.0) for the full list of changes.
  - [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp#readme), the [WhatsApp](https://www.whatsapp.com/) to XMPP gateway based on Slidge and [whatsmeow](https://github.com/tulir/whatsmeow), versions [0.3.0beta](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.0beta) and [0.3.0](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.0) have been released.
  - [sleamdge](https://codeberg.org/slidge/sleamdge#readme), the [Steam](https://steamcommunity.com/) to XMPP gateway based on Slidge and [steamio](https://steam-py.github.io/docs/latest/), version [0.3.0](https://codeberg.org/slidge/sleamdge/releases/tag/v0.3.0) has been released.
  - [matteridge](https://codeberg.org/slidge/matteridge#readme), the [Mattermost](https://mattermost.com/) to XMPP gateway based on Slidge and [mattermost-api-reference-client](https://git.sr.ht/~nicoco/mattermost-api-reference-client), version [0.3.0](https://codeberg.org/slidge/matteridge/releases/tag/v0.3.0) has been released.
  - [slidcord](https://codeberg.org/slidge/slidcord#readme), the [Discord](https://discord.com/) to XMPP gateway based on Slidge and [discord.py-self](https://discordpy-self.readthedocs.io/en/latest/), version [0.3.0](https://codeberg.org/slidge/slidcord/releases/tag/v0.3.0), has been released.
  - [matridge](https://codeberg.org/slidge/matridge#readme), the [Matrix](https://matrix.org/) to XMPP gateway based on Slidge and [nio](https://matrix-nio.readthedocs.io/en/latest/), versions [0.3.0](https://codeberg.org/slidge/matridge/releases/tag/v0.3.0) and [0.3.1](https://codeberg.org/slidge/matridge/releases/tag/v0.3.1) have been released.
  - [slidgram](https://codeberg.org/slidge/slidgram#readme), the [Telegram](https://telegram.org/) to XMPP gateway based on Slidge and [Pyrofork](https://pyrofork.wulan17.dev/main/), version [0.3.0](https://codeberg.org/slidge/slidgram/releases/tag/v0.3.0), has been released.
- [Slixmpp](https://codeberg.org/poezio/slixmpp) version [1.11.0](https://codeberg.org/poezio/slixmpp/releases/tag/slix-1.11.0) has been released. You can read the official [release announcement](https://blog.mathieui.net/en/slixmpp-1.11.html) for all the details.
- [xmpp-dns](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/README.md?ref_type=heads) versions [0.5.2](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.5.2) and [0.5.3](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.5.3) have been released. Full details on the [changelog](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/CHANGELOG.md?ref_type=heads).
- [xmpp-fastcgi-authorizer](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer), a FastCGI Authorizer implementing [XEP-0070](/extensions/xep-0070.html) (Verifying HTTP Requests via XMPP) to allow logging in to websites using an XMPP account, versions [0.1](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/+/refs/tags/v0.1) and [0.2](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/+/refs/tags/v0.2) have been released.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](/extensions/) in addition to [XMPP RFCs](/rfcs/). Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([online archive](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the [XMPP Editor](/about/xsf/editor-team/). Within two weeks, the [Council](/about/xmpp-standards-foundation/#council) decides whether to accept this proposal as an Experimental XEP.

- [Pubsub Node Bookmark](/extensions/inbox/pubsub-node-bookmark.html)
  - This specification defines a bookmark element pointing to a Pubsub node.

### New

- No New XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- Version 0.3.1 of [XEP-0317](/extensions/xep-0317.html) (Hats)
  - Typos, completed some examples and paragraph clarifications thanks to badlop feedback. (tj)
- Version 0.2.0 of [XEP-0503](/extensions/xep-0503.html) (Server-side spaces)
  - Rewrite using pubsub semantics. (nc)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the [Council](/about/xmpp-standards-foundation/#council) decides whether the XEP seems ready, the [XMPP Editor](/about/xsf/editor-team/) issues a Last Call for comments. The feedback gathered during the Last Call can help improve the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- No XEPs moved to Stable this month.

### Deprecated

- No XEPs deprecated this month.

### Rejected

- No XEPs rejected this month.

## XMPP Public channels

New rooms and public channels are created on a daily basis on the XMPP network. So, if you are on the look out for new and exciting public channels to join, make sure to check out the [Public Channel Search Engine](https://search.jabber.network/search) to find out groups or communities that share your interests!

- If you want to list all the channels, you can find them [here](https://search.jabber.network).
- If you are interested on something in particular, [look by tag](https://search.jabber.network/tags/)!
- If you only want to list rooms in a particular language just add `lang:xx` in the search box, like in this example for the [Spanish language](https://search.jabber.network/search?q=lang%3Aes&f=y&sinaddr=on&sindescr=on&sinname=on). Just make sure to replace `es` for your desired language (like `lang:fr`, `lang:de`, `lang:pt` and so on).

## Spread the news

Please share the news on other networks:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp.org)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)
- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)
- [XMPP Facebook page (unofficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations section:

This is a community effort, and we would like to thank translators for their contributions.
Volunteers and more languages are welcome!
Translations of the XMPP Newsletter will be released here (with some delay):

Newsletter Contributors this month:
*emus, Badri Sunderarajan, cal0pteryx, Gonzalo Raúl Nemmi, Kris "poVoq", Ludovic Bocquet, XSF iTeam*

Translation Contributors:
- [French](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), anubis, Benoît Sibaud, Julien Jorge seveso, Pierre Jarillon*
- [German](/categories/newsletter/): *Millesimus*
- [Italian](https://notes.nicfab.eu): *nicola*
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

## XSF Fiscal Hosting Projects

The XSF offers [fiscal hosting](/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](/2021/09/the-xsf-as-a-fiscal-host/). Current projects you can support:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav](https://opencollective.com/pravapp)
- [diasp.in](https://opencollective.com/diasp-in)

## Unsubscribe from the XMPP Newsletter

To unsubscribe from this list, [please log in first](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/).
If you have not previously logged in, you may need to set up an account with the appropriate email address.

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
