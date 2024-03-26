---
Title: Client Design Guidelines
---

This document lays out a set of guidelines for designing Modern XMPP clients. For contributions,
please [open an issue or pull request](https://github.com/modernxmpp/modernxmpp) at Github for discussion.

## Registration

!!! TODO

## Initial configuration

At initial startup, a client should present a welcome screen, to prompt the user for their JID,
and a password. Optionally, a button or link to provide other forms of credentials may be included.

If the client has an out-of-band configuration mechanism, or it can query the OS for sensible defaults,
it may use these.

## Configuration options
List recommended configuration options.

### Account

| Option | Description           |
|:-------|:----------------------|
| JID    | The user's JID        |
| Password | The user's password |

### Network

Support for these options is OPTIONAL, but **not** recommended. They are only needed for testing/development purposes or working around misconfigured server deployments. If included in the client, they MUST NOT be requested by default at startup, but should be accessible through an advanced options interface.

| Option              | Description                                  |
|:--------------------|:---------------------------------------------|
| Connect host        | The network hostname to connect to           |
| Connect port        | The network port to connect to               |
| TLS Mode[^tls-mode] | Multiple choice: "STARTTLS" or "Direct TLS"  |

Both of the above should be automatically discovered from DNS, according to the [rules in RFC 6120](/rfcs/rfc6120.html#tcp-resolution).
Clients that support other connection mechanisms, such as BOSH, SHOULD also implement [XEP-0156](/extensions/xep-0156.html).

### Deprecated options

Support for these options is NOT RECOMMENDED.

| Option       | Description                              | Notes |
|:-------------|:-----------------------------------------|:--------|
| Resource     |  The resource to request from the server | see [Resource generation](/implementation-guidelines/protocol#resource-generation)  |
| Priority     |  The priority to include in presence     | 0       |

## User status

The client, by default, MUST NOT include any status messages in its presence, unless they are chosen by the user. Built-in status messages that
convey the same meaning as the user's selected 'show' value (e.g. "Available", "Do not disturb") are not allowed.

Allowing the user to set a status message is an OPTIONAL feature.

## Contact list

### Terminology
In its interface, the client MUST NOT use the technical term "roster", but MUST instead use the term "contact list" (or a suitable translation)
where necessary. See the main "Terminology" section for more information.

### Offline contacts

The client MUST display offline contacts by default, and allow sending messages to them, as for online contacts..

### Sorting of contact list

The client MUST sort the contact list. Either in [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order) by contact name or
chronologically by the time of the last message exchanged with that contact.

!!! Note
    Historically, some clients have sorted by presence (available, offline,
    busy, etc.) as a secondary sorting category.
    Due to the rise in mobile clients which always consider themselves
    "available", presence is not always a reliable indicator that a contact is
    available to chat.

If sorting chronologically and/or by presence, clients MUST NOT rearrange the
contacts list while fetching history, or when the contact list has focus.
The definition of "focus" depends on the context, but may be the cursor hovering
over the list, the list pane being visible, or the list being selected in a
screen reader or during tab selection.

### Visualizing status

The client MUST display status messages of contacts when present. It MAY also provide visual indication of the contact's status ('show'), but
SHOULD NOT rely on color alone to distinguish different status values[^color].

!!! todo
    Describe how to display multiple remote resources.

## Conversation view

### Message states

#### Outgoing messages

A client must be able to unambiguously display the following outgoing message states:

* Message pending delivery
* Message delivered to server
* Message delivered to contact
* Message read by contact
* Delivery error for message

!!! todo
    Add table or flowchart

## Notifications

Carbons, notifications for new messages in MAM

## Error handling

Obey error types (modify, cancel, wait, etc.)

Do display error text

## Multiple accounts

Support for multiple accounts is OPTIONAL.

!!! todo
    Research recommendations for the best way to handle multiple accounts. E.g. merge contacts, or not.
    Not required. Describe how to display multiple accounts in a single client?

## Group chat

You can find more details about [group chats here](/implementation-guidelines/groupchat).

## Documentation

Clients should have documentation covering essential functionality, including:

!!! todo
    List of recommended documentation topics, e.g. how to add a contact

## Privacy

Clients must not reveal full JID. Don't query unsubscribed contacts.

!!! todo
    Probably belongs in protocol reference. Probably some things relevant
    to UI that should be mentioned, however.

## Names

When displaying messages received from a remote JID, either within a one-to-one or multi-user chat, clients need to show a human-readable
name for that sender.

There are multiple sources for such a display name, which depend on the context (e.g. whether the conversation is one-to-one or a group chat).

### Name sources

Valid sources are:

Roster
: If the contact is in the user's roster, and the user has set a custom name.

Address book
: Platform-dependent. If the application is somehow linked to the user's address book and is able to access a contact's information there.

User nickname
: A nickname published by the sender in PEP per [XEP-0172](/extensions/xep-0172.html).

Resource
: The resource of the sending JID.

Local part
: The part of a bare JID before the '@' symbol.

Bare JID
: The sending JID with any resource removed.

### Contexts

The kind of view where a name is displayed decides which sources should be used. Since most sources are optional, they
should be checked in the order described by the table below, displaying the first one available.

| View type               | Name priorities                                           |
|-------------------------|-----------------------------------------------------------|
| Conversation - normal   | Roster name, (Address book), User nickname, Local part    |
| Conversation - group    | Roster name, (Address book), User nickname, Resource (\*) |
| Conversation - channel  | Resource                                                  |
| Contact list            | Roster name, User nickname, Bare JID                      |
| User profile            | Roster name, User nickname, Bare JID                      |

(\*) Mentions refer to resource. if you do proper references you can live replace it with the 'nice' name.

Avatar display should follow the same order

## Auto-generated colors

A client may want to associate a color with a user. Example use cases for this include, but are not limited to:

- Dummy avatars in contexts where an avatar cannot be or has not yet been retrieved
- Coloring the user name in a conversation log (be aware that this needs to be done very carefully to be accessible!)

To generate a color for a user, the algorithm described in [XEP-0392](/extensions/xep-0392.html) MUST be used.

### Generator input based on context

The generator described in XEP-0392 needs a text input to operate and for which a deterministic color will be generated.

The following table lists which strings to use as input for the generator:

| View type               | Generator Input     |
|-------------------------|---------------------|
| Conversation - normal   | Normalised Bare JID |
| Conversation - group    | Normalised Bare JID |
| Conversation - channel  | Resource            |
| Contact list            | Normalised Bare JID |
| User profile            | Normalised Bare JID |

### Contrast ratio considerations

To provide a good contrast ratio for accessibility of the resulting user interface, the guidelines from [^color] should be obeyed. XEP-0392 intentionally allows the implementation to pick a saturation and lightness value based on the environment to allow for high contrast.

Contrast considerations apply between the generated color and the background, as well as for text rendered on top of the generated color (for example in a dummy avatar).


<!-- Footnotes -->

[^color]: Resources for the use of color in interface design:

    * [WCAG 2.1: Understanding Use of Color](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)
    * [Color contrast checker](https://webaim.org/resources/contrastchecker/)

[^tls-mode]: This is presented as a multiple-choice option. A checkbox labeled e.g. "Direct TLS"
    may confuse users by implying that the opposite of "Direct TLS" is potentially "No TLS". Security is
    not an option, and TLS is always used. This option is about what style the server supports.
