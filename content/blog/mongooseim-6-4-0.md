---
title: MongooseIM 6.4 - Simplified and Unified
date: 2025-08-22
author: Paweł Chrząszcz (Erlang Solutions)
categories: ["Miscellaneous"]
---

[MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim) is a scalable and efficient instant messaging server. It implements the open, proven, extensible and constantly evolving XMPP protocol, which is an excellent choice when it comes to instant messaging. To communicate with other XMPP entities, the server uses three main types of interfaces, listed in the table below.

| XMPP Interface | Purpose | Connection type | Reworked in version |
|---|---|---|---|
| C2S (client-to-server) | Accept connections from XMPP clients | inbound | 6.1.0 – 6.4.0 |
| S2S (server-to-server) | Federate with other XMPP servers | inbound/outbound | 6.4.0 |
| Component | Accept connections from external components | inbound | 6.4.0 |

The C2S interface was reworked and improved already in version 6.1.0 (see the [blog post](https://www.erlang-solutions.com/blog/mongooseim-6-1-handle-more-traffic-consume-less-resources/)), making it more modern, organised and extensible. In the most recent version 6.4.0, this trend is continued by reworking the S2S and component interfaces while unifying the whole connection handling logic.

### Simplified, unified and more complete

Connection accepting and handling was simplified and unified in multiple ways, allowing the addition of new features along the way. All connections are now accepted by [ranch](https://github.com/ninenines/ranch), a state-of-the-art socket acceptor pool for Erlang. Modern [gen_statem](https://www.erlang.org/doc/apps/stdlib/gen_statem.html) behaviour is then used to handle open connections using state machines. These changes allowed for improved handling of various corner cases, removing unexpected limitations and mishandled error conditions. There is also improved separation of concerns, resulting in easier extensibility and configurability.

Another unified and improved system aspect is the **TLS encryption**. The legacy `fast_tls` library is now fully replaced with the Erlang implementation, resulting in much more straightforward configuration and implementation without a drop in performance (as evidenced by rigorous load tests). This change made it possible to fill in some gaps in functionality, such as the support for *channel binding* as required for TLS 1.3 (see [RFC 9266](https://datatracker.ietf.org/doc/rfc9266/) for details). Additionally, TLS is now supported for component connections. Moreover, CA certificates can be provided by the OS, reducing the need for manual certificate provisioning. As a result of these changes, your MongooseIM installation will be more secure and robust.

All these changes are reflected in the [TOML configuration file](https://esl.github.io/MongooseDocs/latest/configuration/configuration-files/#mongooseimtoml). When compared with the previous version of MongooseIM, there are the numerous improvements such as the following:
- Components can benefit from TLS connections.
- S2S options are separate for the incoming (`listen.s2s`) and outgoing (`s2s.outgoing`) connections. Common options are placed directly in the `s2s` section (e.g. `default_policy`).
- Traffic shapers are configured the same way for all types of connections, and are always referenced by their names.
- S2S outgoing connections can have traffic shaping enabled.
- All TLS options follow the same pattern throughout the configuration file. This also affects multiple options that were omitted from this example for simplicity.

Another improved layer is the **instrumentation**. Most changes affect XMPP traffic events.
For example, there used to be an event called `c2s_element_in`, emitted when an XML element is received on a C2S connection.
A separate event called `c2s_xmpp_element_size_in` was emitted to measure element size. Now, there is one event called `xmpp_element_in` - and it covers measurements from both previous events. Event names are now more concise, making them easier to remember and reason about. This was possible due to the use of labels like `connection_type` and `host_type`.
Additionally, event coverage got improved, e.g. `xmpp_element_in` now covers S2S and component connections as well. Also, the events are emitted more consistently. For incoming data, there is always one event emitted as soon as an XML element (most often a stanza) is parsed. For outgoing data, there is always one event emitted just before sending an XML element out. As a result, the metrics are consistent with actual network traffic. For more information, see the [documentation on metrics](https://esl.github.io/MongooseDocs/latest/operation-and-maintenance/MongooseIM-metrics/#list-of-metrics). Our [blog post](https://www.erlang-solutions.com/blog/mongooseim-6-3-prometheus-cockroachdb-and-more/) about release 6.3.0 can also give you more details about the instrumentation layer and its integration with Prometheus.

## SASL 2, Bind 2, FAST

Over the past few releases, we have been implementing extensions speeding up the XMPP stream negotiation and authentication:

- [XEP-0388](https://xmpp.org/extensions/xep-0388.html): Extensible SASL Profile (SASL2) allows a client to authenticate, resume its session and more in one round-trip.
- [XEP-0386](https://xmpp.org/extensions/xep-0386.html): Bind 2 allows a client to bind the resource and enable selected extensions (SM, carbons, CSI) as part of SASL2.
- [XEP-0484](https://xmpp.org/extensions/xep-0484.html): FAST allows a client to authenticate with a token as a part of SASL2. According to the specification, this is a token-based method for streamlining authentication in XMPP, enabling fully authenticated stream establishment within a single round-trip.

### FAST features supported in MongooseIM

In version 6.4, additional advanced features of FAST are supported. One of them is **token rotation**: the server invalidates tokens after a configurable period, and provides a new token on reconnection if the current one is close to expiry (this period is also configurable). Additionally, a client can request immediate token invalidation – with or without requesting a new one. Another addition is the support for **0-RTT** (zero round-trip time) data in TLS 1.3 (see [RFC 8446, section 2.3](https://datatracker.ietf.org/doc/html/rfc8446#section-2.3)). The FAST token can be provided by the client during a subsequent handshake after reconnection, meaning that there is no additional round-trip needed after the handshake – hence the name “0-RTT”. A different extension is the `tls-exporter` **channel binding** in TLS 1.3 (see [RFC 9266](https://datatracker.ietf.org/doc/rfc9266/) for details) – it can be used with FAST, resulting in the channel binding data being passed with the FAST token, increasing the security. Note that currently it cannot be used with 0-RTT data. See the documentation for [mod_fast_auth_token](https://esl.github.io/MongooseDocs/latest/modules/mod_fast_auth_token/) and the [Hashed Token SASL Mechanism](https://datatracker.ietf.org/doc/draft-ietf-kitten-sasl-ht/00/) specification for more information.

## What's next?

You can read more about MongooseIM 6.4 in the detailed [blog post](https://www.erlang-solutions.com/blog/mongooseim-6-4-simplified-and-unified/). You can also find more information in the [release notes](https://github.com/esl/MongooseIM/releases/tag/6.4.0). Don’t hesitate to visit our [product page](https://www.erlang-solutions.com/technologies/mongooseim/), [try it online](https://trymongoose.im/) and [contact us](https://www.erlang-solutions.com/contact/) if you are considering using it in your business.

[Read about Erlang Solutions as sponsor of the XSF](/sponsors/erlang-solutions/).

{{< figure src="/images/logos/erlang-solutions.png" class="p-2 sponsor-logo" >}}
