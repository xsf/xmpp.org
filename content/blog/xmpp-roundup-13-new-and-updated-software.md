---
title: "XMPP Roundup 13: new and updated software"
date: 2010-01-29
author: Nyco
categories: ["XMPP Roundup"]
---

Welcome to the XMPP software Roundup 13. As announced in the [latest Roundup](http://blog.xmpp.org/index.php/2010/01/xmpp-roundup-13-articles-talks-and-events/), we have split it into different parts. The first part covered articles, talks and events. This post covers new and updated software, the next one will cover XMPP services.

Special thanks to Will, Waqas, Jack, Guillaume, Nicolas, who have actively contributed to this report.

Due to the high number of new items (yes, the XMPP community is super-active), we have sectionned these into the classical division clients, servers, and libraries, and... a last section you should check carefully.

**Clients**

*Jabbim for Android*

The Jabbim team has released an early version of [Jabbim for Android](http://www.jabbim.com/android/ "http://www.jabbim.com/android/"), the Linux-based OS platform for mobile phones and devices from Google.

*joom*

Released under the Artistic and GPL licenses, [joom](http://code.google.com/p/joom/) is a collaborative brainstorming tool, similar to a group chat plus topics creation. First originality, the UI combines the personal roster, as well as the room roster. The other originality, is that the UI shows different views of the conversations: the regular stream of messages, and the active and inactive topic views, which filter out messages with certain hashtags. Thus it is possible to hold mulitple conversations in one room.

*Gajim 0.13*

Yann Le Boulanger, aka Asterix, has announced the [release 0.13 of the Gajim XMPP client](http://www.gajim.org/), bringing BOSH, roster versionning, XHTML-IM sending, and many bug fixes.

*Coccinella 0.96.16 Released*

Sander Devrieze has [announced Coccinella 0.96.16](http://coccinella.im/coccinella-0.96.16), bringing a lot of bug fixes, as well as a tenth birthday.

*Psi 0.14 is out*

This time we've made sure Psi is not missed in the Roundup: Justin Karneges has [announced the version 0.14 of the Psi XMPP client](http://lists.affinix.com/pipermail/psi-devel-affinix.com/2009-December/008928.html). It brings color options to the chat window, reason for kick/ban in groupchat, improved User Info window, support for Enchant as an alternative to Aspell, commandline interface now supports choosing profile and setting status, D-BUS interface now supports setting status and indicating sleep/wake, fixed voice calling compatibility bugs with Pidgin and Empathy, and of course various other minor improvements and bugfixes.

*Haskell: XMPP and matsuri*

[matsuri](http://kagami.touhou.ru/projects/show/matsuri) is a ncurses XMPP client written on Haskell, published under the GPLv3 license by Kagami.

*Yaxim*

[Yaxim](http://github.com/pfleidi/yaxim) is new XMPP client for the Android platform.

*Juick for Android*

Juick, the real-time blogging and social network platform based on XMPP, has a [specific client](http://code.google.com/p/juick-android/) on the Android platform.

*Vacuum-IM*

[Vacuum-IM](http://code.google.com/p/vacuum-im/) is a new multi-account, multi-platform XMPP client. It uses the Qt library, and is released under the GPLv3 license, as a version number 1.0.

**Servers**

*Openfire under the Apache license*

The Openfire server is undergoing [a change of license](http://www.igniterealtime.org/community/message/196063), from the GPL to the Apache 2.0 license. The next version with the updated license will be released in the near future.

*Legacy IM Connections via M-Link*

Isode has [announced](http://isode.com/company/wordpress/?p=6) that they are partnering with Zion Software to deploy the [JBuddy XMPP Gateway](http://www.zionsoftware.com/products/xmpp-gateway/) for connectivity between Isode's M-Link server software and legacy IM networks.

*Tigase Server 4.3*

Artur Hefczyc has released [version 4.3 of the Tigase Server](http://www.tigase.org/en/content/tigase-xmpp-server-431-b1858). It contains a lot of performance improvements, as well as new features, like monitoring, scripting, or roster versionning, and much more.

*Spectrum*

[Spectrum](http://spectrum.im/) is an XMPP gateway, released under the GPL license, using the libpurple and gloox libraries, coming from a Google Summer of Code project. It supports ICQ, XMPP (Jabber, GTalk), AIM, MSN, Facebook, Twitter, Gadu-Gadu, IRC and SIMPLE.

*python-xmpp-server*

[python-xmpp-server](http://github.com/thisismedium/python-xmpp-server) speaks for itself, it has been developed by [Medium](http://en.wikipedia.org/wiki/Medium_%28company%29).

*Clustering plugin for Openfire is now open source*

[Ignite Realtime](http://www.igniterealtime.org/) has [announced](http://www.igniterealtime.org/community/blogs/ignite/2009/11/10/clustering-plugin-for-openfire-is-now-open-source) the release of the [clustering plugin](http://www.igniterealtime.org/projects/openfire/plugins/clustering/readme.html) for Openfire as opensource, under the Apache 2.0 license.

*Prosody 0.6 and 1 year old*

Prosody, which is [one year old](http://blog.prosody.im/one-year-ago-today/), has been [published in version 0.6](http://blog.prosody.im/prosody-0-6-0-released/), bringing a telnet console, multi-sessions in MUC, stream compression, S2S encryption, per-host certificates, an importer for ejabberd MySQL dumps, and compatibility with ejabberd's vcard behaviour.

**Libraries**

*Strophe.js 1.0*

[Jack Moffit](http://metajack.im/ "http://metajack.im/") has announced the [release of version 1.0](http://metajack.im/2010/01/01/celebrate-2010-with-strophejs-10/) of the [Strophe.js](http://code.stanziq.com/strophe/) library.

*MatriX Mobile and MatriX for .NET released*

Alexander Gnauck has released [MatriX Mobile](http://blog.ag-software.de/?p=87) for the .NET Compact Framework, as well as [MatriX for .NET](http://blog.ag-software.de/?p=79).

*asmack*

The [asmack](http://code.google.com/p/asmack/) library has been released. Basically, it a the smack library, adding SASL and DNS SRV for the Android platform.

*Libjingle in Chromium*

Libjingle, the Google's opensource library for Jingle, [has been committed in Chromium](http://git.chromium.org/viewvc/chrome/trunk/src/third_party/libjingle/), the opensource base of the Chrome browser.

*GWT bindings for the Strophe XMPP library*

[Johann Prieur](http://jprieur.wordpress.com/2009/10/07/gwt-bindings-for-the-strophe-xmpp-library/) has announced on his blog the availability through Bazaar of [gwt-strophe](https://launchpad.net/gwt-strophe), under the MIT/X/Expat License, a binding for Strophe, the XMPP library. It is now in its early stage, and need testing and bug reports.

*Emite*

[Emite](http://code.google.com/p/emite/) 0.5.0 has been released, now with support for GWT 2.0. Emite is a GWT XMPP library (Google Web Toolkit) under the LGPL v3 license.

*gloox 1.0*

The famous [gloox](http://camaya.net/gloox/) library, for clients and components, has been [released in version 1.0](http://camaya.net/api/gloox/), under the GPL license. This should not be confused with the [glooxd libray](http://camaya.net/glooxd/), made for servers.

*retepXMPP Server, Client & Library*

[retepXMPP](http://kenai.com/projects/retepxmpp/) is a suite of libraries for writing applications using the XMPP protocol, with which it is possible to create components, clients or even embedded servers.

**Unclassifiable (aka "Others")**

Although the title of this section might sound a bit demeaning, this is the place you should focus, because it is sometimes the place where most interesting (weird?) innovations appears...

*Jorge*

Zbyszek Zólkiewski has written [Jorge](http://dev.jabbim.cz/jorge/), a free PHP-based front-end for the [mod\_logdb](http://www.ejabberd.im/mod_logdb) message archiving system for ejabberd written by Oleg Palij.

*xeerkat*

[xeerkat](http://code.google.com/p/xeerkat/) is a P2P computing framework over XMPP. xeerkat is not a new project, but original and not previously covered by the XMPP Roundup.

*XMPP Framework*

[XMPP Framework](http://drupal.org/project/xmppframework), using XMPPHP, brings XMPP features to Drupal: XMPP-Drupal users correlation and relationship, XWChat web chat client (based on JSJaC), MUC, and notifications. This module has been contributed by Darren Ferguson of OpenBand.

*XMPPKit*

The [Étoilé](http://etoileos.com/etoile/) user environment for the [GNUstep](http://www.gnustep.org/) project is building in support for sending what they call "CoreObjects" over XMPP using their emerging [XMPPKit](http://etoileos.com/news/archive/2009/09/15/1659/); as a result they hope to enable collaborative editing, whiteboarding, and other interactive applications.

*RDFbus*

The Ruby software [RDFbus](http://github.com/bendiken/rdfbus), published under a BSD-like license, is a middleware for enabling RDF publish/subscribe payloads over XMPP and Stomp.

*Device state and MWI via PubSub in Asterisk*

[Asterisk](http://www.asterisk.org/), the well-known opensource telephony platform, integrates a feature (at the time of writing, waiting for testing) enabling to [broadcast the device states and the MWI](https://issues.asterisk.org/view.php?id=15757) (Message Waiting Indicator), using the XMPP's [publish-and-subscribe mechanism](https://xmpp.org/extensions/xep-0060.html).

*Telepaatti*

[Telepaatti](http://23.fi/telepaatti/) is IRC to Jabber/XMPP gateway compatible with MUC-protocol (Multi user chat). It allows you to join MUC-rooms and communicate with Jabber/XMPP users via your IRC client. Telepaatti acts as Jabber/XMPP client imitating IRC-server.

*mod\_ircd for Prosody*

[Matthew Wild](http://www.matthewwild.co.uk/) has written [mod\_ircd](http://code.google.com/p/prosody-modules/wiki/mod_ircd), an IRC to MUC gateway for [Prosody](http://prosody.im/), which allows joining Jabber chatrooms using an IRC client.

*Streaming Apple Events over XMPP*

Dan Brickley has released a Ruby script that [re-routes the Mac OS X Apple Remote event stream to XMPP](http://danbri.org/words/2009/10/19/483).

*Confbot: a Google Talk conference bot*

Perry Lorier has written and released [Confbot](http://coders.meta.net.nz/%7Eperry/jabber/confbot.php) under the GPL license. It is a python bot that enables group chats to Gtalk (and XMPP) users. It has been written in the early days of Gtalk, back in 2005.

*ejabberd\_testing: automated testing for ejabberd modules*

Eric Cestari has posted a [short article](http://cestari.wordpress.com/2009/10/27/ejabberd_testing-automated-testing-for-ejabberd-modules/) on his blog, pointing to [ejabberd\_testing](http://github.com/cstar/ejabberd_testing). The goal is is to be able to test ejabberd modules. It is released under the BSD license.

*jctalk*

Jongmyung Choi is coding the Smack-based [jctalk instant messaging](http://sourceforge.net/projects/jctalk/) system that is able to monitor and control home appliances.

*oai-pmh and xmpp*

Interesting read, Ed Summers experiments with [oai-pmh over XMPP](http://inkdroid.org/journal/2009/09/23/oai-pmh-and-xmpp/), where he takes advantage of XMPP to push updates, instead of constantly polling them. For the record, oai-pmh stands for [The Open Archives Initiative Protocol for Metadata Harvesting](http://www.openarchives.org/OAI/openarchivesprotocol.html).

*Oslo Protocol*

The [Oslo protocol](http://code.google.com/p/oslo-protocol/), released under a BSD license, describes a federated location sharing and proximity detection system, based on XMPP.

*ejabberd webpresence plugin for jQuery*

[Mahlon E. Smith](http://www.martini.nu/) has released a [jQuery plugin](http://plugins.jquery.com/project/ejabberd_presence) that shows a dynamic XMPP status badge, reflecting current presence information for a given XMPP account. Requires ejabberd's [mod\_webpresence](http://www.ejabberd.im/mod_webpresence).

*Musubi*

Teruaki Gemmahas has developped [Musubi](http://musubi.im/), a Firefox extension using xmpp4moz, that lets you create [online games and real-time apps](http://musubi.im/mediawiki/) in web pages.

*OneWeb*

ProcessOne has released OneWeb, an alpha Firefox extension ([desktop](http://www.process-one.net/en/blogs/article/oneweb_demonstrates_the_power_of_xmpp_inside_the_browser/) and [mobile](http://www.process-one.net/en/blogs/article/oneweb_works_on_firefox_mobile/)), that lets you manage and share bookmarks between browsers, with interoperation with regular XMPP chat clients.

*Jabber Feed 0.5*

Jehan has [announced Jabber Feed 0.5](http://jehan.zemarmot.net/blog/lang/all/2010/01/24/jabber-feed-0-5jabber-feed-0-5-released/) WordPress plugin, that lets articles and comments be posted on PubSub.

This is it, this software Roundup is over. We hope you enjoyed discovering new software, or just being informed of new releases and features. You are encouraged to talk about this Roundup and/or the software mentionned here you care about in your blogs and microblogs, in order to promote XMPP technologies further.
