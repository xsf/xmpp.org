---
title: XMPP Newsletter, 01 Oct 2019, FOSDEM 2020, modernization of XMPP, peer networks
date: 2019-10-01
author: nyco
categories: ["Newsletter"]
aliases:
    - "/2019/10/newsletter-01-october/"
---

Welcome to the XMPP newsletter covering the month of September.

New this month: we've made explicit that this newsletter can be shared and adapted as defined by the [CC by-sa 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/), and we've added the credits as this is a community effort.

Be kind, inform your friends and colleagues: forward this newsletter!

Please [submit your XMPP/Jabber articles, tutorials or blog posts](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter) on our wiki.

{{< newsletter-subscribe >}}

## Articles

Ralph Meijer, chairman of the Board of Directors of the XSF, has written an introductory piece about "[XMPP Message Attaching, Fastening, References](https://ralphm.net/blog/2019/09/09/fastening)", specifications currently in progress.

In case of internet shut down, whether by disaster or voluntarily, peer networks are useful. [Monal uses Airdrop](http://monal.im/blog/xmppsignalbluetoothp2p-wifi-serverless-chat/) (wifi and bluetooth) along with XMPP and OMEMO end-to-end encryption.

![Monal and Airdrop screenshots](https://framapic.org/Qg1mv43w1673/akPmtepp0nfH.png)

JabberFr, the French XMPP/Jabber community, has again [translated the XMPP newsletter in French](https://news.jabberfr.org/2019/09/lettre-dactualite-xmpp-du-3-septembre-2019/), merci beaucoup.

We have started a very minimalistic [communication guide](https://wiki.xmpp.org/web/Basic_communication_guide_for_XMPP_techies) to help promoting a project through social networks and other means such as blog posts. Could be valuable for those involved in XMPP projects and would like to get ideas on how to reach out to different communities.

## Events

As usual every year, that time has come: we proudly announce the XMPP Summit 24 and the XSF participation to [FOSDEM](https://fosdem.org/2020/). The 24th XMPP Summit will happen on Thursday 30th and Friday 31st of January, and FOSDEM will be held on Saturday 1st and Sunday 2nd of February. Prepare for the community gathering; now is a good time to start booking your flights!

![FOSDEM 2020](https://framapic.org/fTZlikXsyi0F/ZqlvJhNjWDFj.png)

## Software releases
          
### Servers

Réda Housni Alaoui is reviving the formerly dormant [Vysper XMPP server](https://github.com/apache/mina-vysper) (pronounced as "whisper").

[Xabber Server v.0.9 alpha is released](https://blog.xabber.com/xabber-server-v-0-9-alpha-is-released/), with quick installation and management panel and interesting innovations.

[MongooseIM 3.4.1 is out now](https://www.erlang-solutions.com/resources/download.html) with an important security upgrade, fixing a vulnerability that allowed any logged in user to crash the node with malicious stanza on certain (but popular) configurations. [Read the whole thread on Twitter](https://twitter.com/MongooseIM/status/1176111308430815232) for more information.

The igniterealtime community has a lot of news:

* [Openfire 4.4.2](https://discourse.igniterealtime.org/t/openfire-4-4-2-release/86209): "This release should better support server to server (s2s) connections, fix a few admin console XSS-style issues, and improve client session stability."
* The Fastpath Service plugin has been released in versions [4.4.4](https://discourse.igniterealtime.org/t/fastpath-service-plugin-4-4-4-released/86155) and [4.4.5](https://discourse.igniterealtime.org/t/fastpath-service-plugin-4-4-5-released/86198), bringing support for managed queued chat requests, such as a support team might use.
* [Search plugin 1.7.3](https://discourse.igniterealtime.org/t/search-plugin-1-7-3-released/86207): "This update adds protection against CSRF and XSS attacks."
* [Monitoring Service plugin 1.8.1](https://discourse.igniterealtime.org/t/monitoring-service-plugin-1-8-1-released/86208): "This hotfix update adds protection against XSS attacks on Archiving Settings page."

Jérôme Sautret, from ProcessOne, has announced [ejabberd 19.09](https://blog.process-one.net/ejabberd-19-09/), that brings improved automatic certificate management stack.

The Prosody team have just released a new update to their stable branch, [Prosody 0.11.3](https://blog.prosody.im/prosody-0.11.3-released/) which includes performance and compatibility improvements among other fixes.

### Clients and applications

Profanity, has been released in [version 0.7.0](https://github.com/profanity-im/profanity/releases/tag/0.7.0) after five months of work, bringing OMEMO end-to-end encryption, followed by a [0.7.1](https://github.com/profanity-im/profanity/releases/tag/0.7.1) bug fix release.

[Multiple vulnerabilities have been found in Dino](https://gultsch.de/dino_multiple.html), please update as soon as possible if you are a Dino user.

Converse has been released in versions [5.0.2](https://github.com/conversejs/converse.js/releases/tag/v5.0.2) and [5.0.3](https://github.com/conversejs/converse.js/releases/tag/v5.0.3) fixing security issues among others.
Converse users may find useful the new [plugin to verify HTTP Requests via XMPP](https://blog.agayon.be/converse_xep_0070.html) from Agayon.
For developers, there is a [Converse Docker image](https://github.com/conversejs/converse.js-docker) by odajay. 

Conversations has been released in versions [2.5.8](https://github.com/siacs/Conversations/releases/tag/2.5.8), [2.5.9](https://github.com/siacs/Conversations/releases/tag/2.5.9), [2.5.10](https://github.com/siacs/Conversations/releases/tag/2.5.10) and [2.5.11](https://github.com/siacs/Conversations/releases/tag/2.5.11).

[Monal 4 with iOS 13 support and dark mode is out](https://monal.im/blog/monal-4-out/). Mac update is expected to be released for October.

## Services

[Christopher Muclumbus](https://search.jabber.network/), a listing and search engine of public XMPP chats, has been updated with a visual redesign, group chat avatars, link to anonymous web chat and logs if available, and software version pie chart.

## Extensions and specifications

This month, there were three proposed XEPs, and two updated. No XEPs in Last Call, New, or Obsoleted.

### Proposed

#### Message Fastening

Abstract:
This specification defines a way for payloads on a message to be marked as being logically fastened to a previous message.

URL: https://xmpp.org/extensions/inbox/fasten.html

#### XMPP Compliance Suites 2020

Abstract:
This document defines XMPP protocol compliance levels.

URL: https://xmpp.org/extensions/inbox/cs-2020.html

#### Authorization Tokens

Abstract:
This document defines an XMPP protocol extension for issuing authentication tokens to client applications and provides methods for managing сlient connections.

URL: https://xmpp.org/extensions/inbox/auth-tokens.html

### Updated

* Version 0.13.1 of XEP-0280 (Message Carbons) has been released. Changelog: Add clear example on problematic (spoofed) carbon messages and that they need to be handled. (gl). URL: https://xmpp.org/extensions/xep-0280.html
* Version 1.16.0 of XEP-0060 (Publish-Subscribe) has been released. Changelog:Add a pubsub#rsm disco#info feature to clear confusion (edhelas). URL: https://xmpp.org/extensions/xep-0060.html

## See you in November!

This XMPP Newsletter is a community collaborative effort. Thanks to Nÿco, Daniel, Jwi, and MDosch for aggregating the news. Thanks Nÿco, Seve, Jwi, and Matt for the copywriting. Thanks Guus, Seve, Jonas for the reviews.

Please follow and relay the XMPP news on our Twitter account [@xmpp](https://twitter.com/xmpp).

## License

This newsletter is published under the CC by-sa license: https://creativecommons.org/licenses/by-sa/4.0/
