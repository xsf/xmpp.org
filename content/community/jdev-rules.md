---
Title: jdev Channel
Url: community/channels/jdev
---

## About the XMPP Developers Channel ("jdev")

The XMPP Developers Channel is located at [jdev@muc.xmpp.org](xmpp:jdev@muc.xmpp.org?join). It is a place primarily for developers of software following or aiming to follow XMPP standards (RFC 6120--6122, as well as XMPP Extension Proposals, and updated versions of the RFCs), to have civil and low-bar knowledge transfer, learning and support in the task of implementing the various pieces of the XMPP standard compendium.

## Code of Conduct

Like any growing community, the XMPP Developers Channel has a set of rules to govern the interactions, in order to make as many people as possible feel safe and welcome.

Above all, the [Community Code of Conduct of the XMPP Standards Foundation](https://xmpp.org/extensions/xep-0458.html) (still under discussion, but unless stated otherwise in *this* document, the current experimental version applies nontheless) applies, called CoC hereafter. That means that behaviour which goes against the CoC is automatically not accepted.

For transgressions solely happening within the XMPP Developers channel, the channel admins are an acceptable first point of contact.

**Note**: The CoC only applies to XMPP Standards Foundation (XSF) members and venues. It does not automatically apply to all members of all XMPP channels. Do not report misconduct in venues outside of the control of the XSF to this room or the XSF Conduct Team, unless an XSF member is involved.

## On-Topicness

The channel started out as a place for developers to work together to improve the state of XMPP software in general, encompassing topics such as software interoperability (as opposed to deployment interoperability; for the latter, the [Operators channel](operators-rules.md) is the better a place), reliability, security and standards edge cases. It can provide valuable information when just reading passively, but also when actively asking.

In order to keep the signal-to-noise ratio useful for people listening in on the channel passively, it is helpful to keep off-topic discussions to a minimum. To give you an idea about what people expect from the channel, here is a non-exhaustive list of topics which fit into the scope of the channel:

* Discussion about tools for software developers specific to XMPP (e.g. XMPP test suites, test vectors, network simulation tools, XML linting, parsing, generation tools).
* Reaching out to implementors of different software to discuss interoperability issues or find a place to responsibly disclose security issues.
* Discussion of past security vulnerabilities in XMPP software.
* Discussion of the effects of implementation choices on the broader ecosystem.
* Asking questions about how specific pieces of a standard are meant to be interpreted.

Please note the FAQ for a suggestion for places to discuss specific adjacent topics!

### On-Topic induced Off-Topic

Since some of the on-topic cases can quickly derail into off-topic when debates become ad-hominem. When debating controversial topics, the difference between an insult or judgement and a discussion is in the rationale.

To help you finding the line, here’s an on-topic example:

> Showing unsolicited presence subscriptions in a focus stealing popup window is problematic because that allows unauthenticated foreign users to interrupt users workflows.

> Storing logs unencrypted in a human-readable format on-disk is risky because many desktop operating systems do not restrict access to other app's data, allowing a single malicious app to carry away lots of information.

On the other hand, the following variants are are off-topic:

This is combined with something which is easily read as a personal attack:

> Storing unencrypted messages on disk is stupid.

This *is* a personal attack:

> Storing unencrypted messages on disk is stupid and you’re a bad person for making your client do it.

This lacks a rationale and is easily based on wrong assumptions; it can also be taken as an offense, because it does not acknowledge any countermeasures or trade-offs which might have been taken into account.

> You are irresponsible for storing chat logs without extra security.

If you find yourself unable to find a rationale which is technical and XMPP related, that is probably a good point to stop the interaction.

## Enforcement

As soon as the moderator team gains knowledge of behaviour in the channel which violates those rules and the offense is confirmed, the following actions may be taken against the offending user(s).

Sometimes, a swift action is necessary to restore order in the channel. For those cases, the channel admins can take the following actions at their discretion:

* One-time kick (serves as a warning).
* Temporary enforced removal from the channel (banning) for 1 day. This action should only be applied once to an entity before the Conduct Team is getting involved.

If the behaviour continues despite those measures or if the transgression is sufficiently excessive to warrant more strong action, the Conduct Team of the XSF should be invoked, as described in the CoC.

## FAQs

### I want to discuss something that is considered off-topic in this channel, where can I go?

To discuss operating XMPP server software as well as deployment interoperability, there exists the [XMPP Operators channel](operators-rules.md) at [operators@muc.xmpp.org](xmpp:operators@muc.xmpp.org?join). Discussion of XMPP Extension Proposals as well as the XMPP standard itself and matters concerning the XMPP Standards Foundation takes place in [xsf@muc.xmpp.org](xmpp:xsf@muc.xmpp.org?join).

Other options include the following channels which are not XSF-operated channels. They may have their own rules and moderation policies. Accordingly it follows that we are not responsible for the content or moderation of these channels. They are merely suggestions.

For general software development discussions not specifically related to XMPP, check out the Virtual Tinkerspace at [programming@chat.cluxia.eu](xmpp:programming@chat.cluxia.eu?join).

For broader discussions related to the XMPP network and ecosystem, check out the [joinjabber.org community](https://joinjabber.org/about/community/). They have a range of channels across various relevant topics.

A general off-topic chat can be found at [conversations-offtopic-reloaded@conference.trashserver.net](xmpp:conversations-offtopic-reloaded@conference.trashserver.net?join).
