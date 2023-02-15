---
title: The XMPP Newsletter December 2022 & January 2023
date: 2023-02-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of December 2022 & January 2023. 
This is the first release after a well-deserved winter break! Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

## XSF Announcements

If you are interested in becoming an XSF member, the [listings are open until 19th February 2023](https://wiki.xmpp.org/web/Membership_Applications_Q1_2023).

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

### Google Summer of Code 2023

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

We are considering to participate the Google Summer of Code 2023! If you are interested start [reading here](https://wiki.xmpp.org/web/Google_Summer_of_Code_2023).

## XMPP Events

- [XMPP Summit 25 and at FOSDEM 2023](https://xmpp.org/2023/01/xmpp-at-fosdem-2023/)
- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## XMPP Talks

- [XMPP - End of the year 2022 talk](https://bbb.sfconservancy.org/b/ste-fdo-qen)
- [Interoperable Chat, Dutch Healthcare and the Digital Services Act](https://fosdem.org/2023/schedule/event/interoperable_chat/) Winfried shares the many challenges faced while working on a standard for interoperable chat in healthcare that’s compatible with the EU’s new regulations.
- [P10K: getting 10000 participants into a Jitsi meeting](https://fosdem.org/2023/schedule/event/jitsi_p10k/), Saúl from the Jitsi team reveals their interesting journey to reach 10000 participants in an XMPP-powered Jitsi video conference.
- [Modernizing Authentication and Authorization in XMPP](https://fosdem.org/2023/schedule/event/modern_xmpp_auth/): Matthew Wild, founder of the Prosody and Snikket projects, explains why it’s time for us to look beyond passwords for authentication.

## Articles

A [stress test of PeerTube streaming server](https://www.octopuce.fr/test-de-charge-dun-peertube-en-live-avec-auposte/) [FR] including a live chat based on XMPP (Prosody) was performed. It helped to identify a number of possible optimizations in the Peertube live chat plugin. Read the [plugin author's post](https://john-livingston.fr/foss/article/peertube-chat-plugin-quick-feedbacks-about-a-live-stress-test) for more details.

{{< figure src="/images/newsletter/2023-02-05/peertube.jpg" caption="Peertube with XMPP-based live chat" >}}

Jabber.org, the original XMPP instant messaging service was [migrated to the Prosody IM server on the weekend of January 14-15th](http://www.jabber.org/notices.html). Full history: jabberd -> ejabberd -> Isode M-Link -> Prosody IM

An article about ["Tokenization of sustainable real estate in Smart Cities : Monetization as basis for construction, authorization and carbon neutralization in CPS"](https://ieeexplore.ieee.org/document/9968404) (using techniques based on XMPP) was presented on IECON2022 and got published recently.

[JMP's December Newsletter](https://blog.jmp.chat/b/december-newsletter-2022) talks about their new co-op structure, an important security fix in the Cheogram Android app, and a review of the highlights of 2022.  [JMP's January Newsletter](https://blog.jmp.chat/b/january-newsletter-2023) mentions another new release including a new [XMPP Threaded Chat UI](https://kumi.tube/w/1LQQp5Uia4u8Pdojxen1y8) and new payment options for the service. Last but not least: [Writing a Chat Client from Scratch](https://blog.jmp.chat/b/2022-chat-client-from-scratch) in Ruby.

Snikket informs about the [F-Droid security warnings](https://snikket.org/blog/fdroid-security-warning/) and their [Security update](https://snikket.org/blog/fdroid-security-update/). The issues has been solved already.

[vanitasvitae](https://blog.jabberhead.tk/) writes about PGPainless: [Use Any SOP Binary With SOP-Java and External-SOP](https://blog.jabberhead.tk/2023/01/13/use-any-sop-binary-with-sop-java-and-external-sop/)

nicfab writes about the new [EU NIS 2 directive: does it apply to anyone who provides free online digital services?](https://notes.nicfab.eu/en/posts/nis2/)

## Software news
### Clients and applications

[BeagleIM 5.3.2, 5.3.3 and SiskinIM 7.3.1, 7.3.2](https://tigase.org/blog/beagleim-5.3.2-and-siskinim-7.3.1-released/) have been released with an option to block whole domains and a number of bugfixes. And brand new logos and icons.

[Conversation 2.11.0 to 2.12.1 have been released](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md)! They implement Extensible SASL Profile, Bind 2.0 + Channel Binding and Fast for faster reconnects. Furthermore the ability to switch from audio call to video call, to delete your own avatar and a notification for missed calls has been added. Since version 2.12.0 it now also integrates an [UnifiedPush Distributor](https://unifiedpush.org/users/distributors/) to facilitate push messages to other UnifiedPush enabled apps like Tusky and Fedilab. Users can use the developer provided UP server or ask their server admins to host an UP server as [an universal XMPP transport component](https://codeberg.org/iNPUTmice/up) or load the [new Prosody module](https://modules.prosody.im/mod_unified_push). As announced in the [November 2022 newsletter](https://xmpp.org/2022/12/the-xmpp-newsletter-november-2022/) version 3.0 got funded, hence development has started already, you can keep an eye on its pace in the [new `c3` code branch](https://codeberg.org/iNPUTmice/Conversations/commits/branch/c3).

[Gajim 1.6.0](https://gajim.org/post/2023-01-07-gajim-1.6.0-released/) and [1.6.1](https://gajim.org/post/2023-01-14-gajim-1.6.1-released/) have been released. For Gajim 1.6, developers ported Gajim’s and python-nbxmpp’s underlying HTTP library to libsoup3. Also, audio previews now look nicer and allow for more control (playback speed, jumping). Emoji rendering on MacOS has been repaired and many fixes have been implemented under the hood.

Libervia has been granted a [NLnet NGI Assure Fund for implementation of Audio/Video Calls](https://nlnet.nl/project/Libervia-AV/).

[Moxxy 0.4.0](https://codeberg.org/moxxy/moxxy/releases/tag/v0.4.0) and [0.4.1](https://codeberg.org/moxxy/moxxy/releases/tag/v0.4.1) have been released. These two releases bring stickers, reactions, voice message recording and various improvements and fixes to the UI and XMPP code.

From the ignite realtime community:

- [Spark 3.0.1 Released](https://discourse.igniterealtime.org/t/spark-3-0-1-released/92353)
{{< figure src="/images/newsletter/2023-02-05/spark.png" caption="Spark 3.0.1" >}}

- A Denial of Service Vulnerability in Smack 4.4 [has been fixed](https://discourse.igniterealtime.org/t/denial-of-service-vulnerability-in-smack-4-4-if-xmpptcpconnection-is-used-with-stax/92314)
- [The Ignite Realtime community now offers a Mastodon service](https://discourse.igniterealtime.org/t/new-mastodon-service-for-the-ignite-realtime-community/92389)
- [The community started a call for help with translating Spark and Openfire](https://discourse.igniterealtime.org/t/help-us-translate-spark-and-openfire/92399)

### Servers

[ejabberd 23.01 has been released](https://www.process-one.net/blog/ejabberd-23-01/). Almost three months after the previous release, ejabberd 23.01 includes many bug fixes, several improvements and some new features. A new module, mod_mqtt_bridge, can be used to replicate changes to MQTT topics between local and remote servers. Supported XEPs are now automatically gathered from source code documentation in order to provide a DOAP file for further processing on [xmpp.org/servers/ejabberd](https://xmpp.org/software/servers/ejabberd/).

[Prosody 0.12.2](https://blog.prosody.im/prosody-0.12.2-released/) and [Prosody 0.11.14](https://blog.prosody.im/prosody-0.11.14-released/) have been released. The 0.12 release brings bug fixes and improvements.

[Tigase XMPP Server 8.3 has been released](https://tigase.org/blog/tigase-xmpp-server-8.3.0/). It includes Tigase MEET - Tigase's take at SFU (Selective Forwarding Unit) group video-calls, support for XEP-0440 SASL Channel Binding Type Capability as well as initial, preview support for SASL2 and Bind2 and lots of usual fixes.

### Libraries & Tools

[omemo_dart](https://github.com/PapaTutuWawa/omemo_dart) is a Dart library to help developers of Dart/Flutter XMPP clients to implement OMEMO in its newest version - currently 0.8.3. It has been released in version 0.4.2.

[python-nbxmpp 4.0.0 to 4.1.0 have been released](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog). These versions bring support for Message Reactions (XEP-0444) and port the library to libsoup3.

A new tool for server operators and developers has arrived: [nbxmpp-client](https://pypi.org/project/nbxmpp-client/) lets you check and test various XMPP connection methods (and proxy configurations) while having an eye on the protocol's XML stream. Version 2.0.0 has just been released and comes with a fresh design (Gtk4+libadwaita).

[Slidge 0.1.0 RC1 has been released](https://www.nicoco.fr/blog/2023/01/08/slidge-rc1/). Slidge is a collection of XMPP gateway components that lets you use your favorite XMPP client(s) to chat with other, non-XMPP and/or non-federated chat networks (i.e. WhatsApp, Facebook, Mattermost, Signal, Skype, Steam, Telegram).

Daniel Gultsch's [compliance.conversations.im](https://compliance.conversations.im/) [will be discontinued](https://gultsch.social/@daniel/109653873511471850). This online compliance checker allowed server administrators and users to identify the XEPs/features supported by a provider, and it also allowed to check XEP support over time. This service helped users to check whether they are creating a future-proof account with a provider. Due to difficulties in maintaining the software, the service will be shut down in the near future.

[QXmpp 1.5](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.0) has been released! The Qt-/C++-based XMPP library supports OMEMO 2, Stanza Content Encryption and Automatic Trust Management now. Much more data than with the old OMEMO versions can be end-to-end encrypted. For example, files including thumbnails are shared encrypted via Stateless File Sharing. Furthermore, Message Reactions is supported and QXmpp's PubSub implementation is almost feature-complete.

## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to 
accept this proposal as an Experimental XEP.

- [XMPP Compliance Suites 2023](https://xmpp.org/extensions/inbox/cs-2023.html)
  - This document defines XMPP application categories for different use cases (Core, Web, IM, and Mobile), and specifies the required XEPs that client and server software needs to implement for compliance with the use cases.
- [Stream Limits Advertisement](https://xmpp.org/extensions/inbox/xep-sla.html)
  - This specification defines a way for an XMPP entity to announce the limits it will enforce for data received on a stream.

### New

- [Version 0.1.0 of XEP-0477 (Pubsub Targeted Encryption)](https://xmpp.org/extensions/xep-0477.html)
  - Accepted by vote of Council on 2022-11-30. (XEP Editor (jsc))
- [Version 0.1.0 of XEP-0476 (Pubsub Signing: OpenPGP Profile)](https://xmpp.org/extensions/xep-0476.html)
  - Accepted by vote of Council on 2022-11-30. (XEP Editor (jsc))
- [Version 0.1.0 of XEP-0475 (Pubsub Signing)](https://xmpp.org/extensions/xep-0475.html)
  - Accepted by vote of Council on 2022-11-30. (XEP Editor (jsc))
- [Version 0.1.0 of XEP-0471 (Events)](https://xmpp.org/extensions/xep-0471.html)
  - Accepted by vote of Council on 2022-09-28. (XEP Editor (jsc))
- [Version 0.1.0 of XEP-0474 (SASL SCRAM Downgrade Protection)](https://xmpp.org/extensions/xep-0474.html)
  - Accepted by vote of Council on 2022-10-19. (XEP Editor (jsc))
- [Version 0.1.0 of XEP-0473 (OpenPGP for XMPP Pubsub)](https://xmpp.org/extensions/xep-0473.html)
  - Accepted by vote of Council on 2022-10-19. (XEP Editor (jsc))
- [Version 0.1.0 of XEP-0472 (PubSub Social Feed)](https://xmpp.org/extensions/xep-0472.html)
  - Accepted by vote of Council on 2022-10-19. (XEP Editor (jsc))
  
### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it 
will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- [Version 0.2.0 of XEP-0474 (SASL SCRAM Downgrade Protection)](https://xmpp.org/extensions/xep-0474.html)
  - Add description of attack model
  - Add section defining IETF interaction (tm)
- [Version 0.2.0 of XEP-0461 (Message Replies)](https://xmpp.org/extensions/xep-0461.html)
  - Fix example character counting. Add disco feature. Relax the 'to' attribute constraints. (nc)
- [Version 0.1.1 of XEP-0444 (Message Reactions)](https://xmpp.org/extensions/xep-0444.html)
  - Add the XML Schema (egp)
- [Version 0.3.0 of XEP-0426 (Character counting in message bodies)](https://xmpp.org/extensions/xep-0426.html)
  - Added section about subsequences. (lmw)
- [Version 0.5.0 of XEP-0353 (Jingle Message Initiation)](https://xmpp.org/extensions/xep-0353.html)
  - Recommend usage of UUID v4 for id attributes. (tm)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- No XEP moved to stable this month.
  
### Deprecated

- No XEP deprecated this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Spread the news!

Please share the news on other networks:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [Twitter](https://twitter.com/xmpp)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Lemmy instance](https://community.xmpp.net/)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **Alexander "PapaTutuWawa", emus, Licaon_Kter, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), wurstsalat, Zash** 
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, Pierre Jarillon, Ppjet6, Ysabeau**
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
  - Translators: **Jeybe, wh0nix**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu/)
  - Translators: **nicfab**
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Translators: **daimonduff, TheCoffeMaker**

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations
- communication via media accounts

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
