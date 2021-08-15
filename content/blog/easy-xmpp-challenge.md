---
title: "Easy XMPP: The Challenges"
date: 2017-08-14
author: ge0rg
categories: ["Easy XMPP"]
aliases:
  - "/2017/08/easy-xmpp-the-challenges/"
---

Over the last years, the XMPP community has had a hard time competing with
other Instant Messaging implementations, especially in the mobile / smartphone
ecosystems. By focusing a small part of our resources on user experience (UX),
we can gain significant improvements. This article is the first in a series of
"Easy XMPP" posts: easy ways for application developers to make XMPP easy to
use.

## Complexity of Federation

As opposed to most other Instant Messaging solutions, XMPP is a federated
protocol. That allows everyone to run their own servers, at the cost of
additional complexity for users:

* the user identifier always consists of a *user* and a *domain* part,
* there is no central registry that will consume your phone book and tell you
  who else is using XMPP,
* some servers might be running an older stack not supporting modern features,
  etc.

This inherent complexity, together with many developers' lack of attention to
good UX, have left us in a situation where on-boarding of new users and
finding contacts is painfully hard, especially when compared to
proprietary/centralized IM solutions.

It is not possible to remove the inherent complexity of federation without
replacing XMPP with a completely different protocol. However, there is another
federated system that is well established and used by people all over the
world: **email**. XMPP and email share the same basic principles - they are
federated, user identifiers are *user@domain* and it is possible (albeit less
common) to run your own server (or to get your own domain hosted with a
commercial provider).

By leveraging users' knowledge about how email works, learning from over forty
years of email evolution, and applying ideas from modern UX design on top, it
is possible to make XMPP easier to use today.

## Our Challenges

There are several areas where our community needs to improve. This post
provides an overview of the challenges we are currently facing in different
areas. Subsequent posts will dive deeper into the individual topics and
work out possible solutions.

### Terminology

The XMPP terminology is driven by technical requirements and exposes
complexities of the protocol. Normal IM users don't want to know about *PubSub
Publish Options*, *asymmetric presence subscription* in their *roster*, or
*MUC-PM Carbons*. All they care about is to see whether their friends are
online and that they can exchange cat pictures.

It is our task as the developer community to create understandable
abstractions of the technical complexities, and to set up a
[common glossary](https://wiki.xmpp.org/web/Usability/Glossary)
for the user-facing elements, including translations into common languages.
We need to define what the difference between "Jabber" and "XMPP" is, whether
the user identifier is a "JID", a "Jabber ID", an "XMPP address", or a "user
identifier", and fix all the other terms that are exposed to users and make
clients inconsistent today. And then we need to apply this glossary to our
implementations.

### First-time User Experience

The first-time user experience for IM users needs to be streamlined. The users
who need the most assistance are newcomers to the ecosystem who got invited by
a friend, and start out with nothing but their friend's Jabber ID. They need
help to accomplish these tasks:

* install a modern client
* create an account
* add their friend
* automatically find all their other friends
* find other users and chat rooms

Projects like [Easy XMPP Invitations](https://github.com/ge0rg/easy-xmpp-invitation),
[Pre-Authenticated Roster Subscription](https://xmpp.org/extensions/xep-0379.html),
and [invite URLs](https://modules.prosody.im/mod_invite.html)
are a first step in that direction, and getting them into your client today
will make new users' lives easier. But there is also potential to further
streamline the whole process.

### Easy Group Chats

There are two typical IM use cases for group chats: chat with friends or
family (private groups), or participate in a public chat room (typically for
support purposes, pioneered by
[Internet Relay Chat](https://en.wikipedia.org/wiki/Internet_Relay_Chat)).

The latter is well-covered by [MUC](https://xmpp.org/extensions/xep-0045.html),
and the upcoming [MIX](https://xmpp.org/extensions/xep-0369.html) should
provide a solid technical basis for both use cases. The next logical step is
to allow the easy
[creation and sharing of ad-hoc rooms](https://wiki.xmpp.org/web/Easy_Group_Chats)
between different clients, with a coherent user experience.

### Fighting Spam

If the amount of spam is a measure of XMPP's popularity, the network is doing
exceptionally well. Almost all of today's XMPP spam can be blocked with some
easy pattern matching rules, and the inevitable arms race will move to the
next round.

The community needs to prepare for that, by improving
[reporting between server operators](https://xmpp.org/extensions/xep-0161.html),
adding [anti-spam features into clients](https://xmpp.org/extensions/xep-0377.html) and
providing better whitelisting mechanisms to users.

## Call for Action

You can help making XMPP easier to use. As a user, you can contribute ideas,
add user stories, check your favorite client for confusing UI elements and
non-helping wizards, and report those to the developers.  As a developer, you
can streamline the on-boarding process in your client and contribute to the
[common glossary](https://wiki.xmpp.org/web/Usability/Glossary).

Get yourself a [wiki account](https://wiki.xmpp.org/web/Sysops) and start
hacking on [Easy XMPP](https://wiki.xmpp.org/web/Easy_XMPP) today!


