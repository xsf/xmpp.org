---
title: XMPP URNs
date: 2007-02-28
author: stpeter
categories: ["Miscellaneous"]
---

Yesterday the IETF [announced](http://www1.ietf.org/mail-archive/web/ietf-announce/current/msg03462.html) that [draft-saintandre-xmpp-urn](https://xmpp.org/internet-drafts/draft-saintandre-xmpp-urn-03.html) has been approved by the [IESG](http://www.ietf.org/iesg.html) for publication as an informational RFC. What this means for us is that the XSF (specifically the [XMPP Registrar](https://xmpp.org/registrar/)) will control its own "tree" of [Uniform Resource Names](http://www.ietf.org/rfc/rfc2141.txt) to issue for use in [XMPP Extension Protocols](https://xmpp.org/extensions/), as specified in Section 4 of [XEP-0053](https://xmpp.org/extensions/xep-0053.html). This is good because URNs are more stable than the URIs (such as "http://jabber.org/protocol/muc") that we've been using for XML namespaces in our protocols. Although we lose the ability to copy and paste such a URI into a browser and find information about the relevant protocol, it's easy enough to search for a string like "urn:xmpp:chatneg" and find the [relevant specification](https://xmpp.org/extensions/xep-0155.html). So the slight loss in convenience is offset by the improved permanence of our XML namespaces. Besides, all the other standards development organizations are using URNs, so why not us? :-)

UPDATE 2007-04-28: This document has now been published as [RFC 4854](http://www.rfc-editor.org/rfc/rfc4854.txt).
