---
title: Brussels Trip Report
date: 2011-02-18
author: stpeter
categories: ["XMPP Summit"]
---

Once again the XMPP community came together recently in Brussels to discuss XMPP technologies at the [XMPP Summit](https://xmpp.org/participate/the-xmpp-summit/xmpp-summit-10/) and to evangelize at the [Free and Open Source Software Developers' European Meeting](http://fosdem.org/) (FOSDEM). Here is a brief "trip report" from yours truly, XSF executive director Peter Saint-Andre.

The weekend consisted of several related events: a "hackfest" on Friday at the Cisco offices outside Brussels, a "devroom" on Saturday afternoon at FOSDEM (held at a local university), an official XSF dinner on Sunday evening, and Monday it was back to the Cisco offices for the XMPP Summit in the morning and an interim meeting of the IETF's XMPP Working Group in the afternoon.

**Friday**

At the hackfest on Friday, several XMPP software projects performed interoperability testing on [BOSH](https://xmpp.org/extensions/xep-0124.html) (the standard method for doing XMPP over HTTP). In addition, informal breakout groups discussed topics such as migrating to the IETF's upcoming vCard4 standard (it's time to say goodbye to our old [vcard-temp](https://xmpp.org/extensions/xep-0054.html) format!), multi-user Jingle and Jingle-based file sharing, and the need for an XMPP validation service at xmpp.org. Good progress was made on all of those topics (expect to see more about the validation effort over the next few months). After a classic developer's lunch of pizza and soft drinks, on Friday afternoon I presented a 90-minute tutorial on Unicode, UTF-8, stringprep, and other internationalization issues. Special thanks to everyone who paid attention the whole time! In addition, Klaas Wierenga of Cisco's Amsterdam office gave a talk about some experiments he and his team have conducted on single sign-on by combining XMPP's support for the Simple Authentication and Security Layer (SASL) with OpenID and the Security Assurance Markup Language (SAML).

Naturally, Friday night brought the legendary FOSDEM beer event, although some of us skipped out to catch up on email and such. However, we hear that a good time was had by all.

![](/images/delirium.jpg)

**Saturday**

Once again the good folks who run FOSDEM allotted a "developer room" to the Jabber/XMPP community, and once again it was packed most of the time. Especially popular were Remko Tronçon's intro to XMPP and the sessions on social networking and mobile applications. Dave Cridland of [Isode](http://www.isode.com/) received extra points for his interactive presentation on security!

![](/images/devroom-summit10.jpg)

**Sunday**

This year Sunday was a bit more ad-hoc than in years past because we did not have a table in the hallways at FOSDEM. However, that didn't stop folks from having productive hacking sessions and conversations on everything from ways to better evangelize XMPP within specialized developer communities, to improved handling of multiple simultaneous connected devices by clients and servers, to digital signatures and end-to-end encryption. Sunday evening also brought the now-traditional XSF dinner at [L'Auberge Bretonne](http://www.aubergebretonne.be/) in Overijse outside Brussels. In addition to enjoying some of the best food and friendliest service you'll find anywhere, the assembled XMPP developers discussed a wide range of topics and might even have made progress on some technical issues! Many thanks to the companies and individuals who sponsored this year's dinner: [Isode](http://isode.com/), [Nokia](http://nokia.com/), [&yet](http://andyet.net/), [Collabora](http://collabora.co.uk/), [AG Software](http://www.ag-software.de/), [Tigase](http://www.tigase.org/),   [Google](http://www.google.com/), the [Yate Project](http://yate.null.ro/), [Winfried Tilanus](http://www.tilanus.com/) of [HelpIM](http://helpim.org/), and [Netinstall](http://www.netinstall.cz/). Your support is very much appreciated!

![](/images/dinner-summit10.jpg)

**Monday**

Monday morning started with a demo of the entries in this year's developer challenge, sponsored by [Nokia](http://www.nokia.com/) and [Mobile Vikings](http://www.mobilevikings.com/). Although we didn't receive as many entries as last year, the winning entry showed creativity and the benefits of late-night hacking over the weekend.

After the excitement of the dev challenge, we held two technical sessions on Monday. In the morning, the XSF ran its XMPP Summit, with a focus on four topics:

1.  Reliable communications. Following up on implementation feedback provided by Matthew Wild of the [Prosody project](http://prosody.im/), Dave Cridland of [Isode](http://www.isode.com/), and Tobias Markmann of the [Psi project](http://psi-im.org/), the group discussed some improvements to our protocol for [stream management](https://xmpp.org/extensions/xep-0198.html), with consensus to simplify the protocol in several ways. The [XMPP Council](https://xmpp.org/about/xsf/the-xsf-council/) will be voting to approve those changes next week.

2.  Transferring multiple files using Jingle. The still-experimental [Jingle extension for file transfer](https://xmpp.org/extensions/xep-0234.html) currently defines only a way to transfer a single file. After discussions in Brussels, we will be modifying the protocol to enable sending of multiple files (e.g., for photo-sharing applications). These modifications will occur over the next few months as we work to stabilize the relevant suite of specifications.

3.  Distributed chatrooms. This is an early-stage research project to make [multi-user chat](https://xmpp.org/extensions/xep-0045.html) more robust and reliable, especially in deployments where server-to-server connectivity can be brittle. I provided an overview of the existing proposals (by myself, Carlo von Loesch and Philipp
Hancke of the [psyced project](Carlo%20von%20Loesch,%20Philipp%20Hancke), and XMPP Council member Kevin Smith of [Isode](http://www.isode.com/)), and we had some agreement on technology direction and open issues. Now we just need to get to work on further defining the approach.

4.  Finally, Kurt Zeilenga of [Isode](http://www.isode.com/) led a discussion about digital signatures and end-to-end encryption, reflecting the emerging consensus from discussions over the weekend among Joe Hildebrand and XMPP Council member Matt Miller of [Cisco](http://www.cisco.com/), Dave Cridland of [Isode](http://www.isode.com/), XMPP Council member Ralph Meijer of [Mediamatic](http://www.mediamatic.nl/?lang=en), and various other interested parties. This work is still somewhat preliminary, but those who've been involved have made good progress on issues like public key publishing (via [Personal Eventing Protocol](https://xmpp.org/extensions/xep-0163.html)) and message encryption (probably using an approach similar to the one that Matt Miller and I outlined in [draft-miller-3923bis](http://tools.ietf.org/html/draft-miller-3923bis-02)).

![](/images/xmppwg-summit10.jpg)

On Monday afternoon, the XSF ceded the floor to the IETF's [XMPP Working Group](http://tools.ietf.org/wg/xmpp/) so that the community could make progress on internationalization issues. Following up on my tutorial from Friday, I led a two-hour discussion to help narrow the scope of decisions that need to be made over the next few months as we work to replace stringprep with a more modern internationalization approach for XMPP. These are difficult issues, and solutions will require a bit of energy from the community this year, but hopefully we (along with other participants in the IETF's [PRECIS WG](http://tools.ietf.org/wg/precis/)) can develop an approach that is reasonable and sustainable.

The final topic of the day centered around improved security and scalability for server-to-server federation, which is already one of the strong points of XMPP technologies. Given the rapid progress of [DNSSEC](http://www.dnssec.net/) deployment over the last 12-18 months (including the imminent signing of the DNS root for .com domains), the group appeared to have agreement on pursuing an approach based on DNSSEC. Richard Barnes of [BBN](http://www.bbn.com/), Jonas Lindberg of [Google](http://www.google.com/), and Joe Hildebrand of [Cisco](http://www.cisco.com/) will be working on the relevant specifications soon.

After a long weekend of technical work, the assembled developers scattered throughout Europe and the world, but not before many of them repaired to their favorite (but top-secret) ribs restaurant in the center of Brussels. :)

I'd like to give a special thanks to the helpful staff at the Cisco office in Diegem, Belgium (especially our local coordinator Catherine Piret) for hosting the Friday and Monday sessions, and of course to the volunteer organizers of FOSDEM for putting on yet another great conference.

Finally, be aware that plans are already afoot for XMPP Summit \#11 in Portland, Oregon this summer. Expect announcements about that soon!
