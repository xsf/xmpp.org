---
title: The XMPP Newsletter February 2021
date: 2021-03-05
author: emus
categories: ["Newsletter"]
aliases:
    - "/2021/02/newsletter-02-february/"
---

Welcome to the XMPP newsletter covering the month of February 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. 
If you are happy with the services and software you may be using, especially throughout the last year, 
please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom! Other than that - enjoy reading! 

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news.jabberfr.org/category/newsletter/).
- The German translation of the [XMPP Newsletter for January 2021 is available at Anoxinon](https://anoxinon.de/blog/xmpp_newsletter_januar_2021/).

## Events

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of every month.

## Videos

Matthew Wild gave a talk about [Products vs Protocols](https://peertube.thepacket.exchange/videos/watch/96e35d83-e70c-4a87-868b-f9cbeb48e1d0) at FOSDEM 2021.

[XMPP - eine Alternative zu Telegram, WhatsApp & Co? Mit Daniel Gultsch und DIE LINKE Berlin](https://video.ploud.fr/videos/watch/7e6876ed-7d4b-478d-a850-25dc84dcaf96) [DE]

The French [april.org](https://april.org) community podcast _(or on air on radio Cause Commune 93.1 FM and online)_ had a show on Jan 26 with Adrien Bourmault, Emmanuel Gil Peyrot and Nicolas Vérité about libre instant messaging. If you didn't catch it live, the [recording is out now](https://april.org/91-messageries-instantanees) _(the interesting part starts at 17:30)_. A transcript is [available as well](https://www.librealire.org/emission-libre-a-vous-diffusee-mardi-26-janvier-2021-sur-radio-cause-commune#Les-messageries-instantanees-libres-avec-Adrien-Bourmault-Emmanuel-Gil-nbsp) [FR].

[A quick introduction to XMPP (with Node.js and eJabberd)](https://www.youtube.com/watch?v=OVN99SgBGkM) by Hussein Nasser. In this video he goes through XMPP architecture, explains how it works and then finallly shows how to spin up an XMPP chat server and connect to it via Node.js.

[Movim](https://movim.eu) has been featured in the [Destination Linux Podcast](https://youtu.be/NhQW2yETvwU?t=2833).

## Articles 

Snikket: [Products vs Protocols: What Signal got right](https://snikket.org/blog/products-vs-protocols/). This extended version of Matthew Wild's recent [FOSDEM talk](https://peertube.thepacket.exchange/videos/watch/96e35d83-e70c-4a87-868b-f9cbeb48e1d0) explores the thinking behind Snikket, and what XMPP and decentralized protocols can learn from Signal's success.

Rohan Kumar's blog article about [WhatsApp and the domestication of users](https://seirdy.one/2021/01/27/whatsapp-and-the-domestication-of-users.html) has been making the rounds around the internet, it mentions XMPP and other decentralized solutions. It has been translated into several other languages too. There's also follow up on [Keeping platforms open](https://seirdy.one/2021/02/23/keeping-platforms-open.html) that covers a bit of XMPP history.

Within the recent month, particularly after WhatsApp’s announcement and subsequent postponement of its updated privacy policy, thousands of users started migrating messengers. [An introduction to the 3 types of messengers, simply explained](https://thilobuchholz.de/2021/02/3-types-of-messengers-simply-explained/).

In February 2021 the year of the Ox starts. At Berlin XMPP meetup, the new year [was celebrated with an introducting talk](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup/4d69d3cc-f28f-465a-baf2-0696024dc9ef) about "[XEP-0373: OpenPGP for XMPP](https://xmpp.org/extensions/xep-0373.html)" and "[XEP-0374: OpenPGP for XMPP Instant Messaging](https://xmpp.org/extensions/xep-0374.html)" with a panel of experts, namely DebXWoody (implementer of OX in Profanity), defanor (implementer of OX in rexmpp), Florian (co-author of the OX standards), lovetox (implementer of OX for Gajim), and Paul (implementer of OX in Smack). While the presentations were not recorded [the notes from the meeting](https://hackmd.io/Ig2azxzUTQuFxN73Ds8Qig) are available for reading.

Short guide on the setup of Siskin IM in [English](https://xmppeinrichtung.blogspot.com/2021/01/installation-and-configuration-of.html) and [German](https://xmppeinrichtung.blogspot.com/2021/01/installation-and-configuration-of.html).

A tutorial on how to [set up an XMPP server with Prosody](https://toutetrien.lithio.fr/article/installer-son-serveur-xmpp-avec-prosody) [FR].

[Mellium](https://mellium.im) has released a [yearly progress report](https://blog.samwhited.com/2021/02/mellium-year-in-review/) post for 2020 as well as an [Architecture Overview](https://blog.samwhited.com/2021/02/mellium-architecture/) meant to help new contributors find their way around the codebase.

Sam Whited has re-published documentation on parsing and validating XMPP addresses (JIDs) as a [blog post](https://blog.samwhited.com/2021/02/xmpp-addresses/).

Thoughts on [Decentralized forge: distributing the means of digital production](https://staticadventures.netlib.re/blog/decentralized-forge/) covers a lot of protocols and tech, and XMPP is mentioned (OAuth and Salut-a-Toi).

## Software news

### Clients and applications

[Conversations 2.9.7 has been released](https://github.com/iNPUTmice/Conversations/blob/master/CHANGELOG.md), adding the ability to select incoming call ringtone, fixing OpenPGP key ID discovery for OpenKeychain 5.6+, improving stability of RTP session establishment (calling), and more.

[Gajim 1.3.0](https://gajim.org/post/2021-02-08-gajim-1.3.0-released/) and [1.3.1](https://gajim.org/post/2021-03-01-gajim-1.3.1-released/) have been released. Five months have passed since the release of Gajim 1.2.2. Many new features have been developed during this time, including a complete redesign of both Gajim’s Preferences window and configuration backend, an all new Profile window, support for Chat Markers, a new user interface for voice/video calls, and much more. As covered in [February's development news](https://gajim.org/post/2021-02-25-development-news-february/), February brought mostly bug fixes. The Profile window’s error handling has been improved, and selecting small images for an avatar should now work as expected. While fixing those bugs, Gajim’s team has been working on something big.

[Kaidan 0.7 has been released](https://www.kaidan.im/2021/02/02/kaidan-0.7.0/): This release enables users to send files via drag and drop. Furthermore, it is now possible to see which chat client and operating system a contact is using.

[Monal 5 Beta 1 has been released](https://monal.im/blog/monal-5-beta-1/), which brings many improvements with OMEMO. While in Beta, the Monal developers are working on support for MUC, and a new file transfer user interface. Monal 5 will also support [inline display of audio and video files](https://monal.im/blog/monal-5-will-support-inline-audio-and-video/). [Push server stats from January](https://monal.im/blog/monal-stats-1-2021/) reveal quite some activity around Monal. Monal developers also seek to [redesign the logo](https://monal.im/blog/redesign-of-the-monal-logo/), so if you are feeling creative, feel free to give them a hand before March 31.

![Preview of the Monal inline audio and video player](/images/newsletter/february2021/Monal_voicemessage.png "Monal inline A/V")

[Movim 0.19 - Ikeya is out](https://mov.im/?node/pubsub.movim.eu/Movim/944ac1f8-8034-45ac-976a-cc5fcd35d63e)! With a lot of performances improvements but also many new features such as GIF in chats, messages replies, community browsing redesign, and much more.
 
The PeerTube plugin livechat [ships with Converse.js](https://github.com/JohnXLivingston/peertube-plugin-livechat).
 
[SiskinIM 6.3 has been released](https://github.com/tigase/siskin-im/releases/tag/6.3) containing several fixes (clicking on links, crashes related to markdown formatting, sharing in public groups, issues with message corrections and group chat layout improvements).
 
## Servers

[Snikket’s February 2021 Server Release](https://snikket.org/blog/feb-2021-server-release/) brings a fancy new web-based admin dashboard, allowing you to perform all kinds of management tasks. It also adds a simple portal for non-administrative users to log in and manage their account. Currently this contains a profile editor, and will grow to include other account settings, and data import/export. And there is more: Raspberry Pi and ARM support, and the introduction of user groups, known as "circles".

![Snikket web admin view](/images/newsletter/february2021/snikket-web-admin-multilingual.png "Snikket web admin view")

[Prosody 0.11.8 has been released](https://blog.prosody.im/prosody-0.11.8-released/). This release brings bugfixes, improvements to websocket performance (thanks to the Jitsi folks), and also fixes a security issue.

[ejabberd 21.01](https://www.process-one.net/blog/ejabberd-21-01/) has been released, includes many improvements & bugfixes (e.g. STUN/TURN default blacklist, better systemd integration). Server admins can get the new version from the developers website as usual, and Debian users already can upgrade to the new version from `buster-backports` repo.

The Ignite Realtime community is happy to announce the [release of version 0.8.0 of the Push Notification plugin for Openfire](https://discourse.igniterealtime.org/t/push-notification-openfire-plugin-0-8-0-released/89657)! This update fixes a problem that prevented certain clients (like Siskin) from successfully registering a push notification service.

## Libraries

[Mellium v0.18.0 has been released](https://pkg.go.dev/mellium.im/xmpp@v0.18.0), bringing with it refactored connection APIs, better server support, websockets, and the usual assortment of bug fixes and usability improvements. For the full list, see the [changelog](https://github.com/mellium/xmpp/releases/tag/v0.18.0).

[python-nbxmpp 2.0.1 and 2.0.2 have been released](https://gajim.org/post/2021-02-25-development-news-february/), both addressing multiple bugs.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   [Implicit XMPP WebSocket Endpoints](https://xmpp.org/extensions/inbox/xep-iwe.html)
    -   This document specifies implicit connection endpoints for XMPP over WebSocket (RFC 7395).

### New

-   Version 0.2.0 of [XEP-0455](https://xmpp.org/extensions/xep-0455.html) (Service Outage Status)
    -   This document defines an XMPP protocol extension that enables server administrators to communicate issues with the server to all users in a semantic manner.

### Deferred

If an experimental XEP is not updated for more than six months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 0.2.0 of [XEP-0452](https://xmpp.org/extensions/xep-0452.html) (MUC Mention Notifications)
    -   Require nickname registration for notifications to work (jcb)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   No new Last Call this month.

### Draft

-   No Drafts this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to wurstsalat3000, Sam Whited, pitchum, Licaon_Kter, jeybe and emus for their help in creating it!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

## Help us to build the newsletter

We started drafting in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days) in parallel to our efforts in the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. 

You have a project and write about it? Please consider sharing your news or events here, and promote it to a large audience! 
Even if you can only spend a few minutes, these would already be helpful!

Tasks which need to be done on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Preparation for media images
- Translations: especially German and Spanish

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).

