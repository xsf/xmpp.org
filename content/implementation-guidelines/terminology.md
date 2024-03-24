---
Title: Terminology
---

To reduce user confusion when switching between clients, it is good to use only recommended
terms.

| Historic/protocol terms          | Recommended user-facing terms                                        |
|----------------------------------|----------------------------------------------------------------------|
| MUC, Room, Chatroom, Conference  | *Group chat* or *Channel*[^rationale-gc] (see [Multi-user Chats][])  |
| Occupant                         | *Participant*                                                        |
| JID                              | *Address* or *XMPP address*                                          |
| Roster                           | *Contact list*                                                       |
| Avatar                           | *Profile picture*                                                    |

**Note:** The recommendations only apply to user-facing text, such as application UIs and other content directed towards end users. There is no intent to change the language used by developers for discussing protocol elements[^rationale-dev-terms]. This is why you will still see terms such as "JID" used across the developer-oriented documentation of this project, for example.

## Translation

Most XMPP Clients are distributed in multiple languages. In the process of translating a client, people with various backgrounds (not necessarily XMPP-related) are contributing translations.
This table of terms (German, French and Spanish to begin with) aims to be a reference for recommended translations in the future.

At the moment, this table intends to support discussing the translation of key terms. [Discuss with us!](xmpp:modernxmpp@rooms.modernxmpp.org?join)

| English term            | German         | French            | Spanish            | Portuguese         | Japanese         |
|-------------------------|----------------|-------------------|--------------------|--------------------|------------------|
| Group chat              | Gruppenchat    | Groupe            | Grupo de chat      | Grupo de conversa  | グループチャット |
| Channel                 | Channel        | Salon             | Canal              | Canal              | チャンネル       |
| Participant             | Teilnehmer     | Participant       | Participantes      | Participantes      | 参加者           |
| Address or XMPP address | XMPP-Adresse   | Adresse XMPP      | Dirección XMPP     | Endereço XMPP      | XMPPアドレス     |
| Contact list            | Kontaktliste   | Liste de contacts | Lista de contactos | Lista de contactos | 連絡帳           |
| Profile picture         | Profilbild     |                   |                    |                    | プロフィーロ写真 |

You’ll find more terms in the [term overview](/translation-discussion).

[Add a language...](https://github.com/modernxmpp/modernxmpp)

<!-- Footnotes -->

[^rationale-gc]: Rationale [group chat terminology](/rationale#terminology)

[Multi-user Chats]: client/groupchat.md

[^rationale-dev-terms]: General agreement is that this would only cause confusion, for little gain. See e.g. discussion at https://github.com/modernxmpp/modernxmpp/pull/23
