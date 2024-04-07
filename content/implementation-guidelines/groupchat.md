---
Title: Multi-user Chats
---

## Types of chat

There are two kinds of multi-user chat. Private *group chats*, and public *channels*[^rationale-gc].

### Properties

To detect if a multi-user chat is a *group chat* or a *channel*

|                  | MUC Configuration variable (1) | Group chat | Disco Feature (2)  | Channel | Disco Feature (2)  |
|:-----------------|:-------------------|:-----------|:---------------|:--------|:---------------|
| Persistent       | muc#roomconfig_persistentroom | Yes        | muc_persistent | Yes     | muc_persistent |
| MAM enabled      | **Prosody** muc#roomconfig_enablearchiving  **ejabberd community**: mam  **ejabberd saas** muc#roomconfig_mam | Yes        | urn:xmpp:mam:2 | Yes     | urn:xmpp:mam:2  |
| Subject editable | muc#roomconfig_changesubject | No         | muc#roomconfig_changesubject to `false` | No      | muc#roomconfig_changesubject to `false` |
| Members-only     | muc#roomconfig_membersonly | Yes (3)   | muc_membersonly | No      | muc_open      |
| JIDs revealed    | muc#roomconfig_whois | Yes (3)   | muc_nonanonymous| No      | muc_semianonymous |
| Publicly listed  | muc#roomconfig_publicroom | No  (3)   | muc_hidden      | Yes     | muc_public    |
| PMs              | muc#roomconfig_allowpm | No  (3)   | muc#roomconfig_allowpm to `none` | Yes     | muc#roomconfig_allowpm to `anyone` |

(1) As defined in [XEP-0045: Multi-User Chat - 16.5.3](/extensions/xep-0045.html#registrar-formtype-owner)

(2) As defined in [XEP-0045: Multi-User Chat - 16.3](/extensions/xep-0045.html#registrar-features)

(3) Immutable for *group chats*.

Options marked `(3) Immutable` should be used when creating group chats, and also as a means of detection. These options may be hidden or greyed out in a configuration dialog. The other options are recommendations.

#### About PMs

While it is possible to entirely prevent PMs from being sent with
[`muc#roomconfig_allowpm`](/extensions/xep-0045.html#privatemessage),
clients should prefer using JIDs when `muc#roomconfig_whois` is set to `anyone`.

In channels, if the initiating client has access to revealed JIDs (with
`muc#roomconfig_whois` set to `moderators`), clients may want to refrain from
using them to prevent disclosing the JID of the user initiating the chat,
unless the recipient already knows them from another venue (e.g., the
recipient is in their roster).

### Terminology

People in the *group chat* / *channel*: *Participants*

Roles are not displayed and cannot be modified through the UI.

| Affiliations | In group chats | In channels |
|:-------------|:--------------:|:-----------:|
| none         | N/A **         | Guest       |
| member       | -              | -           |
| admin        | *Admin* (\*)   | Admin       |
| owner        | Owner          | Owner       |

(\*) A *group chat* will display an existing admin as such but it will not encourage/allow
someone to be promoted to admin. UI options in *group chats* only allow a member to become
an owner but not admin. So admins are discouraged by the UI but will be displayed as such
if they end up being one for some reason.

(\*\*) Everybody is a member in *group chats*

Clients MAY create an 'advanced view' that displays roles as well.

## User nickname

When joining a group chat, a client needs to select a nickname to use. There are multiple
sources from which this name may be selected. The client should use the following sources
in order:

Bookmark
: If the chat is present in the user's bookmarks and has a nickname present (as the resource).

Reserved name
: A chat [may be queried](/extensions/xep-0045.html#reservednick) to fetch the
    name that is registered by the user for that chat.

User nickname (PEP)
: The name stored in the user's account according to
    [XEP-0172](/extensions/xep-0172.html#manage).

User nickname (vCard)
: The name stored in the user's vCard as `NICKNAME`.

Local nickname
: (Optional, not recommended[^local-nickname]) A nickname previously configured by the user in this client instance.

JID username
: The username portion of the user's JID (i.e. before the '@').

### Other user's names

The display of other user's names is covered in the [general UI recommendations](/implementation-guidelines/design#names).

## Bookmarks

Figuring out which group chats to join is the client’s job. For that it
should store the list of group chats to rejoin automatically on the
server, named bookmarks. Three possible protocols exist for this:

- [XEP-0402](/extensions/xep-0402.html) which is the
  current preferred method
- [XEP-0048 1.1](/extensions/xep-0048.html), recently
  deprecated but still in use by some clients
- [XEP-0048 1.0](/extensions/attic/xep-0048-1.0.html),
  in wide use, based on
  [XEP-0049](/extensions/xep-0049.html)

In order to see the same set of bookmarks as every other client the
user might be using, it is recommended to implement **XEP-0048 1.0** first
and foremost when the user's account may be shared with other clients.

This legacy protocol however doesn’t support notifications when the bookmarks
change due to another client or the server. To avoid this issue, a modern client
should also implement **XEP-0402** ("PEP Native Bookmarks"), but use it *only* if the account
advertises 'urn:xmpp:bookmarks:1#compat' (as defined in [XEP-0402 paragraph 5.3
Compatibility](/extensions/xep-0402.html#compatibility)).

Implementing XEP-0048 1.1 is not recommended in modern clients.

The following table summarizes the implementation recommendations described in this section:

| XEP                                        | Implement                                | Use                                                                         |
|--------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------|
| XEP-0048 1.0  (Private XML storage)      | Yes  (for backwards compatibility)     | When `urn:xmpp:bookmarks:1#compat` **is not** advertised by the server on the user's account. |
| XEP-0048 1.1  (PEP storage, single-item) | No  (deprecated in favour of XEP-0402) | Never                                                                       |
| XEP-0402  (PEP storage, multi-item)      | Yes                                      | When `urn:xmpp:bookmarks:1#compat` **is** advertised by the server on the user's account.     |

## Private messages

Clients must always use real JIDs for messaging privately within a *group chat* if (and only if) JIDs are publicly visible to all participants.[^pm-realjid]

<!-- Footnotes -->

[^rationale-gc]: Rationale [group chats](/implementation-guidelines/rationale#group-chats)
[^local-nickname]: To avoid requiring the user to configure a nickname manually on each device, shared cross-device stores such as PEP and vCard should be preferred.
[^pm-realjid]: If real JIDs are known to all participants, it is preferable to use that for private communication to avoid confusion. Through-MUC PMs have the following disadvantages:

    - Only work while connected to the group chat
    - Do not interact well with multiple devices (e.g. not all of a recipient's devices may be in a group chat)
    - Can cause confusion if talking to the same person through different views (e.g. if the person is already a contact in your roster, and you already have a chat open with them)

    However if the sending user is an admin of a room where JIDs are hidden, using a real JID will reveal the admin's private JID to the recipient. Either warn the sender that their JID will be revealed, or always use the in-room JID in such channels.
