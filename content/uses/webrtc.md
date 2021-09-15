---
Title: WebRTC
Url: uses/webrtc
aliases:
    - "/uses/webrtc.html"
---

## WebRTC + XMPP = <3
WebRTC is a free, open project that provides browsers and mobile applications with real-time communications capabilities.

Jingle, the XMPP framework for establishing p2p sessions, makes for a great pairing with WebRTC. 

XMPP is particularly a great fit with WebRTC in settings where there is a desire to pair WebRTC audio/video calls with text chat, but the advantages of XMPP 

Because WebRTC is a peer-to-peer protocol, multi-user experiences become exponentially complex. Pairing a WebRTC service with XMPP allows developers to dramatically reduce this complexity.

## Projects using WebRTC with XMPP

There are many people pairing WebRTC with XMPP. 

The [Jitsi Videobridge](https://jitsi.org/Projects/JitsiVideobridge) uses the [COLIBRI XEP](/extensions/xep-0340.html) to manage connections and conference mixing. 

[Jitsi Meet](https://jitsi.org/Projects/JitsiMeet) is an open source instant videoconferencing web application, which uses XMPP.

Combining Jitsi videobridge and Jitsi Meet into a single package, [Openfire Meetings](https://github.com/igniterealtime/community-plugins/tree/master/ofmeet) makes WebRTC video conferences simple to deploy and use.

[Otalk](http://otalk.org) is an open-source platform for building realtime applications using XMPP. [Talky](http://talky.io) is an example of an application built using these libraries.
