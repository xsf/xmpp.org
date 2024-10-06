---
Title: Registration through invitation
layout: single-implementation-guidelines
---

It is possible to create invitation links in XMPP. There are currently a few
types of invitation possible, e.g. you may be invited to register on a server,
or be invited to add someone as a contact, or both.

## Invitation types

There are three types of invitation:

- [Account-only](#account-only)
- [Subscription-only](#subscription-only)
- [Account-and-subscription](#account-and-subscription)

They are described individually in the following sections.

### Account-only

This type of invitation can be used by server operators to allow
people to create accounts on their server, without needing to open up
registration to the public.

#### Format

Invitation to register an account on a given domain (e.g. 'example.com'):

```
xmpp:example.com?register;preauth=3c7efeafc1bb10d034
```
or an invitation to register an account with a **specific** username (e.g.
'romeo') only:

```
xmpp:romeo@example.com?register;preauth=3c7efeafc1bb10d034
```

See [XEP-0445][] for how to register an account using this type of invitation.

### Subscription-only

This invitation type can be shared with someone who you would
like to add you as a contact. Unlike a normal XMPP subscription request, these
invitations can be shared to people via any mechanism (e.g. email, SMS, web)
and if you don't know the recipient's XMPP address or they don't yet have one.

A potential contact invites you to communicate with them:

```
xmpp:contact@example.com?roster;preauth=3c7efeafc1bb10d034
```

The protocol to handle this type of invitation is specified in
[XEP-0379][]. After following the protocol, you will have a mutual presence
subscription with `contact@example.com`.

If the user does not currently have an account, the client must walk
them through the account registration process on a suitable XMPP service.

### Account-and-subscription

The same as a subscription-only invite, but it indicates you
are able to use the token to also register an account on the contact's
domain, signalled by the presence of `ibr=y` in the URI parameters:

```
xmpp:contact@example.com?roster;preauth=3c7efeafc1bb10d034;ibr=y
```

If the recipient of such an invite does not yet have an XMPP account, their
client should follow the *Registration protocol* section of this document.
After completing the registration, the user will automatically be subscribed
to the sender of the invitation.

If the recipient already has an XMPP account, the invitation should be
handled the same as a subscription-only invitation documented above,
and follow the protocol defined in [XEP-0379][].

## Protocols

There are three standards governing the creation and consumption of invitations:

- [XEP-0401][] - describes how to create new invitations (of all types).
- [XEP-0445][] - describes how to register an account using an account-only or account-and-subscription invitation.
- [XEP-0379][] - describes how to convert an invitation (subscription-only or account-and-subscription types) into a roster subscription.

### Registration protocol

The account-only and account-and-subscription invitation types allow a recipient
to create an account on a server (which may otherwise have closed registration).
XMPP clients can use these invitation types to create an account by following
the protocol in [XEP-0445][].

## Creating an invitation

To create an invitation, use [XEP-0401: Ad-hoc Account Invitation Generation][XEP-0401].
Your server may also provide a mechanism (e.g. web interface or command-line
utility) to create invitations.

Services may restrict the types of invitation that can be created, depending
on policy. E.g. private servers may allow anyone to create contact invitations,
but only allow administrators to create account invitations.

When using XEP-0401, the server will provide at minimum an `xmpp:` URI that can be interpreted by any compatible XMPP client. However this URI SHOULD NOT be shared directly by clients. It is generally likely that the recipient of an invite does not yet have an XMPP client installed and configured.

Instead, if the server provides a `landing-url` in the response, the client SHOULD share this URL with contacts. Otherwise it SHOULD use the URI in combination with a landing page (which may be hosted by the client developer or other entity) to generate a `https://` URL suitable for sharing. One such landing page implementation can be found at [ge0rg/easy-xmpp-invitation](https://github.com/ge0rg/easy-xmpp-invitation).
Sharing the URL can be done by visually displaying a QR code on the user's screen (if the contact is in physical proximity) or e.g. through the platform's own sharing mechanism (to share via SMS, email, social apps, etc.)

## Guidance for landing pages

As well as embedding the XMPP URI in a visually obvious clickable/tappable element (e.g. a button), it should include text and download links for compatible XMPP clients.

If it is possible for a particular platform's download links to automatically relay the `xmpp:` URI to the installed app, that should be implemented. See for example [Google Play Install Referrer](https://developer.android.com/google/play/installreferrer/).

If possible, platform detection should be used to highlight download links relevant to the user's current platform.

If the detected platform is a desktop environment, consider also adding a QR code for easy transmission to a user's mobile device.

[XEP-0401]: /extensions/xep-0401.html "Ad-hoc Account Invitation Generation"
[XEP-0445]: /extensions/xep-0445.html "Pre-Authenticated In-Band Registration"
[XEP-0379]: /extensions/xep-0379.html "Pre-Authenticated Roster Subscription"
