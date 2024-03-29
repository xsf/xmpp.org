---
title: Der XMPP Newsletter Mai 2022
date: 2022-06-05
categories: ['Newsletter']
---

*Info: [Anoxinon e.V.](https://anoxinon.de/) publiziert die deutsche Übersetzung des unter der CC by-sa 4.0 Lizenz stehenden XMPP Newsletters für die XSF Foundation. Den [Originalartikel findest Du im Blog der XSF](https://xmpp.org/2022/06/the-xmpp-newsletter-may-2022/). Übersetzung und Korrektur der dt. Version von Anoxinon e.V..*

Willkommen zum XMPP Newsletter, schön, dass du wieder da bist! Diese Ausgabe umfasst den Mai 2022.

Wie dieser Newsletter auch sind viele Projekte und deren Mühen in der XMPP Gemeinschaft das Ergebnis der Arbeit von Freiwilligen. Wenn du mit den von dir verwendeten Diensten und Applikationen zufrieden bist - gerade in der jetzigen Situation - dann denke bitte darüber nach, dich bei diesen Projekten zu bedanken oder helfend einzubringen! Bist du daran interessiert, das Newsletter-Team zu unterstützen? Ließ mehr am Ende des Artikels.

### Übersetzungen des Newsletters

Dies ist eine Gemeinschafstarbeit und wir wollen allen Übersetzer:innen für deren Beiträge danken! Freiwillige sind Willkommen! Die Übersetzungen des XMPP Newsletters werden auf den folgenden Seiten veröffentlicht (mit etwas Verzögerung):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
- Französisch: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) und [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- Deutsch: [xmpp.org/de/blog](https://xmpp.org/de/blog/) und [anoxinon.de](https://anoxinon.de/blog/)
- Italienisch: [nicfab.it](https://www.nicfab.it/)
- Spanisch: [xmpp.org/es/blog](https://xmpp.org/es/blog/)

## XSF Ankündigungen

![Logo von XMPP, ein "+" und das Logo vom GSoC](/images/logos/GSoC_2022_Logo.png)

- Der Google Summer of Code 2022 steht in den Startlöchern und das Programmieren beginnt bald! Begrüßt die beiden neuen Mitwirkenden Patiga und PawBud, die an Open-Source-Softwareprojekten in der XMPP-Umgebung arbeiten werden!
        - Patiga wird an [flexibleren Dateiübertragungen in Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ) [EN] arbeiten. Mentoren werden fiaxh und Marvin W. sein - vielen Dank an euch beide!
        - PawBud wird daran arbeiten, [Unterstützung für A/V-Kommunikation über Jingle in ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19) [EN] hinzuzufügen. Mentoren werden JC Brand und vanitasvitae sein - vielen Dank auch an euch beide!
 Fühlt euch frei, die Nachricht über [Mastodon](https://fosstodon.org/@xmpp/108358826402429966) [EN] oder [Twitter](https://mobile.twitter.com/xmpp/status/1529199174729728000) [EN] zu verbreiten. Weitere Einzelheiten findest du auf der dafür [vorgesehenen Seite unter xmpp.org](https://xmpp.org/community/gsoc-2022/) [EN].
- Die aktuelle [Abstimmungsphase für XSF-Mitglieder läuft noch](https://wiki.xmpp.org/web/Membership_Applications_Q2_2022) [EN]. Wenn du ein XSF-Mitglied bist, nutze bitte deine Chance, abzustimmen. Wenn du Interesse an einer Bewerbung hast, besuche unsere [entsprechende Seite](https://xmpp.org/community/membership/) [EN].

## XSF finanziell bewirtete Projekte

Die XSF bietet [finanzielle Bewirtung (fiscal hosting)](https://xmpp.org/community/fiscalhost/) [EN] für XMPP-Projekte. Bewerbungen bitte via [Open Collective](https://opencollective.com/xmpp) [EN]. Weitere Informationen finden sich in der [Ankündigung](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/) [EN]. Aktuelle Projekte:

- [Bifrost bridge: Offline Nachrichtenaustausch zwischen Matrix und XMPP](https://opencollective.com/bifrost-mam) [EN]
- [Mellium Co-op](https://opencollective.com/mellium) [EN]

## Veranstaltungen

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours) [EN]: Verfügbar auf unserem [YouTube-Kanal](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA) [EN]
- [Berlin XMPP Treffen (virtuell)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) [EN]: Monatliches Treffen von XMPP-Enthusiast:innen in Berlin, jeden zweiten Mittwoch eines Monats

## Artikel

Der Bifrost-Bridge Fork auf aria-net.org implementierte Unterstützung für Offline-Nachrichten in Matrix-Räumen, auf die über die Bridge zugegriffen wurde: XMPP-Benutzer:innen, die sich über die Bifrost-Bridge mit Matrix-Räumen verbanden, erhielten keine Offline-Nachrichten, da die Unterstützung für die Gruppenchat (MUC)-Historie nicht in die XMPP-Server-Implementierung der Bridge (basierend auf xmpp-js) implementiert war. Dank der großartigen Arbeit von Maranda können wir nun die Historie und auch den Nachrichtenverlauf (MAM) für Matrix zu XMPP überbrückten Räumen unterstützen. In [diesem Beitrag findest du eine vollständige Anleitung](https://opencollective.com/bifrost-mam/updates/maranda-from-aria-net-org-implements-mam-support-in-bifrost-bridge) [EN] zur Nutzung dieser Funktion.

[Der JMP-Newsletter](http://blog.jmp.chat/b/may-newsletter-2022) [EN] kündigt eine neue Version des Cheogram-Android-Clients, SMS-only-Telefonnummern-Ports, eine tiefere Integration mit Snikket und ein [neues Projekt für Social Instance Hosting](https://blog.jmp.chat/b/togethr-sopranica-social) [EN] an.

### Clients und Applikationen

[Gajim 1.4.0](https://gajim.org/de/post/2022-05-11-gajim-1.4.0-released/), [1.4.1](https://gajim.org/de/post/2022-05-21-gajim-1.4.1-released/), [1.4.2](https://gajim.org/de/post/2022-05-25-gajim-1.4.2-released/) und [1.4.3](https://gajim.org/de/post/2022-06-01-gajim-1.4.3-released/) sind veröffentlicht worden! Nach mehr als einem Jahr Entwicklungszeit ist es endlich an der Zeit, die Veröffentlichung von Gajim 1.4 anzukündigen! Die Gajim 1.4 Serie kommt mit einem komplett neu gestalteten Nachrichtenfenster und einer neuen Gesprächsverwaltung. Arbeitsbereiche ermöglichen es dir, deine Chats zu organisieren, um Angelegenheiten getrennt zu halten, wo es nötig ist. Diese Änderungen waren nur durch viele Eingriffe in Gasjims Codebasis möglich, und wir sind dankbar für all das Feedback, das wir von euch erhalten haben.

![Bildschirmfoto des Gajim-Hauptfesters mit einem geöffneten Chat. Man sieht links drei Arbeitsbereiche, eine Liste mit Konversationen, zwei angepinnte Konversationen und eine geöffnete Konversation inklusive Konversationsverlauf selbst.](/images/newsletter/2022-06/gajim-window-1-4.png)

[Psi+ portable 11.5.1627 (2022-05-21)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) [EN] und [Psi+ installer 11.5.1629 (2022-05-31)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) [EN] sind veröffentlicht worden.

Go-sendxmpp [0.5.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.5.0) [EN] mit Verbesserungen an Ox (OpenPGP für XMPP) wurde veröffentlicht, gefolgt von einer Bugfix-Version [0.5.1](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.5.1) [EN].

Das Soprani.ca-Projekt hat ein kleines Tool auf seiner Cheogram-Infrastruktur veröffentlicht, mit dem man [leicht eine äquivalente Matrix-ID für seine Jabber-ID über bekannte Bridges berechnen kann](https://cheogram.com/matrix/)[EN].

![Bildschirmfoto des Cheogram Tools. Man sieht die Eingabemaske für die Jabber-ID und verschiedene Reiter für Jabber-ID, SMS, E-Mail und Telefon, während ersterer ausgewählt ist.]/images/newsletter/2022-06/cheogram.png)


## Server

[ejabberd 22.05](https://www.process-one.net/blog/ejabberd-22-05/) [EN] ist veröffentlicht worden. Diese Version enthält fünf Monate Arbeit, 200 Commits, darunter viele Verbesserungen (MQTT, MUC, PubSub, ...) und Fehlerbehebungen.

```
mod_opt_type(bosh_service_url) ->
    econf:either(auto, econf:binary());
mod_opt_type(websocket_url) ->
    econf:either(auto, econf:binary());
mod_opt_type(conversejs_resources) ->
    econf:either(undefined, econf:directory());
mod_opt_type(conversejs_options) ->
    econf:map(econf:binary(), econf:either(econf:binary(), econf:int()));
mod_opt_type(conversejs_script) ->
    econf:binary();
mod_opt_type(conversejs_css) ->
    econf:binary();
mod_opt_type(default_domain) ->
    econf:binary().

mod_options(_) ->
    [{bosh_service_url, auto},
     {websocket_url, auto},
     {default_domain, <<"@HOST@">>},
     {conversejs_resources, undefined},
     {conversejs_options, []},
     {conversejs_script, auto},
     {conversejs_css, auto}].
```

[Jackal 0.60.0](https://github.com/ortuman/jackal) [EN] wurde veröffentlicht.


### Libraries (Bibliotheken)

[python-nbxmpp Versionen 3.0.0 bis 3.1.0](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) [EN] wurden veröffentlicht, die Unterstützung für Nachrichtenmoderation, Lesezeichen-Erweiterungen und viele Fehlerkorrekturen bieten.

## Extensions and Specifications (Erweiterungen und Spezifikationen)

Entwickler:innen und andere Standard-Expert:innen von aller Welt arbeiten zusammen an diesen Extensions, entwicklen neue Specifications für aufkommende Praktiken und verfeinern die bestehenden Wege, Dinge umzusetzen. Proposed (Vorgeschlagen) werden können sie von jeder und jedem, wobei die besonders erfolgreichen es in den Status Final oder Active (Aktiv) schaffen - je nach Typ. Andere hingegen werden bedacht als Deferred (Zurückgestellt) markiert. Dieser Lebenszyklus ist in [XEP-0001](https://xmpp.org/extensions/xep-0001.html)  [EN] beschrieben, welches die formalen und anerkannten Definitionen für die Types (Typen), States (Status) und Processes (Prozesse) enthält. [Ließ mehr über den Standards Process (Standard-Prozess)](https://xmpp.org/about/standards-process.html) [EN]. Die Kommunikation rund um Standards und Extensions findet auf der [Standards Mailing List [EN]](https://mail.jabber.org/mailman/listinfo/standards) statt. ([Online Archiv](https://mail.jabber.org/pipermail/standards/) [EN].)

Übrigens: Auf xmpp.org gibt es [eine neue Seite über XMPP RFCs](https://xmpp.org/rfcs/) [EN].

### Proposed (Vorgeschlagen)

Der XEP-Entwicklungs-Prozess startet damit, eine Idee auszuformulieren und sie an eine XMPP-Editorin oder einen XMPP-Editor zu übergeben. Innerhalb von zwei Wochen entscheidet der Council (Rat), ob der Vorschlag als Experimental XEP akzeptiert wird.

- Diesen Monat werden keine XEPs vorgeschlagen.

### New (Neu)

- Version 0.1.0 von [XEP-0465](https://xmpp.org/extensions/xep-0465.html) [EN] (Pubsub Public Subscriptions)
    - Angenommen durch Abstimmung des Rates am 2022-04-13. (XEP Editor (jsc))
- Version 0.1.0 von [XEP-0466](https://xmpp.org/extensions/xep-0466.html) [EN] (Ephemeral Messages)
    - Angenommen durch die Abstimmung des Rates am 2022-05-03. (XEP-Redakteur (jsc))

### Deferred (Zurückgestellt)

Wenn ein Experimental XEP für mehr als zwölf Monate nicht aktualisiert wurde, wird es von Experimental zu Deferred verschoben. Sobald es wieder eine Aktualisierung gibt, wird es wieder nach Experimental verschoben.

* Diesen Monat wurden keine XEPs verschoben.

### Updated (Aktualisiert)

- Version 0.3 von [XEP-0365](https://xmpp.org/extensions/xep-0365.html) [EN] (Server to Server communication over STANAG 5066 ARQ)
    - Nutzung des SLEP-Streaming-Dienstes, der in Version 0.1 nicht verfügbar war. Dies bietet eine bessere Dienstabbildung als die direkte Nutzung von 5066 und ermöglicht eine Kompression. (sek)

### Last Call (Letzter Aufruf)

Last Calls werden ausgerufen, sobald jede und jeder mit dem aktuellen Status eines XEPs zufrieden ist. Nachdem der Council (Rat) entscheidet, ob ein XEP bereit scheint, ruft die XMPP-Editorin oder der XMPP-Editor einen Last Call for Comments (Letzten Aufruf für Kommentare) auf. Das Feedback, das während dieses Last Calls gesammelt wird, hilft, das XEP nochmals zu verbessern, bevor es für die Aufwertung zum Entwurf zurück an den Council geht.

* Kein Last Call diesen Monat.

### Stable (Stabil)

* In diesem Monat wurden keine XEPs zu Stable hochgestuft.

### Deprecated (Veraltet)

* Diesen Monat wurde kein XEP als deprecated eingestuft.

### Call for Experience (Aufruf für Erfahrungen)

Ein Call for Experience (ein Aufruf für Erfahrungen) ist, wie ein Last Call, eine explizite Aufforderung für Kommentare. In diesem Fall ist es jedoch hauptsächlich an die Menschen gerichtet, die die Specification implementiert und idealerweise auch ausgerollt haben. Dann stimmt der Council darüber ab, ob sie nach Final verschoben wird.

* Kein Call for Experience in diesem Monat.

## Teile die Neuigkeiten!

Teile unsere Neuigkeiten in "Sozialen Netzwerken":

* [Mastodon](https://fosstodon.org/@xmpp/) [EN]
* [Twitter](https://twitter.com/xmpp) [EN]
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA) [EN]
* [Lemmy-Instanz](https://community.xmpp.net/) [EN]
* [Reddit](https://www.reddit.com/r/xmpp/) [EN]
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/) [EN]

Schau doch auch mal unsere RSS-Feed in [Englisch](https://xmpp.org/feeds/all.atom.xml) und in [Deutsch](https://anoxinon.de/tags/xmpp-newsletter/index.xml) an!

Auf der Suche nach Jobangeboten oder danach eine:n professionelle:n Berater:in für dein XMPP-Projekt? Besuche unser [XMPP job board](https://xmpp.work/) [EN].

## Hilf uns, diesen Newsletter zu erstellen

Der XMPP-Newsletter wurde kollaborativ von der Community produziert. Danke an  Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, daimonduff, emus, Holger, Ludovic Bocquet, Licaon_Kter, Martin, mathieui, MattJ, nicfab, Pirate Praveen, Ppjet6, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat, Ysabeau und Zash für die Hilfe, ihn zu erstellen!

Jede monatliche Ausgabe des Newsletters wird in [einfachen Notiz](https://yopad.eu/p/xmpp-newsletter-365days) [EN] entworfen. Am Ende des Monats wird der Inhalt dieser Notiz in das [XSF Github Repositorium](https://github.com/xsf/xmpp.org/milestone/3) [EN] übertragen. Wir freuen uns immer über Beteiligung. Zögere nicht, unserer Diskussion in unserem [Comm-Team Gruppenchat](xmpp:commteam@muc.xmpp.org?join) [EN] beizutreten und dabei zu helfen, den Newsletter in Community-Arbeit forzuführen. Du hast ein Projekt und schreibst darüber? Denk’ doch darüber nach, die Neuigkeiten oder Veranstaltungen im Newsletter zu teilen und einer großen Zielgruppe zu präsentieren. Schon ein Beitrag von ein paar Minuten ist hilfreich!

Aufgaben, die regelmäßig erledigt werden müssen:

- Neuigkeiten aus dem XMPP-Universum sammeln
- Neuigkeiten und Veranstaltungen kurz zusammenfassen
- Die monatliche Kommunikation über Erweiterungen (XEPs) zusammenfassen
- Den Entwurf des Newsletters gegenlesen
- Medienbilder vorbereiten
- Übersetzungen

## Lizenz

Dieser Newsletter wird unter der [CC BY-SA Lizenz](https://creativecommons.org/licenses/by-sa/4.0/deed.de) [DE] veröffentlicht.