---
title: The XMPP Newsletter, 29 June 2018
date: 2018-06-29
author: jcbrand
categories: ["Newsletter"]
aliases:
    - "/2018/06/the-xmpp-newsletter-29-june-2018/"
---

Welcome to the XMPP newsletter.

If you have an article, tutorial or blog post you'd like us to include in the
newsletter, please [submit it on the XMPP wiki](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## News

* [Decentralized code forge, based on XMPP](https://www.goffi.org/b/F4xScokjZejCYAB4NamBbc/decentralized-code-forge,-based-xmpp)

Github has been acquired by Microsoft, prompting some FOSS developers with long
memories to reconsider whether they still want to host their projects there.

The Salut à Toi project is working on a decentralized and federated solution for issues and
merge requests, based on XMPP, and Jérôme Poisson explains in this article
their motivation for doing this work.

* [Project MAXS](http://projectmaxs.org/documentation/introduction.html), which stands for *Modular Android XMPP Suite*, allows you to control your Android device and receive notifications over XMPP.

* [XMPP vs Firebase: Choosing the right platform for real-time chat apps](https://www.techcronus.com/blog/real-time-chat-application-development-xmpp-firebase)

Every now and then a blog post comparing XMPP and Firebase appears. Generally
these posts seem to be poorly disguised attempts at SEO and to promote application
development by a particular devshop. This submission seems to follow the trend
and is also relatively superficial. It is however interesting to note that they
mention multiple times that it's difficult to set up an XMPP server. Perhaps
something to take note of and to consider how we could ease setup of an
XMPP-based solution.

* [Monal now has initial OMEMO support](https://monal.im/blog/monal-has-omemo/)

Monal has received a lot of updates last months and now it
also has initial OMEMO support. More work needs to be done, so don't expect to
see this in the App Store before August.

* Paul Schaub continues writing about his Summer of Code adventures:

    - [Command-line OX client](https://blogs.fsfe.org/vanitasvitae/2018/06/01/summer-of-code-command-line-ox-client/)
    - [PGPainless 2.0](https://blogs.fsfe.org/vanitasvitae/2018/06/06/summer-of-code-pgpainless-2-0/)
    - [Evaluation and key lengths](https://blogs.fsfe.org/vanitasvitae/2018/06/11/summer-of-code-evaluation-and-key-lengths/)
    - [The demotivating week](https://blogs.fsfe.org/vanitasvitae/2018/06/19/summer-of-code-the-demotivating-week/)
    - [An almost three line fix to a three days problem](https://blogs.fsfe.org/vanitasvitae/2018/06/26/summer-of-code-an-almost-three-line-fix-to-a-three-days-problem/)
 
## Software releases

### Servers

* [Jackal 0.2.0](https://github.com/ortuman/jackal/releases/tag/0.2.0)

The XMPP server written in Go has a new release with support for [Websocket (RFC-6395)](https://tools.ietf.org/html/rfc7395), [XEP-0191 (Blocking Command)](https://xmpp.org/extensions/xep-0191.html),
[XEP-0012 (Last Activity)](https://xmpp.org/extensions/xep-0012.html) and [XEP-0237 (Roster Versioning)](https://xmpp.org/extensions/xep-0237.html).

* [Ejabberd 18-06](https://blog.process-one.net/ejabberd-18-06/)

The new release includes improved robustness of external authentication
backends, support for REST API custom headers and more.

* [MongooseIM 3.0.0](https://www.erlang-solutions.com/blog/mongooseim-3-0-0-application-turbocharger.html)

This release includes the so-called "Inbox" feature which was also discussed at
the XSF summit in FOSDEM. It is a list of all ongoing conversations, with excerpts of
last messages and unread messages count, to help you gain an overview of what
happened while you were gone. There is no XEP for this yet, but Erlang Solutions
have promised to submit one. 

### Clients

* [Monal 3.0.2](https://itunes.apple.com/us/app/monal-free-xmpp-chat/id317711500?mt=8) has been released.

* [JSXC 3.4.0](https://www.jsxc.org/blog/2018/05/23/v3.4.0-released.html) released including support for location sharing and improved roster management in our internal Nextcloud backend.

### Libraries

* [XMPPFramework 4.0](https://github.com/robbiehanson/XMPPFramework/releases/tag/4.0.0)

Chris Ballinger has released Version 4.0 of XMPPFramework, the XMPP
library for iOS and macOS. It brings support for [XEP-0048:
Bookmarks](https://xmpp.org/extensions/xep-0048.html) and
[XEP-0359: Stanza Ids](https://xmpp.org/extensions/xep-0359.html).
It also has improved Swift support with optional Swift-only features.

* [Smack 4.3.0-rc1 and 4.4.0-alpha1](https://discourse.igniterealtime.org/t/smack-4-3-0-rc1-and-4-4-0-alpha1-released/81962)
