---
title: Der XMPP Newsletter für September 2025
date: 2025-10-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Herzlich willkommen zum XMPP Newsletter! Schön, Dich wiederzusehen.
Diese Ausgabe behandelt September 2025.

Der [XMPP-Newsletter](/categories/newsletter/) wird präsentiert vom [XSF Communication Team](/about/xsf/comm-team/).

Viele Projekte in der XMPP-Gemeinschaft – auch dieser Newsletter – sind das Ergebnis freiwilliger Arbeit. Wenn Du mit den Diensten und der Software, die Du nutzt, glücklich bist, lass diesen Projekten ein Dankeschön da oder unterstütze sie in ihrer Arbeit. Auch der Newsletter ist ein offenes Projekt.

Informationen dazu, wie Du das [XSF Communication Team](/about/xsf/comm-team/) unterstützen kannst, findest Du am [am Ende des Newsletters](#help-us-to-build-the-newsletter).

## Ankündigungen der XSF

### Mitgliedschaft in der XSF

Wenn Du der XMPP Standards Foundation (XSF) beitreten möchtest, dann [bewirb Dich vor dem 23. November 2025, 00:00 Uhr Weltzeit (UTC)](https://wiki.xmpp.org/web/Membership_Applications_Q4_2025)[EN].

### Wahlen zum XSF-Direktorat und -Beirat 2025

Die [XMPP Standards Foundation](/about/xmpp-standards-foundation/) ruft alle zu Bewerbungen für das [Board of Directors](/about/xmpp-standards-foundation/#board) und Mitglieder für das [XMPP Council](/about/xmpp-standards-foundation/#council) 2025/2026 auf.

Wenn Du Dich für das Board oder das Council bewerben möchtest, füge bitte bis zum 2. November 2024, 0:00 Uhr Weltzeit (UTC), eine [Wiki](https://wiki.xmpp.org/web/Main_Page)-Seite für Deine Kandidatur [zur entsprechenden Wahlübersichtsseite](https://wiki.xmpp.org/web/Board_and_Council_Elections_2025) im Wiki hinzu. 

Bringe Dich in die Entscheidungen und Spezifikationsprozesse der XSF ein und stelle Dich zur Wahl auf!

Hinweis: _Council_-Mitglieder müssen gewählte Mitglieder der XSF sein. Beim _Board of Directors_ besteht diese Beschränkung nicht.

## Videos und Vorträge

- [XMPP Tutorials DE](https://makertube.net/c/xmpp_tutorials_de/videos) by [eversten.net](https://makertube.net/a/eversten.net/video-channels). 
  - [Conversations (XMPP) - Verbindungsproblem nach Update beheben](https://makertube.net/w/8yXjHWpVd77tz5vRySpJeH).
  - [Quicksy - Der einfachste Einstieg in XMPP (iOS-Version)](https://makertube.net/w/7osSvECKBQvFPTYkjP9kz5).
- [UnifiedPush](https://gultsch.video/w/85UeGATR1i13E7j6eKzq2r): Eine [Vorlesung](https://talks.datenspuren.de/ds25/talk/3783DB/) von [Daniel Gultsch](https://gultsch.de/) bei den [Datenspuren 2025](https://www.datenspuren.de/2025/).

## Artikel über XMPP

- [ProcessOne](https://www.process-one.net/)
  - ["Why Europe's 'Chat Control' Proposal Will Cripple European Communication Industry While Failing to Protect Children"](https://www.process-one.net/blog/chat-control-2025/) von [Mickaël Rémond ](https://www.process-one.net/author/mremond/) für den [ProcessOne Blog](https://www.process-one.net/blog/) [EN].
- [XMPP Interoperabilitäts-Tests](https://xmpp-interop-testing.github.io/)[EN]
  - [Lots More Options!](https://xmpp-interop-testing.github.io/2025/09/14/lots-more-options.html): Es wurden eine ganze Reihe an Continuous Integration (CI)-Systemen hinzugefügt. Dieses Mal standen Freiheits-respektierende, quelloffene Projekte im Fokus (u.A. [Jenkins](https://www.jenkins.io/), [Drone](https://www.drone.io/), [Harness](https://www.harness.io/) und [Woodpecker](https://woodpecker-ci.org/) ). Damit vergrößert sich die Zahl der CI-Systeme, in denen XMPP-Interoperabilitätstests laufen können, auf kolossale ELF! Zuzüglich allen anderen Container-basierten Systemen. Falls Du ein anderes CI-System benutzt und dafür gerne Unterstützung sehen würdest oder selbst Unterstützung brauchst, [tritt dem Interop-MUC bei](xmpp:interop@conference.igniterealtime.org?join) oder [öffne ein Github-Issue](https://github.com/XMPP-Interop-Testing/smack-sint-server-extensions). Von [Dan Caseley](https://xmpp-interop-testing.github.io/contact) für den [XMPP Interop Testing Blog](https://xmpp-interop-testing.github.io/blog).
  - [Two New Features for Clearer Testing](https://xmpp-interop-testing.github.io/2025/09/26/new-features-for-clearer-testing.html): Version 1.7.1 aller Test-Runner wurde veröffentlicht. Die Version bringt zwei Verbesserungen, um Interoperabilitätstests sowohl striker als auch einfacher aufzusetzen zu machen! Die Suite kann unmögliche Tests als Fehlschläge handhaben und so sicherstellen, dass "grün" wirklich bedeutet, dass jeder konfigurierte Test durchgelaufen ist und erfolgreich war. Du kanst jetzt zwischen drei Wegen der Provisionierung wählen:
    - Adminkonto mit [XEP-0133](/extensions/xep-0133.html) (Service Administration) um Testkonten anzulegen.
    - Explizite Testkonten, die Du vorab selbst anlegst.
    - Bandinterne Registrierung via [XEP-0077](/extensions/xep-0077.html) (In-Band Registration).
    Wähle den Weg, der am besten zu Deinem Setup passt. Die [Dokumentation](https://xmpp-interop-testing.github.io/documentation/provisioning-accounts)[EN] enthält alle Details zum Nachlesen.
- [Libervia CLI tips](https://mastodon.social/@Goffi/tagged/tips): Wusstest Du , dass Liverbia](https://libervia.org/) ein [CLI](https://libervia.org/__b/doc/backend/libervia-cli/) hat, mit dem man nahezu alles machen kann? Richtig gehört! [Goffi](https://mastodon.social/@Goffi), der Autor, hat eine Serie von Mastodon-Toos verfasst, die Dir dabei helfen, das meiste aus dem CLI herauszuholen! Dateien Teilen, Blogposts verfassen, verschlüsselte Nachrichten senden, Audio- und Videoanrufe, PubSub-Knoten verschlüsseln, Automatisierung von Aufgaben mit Ad-Hoc-Kommandos, u.v.m., gemütlich vom Terminal aus!
- [FastCGI Authorizer](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/#fastcgi-authorizer-implementing-xep_0070-xmpp-confirmation) implementiert [XEP-0070](/extensions/xep-0070.html) (Verifying HTTP Requests via XMPP) XMPP confirmation von [PulkoMandy](https://mastodon.tetaneutral.net/@pulkomandy) in den [pulkomandy.tk Git repositories](https://pulkomandy.tk/gerrit/plugins/gitiles/?format=HTML). [[FR](https://linuxfr.org/users/pulkomandy/journaux/authentifiez-vous-sans-mot-de-passe-grace-a-xmpp-10-ans-plus-tard)]
- [Montando un WhatsApp gateway desde XMPP con Slidge](https://portal.mozz.us/gemini/z3r0.maverick-hq.org/gemlog/montando-un-whatsapp-gateway-desde-xmpp-con-slidge.gmi) von [z3r0](https://gts.maverick-hq.org/@z3r0) via [SMOLNET PORTAL](https://portal.mozz.us/about). [ES]
- [Modern messaging: Running your own XMPP server](https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server/) von [Holger](https://hachyderm.io/@theaitch) für [codedge](https://www.codedge.de/).
- [Install Slidgram in NetBSD](https://eugene-andrienko.com/it/2025/09/20/slidgram-netbsd-install-howto.html) von [Eugene](https://eugene-andrienko.com/about.html) für [Dragon's notes](https://eugene-andrienko.com/).
- XMPP Brasil [feiert seinen ersten Geburtstag](https://mastodon.social/@xmppbrasil/115232713992094928) mit kostenlosen Nutzerkonten für die brasilianische Gemeinschaft und seinem neuen Status als [Anbieter der Kategorie A](https://providers.xmpp.net/provider/xmpp.eco.br/) unter den [XMPP Providers](https://providers.xmpp.net/). [PT]

## Neuigkeiten über XMPP-Software

### XMPP-Clients und -Anwendungen

- [Cheogram](https://cheogram.com/) hat Version [2.19.0-2](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.19.0-2) für Android veröffentlicht. Eine Bugfix-Version, die Probleme mit der Registrierung und Auffindbarkeit in [Snikket](https://snikket.org/)-Instanzen, Insets im neuesten Android behebt und beim Scrollen von Kontoverwaltungen mit vielen Konten behebt, neben anderen Dingen. Sieh Dir das [Änderungsprotokoll](https://git.sr.ht/~singpolyma/cheogram-android/tree/master/item/CHANGELOG.md) an, um alle Details zu erfahren.
- [Conversations](https://conversations.im/) ist in Version [2.19.5](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.5) für Android erschienen. Die Fehlermeldung für Server, die TLS 1.3 nicht unterstützen, wurde verbessert, Probleme mit dem Kippen von Geräten behoben and viele andere [Korrekturen und Verbesserungen implementiert](https://codeberg.org/iNPUTmice/Conversations/compare/2.19.4...2.19.5). Das [Änderungsprotokoll](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) trägt diese Änderungen zusammen.
- [Convo](https://git.disroot.org/badrihippo/convo), der XMPP-Client für [KaiOS](https://www.kaiostech.com/) hat Version [0.2.0](https://git.disroot.org/badrihippo/convo/releases/tag/0.2.0) (Codename "Eyes Only") veröffentlicht. Die Version bringt Ende-zu-Ende-Verschlüsselung mit OMEMO! Damit wird XMPP mit OMEMO zum ersten Mal auf einem "One Button Phone" verfügbar. Alle Ankündigungen findest Du in ihrer [Versionsübersicht](https://git.disroot.org/badrihippo/convo/releases/).

{{< figure src="/images/newsletter/2025-10-05/convo.png" caption="Convo 0.2.0: Ende-zu-Ende-Verschlüsselung mit OMEMO." >}}

- [Gajim](https://gajim.org/) hat die Versionen [2.3.5](https://gajim.org/posts/2025-09-11-gajim-2.3.5-released/) und [2.3.6](https://gajim.org/posts/2025-09-30-gajim-2.3.6-released/) seiner freien und featurerreichen Chatapp für XMPP veröffentlicht. Diese Version bringt neu organisierte Kontoeinstellungen, einen brandneuen Verknüpfungsmanager, mehr Kontaktinformationen, Videovorschauen, Performanzverbesserungen und viele Fehlerkorrekturen. Das jüngste Update löst Probleme mit Videovorschauen sowie mit Probleme mit Lade-Icons. Du kannst einen Blick auf das [Änderungsprotokoll](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) werfen, um alle Details zu erfahren. Danke für all eure Beiträge!

{{< figure src="/images/newsletter/2025-10-05/main-window.png" caption="Gajim 2.3.5 bündelt Präferenzen und Kontoeinstellungen!" >}}

- [Kaidan](https://www.kaidan.im/) hat Version [0.13.0](https://www.kaidan.im/2025/09/21/kaidan-0.13.0/) seiner nutzer:innenfreundlichen, modernen Chatapp für XMPP veröffentlicht. Die neue Version unterstützt die gleichzeitige Verwendung mehrerer Konten, das Aktivieren und Deaktivieren von Konten, Nachrichtenweiterleitungen, verbessert die Kriterienkonsistenz bei Nachrichtenkorrekturen, bringt einen sicheren Passwortspeicher und probiert bei Registrierungsfehlern alle Anbieter aus, neben vielen weiteren neuen Features und Bugfixes! Eine detaillierte Liste der neuen Features, Bugfixes und weiteren Anmerkungen findest Du im [Änderungsprotokoll](https://invent.kde.org/network/kaidan/-/blob/Kaidan/0.13/NEWS.md?ref_type=heads).

{{< figure src="/images/newsletter/2025-10-05/kaidan.png" caption="Kaidan 0.13.0: Mehrere Konten mit Schalter zum (De-)Aktivieren." >}}

- [Monocles](https://monocles.eu/) hat Versionen [2.0.14](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.14) und [2.0.15](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.15) seines Chatclients für Android veröffentlicht. Die Updates bringen die Fähigkeit, Bilder und Dateien oben am Chatfenster anzupinnen, Unterstützung für Geo-URIs in angepinnten Nachrichten und Antwortvorschauen, Videovorschau für angepinnte Nachrichten und ein Audio-Dateiicon für angepinnte Audionachrichten, neben weiteren Verbesserungen im Bezug zu angepinnten Nachrichten. Sie erlauben außerdem antworten an sich selbst, Antworten mit OMEMO und mit einem Antippen zur referenzierten Nachricht zu scrollen, neben vielen weiteren Features und einer Menge Korrekturen. Sieh Dir das [Änderungsprotokoll](https://codeberg.org/monocles/monocles_chat/src/branch/master/fastlane/metadata/android/en-US/changelogs/19101.txt) an und erfahre alle Details!
- [Psi+](https://sourceforge.net/projects/psiplus/) hat Version [1.5.2117 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) des Entwicklungszweigs des [Psi](https://sourceforge.net/projects/psi/)-XMPP-Clients für erfahrene Nutzer:innen veröffentlicht.
- [Renga](http://pulkomandy.tk/projects/renga), XMPP-Client für [Haiku](https://www.haiku-os.org/) ist in Version 1.28 erschienen, mit Verbesserungen bei MUCs und einer Implementierung von [XEP-0070](/extensions/xep-0070.html) (Verifying HTTP Requests via XMPP) zur HTTP-Authentifizierung via XMPP. Details findest Du in den [aktuellen Nachrichten des Projekts](https://pulkomandy.tk/projects/renga#Latestnews).
- [xmpp-web](https://github.com/nioc/xmpp-web/blob/master/README.md) hat Version [0.10.7](https://github.com/nioc/xmpp-web/releases/tag/0.10.7) des leichtgewichtigen Webchats für XMPP-Server veröffentlicht.
- [XOWS](https://github.com/iquercorb/xows/blob/main/README.md) hat Version [0.9.9c](https://github.com/iquercorb/xows/releases/tag/0.9.9c) seines Webclients für XMPP über WebSocket veröffentlicht, mit refaktorisierten Abläufen zum Abruf von Avataren, Optimierungen bei der DOM-Aktualisierung, Fehlerbehebungen im Kontoerstellungsprozess und bei der Dopplung von MUC-Teilnehmeer:innen.

### XMPP-Server

- Die [Gemeinschaft um Ignite Realtime](https://www.igniterealtime.org/) freut sich, die Veröffentlichung von [Openfire 5.0.2](https://discourse.igniterealtime.org/t/openfire-5-0-2-release/95982) verkünden zu dürfen! Diese Version schließt eine kürzlich entdeckte Sicherheitslücke ([CVE-2025-59154](https://github.com/igniterealtime/Openfire/security/advisories/GHSA-w252-645g-87mp)). Die Lücke erlaubte Angreifer:innen, Identitätsschwindel über unsicheres Parsing von "Common Name"-Attributen zu betreiben. Bitte informiere Dich im [Security Advisory](https://github.com/igniterealtime/Openfire/security/advisories/GHSA-w252-645g-87mp) für genauere Informationen. Die Version verbessert auch SystemD-basierte Skripte und löst dabei mühselige Fehlerchen aus Version 5.0.1. Sieh Dir das ganze [Änderungsprotokoll](https://download.igniterealtime.org/openfire/docs/latest/changelog.html) für alle Details an.

### XMPP-Programmbibliotheken und -Werkzeuge

- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md?ref_type=heads) ist in Version [6.3.1](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/6.3.1) erschienen. Alle Details findest Du im [Änderungsprotokoll](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md?ref_type=heads) Version [1.11.2](https://invent.kde.org/libraries/qxmpp/-/tags/v1.11.2) wurde veröffentlicht. Alle Details findest Du im [Änderungsprotokoll](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- [Slidge](https://slidge.im/) ist in den Versionen [0.3.0](https://codeberg.org/slidge/slidge/releases/tag/v0.3.0) und [0.3.1](https://codeberg.org/slidge/slidge/releases/tag/v0.3.1) erschienen. **Migration von der 0.2-Minor-Version ist nicht unterstützt. Das Slide-Homeverzeichnis muss gelöscht und die Nutzer:innen neu angelegt werden**. Neue Features und Verbesserungen umfassen: Unterstützung für (optionale) Reaction-Ausweichlösungen (für ältere XMPP-Clients ohne Unterstützung für Reactions), Verschieben vieler Gateway-weiter Einstellung in die Nutzer:innen-Einstellungen (siehe "preferences"-Kommando) und Unterstützung für Pronomina in VCards. Siehe die [Commit-Übersicht von Version 0.2.12 bis 0.3.0](https://codeberg.org/slidge/slidge/compare/v0.2.12...v0.3.0) für alle Änderungen.
  - [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp#readme), das [WhatsApp](https://www.whatsapp.com/)-zu-XMPP-Gateway auf Basis von Slidge und [whatsmeow](https://github.com/tulir/whatsmeow), hat Versionen [0.3.0beta](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.0beta) und [0.3.0](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.0) veröffentlicht.
  - [sleamdge](https://codeberg.org/slidge/sleamdge#readme), das [Steam](https://steamcommunity.com/)-zu-XMPP-Gateway auf Basis von Slidge und [steamio](https://steam-py.github.io/docs/latest/), ist in Version [0.3.0](https://codeberg.org/slidge/sleamdge/releases/tag/v0.3.0) erschienen.
  - [matteridge](https://codeberg.org/slidge/matteridge#readme), das [Mattermost](https://mattermost.com/)-zu-XMPP-Gateway auf Basis von Slidge und dem [mattermost-api-reference-client](https://git.sr.ht/~nicoco/mattermost-api-reference-client), hat Version [0.3.0](https://codeberg.org/slidge/matteridge/releases/tag/v0.3.0) veröffentlicht.
  - [slidcord](https://codeberg.org/slidge/slidcord#readme), das [Discord](https://discord.com/)-zu-XMPP-Gateway auf Basis von Slidge und [discord.py-self](https://discordpy-self.readthedocs.io/en/latest/), ist in Version [0.3.0](https://codeberg.org/slidge/slidcord/releases/tag/v0.3.0) erschienen.
  - [matridge](https://codeberg.org/slidge/matridge#readme), das [Matrix](https://matrix.org/)-zu-XMPP-Gateway auf Basis von Slidge und [nio](https://matrix-nio.readthedocs.io/en/latest/), hat die Versionen [0.3.0](https://codeberg.org/slidge/matridge/releases/tag/v0.3.0) und [0.3.1](https://codeberg.org/slidge/matridge/releases/tag/v0.3.1) veröffentlicht.
  - [slidgram](https://codeberg.org/slidge/slidgram#readme), das [Telegram](https://telegram.org/)-zu-XMPP-Gateway auf Basis von Slidge und [Pyrofork](https://pyrofork.wulan17.dev/main/), ist in Version [0.3.0](https://codeberg.org/slidge/slidgram/releases/tag/v0.3.0) erschienen.
- [Slixmpp](https://codeberg.org/poezio/slixmpp) Version [1.11.0](https://codeberg.org/poezio/slixmpp/releases/tag/slix-1.11.0) wurde veröffentlicht. Lies die [offizielle Ankündigung](https://blog.mathieui.net/en/slixmpp-1.11.html) für alle Details.
- [xmpp-dns](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/README.md?ref_type=heads) ist in den Versionen [0.5.2](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.5.2) und [0.5.3](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.5.3) erschienen. Alle Details findest Du im [Änderungsprotokoll](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/CHANGELOG.md?ref_type=heads).
- [xmpp-fastcgi-authorizer](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer), ein FastCGI Authorizer, der [XEP-0070](/extensions/xep-0070.html) (Verifying HTTP Requests via XMPP) implementiert und es so ermöglicht, sich mittels eines XMPP-Kontos bei Webseiten anzumelden, hat die Versionen [0.1](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/+/refs/tags/v0.1) und [0.2](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/+/refs/tags/v0.2) veröffentlicht.

## Erweiterungen und Spezifikationen

Die XSF entwickelt Erweiterungen für das XMPP-Protokoll. Diese [XEPs](https://xmpp.org/extensions/) ergänzen die ursprünglichen [XMPP-RFCs](https://xmpp.org/rfcs/). Entwickler:innen und andere Expert:innen für Standardisierung aus der ganzen Welt arbeiten für diese Erweiterungen zusammen. Sie entwickeln neue Spezifikationen für entstehende Features und Praktiken und verbessern bestehende Erweiterungen des Protokolls. Erweiterungen können von jedem Menschen vorgeschlagen werden. Falls erfolgreich, werden sie je nach Typ als _Final_ oder _Active_ hinterlegt. Andere werden als _Deferred_ sorgsam für die Zukunft bewahrt. Beschrieben wird dieser XEP-Lebenszyklus samt förmlicher und kanonischer Definitionen der Typen, Zustände und Prozesse im ersten XEP, [XEP-0001](https://xmpp.org/extensions/xep-0001.html). [Lerne mehr über den Standardisierungsprozess](https://xmpp.org/about/standards-process.html). Über die Standards und Erweiterungen wird auf der [Standards Mailing List](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) kommuniziert ([Online-Archiv](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposed (vorgeschlagen)

Der XEP-Lebenszyklus beginnt damit, eine Idee in einen XEP-Entwurf zu gießen und [dem Editor-Team](/about/xsf/editor-team/) zu übermitteln. Binnen zwei Wochen entscheidet der [Rat](/about/xmpp-standards-foundation/#council) über die Annahme. Der erste Zustand eines angenommenen Entwurf heißt _Experimental_.

- [Pubsub Node Bookmark](/extensions/inbox/pubsub-node-bookmark.html)
  - Diese Spezifikation definiert ein Lesezeichen-Element, das auf einen Pubsub-Knoten zeigt.

### New (neu)

- Diesen Monat sind keine neuen XEPs dazugekommen.

### Deferred (aufgeschoben)

Wenn ein experimenteller XEP länger als zwölf Monate nicht aktualisiert wird, wird er von _Experimental_ nach _Deferred_ verschoben. Nach einer Aktualisierung wird er wieder als _Experimental_ eingestuft.

- Es wurden in diesem Monat keine XEPs aufgeschoben.

### Updated (aktualisiert)

- Version 0.3.1 of [XEP-0317](/extensions/xep-0317.html) (Hats)
  - Typos, completed some examples and paragraph clarifications thanks to badlop feedback. (tj)
- Version 0.2.0 of [XEP-0503](/extensions/xep-0503.html) (Server-side spaces)
  - Rewrite using pubsub semantics. (nc)

### Last Call (letzter Aufruf)

Letzte Aufrufe (_Last Calls_) erfolgen sobald sich der Status eines XEPs konsolidiert hat. Heißt: Nachdem der [Rat](/about/xmpp-standards-foundation/#council) einen XEP für fertig befunden hat, startet [das Editor-Team](/about/xsf/editor-team/) einen letzten Aufruf zu Kommentaren. Die so erhaltenen Rückmeldungen helfen, den XEP zu verbessern. Danach geht er zurück an den Rat, um als _Stable_ eingestuft zu werden.

- Es wurden in diesem Monat keine letzten Aufrufe gestartet.

### Stable (gefestigt)

- Es wurden in diesem Monat keine XEPs nach Stable verschoben.

### Deprecated (veraltet)

- Es wurden in diesem Monat keine XEPs als veraltet eingestuft.

### Rejected (abgewiesen)

- Es wurden in diesem Monat keine XEPs abgewiesen.

## Öffentliche Kanäle im XMPP-Netzwerk

Es werden jeden Tag neue Räume und öffentliche Kanäle im XMPP-Netzwerk erstellt. Wenn Du auf der Suche nach einem neuen, spannenden Kanal bist, sieh Dir die [öffentliche Kanalsuche](https://search.jabber.network/search) an und finde Gruppen und Gemeinschaften, die Deine Interessen teilen!

- Eine Liste aller Kanäle findest Du [hier](https://search.jabber.network).
- Wenn Du nach etwas Bestimmtem suchst, könnten die [Schlagwörter](https://search.jabber.network/tags/) interessant sein!
- Wenn Du nur Kanäle in einer bestimmten Sprache sehen möchtest, füge `lang:xx` im Suchfeld ein, so wie in diesem Beispiel für [Spanisch](https://search.jabber.network/search?q=lang%3Aes&f=y&sinaddr=on&sindescr=on&sinname=on). Ersetze einfach `es` mit dem zweistelligen Ländercode (wie `lang:fr`, `lang:de`, `lang:pt` usw.).

## Spread the news

Teile diese Neuigkeiten auch in anderen Netzwerken:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp-official.bsky.social)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance (inoffiziell)](https://slrpnk.net/c/xmpp)
- [Reddit (inoffiziell)](https://www.reddit.com/r/xmpp/)
- [XMPP Facebook page (inoffiziell)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Du kannst den Newsletter auch als [RSS Feed](/feeds/all.atom.xml) abonnieren!

Auf der Suche nach Jobangeboten im XMPP-Umfeld oder professionellem Consulting für ein XMPP-Projekt? Wirf einen Blick auf unser [job board](https://xmpp.work/)!

### Newsletter-Beiträge & -Übersetzungen

Dieser Newsletter ist ein Gemeinschaftsprojekt und wir bedanken uns herzlich bei allen Mitwirkenden, ob Inhalt oder Übersetzung! Freiwillige und weitere Sprachen sind uns sehr willkommen! Übersetzungen des XMPP-Newsletters sind hier zu finden (mit Verzögerung):

Newsletter-Beiträge in diesem Monat von:
*emus, Badri Sunderarajan, cal0pteryx, Gonzalo Raúl Nemmi, Kris "poVoq", Ludovic Bocquet, XSF iTeam*

Übersetzungsbeiträge:
- [Französisch](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), anubis, Benoît Sibaud, Julien Jorge seveso, Pierre Jarillon*
- [Deutsch](/categories/newsletter/): *Millesimus*
- [Italienisch](https://notes.nicfab.eu): *nicola*
- [Portugiesisch](/categories/newsletter/): *Paulo*

## Hilf dem Newsletter!

Der XMPP-Newsletter wird gemeinsam von der XMPP-Gemeinschaft geschrieben. Die monatlich erscheinende Ausgabe wird in einem [schlichten Pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung) vorbereitet und am Ende des Monats in das [Github-Repositorium der XSF](https://github.com/xsf/xmpp.org/milestone/3) übertragen. Mach gerne mit! Komm in [unseren Chatraum (MUC)](xmpp:commteam@muc.xmpp.org?join) und hilf uns dabei, dieses Projekt fortzuführen. Hast Du ein neues Projekt, von dem Leute wissen sollten? Teile es in unserem Newsletter mit einem großen Publikum!

Regelmäßige Aufgaben umfassen:

- Neuigkeiten aus dem XMPP-Universum sammeln
- diese _kurz_ zusammenfassen
- Zusammenfassung der aktuellen XEP-Entwicklungen
- Begutachtung des Newsletters
- Vorbereitung von Pressebildern
- Übersetzungen
- Kommunikation in den diversen sozialen Medien

### Spenden für XMPP-Projekte

Die XSF bietet XMPP-Projekten an, die [steuerliche Verwaltung ihrer Finanzen](https://xmpp.org/community/fiscalhost/) zu übernehmen. Projekte können dies via [Open Collective](https://opencollective.com/xmpp) anfragen. Für weitere Informationen, siehe [die ursprüngliche Ankündigung im Blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Derzeit kann so an folgende Projekte gespendet werden:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav](https://opencollective.com/pravapp)
- [diasp.in](https://opencollective.com/diasp-in)

## Den Newsletter de-abonnieren

Um Dich aus dieser Liste auszutragen, [logge Dich ein](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/).
Wenn Du Dich noch nie eingeloggt hast, musst Du gegebenenfalls erst einen Account mit der entsprechenden E-Mail-Adresse erstellen.

## Lizenz

Dieser Newsletter wird unter der [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) veröffentlicht.
