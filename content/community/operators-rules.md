---
Title: XMPP Operators Channel
Url: community/channels/operators
---

## About the XMPP Operators Channel

The XMPP Operators Channel is located at [operators@muc.xmpp.org](xmpp:operators@muc.xmpp.org?join). It is a place primarily for operators of federated XMPP services, to have civil and low-bar discourse and resolution of interoperability issues. In addition to that primary purpose, it is also a place for the wider XMPP community (including end-users and operators of non-federated servers) to get in touch with operators to resolve issues, report abuse (see below for important notes on that!) or any other service related topic.

## Participation

While the channel is currently open for anyone to read, active participation in the channel is currently restricted to:

- Verified operators of XMPP servers on the public federated network
- Members of the XMPP Standards Foundation

This was implemented to create a focused space where the community can collaborate on the channel's stated topics, and to help reduce noise, spam and abuse from other sources.

Participation rights are managed automatically. For more information (including how to obtain permission to send messages) see the FAQ below.

## Code of Conduct

Like any growing community, the XMPP Operators Channel has a set of rules to govern the interactions, in order to make as many people as possible feel safe and welcome.

Above all, the [Community Code of Conduct of the XMPP Standards Foundation](https://xmpp.org/extensions/xep-0458.html) (still under discussion, but unless stated otherwise in *this* document, the current experimental version applies nontheless) applies, called CoC hereafter. That means that behaviour which goes against the CoC is automatically not accepted.

For transgressions solely happening within the XMPP Operators channel, the channel admins are an acceptable first point of contact.

**Note**: The CoC only applies to XMPP Standards Foundation (XSF) members and venues. It does not automatically apply to all members of all XMPP channels. Do not report misconduct in venues outside of the control of the XSF to this room or the XSF Conduct Team, unless an XSF member is involved.

## On-Topicness

The channel started out as a place for operators to work together to improve the general health of the XMPP network, encompassing topics such as interoperability, reliability and availability. It can provide valuable information when just reading passively, but also when actively asking.

In order to keep the signal-to-noise ratio useful for people listening in on the channel passively, it is helpful to keep off-topic discussions to a minimum. To give you an idea about what people expect from the channel, here is a non-exhaustive list of topics which fit into the scope of the channel:

* Announcements and raising awareness about problematic actors in the ecosystem affecting end-users or services negatively, preferably with corresponding evidence so that everyone is able to form their own opinion.

  **Note:** When reporting abuse, make sure to not link to the abusive material right away. Do not post triggering text or images directly in the public channel.

* Discussion about tools for server operators (e.g. TLS/DNS checkers, configuration linters, configuration management systems (to some extent)).
* Announcements of security advisories which concern XMPP server or client software (so that operators can pass this on to their users) or tools very commonly used with XMPP server deployments (e.g. anything you’d find in a typical linux server installation; no hard lines here).
* Asking for contact information for a specific XMPP service in order to discuss an issue "off-list" (in private).
* Discussion of approaches to instant messaging spam counter measures.
* Discussion of effects of service policies on interoperability.
* Baselines or standards for interoperability between servers (e.g. TLS ciphers, certificate authorities, port numbers, DNS setups etc.).

### Edge cases

Some topics sometimes fit in the scope. If unsure, you can ask the moderators privately for confirmation beforehand. In general, try to not overuse these categories.

* Announcements or information relevant to services or tools which may be of interest for service operators (e.g. search.jabber.network or xmpp.net).

  Here, it is important to strike the balance between advertisment and useful announcement. In general, security advisories related to such services or tools are always on-topic. If the service is paid for and the announcements aims at acquiring more customers, it may easily be off-topic. This is not an advertisment or business development channel.

### On-Topic induced Off-Topic

Since some of the on-topic cases can quickly derail into off-topic when debates become too political or ad-hominem. When debating controversial topics, the difference between an insult or judgement and a discussion is in the rationale.

To help you finding the line, here’s an on-topic example:

> You should not block messages from non-contacts on the admin account, because other admins may have to reach you to notify you about a problem with your service.

> I think other operators trying to reach me via XMPP should send a presence subscription first, so blocking messages from non-contacts is not an issue.

> Keeping debug logs for 14 days is not a good idea because there is a lot of personal information in there which is at risk of exposure.

On the other hand, the following variants are are off-topic:

This is combined with something which is easily read as a personal attack:

> Blocking messages from non-contacts is stupid.

This *is* a personal attack:

> Blocking of messages from non-contacts is censorship and you’re a bad person for doing it.

This lacks a rationale and is easily based on wrong assumptions; it can also be taken as an offense, because it does not acknowledge any countermeasures or trade-offs which might have been taken into account.

> You are irresponsible for keeping debug logs for 14 days.

If you find yourself unable to find a rationale which is technical and XMPP related, that is probably a good point to stop the interaction.

## Enforcement

As soon as the moderator team gains knowledge of behaviour in the channel which violates those rules and the offense is confirmed, the following actions may be taken against the offending user(s).

Sometimes, a swift action is necessary to restore order in the channel. For those cases, the channel admins can take the following actions at their discretion:

* One-time kick (serves as a warning).
* Temporary enforced removal from the channel (banning) for 1 day. This action should only be applied once to an entity before the Conduct Team is getting involved.

If the behaviour continues despite those measures or if the transgression is sufficiently excessive to warrant more strong action, the Conduct Team of the XSF should be invoked, as described in the CoC.

## FAQs

### Who is authbot?

You may notice an occupant of the channel called `authbot`. It is a moderation assistant bot that automatically grants channel membership to users it identifies as server operators. It performs a [contact addresses (XEP-0157)](https://xmpp.org/extensions/xep-0157.html) query on servers and looks for a match with any of the returned XMPP addresses.

### How do I get channel membership?

Membership is automatically granted by authbot when the criteria are met.

Also, please note that channel membership does not imply any kind of immunity from the rules, or endorsement of a user.

### I want to discuss something that is considered off-topic in this channel, where can I go?

To discuss software development related to XMPP, there exists [jdev@muc.xmpp.org](xmpp:jdev@muc.xmpp.org?join). Discussion of XMPP Extension Proposals as well as the XMPP standard itself and matters concerning the XMPP Standards Foundation takes place in [xsf@muc.xmpp.org](xmpp:xsf@muc.xmpp.org?join).

Other options include the following channels which are not XSF-operated channels. They may have their own rules and moderation policies. Accordingly it follows that we are not responsible for the content or moderation of these channels. They are merely suggestions.

For broader discussions related to the XMPP network and ecosystem, check out the [joinjabber.org community](https://joinjabber.org/about/community/). They have a range of channels across various relevant topics.

For other topics, you may find chat rooms to your liking at [search.jabber.network](https://search.jabber.network).
