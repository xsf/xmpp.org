---
title: The XMPP Newsletter November 2022
date: 2022-12-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of November 2022. This is the final release for this year and we will have a well-deserved winter break until the 5th of February 2023! Many thanks to all readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **emus, Licaon_Kter, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), wurstsalat, Zash** 
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, Pierre Jarillon, Ppjet6, Ysabeau**
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
  - Translators: **Jeybe, wh0nix**
- Italian: [nicfab.it](https://www.nicfab.it/)
  - Translators: **nicfab**
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Translators: **daimonduff, TheCoffeMaker**

## XSF Announcements

- The XSF membership application period for the fourth quarter 2022 has ended. Voting results will be [announced on Dec 13th](https://wiki.xmpp.org/web/Membership_Applications_Q4_2022).

### Google Summer of Code 2022

{{< figure src="/images/logos/GSoC_2022_Logo.png" caption="XSF and Google Summer of Code 2022" >}}

The Google Summer of Code 2022 has finished! The two new contributors Patiga and PawBud worked on open-source software projects in the XMPP environment. Read the final collection blog posts:
  - **Patiga** works on [more flexible file transfers in Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ). Mentors are **fiaxh** and **Marvin W.**.
    - [Stateless File Sharing GSoC project](https://dino.im/blog/2022/06/stateless-file-sharing-gsoc-project/)
    - [Project Stateless File Sharing: First Steps](https://dino.im/blog/2022/06/project-stateless-file-sharing-first-steps/)
    - [Stateless File Sharing: Base implementation](https://dino.im/blog/2022/08/stateless-file-sharing-base-implementation/)
    - [Stateless File Sharing: Sources and Compatibility](https://dino.im/blog/2022/08/stateless-file-sharing-sources-and-compatibility/)
    - [Stateless File Sharing: Source Attachment and Wrap-Up](https://dino.im/blog/2022/11/stateless-file-sharing-source-attachment-and-wrap-up/)
  - **PawBud** works towards [adding support for A/V communication via Jingle in ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19). Mentors are **JC Brand** and **vanitasvitae**.
    - [On-Boarding Experience with XSF (Converse)](https://xmpp.org/2022/06/on-boarding-experience-with-xsf-converse/)
    - [ConverseJS: An in-depth view into my GSoC'22 project!](https://xmpp.org/2022/07/conversejs-an-in-depth-view-into-my-gsoc22-project/)
    - [Google Summer of Code 2022 at XSF: Converse.js - Mid Term Evaluation Update](https://xmpp.org/2022/08/google-summer-of-code-2022-at-xsf-converse.js-mid-term-evaluation-update/)

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

All outstanding Google Summer of Code articles are now complete and have been published. See above ^

From the JMP blog, an article about [building an XMPP client from scratch](http://blog.jmp.chat/b/2022-chat-client-from-scratch), including worked examples of implementing many XEPs. Read also their [Newsletter: New Cheogram Android Release, Chatwoot Instance](https://blog.jmp.chat/b/october-newsletter-2022)

[ejabberd turns 20!](https://www.process-one.net/blog/ejabberd-turns-20/) Congratulations and many thanks to all who contributed to this great project!

{{< figure src="/images/newsletter/2022-12-05/ejabberdturns20.png" caption="ejabberd turns 20" >}}

IT-Business writes about the most important internet protocols - [XMPP is part of it](https://www.it-business.de/iot-protokolle-und-standards-a-0de446b7b0d72c123fb1e2dce23dce0f/) [DE]! 

Read about [how Libervia bridges XMPP and ActivityPub](https://www.goffi.org/b/libervia-progress-note-2022-w45-MTdL) as the gateway developed by Goffi _(thanks to a NLnet/NGI0 grant)_ hit alpha state. Also announced is OMEMO:2 support, for messages, files, file transfers via Jingle and all Pubsub related features.

## Software news

### Clients and applications

Conversations 3.0 has been announced and is being [supported by the NLnet foundation](https://nlnet.nl/project/Conversations-3.0/)

[Gajim 1.5.4](https://gajim.org/post/2022-12-03-gajim-1.5.4-released/) has been released, and it comes with a reworked file transfer interface, better URL detection, message selection improvements, and many fixes under the hood.

{{< figure src="/images/newsletter/2022-12-05/gajim-file-transfer-interface.png" caption="New Gajim file transfer interface" >}}

[Spark 3.0.0](https://discourse.igniterealtime.org/t/spark-3-0-0-released/92231) has been released with a new look and includes the Pade Meetings plugin for audio and video calls via Jitsi Meet.

### Servers

[Openfire 4.7.4](https://discourse.igniterealtime.org/t/openfire-4-7-4-release/92225) has been released, and it includes enhancements to cluster-specific 
implementation of Multi-User Chat functionality, improved websocket handling and improved statistics. Furthermore from the ignite realtime community:
- [Openfire Monitoring Service plugin 2.4.0 released](https://discourse.igniterealtime.org/t/openfire-monitoring-service-plugin-2-4-0-release/92266)
- [Hazelcast plugin version 2.6.1 released](https://discourse.igniterealtime.org/t/hazelcast-plugin-version-2-6-1-released/92224)
- [REST API Openfire plugin 1.10.1 released](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-10-1-released/92223)
- [HTTP File Upload plugin 1.2.0 released](https://discourse.igniterealtime.org/t/http-file-upload-plugin-1-2-0-released/92302)
- [Denial of Service Vulnerability in Smack 4.4 if XMPPTCPConnection is used with StAX](https://discourse.igniterealtime.org/t/denial-of-service-vulnerability-in-smack-4-4-if-xmpptcpconnection-is-used-with-stax/92314)

As mentioned in the [October 2022 Newsletter](https://xmpp.org/2022/11/the-xmpp-newsletter-october-2022/#articles) more info on the SASL2 related work starts to appear. The Prosody server developers talk about [Bringing FASTer authentication to Prosody and XMPP](https://blog.prosody.im/fast-auth/) and how "tokens" are the answer.

### Libraries & Tools

[python-omemo 1.0.2](https://github.com/Syndace/python-omemo) has [been released](https://mail.jabber.org/pipermail/jdev/2022-November/090468.html) with support for the new [SCE](https://xmpp.org/extensions/xep-0420.html)-based OMEMO. Interesting enough the Libervia progress above is based on this work.

And OMEMO news in the Go corner too, [Mellium to receive grant for end-to-end encryption](https://opencollective.com/mellium/updates/mellium-to-receive-grant-for-end-to-end-encryption) from the NGI Assure Fund.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

xmpp.org features [a page about XMPP RFCs](https://xmpp.org/rfcs/) as well.

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to 
accept this proposal as an Experimental XEP.

- [PubSub Social Feed](https://xmpp.org/extensions/inbox/pubsub-social-feed.html)
  - This specification defines a way of publishing social content over XMPP.
- [SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/inbox/xep-downgrade-prevention.html)
  - This specification provides a way to secure the SASL and SASL2 handshakes against method and channel-binding downgrades.
- [OpenPGP for XMPP Pubsub](https://xmpp.org/extensions/inbox/pubsub-encryption.html)
  - Specifies an OpenPGP for XMPP (XEP-0373) profile for the pubsub use case.

### New

- No new XEP this month.
  
### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it 
will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- No XEPs updated this month.

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

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

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
