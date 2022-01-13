---
Title: Internet of Things (IoT)
Url: uses/internet-of-things
aliases:
    - "/uses/internet-of-things.html"
---

**XMPP** is an excellent protocol for use within *Internet of Things*. The aim of this page, is to give a brief introduction to how XMPP can help build solid, secure and interoperable devices, services and applications for the *Internet of Things*. It is meant as a simple portal for people interested in IoT, providing links to more detailed information on each subject.


## A definition for the Internet of Things

While early pioneers into the field later named *Internet of Things*, or **IoT**, were quick to outline their visions of what the Internet of Things could become, the subject has lacked a clear *definition* of what it is, a definition with clear ramifications and consequences that can be studied, and under which different solutions can be compared. Before we embark on the journey of making claims of which protocol is the best for IoT, or if a protocol is good or bad at all, we need to establish some common ground. We therefore make the following definition:

| Internet of Things |
|--------------------|
|The *Internet of Things* (or **IoT**) is what we get when we *connect* *Things*, that are *not operated by humans*, to the *Internet*. |

This definition has some direct consequences that open up into different areas of study:

* **Connection** relates to the study of *communication protocols*, and in particular, how to [connect or bind](/uses/iot/bindings) to the network. XMPP provides various choices, such as [socket connections](/uses/iot/bindings#standard-xmpp-binding), [BOSH - Bidirectional streams over Synchronous HTTP](/uses/iot/bindings#bosh---bidirectional-streams-over-synchronous-http) and [EXI - Efficient XML Interchange](/uses/iot/bindings#exi---efficient-xml-interchange).

	**Connection** also relates to [communication patterns](/uses/iot/patterns). XMPP is particularly rich when it comes to supporting different communication patterns, such as [Request/Response](/uses/iot/patterns#requestresponse), [Asynchronous Messaging](/uses/iot/patterns#asynchronous-messaging), [Publish/Subscribe](/uses/iot/patterns#publishsubscribe), [Event subscription (Observe)](/uses/iot/patterns#event-subscription-observe) and [Delayed delivery](/uses/iot/patterns#delayed-delivery). XMPP also has support for different [Quality of Service levels](/uses/iot/patterns#quality-of-service) for messaging.

* **Things** relates to the study of all kinds of [things](/uses/iot/things) that can be connected, such as [sensors](/uses/iot/things#sensors), [actuators](/uses/iot/things#actuators), [controllers](/uses/iot/things#controllers) and other types of devices.

* **Not operated by humans** relates to [provisioning](/uses/iot/provisioning), [delegation of trust](/uses/iot/provisioning#delegation-of-trust), [automatic decision making](/uses/iot/provisioning#automatic-decision-making), but also [discovery](/uses/iot/provisioning#discovery).

* **Internet** relates to [scalability](/uses/iot/scalability), including topics such as [federation](/uses/iot/scalability#federation) and [global identity](/uses/iot/scalability#global-identity).

	**Internet** also relates very much to all kinds of [security](/uses/iot/security) related topics, such as [identities](/uses/iot/security#identity), [authentication](/uses/iot/security#authentication), [authorization](/uses/iot/security#authorization) and [encryption](/uses/iot/security#encryption) including [end-to-end encryption](/uses/iot/security#end-to-end-encryption).

	Another important aspect of the **Internet** is [interoperability](/uses/iot/interoperability). This includes topics such as [loosely coupled architectures](/uses/iot/interoperability#loosely-coupled-architectures) and [standardized interfaces](/uses/iot/interoperability#standard-interfaces).

As you will see, **XMPP** provides a lot of support into all these areas, making it well suited for use within the area of *Internet of Things*. To check current developments within XMPP and IoT, check the [Work in progress](/uses/iot/work-in-progress) page. There is also a page containing [testimonials](/uses/iot/testimonials).

## Realized example projects

Projects listed which are adopting XMPP for Internet of Things:

| Users         | System / Application            | Description                            | Since |
|---------------|---------------------------------|----------------------------------------|-------|
|  in the range of millions  | [Google Cloud Print](https://www.google.com/intl/en/cloudprint/learn/) | A cloud solution by Google to process documents to [printers](https://www.google.com/cloudprint/learn/printers/) without the need to install drivers. | 2010 |
|  in the range of billions | [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) | Cross-platform notification and message service (formerly Google Cloud Messaging) | 2014 |
|  in the range of millions | [Logitech Harmony Hub](https://www.logitech.com/en-us/product/harmony-hub) | System for [home automation and media remote control](https://www.theverge.com/2018/12/21/18152037/logitech-will-restore-third-party-harmony-home-automation) | 2004 |
| -        | [GitHub](https://github.com/COM8/esp32-xmpp-iot) repository | IoT reference implementation for [ESP32](https://www.espressif.com/en/products/socs/esp32/overview) microcontroller ([B.Sc. Thesis](https://home.in.tum.de/~sauterf/html-data/Thesis_Smart_Building_Control_with_XMPP_for_IoT.pdf)). | 2019 |

There are also projects like: [Jura E6 2019 platin (15326) IoT prototype](https://github.com/COM8/esp32-jura), controlled by XMPP.

## For more information

For more information regarding XMPP and IoT, check the following resources:

* [XMPP Internet of Things](http://www.xmpp-iot.org/) web site.
* [IoT on the XMPP Wiki](http://wiki.xmpp.org/web/Tech_pages/IoT_systems)
* [Learning Internet of Things](http://www.amazon.com/Learning-Internet-Things-Peter-Waher/dp/1783553537) book on Amazon, covering XMPP and IoT.
* [thingk.me](https://www.thingk.me/Provisioning/Api.xml) provisioning server for IoT.
