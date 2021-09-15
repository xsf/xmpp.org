---
title: XMPP Summit - Day One Summary
date: 2010-07-20
author: bear
categories: ["XMPP Summit"]
---

We started with Bear and Joe giving a brief welcome and then we went around the room and allowed the attendees to introduce themselves. After the introductions we worked out the Agenda using the barcamp style of posting topics to the white-board and haggling over which order to work thru them.

Since the focus turned out to be almost all interop testing the group set up infrastructure with Jack E. helped by setting up a local CA Server and Joe setting up both DNS and DHCP while the great guys from &yet provided network hubs and patch cables. This allowed our testing to be done all on a private network, using example.com as our base DNS domain.

Once the servers were up and running, we then retrieved the appropriate certificates that Jack E. had created and installed them into each server. This took longer than expected, as getting each server/OS to import the CA certificate to the appropriate trust store was troublesome.

Once basic private network features were up and each server being tested was online, we then tried to login to each server with [PSI](http://psi-im.org/) and [Gajim](http://www.gajim.org) (they just happened to be the most prevalent multi-account supporting clients we all had) and then moved on to testing BOSH and CORS. BOSH setup and testing continued until the break for lunch.

While some folks were getting BOSH testing working (i.e. once Bear finally learned how to read the Prosody docs!) Jack was also checking that S2S unencrypted connections between the servers that were ready to test was correct at the wire level. He spent a *lot* of time in wireshark!

After lunch we had short presentations from Joe on some of the new XEP's he would like to see worked on (especially Carbons, XEP-0280) and then we had some demos of [&yet's](http://andyet) browser-based client [](http://otalk.org), [DragonForce](http://drakontas.com) and [OneSocialWeb](http://onesocialweb.org).
