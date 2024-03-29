---
title: The XMPP Newsletter, 31 January 2019
date: 2019-01-31
author: Seve, jcbrand
categories: ["Newsletter"]
aliases:
    - "/2019/01/the-xmpp-newsletter-31-january-2019/"
---

Welcome to the XMPP newsletter.

If you have an article, tutorial or blog post you'd like us to include in the
newsletter, please [submit it on the XMPP wiki](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

This week in Brussels we held the UI/UX Sprint, the [23rd XMPP Summit](https://wiki.xmpp.org/web/Summit_23) and
over the weekend many XMPP developers and enthusiasts will attend [FOSDEM19](https://fosdem.org/2019/).

{{< newsletter-subscribe >}}

## News

The [XMPP Standards Foundation (XSF) is applying as Google Summer of Code organization](https://xmpp.org/2019/01/google-summer-of-code-2019/)
and open source projects are invited to [submit project ideas](https://wiki.xmpp.org/web/GSoC/2019/Project_Ideas).

Process One has announced that they followed Basecamp's initiative and have became a
[Facebook-free business](https://blog.process-one.net/moving-away-from-facebook/).

Paul Schaub has written about how the new [OpenPGP for XMPP](https://xmpp.org/extensions/xep-0374.html) XEP
[solves the problem of encrypting arbitrary payload elements](https://blog.jabberhead.tk/2019/01/17/unified-encrypted-payload-elements-for-xmpp/)
and therefore overcomes some of the limitations arising from OMEMO due to the fact that it only
encrypts the message body.

\*Diaspora developer Dennis Schubert has written an [article explaining why he does not consider
ActivityPub as a viable base federation layer](https://schub.io/blog/2019/01/13/activitypub-final-thoughts-one-year-later.html)
for that project. He criticizes ActivityPub for not focusing enough on compliance
and claims that following the spec doesn't guarantee interoperability with other implementations.
As a positive counter-example, he presents XMPP and it's usage of XEPs and compliance specs.
It's an interesting perspective from someone not directly involved with XMPP.

Anu keeps on writing regular small blog posts about develoment of the Monal
client for iOs. You can [read his posts for January here](https://monal.im/2019/01/).

## FOSDEM

Members of the [Ignite Realtime](https://discourse.igniterealtime.org/t/ignite-realtime-goes-fosdem/84059),
[Prosody](https://blog.prosody.im/survey-2019-fosdem/) and [Salut à Toi](https://www.goffi.org/b/NQsienam2XDpRGbA5qHwTV/salut-fosdem-this-week)
communities will be attending FOSDEM in Brussels this weekend (2nd and 3rd February).

There will also be [5 XMPP-related talks](https://wiki.xmpp.org/web/FOSDEM_2019#Submitted_Talks) at FOSDEM this year.

## Tutorials

Linus Jahn, ([Kaidan](https://git.kaidan.im/kaidan/kaidan/)) developer,
explains [how to set up your own Ejabberd instance using Ansible](https://lnj.gitlab.io/post/ejabberd-ansible/).

Mike Kuketz has written [a guide in German on installing and running Ejabberd](https://www.kuketz-blog.de/ejabberd-installation-und-betrieb-eines-xmpp-servers/).
Here's the [Google Translate version](https://translate.google.com/translate?hl=&sl=de&tl=en&u=https%3A%2F%2Fwww.kuketz-blog.de%2Fejabberd-installation-und-betrieb-eines-xmpp-servers%2F).

## Software releases

## Clients

* Converse.js has reached version [4.1.0](https://github.com/conversejs/converse.js/releases/tag/v4.1.0).
* Gajim versions [1.1.1](https://dev.gajim.org/gajim/gajim/blob/gajim-1.1.1/ChangeLog) and [1.1.2](https://dev.gajim.org/gajim/gajim/blob/gajim-1.1.2/ChangeLog) have been released.

## Servers
* Prosody [0.11.2](https://blog.prosody.im/prosody-0-11-2-released/).
* OpenFire [4.3.0](https://discourse.igniterealtime.org/t/openfire-4-3-0-release/83843), [4.3.1](https://discourse.igniterealtime.org/t/openfire-4-3-1-release/83988)
  and [4.3.2](https://discourse.igniterealtime.org/t/openfire-4-3-2-release/84082).
* Tigase [7.1.5](https://tigase.net/blog-entry/tigase-xmpp-server-v715-released).

## Libraries

* slixmpp [1.4.2](https://github.com/poezio/slixmpp/releases/tag/slix-1.4.2).

## Other

[OTR version 4](https://github.com/otrv4/otrv4/blob/master/otrv4.md) has been
released. Highlights are improved deniability through "Deniable Authenticated Key Exchange" (DAKE) and
improved forward secrecy by using "Double Ratcheting".
