---
title: Practical Network Security
date: 2007-02-07
author: stpeter
categories: ["Miscellaneous"]
---

Two months ago we launched the XMPP Intermediate Certification Authority at [xmpp.net](https://www.xmpp.net/). It was a bit of an unusual step for a standards development organization to take -- after all, you don't see the [IETF](http://www.ietf.org/), [W3C](http://www.w3.org/), and [IMC](http://www.imc.org/) offering free digital certificates to hostmasters, webmasters, and postmasters. But we decided that we needed provide some practical leadership regarding the security of the Jabber/XMPP network, and [StartCom](http://cert.startcom.org/) (our root CA) has made that task much easier than we could have hoped.

Here are the results so far:

1.  We have issued around 100 active server certificates.
2.  We have stabilized the certificate data format based on feedback from server admins and developers.
3.  Several large XMPP-based code projects have built in support for StartCom's root certificate.
4.  More widespread deployment has exposed incorrect certificate handling in several software codebases, leading to bug fixes and more secure code.

Clearly we have much farther to go.

First, we'd like to see all server and client codebases support [TLS](http://www.ietf.org/rfc/rfc4346.txt) for channel security, [SASL](http://www.ietf.org/rfc/rfc4422.txt) for strong authentication, and the StartCom root certificate.

Second, we need many more server deployments to obtain digital certificates. In the past that has been an expensive proposition, but now the XSF provides no-cost ("free as in beer") digital certificates so there's no excuse! By the end of 2007 we hope that a majority of the traffic on the XMPP network will be protected by channel encryption. But to make that happen we need server admins to visit [xmpp.net](https://www.xmpp.net/), sign up for an account, and request a free certificate by following our simple [certificate process](https://www.xmpp.net/certificate-process).

Remember, it's easy, it's fun, and it makes the network more secure, one server at a time!
