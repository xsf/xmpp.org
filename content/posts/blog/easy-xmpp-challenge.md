---
title: Easy XMPP: The Challenge
date: 2017-03-13 12:47
author: Georg
blog_id: blog
---

TL;DR:
* XMPP is federated and based on e-mail-like user identifiers
* UX is harder than with centralized/proprietary messengers
* Providing UX equal to proprietary messengers = hard problem
* huge potential for big improvements in 90% solution
* "Easy XMPP" = solving the easy problems of making XMPP easy for users

## Challenges

* Terminology
* User Onboarding & Roster Invitations
* Group Chats

### Terminology

* XMPP has historically grown technical terminology (jabber/xmpp, roster, presence) that's hard to grasp for users, and partially irrelevant
* need to focus on [common glossary](https://wiki.xmpp.org/web/Usability/Glossary)
* challenge: i18n

### User Onboarding

* Choosing and installing the right client
  * "Modern"? (HTTP-Upload, ...?)
  * Support for multi-client operation? (Carbons, MAM)
  * Support for mobile operation? (SM, ACKs)

* Choosing the right server
  * Inherent complexity compared with centralized services
  * Idea: curated server list with TLDR-ToS

* Creating an account
  * As easy as possible: user defines their "screen name", client suggests JID = `slug($screenname)@$serverdomain`
  * auto-generated secure password with option to export/change
  * Need: better password recovery

* Empty Roster problem
  * How to discover users?
  * HARD problem
  * DNS? Centralized vCard services?
  * Probe all email addresses?
  * partial "Easy" solution: [PARS](https://xmpp.org/extensions/xep-0379.html) plus [landing page](https://github.com/ge0rg/easy-xmpp-invitation)
    * server side implementation TBD
  * Follow-up solution:
    * sharing of roster items with better UX
    * client indicates to contact(s) that it only has a low number of friends, encourages sharing of "common friends" contacts
    * challenges: security of user, contacts

* Onboarding more device
  * One-time links
  * Email-based password reset (UX challenge)
  * per-device passwords
  * 2FA logins
  * [Account migration / merging / moving](https://wiki.xmpp.org/web/Easy_Account_Migration)

### (Private) Group Chats

* Long-term future: MIX
* today: MUC is 80% of the solution
  * need to codify ad-hoc private MUCs for party planning, family matters etc.
  * ideas: [Easy Group Chats](https://wiki.xmpp.org/web/Easy_Group_Chats)
  * challenge: security
    * MUC hosted on external domain - nothing can be trusted
    * who is allowed to invite you?

