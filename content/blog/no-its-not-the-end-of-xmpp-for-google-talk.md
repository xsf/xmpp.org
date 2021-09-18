---
title: "No, it's not the end of XMPP for Google Talk"
date: 2015-03-02
author: fippo
categories: ["Miscellaneous"]
---

There's some recent discussion about the sky falling for XMPP at Google. See [this blog post by Dan York](http://www.disruptivetelephony.com/2015/02/google-finally-kills-off-googletalk-and-xmpp-jabber-integration.html) for example.

In reality, we don't know the state of XMPP inside Google because they don't share their use of XMPP with the XSF. We do know Android's [Google Cloud Messaging](https://developer.android.com/google/gcm/ccs.html) uses it. We know [Hangouts Videochat uses it](http://juberti.blogspot.com/2011/07/hangouts-mailbag.html). We know Google Talk still (insecurely) federates with (some) XMPP services. But from an outside perspective, Google has made no major recent changes in terms of how they're using XMPP from what we can observe.

So what happened?

The Google Talk app for Windows has been deprecated as of February 23, 2015 [as explained by the product manager](https://plus.google.com/+MayurKamat/posts/ETBvtp9VYav). Google [announced a while ago](http://googleappsupdates.blogspot.ca/2014/10/notification-re-google-talk-app-for.html) they intended to do this, but it comes as little surprise given the client has not seen much development in this decade.

Instead of Google Talk, Hangouts is promoted. Hangouts does not interoperate with federated XMPP clients. Users appear as visible, but messages from federated contacts are lost, which is a very confusing user experience.

The XSF still believes in the principle of client choice, best explained by Google on their [developer pages](https://developers.google.com/talk/open_communications):

> We believe users should have choice in which clients they use to > connect to the Google Talk service and we want to encourage the > developer community to create new and innovative applications that > leverage our service. To enable this, Google Talk uses the standard > XMPP protocol for authentication, presence, and messaging.

Note that you can still continue to use the Google Talk Service with a third party XMPP client and the Google Talk XMPP servers continue to federate with other domains.   This is called "service choice". The principle is, again, [best explained by Google](https://developers.google.com/talk/open_communications#service_1):

> Service choice is something you have with email and, for the most > part, with your regular phone service today. This means that > regardless of whom you choose as your email service provider (Gmail, > Hotmail, Yahoo! Mail, your school or ISP, etc), you can email anyone > who is using another service provider. The same applies to phone > service. You can call someone even if they do not use the same phone > company as you do. This allows you to choose your service provider > based on other more important factors, such as features, quality of > service, and price, while still being able to talk to anyone you want.

However, since the Google Talk Service does not support server-to-server encryption via TLS (something that was required by RFC 3920 in 2004), a number of servers (including jabber.org) refuse to establish a connection [since May 2014](https://xmpp.org/2014/05/happy-encrypted-network/).

We'd love to see Google embrace secure messaging for federated messaging. But aside from this long-standing issue, XMPP is alive and kicking at Google.
