---
Title: Myths & Legends
Url: about/myths
aliases:
    - "/about/myths.html"
---

XMPP seems to have some interesting myths, too. As typical with myths, many of these are made up. Here's some of our (least) favourite:

## XMPP is XML, so it's too slow.

The hypothesis:
> XML is inarguably slower than JSON and other similar syntaxes, and XMPP will subsequently suffer in terms of performance.

The fact:
> XML is just as fast as JSON, and therefore XMPP pays no penalty.

JSON, in particular, is often heralded as being better in all possible ways than XML. In reality, while JSON can be constructed in slightly fewer bytes, that's really its only advantage. You may think this is a key advantage for mobile, in which case hold on there for Myth Three.

In "typical" parsers, XML and JSON perform more or less identically in practice. It's worth noting that there are a number of high-performance XML parsers, but comparatively few high-performance JSON parsers, too.

But even ignoring the high performance, specialist end, XML still holds its own. Consider [these findings](https://www.balisage.net/Proceedings/vol10/html/Lee01/BalisageVol10-Lee01.html), for example.

## XMPP is not secure.

The hypothesis:
> XMPP is not secure.

The fact:
> XMPP offers state-of-the-art end-to-end encryption, and a relatively high-degree of pseudonymity

"Secure" is not an absolute. In order to decide whether XMPP is secure, you need to decide what you want to be secure against. No system that relies on servers is secure against for example a rogue administrator (end-to-end encryption can protect your message contents even against a rogue admin, but only if you verify keys appropriately). Instead, our specifications consistently remind developers of the risks of various choices. Plenty of XMPP extensions will certainly increase the risk for both for the users and for the administrator - including allowing registration and password changing via the protocol.

Different deployment patterns radically alter the security, too. XMPP is designed by its nature to be highly flexible. This is why it is used by everything from gamers to militaries and nation states, and from telephone switchboards to the video game handhelds. Security that suits the military will rarely suit the average internet user, and vice-versa - XMPP strives to handle all of these, and it's certainly possible to configure a server to provide much worse security - or much better. That said, basic security is both encouraged and provided for; and this is most effective when using a server you trust. One way of trusting your server administrator is, of course, to be your own server administrator. This may sound obvious, but XMPP has from its outset ensured that this is always an option; even on low-budget.

Some messaging systems will expose less metadata. Some will ensure and enforce end to end encryption. Some will allow for federation, which inevitably increases the metadata involved. Others will sacrifice server-side message handling entirely, trading user-experience for reduced exposure. The system-specific issues raised will affect any messaging system to some degree - sometimes better, and sometimes worse.

The community vision remains as it always has - that users are enabled to make their own choices about their client software, server software, and the people involved in both. We think XMPP enables exactly this.

Finally, XMPP specifications usually contain a "Security Considerations" section where developers are made aware of the risks of various choices.

## XMPP is not privacy-friendly.

The hypothesis:

> XMPP is not privacy-friendly.

The fact:

> As any other system, XMPP will interact with metadata and privacy must be enforced by the implementation and server administrators.

XMPP enables in most aspects privacy-friendly implementations and usage. But there are no absolutes here. By using XMPP - or any other system - you give access to your metadata to some degree. XMPP is certainly not the system with the least metadata available to an observer, especially an observer with access to your server. But no single server administrator can possibly see all the metadata you provide via your interactions.

By allowing federation, XMPP provides the user with the ability to self-host their own server, to choose which server administrator to trust, or even to split trust over several servers by using multiple accounts. Remote servers from contacts will only see the relevant metadata that concerns them.

## The baseline is minimal, therefore XMPP is useless.

The hypothesis:
> The core of XMPP is so small it has no practical use, and features that are essential for my use case have been bolted on as an afterthought.

The fact:
> XMPP is designed to be extensible, and many extensions have very broad deployment.

"It's a feature, not a bug" is the obvious thing to say here. XMPP's core, [RFC 6120](/rfcs#6120), does not even include the "classic" IM features, really; those are present in its companion specification, [RFC 6121](/rfcs#6121). As a protocol that's [nearly fifteen years old](/about/history.html), had the core been constantly redesigned to add new capabilities as new mandatory, baked-in features, lots of existing servers would have been redeclared as broken.

Instead, what we have is a [pretty large number of extensions](/extensions/index.html) to a clean core. This core defines, amongst other things, how to extend the core properties of the connection - but in fact the community designed an end-to-end extension system early on.

While you can still connect a client that supports no extensions at all to a server and have it work, nearly every client supports a wide range of extensions suited to its purpose, and every server supports several.

## Everybody implements different, incompatible extensions

The hypothesis:
> There are so many different XMPP extensions, sometimes for the same task, that everybody implements a different subset of them and no implementation is compatible with another one.

The fact:
> The [Compliance Suites](/about/compliance-suites) outline which extensions are needed to implement typical tasks like *IM*, *Mobile* or *Web*, both for servers and for clients.

The XSF is keeping an up-to-date list of the extensions that are recommended to fulfill typical tasks with the Compliance Suites.
They define XMPP application **Categories** based on typical use cases (*Core*, *Web*, *IM*, *Mobile*) and **Levels** (*Core*, *Advanced*) based on functionality in the respective category. For each combination of those, the required XEPs are referenced. As the protocol landscape changes over time, Compliance Suites are updated roughly once a year.

For developers, Compliance Suites provide guidance on which specifications they need to consider when implementing an application of a certain kind. By completing a compliance test or performing a self-assessment, they can advertise their implementation as compliant with a given **Category** and **Level**.

For users, Compliance Suites provide an easy way to compare implementations based on their respective advertised compliance levels and year.

## It's too bandwidth-inefficient for mobile.

The hypothesis:
> XMPP stanzas are just too verbose to work on mobile.

The fact:
> XMPP has been successfully deployed over SATCOM and HF.

You might think that, because XML is known to be relatively verbose compared to other serialization formats, that this would be a problem in low bandwidth. However, XMPP's use of XML is actually quite concise - it's really nothing like the uses you see in, say, SOAP - and XMPP has been used (and is still used) over some ridiculously slow links.

SATCOM links tend to run at around 9600 - that's the same speed as a GSM data call, which won't help you because you'll have never made one. The latency is around 30s. HF, on the other hand, runs considerably lower, and is half-duplex to boot - it'll run down to around 9 bits/s, and with radio turnaround times at the 2 minute mark every time you need to switch direction, that's almost glacial.

Yet XMPP still works - at least as well as anything else. Isode have an excellent whitepaper on this: [M-Link Support for XMPP over Constrained Networks](http://www.isode.com/whitepapers/low-bandwidth-xmpp.html), but the majority of XMPP running over SATCOM are ordinary open source servers such as Openfire.

On mobile, the most concerning cost is the stream startup time - because it uses a sequence of round trips - but extensions such as [XEP-0198](/extensions/xep-0198.html) can help reduce this substantially.

And as said before, XMPP is a NAK protocol - traffic doesn't get acknowledged in the success case normally, only on error. If you examine protocols specifically designed for low-bandwidth, you'll find the same design prevails.

Compare this with any protocol that is based on JSON over HTTP - HTTP/1.1 is an amazingly verbose protocol, so the overhead of each transaction is going to be quite astonishing - and every HTTP API command must be acknowledged with a response. HTTP/2.0 may help with this, of course, but the overhead doesn't vanish entirely.

XMPP has been used over mobile for years, and while [XEP-0357 &quot;Push Notifications&quot;](/extensions/xep-0357.html) is relatively new, that's in part because mobile platforms other than Apple's simply haven't required it - Android clients work fine without, for example - and as a community we've been working with mobile as a focus for a number of years (see [XEP-0286 &quot;Mobile Considerations&quot;](/extensions/xep-0286.html)).

## XMPP is unreliable without a bunch of extensions.

The hypothesis:
> XMPP stanzas can be lost, therefore the system is unreliable.

The fact:
> XMPP typically uses reliable stream transports, so even without extensions it's pretty reliable.

There's a classic problem in computer communications called the [Two generals problem](https://en.wikipedia.org/wiki/Two_Generals%27_Problem)

On the TCP binding - the normal one people use - TCP gives XMPP a slew of features in order to minimize any failure case. If you receive a stanza over TCP, you can be totally assured that every stanza beforehand in the stream has arrived safely - mitigating the Two Generals to the point that only the last few messages sent are subject to it. This is important, and I'll come back to it. WebSockets are the same; they, too, run over a continuous TCP stream.

It's easy to take this for granted, but take a look at [BOSH - the HTTP binding for XMPP](/extensions/xep-0124.html) - here, the transport has no such reliability to offer, so the community had to add in the same guarantees, with resend timers, buffering, and so on. In fact, any system based around HTTP polling must do something fairly intensive in order to get basic reliability, so it's no surprise that when viewed from that angle, the utter lack of visible support for reliability seems like there's something crucial missing.

So if this is the case, then the question becomes why did we need any extensions anyway? There's two cases, each addressed in a different way - though both involve "acks".

The first is that XMPP is, by default, a NAK protocol (see the &quot;It's too bandwidth-inefficient for mobile&quot; Myth). This is great for bandwidth, but it's a little disconcerting since it's nice to know people are getting your messages - their client hasn't crashed, their connection hasn't dropped, and so on. So [XEP-0184](/extensions/xep-0184.html) exists to fill that gap - you can ask the other client for an Ack, and when the client has received your message, it'll send one back.

But if you don't get one back, there's no way to tell if it was the message that was lost or the ack, and there's no very obvious way to handle the situation anyway. Do you send another? Or will the client get the message from offline storage? Do you care?

This is where [XEP-0198 &quot;Stream Management&quot;](/extensions/xep-0198.html) comes in. The community developed this extension because TCP sessions are a lot less reliable over mobile — now a number of servers support it, and many mobile clients (particularly the Android ones) will use it if available.

XEP-0198 extends TCP's reliability across multiple sessions, and also extends it through to the application. It, too, sends acks on request, but only across a single link. So a client and server can maintain a buffer of sent stanzas, and if they're not acked (and they must be acked in sequence, just like TCP) then when the client reconnects, it can resume the XMPP session (and both ends can resend any missed stanzas).

This mitigates the Two Generals to the point that only the last few messages sent within a session are subject to it, and only then if resuming the session was somehow impossible.

So wait, doesn't this mean that XMPP, even with all these extensions, is still unreliable in some cases? Isn't the hypothesis - that XMPP stanzas can be lost sometimes - still true? Sure it is. The Two Generals problem is [provably insoluble](https://en.wikipedia.org/wiki/Two_Generals%27_Problem#Proof) - anyone claiming that their communications system is 100% reliable is making the network communications equivalent of saying they have a perpetual motion machine, and I'm not *that* much of an idiot.

XMPP is, however, as reliable as a protocol can practically be.

## XMPP is unsuited to the web.

The hypothesis:
> XMPP is unsuited to the web because angle brackets and stuff.

The fact:
> XMPP has been successfully deployed to thousands of websites and has had pure Javascript libraries since its early days.

OK, I admit, I'm not a web guy, and I really don't understand the idea that because XMPP, like HTTP, isn't based around JSON, and because it instead uses angle brackets, like HTML, it should never be used on the web. Really, this bewilders me. XML is a web technology, after all, albeit it's not nearly as popular as it once was. Bindings like BOSH have been used for literally years to provide solid XMPP over HTTP, and libraries like Strophe.js handled a full XMPP stack in the browser sandbox amazingly well, due to the native (and fast - see Myth One) support for XML in the browser.

But I accept that many sensible people feel strongly that any self-respecting web-based API should involve passing JSON strings about, and the good news is that there's at least two libraries for you that present XMPP in exactly this way.

Stanza.io operates purely client-side, using the standard XMPP bindings for HTTP long-poll (BOSH) and WebSockets (both supported by any modern server) to give an amazingly powerful and broad JSON API.

On the other hand, XMPP-FTW uses a server-side thin proxy to translate the XML-based standard TCP session (supported by every server) into a JSON API, presented over traditional browser tech like Primus, allowing the client session to switch between transports on the fly.

And not only that, but they're the same JSON translator code, now, so switching between them is as comfortable as it gets.

You can even make WebRTC calls using XMPP's Jingle signalling technology from one stack to another, or indeed to the original Strophe.js library too - hardly surprising, since Jingle hugely influenced the capabilities of WebRTC during its design. In fact, desktop XMPP clients are actually playing catch-up on this front, because WebRTC pushed the boundaries so quickly - on that front, at least, one could argue that XMPP is more at home on the web than it is anywhere else.
