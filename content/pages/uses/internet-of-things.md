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

**XMPP** is an excellent protocol for use within *Internet of Things*. The aim of this page, is to give a brief introduction to how XMPP can help build solid, secure and interoperable devices, services and applications for the *Internet of Things*. It is meant as a simple portal for people interested in IoT, providing links to more detailed information on each subject.


## A definition for the Internet of Things

While early pioneers into the field later named *Internet of Things*, or **IoT**, were quick to outline their visions of what the Internet of Things could become, the subject has lacked a clear *definition* of what it is, a definition with clear ramifications and consequences that can be studied, and under which different solutions can be compared. Before we embark on the journey of making claims of which protocol is the best for IoT, or if a protocol is good or bad at all, we need to establish some common ground. We therefore make the following definition:

| Internet of Things |
|--------------------|
|The *Internet of Things* (or **IoT**) is what we get when we *connect* *Things*, that are *not operated by humans*, to the *Internet*. |

This definition has some direct consequences that open up into different areas of study:

* **Connection** relates to the study of *communication protocols*, and in particular, how to [connect or bind](uses/iot/bindings) to the network. XMPP provides various choices, such as [socket connections](uses/iot/bindings#standard-xmpp-binding), [BOSH - Bidirectional streams over Synchronous HTTP](uses/iot/bindings#bosh---bidirectional-streams-over-synchronous-http) and [EXI - Efficient XML Interchange](uses/iot/bindings#exi---efficient-xml-interchange).

	**Connection** also relates to [communication patterns](uses/iot/patterns). XMPP is particularly rich when it comes to supporting different communication patterns, such as [Request/Response](uses/iot/patterns#requestresponse), [Asynchronous Messaging](uses/iot/patterns#asynchronous-messaging), [Publish/Subscribe](uses/iot/patterns#publishsubscribe), [Event subscription (Observe)](uses/iot/patterns#event-subscription-observe) and [Delayed delivery](uses/iot/patterns#delayed-delivery). XMPP also has support for different [Quality of Service levels](uses/iot/patterns#quality-of-service) for messaging.

* **Things** relates to the study of all kinds of [things](uses/iot/things) that can be connected, such as [sensors](uses/iot/things#sensors), [actuators](uses/iot/things#actuators), [controllers](uses/iot/things#controllers) and other types of devices.

* **Not operated by humans** relates to [provisioning](uses/iot/provisioning), [delegation of trust](uses/iot/provisioning#delegation-of-trust), [automatic decision making](uses/iot/provisioning#automatic-decision-making), but also [discovery](uses/iot/provisioning#discovery).

* **Internet** relates to [scalability](uses/iot/scalability), including topics such as [federation](uses/iot/scalability#federation) and [global identity](uses/iot/scalability#global-identity).

	**Internet** also relates very much to all kinds of [security](uses/iot/security) related topics, such as [identities](uses/iot/security#identity), [authentication](uses/iot/security#authentication), [authorization](uses/iot/security#authorization) and [encryption](uses/iot/security#encryption) including [end-to-end encryption](uses/iot/security#end-to-end-encryption).

	Another important aspect of the **Internet** is [interoperability](uses/iot/interoperability). This includes topics such as [loosely coupled architectures](uses/iot/interoperability#loosely-coupled-architectures) and [standardized interfaces](uses/iot/interoperability#standard-interfaces).

As you will see, **XMPP** provides a lot of support into all these areas, making it well suited for use withing the area of *Internet of Things*. To check current developments withing XMPP and IoT, check the [Work in progress](uses/iot/work-in-progress) page. There is also a page containing [testimonials](uses/iot/testimonials).

## For more information

For more information regarding XMPP and IoT, check the following resources:

* [XMPP Internet of Things](http://www.xmpp-iot.org/) web site.
* [IoT on the XMPP Wiki](http://wiki.xmpp.org/web/Tech_pages/IoT_systems)
* [Learning Internet of Things](http://www.amazon.com/Learning-Internet-Things-Peter-Waher/dp/1783553537) book on Amazon, covering XMPP and IoT.
* [thingk.me](https://www.thingk.me/Provisioning/Api.xml) provisioning server for IoT.
