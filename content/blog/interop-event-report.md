---
title: Interop event report
date: 2010-12-14
author: kev
categories: ["Events"]
---

From 6th-11th December 2010, the XSF ran its first remote interop event. All client and server projects were invited to attend, and we had a good turnout. The aim of the interop event was to test basic XMPP interoperability, particularly re correct TLS and certificate handling, for both clients and servers. We provided projects with a list of tests, together with a set of known-bad server configurations, and worked through these during the week. Several ancillary tests were also performed, which are listed after the scripted test results.

Server to server testing:

Five server projects provided test servers for the event:

-   [Isode](http://www.isode.com/products/m-link.html) provided servers running M-Link's development trunk for the upcoming R15.0, and the current R14.6 release.
-   [Prosody](http://prosody.im/) provided a sever running the trunk for their upcoming 0.8 release.
-   [ProcessOne](http://www.process-one.net/) provided a server running the [ejabberd](http://www.ejabberd.im/) 2.1.x branch.
-   [psyced](http://www.psyced.org/) provided several configurations of their server to server support, covering different test cases.
-   [Tigase](http://www.tigase.org) supplied a server running the development trunk.

Initial tests occurred on Wednesday, with no requirements on TLS, SASL, or cert checking - only testing that the servers were able to interoperate by passing an 'iq' query stanza and receiving a reply (indicating two-way communication). All projects were demonstrated to interoperate at this level.

The scripted server tests for Thursday required that all server to server connections were encrypted with TLS, but not that the certificates were verified. M-Link's trunk, ejabberd, Prosody and psyced were able to demonstrate interoperability; M-Link's release didn't participate as it cannot be configured to require TLS, although the aforementioned servers interoperated with it; Tigase does not support TLS for server to server communication, so didn't participate.

The last server tests were conducted on Friday; these required servers to require all communication with other servers to occur over TLS, with full certificate trust and validity checking. M-Link's trunk, Prosody and psyced were able to demonstrate this through correct interoperability with the test servers and failed interoperability with provided servers with different mis-configurations covering: no TLS, expired certificates, revoked certificates, untrusted certificates and certificates not matching the service. ejabberd passed all tests except for the test of revocation list checking. M-Link R14.6 and Tigase did not participate.

Client results:

-   [Swift](http://swift.im) was the only client to participate in the scripted tests, with the development trunk.

Swift was able to demonstrate interoperability with all servers (excluding psyced, which wasn't configured for client connections) with and without the servers requiring TLS. When testing against servers with invalid certificates, Swift correctly rejected the expired and untrusted certs, and the one for the wrong service. Swift did not support certificate revocation checks.

Other results:

In addition to the formal tests above, several projects performed additional testing, the highlights of which are below.

-   The Gajim, OneTeam and N900 clients reported success with Jingle interoperability for voice calls with acceptable voice quality on standard connections. Connections over mobile (3G) connection with the N900 were less encouraging.
-   Interoperability was reported between the Telepathy framework and M-Link for the 'google:queue' extension for reducing battery cost for mobile clients. It is expected that standardization will follow.
-   Interoperability was demonstrated between Swift and M-Link over IPv6.
-   Servers were reported not to use or negotiate the SSLv2 protocol, complying to the requirements given in [draft-ietf-tls-ssl2-must-not](http://tools.ietf.org/html/draft-ietf-tls-ssl2-must-not-03).
-   XEP-0198 support was demonstrated between Swift and M-Link, M-Link and Prosody, and Prosody and Swift, demonstrating the possibility of a more reliable XMPP network as this technology gets deployed.
-   M-Link and psyced demonstrated bi-directional server communication support, using XEP-0288.
-   Interoperability of SCRAM-SHA1-PLUS (channel binding) was demonstrated between Isode's implementation and the GNU SASL implementation, and Swift was able to connect to M-Link also using SCRAM-SHA1-PLUS.

From the XSF's point of view, the week was an outstanding success, demonstrating general stability of server to server communications between a number of projects, and all projects taking part in the scripted tests reported that they had found and corrected issues during the course of the week as a consequence of the testing, making it a valuable event for all involved.
