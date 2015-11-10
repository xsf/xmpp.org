---
Title: Internet of Things (IoT)
Url: uses/internet-of-things
Save_as: uses/internet-of-things.html
Parent_id: uses
Top_menu_show: false
Top_Menu_order: -1
Dropdown_menu_show: false
Footer_show: false
Sidebar_menu_show: true
Sidebar_menu_size: 4
Sidebar_menu_title: Uses of XMPP
Sidebar_menu_elem_name_1: Instant Messaging
Sidebar_menu_elem_url_1: uses/instant-messaging
Sidebar_menu_elem_name_2: Internet of Things
Sidebar_menu_elem_url_2: uses/internet-of-things
Sidebar_menu_elem_name_3: Social
Sidebar_menu_elem_url_3: uses/social
Sidebar_menu_elem_name_4: WebRTC
Sidebar_menu_elem_url_4: uses/webrtc
Content_layout: multiple-columns
---

**XMPP** is an excellent protocol for use within *Internet of Things*. The aim of this page, is to give a brief introduction to how XMPP can help build solid, secure and interoperable devices, services and applications for the *Internet of Things*.


## A definition for the Internet of Things

While early pioneers into the field later named *Internet of Things*, or **IoT**, were quick to outline their visions of what the Internet of Things could become, the subject has lacked a clear *definition* of what it is, a definition with clear ramifications and consequences that can be studied, and under which different solutions can be compared. Before we embark on the journey of making claims of which protocol is the best for IoT, or if a protocol is good or bad at all, we need to establish some common ground. We therefore make the following definition:

: Internet of Things :
:--------------------:
:The *Internet of Things* (or **IoT**) is what we get when we *connect* *Things*, that are *not operated by humans*, to the *Internet*. :

This definition has some direct consequences that open up into different areas of study:

* **Connection** relates to the study of *communication protocols*.
* **Things** relates to the study of *sensors*, *actuators*, *controllers* and other types of devices.
* **Not operated by humans** relates to *provisioning* and *automatic decision making*.
* **Internet** relates to *scalability* and *security*, including identities, authentication and authorization, but also to *interoperability*.

As you will see, **XMPP** provides a lot of support into all these areas, making it well suited for use withing the area of *Internet of Things*.

## Communication Protocols

One important aspect of **IoT** is how things connect to the Internet and how they can communicate with the outside world, and how the outside world in turn can communicate with the things. XMPP provides a stable and well tested extensible protocol that gives exceptional possibilities both to things and any applications wanting to communicate with them. The following subsections will outline why that is.

### Connection Bindings

When things and applications connect to the Internet using **XMPP**, they need to connect to the XMPP network using a **binding**. There are various options available, depending on the capabilities of the broker used to connect to the network.

#### Standard XMPP binding

This binding mechanism allows things to connect to the network using a normal bi-directional socket connection to the server. XML fragments are later sent both ways over this socket connection as part of the communication. This method is clearly outlined in the XMPP RFCs.

#### BOSH - Bidirectional streams over Synchronous HTTP

This binding mechanism allows clients that can only access the Internet using the HTTP protocol series (such as Javascript clients) to connect to the XMPP network. **BOSH** is described in [XEP-0206](http://xmpp.org/extensions/xep-0206.html).

#### EXI - Efficient XML Interchange

For small devices in resource constrained networks, XMPP can seem to verbose. Often network packets have to be small to not be fragmented, such as is the case if using 6LowPan IPv6 radio networks. To allow such devices to use the powers of XMPP, an **EXI** binding is available. EXI, or Efficiant XML Interchange, is an exceptionally efficient way of compressing XML, using knowledge derived from the XML schemas, and allows XML fragments to be compressed to sizes suitable for resource contrained networks. **EXI** binding is described in [XEP-0322](http://xmpp.org/extensions/xep-0322.html). 

## Communication Patterns

#### Request/Response

#### Asynchronous Messaging

#### Publish/Subscribe

#### Event subscription (Observe)

### Quality of Service

## Scalability

### Federation

### Global identity

## Things

### Sensors

### Actuators

### Controllers

### Concentrators

## Provisioning

### Delegation of Trust

### Discovery

## Security

### Identity

### Authentication

### Authorization

### Encryption

### End-to-end encryption

## Interoperability

### Loosely coupled architectures

### Standard interfaces

## Work in progress

## For more information
