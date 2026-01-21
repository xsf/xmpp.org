---
title: MongooseIM 6.5 - Open for Integration
date: 2026-01-21
author: Paweł Chrząszcz (Erlang Solutions)
categories: ["Miscellaneous"]
---

# MongooseIM 6.5: Open for Integration

Our latest [release 6.5.0](https://github.com/esl/MongooseIM/releases/tag/6.5.0) of [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim) focuses on easier integration with your applications while continuing to deliver a scalable and reliable messaging server built on top of the extensible and battle-proven XMPP protocol.

For integration with other services, you can use the [Admin](https://esl.github.io/MongooseDocs/latest/graphql-api/Admin-GraphQL/) or [User](https://esl.github.io/MongooseDocs/latest/graphql-api/User-GraphQL/) GraphQL API. Another example is the interaction of MongooseIM with a database. A relational DB such as PostgreSQL, MySQL or CockroachDB can be used to store user accounts, message archives, multi-user chatrooms, publish-subscribe nodes, cluster nodes and much more. Other supported databases and storage services include Cassandra or Elastic Search for message archive, Redis for user sessions and LDAP for authentication.

You can see the [complete list](https://esl.github.io/MongooseDocs/latest/configuration/database-backends-configuration/) in our documentation.

There is another important way to let MongooseIM interact with your distributed system: **event pushing**. The core of this functionality is the [event pusher](https://esl.github.io/MongooseDocs/latest/modules/mod_event_pusher/) module, which can push selected events to services like [Amazon SNS](https://aws.amazon.com/sns/), [RabbitMQ](https://www.rabbitmq.com/) or [MongoosePush](https://github.com/esl/MongoosePush). In the most recent release 6.5.0, we have improved the event pushing mechanism, focusing on better integration with RabbitMQ.

## Event pushing in MongooseIM 6.5.0

The diagram below explains the event pushing architecture in the latest version of MongooseIM:

{{< figure src="/images/blog/mongooseim_events.png" >}}

Events utilize the concept of [hooks and handlers](https://esl.github.io/MongooseDocs/latest/developers-guide/Hooks-and-handlers/). Currently, events are triggered for a few selected hooks, e.g. when a user logs in/out or sends/receives a message. There are almost 140 different hooks defined in MongooseIM though, so there is much room for adding custom events. A module called `mod_event_pusher_hook_translator` handles the selected hooks, creating events and passing them to the main event pusher API function, `mod_event_pusher:push_event/2`.

Then, a hook called `push_event` is triggered, leveraging the hooks-and-handlers mechanism for the second time. This hook is handled by configurable service-specific backend modules, such as:

- `sns` – for sending notifications to Amazon SNS,
- `rabbit` – for sending notifications to RabbitMQ or CloudAMQP,
- `http` – for sending notifications to a custom service,
- `push` – for sending push notifications to mobile devices with the help of MongoosePush.

These modules act as interfaces to the corresponding external services. A key feature of this design is its extensibility. For example, one can easily add a `kafka` backend module that would deliver the events to Apache Kafka as shown on the diagram above.

### Push notifications

Let’s focus on the `push` module as it is a bit more complex. In general, it uses hooks and handlers once again – the `push_notifications` hook in particular. In order to actually deliver push notifications to a mobile device, a module called [mod_push_service_mongoosepush](https://esl.github.io/MongooseDocs/latest/modules/mod_push_service_mongoosepush/) handles that hook by sending the notifications to a separate service called [MongoosePush](https://github.com/esl/MongoosePush). Finally, MongoosePush will dispatch the notification request and send the notifications to configured services such as [APNs](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns) or [Google FCM](https://firebase.google.com/docs/cloud-messaging).

Each stage of this process is configurable and extensible. Firstly, we have assumed that a [virtual pubsub host](https://esl.github.io/MongooseDocs/latest/modules/mod_event_pusher_push/#virtual-pubsub-hosts) is used, but there is also an option to use a separate pubsub node for push notifications as described in [XEP-0357: Push Notifications](https://xmpp.org/extensions/xep-0357.html), adding another step before running the `push_notifications` hook. Speaking about that hook, you can implement your own module handling it by calling your own service instead of MongoosePush. Additionally, if you need to extend the notification logic with additional filtering and processing, you can implement a [plugin](https://esl.github.io/MongooseDocs/latest/modules/mod_event_pusher_push/#plugin-module) module to `mod_event_pusher_push`.

### Pushing events to RabbitMQ

The RabbitMQ backend module was improved and made production-ready in version 6.5.0, and our full [blog post](https://www.erlang-solutions.com/blog/mongooseim-6-5-open-for-integration/) shows how you can easily configure MongooseIM to push events to RabbitMQ - you can literally set up a working dockerized solution in a few minutes.

## Summary

The most important improvement in MongooseIM 6.5.0 is the production-ready integration with RabbitMQ, allowing external services to process the events from the server. It is worth noting that the mechanism is highly extensible – you can craft such extensions yourself, but of course don’t hesitate to [contact us](https://www.erlang-solutions.com/contact/) if you are considering using it in your business – we will be happy to help you install, configure, maintain, and – if necessary – customise it to fit your particular needs. For more information about the latest improvements, see the [release notes](https://github.com/esl/MongooseIM/releases/tag/6.5.0).

[Read about Erlang Solutions as sponsor of the XSF](/sponsors/erlang-solutions/).

{{< figure src="/images/logos/erlang-solutions.png" class="p-2 sponsor-logo" >}}
