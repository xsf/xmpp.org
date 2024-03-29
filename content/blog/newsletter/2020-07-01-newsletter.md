---
title: XMPP works - 1 July 2020
date: 2020-07-01
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/07/newsletter-01-july/"
---

Welcome to the XMPP newsletter covering the month of June 2020.

## Subscribe to the newsletter

We suggest you to [subscribe](https://tinyletter.com/xmpp) to receive the next editions in your inbox as soon as it is published! Promote this newsletter to whoever may be interested.

## Help us to build the newsletter

We started drafting every new issue in the [XSF Github repository](https://github.com/xsf/xmpp.org/pulls). 
We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. 

You have a project and write about it? Please consider sharing your news or events here, and promote it to a large audience! Even if you can only spend a few minutes, these would already be helpful!
Tasks which need to be done on a regular basis are for example:
- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Translations: especially German and Spanish

### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news.jabberfr.org/category/newsletter/).

## XSF Announcements

JC Brand created an [XMPP job board](https://xmpp.work/)! It enables people to review job offers as well as advertise XMPP services. Please take a look, post your own offers and recommend it. XMPP works!

## Article

Ingo Jürgensmann wrote an article on the backround of the 'Jabber' and 'XMPP' terminology and their [differences and similarities](https://blog.windfluechter.net/content/blog/2020/06/09/1758-jabber-vs-xmpp).

:de: The XMPP client Dino is one out of three projects which were awarded with the [10th Thomas Krenn Award](https://www.thomas-krenn.com/de/unternehmen/presse/pressemeldung.thomas-krenn-award-2020.html).

Michał Piotrowski wrote an article on [how to quick start Instant Messaging implementation to an app](https://www.erlang-solutions.com/blog/add-value-to-your-app-with-instant-messaging-here-s-where-to-start.html). He discusses the value of a chat feature in an app, scalability, customising and common mistakes: 'Choose your XEP, and choose wisely.'

:fr: Linuxfr.org user Space_e_man proposed his short overview of [Quicksy the easy XMPP based libre instant messaging platform](https://linuxfr.org/users/space_e_man/journaux/quicksy-la-messagerie-instantanee-libre-basee-sur-xmpp-facile). While the article itself concentrates on the reasons why it should be prefered to other proprietary solutions, the comments of linuxfr.org users, as usual, bring a lot of various points of view, as well as alternatives.

## Video

:es: Conociendo XMPP - The 'Comunidad Latina de Tecnologías Libres' had an online introduction to XMPP for users back in April 2020. We would like to [point you to the video](https://www.youtube.com/watch?v=VwnzJ9V732E), even if it is a bit late. They also offer a user chat reachable under this (short and handy) address
[comunidadlatinadetecnologiaslibres@chat.disroot.org](xmpp:comunidadlatinadetecnologiaslibres@chat.disroot.org?join).

Daniel Gultsch and Holger Weiss had a [virtual talk on their A/V implementation](https://www.youtube.com/watch?v=v_riuu4XU6Q) in Conversation and they described the technical details. The session was finalized with a second talk by eta who defined love by this formula: Asterisk + XMPP = <3

:de: Prof. Dr. P. Löbbecke spoke in a virtual talk about "[Freie Messenger - Sichere Kommunikation](https://libre.video/videos/watch/1b646209-24e0-489b-8060-793f4513da9d)" ('Free Messengers - Secure Communication') which also included XMPP (German).

## Software news

### Clients and applications

[Gajim 1.2.0](https://gajim.org/post/2020-06-21-gajim-1.2.0-released/) has been released. More than a year after the release of Gajim 1.1.3, it is finally time for Gajim 1.2. A year put at use to develop new features, clean up old code, and fix bugs. Highlights of this release are (amongst others): improved group chat system, completely rewritten network code, and a new account creation assistant. And there is much more to discover.
[Gajim Development News](https://gajim.org/post/2020-06-28-development-news-june/): June already brought Gajim 1.2, python-nbxmpp 1.0, and many plugin updates. But there is more: Blind Trust Before Verification for OMEMO, drag and drop improvements, and a new translation service for Gajim.

Anu, the main developer of Monal, pushed [new beta builds out for iOS and Mac](https://monal.im/blog/new-builds-fro-4-7/) - thanks to Thilo's and Friedrich's efforts, there are new debug features included. He asks to supply debug logs for existing issues, where possible.

Profanity released its version 0.9.0 which supports Last Message Correction (XEP-0308) and fixes various issues that can be found in their [blog post](https://profanity-im.github.io/blog/post/release-090/). After the new major release, bugfix releases [0.9.1](https://github.com/profanity-im/profanity/releases/tag/0.9.1), [0.9.2](https://github.com/profanity-im/profanity/releases/tag/0.9.2), [0.9.3](https://github.com/profanity-im/profanity/releases/tag/0.9.3) and [0.9.4](https://github.com/profanity-im/profanity/releases/tag/0.9.4) followed.

![profanity 0.9 screenshots](/images/newsletter/june2020/profanity090.png "profanity 0.9") 

[JSXC](https://jsxc.org) released [version 4.1.1](https://github.com/jsxc/jsxc/releases/tag/v4.1.1) which fixes several video related issues and enhances interoperability with Conversations. Additionally, a [first experimental desktop build](https://www.jsxc.org/blog/2020/06/25/JSXC-Desktop.html) for all platforms was released. The project is looking for early testers and people with experience in Electron and the Travis build chain.

![Desktop client JSXC](/images/newsletter/june2020/jsxc41.png "Desktop client JSXC")

Pix-Art Messenger removed their [OTR support by the 30th of June](https://social.tchncs.de/@pixart/104349576991457471). The general note on this can be [read on Github](https://github.com/kriztan/Pix-Art-Messenger/blob/master/docs/encryption.md).

And last but not least - can you believe this? [Pidgin 2.14.0](https://pidgin.im/posts/2020-06-2.14.0-released/) 😯 There is also a live development [Twitch stream](https://twitter.com/rw_grim/status/1278857182629498880) every Thursday.

### Servers

The ignite realtime community released [Openfire Beta 4.6.0](https://discourse.igniterealtime.org/t/openfire-4-6-0-beta-is-released/88203), implementing  XEP-0289, Federated MUC for Constrained Environments and improved PEP/PubSub support. If you have time to test please join them to help out!

## Libraries

Gajim’s XMPP library '[python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/tree/master)' had its 1.0 release. Being a friendly fork of the xmppy library back in the days, many things changed since then. A lot of work went into it, especially during the past year. If you’re interested, there is a simple example client included.

## Other

Did you actually know? [League of Legends uses XMPP in their backend](https://technology.riotgames.com/news/chat-service-architecture-protocol).

## Google Summer of Code

Since the beginning of May students all over the world are working on many open-source projects within the Google Summer of Code Season 2020. We would like to introduce the students who work on [GSoC XMPP projects](https://summerofcode.withgoogle.com/organizations/5474262808264704/#6018598289539072) and share their blog posts:

[Aditya Borikar](https://adiaholic.github.io/gsoc2020/2020/05/16/Chapter-0-Introduction.html) is working on WebSocket support for Smack. Blog history: 
- [Chapter 1: Handshake](https://adiaholic.github.io/gsoc2020/2020/05/24/Chapter-1-Handshake.html)
- [Chapter 2: Modular Shift](https://adiaholic.github.io/gsoc2020/2020/05/31/Chapter-2-Modular-Shift.html)
- [Chapter 3: SASL Negotiations](https://adiaholic.github.io/gsoc2020/2020/06/07/Chapter-3-sasl-negotiations.html)
- [Chapter 4: Fixing loose endpoints](https://adiaholic.github.io/gsoc2020/2020/06/14/Chapter-4-fix-loose-endpoints.html)
- [Chapter 5: Discrete Http Lookup Method](https://adiaholic.github.io/gsoc2020/2020/06/21/Chapter-5-Discrete-Http-Lookup-Method.html)
- [Chapter 6: A Part Of The Whole, Merged](https://adiaholic.github.io/gsoc2020/2020/06/28/Chapter-6-Part-Of-The-Whole.html)

[Anmol (wolfie_anmol)](https://wolfieanmol.github.io/gsoc-blog/) is working on implementing Real Time Texting in Dino ([XEP-0301](https://xmpp.org/extensions/xep-0301.html)). Blog history:
- [GSoC 2020 begins - Introduction to RTT](https://wolfieanmol.github.io/gsoc-blog/introduction/)
- [RTT stanza and message comparision](https://wolfieanmol.github.io/gsoc-blog/rtt-stanza-and-message-comparision/)
- [Receiving Real Time Texts](https://wolfieanmol.github.io/gsoc-blog/receiving-rtt/)
- [User Interface](https://wolfieanmol.github.io/gsoc-blog/ui/)

![RTT User Interface](/images/newsletter/june2020/dino_rtt_demo.gif "RTT User Interface")

Thank you for joining GSoC XMPP projects and keep up the good work! To be continued.


## Extensions and specifications

### Updated

- Version 0.5.0 of [XEP-0373](https://xmpp.org/extensions/xep-0373.html) (OpenPGP for XMPP)
  - Use RFC 4880 terminology: it is "primary key", not "master key".
  - Clarify encryption of secret key material.
  - Move the information from the 'date' attribute into the item ID. (fs)

- Version 1.3.0 of [XEP-0156](https://xmpp.org/extensions/xep-0156.html) (Discovering Alternative XMPP Connection Methods)
  - Fix reference to RFC 6415 and organize requirements more clearly. This raises the JSON requirement from MAY (OPTIONAL) to SHOULD (effectively), to accustom web-based software. (fs)

- Version 1.1.0 of [XEP-0157](https://xmpp.org/extensions/xep-0157.html) (Contact Addresses for XMPP Services)
  - Add 'status-addresses' value in registrar, with example. (mb, fs)

- Version 0.1.0 of [XEP-0440](https://xmpp.org/extensions/xep-0440.html) (SASL Channel-Binding Type Capability)
  - Accepted by vote of Council on 2020-05-27. (XEP Editor (jsc))

- Version 0.3.1 of [XEP-0390](https://xmpp.org/extensions/xep-0390.html) (Entity Capabilities 2.0)
  - Add another xml:lang example (fs)

- Version 0.6.0 of [XEP-0384](https://xmpp.org/extensions/xep-0384.html) (OMEMO Encryption)
  - Incorporate feedback around cryptographic terms and content by Sofía Celi. (ps)

- Version 0.3.0 of [XEP-0424](https://xmpp.org/extensions/xep-0424.html) (Message Retraction)
  - Clarify when a service must advertise support via disco.
  - Add another service discovery URN for tombstones. (jcb)

- Version 0.4.0 of [XEP-0393](https://xmpp.org/extensions/xep-0393.html) (Message Styling)
  - Remove description of mechanism for disabling styling on individual spans and blocks, users can do this themselves without us documenting the use of a codepoint that's not specifically for this purpose. (ssw)

- Version 0.3.0 of [XEP-0393](https://xmpp.org/extensions/xep-0393.html) (Message Styling)
  - Add ability to disable styling, further clarify accessibility considerations, and mention that Styling is not Markdown in the security considerations section. (ssw)


## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to emus, mdosch, nyco, pep., pmaziere, sualko, vanitasvitae, wurstsalat3000 for their help in creating it!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
