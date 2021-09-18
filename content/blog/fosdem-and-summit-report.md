---
title: FOSDEM and Summit Report
date: 2010-02-10
author: stpeter
categories: ["XMPP Summit"]
---

The XSF held another successful [XMPP Summit](/2010/08/xmpp-summit-8) over the weekend at [FOSDEM 2010](http://fosdem.org/2010/) in Brussels, Belgium. Many thanks to the companies who sponsored this event: [Nokia](http://www.nokia.com/), [Vodafone](http://www.vodafone.com), [Collabora](http://collabora.co.uk/), [Isode](http://www.isode.com/), [TANDBERG](http://www.tandberg.com/), [Buddycloud](http://www.buddycloud.com/), [Collecta](http://collecta.com/), and [Ooros](http://www.ooros.com/). Special thanks to Nokia for temporarily donating some N900 devices for the Developer Challenge, and to [Mobile Vikings](http://mobilevikings.com/) for the SIM cards that enabled a number of XMPP developers to experiment with building mobile applications at the conference. And extra special thanks to XSF Board member Florian Jensen for his hard work on local coordination (as well as the photos in this blog post).

The weekend events started with a "hackfest" on Friday where developers could work together on code projects, perform interoperability testing, and give informal talks on technical topics.

On Saturday we had a "devroom" at FOSDEM 2010, which was packed the entire afternoon.

![](/images/summit8-devroom.jpg)

One of the most popular sessions was "Stump the XMPP Experts" with XMPP book authors and the current [XMPP Council](/about/xmpp-standards-foundation#council) (left to right, the experts were Kevin Smith, Ralph Meijer, Remko Tronçon, Matthew Wild, Jack Moffitt, Dave Cridland, and Peter Saint-Andre).

![](/images/summit8-stump.jpg)

The talks ranged from fun demos to technical explorations of XMPP technologies. Here Ralph Meijer illustrates the use of Atom feeds over XMPP pubsub (photo by Dan Brickley).

![](/images/summit8-ralphm.jpg)

Other speakers included the winners of the XMPP developer challenge, Frank Scholz and Philippe Normand, who gave a talk about their [Mirabeau](http://coherence.beebits.net/wiki/MirabeauHowTo) application for personal media networks.

![](/images/summit8-mirabeau.jpg)

On both Saturday and Sunday the XSF had a booth at FOSDEM, which was the center of many ad-hoc discussions.

![](/images/summit8-booth.jpg)

We had a new T-shirt design especially for the event, here donned along with an older Jabber shirt and last year's XMPP design by Sebastiaan Deckers of the Pandion project, Joe Hildebrand of Cisco, XSF Board member Florian Jensen, and XMPP Council member Ralph Meijer.

![](/images/summit8-shirts.jpg)

As usual, one of the highlights of the weekend was the official XSF dinner, where participants got a chance to know each other better over some excellent Belgian food.

![](/images/summit8-dinner.jpg)

Finally, on Monday we held the Summit itself, with in-depth discussions and brainstorming sessions about technical challenges facing the XMPP developer community. The hot topics this year included:

-   Mobile Optimizations. Here there was general agreement that we need to experiment further with some of the technologies we defined at past Summits (including [Roster Versioning](https://xmpp.org/extensions/xep-0237.html) and
[SIFT](https://xmpp.org/extensions/xep-0273.html)), more fully specify methods for session resumption and quick reconnect, and perhaps define a straightforward method for "hushing" a session to turn off incoming presence notifications. Expect follow-up discussion on the [mobile@xmpp.org list](https://mail.jabber.org/mailman/listinfo/mobile).
-   Network Reliability. Here again the participants concluded that we need more implementation and deployment experience with existing extensions, especially [stanza acknowledgements](https://xmpp.org/extensions/xep-0198.html) and [message receipts](https://xmpp.org/extensions/xep-0184.html), so that we can see what reliability gaps remain once those are more widely deployed.
-   Server-to-Server Security. We had a wide-ranging discussion about [Domain Name Assertions](http://tools.ietf.org/html/draft-ietf-xmpp-dna-00), a proposal being worked on within the IETF's XMPP Working Group that would enable XMPP hosting services to deploy SSL/TLS without having access to the private keys for the domains they host. One result of the discussion was agreement to further explore attribute certificates as the most secure method for this feature. Another was to probably define a new DNS SRV record for delegated services; for example, \_xmpp-delegate.\_tcp.example.com might point to google.com, dreamhost.com, gmx.com, cisco.com, i-pobox.net, or some other hosting provider so that a connecting user or server would know that it's OK to connect to the hosting provider securely. These topics will be discussed on the [xmpp@ietf.org list](https://www.ietf.org/mailman/listinfo/xmpp).
-   Jingle. There was quite a bit of excitement about Thiago Camargo's proposal for [Jingle Relay Nodes](https://xmpp.org/extensions/inbox/jingle-nodes.html), which will make it easier to realistically deploy Jingle services for voice, video, and other multimedia use cases. Sign up for the [jingle@xmpp.org list](https://mail.jabber.org/mailman/listinfo/jingle) to discuss.
-   Multi-User Chat ("MUC"). Although this is one of the oldest and most widely-used XMPP extensions (powering everything from IETF chatrooms to replacements for IRC in military applications), further improvements are on the way. Summit participants discussed a more flexible model for user roles (provisionally called "hats"), the ability to share and subscribe metadata about the room and its occupants, the use of MUC as a control channel for voice and video conferences (i.e., [Multiparty Jingle](https://xmpp.org/extensions/xep-0272.html)), [distribution of MUC rooms](https://xmpp.org/extensions/inbox/distributedmuc.html) across servers, and several other topics. We're sure to have much discussion about these topics over the weeks and months ahead on the [muc@xmpp.org](https://mail.jabber.org/mailman/listinfo/muc) and [standards@xmpp.org](https://mail.jabber.org/mailman/listinfo/standards) lists.

As in years past, it was extremely beneficial to gather active members of the XMPP developer community together for coding, outreach, and in-depth technical discussion. The success of this year's Summit is already inspiring developers to work on smaller-scale events around the world, and to plan for XMPP Summit \#9 in North America this summer. Stay tuned for details.

--stpeter
