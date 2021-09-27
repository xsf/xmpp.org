---
title: MXM 2
date: 2009-04-14
author: stpeter
categories: ["Miscellaneous"]
---

*Reported by Peter Saint-Andre*

Back in March, we decided to hold an informal "Monthly XMPP Meeting" among developers in our community. Here is a brief report on the second such meeting, held today (April 14) in the [jdev@conference.jabber.org](xmpp:jdev@conference.jabber.org?join) chatroom (the archived discussion log is [here](http://logs.jabber.org/jdev@conference.jabber.org/2009-04-14.html#14:06:45)).

Here are some of the topics we discussed...

1. Last Call for [XEP-0232: Software Information](https://xmpp.org/extensions/xep-0232.html)

    The points raised included:
    -   Is this a misuse of service discovery?
    -   Will this make [entity capability](https://xmpp.org/extensions/xep-0115.html) caches less useful because they will be too large to search easily?
    -   Does it make more sense to publish this information via the [Personal Eventing Protocol](https://xmpp.org/extensions/xep-0163.html) using the old [software version](https://xmpp.org/extensions/xep-0092.html) format?

    The [XMPP Council](/about/xmpp-standards-foundation#council) will vote on XEP-0232 at its next meeting (April 22). More feedback is welcome before then on the [standards@xmpp.org](https://mail.jabber.org/mailman/listinfo/standards) mailing list.

2.  Last Call for [XEP-0237: Roster Versioning](https://xmpp.org/extensions/xep-0237.html)

    There is general agreement that this proposed modification to the core XMPP roster management protocol is in good shape. There are still a few edge cases to figure out, especially the empty roster case.

3.  Last Calls for the [core Jingle specs](https://xmpp.org/tech/jingle.shtml)

    No real discussion here. Most people seemed to think that these are ready for advancement to Draft in the XSF's standard process.

4.  Pubsub/PEP implementations Consensus that we need more interop testing among implementation such as ejabberd, idavoll, Openfire, and Tigase. Perhaps we will make this a focus at the next [XMPP Summit](https://xmpp.org/summit/).

5.  [XEP-0198: Stream Management](https://xmpp.org/extensions/xep-0198.html)

    People like this because it will improve the reliability of communications across the network. Now we need to go forth and implement.

6.  Bidirectional server-to-server connections

    As defined in RFC 3920, XMPP requires two TCP connections for each server-to-server ("s2s") link. This is sub-optimal. We decided that we need to hold a dedicated discussion session about s2s fixes and improvements (server dialback, multiplexing domains over a given stream, etc.). We agreed to make that the focus of the next Monthly XMPP Meeting, tentatively scheduled for May 5 (add it to your calendar [here](https://xmpp.org/xsf/XSF.ics)).

My impression is that it is quite valuable to hold these meetings. I especially found it helpful to have a more general community discussion about XMPP Extension Protocols that are currently in Last Call or under heavy development, because it gives people a chance to talk about them in real time rather than only on the standards@xmpp.org mailing list.

So expect us to keep holding this kind of online meeting over the coming months.
