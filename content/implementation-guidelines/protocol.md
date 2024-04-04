---
Title: XMPP Protocol Guidelines
---

## Overview

The XSF has published [over 400 XEPs](/extensions/) over many years. However as technology,
user expectations and best practices evolve, the protocol too is always evolving.

This leads to confusion about which set of XEPs are "current", which are required
only for backwards-compatibility, and which serve only to document experimental
protocols that never made it off the drawing board.

Instead of focusing on XEP numbers, this document simply focuses on the different
areas of functionality, and describes the currently-recommended XEPs that should be
used to implement each.

Notes are provided to provide context about past and future versions of the protocol,
which may be helpful for backwards-compatibility or planning future development.

### Target audience

The protocols discussed here should be implemented in reusable libraries. Client developers
may use this document to assist them in choosing an XMPP library, or submitting feature
requests or contributions to their library of choice.

Reusing libraries whenever possible reduces fragmentation and duplicated effort.

## Core

### Service discovery

One of the unique features of XMPP is its ability to support a diverse range of software
on a single network, yet always allow basic functionality to work.

Either due to the ongoing evolution of technology, or due to constrained environments (e.g. IoT)
or usage restrictions (e.g. accessibility), different XMPP software may support different
sets of features on top of the core messaging and presence functionality described in the
RFCs.

It is often useful to know what features a remote entity supports before performing some operation.
For example when deciding whether to send formatted messages, or determining the best available
method of transferring a file.

- [XEP-0030](/extensions/xep-0030.html) is the basic mechanism for advertising and discovering features
- [XEP-0115](/extensions/xep-0115.html) is a strongly recommended extension that allows caching of these features

#### Notes

[XEP-0115](/extensions/xep-0115.html) may be revised or replaced at some point in the future, such as by [XEP-0390](/extensions/xep-0390.html), to allow
hash agility and making the algorithm more robust to cache poisoning attacks.

### Resource generation

The client should generate a unique random identifier per device or client instance. The
identifier should be reused between sessions, and should not reveal any information
about the user, their device, or their location.

## Messaging

This section covers some protocols that are useful for general messaging.

### Formatting

The current recommendation is that developers may simply implement the rules in [XEP-0393](/extensions/xep-0393.html) for
formatting message bodies that they receive.

#### XHTML-IM deprecation

