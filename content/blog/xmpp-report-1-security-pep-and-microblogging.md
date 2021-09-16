---
title: XMPP Roundup 1
date: 2008-09-16
author: admin
categories: ["XMPP Roundup"]
aliases:
    - "/2008/09/xmpp-roundup-1/"
---

Welcome to the first installment of what we hope will be a continuing series of reports on XMPP technologies and the XMPP community (you can think of this series is a replacement for the old [Jabber Journal](http://www.saint-andre.com/jabber/journal/)). This report is authored by [Peter Saint-Andre](http://stpeter.im/), [Florian Jensen](http://florianjensen.com/), and [Jack Moffitt](http://metajack.im/). Future reports might involve different authors just to keep things interesting; let us know if you'd like to help.

### Secure Communications Week

The first [Secure Communications Week](http://www.jabber.org/web/Secure_Communications_Week) is coming soon: October 4-11, 2008. For an entire week all participating XMPP-based IM services, led by the jabber.org IM team, will require channel encryption (SSL / TLS) for stronger security. During the first week, we will focus on client-to-server encryption, but in future weeks, participating servers may also test encryption of server-to-server connections.

Why are we doing this? Isn't this just annoying for people whose IM clients don't support SSL/TLS? There are two reasons:

1.  Privacy matters. The Internet isn't a secure place, and we think it's in your interest to keep IM conversations private. By using SSL or TLS encryption, you ensure that everything sent through Jabber is encrypted and unreadable by a "man in the middle". As a result, only your server and the person you chat with can read your messages.
2.  Many of the volunteers and organizations who run IM services on the federated XMPP network are aiming to require encryption of all traffic on the network. Therefore, we plan to hold real-life security tests on the network over the next few months, with the goal of requiring encryption among some of the existing IM services in time for the 10th anniversary of Jabber on January 4, 2009.

IM users can prepare for Secure Communications Week by making sure that they have an [up-to-date IM client](http://www.jabber.org/web/Secure_Communications_Week#How_Can_End_Users_Prepare.3F). If you notice that you can't log on to your server, you can find help on the [Jabber Community Forums](http://www.jabber.org/web/JabberWiki:Community_Portal "Jabber Community").

Have a secure week! :)

### Jabber.org Gets Peppy

The [Personal Eventing Protocol](https://xmpp.org/extensions/xep-0163.html), also known as PEP, is the next-generation transport for advertising [moods](https://xmpp.org/extensions/xep-0107.html), [activities](https://xmpp.org/extensions/xep-0108.html), [geolocation](https://xmpp.org/extensions/xep-0080.html), [music tunes](https://xmpp.org/extensions/xep-0118.html), [microblogging](https://xmpp.org/extensions/inbox/microblogging.html), and more. It turns each user's IM account into a flexible publish-subscribe service. The XMPP community has been working on these technologies for several years, and now they are mature enough for deployment by large IM service providers like jabber.org.

How do you get it?

The good thing is, you probably don't need to do anything! Recent releases of popular Jabber clients like [Psi](http://psi-im.org), [Gajim](http://www.gajim.org/), and [Coccinella](http://coccinella.im) support PEP, so you don't need to download anything new to use this feature. You will automatically see new options like "Publish Tune" appear in your client interface.

![Publishing a Tune in Psi](http://stage.xmpp.org/wp-content/uploads/2008/09/publish-tune.png "publish-tune")

### Community Discussions

The Jabber/XMPP community has a large number of communication venues -- multiple email lists, chat rooms, web forums, blogs, microblogs, wikis, and project websites. It is difficult for any one person to keep track of all these conversations, and it gets harder all the time. In the XMPP Report we'll try to summarize those discussion threads so you don't have to read them all.

One of the hot topics right now is the integration of XMPP into microblogging services like [Twitter](http://twitter.com/), [Jaiku](http://jaiku.com/), [identi.ca](http://identi.ca/), and [Yammer](http://yammer.com/). Many of these services are turning to XMPP for two reasons.  First, it's natural to offer an XMPP interface into microblogging streams because the conversation between participants happens in real time, and also because XMPP's push mechanisms like the core message stanza and advanced [publish-subscribe extension](https://xmpp.org/tech/pubsub.shtml) can save such services from the heavy load of HTTP polling.

Last week, several members of the XMPP community participated in [BearHugCamp](http://microblog.org/wiki/BearHugCamp) in San Francisco along with others from the microblogging community.  Jack Moffitt provides some background [here](http://metajack.im/2008/09/10/xmpp-microblogging-thoughts/) and a report on the conference [here](http://metajack.im/2008/09/13/bearhugcamp-for-those-who-missed-it/). Expect more discussion about this in the coming weeks and months, especially on the [social@xmpp.org](https://mail.jabber.org/mailman/listinfo/social) email list.

Well, that's it for this report. We'll try to write another one soon!
