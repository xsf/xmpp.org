---
title: Summit Report
date: 2025-02-05
author: deuill
categories: ["XMPP Summit"]
---

# XMPP Summit 27 - January 2025

[Summit wiki page](https://wiki.xmpp.org/web/Conferences/Summit_27) | [Discussion channel](xmpp:summit@muc.xmpp.org?join) | [Code of Conduct](https://xmpp.org/extensions/xep-0458.html)

---
## Day 1

Topics proposed:

- Groupchat 3.0 ("GC3")
- HTTP Upload Retention
- User Account Configuration
- Spam reporting
- XMPP, Dutch healthcare, EU DMA
- MUC Push
- Server disco optimization
- IM Routing NG
- Device management (OMEMO)
- MIMI/MLS
- Foundation in EU

### GC3

- Presentation
- Feedback:
    - Daniel:
        - Most visible pain point for users is "Schrödinger's chat"
    - Andrzej:
        - Need to figure out nicks of participants who have left
    - Dave:
        - Submit it already
    - Marvin:
        - Consider privacy of traffic (e.g. iq) routed to bare JID
        - Look into MIMI room policy for ACL stuff

### HTTP Upload retention

Retention of uploaded files is not currently controllable by clients, but they may have use cases for longer or shorter periods of retention (e.g. avatars are long-term, while media attached to stories may be shorter).

Daniel's proposal: client specifies the "purpose" of the upload, and the server can use this as a hint about what policy (retention, quota, allowed MIME types, etc.) to apply.

Feedback:

- Named buckets?
- Assign priorities to uploaded files?
- Use XEP-0498 (uploaded file retraction is already handled) + pubsub#item_expire, XEP-0496 can be used for buckets. An upload profile as suggested by Daniel could be linked to those XEPs to automatically select suitable pubsub#expire value, node and permissions.

### Service discovery updates

- We need to optimize the recursive service discovery that happens at the start of a session
- We should define a standard way to find services of a given type (e.g. "As a client, what HTTP upload service do I use?")

Action items:

- Document Disco Items 2 (MattJ)
    - Include caps hash of item when known
    - Include category/type when known
- Informational "How to Disco" XEP (MattJ)

### XMPP and the EU

Talk by Winfried.

---

Break for lunch

---

### Lightning Talk: Reducing Pre-Connection Roundtrips

Work has been done on reducing post-connection roundtrips (SASL2/BIND2/FAST), but pre-connect roundtrips still an issue; SRV record lookup, A/AAA record lookup, TCP connection, TLS handshake. Good precedent for reducing roundtrips in QUIC.

Proposal to use SVCB records to compress lookups as much as possible; STARTTLS can be an issue but is on the way to be deprecated.

### User Account Configuration

Need to configure user preferences at the server level, across devices; e.g. spam preferences. Lots of protocol-specific configuration should've been made generic.

Feedback:

- Sensible way might be to be to define private PEP nodes.
- Any possible security issues in using PEP nodes?
- Another potential solution is declaring node subscriptions in BIND2.
- PEP feels like misuse, don't want clients submitting unvalidated data.
- Concern of using Pub-Sub on a JID is risk of misconfiguration; pushing private nodes and allowing other JIDs to potentially subscribe can be an issue.
- Would like to have option of reading configuration from PEP, and a different way (e.g. ad-hoc commands) of writing. Need server support for each payload, to allow for server-side validation. Can be use-case for special-case PEP. For account configuration, we assume server has support, but for MDS, configuration can be server-agnostic.
- Ad-hoc buys compatibility with existing clients, e.g. Gajim, Cheogram. Potential for both ad-hoc and new IQ method (which could be a PEP publish).
- Ad-hoc buys extensability so that the server can add new commands / items to configure and the client can support letting the user configure these without requiring special client knowledge ==> (Goffi) ~~ad-hoc doesn't advertise when there are new fields, meanwhile XEP-0346 does (new item in template node).~~ (maybe not useful in this use case)
- Breaking out each configuration into an individual PEP item.
- Goffi: In my Libervia Pubsub implementation, I have a node option to enforce template with XEP-0346, in which case invalid items are rejected. This can be used instead of Ad-Hoc commands, and we keep compatibility with most existing clients. This feature is generally desirable for Pubsub, so I may propose a protoXEP for that (just a well-known configuration option).

### Spam Reporting

A way to Spam

- xmppbl.org as a way to share banlists across services
- RTBL as a way to keep track of domains that send spam
- Re-using XEP-0377 

### OMEMO Device Management

New SASL2/BIND2 stack allows us to do device tracking, OMEMO has devices as well; before OMEMO goes stable is a good opportunity to add a mapping between two -- letting the server track of devices. Once connection is established we can do further optimizations.

If there's objection to extending existing OMEMO XEP, can move to new XEP.

Feedback:

  - MLS also has similar requirements to OMEMO (bundles/keying); is it worth trying to do something generic that OMEMO uses? Suggestion is using a common model for both OMEMO and MLS. 
    - Device management in general will be generic. Don't want to prematurely generalize.
    - Start by establishing link and do device management, then move to doing bundle management; will keep in mind future extensibility in terms of MLS.
  - Comes down to cleaning keys when devices go away?
    - Problem is also the constant announcing.
  - Does it imply moving away from PEP? Do we have a way to link PEP items to device IDs (e.g. so we can clean up pub-sub items connected to a device when it leaves)?
    - Having clients explicitly announce device IDs to servers is more robust; servers can also track themselves if they're willing to implement this. Plan for Prosody to implement this as a background feature, but would be better if it was part of PEP spec.
  - Is there existing workflow for moving to a new device -- converting history, moving keys, etc.
    - Not really.
  - What I (Daniel) ultimately want is device-to-device MAM.
  - Prosody has `mod_client_management`, need to submit that as a ProtoXEP; way to list clients, way to remove clients. In Prosody, have different types of clients you want to revoke, including clients with no SASL2 support. Handles things like OAUTH2 grants. Research was made how other online platforms handle device management and metadata.
  - If device is removed and OMEMO bundles are be removed, push registrations should also be removed.
    - Plan for doing this in Prosody quietly; behaviour should be documented in XEP.

### MIMI/MLS

Looked at protocol and have funding to implement in XMPP, no work done yet. MIMI; CBOR encoded inspired by MIME format, protocol-to-protocol format is based on HTTP.

Feedback:

  - What are they doing with addressing?
    - Not specified yet. Probably lookup mechanism based on email address and phone number; we could do something based on XMPP as well.
  - What parts are more relevant to XMPP community, MLS? MLS+Payload?
    - Probably would want to implement payload stuff, MLS has content-type annotations so can extend that with XMPP-specific MIME type. GC3 confirmed!
  - What are we trying to get out of MLS? Better encryption? Interop?
    - Interop is one thing, but is also superior for group-chats (even small ones); management is better. In MLS, state is handled on the MUC server rather than on each device. Hard to implement for direct messages for XMPP, focusing on group-chats. Might land on OMEMO for direct, MLS for group.
  - The fact that MLS is developed by IETF is a good plus, whether or not we interoperate.
  - The fact that MLS has libraries maintained, etc, is a good plus
  - It makes sense to focus on MLS where it shines, group-chats, then moving to implementing direct messages. Way closer to impelementing ordering of messages in MUC than direct. MLS requires strict ordering of messages.
    - Matrix cannot guarantee strict ordering, XMPP not for direct messages but can be implemented for MUCs.
  - Multiple devices makes this more complex?
    - Could probably get around strict ordering if not for multiple devices which can show up in the middle of a session.

---

End of day 1

---

## Day 2

### IMNG

Carbons, Message Routing, potentially GC3 or Spaces should go into XMPP 2.0. Currently planning a sprint in Berlin in May, get together and start implementing.

Feedback:

  - Business rules for IMNG -- for group-chat, there's no marking that IMNG is in place. Might be problematic because sending messages to bare JID might also be used for MUC Push. Intercept messages sent to bare JID when user is offline, and translate to push notifications on the server; used in Tigase and works.
  - We should have a clear idea what the routing rules are when a server talks to a single device vs. device-to-device.
    - Send to bare JID when sending to the user; server will route that in a rough carbon, send to the full JID if you want to go to specific client.
  - No known `normal` message types that IMNG helps with.
  - Routing rules for servers are quite unpleasant; end-goal is not just improving client-side routing, but improving server-side as well.
    - As a client, migrating to IMNG isn't attractive because Carbons is equivalent. Implementation should reflect what clients need.
  - Need to also figure out more complex routing rules (e.g. fallbacks when destination device is offline) beyond basic routing and addressing.
  - Idea: certain message types don't specify a message type on the message, but specify routing rules per-message; only for `type=normal` messages.

### MUC Push

How we should think about implementing MUC Push; different servers do different things, clients do different things. Should have MUC Push for GC3; if anyone is registered on MUC/GC3 room, MUC sends push messages to bare JID by default.

Feedback:

  - Avoid needing to have MUC/GC3 room to know which devices user has. If room doesn't know about devices, then having one device connected to MUC, then another offline and needing push leads to issues.
    - Solution could be to send all messages to bare JID.
    - Server could do distribution of messages. Clients should be able to cope when they're connected.
  - Tying XEPs together (IMNG/GC3 PAM) makes implementation slower on the server side at least.
    - Require to have GC3 PAM support to implement MUC Push.
      - Would be weird to have GC3 clients to also have them implement PAM. All servers and clients would have to retain non-GC3 logic anyways.
  - There is alternative method: having a push registration, persist the client's registration as under XEP-0198; no TCP connection but client is online-ish. It has benefits but requires more server-side state.
    - Agree it works, a lot of state that is pushed to the server is a waste of resources. Clients that are disconnected for a long period of time and don't reconnect has server hold onto all stanzas, in memory. Also take into account if client think it's connected but server is rebooted, all state is lost.
      - Was also problematic in MIX, but there you could depend on user's personal archive. User's MAM was source of truth even if push messages were dropped.
    - XEP-0198 at the S2S level will have an error message returned on misdelivery.

### Daniel: Two Half-Items

#### XEP Stabilization

Main argument against XMPP was "too many XEPs"; in role as Council Chair, Editor, etc. was taking us out of situation. Push XEPs to stable. Council chairs can't push XEPs to stable; only authors can do that. Please push any XEPs to last call if able.

If Stable is where many implementations exist, Experimental can become a playground again.

Feedback:

  - Is it worth investing a bit of time in automating. Fairly easy to have a system that iterates over XEPs.
    - Icons next to implementations in XEPs list; clock means "needs advancement/deferral".
      - Worth sending out emails in those cases?
    - Daniel: If Council Chair and Editor is the same seat, it makes job easier. Not sure if automation is helping much, but existing tooling on XEP page helps as Editor.
      - Not suggesting Silver Bullet, but maybe email notification.
        - Getting to Last Call as author is a lot of work; need to find the right moment for the author to push.
  - XEP advancement can be requested by approving body in addition to author; XEP might be proposed for advancement by anyone if abandoned by author.
    - Encouraging authors to lead helps makes process smoother; authors may not have all changes implemented for advancement.
    - Need a person, any person, to push through; by default it's the author but Council will generally not find another person unless XEP is visibily abandoned.
    - Finding another document shepherd isn't easy.
    - If people are keen enough to push XEP though, they might be also willing to be document shepherd, even if author is active but doesn't have bandwidth, but using normal process and relying on author is best way to go.
  - Reactions XEP has provisions for restrictions, relevant to gateways, but clients currently don't provide implementation.

#### Jingle File Transfer Last Call

Jingle File Transfer XEP is stuck in process, need to start discussion on the mailing list on pushing through; some edge-cases are apparently not covered. We know from Conversations crash reports that Jingle File Transfer is used.

Feedback:

  - Bunch of features in spec that are optional, and may not have had eyes. Large XEP, lots of features; need to do Last Call but need to review the whole XEP as well.
    - Might need to remove some parts (e.g. file request) before pushing through process.
    - XEP-0358 would replace file requesting.

### Lightning Talk: Goffi Experiments

Experimenting with remote control of (Galene) video conferences. Video conferencing in the terminal with Sixel/Kitty/Unicode half-blocks. Cool stuff!
