---
title: Progress on Internationalization
date: 2011-05-17
author: stpeter
categories: ["Miscellaneous"]
---

As you might recall from our [Brussels trip report](/2011/02/brussels-trip-report/) a few months ago, the XMPP community has a bit of work to do on internationalization. It's not that XMPP messages or addresses can't include non-ASCII characters, because we've had that capability since 1999. The problem comes from our dependence on a technology called stringprep ([RFC 3454](http://tools.ietf.org/html/rfc3454)), which we use to compare JabberIDs for tasks like authentication and authorization of users and servers. Because stringprep is being deprecated by the [IETF](http://www.ietf.org/) for internationalized domain names, various application technologies that use stringprep for identifiers other than domain names (e.g., usernames and passwords) need to develop a new approach to comparing protocol strings.

This subject was discussed extensively in the interim meeting of the IETF's XMPP Working Group in Brussels at the beginning February and in the PRECIS and XMPP sessions during IETF 80 in Prague at the end of March, resulting in some very rough consensus on a possible path forward. Today, yours truly submitted two Internet-Drafts that start to capture that rough consensus: a new [internationalization framework](https://datatracker.ietf.org/doc/draft-blanchet-precis-framework/) for consideration by the PRECIS Working Group and a [proposed replacement](https://datatracker.ietf.org/doc/draft-saintandre-xmpp-6122bis/) of [RFC 6122](http://tools.ietf.org/html/rfc6122) for consideration by the XMPP Working Group.

Expect intensive work on these specifications over the next few months as we strive to modernize the internationalization support in XMPP.
