---
title: IETF Advancement
date: 2007-06-11
author: stpeter
categories: ["Miscellaneous"]
---

As previously mentioned, we are working to update the core XMPP specifications by incorporating feedback based on the significant implementation and deployment experience with XMPP technologies we have gained since [RFC 3920](http://www.ietf.org/rfc/rfc3920.txt) and [RFC 3921](http://www.ietf.org/rfc/rfc3921.txt) were published in October, 2004. To date we have expected the revised versions to advance XMPP to a status of Draft Standard within the [Internet Standards Process](http://www.ietf.org/rfc/rfc2026.txt) managed by the IETF.

However, it seems that we overlooked some of the rules from RFC 2026, specifically that "standards track specifications normally must not depend on other standards track specifications which are at a lower maturity level".

What this means is that the XMPP specifications will not be able to advance to Draft until the specs defining IETF technologies on which XMPP depends also advance to Draft (i.e., until there are no more downward references or "downrefs").

Unfortunately, the XMPP specs have many downrefs, including the following:

-   [RFC 2743: Generic Security Service Application Program Interface Version 2, Update 1](http://www.ietf.org/rfc/rfc2743.txt)
-   [RFC 2782: A DNS RR for specifying the location of services (DNS SRV)](http://www.ietf.org/rfc/rfc2782.txt)
-   [RFC 2831: Using Digest Authentication as a SASL Mechanism](http://www.ietf.org/rfc/rfc2831.txt)
-   [RFC 3280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](http://www.ietf.org/rfc/rfc3280.txt)
-   [RFC 3454: Preparation of Internationalized Strings ("stringprep")](http://www.ietf.org/rfc/rfc3454.txt)
-   [RFC 3490: Internationalizing Domain Names in Applications (IDNA)](http://www.ietf.org/rfc/rfc3490.txt)
-   [RFC 3491: Nameprep: A Stringprep Profile for Internationalized Domain Names (IDN)](http://www.ietf.org/rfc/rfc3491.txt)
-   [RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace](http://www.ietf.org/rfc/rfc4122.txt)
-   [RFC 4346: The Transport Layer Security (TLS) Protocol Version 1.1](http://www.ietf.org/rfc/rfc4346.txt)
-   [RFC 4422: Simple Authentication and Security Layer (SASL)](http://www.ietf.org/rfc/rfc4422.txt)
-   [RFC 4648: The Base16, Base32, and Base64 Data Encodings](http://www.ietf.org/rfc/rfc4648.txt)

Given the serious number of significant downrefs, I think it's unrealistic for us to expect advancement of XMPP to Draft Standard anytime soon. It appears that the best we can do is update the XMPP specs as we have been doing, resulting in revised specifications that reflect our community's implementation and deployment experience but that are still at the Proposed Standard level.

And speaking of updated specs, expect revised versions of [rfc3920bis](https://xmpp.org/internet-drafts/draft-saintandre-rfc3920bis-02.html) and [rfc3920bis](https://xmpp.org/internet-drafts/draft-saintandre-rfc3921bis-02.html) soon.

UPDATE: As [Joe Hildebrand](http://arch.jabber.com/2007/06/11/ietf-process/) mentions (see also [my reply](http://stpeter.im/?p=1920)), things are probably not quite so dire. Check for further updates as we work with folks at the IETF on this topic...
