---
Title: Internet of Things (IoT) - Bindings
Url: uses/iot/bindings
---

## Communication Protocols

One important aspect of **IoT** is how things connect to the Internet and how they can communicate with the outside world, and how the outside world in turn can communicate with the things. XMPP provides a stable and well tested extensible protocol that gives exceptional possibilities both to things and any applications wanting to communicate with them. The following subsections will outline why that is.

### Connection Bindings

When things and applications connect to the Internet using **XMPP**, they need to connect to the XMPP network using a **binding**. There are various options available, depending on the capabilities of the broker used to connect to the network.

#### Standard XMPP binding

This binding mechanism allows things to connect to the network using a normal bi-directional socket connection to the server. XML fragments are later sent both ways over this socket connection as part of the communication. This method is clearly outlined in the XMPP RFCs [RFC 6120](https://tools.ietf.org/html/rfc6120), [RFC 6121](https://tools.ietf.org/html/rfc6121) and [RFC 6122](https://tools.ietf.org/html/rfc6122).

#### BOSH - Bidirectional streams over Synchronous HTTP

This binding mechanism allows clients that can only access the Internet using the HTTP protocol series (such as Javascript clients) to connect to the XMPP network. **BOSH** is described in [XEP-0206: XMPP Over BOSH](/extensions/xep-0206.html).

#### EXI - Efficient XML Interchange

For small devices in resource constrained networks, XMPP can seem to verbose. Often network packets have to be small to not be fragmented, such as is the case if using 6LowPan IPv6 radio networks. To allow such devices to use the powers of XMPP, an **EXI** binding is available. EXI, or Efficiant XML Interchange, is an exceptionally efficient way of compressing XML, using knowledge derived from the XML schemas, and allows XML fragments to be compressed to sizes suitable for resource contrained networks. **EXI** binding is described in [XEP-0322: Efficient XML Interchange (EXI) Format](/extensions/xep-0322.html). 
