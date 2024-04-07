---
Title: Translation discussion
layout: single-implementation-guidelines
---

Most XMPP clients are distributed in multiple languages. In the process of translating a client, people with various backgrounds (not necessarily XMPP-related) are contributing translations.

The following tables are gathering the various translations of key terms in (a limited set of) clients to give an overview about what is currently used. This document intends to serve as a basis to discuss recommendations for key term translations.

## Translation services used by clients

Client        | Service
--------------|-------------------------------------------------------------------
Conversations | [Weblate](https://translate.codeberg.org/projects/conversations/)
converse.js   | [Weblate](https://hosted.weblate.org/projects/conversejs/)
Dino          | [Weblate](https://hosted.weblate.org/projects/dino/)
Monal         | [Weblate](https://hosted.weblate.org/projects/monal/)
Gajim         | [Weblate](https://translate.gajim.org/)
PSI(+)        | [Transifex](https://www.transifex.com/tehnick/psi-plus/)
Swift         | [swift.im git](https://swift.im/git/swift/tree/Swift/Translations)
yaxim         | [launchpad.net](https://translations.launchpad.net/yaxim/master)

## German

### Terms currently used in clients (German)

| Term \ Client        | Conversations                 | Converse.js                   | Dino                   | Gajim                     | PSI(+)                       | Swift.im            | yaxim                             |
|----------------------|-------------------------------|-------------------------------|------------------------|---------------------------|------------------------------|---------------------|-----------------------------------|
| XMPP address         | XMPP-Adresse                  | XMPP-Adresse                  | JID                    | XMPP-Adresse              | JID                          | JID, Jabber-ID      | JID                               |
| contact list         | Kontaktliste                  | Kontakte                      | Kontaktliste           | Kontaktliste              | Kontaktliste                 | Kontaktliste        | Liste?                            |
| bookmarks            | Lesezeichen                   | Lesezeichen                   | -                      | Gespeicherte Gruppenchats | Lesezeichen                  | Lesezeichen         | -                                 |
| auto join            | Auto-Join-Funktion            | automatisch beitreten         | -                      | automatisch beitreten     | automatisch beitreten        | -                   | -                                 |
| channel              | Channel                       | Gruppenchat, Raum             | Kanal/Konferenz        | Gruppenchat               | Gruppenchat, Chatraum        | Chatraum            | Gruppenchat                       |
| group chat           | Gruppenchat                   | Gruppenchat                   | Raum                   | Gruppenchat               | Gruppenchat, Chatraum        | Chatraum            | Gruppenchat                       |
| role                 | ?                             | Rechte, Rolle                 | -                      | Rolle                     | Rolle, Funktion              | Rolle               | -                                 |
| moderator            | Moderator                     | Moderator                     | -                      | Moderator                 | Moderator                    | Moderator           | -                                 |
| participant          | Teilnehmer                    | Teilnehmer                    | members ?              | Teilnehmer                | Teilnehmer                   | Teilnehmer          | Teilnehmer                        |
| kick                 | ausschließen?                 | hinauswerfen                  | hinauswerfen           | rauswerfen                | rauswerfen                   | rausschmeißen       | kick                              |
| ban                  | ausschließen                 | entfernen                     | -                      | sperren                   | verbannen                    | verbannen           | ban                               |
| affiliation          | Rechte?                       | Zugehörigkeit                 | -                      | Gruppenzugehörigkeit      | Mitgliedschaft, Angliederung | Zugehörigkeit       | -                                 |
| owner                | Eigentümer                    | Eigentümer                    | Eigentümer             | Eigentümer                | Besitzer                     | Besitzer            | -                                 |
| admin                | Administrator                 | Admin                         | Administrator          | Administrator             | Administrator                | Administrator       | -                                 |
| member               | Mitglied                      | Mitglied                      | Mitglied               | Mitglied                  | Mitglied                     | Mitglied            | -                                 |
| user                 | -                             | Besucher                      | Gast                   | -                         | -                            | -                   | -                                 |
| nickname             | Nickname                      | Spitzname, Nickname           | Spitzname              | Spitzname                 | Spitzname                    | Spitzname, Nickname | Nickname                          |
| history              | Verlauf                       | -                             | Gesprächsverlauf       | Unterhaltungsverlauf      | Nachrichtenchronik           | Verlauf             | Chatverlauf, Unterhaltungsverlauf |
| fingerprint          | Fingerabdruck                 | Fingerabdruck                 | Fingerabdruck          | Fingerabdruck             | Fingerabdruck                | -                   | -                                 |
| subscription request | Online-Status anfragen        | Kontaktanfrage[^sub-converse] | Kontaktanfrage         | Kontaktanfrage            | Anfrage                      | Anfrage             | Abonnementanfrage                 |
| subscription         | Online-Status                 | Anwesenheitsabonnement        | -                      | Abonnement                | Abonnement                   | Abonnement          | -                                 |
| chat                 | Unterhaltung                  | Chat                          | Unterhaltung           | Chat                      | Chat                         | Chat                | (Unterhaltung)                    |
| read receipts        | Lese- und Empfangsbestätigung | -                             | Lesebestätigungen      | Empfangsbestätigungen     | Übermittlungsbestätigung     | Empfangsbestätigung | -                                 |
| typing notifications | Tipp-Benachrichtigung         | -                             | Tippbenachrichtigungen | Chatstatus                | Tipp-Benachrichtigung        | -                   | -                                 |
| avatar               | Profilbild                        | Avatarbild                    | Profilbild                      | Kontaktbild               | Avatar                       | Bild                | -                                 |

### Recommended translation

Term         | Translation
-------------|------------
XMPP address |
contact list |
bookmarks    |
auto join    |
...          |

## French

### Terms currently used in clients (French)

| Term \ Client | Conversations          | Converse.js | Dino   | Gajim                 | PSI(+)  | Swift.im  | yaxim  |
|---------------|------------------------|-------------|--------|-----------------------|---------|-----------|--------|
| channel       | Canal                  | Salon       | Salon  | Salon (de discussion) |         | Salon     | Salon  |
| group chat    | Conversation de groupe | Salon       | Salon  | Salon (de discussion) |         | Salon     | Salon  |

### Notes for french translations (from pep.)

English      | French
-------------|-----------------------
group chat   | groupe (de discussion)
channel      | salon (de discussion)
participant  | participant
XMPP address | Adresse XMPP
contact list | Liste de contact

<!-- Footnotes -->

[^sub-converse]: Subscription requests in converse.js are called contact requests
