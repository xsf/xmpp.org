---
title: The XMPP Newsletter, 1 June 2018
date: 2018-06-01
author: jcbrand
categories: ["Newsletter"]
aliases:
  - "/2018/06/the-xmpp-newsletter-1-june-2018/"
---

Welcome to another edition of the XMPP newsletter.

## News

The next release of [Salut à Toi will include file sharing](https://www.goffi.org/b/hGKs6B4wd8dsgNZd5MzQjN/file-sharing-landing-next-release-salut?utm_source=xmppnewsletter).
Sharing files directly between two users has been possible before, but now it's
possible to share a file hierarchy, or in other words one or several
directories. To share with someone, just use their XMPP address (JID).

[Christopher Muclumbus](https://muclumbus.jabbercat.org) 
is a new project to publicly list XMPP chat rooms.
It provides a web interface with full-text search for room names, descriptions
and addresses. Only rooms which are configured to be publicly listed are shown.

{{< newsletter-subscribe >}}

Blazemeter have written about [5 ways to load test chat plugins with JMeter](https://www.blazemeter.com/blog/5-ways-to-load-test-popular-chat-plugins-with-jmeter?utm_campaign=Blog%20Post%20-%205%20Ways%20to%20Load%20Test%20Popular%20Chat%20Plugins%20with%20JMeter?utm_source=xmppnewsletter).
JMeter is an open source Java application designed to load test functional behavior and measure performance.
The article briefly discusses XMPP and mentions that JMeter has a plugin which
provides support for XMPP.

[Fanout has removed XMPP support](http://blog.fanout.io/2018/05/18/goodbye-xmpp/?utm_source=xmppnewsletter) from their cloud offering.
It was never used at scale, and was mainly relegated to chat bots that needed
compatibility with Google Talk. However, as Google phased out XMPP federation,
such usefulness dwindled.

JC Brand wrote a [blogpost about the Gulaschprogrammiernacht](https://opkode.com/blog/2018-gulaschprogrammiernacht/)
a hacker/maker event in Karlsruhe, where six people worked on XMPP-related projects and plans
where hatched to organize a sprint in Cambridge.

### Google Summer of Code Projects

Paul Schaub has been [blogging regularly in May](https://blogs.fsfe.org/vanitasvitae/2018/05/?utm_source=xmppnewsletter)
about his Google Summer of Code project, adding OpenPGP support for SMACK
([XEP-0373](https://xmpp.org/extensions/xep-0373.html) and [XEP-0374](https://xmpp.org/extensions/xep-0374.html)).

Rishi Raj wrote a blogpost about their GSoC project, an [XMPP Compliance Tester](https://rishiraj22.github.io/articles/2018-05/gsoc-project).

### Events

An XMPP sprint is being organized for August in Cambridge.
The event will take place in the Collabora offices and dates are still to be
finalized. You still have a chance to vote for your preferred date and to suggest
topics for the sprint. Visit [https://col.la/xmppsprint](https://col.la/xmppsprint)
and join the groupchat [xmpp-sprint@chat.cluxia.eu](xmpp:xmpp-sprint@chat.cluxia.eu?join).

### GDPR

On 25th May the European Union's "General Data Protection Regulation" has come
into force.

The GDPR has had some people spooked, for example, in an alarmist
post [Monal has announcing its withdrawal from the EU](https://monal.im/blog/gdpr-removing-monal-from-the-eu/).

The XMPP community has been discussing the GDPR's impact and have come up
with various ideas and strategies on how to ensure compliance.

Discussions happened regularly in the [xsf@muc.xmpp.org](xmpp:xsf@muc.xmpp.org?join) groupchat.

There is a [GDPR page on the XMPP wiki](https://wiki.xmpp.org/web/GDPR) which
collects and summarises the results of these discussions.

Winfried Tilanus, who's been active in these discussions, created a new
proto-XEP: [Best practices for GDPR compliant deployment of XMPP](https://xmpp.org/extensions/inbox/gdpr.html)



## Software releases

### Servers

* [Prosody 0.9.13](http://blog.prosody.im/prosody-0-9-13-released/?utm_source=xmppnewsletter):
  A maintenance release to the old stable 0.9 branch, with many bug fixes, including some important security improvements.
  And then more recently [0.9.14](https://prosody.im/doc/release/0.9.14), which
  fixes a [privilege escalation security issue]((https://issues.prosody.im/1147).

* [Prosody 0.10.1](http://blog.prosody.im/prosody-0-10-1-released/?utm_source=xmppnewsletter) and then [0.10.2](https://prosody.im/doc/release/0.10.2):
  which fixes a [privilege escalation security issue](https://issues.prosody.im/1147).

* [OpenFire 4.2.3](https://discourse.igniterealtime.org/t/openfire-4-2-3-release/8112?utm_source=xmppnewsletter")
  This release fixes a regression which made it impossible to update plugins from the admin console.

* [Metronome 3.8.27](https://metronome.im/news/3-8-27-maintenance-release?utm_source=xmppnewsletter)

* [Conversations Push Proxy](https://github.com/iNPUTmice/p2), 
  An XEP-0357: Push Notifications app server that relays push messages between
  the user’s server and Googles Firebase Cloud Messaging.

### Clients

* [Escalus 4.0.0](https://www.erlang-solutions.com/blog/escalus-4-0-0-faster-and-more-extensive-xmpp-testing.html?utm_source=xmppnewsletter):
  originally created as a tool to test XMPP servers, it can also be used as a standalone Erlang application.
  Changes include a new XML viewer, a new XML parser and stanza pipelining.

* [Monal iOS 3.0.0](https://monal.im/blog/monal-ios-3-released?utm_source=xmppnewsletter) and then [3.0.1](https://monal.im/blog/ios-3-0-1-released-how-is-push?utm_source=xmppnewsletter),
  have been released. The major release adds support for push notifications, a new UI layout, iPhone X support,
  multi-user chat improvements, conversation synchronization and more.

* [Monal Mac 2.1.1](https://monal.im/blog/mac-2-1-1-out/?utm_source=xmppnewsletter)

### Libraries

* [Smack 4.3.0-beta2](https://discourse.igniterealtime.org/t/smack-4-3-0-beta2-released/81680?utm_source=xmppnewsletter):
  This release marks an important milestone in Smack’s development cycle as the ‘4.3’
  branch was created, which means  there are no major API changes to be expected. 

* [Strophe.js 1.2.15](https://github.com/strophe/strophejs/releases/tag/v1.2.15)
