---
title: XMPP Roundup 10
date: 2009-06-11
author: Nyco
categories: ["XMPP Roundup"]
---

[Reporters: Nicolas Vérité and Peter Saint-Andre]
For those who love round numbers, welcome to the tenth edition of the XMPP Roundup, our semi-regular review of news and events in the XMPP community. Since our [last roundup](/2009/05/xmpp-roundup-9/) on May 11, here's what's been happening...

**Software**

*Google Wave*

Google has announced the existence of [Google Wave](http://www.waveprotocol.org/), an early-stage technology for real-time interaction that will incorporate aspects of IM, email, wikis, and other collaboration techniques. The technology for federating different Wave instances is pure XMPP, so the developer community is watching this project quite closely.

*Minbif*

[Minbif](http://symlink.me/wiki/minbif) is an IRC gateway to IM networks which lets the user connect to Jabber (and many proprietary legacy IM systems), through IRC command lines. It is release under the GPLv2 license, in version 1.0alpha as the time of this writing.

*Utterance*

Nolan Darilek has announced the development of [Utterance](http://gitorious.org/utterance), an XMPP microblog transport, written in Ruby under a BSD license.

*modular\_muc*

[Eric Cestari](http://www.cestari.info/) wrote a [Multi-User Chat (MUC) module](http://github.com/cstar/modular_muc/tree/master) in ejabberd that is as modular as the PubSub module.

*exmpp*

ProcessOne has launched its [exmpp](https://support.process-one.net/doc/display/EXMPP/exmpp+home) Erlang XMPP library under the Erlang Public License (EPL), in its newly opened [Labs](http://www.process-one.net/en/labs/).

*Hemlock*

[Hemlock](http://hemlock-kills.com/) is an opensource soon-to-be-released Flash XMPP framework.

**Services**

*Ask me*

[http://askme.im/](http://askme.im/) has a set of XMPP bots that cover quotes, jokes, movie reviews, stock prices and daliy horoscopes, and much more...

*Jabbim's URL shorting service*

Jabbim community has released a [new URL shortening service](http://dev.jabbim.cz/?p=65) at [xmpp:shorty@jabbim.com](xmpp:shorty@jabbim.com): just add it to your roster and start chatting.

**Community**

Members of the XMPP community have started work on two new initiatives: an open framework for XMPP protocol testing and a website for information about the XMPP network. To participate, join the [interop@xmpp.org](https://mail.jabber.org/mailman/listinfo/interop) discussion list or the [operators@xmpp.org](https://mail.jabber.org/mailman/listinfo/operators) discussion list, respectively. Expect to see more work on these projects in the coming months!

**Protocols**

The big news here is that the core Jingle specifications have finally advanced from Experimental to Draft status (version 1.0)! We'll post more about this in the near future. The specs that have moved forward are:

-   [XEP-0166: Jingle](https://xmpp.org/extensions/xep-0166.html)
-   [XEP-0167: Jingle RTP Sessions](https://xmpp.org/extensions/xep-0167.html)
-   [XEP-0176: Jingle ICE-UDP Transport Method](https://xmpp.org/extensions/xep-0176.html)
-   [XEP-0177: Jingle Raw UDP Transport Method](https://xmpp.org/extensions/xep-0177.html)

Another important specification to advance from Experimental to Draft is [Roster Versioning](https://xmpp.org/extensions/xep-0237.html). This technology will make it much more efficient for IM clients to log into XMPP servers, since the server can inform the client if the user's contact list has not changed since the client last logged in (or send a small diff if it has changed). This is especially important in mobile applications such as cell phones and PDAs. The roster versioning technology is one of the mobile optimizations we are working on, and will be incorporated into the revisions to RFC 3921 within the IETF's newly re-formed [XMPP Working Group](http://tools.ietf.org/wg/xmpp/).

In addition, the [XMPP Council](https://xmpp.org/council/) has been working to advance more XEPs from Draft to Final. The latest specification to be so honored are:

-   [XEP-0138: Stream Compression](https://xmpp.org/extensions/xep-0138.html)
-   [XEP-0199: XMPP Ping](https://xmpp.org/extensions/xep-0199.html)

Finally, the Council has also been performing some "spring cleaning" by officially obsoleting XEP-0003: Proxy Accept Socket Service, XEP-0011: Jabber Browsing, XEP-0022: Message Events, XEP-0023: Message Expiration, XEP-0025: Jabber HTTP Polling, XEP-0090: Legacy Entity Time, and XEP-0091: Legacy Delayed Delivery.

**Conclusion**

Again, 2009 seems to be a very active year for XMPP technologies.
