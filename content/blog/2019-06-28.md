---
title: The XMPP Newsletter, 28 June 2019
date: 2019-06-28
author: jcbrand
categories: ["Newsletter"]
aliases:
    - "/2019/06/newsletter-28-june/"
---

Welcome to a bumper edition of the the XMPP newsletter, containing news from the last two months.

If you have an article, tutorial or blog post you'd like us to include in the
newsletter, please [submit it on the XMPP wiki](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## News

Mickaël Rémond from ProcessOne has written about how the [Nintendo Switch uses ejabberd for push notifications](https://blog.process-one.net/ejabberd-nintendo-switch-npns/).
He explains why XMPP was chosen as protocol, why ejabberd was chosen as the
server and the performance tuning they had to do so that the Nintendo Switch
push service can now handle 10 million simultaneous connections and 2 billion
messages per day.

Recently a German politician, Katarina Barley of the Social Democrats, tweeted
that she'd like to see regulation in the instant messaging space where
messengers are forced to interoperate similarly to wireless carriers.
Many people responded to her tweet, saying that this is impossible or undesirable.
Daniel Gultsch, author of the Conversations and Quicksy Android clients,
has written a thoughtful post on why he thinks
[regulation is indeed necessary to create interoperability between instant messengers](https://gultsch.de/regulations.html).

{{< newsletter-subscribe >}}

Peter Saint-Andre wrote a short post on being invited to become [co-author of RFC 8600 XMPP Grid](https://stpeter.im/journal/1629.html).

Kaidan, an XMPP client, [has joined KDE](https://www.kaidan.im/2019/05/10/kaidan-joins-kde/).

Movim is the the first XMPP-based app that has [added emoji reactions to messages](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/movim-is-the-first-xmpp-client-that-supports-message-reactions-Id7F5J),
in both one-on-one conversations and groupchats, by making use of [XEP-0367: Message Attaching](https://xmpp.org/extensions/xep-0367.html). You can now [support the project on Patreon](https://www.patreon.com/movim).

Heather Ellsworth from Purism has written a [progress note for the Librem 5](https://puri.sm/posts/librem-5-end-of-may-progress/).
A notable messaging-related change is that the Lurch OMEMO plugin, used in Librem's Chatty messenger, has received a lot of updates recently.

Goffi is keeping us informed about his progress on Salut à Toi by writing weekly progress notes.
Recently he published notes for weeks [24](https://www.goffi.org/b/PfwWuArAxKnqvSND78iTig/progress-note), [25](https://www.goffi.org/b/byydDYtov3BUtRBwT8fgUg/progress-note)
and [26](https://www.goffi.org/b/mhS4EvyVJWaGteMCaSsTFR/progress-note).

Kiran Jasvanee has written an [introductory piece on XMPP](https://medium.com/@kiran.jasvanee/what-is-xmpp-ios-perspective-e1357555bef),
explaining protocol features such as Jabber IDs, extensibility and streams.

Mickaël Rémond wrote down some [thoughts on code style in library design](https://blog.process-one.net/thoughts-on-code-style-in-library-design/)
focusing on designing an API for the Fluux XMPP library.

Anurodh Pokharel (aka Anu) has written about a [first experimental Mac Build of Monal using Catalyst](https://monal.im/blog/first-mac-build-with-catalyst/).

Arnaud Joset has written guides to [using sat-pubsub](https://blog.agayon.be/sat_pubsub.html),
the PubSub component from the Salut à Toit project, and [JP, a powerful command line interface for Salut à Toit](https://blog.agayon.be/sat_jp.html).


## Events

Openfire developer Guus der Kinderen has written a [summary of the recent XMPP Sprint in The Hague](https://discourse.igniterealtime.org/t/xmpp-sprint-in-the-hague-nl-june-2019/85315).
Much of the work revolved around better support for push notifications. Multiple clients and servers were represented and being worked on.

Another XMPP Sprint is coming in Lyon, France, on 13-14th of July.

## Software releases

### Servers

ProcessOne has released [ejabberd 19.05](https://blog.process-one.net/ejabberd-19-05/), improving MIX and MucSub.

Ignite Realtime has released [Openfire 4.4.0 beta](https://discourse.igniterealtime.org/t/openfire-4-4-0-beta-release/).

Erlang Solutions has released [MongooseIM 3.4.0](https://www.erlang-solutions.com/blog/mongooseim-3-4-designed-with-privacy-in-mind.html) with a strong focus on GDRP compliance.

### Clients

[Conversations 2.5.0, 2.5.1, 2.5.2](https://github.com/siacs/Conversations/blob/master/CHANGELOG.md) added public channel search via search.jabbercat.org and reworked onboarding screens.

[Monal 3.8 for iOS](https://monal.im/blog/ios-3-8-released/) makes onboarding easier for non-technical users, as the new registration screen is easier and faster.

[BeagleIM (for macOS)](https://tigase.net/content/beagle-im) and [SiskinIM (for iOS)](https://siskin.im/), brought to you by Tigase, now
[both support the OMEMO end-to-end encryption protocol](https://tigase.net/blog-entry/beagleim-and-siskinim-just-got-omemo-support).

### Libraries

Strophe.js, the JavaScript XMPP library (published under the MIT license) has released [version 1.3.3](https://github.com/strophe/strophejs/releases/tag/v1.3.3).

### Google Summer of Code

The XSF has announced its participation in the Google Summer of Code 2019. The selected projects are:

[Prosody plugin installer](https://gsoc-prosody-2019.blogspot.com/), by João Duarte
[Poezio infinite scrolling using MAM](https://madhur96.github.io/gsoc19/), by Madhur Garg
[Jingle File Transfer for Dino](https://hrxi.github.io/gsoc/), by hrxi

### Other

The Debian XMPP Team has [launched a blog](https://xmpp-team.pages.debian.net/blog/2019/05/debian-xmpp-team-starts-a-blog.html).

Conversation's [server compliance tester](https://compliance.conversations.im/) has been redesigned and is now easier to navigate.

Tigase is now a Gold sponsor of the XSF.
