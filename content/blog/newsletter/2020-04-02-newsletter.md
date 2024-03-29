---
title: Collaboration over the Internet! - 7 May 2020
date: 2020-05-07
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/05/newsletter/"
---

## Intro

Welcome to the XMPP newsletter covering the month of April 2020.

We are always happy about contributors. Just join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and help us sustain this as a community effort. The drafting process for each newsletter [is fully documented](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).
Furthermore, we started drafting each new version in the [XSF Github repository](https://github.com/xsf/xmpp.org/pulls) - feel free to add information by yourself.

{{< newsletter-subscribe >}}

#### Newsletter translations

The translations of the XMPP Newsletter will be released here:

- [German](https://www.jabber.de/)
- [French](https://linuxfr.org/tags/xmpp/public)
- [Spanish](https://www.jabber.de/)


## XMPP Standards Foundation

The XSF is renewing its sponsorship for 2020. Many thanks to everyone supporting and sponsoring us in 2019.
We would be happy if your organization would also consider [sponsoring in 2020](https://mail.jabber.org/pipermail/standards/2020-April/037254.html).
If your organization considers sponsoring for the first time, [our mission may interest you as well](https://xmpp.org/about/xsf/mission).

Alexander Gnauck published the [Membership Applications Q2 2020](https://wiki.xmpp.org/web/Membership_Applications_Q2_2020). Applications are welcome!


## Articles

[Pasis](https://github.com/pasis), maintainer of libstrophe and contributor to profanity, wrote about using the [XML console in profanity](https://profanity-im.github.io/blog/post/xml-console-in-profanity/) for debugging.

Jan Cieśla from MongooseIM wrote a blog post about how [they drive their project by the metrics](https://www.erlang-solutions.com/blog/how-data-drives-mongooseim.html).

Can you believe it? Zoom uses XMPP for its chat - cool! [Vulnerability](https://blog.talosintelligence.com/2020/04/zoom-user-enumeration.html) - not cool.

MattJ (Prosody developer) mentioned that, according to Debian popcon statistics, the Prosody installations [have doubled since march](https://mastodon.technology/@mattj/104053716175271438).

## Software releases

[Kaidan 0.5.0](https://www.kaidan.im/2020/04/06/kaidan-0.5.0/) - Bam! Check out their new onboarding!

Let's sum it up like this: Remove OTR + Rework conference and contact details + Show PDF previews + Add title for audio files = [Pix-Art Messenger 2.3.5](https://github.com/kriztan/Pix-Art-Messenger/blob/master/CHANGELOG.md)

Four letters for Windows 10 Users: [UWPX 0.25.0](https://github.com/UWPX/UWPX-Client/releases/tag/v.0.25.0.0) is online with Windows10X support and a push server. So give it a try!

Monal continues the fight on the iOS front: included in the upcoming [beta](https://monal.im/blog/4-6-betas/) are support for geo-location messages, [TLS ALPN support](https://github.com/anurodhp/Monal/issues/206) and improvements on [OpenFire push notifications](https://github.com/anurodhp/Monal/issues/354) as well as many fixes with smack.

Wow - no late April joke - Conversations released version 2.8.0 adding [audio and video calls](https://twitter.com/iNPUTmice/status/1254662039592742913)! The German IT magazine heise.de [wrote an article about the new A/V-Feature](https://www.heise.de/newsticker/meldung/Conversations-Open-Source-Messenger-mit-Audio-und-Videoanruf-4711187.html).

### Servers

Guus der Kinderen, from the Ignite Realtime Foundation Board, wrote a short article on [how to setup a STUN and TURN service in Openfire for audio and video calls](https://discourse.igniterealtime.org/t/preparing-openfire-for-audio-video-calls-with-conversations/87828). The improvements for push notifications on iOS (see the post above for Monal) found their way into the [Push Notification Openfire plugin 0.7.0](https://discourse.igniterealtime.org/t/push-notification-openfire-plugin-0-7-0-released/87855).

### Clients and applications

The maintainer of libstrophe, [Pasis](https://github.com/pasis), and contributor to Profanity, created a tool named [xmppconsole](https://github.com/pasis/xmppconsole) which sends raw XMPP stanzas over an XMPP connection and displays the XMPP stream. Main purpose is to study XEPs and debug servers implementation.
The tool is under development. The final version will support both GTK UI and ncurses UI. In their blog, they also explained how to easier contribute commits to their repository, [read on](https://profanity-im.github.io/blog/post/contributing-a-patch-via-github/).

Dino now features [Last Message Correction](https://github.com/dino/dino/commit/871ff33ac79f3d17b0260b8bfcd27780038edd6d) for all the typos you made and the regrets you have. And also [voice handling in moderated groups](https://github.com/dino/dino/commit/2631a9bdbaf9a40f329f05c55c6e2ea38efeb10c)

Gajim [Development News April 2020](https://gajim.org/post/2020-04-28-development-news-april/): Multi-account handling improvements and polishing for the release of Gajim 1.2. One year after the last release, a beta for the upcoming version is just around the corner.

## Services

yax.im updated their servers from prosody 0.11 to [prosody-trunk](https://hg.prosody.im/trunk/file/d0e6d5bc7ea2/CHANGES). Read more about the changes [here](https://yaxim.org/blog/2020/04/23/new-prosody-on-yax-dot-im/). Unfortunately with a first [outage](https://yaxim.org/blog/2020/04/27/multi-day-message-archive-outage/) :(

On April 25th, [observe.jabber.network](https://observe.jabber.network) was launched into public beta. It offers free monitoring-as-a-service for federated XMPP domains, checking connectivity via c2s and s2s, as well as optionally in-band registration and federated XMPP pings. Application details and more information are available on the website.

[Process One released ejabberd 20.04](https://www.process-one.net/blog/ejabberd-20-04/). Highlight: Support for XEP-0215 External Service Discovery which improves support for audio and video calls. The mod_stun_disco module allows XMPP clients to discover STUN/TURN services.

## Libraries

StropheJS, a XMPP library for JavaScript, has been [released in version 1.3.5](https://github.com/strophe/strophejs/releases/tag/v1.3.5) with bugfixes and removal of support for SASL DIGEST-MD5 auth.


## Extensions and specifications


### Updated

* Version 1.18.0 of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    - Properly specifiy that an empty `<item/>` is invalid on publish. (jsc)

* Version 0.4 of [XEP-0333](https://xmpp.org/extensions/xep-0333.html) (Chat Markers)
    * Add notes about usage within MUCs. (mw)

* Version 0.4.0 of [XEP-0389](https://xmpp.org/extensions/xep-0389.html) (Extensible In-Band Registration)
    - Add OOB challenge type.
    - Add IQ query for flows.
    - Add a glossary.
    - Make challenge listings more consistent.
    - Cleanup and expand the registrar considerations section.
    - Clarifications and typo fixes throughout the text. (ssw)

### Proposed

The XMPP Extensions Editor has received proposals for new XEPs.

* [MUC presence versioning](https://xmpp.org/extensions/inbox/muc-presence-versioning.html)
    - Defines a versioning mechanism which reduces the amount of presence traffic in a XEP-0045 MUC.

* [Room Activity Indicators](https://xmpp.org/extensions/inbox/room-activity-indicators.html)
    - Describes a lightweight mechanism for activity notifications in MUCs.

* [Quick Response](https://xmpp.org/extensions/inbox/quick-response.html)
    - Quickly respond to automated messages.

* [Best practices for password hashing and storage](https://xmpp.org/extensions/inbox/password-storage.html)
    - Best practices for handling user passwords on the public Jabber network for both clients and servers.

### Miscellaneous

**Experimental**

* Version 0.1.0 of [XEP-0435](https://xmpp.org/extensions/xep-0435.html) (Reminders)
    - This specification provides a way to set up reminders.
    - Accepted by vote of Council on 2020-03-04. (XEP Editor (jsc))

**Draft**

* Version 1.0.0 of [XEP-0402](https://xmpp.org/extensions/xep-0402.html) (PEP Native Bookmarks)
    - Abstract: This specification defines a syntax and storage profile for keeping a list of chatroom bookmarks on the server.
    - Changelog: Advanced to Draft per Council vote from 2020-03-04. (XEP Editor (jsc))


## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to Aleja, emus, horazont, jcbrand, mdosch, pep., pmaziere, Sven, wurstsalat3000 for their help in creating it!

Please share the news on "social networks":

* Twitter: [https://twitter.com/xmpp](https://twitter.com/xmpp)
* Mastodon: [https://fosstodon.org/@xmpp/](https://fosstodon.org/@xmpp/)
* LinkedIn: [https://www.linkedin.com/company/xmpp-standards-foundation/](https://www.linkedin.com/company/xmpp-standards-foundation/)
* Facebook: [https://www.facebook.com/jabber/](https://www.facebook.com/jabber/)
* Reddit: [https://www.reddit.com/r/xmpp/](https://www.reddit.com/r/xmpp/)

## License

This newsletter is published under the [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/)