A previous formatting specification defined in [XEP-0071](/extensions/xep-0071.html) has been deprecated. Many implementations
failed to properly sanitize the formatted payload (it's tricky), leading to security issues
(particularly in web applications).

Implementation of [XEP-0071](/extensions/xep-0071.html) is not encouraged, but if formatting is a strong requirement along with
backwards compatibility (many clients still implement it currently), it remains an option if careful
attention is given to sanitizing the XHTML before display. Consider using [xhtml-im.js](https://github.com/zeen/xhtml-im.js) in a web client, or as a reference.

## Multi-device

XMPP was ahead of its time in supporting multiple devices connected to a single account - although
interestingly even today some popular messaging systems are still limited to a single device,
typically mobile, even when many people have a mobile, tablet and laptop or desktop.

Historically XMPP aimed to determine which device the user most likely wanted to receive messages
on - it did this using a 'priority' mechanism in presence. Over time bandwidth and CPU costs,
as well as user expectations, have shifted. Today most people want an "everything everywhere"
approach to messaging, where all their devices are in sync.

Modern XMPP clients should not set a priority in their presence, and they should implement the
following XEPs:

- [XEP-0280](/extensions/xep-0280.html): Message Carbons - for "live" synchronization of conversations between online devices
- [XEP-0313](/xep-0313.html): Message Archive Management - for "catch-up" of messages that were exchanged while a device was offline

### Known issues

There are currently some minor open issues regarding these protocols that developers should be aware of.

#### Race during login

There is a race condition during login between Carbons and MAM. If you synchronize with the archive first,
you may miss some messages sent to other devices before you enable Carbons.

If you enable Carbons first, you may receive duplicates from the archive of messages you already received.

The current best solution is to enable Carbons, perform the query, and de-duplicate any received messages
before presentation to the user.

This issue will be solved in the future through [XEP-0386](/extensions/xep-0386.html) or an alternative atomic "fetch and subscribe"
command.

#### IDs of outgoing messages

When a client sends a message, it is not currently possible for it to discover the ID that the
server assigned to the message in the archive. This means that it is unable to use them as synchronization
points and therefore it may receive its last outgoing message(s) when performing an archive sync.

Example:

1. Client receives message A, and records the ID so it can use
2. Client sends message B, but the ID is not known to the client
3. Client goes offline
4. Client comes online, and tries to sync with archive. Last known ID was of message A, so it synchronizes from that point
5. Server responds to the sync with message B, and all subsequent messages.

Solving this issue may happen through an extension of Carbons (to reflect sent messages back to the sender
with the ID added and any other additional info), or through a new MAM subscription protocol.

## Mobile

There are some special considerations that mobile clients can make to increase battery life and reduce
data consumption.

- [XEP-0286](/extensions/xep-0286.html) - informational XEP providing advice to mobile developers on efficient data usage
- [XEP-0352](/extensions/xep-0352.html) - used to inform the server of whether the client is currently active/focused (which allows
the server to prioritize traffic)

## Reliability

In the real world, it is normal for clients to get briefly disconnected. These extensions deal with
ensuring reliable message delivery and reporting.

- [XEP-0184](/extensions/xep-0184.html) - end-to-end acknowledgement, i.e. the recipient has successfully received the message
- [XEP-0198](/extensions/xep-0198.html) - hop-to-hop acknowledgement, and allows efficient resume of broken connections without data loss

## Read state synchronization

[Multi-device][#multi-device] support is all well and good but one thing
that further improves the experience is not having to dismiss
notifications and unread counters for messages that have already been
read on another device.

- [XEP-0280](/extensions/xep-0280.html): Carbon copies
  of replies, implying that prior messages have been read.
- [XEP-0333](/extensions/xep-0333.html): Chat Markers -
  to signal that messages have been shown to the user.

### Notifications

Avoid notifications while activity from another client is detected via
Carbons. Combine with Chat Marker tracking to determine whether to
notify after activity ceases, with some timeout.

## File transfer

Transferring a file from A to B is surprisingly a non-trivial problem for the internet, it seems.

A number of approaches have been tried in XMPP. They are documented here, and fall into two categories:
peer-to-peer and server-mediated.

It is strongly recommended for clients to implement HTTP upload to provide the best user experience.
The other mechanisms are optional (the advantages of implementing each one are documented in the
relevant section).

There are three file transfer methods that a modern XMPP client may implement:

- HTTP upload (required)
- Jingle streams (recommended for large file support)
- Stream initiation (deprecated, but may be implemented for backwards-compatibility)

### HTTP upload

**Required:** *yes*

The newest file transfer mechanism available, described in [XEP-0363](/extensions/xep-0363.html). It is strongly recommended to
implement this mechanism to provide the best user experience.

#### Benefits

- Does not depend on the recipient supporting it (simply falls back to sending a URL)
- Works with group chats
- Works when the recipient is offline
- Allows the recipient to receive on multiple devices

#### Disadvantages

- Unsuitable for large files (server determines what the size limit is, and may enforce usage quotas)
- Does not support streaming (file must be entirely uploaded to the server before recipient can begin to receive it)
- Requires server support

#### Communicating the URL

After uploading the file successfully, the sender should communicate the URL to the recipient by sending a
`<message>` stanza with the "Get URL" provided by the server in the `<body>` of the message.

Additionally the sender should include a [jabber:x:oob](/extensions/xep-0066.html#x-oob)
element in the message stanza with the same URL.

{{< info-block type="note" >}}
To enable automatic display of media in the conversation view, Conversations (at least) currently requires that the `<body>` contain *just* the URL, and it must be identical to the URL in the `jabber:x:oob` payload.  
The `<desc>` element is not used or supported by Conversations.  
This behavior means that it is not possible for any text to directly accompany a media file, and must be sent separately.
{{< /info-block >}}

### Jingle

**Required:** *optional - used for large file support*

Jingle is a generic framework that allows clients to negotiate a direct stream between themselves, which can
be used to transfer files (it is also used for voice/video and other p2p applications based on XMPP). It was
originally developed at Google and contributed to the XSF where it evolved into today's standard.

Because it is a generic framework that supports different underlying transports and different media types,
Jingle is split into multiple XEPs. For file transfer the following are relevant:

- [XEP-0166](/extensions/xep-0166.html) - the core Jingle framework
- [XEP-0234](/extensions/xep-0234.html) - the Jingle file transfer definition
- [XEP-0260](/extensions/xep-0260.html) - the most common transport mechanism for files (SOCKS5 Bytestreams - may be directly peer-to-peer or server-mediated)
- [XEP-0261](/extensions/xep-0261.html) - a fallback transport for tunneling the data directly over the XMPP stream (inefficient and slow, but always succeeds)

#### Advantages

- Supports streaming (recipient receives at the same time as the sender sends)
- Allows code re-use if the client also implements Jingle for audio/video streams
- No server-side storage required, and the data will pass directly between clients if firewalls/network conditions allow, which makes
it suitable for larger files.

#### Disadvantages

- Because it is a multi-purpose framework it can be complex.
- Not all clients support it.
- In the case of the recipient having multiple devices, only a single one can receive the file.
- Does not work for sharing a file with multiple people (e.g. in a group chat)
- Only works if the recipient is online

{{< info-block type="note" >}}
Although it is the only recommended negotiation protocol for peer-to-peer streams today, note that Jingle support is not nearly universal even among modern clients.
{{< /info-block >}}

### Stream Initiation (pre-Jingle)

**Required:** *no - optionally implement for sending large files to pre-Jingle clients*

[XEP-0096](/extensions/xep-0096.html) describes the stream negotiation protocol that was used before Jingle. It is widely supported, and can use the same
transports:

- [XEP-0065](/extensions/xep-0065.html)
- [XEP-0047](/extensions/xep-0047.html)

It is not recommended to implement this mechanism in new clients, except for compatibility with older clients
is required (and HTTP Upload does not suffice for some reason).

#### Advantages

- Supports streaming (recipient receives at the same time as the sender sends)
- Widely supported in older clients

#### Disadvantages

- Deprecated. Modern clients are switching to Jingle negotiation.
- In the case of the recipient having multiple devices, only a single one can receive the file.
- Does not work for sharing a file with multiple people (e.g. in a group chat)
- Only works if the recipient is online

## User Profiles

-   [XEP-0163](/extensions/xep-0163.html) is the base publishing method.
-   [XEP-0222](/extensions/xep-0222.html) for access controls.
-   [XEP-0084](/extensions/xep-0084.html) for profile picture.
-   [XEP-0172](/extensions/xep-0172.html) for nickname.
-   [XEP-0292](/extensions/xep-0292.html) for extended details (optional).

Simpler clients may choose to only use XEP-0084 and XEP-0172 to provide a limited user profile,
while more advanced clients could publish more details via XEP-0292.

### Avatars

-   **Do** publish avatars via XEP-0084.
-   **Do not** publish avatars via XEP-0292.

#### Format and size considerations

Use widely supported format such as PNG or JPEG.

The avatar must fit within stanza size restrictions, after being base64-encoded and wrapped in
protocol.  Recommended to keep the avatar no larger than 72 KiB which would keep resulting stanzas
under 100 KiB.

### Access control

Data published via [XEP-0163](/extensions/xep-0163.html) would by default be
available only to the user's contacts. Historically, profiles published via the legacy
[XEP-0054](/extensions/xep-0054.html) method were public.

Modern PEP implementations should implement for 'access model' as described by
[XEP-0222](/extensions/xep-0222.html), and allow users to share or limit their
personal details as they choose.

Access model for both XEP-0084 nodes and the XEP-0172 node should be kept the same.

Access to the full XEP-0292 profile, if supported, may be configured separately or via a tri-state
such as:

-   Everything contacts only
-   Public picture and nickname, private profile
-   Everything public

### Legacy

-   [XEP-0054](/extensions/xep-0054.html) is the legacy profile publishing method.
-   [XEP-0153](/extensions/xep-0153.html) notifies contacts about avatar changes.
-   [XEP-0398](/extensions/xep-0398.html) tells you whether you can ignore that and
    let the server do it for you.

## Group chat

See [Group Chat](/implementation-guidelines/groupchat).

## Contact management

### Blocking

- [XEP-0191](/extensions/xep-0191.html) for blocking communication with a list of other JIDs

## Encryption

All XMPP streams must be encrypted using TLS as specified in RFC 6920.

Clients may additionally support encrypting messages within the XMPP
stream. This can prevent untrusted servers from viewing or modifying
the contents of exchanged messages, and is known as 'end-to-end
encryption'.

The current preferred protocol for this in XMPP is OMEMO, specified
in [XEP-0384](/extensions/xep-0384.html). Client support is indicated at [omemo.top](https://omemo.top/).

### Notes

#### OTR

Prior to OMEMO, many clients implemented the protocol-agnostic
encryption protocol "OTR".

Although it sufficed for simple use cases (sender and recipient have
a single device connected, and both support OTR), it has a number of
drawbacks when used within XMPP. Traditionally it has not supported multiple devices
very well, nor group chats, and it only protects the message body.

These issues lead to a poor user experience.

Modern XMPP clients that implement OTR must add a [XEP-0380](/extensions/xep-0380.html) tag to their outgoing
messages.

#### MLS

The IETF is currently working on standardizing a new protocol for
['Message Layer Security'](https://datatracker.ietf.org/wg/mls/about/)
with support from a number of prominent members of the online communications
space. It is hopeful that it may one day allow messaging applications
of all protocols to share code and crypto reviewed by experts.

However this work is in its early days, and OMEMO is expected to be
the recommended approach for some time to come.
