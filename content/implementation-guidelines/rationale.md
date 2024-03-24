---
Title: Rationale
---

This page gives additional insight into why some of the recommendations
in the Modern XMPP documentation are made.

## Group chats

Discussion about the UI/UX issues around group chats initially happened
at the first [UX sprint](meetings/2019-01-brussels.md). Some observations
were made:

* MUC configuration is messy, for users and developers
* Most MUCs fall roughly into a couple of standard configurations

### Types of groups

Software is about people. Good UX design is about understanding how
people use the software.

Group communication is a well-studied area of human interaction in
general[^wp-group-dynamics]. It has been noted by researchers that
groups can fall into four different types[^wp-group-types].

Of the four group types, two are formed of people that share a personal
or social connection (the so-called 'Primary' and 'Social' groups). Examples
include families, groups of friends, colleagues or clubs.

The other two group types ('Collective' and 'Category') are formed from
people who share common traits, goals or interests. Such groups tend
to be larger, less sticky, lack concrete social bonds and thus be more
open.

The developers of the Fractal IM client noted[^banquets-bbqs] the struggle
they faced trying to design an ideal UI for chats in their Matrix client.
They observed the two high-level categories which they termed "Barbecue"
(small, social-focused, closed, trusted) and "Banquet" (large,
topic-focused, open, untrusted).

The Fractal developers went as far to consider two completely separate
applications to cater for the two types of discussions.

Many other modern messaging apps contain both types of group chat, but
unlike most XMPP clients, they *do* distinguish them visually.

From a protocol perspective this distinction is unnatural - XMPP, like
similar open chat protocols such as IRC and Matrix cares little for how
the group is used, and provides various fine-grained configuration options.
Other than minor configuration tweaks there is little to distinguish the
two use-cases at a technical level.

However dividing these up at the UI level provides a number of advantages:

* Removes/reduces the need for fine-grained configuration options that users
    may not understand, or misuse
* Helps prevent user confusion when sharing content (it is harder to
    accidentally share family photos with an open-source project's chatroom
    full of strangers, if the family group and project group are strongly
    separated)
* Makes managing notification rules easier

#### Terminology

It was agreed that "room" terminology is outdated[^trend-chat-room], and not used by
any modern messaging systems. This deprecates "chat room", "occupant", "entering",
"leaving" and all room-related terminology.

Most applications these days use the terms "Chat" (Messenger), "Group" (WhatsApp, Signal)
or "Channel" (Slack, Discord, IRC).

Primary options are:

- "Chat"
    - Too ambiguous - clients may want to visually separate one-to-one chats
      from other kinds of chats, but if the term "Chats" is used for all of them,
      this is hard
- "Group" or "Group Chat"
    - Widely understood due to its use in all the most popular messaging apps
    - Even for those unfamiliar with such apps, "group" is a natural term for
      multiple people communicating together.
    - Still ambiguous regarding whether the chat is of the private or public kind
      (see above for the rationale on why these are fundamentally different, and should
      be displayed and treated differently). If public and private chats are handled
      so differently, they should have different names.
    - "Group" is already a term used by the roster, may be confusing
- "Private Group Chat" and "Public Group Chat"
    - Too wordy, ambiguous without the modifier (Public/Private), and perhaps doesn't
    adequately capture the differences between public/private chats.
- "Channel"
    - Successfully used by existing large platforms (mostly those focused primarily on
      group chats: Slack, Discord, IRC).
    - Used by Telegram to mean something different: a one-way broadcast from one user to many
    - Significantly different from 'Group Chat', no chance of confusion
    - Unfamiliar to people who haven't already used other communication tools that use
      this term
    - However, not a hard concept to grasp
    - Difficult to translate to other languages - literal translations such as "Kanal" (de)
      don't necessarily make sense.

<!-- Footnotes -->

[^wp-group-dynamics]: https://en.wikipedia.org/wiki/Group_dynamics
[^wp-group-types]: https://en.wikipedia.org/wiki/Group_dynamics#Types_of_groups
[^banquets-bbqs]: https://blogs.gnome.org/tbernard/2018/05/16/banquets-and-barbecues/
[^trend-chat-room]: Google Trends notes a significant decline since
    [at least 2004](https://trends.google.com/trends/explore?date=all&q=chat%20room).
