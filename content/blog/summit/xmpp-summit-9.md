---
title: XMPP Summit 9
date: 2010-12-01
author: willsheward
categories: ["XMPP Summit"]
aliases:
    - "/participate/the-xmpp-summit/xmpp-summit-9"
---

The ninth [XMPP Summit](/participate/the-xmpp-summit/) to be held by the XMPP Standards Foundation was held at [OSCON 2010](http://www.oscon.com/oscon2010) in Portland, Oregon (USA) on Monday July 19 and Tuesday July 20, 2010.

### Participants
The following people registered their participation in advance:

1.  lya Braude 
2.  Nathan Fritz 
3.  Joe Hildebrand 
4.  Steffen Larsen 
5.  Jérôme Sautret 
6.  Jon Snyder 
7.  Lance Stout 
8.  Mike Taylor 
9.  Angela Thomas 
10. Kurt Zeilenga 
11. Matt Miller 
12. Dave Richards 
13. Eero Neuenschwander 
14. Tuomas Koski

### Agenda
#### [Interop](http://wiki.xmpp.org/web/XMPP_Summit_Interop)
-   BOSH C2S
-   Encryption S2S

#### Hacks
-   [Sleek Hackfest](http://github.com/fritzy/SleekXMPP/)

#### Specs
-   Carbons
-   BOSH/WebSockets
-   Time-Based Implicit Invites to PEP
-   OneSocial

#### Demos
-   [OneSocialWeb](http://onesocialweb.org/)
-   [&yet XMPP web client](http://otalk.org/)
-   [DragonForce](http://drakontas.com/)

### Day One Summary
After a brief welcome and introductions the attendees created the Agenda using the barcamp style.

First, the group set up infrastructure for Interop testing. Jack E. helped by setting up a local CA Server and Joe set up DNS and DHCP while the great guys from &yet provided network hubs and patch cables. This allowed our testing to be done all on a private network, using example.com as our base DNS domain.

Once the servers were set up and running, we then retrieved the appropriate certificates that Jack E. had created and installed them into each server. This took longer than expected, as getting each server/OS to import the CA certificate to its trust store, etc. was troublesome.

Once basic server operation was up we tried to login to each server with PSI and Gajim (they just happened to be the most prevalent multi-account supporting clients we all had) and then moved on to testing BOSH and CORS. BOSH setup and testing continued until the break for lunch.

While some folks were getting BOSH testing working (i.e. once Bear finally learned how to read the Prosody docs!) Jack was also testing S2S unencrypted connections for those servers that were ready to test.

After lunch we had some short presentations from Joe on some of the new XEP's he would like to see worked on (especially Carbons, XEP-0280) and then we had some demos of &yet's [browser-based client](http://otalk.org/), [DragonForce](http://drakontas.com/) and [OneSocialWeb](http://onesocialweb.org/).
