---
Title: Internet of Things (IoT) - Communication Patterns
Url: uses/iot/patterns
---

## Communication Patterns

*Communication patterns* are architectorial concepts describing how messages are transported in the network to accomplish certain tasks. Knowledge of these patterns are important to be able to correctly design and implement applications and scale networks of things accordingly, so that functional and performance requirements are met.

#### Request/Response

The **Request/Response** communication pattern is one of the most basic communication patterns. It allows a *client* to request information from a *server* in *real-time*. The words "client" and "server" are here used purely to illustrate the roles of the participants in the pattern, not to describe the hierarchy in the network. Most commonly, they are peers in the network.

XMPP provides an intrinsic method to implement a generic Request/Response mechanism, by use of the **iq** stanza built into XMPP. This allows one client to request information from another. What information is defined by the contents of the **iq** stanza. The receiver of the request is informed of whom originated the request, and the client is also informed from whence the response came.

For proprietary applications in IoT, the **iq** stanza might be sufficient. But there are instances where it is not. One such instance is if the response is slow to be collected, and partial results have to be returned to show progress. This might be the case when communicating with devices behind gateways, behind which very slow communication protocols are used. Another important instance, is if [interoperable](#interoperability) solutions are desired. In such cases, proprietary solutions create walled gardens that are difficult to integrate in larger contexts.

To facilitate the creation of an *open* and [loosely coupled](#loosely-coupled-architectures) architecture that enable [interoperability](#interoperability) between things and applications, [XEP-0323: Internet of Things - Sensor Data](/extensions/xep-0323.html) was created. It defines a Request/Response mechanism where sensor data can be read from devices asynchronously. Apart from the normal request/response mechanism provided by the **iq** stanza, it allows for slow responders and defines a data format that can be used to encapsulate sensor data in an interoperable manner. It is designed to allow new types of devices to be added to networks without the need to upgrading software to perform basic tasks, such as sensor data readout, machine processing of data and presentation of data to human users. It also allows devices from different manufacturers and applications from different developers to exchange data seemlessly.

![IoT Request/Response](/images/iot/reqresp.png)  
*Example of asynchronous Request/Response flow in [XEP-0323](/extensions/xep-0323.html)*

#### Asynchronous Messaging

The **Asynchronous Messaging** communication pattern allows peers in the network to asynchronously send messages in *real-time* between each other when they decide to, not when requested. This is done by encapsulating the content of the message into a **message** stanza, which is built into XMPP. The receiver of a message is always informed who sent the message.

To facilitate the interchange of IoT-data in asynchronous messages between things from different manufacturers, IoT data can be encapsulated using the sensor data format defined in [XEP-0323: Internet of Things - Sensor Data](/extensions/xep-0323.html) or control format defined in [XEP-0325: Internet of Things - Control](/extensions/xep-0325.html).

#### Publish/Subscribe

The **Publish/Subscribe** pattern allows for mass distribution of information to interested parties in an efficient manner. It reduces network traffic by up to half, by allowing the publisher of information to send its information only once to a publish/subscribe server, who then retransmits it to subscribers. The *Publish/Subscribe* pattern is more efficient than other patterns, such as *Request/Response* or *Asynchronous Messaging* if the following conditions are met:

* Information does not have to be updated in *real-time* for continous values (non-discrete values).
* Information does not have to be updated on *demand*.
* Published information is actually used.

If, on the other hand, *real-time* access to information of continous values (non-discrete values), or access to information on-demand, or if only small portions of generated data is to be used, other communication patterns are more efficient.

Example of IoT use cases where data is more efficiently distributed using Publish/Subscribe than using other patterns:

* Public sensors with massive base of uniform users that will use the data.
* Sensor data where storage of historical values using well-defined intervals is important.
* Data is uniform without need to be adapted to use case or user.
* Data is not confidential.

Examples of IoT use cases where data might be better distributed using other patterns:

* Individual control actions
* Monitoring sensors in real-time
* User base have completely different requirements on the data, intervals and content.
* Data is tailored to the receiver, for instance using provisioning capabilities.
* Data is confidential.

The Publish/Subscribe pattern is defined in [XEP-0060: Publish-Subscribe](/extensions/xep-0060.html). To facilitate the interchange of IoT-data using the publish/subscribe pattern to mass distribute information, IoT data can be encapsulated using the sensor data format defined in [XEP-0323: Internet of Things - Sensor Data](/extensions/xep-0323.html) or control format defined in [XEP-0325: Internet of Things - Control](/extensions/xep-0325.html).

![IoT Publish/Subscribe](/images/iot/pubsub.png)  
*Example of Publish/Subscribe flow*

| Calculation Example |
|---------------------|
| Consider a temperature sensor measuring outside temperature. People who wants to use it to see outside temperature will want to have sufficiently recent information in order for it to be of interest. In order to use Publish/Subscribe pattern to distribute this temperature, a relatively short time-interval is therefore of interest. Let's assume a 15-minute interval is sufficient. This implies *N=96* values are published per day. If *n&middot;E* is the expected or average number of values that are actually being used by users per day, where *n* is the number of users and *E* is the expected number of values that each user uses per day (they might actually only view the application once a day), we see that the number of messages distributed in the network, if only one broker is involved, is *2&middot;N+n&middot;N*, if notification with payload is used, or *2&middot;N+n&middot;(N+2&middot;E)*, if notification without payload is used. However, if Request/Response is used instead, *4&middot;n&middot;E* messages are sent (counting messages to and from broker separately). The break-even point between Publish/Subscribe and Request/Response in these examples is therefore (if notification with payload is used) *N&le;4&middot;n&middot;E/(2+n)&rarr;4&middot;E* as *n&rarr;&infin;*. In our example, we would need users to use at least *E=N/4=96/4=24* temperature values before the Publish/Subscribe pattern is more efficient than the Request/Response pattern. Such is normally the case only if all historical values are used on the receiving end.
![IoT Publish/Subscribe](/images/iot/pubsubreqrespbreakeven.png)
While the above calculation compared Publish/Subscribe with Request/Response, a similar relationship exists between Publish/Subscribe and Event subscription (Observe) in the distribution of data that is event-driven.|

#### Event subscription (Observe)

#### Delayed delivery

### Quality of Service
