---
title: Easy XMPP: The Challenges
date: 2017-08-08
author: ge0rg
blog_id: blog
category: Easy XMPP
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

We can not remove the inherent complexity of federation without replacing XMPP
with a completely different protocol. However, there is another federated
system that is well established and used by people all over the world:
**email**. XMPP and email share the same basic principles - they are
federated, user identifiers are *user@domain* and it is possible (albeit less
common) to run your own server (or to get your own domain hosted with a
commercial provider).

We can leverage users' knowledge about how email works, learn from over forty
years of email evolution, and apply ideas from modern UX design on top, to
make XMPP easier to use today.

## Our Challenges

There are several areas where we as a community need to improve. This post
focuses on terminology and the first-time user experience. Topics that will be
covered by subsequent posts are contact discovery, group chats, handling of
spam, and more.

### Terminology

The XMPP terminology is driven by technical requirements and exposes
complexities of the protocol. Normal IM users don't want to know about *PubSub
Publish Options*, *asymmetric presence subscription* in their *roster*, or
*MUC-PM Carbons*. All they care about is that their messages can
be read by the respective receiver.

It is our task as the developer community to create understandable
abstractions of the technical complexities, and to set up a
[common glossary](https://wiki.xmpp.org/web/Usability/Glossary)
for the user-facing elements, including translations into common languages.

We need to define what the difference between "Jabber" and "XMPP" is, whether
the user identifier is a "JID", a "Jabber ID", an "XMPP address", or a "user
identifier", and many other terms that are exposed to users and make clients
inconsistent today. And then we need to apply this glossary to our
implementations.

### First-time User Experience

We need to streamline the first-time user experience for IM users. The users
who need the most assistance are newcomers to the ecosystem who got invited by
a friend, and start out with nothing but their friend's Jabber ID. We need to
help those users:

* install a modern client
* create an account
* add their friend
* find other users and chat rooms

Projects like [Easy XMPP Invitations](https://github.com/ge0rg/easy-xmpp-invitation),
[Pre-Authenticated Roster Subscription](https://xmpp.org/extensions/xep-0379.html),
and [invite URLs](https://modules.prosody.im/mod_invite.html)
are a first step in that direction, and getting them into your client today
will make new users' lives easier. But there is also potential to further
streamline the whole process.

### Call for Action

You can help making XMPP easier to use. As a user, you can contribute user
stories, check your favorite client for confusing UI elements and non-helping
wizards, and report those to the developers.  As a developer, you can
streamline the on-boarding process in your client and contribute to the
[common glossary](https://wiki.xmpp.org/web/Usability/Glossary).

Get yourself a [wiki account](https://wiki.xmpp.org/web/Sysops) and start
hacking on [Easy XMPP](https://wiki.xmpp.org/web/Easy_XMPP) today!


