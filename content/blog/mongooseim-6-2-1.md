---
title: Scaling up with MongooseIM 6.2.1
date: 2024-05-28
author: Paweł Chrząszcz (Erlang Solutions)
categories: ["Miscellaneous"]
---

[MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) is a scalable, extensible and efficient real-time messaging server that allows organisations to build cost-effective communication solutions. Built on the XMPP server, MongooseIM is specifically designed for businesses facing the challenge of large deployments, where real-time communication and user experience are critical. The main feature of the recently released [MongooseIM 6.2.1](https://github.com/esl/MongooseIM/releases/tag/6.2.1) is the improved [CETS in-memory storage backend](https://esl.github.io/MongooseDocs/latest/configuration/internal-databases), which simplifies and enhances its scalability.

It is difficult to predict how much traffic your XMPP server will need to handle. This is why MongooseIM offers several means of scalability. Firstly, even one machine can handle millions of connected users, provided that it is powerful enough. However, one machine is not recommended for fault tolerance reasons, because every time it needs to be shut down for maintenance, upgrade or because of any issues, your service would experience downtime. As a result, it is recommended to have a cluster of connected MongooseIM nodes, which communicate efficiently over the [Erlang Distribution protocol](https://www.erlang.org/doc/apps/erts/erl_dist_protocol.html). Having at least three nodes in the cluster allows you to perform a *rolling upgrade*, where each node is stopped, upgraded, and then restarted before moving to the next node, maintaining fault tolerance. During such an upgrade, you can increase hardware capabilities of each node, scaling the system vertically. Horizontal scaling is even easier, because you only need to add new nodes to the already deployed cluster.

## Mnesia

[Mnesia](https://www.erlang.org/doc/man/mnesia.html) is a built-in Erlang Database that allows sharing both persistent and in-memory data between clustered nodes. It is a great option at the start of your journey, because it resides on the local disk of each cluster node and does not need to be started as a separate component. However, when you are heading towards a real application, a few issues with Mnesia become apparent:

1. Consistency issues, which tend to show up quite frequently when scaling or upgrading the cluster. Resolving them requires Erlang knowledge, which should not be the case for a general-purpose XMPP server.
2. A persistent volume for schema and data is required on each node. Such volumes can be difficult and costly to maintain, seriously impacting the possibilities for automatic scaling.
3. Unlike relational databases, Mnesia is not designed for storing huge amounts of data, which can lead to performance issues.

First and foremost, it is highly recommended not to store any persistent data in Mnesia, and MongooseIM can be configured to store such data in a relational database instead. However, up to version 6.1.0, MongooseIM would still need Mnesia to store in-memory data shared between the cluster nodes. For example, a shared table of user sessions is necessary for message routing between users connected to different cluster nodes. The problem is that even without persistent tables, Mnesia still needs to keep its schema on disk, and the first two issues listed above would not be eliminated.

## Introducing CETS

Introduced in version 6.2.0 and further refined in version 6.2.1, [CETS](https://github.com/esl/cets) (Cluster ETS) is a lightweight replication layer for in-memory ETS tables that requires no persistent data. Instead, it relies on a discovery mechanism to connect and synchronise with other cluster nodes. When starting up, each node registers itself in a relational database, which you should use anyway to keep all your persistent data.

Getting rid of Mnesia removes a lot of important obstacles. For example, if you are using [Kubernetes](https://kubernetes.io), MongooseIM no longer requires any persistent volume claims (PVC's), which could be costly, can get out of sync, and require additional management. Furthermore, with CETS you can easily set up horizontal autoscaling for your installation.

## See it in action

If you want quickly set up a working autoscaled MIM cluster using Helm, see the detailed [blog post](https://www.erlang-solutions.com/blog/instant-scalability-with-mongooseim-and-cets). For more information, consult the [documentation](https://esl.github.io/MongooseDocs/latest/), [GitHub](https://github.com/esl/MongooseIM) or the [product page](https://www.erlang-solutions.com/technologies/mongooseim). You can [try MongooseIM](https://trymongoose.im/) online as well.

[Read about Erlang Solution as sponsor of the XSF](https://xmpp.org/sponsors/erlang-solutions/).

{{< figure src="/images/logos/erlang-solutions.png" class="p-2 sponsor-logo" >}}
