---
Title: UX Sprint (January 2019, Brussels)
---

These are the archived notes from the Jan 2019 Brussels sprint,
which focused primarily on discussing various UX issues facing
the community as a whole. There is an associated
[wiki page](https://wiki.xmpp.org/web/Sprints/2019_January_Brussels).

The notes were taken in real-time by volunteers during the discussions.
As such, they are far from editorially perfect, and are not intended as
documentation. Relevant items around which consensus was formed are
either already merged or in the process of being merged into the actual
documentation.

I don't know why Tux is here, but I'll let him stay.

- - -

```
              .-"""-.
             '       \
            |,.  ,-.  |
            |()L( ()| |
            |,'  `".| |
            |.___.',| `
           .j `--"' `  `.
          / '        '   \
         / /          `   `.
        / /            `    .
       / /              l   |
      . ,               |   |
      ,"`.             .|   |
   _.'   ``.          | `..-'l
  |       `.`,        |      `.
  |         `.    __.j         )
  |__        |--""___|      ,-'
     `"--...,+""""   `._,.-'
```

## TODO

- Extend https://wiki.xmpp.org/web/Usability/Glossary

### Daniel’s list
* What to name things?
   * Common Jabber vocabulary for Groups, 'Jabber ID', bookmarks, "MUC members / participants"
   * Persons; (preference of roster name, pep name, local sync name (address book).
   * Persons in MUC (order of preference of room nick, roster name, pep name, …)
     * order of people in member list admins first?, alphabetical? (see affiliations)
   * Groups / Chats (preference of description, subject, local part, name, bookmark name, auto generated name)
 * do not get MUC name from identity name but from disco form fields because identity name is set to localpart on some servers
 * Do we want to replace a referenced nick with the local version?
 * Ad hoc, Impromptu group chat; come up with a cool default settings like members only, non-anon, allow pm?, allow subject change, allow invite. What to expose
Behavioral changes in impromptu MUCs (send chat states, display read markers, e2ee by default, prefer 1:1 instead of PM when contacting a participant) and how to recognize and impromptu chat (isMemberOnly && isNonAnon)
* Affiliations
   * Do we need an owner. Should in a three person chat someone be the 'owner'
   * Administrators might make sense. But maybe we want to show owner and admin as the same.
   * Maybe it makes sense to make everyone owner and then call owner the admin

* Do we need different profiles?
   * Private, non-anon
   * Public
   * Announcements. w/o presence broadcast, moderated
   * should those profiles be locked afterwards


* Do we want to keep bookmarks or just use it as a sync mechanism?
  * open/close conversations when bookmark created / autojoin flag removed?
  * do we also leave when bookmark is removed? Does that work? this basically means no join without bookmark. 'remove bookmark' (w/o leave) can not be an action anymore


## Naming things?!

* Jabber ID? JID? XMPP address?
	* "Jabber" trademark
  * "JID" widely used but might be a more technical term
  * "something address" is clear to people
  * "XMPP" is usually hard to remember, "Jabber" is more friendly to the ear
  * Jabber is the community, XMPP is the protocol
  * What about calling it "Conversations ID", or "Converse ID", or "Movim ID", all at the same time. Might be confusing for users when they use multiple clients but most don't.
  * Some other protocols use "username" (with a hint for the default domain)

Consensus: "XMPP Address"? (until another user-friendly term for "XMPP" can be found/agreed upon)


## Results / Consensus


### XMPP Address / Jabber ID
 - XMPP Address input: Always use one field. Never split into localpart and domain part. If possible do auto-complete on the server part in drop down


### Group chats / channels:
 - Private group chat (or groupchat)

    - members only
    - JID visibility: all
    - MAM: yes
    - not listed (non public)
    - persistence
    - users can invite. default off. (does this need to be configurable?)
    - subject editability: owner only (probably make it configurable?)
    - disallow pm

 - Public channel
    - public / everyone can join
    - MAM: yes
    - listed: yes
    - persistent
    - JID: visibility anonymous
    - subject editability: admins only (probably make it configurable)
 - Possibility to omit the words 'private' and 'public' later down the UI flow and just talk about 'groupchat' and 'channel' (for example when constrained on screen estate)
 
   - recognize on members only AND visible JIDs AND not listed, everything else is a public channel. but a client should maybe warn before entering a public channel that makes your JID public. Those three 'detection properties' are immutable for private group chats

   - private group chats use randomized, auto generated JID (always on the server’s own MUC host)
   - public channels always ask for bare JID on create (auto suggest of know MUC hosts)
      - UI suggestion. ask for name first. Then normalize to local part of JID. But let user change the JID if they want to


Group chats and channels should be clearly distinguished visually.

|                  | Groupchat | Channel | Immutable for groupchats |
|:-----------------|:---------:|:-------:|:------------------------:|
| Members-only     | Yes       | No      | X                        |
| Reveal JIDs      | Yes       | No      | X                        |
| Publicly listed  | No        | Yes     | X                        |
| Persistent       | Yes       | Yes     |                          |
| MAM enabled      | Yes       | Yes     |                          |
| Subject editable | No        | No      |                          |
| PMs              | No        | Yes     | X                        |


### Terminology

People in the group chat / channel: Participants   	


| Affiliations | In groupchats | In channels |
|:-------------|:-------------:|:-----------:|
| none         | N/A **        | Guest       |
| member       | -             | -           |
| admin        | *Admin* (\*)  | Admin       |
| owner        | Owner         | Owner       |

Roles should not be used anymore.

(\*) A group chat will display an existing admin as such but it will not encourage/allow someone to be promoted to admin. UI options in group chats only allow a member to become an owner but not admin. So admins are discouraged by the UI but will be displayed as such if the end up being one for some reason.

clients MAY create an 'advanced view' that displays roles as well.

** Everybody is a member in groupchats


### Suggested order of what to call an individual
message: roster name, (address book), user nickname, localpart
groupchat message: roster name, (address book), user nickname, resource (mentions refer to resource. if you do proper references you can live replace it with the 'nice' name)
channel message: resource
roster: roster name, user nickname, bare JID
profile: roster name, user nickname, bare JID

Avatar display should follow the same order

### Bookmarks
Unbookmarking a bookmark doesn’t do magic leave on any devices
when receiving set/unset autojoin will join/leave on all devices
leave/join will unset/set the autojoin flag (exposed as a choice to the user)
clients should offer global sync-opt-out (Don’t adhere to autojoin)
clients should store the list of groupchats open, unrelated to the autojoined bookmarks

Summary: clients store the list of open chats (groupchats or not) and restore it on next start; on receiving a bookmark with a new autojoin from PEP, add the room to that list and open it; on receiving one without an autojoin, remove it from that list and close it; on joining a room add an autojoin bookmark; on leaving a room ask whether to leave it globally (then remove the autojoin from the bookmark), or to leave it locally (then remove the bookmark).

## Places to update/remove

https://wiki.xmpp.org/web/Usability/Glossary
https://wiki.xmpp.org/web/Easy_Group_Chats
