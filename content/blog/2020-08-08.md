---
title: XMPP brews coffee!
date: 2020-08-08
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/08/newsletter-08-august/"
---

Welcome to the XMPP newsletter covering the month of August 2020.

### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news/jabberfr.org/category/newsletter/)


## Articles

Lorenz Kästle wrote an article (in German and English) on [how to setup an Icinga 2 notification system using python3-slixmpp](https://www.netways.de/blog/2020/08/28/zurueck-in-die-zukunft-icinga2-benachrichtigungen-mit-xmpp/) ([reposity on Github](https://github.com/RincewindsHat/icinga2_xmpp-notifications)).

## Software news

### Clients and applications

The multi-platform desktop client [Gajim 1.2.2 has been released](https://gajim.org/post/2020-08-15-gajim-1.2.2-released/). It brings an automatic weekly update check for Gajim on Windows and MacOS, a big status message overhaul, and many improvements. [More development news from August](https://gajim.org/post/2020-08-30-development-news-august/): The settings backend received an upgrade to migrate from text files to SQLite based storage, and a lot of code has been cleaned up, which should make it easier for you to handle all of Gajim’s configuration possiblities.

The iOS and macOS client Monal is now managing translations on [Weblate](https://hosted.weblate.org/engage/monal/). 27 languages are waiting for excellent and native speakers! Please also check out the current [Monal Beta 4.7.0](https://github.com/anurodhp/Monal/releases/tag/Build_iOS_636) and get ready for the upcoming release!

There have been UI and file sharing improvements on the "[Salut à Toi](https://salut-a-toi.org/)" project:

- Libervia, the web frontend, has seen a major UI revamp, with a new theme based on Bulma CSS framework. The [W31 progress note](https://www.goffi.org/b/n9nzn3ySF7Lv4pYBpTqYtP/progress-note) also explains how the templating engine Nunjucks is used in the browser to use the same templates as in the Jinja 2 based backend.  

- The file sharing component included in SàT now implements [XEP-0363](https://xmpp.org/extensions/xep-0363.html) (HTTP File Upload), which completes the [XEP-0234](https://xmpp.org/extensions/xep-0234.html) (Jingle File Transfer) method. Files uploaded to this component from any XMPP client will appear in SàT's file sharing UI, and can be deleted from there or with [XEP-0050](https://xmpp.org/extensions/xep-0050.html) (Ad-Hoc Commands).  

- Libervia photo album has been greatly improved with a mobile and desktop friendly slideshow, easy way to upload files from browser, and integration of videos. Work is currently in progress to make SàT/Libervia a good fit for an XMPP based familial social network, with a release expected around the end of September or beginning of October.  

![SàT Libervia photo album](/images/newsletter/august2020/SaT.png "SàT Libervia photo album") 



The Android client aTalk 2.4.0 has been released. [Changes](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt) are mainly internal with several libraries upgrades and compilation fixes. It was followed by version 2.4.1 which fixes an Android Q specific storage issue.

The desktop client [Dino received a NGI0 PET Fund](https://dino.im/blog/2020/08/setting-out-for-calls-and-conferences/) managed by NLnet which receives financial support from the European Commission’s Next Generation Internet program. This allows the developers to dedicate time and efforts to implement video and audio calls into their client. This is really great news!

The multi-platform client [Kaidan 0.6.0 has been released](https://www.kaidan.im/2020/08/20/kaidan-0.6.0/). The update includes stability fixes, a new offline message queue, and improved message correction. Furthermore, the upstream HTTP File Upload implementation of its XMPP library [QXmpp](https://github.com/qxmpp-project/qxmpp) is used now.

![Kaidan offline message queue](/images/newsletter/august2020/kaidan060.gif "Kaidan offline message queue") 

Spark, the multi-platform client from the Ignite RealTime community, has released its long overdue [version 2.9.0](https://discourse.igniterealtime.org/t/spark-2-9-0-released/88551), with improvement in certificates management, and additional file transfer methods. It was followed by 2.9.1 and 2.9.2. Go ahead and check the [changelog](http://download.igniterealtime.org/spark/docs/latest/changelog.html) for the numerous bug fixes and improvements.

## Servers

The java based Tigase XMPP Server [is now available as a Docker image](https://tigase.net/tigase-meets-docker/) to facilitate its deployment on your server.

The Ignite Realtime community XMPP server, Openfire, has a [new plugin](https://discourse.igniterealtime.org/t/jsxc-web-client-now-available-as-a-plugin-for-openfire/88467)  to make the JSXC web client available to its users.

## Libraries

The Ignite RealTime community modular XMPP client library Smack has [had its first beta release](https://discourse.igniterealtime.org/t/smack-4-4-0-beta1-released/88519) for the upcoming release of Smack version 4.4! The [list of changes](https://github.com/igniterealtime/Smack/wiki/Smack-4.4-Readme-and-Upgrade-Guide) ranges from a new modular transport API which makes it easy to swap the underlying transport mechanism of an XMPP connection during runtime, to added support for [XEP-0373](https://xmpp.org/extensions/xep-0373.html) (OpenPGP for XMPP), [XEP-0424](https://xmpp.org/extensions/xep-0424.html) (Message Retraction), and about a dozen other specifications. As usual, it's available on Maven Central.

python-nbxmpp, the library powering Gajim, had it’s [1.0.2 release](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/nbxmpp-1.0.2). The latest version contains some domain mapping improvements and fixes network issues which occured under certain circumstances after suspending the device.

## Other

Want a coffee with a taste of XMPP? Over the past months [COM8](https://github.com/com8) has been working on creating a [reference implementation](https://github.com/COM8/esp32-jura) for his new XMPPIoT protocol. A first rather basic draft has been published in his [B.Sc. Thesis](https://home.in.tum.de/~sauterf/html-data/Thesis_Smart_Building_Control_with_XMPP_for_IoT.pdf). Using the Windows 10 [UWP](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide) XMPP client [UWPX](https://uwpx.org), it is possible to register a JURA coffee maker as a new IoT device. This allows sending and receiving commands from and to it, using an [ESP32](https://www.espressif.com/en/products/socs/esp32) from Espressif (low-power and low-cost system on a chip microcontroller). The ESP32 functions as a proxy between XMPP and the proprietary JURA protocol. A video of the working prototype [can be found on Twitter](https://twitter.com/UWPX_APP/status/1293461429677436931?s=20).

![XMPP brews coffee](/images/newsletter/august2020/XMPPcoffee.png "XMPP brews coffee") 


## Google Summer of Code

Since the beginning of May students all over the world are working on many open-source projects within the Google Summer of Code Season 2020. We would like to introduce the students who work on [GSoC XMPP projects](https://summerofcode.withgoogle.com/organizations/5474262808264704/#6018598289539072) and share their blog posts:

[Aditya Borikar](https://adiaholic.github.io/gsoc2020/2020/05/16/Chapter-0-Introduction.html) is working on WebSocket support for Smack. Blog history: 

- [Chapter 1: Handshake](https://adiaholic.github.io/gsoc2020/2020/05/24/Chapter-1-Handshake.html)  
- [Chapter 2: Modular Shift](https://adiaholic.github.io/gsoc2020/2020/05/31/Chapter-2-Modular-Shift.html)  
- [Chapter 3: SASL Negotiations](https://adiaholic.github.io/gsoc2020/2020/06/07/Chapter-3-sasl-negotiations.html)  
- [Chapter 4: Fixing loose endpoints](https://adiaholic.github.io/gsoc2020/2020/06/14/Chapter-4-fix-loose-endpoints.html)  
- [Chapter 5: Discrete Http Lookup Method](https://adiaholic.github.io/gsoc2020/2020/06/21/Chapter-5-Discrete-Http-Lookup-Method.html)  
- [Chapter 6: A Part Of The Whole, Merged](https://adiaholic.github.io/gsoc2020/2020/06/28/Chapter-6-Part-Of-The-Whole.html)  
- [Chapter 7: The Bigger Picture](https://adiaholic.github.io/gsoc2020/2020/07/06/Chapter-7-The-Bigger-Picture.html)  
- [Chapter 8: Reworking FSM](https://adiaholic.github.io/gsoc2020/2020/07/12/Chapter-8-Reworking-FSM.html)  
- [Chapter 9: Bug Fixation](https://adiaholic.github.io/gsoc2020/2020/07/19/Chapter-9-Fixing-Bugs.html)  
- [Chapter 10: End of the second phase](https://adiaholic.github.io/gsoc2020/2020/07/26/Chapter-10-End-of-second-phase.html)  
- [Chapter 11: TLS - The Last Stage](https://adiaholic.github.io/gsoc2020/2020/08/02/Chapter-11-TLS.html)  
- [Chapter 12: Titbits](https://adiaholic.github.io/gsoc2020/2020/08/09/Chapter-12-Titbits.html)  
- [Chapter 13: Testing](https://adiaholic.github.io/gsoc2020/2020/08/16/Chapter-13-Testing.html)  
- [Chapter 14: Final Stage](https://adiaholic.github.io/gsoc2020/2020/08/23/Chapter-14-Final-Stages.html)  

[Anmol (wolfie_anmol)](https://wolfieanmol.github.io/gsoc-blog/) is working on implementing Real Time Texting ([XEP-0301](https://xmpp.org/extensions/xep-0301.html)) in Dino. Blog history:

- [GSoC 2020 begins - Introduction to RTT](https://wolfieanmol.github.io/gsoc-blog/introduction/)  
- [RTT stanza and message comparision](https://wolfieanmol.github.io/gsoc-blog/rtt-stanza-and-message-comparision/)  
- [Receiving Real Time Texts](https://wolfieanmol.github.io/gsoc-blog/receiving-rtt/)  
- [User Interface](https://wolfieanmol.github.io/gsoc-blog/ui/)  
- [Settings to Enable/Disable RTT](https://wolfieanmol.github.io/gsoc-blog/settings/)  
- [Settings Radio Button Menu](https://wolfieanmol.github.io/gsoc-blog/settings-radio-button-menu/)  
- [Realistic RTT with wait](https://wolfieanmol.github.io/gsoc-blog/realistic-rtt-with-wait/)  
- [Support for Multiple Devices and MUCs](https://wolfieanmol.github.io/gsoc-blog/support-for-multiple-devices-muc/)  

Thank you for joining GSoC XMPP projects and keep up the good work! These last posts mark the end of 2020’s Google Summer of Code. Thanks to all participants within the XMPP community for their great work. Stay safe and stay connnected with XMPP!


## Extensions and specifications

Read more about the [standards process](https://xmpp.org/about/standards-process.html).

### New

- [XEP-0442](https://xmpp.org/extensions/xep-0442.html) (Pubsub Message Archive Management)  
  - This document defines a protocol to query and control a pubsub node's message archive. (Accepted by vote of Council on 2020-08-19)

- [XEP-0441](https://xmpp.org/extensions/xep-0441.html) (Message Archive Management Preferences)  
  - This document defines a protocol to control a user's archiving preferences. (Accepted by vote of Council on 2020-08-19)

### Updated

- Version 1.19.0 of [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish Subscribe)  
  - Add missing 'item' key and 'retrieve' action to query type registry.

- Version 1.2 of [XEP-0178](https://xmpp.org/extensions/xep-0178.html) (Best Practices for Use of SASL EXTERNAL with Certificates)  
  - Add fallback to dialback if EXTERNAL authentication fails due to practical experience

- Version 1.33.0 of [XEP-0045](https://xmpp.org/extensions/xep-0045.html) (Multi-User Chat)  
  - Clarify that the 307 status code should not be used alongside 333 for user disconnects

- Version 0.2.0 of [XEP-0440](https://xmpp.org/extensions/xep-0440.html) (SASL Channel-Binding Type Capability)  
  - Discuss interaction with SASL mechanism and add security considerations  
  - Recommend implementation of tls-server-end-point  

- Version 1.2 of [XEP-0048](https://xmpp.org/extensions/xep-0048.html) (Bookmarks)  
  - Deprecate in favour of [XEP-0402](https://xmpp.org/extensions/xep-0402.html) (PEP Native Bookmarks)  

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedbacks gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

- [XEP-0352](https://xmpp.org/extensions/xep-0352.html) (Client State Indication)  
- [XEP-0411](https://xmpp.org/extensions/xep-0411.html) (Bookmarks Conversion)  

### Proposed Extensions

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

- [Pubsub Message Archive Management](https://xmpp.org/extensions/inbox/xep-pubsub-mam.html)  
  - This document defines a protocol to query and control a pubsub node's message archive.

- [Message Archive Management Preferences](https://xmpp.org/extensions/inbox/xep-mam-prefs.html)  
  - This document defines a protocol to control a user's archiving preferences.

## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to COM8, emus, jcbrand, jerome-poisson, jonas', Licaon_Kter, melvo, pmaziere, SeveFP, vanitasvitae, wurstsalat, Zash for their help in creating it!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

## Subscribe to the newsletter

We suggest you to [subscribe to receive the next editions](https://xmpp.org/newsletter.html) in your inbox as soon as they are published! 
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
