---
title: Uncontrolled Resource Consumption with Highly Compressed XMPP Stanzas
aliases:
    - "/community/security-notices/uncontrolled-resource-consumption-with-highly-compressed-xmpp-stanzas.html"
---

_Original Release Date: 2014-04-04_

_Last Updated: 2014-04-15_

## Overview

Several XMPP server implementations that support application-layer compression ([XEP-0138](/extensions/xep-0138.html)) suffer from an uncontrolled resource consumption vulnerability ([CWE-400](https://cwe.mitre.org/data/definitions/400.html)). This vulnerability can be remotely exploited by attackers to mount Denial-of-Service attacks by sending highly-compressed XML elements over XMPP streams.

## Description

XMPP stream compression is a desirable feature that reduces the amount of data transferred between the protocol principals. In XMPP, compression can be negotiated at the TLS layer (as described in [RFC 6120](https://datatracker.ietf.org/doc/html/rfc6120)) or at the application layer (as described in [XEP-0138](/extensions/xep-0138.html)). The vulnerability that has been discovered applies specifically to application-layer compression; such compression is negotiated between an XMPP client and server (or two servers) as follows:

1. An XMPP server supporting application-layer compression advertises it in the stream feature message:

```xml
<stream:features>
  <starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>
  <compression xmlns='http://jabber.org/features/compress'>
    <method>zlib</method>
    <method>lzw</method>
  </compression>
</stream:features>
```

2.  The client selects one of the advertised compression algorithms:

```xml
<compress xmlns='http://jabber.org/protocol/compress'>
  <method>zlib</method>
</compress>
```

3.  If no errors occur, the server agrees on the choice with the following message:

```xml
<compressed xmlns='http://jabber.org/protocol/compress'/>
```

After a successful negotiation, all the subsequent protocol messages are compressed.

When decompressing XMPP stanzas, an XMPP server must limit the resources
allocated to this task. If the server fails to do that, it can monopolize the
CPU usage and allocate all the available memory. As a result, remote attackers
can exploit this vulnerability to mount a Denial of Service attack (DoS) by
submitting highly-compressed XML elements over an XMPP stream (we call these
“xmppbombs” for short).

An "xmppbomb" is a valid XML element sent over an XML stream but containing a
huge number of white spaces. See for example the following element sent during
stream negotiation (e.g., on a stream restart after TLS negotiation):

```xml
<?xml version='1.0' ?>
<stream:stream $SPACES to='$SERVER'
	xmlns='jabber:client'
	xmlns:stream='http://etherx.jabber.org/streams'
	version='1.0'>
```

where $SPACES is a 4GB long string of spaces and $SERVER is the server domain
name. By using the zlib compression algorithm, it is possible to compress the
above message to 4MB (compression ratio of ~1:1000).

[XEP-0170](/extensions/xep-0170.html) on "Recommended Order of
Stream Feature Negotiation" suggests to negotiate stream compression after the
authentication of the principals. This suggests that xmppbombs can be used only
after the user authentication. However, it has been reported that some
implementations allow the use of compression before the authentication phase
therefore opening up this vulnerability to unknown attackers.

## Impact

Affected servers are reported to:

1.  Consume the virtual memory; in certain cases, it has been reported that servers are terminated by the operating system for out of memory conditions;
2.  Monopolize the use of the CPU;
3.  In certain cases, not allow administrators to disable stream compression.

## Solution

It is best to upgrade to corrected server code. An alternative, temporary workaround is to disable XMPP-level compression.

## Vendor Information

The following table provides information about existing XMPP server implementations. To the best of our knowledge it is accurate and complete, but server administrators are advised to check with the developers of their preferred server software to verify the information provided here.

| Vendor 		| Product 				| Status 		| Contacted 			| Updated 	|
|-			|-					|-			|-				|-		|
| Apache		| Vysper				| Unknown		| 2014-03-12, >2014-04-03	| Unknown	|
| Apple Inc.		| iChat Server				| Unaffected		| 2014-03-12			| N/A		|
| Cisco Systems, Inc.	| Jabber XCP				| Unaffected		| 2014-03-12			| N/A		|
| Citadel		| Citadel				| Unaffected		| 2014-03-12, 2014-04-03	| N/A		|
| CommuniGate		| CommuniGate Pro			| Unaffected		| 2014-03-12			| N/A		|
| Coversant		| SoapBox Server			| Unknown		| 2014-03-12, 2014-04-03	| Unknown	|
| djabberd		| djabberd				| Unknown		| 2014-03-12, 2014-04-03	| Unknown	|
| Erlang Solutions	| MongooseIM				| Fixed in 1.3.2	| 2014-04-03			| 2014-04-15	|
| Google		| Google Talk				| Unknown		| 2014-03-12, 2014-04-03	| Unknown	|
| IBM			| Lotus Sametime Gateway		| Unaffected		| 2014-03-12, 2014-04-03	| N/A		|
| IceWarp		| IceWarp Instant Messaging Server	| Unknown		| 2014-03-12, 2014-04-03	| Unknown	|
| igniterealtime.org	| Openfire				| Fixed in 3.9.2	| 2014-03-12			| 2014-04-03	|
| inetdextra		| in.jabberd				| Unknown		| 2014-03-12, 2014-04-03	| Unknown	|
| Isode Ltd.		| M-Link				| Fixed in 16.0v7	| 2014-03-12			| 2014-03-31	|
| jabberd 1.x		| jabberd 1.x				| Unaffected		| 2014-03-12, 2014-04-03	| N/A		|
| jabberd 2.x		| jabberd 2.x				| Unaffected		| 2014-03-12			| N/A		|
| j-livesupport		| Jerry Messenger			| Unknown		| 2014-03-12, 2014-04-03	| Unknown	|
| Kwickserver		| Kwickserver				| Unaffected		| 2014-03-12, 2014-04-03	| N/A		|
| lightwitch.org	| Metronome				| Fix in progress	| 2014-04-03			| TBD		|
| ProcessOne		| ejabberd				| Unaffected		| 2014-03-12			| N/A		|
| Prosody		| Prosody				| Fixed in 0.9.4	| 2014-03-12			| 2014-04-02	|
| psyced		| psyced				| Unaffected		| 2014-03-12, 2014-04-03	| N/A		|
| Siemens		| Siemens OpenScape			| Unaffected		| 2014-03-12, 2014-04-03	| N/A		|
| Tigase		| Tigase				| Fixed in 5.2.1	| 2014-03-12			| 2014-03-30	|
| Vines			| Vines					| Unaffected		| 2014-03-12, 2014-04-03	| N/A		|
| Wokkel		| Wokkel				| Unknown		| 2014-03-12, 2014-04-03	| Unknown	| 

Note: Although it is likely that a number of the servers with a status of “unknown” do not support XMPP-layer compression and therefore are not vulnerable to this uncontrolled resource consumption vulnerability, we have not heard from the developers of such servers and therefore cannot provide definitive information.

## References

*   [CWE-400: Uncontrolled Resource Consumption (‘Resource Exhaustion’)](https://cwe.mitre.org/data/definitions/400.html)
*   [RFC 6120: Extensible Messaging and Presence Protocol (XMPP): Core](https://datatracker.ietf.org/doc/rfc6120/)
*   [XEP-0138: Stream Compression](/extensions/xep-0138.html)
*   [XEP-0170: Recommended Order of Stream Feature Negotiation](/extensions/xep-0170.html)

## Credits

The vulnerability was reported by Giancarlo Pellegrino. This report was written by Giancarlo Pellegrino with assistance from Peter Saint-Andre.

## Feedback

If you have feedback, comments, or additional information about this vulnerability, please send email to the [security@xmpp.org discussion list](https://mail.jabber.org/mailman/listinfo/security).
