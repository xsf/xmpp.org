---
title: CA Updates
date: 2009-09-08
author: stpeter
categories: ["Miscellaneous"]
---

Since 2006 the [XMPP Standards Foundation](https://xmpp.org/) has been [offering free digital certificates](http://blog.xmpp.org/index.php/2007/02/practical-network-security/) to administrators of XMPP servers as a way of encouraging encryption of point-to-point "hops" on the XMPP network. This program has been successful in several ways:

-   Thousands of XMPP deployments currently use certificates issued by the [XMPP ICA](https://xmpp.net/).
-   Popular XMPP clients and servers have fixed bugs in their code related to certificate handling.
-   The XMPP community has gained practical experience with stronger encryption.

Since the beginning, the XSF has functioned as an "intermediate certification authority" or "ICA", where the root CA is [StartCom](http://www.startssl.com/). In collaboration with our friends at StartCom, we recently decided that StartCom will directly offer Class 1 certificates through its normal process at [http://www.startssl.com/](http://www.startssl.com/) instead of running a specialized service only for XMPP servers at xmpp.net. This lowers the administrative burden both for the XSF (we will no longer need to manually approve certain certificate requests) and for StartCom (they will be able to use the same code for issuing both web server certificates and IM server certificates).

We have always seen our arrangement with StartCom as something of an experiment. Although there were many good reasons for choosing StartCom as our partner in offering free certificates (they enabled us to run an intermediate CA, they have great customer service, and the price was extremely competitive), that partnership was never exclusive. We have hoped that StartCom's example would encourage other CAs to offer XMPP-specific certificates as well. Although that has not happened yet, modifying our relationship with StartCom is a movement in that direction because their issuance of XMPP-specific certificates is now part of their "mainstream" offerings.

The XSF will continue to issue and honor certificates via the XMPP ICA for a few more months, but StartCom is hard at work on upgrading their core service to directly offer XMPP certificates at their own site, so expect a switchover sometime in the relatively near future. We will keep you up to date at this blog and at xmpp.net regarding any service issues.

Finally, we would like to thank [Eddy Nigg](https://blog.startcom.org/) and his team at StartCom for all their hard work over the years. They are true security professionals and a pleasure to work with. We certainly hope that our paths cross again in the future.
