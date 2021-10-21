---
title: The XMPP Newsletter November 2020
date: 2020-12-09
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/11/newsletter-11-november/"
---

Welcome to the XMPP newsletter covering the month of November 2020.

This will be the last newsletter release for this (crazy) year, it was great to have you here reading! Many thanks to you contributors and reviewers. The XMPP Newsletter is a community project, and if you are interested to contribute to it in the coming year - you’re welcome to join!

For everyone having a new year’s break: we wish you a nice time! Until then stay safe and see you in the next year.

Many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout this year, please consider to say thanks or help these projects. Looking forward to XMPP in 2021!

### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news/jabberfr.org/category/newsletter/).

## XSF Announcement

We would like to make an informational announcement about an important circumstance regarding certificates to all parties involved in XMPP.
If you or related parties are affected please spread the word on this:

Let's Encrypt announced to [switch away from their Root CA certificate cross-signed by IdenTrust](https://letsencrypt.org/2020/11/06/own-two-feet.html). 
This means that old client devices (especially the roughly one third of Android phones running Android 7.0 and older) will consider Let's Encrypt certificates issued after January 11th 2021 as untrustworthy. 
This problem will not go away, as the IdenTrust cross-signed certificate will expire in September, but there are some possible mitigations:
- For users: It is possible, but not very straight-forward to [add the new Root CA certificate to the system trust store](https://stackoverflow.com/a/22040887/)
- For client developers: You can bundle the new [ISG Root X1](https://letsencrypt.org/certificates/) certificate with the app, or implement a manual CA approval mechanism like [Memorizing Trust Manager](https://github.com/ge0rg/MemorizingTrustManager)
- For server operators: You can use the ["alternate" option](https://community.letsencrypt.org/t/transition-to-isrgs-root-delayed-until-jan-11-2021/125516) between January and September to obtain certificates signed by the old IdenTrust-based root. 

The implementation of the ISRG Root X1 certificate is [explained in this article](https://www.stoutner.com/lets-encrypt-isrg-root-x1-and-privacy-browser/).

## Articles

Chris Beckstrom wrote a post on the details of how they hacked together a [bridge between iMessage and XMPP](https://chrisbeckstrom.com/posts/How-I-Bridged-iMessage-and-XMPP/).

Nico Wellpott wrote a post on [how he gathered presence and user count statistics for a group chat](https://magicbroccoli.de/post/oh-muc-stats/).

This month ejabberd celebrated their 18th birthday. On this occasion [Marek Foss talked with Alexey Shchepin](https://www.process-one.net/blog/interview-with-alexey-shchepin-creator-of-ejabberd/), who created ejabberd in November 2002.

## Software news

### Clients and applications

Dino 0.2 'Mexican Caribbean Coral Reefs' [has been released](https://dino.im/blog/2020/11/dino-0.2-release/): The 0.2 release adds message correction, improves the file upload functionality and provides more information about message encryption. Besides other smaller changes it also fixes a number of bugs.

![Dino_message_correction](/images/newsletter/december2020/Dino_message_correction.png "Dino_message_correction")

Conversations 2.9.1 [has been released](https://github.com/iNPUTmice/Conversations/releases/tag/2.9.1). This release includes fixes for searching on older Android devices, and optimizes memory consumption.

Snikket also released a [new version](https://snikket.org/blog/snikket-app-update-2.9.0/) of their Android app, based on the Conversations 2.9.0 release. They also announced sponsorship of [OMEMO end-to-end encryption for group chats in Siskin IM](https://snikket.org/blog/sponsoring-group-omemo-in-siskin/), the iOS client by Tigase.

Beagle IM 4.1 and Siskin IM 6.1 [have been released](https://tigase.net/beagleim-4.1-and-siskin-6.1-released/). The biggest change for this release is the introduction of [XEP-0215](https://xmpp.org/extensions/xep-0215.html): External Service Discovery which helps with establishing audio and video calls.

![beagle-accounts](/images/newsletter/december2020/beagle-accounts.png "beagle-accounts")

New [Beta releases for Monal 4.9](https://monal.im/blog/4-9-betas/) have been published. While 4.9 final has already been [released for Mac](https://monal.im/blog/monal-mac-4-9-out-no-arm-yet/), the ARM version still need some time.

The first stable blabber.im App version 3.0.1 is [available for download](https://blabber.im/en/download/). If you want to update your Pix-Art Messenger to blabber.im, please [read our update guide](https://blabber.im/en/update-guide/). (EN/DE)

[Gajim Development News](https://gajim.org/post/2020-11-27-development-news-november/): In November, Gajim’s development team worked on Chat Markers, a feature many of you had wished to see in Gajim. Chat Markers enable you to see whether your contact has read your messages, and they help Gajim to manage notifications if you read messages on your phone or other devices.

News from the Ignite Realtime community: [Spark has been released in version 2.9.4](https://discourse.igniterealtime.org/t/spark-2-9-4-released/89160). This release includes fixes for SSL certificates, a new option to disable games, and further improvements.

## Servers

News again from the Ignite Realtime community: Version 2.1.6 of the [Client Control plugin for Openfire](https://discourse.igniterealtime.org/t/client-control-plugin-2-1-6-released/89159) has been released.

Both Tigase clients had MIX support for a while, so now the XMPP component (based on Tigase PubSub Component) for Tigase XMPP Server providing support for XEP-0369: Mediated Information eXchange (MIX), [is publicly available](https://github.com/tigase/tigase-mix) too.

During the interview with Alexey Shchepin, the author of ejabberd mentioned Jamler, as an 2011 experiment to rewrite ejabberd in OCaml. This historic code is [now released as open-source](https://www.process-one.net/blog/jamler-xmpp-server-an-ocaml-experiment-based-on-ejabberd-2-1-8/) too, so it can be studied.

## Libraries

Yes - more news from the Ignite Realtime community: There is a [first release candidate](https://discourse.igniterealtime.org/t/first-release-candidate-of-smack-4-4-published/89131) of Smack 4.4.0 (Smack 4.4.0-rc1). The developers call for testing.

## Other

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html).

### Proposed Extensions

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   Several extensions have been proposed this month. They have been accepted by the council, and are listed in the New section below.

### New

-   Version 0.1.0 of [XEP-0449](https://xmpp.org/extensions/xep-0449.html) (Stickers)
    -   This specification provides a protocol to send stickers and to create and share sticker packs.
    -   Accepted by vote of Council on 2020-11-18.

-   Version 0.1.0 of [XEP-0448](https://xmpp.org/extensions/xep-0448.html) (Encryption for stateless file sharing)
    -   This specification provides a protocol for sharing encrypted files using the stateless file sharing protocol (XEP-0447).
    -   Accepted by vote of Council on 2020-11-18.

-   Version 0.1.0 of [XEP-0447](https://xmpp.org/extensions/xep-0447.html) (Stateless file sharing)
    -   This specification describes a protocol for stateless asynchronous file sharing with integrity and transport flexibility. It allows clients to provide a good interoperable user experience in combination with Carbons and MAM.
    -   Accepted by vote of Council on 2020-11-18.

-   Version 0.1.0 of [XEP-0446](https://xmpp.org/extensions/xep-0446.html) (File metadata element)
    -   This specification defines a generic file metadata element to be used in other specifications.
    -   Accepted by vote of Council on 2020-11-18.

-   Version 0.2.0 of [XEP-0445](https://xmpp.org/extensions/xep-0445.html) (Pre-Authenticated In-Band Registration)
    -   This document extends the In-Band-Registration protocol to use invitation tokens, e.g. for registering accounts on non-public servers.
    -   Accepted by vote of Council on 2020-11-04.

### Deferred

If an experimental XEP isn’t updated for more than six months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 0.6.0 of [XEP-0373](https://xmpp.org/extensions/xep-0373.html) (OpenPGP for XMPP)
    -   Fix 'to'-attribute requirements: All content elements which are signed using OpenPGP need that attribute to prevent Surreptitious Forward Attacks. The `<crypt/>` element does not require one, as the intended recipient is established by the encryption itself. The XEP had the requirements for `<sign/>` and `<crypt/>` mixed up.

-   Version 0.6.0 of [XEP-0389](https://xmpp.org/extensions/xep-0389.html) (Extensible In-Band Registration)
    -   Error out if a client selects an invalid flow.

-   Version 0.3.0 of [XEP-0443](https://xmpp.org/extensions/xep-0443.html) (XMPP Compliance Suites 2021)
    -   Add more notable XEPs.

-   Version 0.2.0 of [XEP-0438](https://xmpp.org/extensions/xep-0438.html) (Best practices for password hashing and storage)
    -   Update to match draft-ietf-kitten-password-storage-01.

-   Version 1.34.0 of [XEP-0045](https://xmpp.org/extensions/xep-0045.html) (Multi-User Chat)
    -   Specify the use of a delay element in the initial subject message.

-   Version 1.3.0 of [XEP-0118](https://xmpp.org/extensions/xep-0118.html) (User Tune)
    -   Add further tags for non-pop music.

-   Version 1.2.0 of [XEP-0308](https://xmpp.org/extensions/xep-0308.html) (Last Message Correction)
    -   Reword note about how to handle LMC in cases where it is not clear that all recipients support it.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   No Last Call this month.

### Draft

-   Version 1.0.0 of [XEP-0443](https://xmpp.org/extensions/xep-0443.html) (XMPP Compliance Suites 2021)
    -   Accept as Draft as per Council vote from 2020-11-11.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to Dominion0815, emus, kikiuchiyo, Licaon_Kter, mwild1, nico, SeveFP and wurstsalat3000 for their help in creating it! Special thanks to wurstsalat3000, for running a great summary on the XEPs each month!

See you in the next year, stay safe!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

## Subscribe to the newsletter

We suggest you [Subscribe](https://tinyletter.com/xmpp) to receive the next editions in your inbox as soon as it is published! 
Promote this newsletter to whoever may be interested.

## Help us to build the newsletter

We started drafting every new issue in the [XSF Github repository](https://github.com/xsf/xmpp.org/pulls) and we are 
always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) 
and thereby help us sustain this as a community effort. 

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
