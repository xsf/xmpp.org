---
title: Presence Scalability
date: 2007-04-11
author: stpeter
categories: ["Miscellaneous"]
---

Members of the IETF's SIMPLE Working Group recently [analyzed](http://www.ietf.org/internet-drafts/draft-ietf-simple-interdomain-scaling-analysis-00.txt) the scalability of SIP/SIMPLE technologies with respect to sharing presence between domains. Because their work provides a helpful baseline for comparing presence technologies, we decided to perform a [similar analysis](https://xmpp.org/internet-drafts/draft-saintandre-xmpp-presence-analysis-00.html) for XMPP. The results should be of interest to any large enterprise, ISP, or carrier that is contemplating deployment of presence-based services.

Consider some of the relevant results for bandwidth usage between two presence domains:

-   If the domains have 20,000 users, where each user has 4 contacts in the other domain and changes presence 3 times an hour, bandwidth usage is estimated to be 30 kilobytes per second for XMPP and 830 kilobytes per second for SIMPLE.
-   If the domains have 20,000 users, where each user has 20 contacts in the other domain and changes presence 3 times an hour, bandwidth usage is estimated to be 150 kilobytes per second for XMPP and 1,968 kilobytes per second for SIMPLE.
-   If the domains have 60,000 users, where each user has 10 contacts in the other domain and changes presence 3 times an hour, bandwidth usage is estimated to be 225 kilobytes per second for XMPP and 3,683 kilobytes per second for SIMPLE.
-   If the domains have 10,000,000 users, where each user has 10 contacts in the other domain and changes presence 6 times an hour, bandwidth usage is estimated to be 70,833 kilobytes per second for XMPP and 880,555 kilobytes per second for SIMPLE.

While these analyses need to be reviewed, discussed, and extended within the IETF, the preliminary results indicate that the choice of presence technology can make a significant difference with regard to bandwidth usage.

UPDATE 2007-10-02: See [here](https://stpeter.im/?p=2051) for more up-to-date analysis.
