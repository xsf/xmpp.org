---
title: The XMPP Newsletter August 2021
author: emus
date: 2021-09-05
categories: ["Newsletter"]
aliases:
    "2021/08/newsletter-08-august/"
---

Welcome to the XMPP Newsletter covering the month of August 2021.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider to say thanks or help these projects!

[Read this Newsletter via our RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Interested in supporting the Newsletter team? Read more at the bottom.

Other than that - enjoy reading!

### Newsletter translations

Translations of the XMPP Newsletter will be released here (with some delay):

- The French translation appears at [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- The German translation appears at [anoxinon.de](https://anoxinon.de/blog/)
- The Italian translation appears at [NicFab.it](https://www.nicfab.it/)

Many thanks to the translators and their work! This is a great help to spread the news! Please join them in their work or start over with another language!

## Events

[XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours) - Also, checkout our new [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)!

[Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): Monthly Meeting of XMPP Enthusiasts in Berlin - always 2nd Wednesday of the month.

## Articles

What is project XPORTA? As announced in the [April '21 newsletter](https://xmpp.org/2021/04/newsletter-04-april/), the Data Portability and Services Incubator [at NGI](https://dapsi.ngi.eu) is sponsoring the XMPP Account Portability project named XPORTA. This month they host [an interview with Matthew Wild](https://dapsi.ngi.eu/interview-meet-project-xporta-xmpp-account-portability/) about how this project came into existence.

The "have your own TelCo based on XMPP" service [jmp.chat](https://jmp.chat) has a new blog, with a twist, now based on Libervia so based on XMPP, with all the nice blog features that you want (like RSS) and even subscriptions via XMPP (with compatible clients like Movim or Libervia). The [post announcing the new blog](https://blog.jmp.chat/b/august-newsletter-2021) also covers the new registration flow and billing system. But the previous post is the real jewel, called [Adventures in WebRTC: Making Phone Calls from XMPP](https://blog.jmp.chat/b/adventures-in-webrtc-making-phone-calls-from-xmpp-znLOT5). It details the journey through WebRTC debugging, multiple clients, NAT, ICE and all monitored through Wireshark. Get a hot or cold beverage to go with this about 70 minutes long read.

In [the previous newsletter](https://xmpp.org/2021/07/newsletter-07-july/) we mentioned that Debian Linux 11 will soon be launched with updated XMPP software, as this happened in the meantime, server admins are already updating or even setting up new deployments. Such as Nelson from Luxembourg, who published a blog post about setting up a [server with ejabberd on Debian 11 Bullseye](https://www.aroundtheglobe.biz/posts/20210819-your_own_xmpp_server_with_ejabberd_on_Debian_11_Bullseye.html).

While the Snikket iOS client app was just released, read more below, the behind the scenes development continues. In the latest blog post, Matthew Wild announces that [the expert folk at Simply Secure will be performing a usability audit of the current app](https://snikket.org/blog/simply-secure-collaboration/), as well as conducting usability testing thanks to funding from the OTF’s Usability Lab. The analysis will help to improve the UX of the iOS app and Snikket as a whole.

Missed in last month's issue, the folks at [cometchat](https://www.cometchat.com/) have blogged about XMPP's history, working architecture, stanzas and 
features in general in [Everything About XMPP - Extensible Messaging & Presence Protocol](https://www.cometchat.com/blog/xmpp-extensible-messaging-presence-protocol). If you want a quick technical overview (or need one to show others what XMPP is all about) this ~15 minutes read can bring one up to speed.

"Spaces" are the new XMPP frontier to be explored, and you'd get a glimpse of them in Gajim client news below, but the work is pretty elaborate and ongoing with many people involved. [Renga](https://github.com/HaikuArchives/Renga)'s (an XMPP client for Haiku) developer [pulkomandy](https://pulkomandy.tk/_/_.users/_pulkomandy) has blogged [Some random thoughts about XMPP spaces](https://pulkomandy.tk/_/_Development/_Some%20random%20thoughts%20about%20XMPP%20spaces) thinking about use cases (family, business, communities) and user interfaces.

Any Turkish speakers reading the newsletter? We don't have a translation yet, but [Ged](https://fosstodon.org/@Ged) has just published an in-depth blog post about XMPP titled [Hangi "Chat" Programı?](https://www.yunbere.kalfazade.com/post/hangi-chat-programi). In about 40 minutes it takes the reader through the story of the 
protocol, tells about apps, servers, comparisons with popular apps and privacy.

The [March `21 newsletter](https://xmpp.org/2021/03/newsletter-03-march/) brought the news that JSXC (the Javascript XMPP Client) got funding to work on group chat calls. This month [they report](https://www.jsxc.org/blog/2021/08/31/A-group-call-proposal.html) on the work done and explain the current progress that can even be tested.

Finally, how does FaceTime work? [They interestingly use the same port (5223) as XMPP does...](https://matduggan.com/how-does-facetime-work/)

## Software news

### Clients and applications

[Gajim 1.4 Preview: Workspaces](https://gajim.org/post/2021-08-27-workspaces/). The Gajim team has been hard at work in the past months to prepare the 
next v1.4 release. The upcoming version brings a major interface redesign. In this post, they explain how the new interface works and what remains to be decided or implemented before the release.

![Gajim Workspaces (preview)](/images/newsletter/august2021/gajim-workspaces-preview.png "Gajim Workspaces (preview)")

[Libervia progress note 2021-W31](https://www.goffi.org/b/libervia-progress-note-2021-w31-Ua14) is out with information about Docker integration, the translation portal and the first 0.8.0 beta. It also has plenty of details about the work done on the ActivityPub Gateway project (grant announced in the [April '21 newsletter](https://xmpp.org/2021/04/newsletter-04-april/)) with SQL, DBus, PubSub and with new and updated XEPs.

Communiqué is a new XMPP client from the [Mellium Co-op](https://opencollective.com/mellium) team. It was [announced](https://opencollective.com/mellium/updates/introducing-communique) this month and presented at the XMPP Office Hours (unfortunately recording did not work out). The source code can be found [in the repository](https://github.com/mellium/xmpp/).

![Communiqué](/images/newsletter/august2021/communique.png "Communiqué")

Monal 5.0.1 is now available [for both iOS and macOS](https://monal.im/blog/monal-5-0-1-synchronized-builds-and-bugfixes/) bringing mostly corrections and more polish over the previously major release.

JSXC Openfire plugin gets a [4.3.1-1 release](https://discourse.igniterealtime.org/t/jsxc-openfire-plugin-4-3-1-1-released/90583), with mostly bug fixes and improvements from the JSXC project.

After so many months of waiting [the Snikket iOS app is now publicly released](https://snikket.org/blog/snikket-ios-public-release/). Snikket server admins can add the app to the invitations pages to have Apple users easily find it. If you are not running Snikket you can still use the app (you can use credentials directly) but do read the blog post to know what you need to add to your Prosody instance (invitations modules) or what limitations you might experience using any other server software.
 
![Snikket on iOS](/images/newsletter/august2021/snikket_on_ios.png "Snikket on iOS")

## Servers

Prosody 0.11.10 has been [released](https://blog.prosody.im/prosody-0.11.10-released/) with a fix for CVE-2021-37601 and some minor changes. Prosody developers recommend server admins to upgrade in order to fix the remote information disclosure issue.

## Libraries

The Mellium Dev Communiqué for August includes updates to the Mellium XMPP library as well as the new Communiqué instant messaging client. The biggest updates this month are MAM and ad-hoc commands support! [You can read more here.](https://opencollective.com/mellium/updates/dev-communique-for-august-2021)

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   No XEPs proposed this month.

### New

-   Version 0.1.0 of [XEP-0460](https://xmpp.org/extensions/xep-0460.html) (Pubsub Caching Hints)
    -   Accepted by vote of Council on 2021-07-21. (XEP Editor (jsc))

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 1.21.0 of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    -   Revert change from version 1.15.5 which changed meta-data to metadata in wire protocol. That was an unintended breaking change which has now been reverted. (pep)

-   Version 0.3.0 of [XEP-0214](https://xmpp.org/extensions/xep-0214.html) (File Repository and Sharing)
    -   Revert change from version 0.2.1 which changed meta-data to metadata in wire protocol. That was an unintended breaking change which has now been reverted. (rm)

-   Version 0.3.0 of [XEP-0248](https://xmpp.org/extensions/xep-0248.html) (PubSub Collection Nodes)
    -   Revert change from version 0.2.1 which changed meta-data to metadata in wire protocol. That was an unintended breaking change which has now been reverted. (rm)

-   Version 0.2.0 of [XEP-0283](https://xmpp.org/extensions/xep-0283.html) (Moved)
    -   Re-write the flow with a more focused approach. (mw)

-   Version 1.1.0 of [XEP-0429](https://xmpp.org/extensions/xep-0429.html) (Special Interests Group End to End Encryption)
    -   Add discussion venue after creation by the Infrastructure Team. (mw)

-   Version 1.24.0 of [XEP-0001](https://xmpp.org/extensions/xep-0001.html) (XMPP Extension Protocols)
    -   Change "Draft" to "Stable". (ssw)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   No Last Call this month.

### Stable (formely known as Draft)

Info: The XSF has decided to rename 'Draft' to 'Stable'. [Read more about it here.](https://github.com/xsf/xeps/pull/1100)

-   No Stable this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the XMPP community.

Therefore many thanks to Adrien Bourmault (neox), Anoxinon e.V. community, anubis, Benoît Sibaud, emus, Sam, Licaon_Kter, nicola, seveso, SouL, wurstsalat3000, Ysabeau for their support and help in creation, review and translation!

## Spread the news!

Please share the news via other networks:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

## Help us to build the newsletter

We started drafting in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days) in parallel to our efforts in the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. We really need more support!

You have a project and write about it? Please consider sharing your news or events here, and promote it to a large audience! 
And even if you can only spend a few minutes of support, these would already be helpful!

Tasks which need to be done on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Preparation for media images
- Translations: especially German and Spanish

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
