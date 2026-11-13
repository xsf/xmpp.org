---
title: London XMPP Sprint Review
date: 2026-11-13
author: Polarian
categories: ['Events', 'Sprints']
summary: "Review of the London XMPP Sprint in 2026"
---

{{< figure src="/images/blog/lxs2026-room.jpg" caption="London XMPP Sprint" >}}
{{< figure src="/images/blog/lxs2026-plushies.jpg" caption="Dino and Beastie have become good friends!" >}}

From Friday 6th November to Sunday 8th November, 8 XMPP community members
meet for London XMPP Sprint in Greenwich.

For more information about the sprint see the
[wiki](https://wiki.xmpp.org/web/Sprints/2026-11_London).

## Monal IM

[Matthew Fennell](https://wiki.xmpp.org/web/User:MatthewFennell) and [Thilo
Molitor](https://wiki.xmpp.org/web/User:TMolitor) worked on improving the
Monal internals and made progress on chatview.

## Conversations

[Daniel Gultsch](https://wiki.xmpp.org/web/User:Daniel) implemented Oauth
within Conversations with help from [Matthew
Wild](https://wiki.xmpp.org/web/User:MattJ).

## Dino

Fixah worked on message style parsing within Dino.

[Marvin Wißfeld](https://wiki.xmpp.org/web/User:Larma) worked on fixing
multiple bugs within Dino's file transfer feature, with Karel Balej helping
with debugging the bugs.

## BSD Compatibility

[Polarian](https://wiki.xmpp.org/web/User:Polarian) worked on porting the
latest version of Gajim to FreeBSD, unfortunately being beaten by another
user to submitting the patch, and worked on updating gajim dependencies
within FreeBSD. Polarian also worked on improving his build server to be
able to port more XMPP software to BSD in the future.

## Discussions

* HTTP file upload deletion, which resulted in a [PR being
  submitted](https://github.com/xsf/xeps/pull/1584).
* Oauth implementation details, this was mainly discussed between Daniel and
  Matthew Wild during the implementation of Oauth for conversations.
* Spaces implementation details, concerns were raised about spaces
  impersonating existing MUCs.
* Permission synchronisation between MUCs.

## Thanks to

* [Matthew Fennell](https://wiki.xmpp.org/web/User:MatthewFennell) for
  organising the sprint, handling the communications with the venue, and
  funding the sprint.
* [Polarian](https://wiki.xmpp.org/web/User:Polarian) co-hosting the event,
  handling the outreach, writing the majority of the wiki and writing the
  blogposts for the event.
