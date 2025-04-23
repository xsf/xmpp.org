---
title: "Technische Zusammenfassung: Argumente für XMPP - Warum Meta sich echte Messenger-Interoperabilität bemühen muss"
layout: single_open_letter_meta_dma
date: 2025-03-27
author: XMPP Standards Foundation
---

## Einleitung
Der **[Digital Markets Act (DMA)](https://digital-markets-act.ec.europa.eu/about-dma_en?prefLang=de&etrans=de)** der Europäischen Union (EU) wurde erlassen, um fairen Wettbewerb zu schützen und große Technologieunternehmen davon abzuhalten, ihre dominante Marktposition auszunutzen. Ein wesentliches Element des DMA ist die Anforderung an **Number-Independent Interpersonal Communication Services (NIICS)** - u.A. Messenger-Dienste wie WhatsApp - echte Interoperabilität mit den Diensten Dritter herzustellen. Diese Anforderung ist essentiell, um sogenannte "Walled Gardens" abzubauen, den Nutzenden freie Auswahl zwischen den Diensten zu ermöglichen und ein kompetitives, digitales Ökosystem zu fördern.

Die **[XMPP Standards Foundation (XSF)](https://xmpp.org/about/xmpp-standards-foundation/)[EN]** hat die folgende Implementierung des DMA in der EU aufmerksam beobachtet und dabei insbesondere die **Messenger-Interoperabilität** in den Blick genommen. Als Organisation, die offenen Messenger-Standards verpflichtet ist, helfen wir Stakeholdern dabei, die Grundsätze und Technizitäten interoperabler Kommunikationsdienste zu verstehen.

Seit über 25 Jahren haben wir das **eXtensible Messaging and Presence Protocol (XMPP)** entwickelt und weiterentwickelt - einen robusten, erweiterbaren und offenen Standard, der weltweit die Interoperabilität von Kommunikationsdiensten vorangebracht hat. Die XSF wie auch XMPP insgesamt sind unabhängig von jeglichen Anbietern: durch die Mitgliedschaftsvoraussetzungen der XSF auf der einen Seite und die Dezentralität und Erweiterbarkeit des Protokolls XMPP auf der anderen Seite. Manche unserer Mitglieder sind seit XMPPs Geburtsstunde im Jahr 1999 in seine Entwicklung involviert und einige haben der EU bereits Orientierungshilfe gegeben, als neutrale Experten die auf die extensiven Ressourcen und Expertise unserer Foundation verweisen können.

Dennoch glauben wir, unsere Stimme nun nachdrücklich erheben zu müsse. Die von den großen Gatekeepern proprietärer Messenger-Netzwerke eingeschlagene Richtung ist Anlass für ernste Bedenken. Die von ihnen vorgeschlagenen Interoperabilitätslösungen wirken bestenfalls wie halbherzige Maßnahmen, die den Status Quo erhalten sollen. Schlechtestenfalls wie planvolle Strategien zur Verstärkung ihrer Marktmacht unter dem Feigenblatt der Compliance.

Meta, ein [Gatekeeper im Sinne des DMA](https://digital-markets-act.ec.europa.eu/gatekeepers_en)[EN], ist aufgrund seiner Kontrolle über WhatsApp und "Messenger" das einzige Unternehmen im Messenger-Bereich, das den Interoperabilitätsanforderungen des DMA unterliegt. Jedoch bleibt Metas gegenwärtiger DMA-Vorschlag weit hinter den Zielen der EU zurück. Anstatt echte Interoperabilität voranzutreiben, droht der Vorschlag Metas Marktmacht weiter zu zementieren - indem er Metas Kontrolle über Nutzenden-Daten stärkt und wettbewerbsschädliche Netzwerkeffekte verstärkt.

Mit diesem offenen Brief rufen wir zu einer Kurskorrektur auf - eine, die echten Wettbewerb und echte Freiheit der Messenger-Nutzenden sichert, zum Wohle von Individuen, Unternehmen und dem digitalen Ökosystem insgesamt.

## Der Beitrag der XSF zum Wachstum des XMPP-Protokolls

Der XSF-Webseite ist zu entnehmen:

> Die XMPP Standards Foundation (auch bekannt als XSF und zuvor als Jabber Software Foundation) ist eine unabhängige, gemeinnützige Organisation zur Entwicklung technischer Standards, deren primärer Auftrag die Definition offener Protokolle für Präsenz, Instant Messaging und Echtzeitkommunikation auf Basis des Extensible Messaging and Presence Protocols (XMPP) der IETF ist
>
> Die XSF stellt der weltweiten Gemeinschaft der Jabber-/XMPP-Entwickler:innen, Diensteanbieter:innen und Endnutzer:innen außerdem Informationen und Infrastruktur zur Verfügung.
>
> ---
>
> The XMPP Standards Foundation (also known as the XSF and formerly the Jabber Software Foundation) is an independent, nonprofit standards development organisation whose primary mission is to define open protocols for presence, instant messaging, and real-time communication and collaboration on top of the IETF’s Extensible Messaging and Presence Protocol (XMPP).
>
> The XSF also provides information and infrastructure to the worldwide community of Jabber/XMPP developers, service providers, and end users.

### Ursprünge und frühe Entwicklung

Ziel der XMPP-Begründer:innen im Jahr 1999 war es, eine offene Spezifikation zu gestalten, die die Entstehung eines vollständig interoperablen, föderierten Messenger-Netzwerkes ermöglichen würde. Sie wählten einen pragmatischen Ansatz, der es erlauben sollte, serverseitig Brücken in andere Netzwerke zu bauen. Die Nutzenden konnten ihre Legacy-Kommunikationskonten - damals hauptsächlich ICQ, Yahoo! Messenger und Microsoft Messenger - über mit dem damals noch Jabber genannten XMPP-Protokoll als Ankerpunkt verbinden. Entwicklung und Betrieb dieser Brücken geschah damals serverseitig, um das Protokoll schnell anpassen zu können und es den Clients zu ermöglichen, möglichsts effizient mehrere Konten zu benutzen.

Die [Jabber-Initiative war ein Erfolg](https://xmpp.org/about/history/)[EN]. Entwickelnde aus aller Welt trugen dazu bei, Messenger-Interoperabilität Wirklichkeit werden zu lassen. So entstanden mehrere konforme Server und Clients, viele als Open Source-Software, mithilfe derer ein riesiges, föderiertes Netzwerkes über tausende Domänen hinweg entstand.

### Standardisierung und industrieller Einsatz

Das ehemalige Jabber wurde der **Internet Engineering Task Force (IETF)** vorgelegt und im Jahr 2004 durch die **RFCs 3920 und 3921** ein offizieller Standard - unter dem Namen "XMPP".

In ganz Europa boten Internetdienstleister wie **Libertysurf, SAPO und 1&1** XMPP-basierte Clients und Dienste an. Das Protokoll gewann an zusätzlicher Fahrt, als **Google Talk** im Jahr 2005 XMPP in einer föderierten Installation zu betreiben begann und so großformatige Messenger-Interoperabilität ermöglichte.

Im **Mai 2008 kündigte Facebook den Start einer XMPP-Schnittstelle** seines Chatdienstes an, sodass Nutzende sich mit **normalen XMPP-Clients** (damals noch Desktop-Clients) zum Facebook-Chat verbinden konnten. Während Facebook internes Protokoll vom Standard abwich, hat es doch eine [standardisierte Jabber-/XMPP-Schnittstelle](https://web.archive.org/web/20100318030410/https://developers.facebook.com/news.php?blog=1&story=361)[EN] angeboten. Damals war **Facebooks XMPP-Dokumentation** vollständig auf in ihren Entwicklungsseiten verfügbar, was die Bedeutung des XMPP-Protokolls für Mainstream-Kommunikationsdienste unterstrich ([archivierte Dokumentation](https://web.archive.org/web/20111006161206/https://developers.facebook.com/docs/chat/))[EN].

**2009 machte Google XMPP zum Herzstück seines kollaborativen Schreibwerkezugs, Google Wave** und demonstrierte damit die Anpassbarkeit des Prtokolls über die Zwecke des Instant Messagings hinaus. Gleichzeitig **haben sich soziale Netzwerke in der ganzen Welt XMPP zugewendet**, so zum Beispiel **Yandex in Russland** und **StudiVZ in Deutschland**.

### Ein bewährter Standard für Messenger-Interoperabilität

XMPP hat die moderne Messenger-Landschaft entscheidend geprägt. Sein Erfolg bestätigt, dass **echte Interoperabilität durch offene, föderierte Protokolle erreicht** wird und dass die größten Technologieunternehmen - u.A. Google und Facebook - diesen Wert einmal anerkannt haben. Angesichts der Mandatierung von Messenger-Interoperabilität durch den DMA bleibt XMPP die praktikabelste und am besten erprobte Lösung, um diese Anforderungen zu erfüllen.

## Smartphones, WhatsApp and die Gatekeeping-Strategie

XMPPs Erfolg, technischen Vorzügen und seiner Geeignetheit für Messenger-Interoperabilität zum Trotz, verlangsamte sich seine Verbreitung als sich die Messenger-Landschaft entwickelte. Der Schub in Richtung proprietärer Plattformen viel zusammen mit dem Aufkommen von Smartphones, was zu größeren, finanziellen Investitionen in Messenger-Dienste und gesteigerten Anstrengungen der dominanten Akteure führte, die Kontrolle über ihre Netzwerke zu konsolidieren.

### Der Wechsel zu mobilen Geräten und der Aufstieg proprietärer Netzwerke

**2007** veröffentlichte Apple das iPhone und leutete damit die Ära des Smartphones und des mobilen Internets ein. **2009** wurde mit der Einführung des App Store und der Push-Benachrichtigungen der Weg für den Start von **WhatsApp**  geebnet. Messaging, zuvor auf mobilen Endgeräten auf SMS beschränkt, wurde schnell ein **reichhaltiges und umfassendes Werkzeug der Kommunikation**.

WhatsApp nutzte strategisch eine öffentliche Ressource - das System der Telefonnummern - als Identifikator für seine nutzenden. Kombiniert mit dem einfachen Zugriff auf die Kontaktbücher moderner Smartphone-Betriebssysteme startete WhatsApp als **XMPP-Dienst mit eingeschränktem Client** und konnte so ein ausgedehntes, **proprietäres** Netzwerk aufbauen. Im Wesentlichen **wurde es das neue ICQ** in noch größerem Format. Durch sein Wachstum positionierte der Dienst sich **im direkten Wettbewerb zu Mobilfunkunternehmen** - als **Over-the-top (OTT) Dienst**,  der traditionelle Netzanbieter mithilfe des offenen Internets umgeht. Damals wurde die **Netzneutralität** als Schutzmaßnahme angesehen, die verhindern sollte, dass Netzanbieter ihre Kontrolle über die Kommunikationsinfrastruktur auszunutzen, aber sie erlaubte auch proprietären Messenger-Diensten unter ihrem Schutzschirm zu wachsen.

### Das entscheidende Jahr: 2014 and der Aufstieg des Messenger-Gatekeeping

Das Jahr 2014 markierte einen kritischen Wendepunkt, speziell für Meta (formals Facebook). In diesem Jahr

- hat **Facebook WhatsApp für 19 Milliarden USD gekauft**, obwohl das Unternehmen Verluste schrieb, und damit die strategische Bedeutung der Kontrolle über Messenger-Dienste unterstrichen;
- hat **Facebook die Unterstützung für XMPP im Facebook Messenger eingestellt** und **2015 ganz entfernt**.

Als Facebook die Unterstützung für XMPP eingestellt haben, hat es simultan [seine neue Messenger-Platform auf seiner F8-Konferenz vorgestellt](https://developers.facebook.com/blog/post/2015/03/25/introducing-messenger-platform-and-businesses-on-messenger/)[EN] und damit ein neues Ökosystem vorgestellt, in welchem **Unternehmen mit ihren Nutzenden in einer von Facebook kontrollierten Umgebung interagieren** konnten. Die Abkehr von XMPP war keine technische Notwendigkeit, sondern eine strategische Entscheidung: Durch die Einschränkung der API und der Interoperabilität nahm Facebook den Unternehmen die Option, außerhalb seiner Plattform zu operieren und andere Werkzeuge zu nutzen, während Facebook volle Kontroller über die Interaktionen seiner Nutzenden und über die Monetarisierung ihrer Daten behielt.

### Die Konsequenz: Eine vollständig geschlossene Messenger-Landschaft

Facebook stand mit dieser Entscheidung nicht alleine, aber es spielte eine **entscheidende Rolle in der Beschränkung von Nachrichtenkommunikation** noch bevor vollständige Interoperabilität erreicht werden konnte. Zusätzlich frustrierend ist diese Entscheidung, weil

- der **Facebook Messenger XMPP ursprünglich unterstützt hat**,
- **WhatsApp schon immer auf einem XMPP-Server basierte** - seine **interne Logik wurzelt weiterhin in XMPP** und dennoch operiert as vollständig geschlossenes System - und
- beide dieselben, quelloffenen XMPP-Server verwendeten, um ihre Infrastruktur aufzuziehen. 

Im Ergebnis sind wir **zurückgefallen auf eine fragmentierte Messenger-Landschaft, ähnlich zu 1999**, bevor föderierte Interoperabilität möglich wurde. Heute **kämpfen mehrere geschlossene Kommunikationsökosysteme um die Vorherrschaft**:

- **Facebook Messenger**,
- **WhatsApp**,
- **Instagram Private Messaging**,
- **Telegram**,
- **WeChat**,
- **LinkedIn Messaging**,
- **verschiedene Messenger-Dienste von Google**
- und noch viele mehr.

Jeder dieser Dienste **läuft isoliert** und zwingt Nutzende entweder mehrere Konten auf den diversen Plattformen zu erstellen, um mit all ihren Kontakten zu kommunizieren, oder nur einen einzigen Dienst zu verwenden - und forciert damit weiter die Konzentration im Kommunikationssektor. Wenn Nutzende sich entscheiden, nur eine App zu verwenden, müssen sie all ihre Kontakte ebenfalls von dieser App überzeugen und tragen damit effektiv dazu bei, **globale Monopole** des Kommunikations zu festigen.

### Über Nachrichten hinaus: Die Einkapselung der Kommunikation

Das Schlimmste daran: das Thema ist nicht länger auf Textnachrichten beschränkt. Moderne Messenger haben ihren Wirkradius auf **Sprach- und Videoanrufe** ausgehnt und **kontrollieren somit digitale Kommunikation im Ganzen**. Wenn wir diesen Kurs nicht ändern, ist das Ende vom Lied klar: Wir bleiben gefangen in einem Rennen um das **globale Monopol über die Kommunikation im Internet**, unter dem eine handvoll Gatekeeper die Bedingungen diktieren, Wettbewerb einschränken und die Freiheit ihrer Nutzenden beschneiden.


## Die Europäische Kommission und der Digital Markets Act

Um extreme Machtkonzentration im Messenger-Sektor zu verhindern, hat die **Europäische Kommission Messenger fest im Geltungsbereich des DMA verankert**. Ihr Ziel ist es, sicherzustellen, dass Kommunikation **offen, fair und wettbewerbs-basiert** bleibt und eine Zukunft zu verhindern, in der Messenger global von einem **Monopol, Duopol oder, bestenfalls, Oligopol** kontrolliert wird. Die Durchsetzung von Interoperabilität ist der einzige Weg, Nutzenden die **freie Wahl ihrer präferierten Provider** zu ermöglichen anstatt sie in den vorherrschenden Plattformen einzusperren.

Von diesem Geist getragen - einen wahrhaft **kompetitiven Markt** zu ermöglichen, auf dem Nutzende den Provider auswählen können, der am besten zu ihren **Budgets, Geschäftsmodellen und Privatheitsbedürfnissen** passt - müssen wir zurückkehren zum **Kernprinzip der Interoperabilität: die Orientierung an offenen Standards der Kommunikationstechnologie**.

Das ist die Absicht hinter den Anforderungen des DMA.

## Warum die XSF über Metas Vorschlag besorgt ist und warum XMPP die Lösung darstellt

Meta hat seinen Vorschlag für Messenger-Interoperabilität an die Europäische Kommission übermittelt. Wir haben ernsthafte Bedenken, dass Metas Vorschlag nicht bloß **den Status Quo erhalten**, sondern **Meta noch mehr Kontrolle über Nutzendendaten** geben könnte.


### Wesentliche Einwände gegen Metas Interoperabilitätsvorschlag

#### 1. Restriktiver Zugang über NDAs und andere Vereinbarungen

Meta verlangt von Unternehmen **eine Geheimhaltungsvereinbarung (non-disclosure agreement, NDA)** zu unterzeichnen, wenn sie Zugriff auf ihre Interoperabilitätsdokumentation haben wollen und wird die Kommunikation zwischen Netzwerken höchstwahrscheinlich von der Zustimmung zu bestimmten Vereinbarungen abhängig machen. So **bleibt Meta effektiver Gatekeeper**, um wie beim Start von *Messenger for Businesses* die Kontrolle über Nutzendeninteraktionen zu behalten und weiterhin ihr Nutznießer zu sein.

Gegenüber Mitbewerbern **gewähren solche Vereinbarungen Meta einen überproportionalen Hebel** aufgrund der großen Nutzendenbasis. Das ist **keine echte Interoperabilität** - es ist ein **ausgehandletes Privileg**, das Metas vorherrschende Stellung festigt.

Ein NDA zu verlangen **sperrt gemeinnützige Organisationen wie die XSF aus** und nimmt ihnen die Möglichkeit, die Interoperabilitätsmechanismen zu evaluieren und zu ihnen beizutragen. Es **blockiert Open Source-Entwickelnde in der Implementierung von Interoperabilität** in ihrer Software. Innovationsmöglichkeiten werden so scharf beschnitten.

#### 2. Schnittstellen statt offene Protokolle

Metas Vorschlag scheint mehr auf **Schnittstellen anstatt auf offenen Protokollen** zu basieren. Das ist ein tiefgreifendes Problem:

- **Protokolle** sind auf **Interoperabilität und Kooperation** ausgerichtet und sichern somit langfristige Stabilität.
- **Schnittstellen** werden von ihren Anbietern kontrolliert und bieten nur eine **limitierte Auswahl von Features**, zusammen **Nutzungsgrenzen, Abgaben und Einschränkungen**, die sich jederzeit ändern können.

Die Industrie hat die Gefahren des Vertrauens auf Schnittstellen bereits gesehen: bei Twitter, Facebook und Reddit, wo der Schnittstellen-Zugang zulasten des darum liegenden Ökosystems eingeschränkt oder monetarisiert wurde. **Auf einer Schnittstelle allein kann kein dauerhaftes Geschäftsmodell und kein langfristiges Projekt gebaut werden.**

#### 3. Client-seitiger Ansatz ermöglicht Tracking

Metas Ansatz scheint **externe Nutzende zu zwingen, sich wie Meta-Nutzendene** zu verhalten. Das bedeutet:

- Ihr Identifikator wäre in Metas System.
- Mithilfe der durch seine Plattform fließenden Metadaten **könnte Meta externe Nutzende tracken**, auch dann, wenn sie keine Meta-Nutzenden sind.
- Falls **Telefonnummern als Identifikator verlangt** würden, würde das **plattformübergreifendes Tracking** und **Nutzenden-Abgleich** ermöglich, wodurch Metas Datensammlungspraktiken noch weiter ausgedehnt würden.

Dadurch entstehen schwerwiegende Privatsphäre-Risiken, insbesondere für solche Menschen die explizit **nicht Teil von Metas Ökosystem sein wollen**.

#### 4. Das Skalierungsproblem: Schnittstellen-Brücken funktionieren nicht

Schnittstellen zur Herstellung von Interoperabilität zu nutzen ist ineffizient und **skaliert nicht**. Man stelle sich vor:

- Wenn ein Messenger-Dienst möchte mit zehn Anbietern interoperieren will, muss er **zehn separate Schnittstellen-Brücken entwickeln und betreiben**.
- Dieser Ansatz ist **nicht nachhaltig**, da die Kosten und der Wartungsaufwand kleinere Akteur:innen ausschließen würde.
- Schlimmer noch, **Plattformen könnten dieses Schlupfhoch zur Vermeidung echter Interoperabilität nutzen**. Beispielsweise könnten Meta und Telegram jeweils eine Schnittstelle anbieten, die jeweilig andere aber nicht implementieren und beahupten, sie wären offen für Interoperabilität - während sich **tatsächlich nichts ändert**. Das **unterminiert die Absichten des DMA vollständig**.

### Föderation verstehen: Eine Telefon-Analogie: Warum Metas Ansatz mangelhaft ist

Deswegen **schreitet die XSF ein** und wirbt für Interoperabilität auf Basis von Föderationsprinzipien, die das Herz der großen Internetprotokolle darstellen und seine Offenheit ermöglicht haben.

Um die Mängel des von Meta unterbreiteten Vorschlags besser zu verstehen, kann man es mit einem anderen, essentiellen Kommunikationssystem vergleichen: **das globale Telefonnetzwerk**.


Heutzutage sind Telefonnetzwerke **interopabel und föderiert**. Egal welchen Provider man benutzt, man kann alle, die in anderen Netzwerken sind, anrufen - egal, ob Festnetz oder Mobilfunknetz. **Man braucht nicht bei jedem Provider ein Konto um zu kommunizieren.** Diese bruchlose Föderation ist möglich, weil

1. **ein standardisiertes, gemeinsames Protokoll** universelle Kommunikationstechniken sichert und
2. **ein verteiltes System von Identifikatoren** den Verbindungsaufbau zwischen Providern erlaubt.

**Dasselbe Modell kann und sollte für Messenger-Interoperabilität genutzt werden**.

Die XSF hat den Löwenanteil schon erledigt: wenn wir **XMPP S2S (server-to-server) als Interoperabilitätsstandard übernehmen**, können wir **dieselbe bruchlose Kommunikation bei Messengern** erreichen.

## Interoperabilität durch XMPP-Föderation

Der effektivste Ansatzu für Interoperabilität heißt **Föderation**. Es ist das Prinzip, das **E-Mail** und **dezentralisierten, föderierten sozialen Netzwerken**, wie denen die **ActivityPub (z.B. Mastodon)** oder eigenen Ansätzen wie bei **Bluesky** zugrundeliegt.

Meta argumentiert gegen Föderation, mit der Behauptung sie müssten **ihre Nutzenden for Spam, Missbrauch und Sicherheitsbedrohungen schützen**. Schutz der Nutzenden ist wichtig, aber **Föderation ist nicht inhärent unsicher**. Tatsächlich wurden **diese Bedenken bei der Gestaltung von XMPP bedacht** - das Ziel ist ein **nachhaltiges, globales, föderiertes Messenger-Netzwerk** mit **eingebauten Sicherheits-, Moderations- und Kontrollmechanismen**.

### Wie Föderation funktioniert

In einem föderierten System besteht ein Identifikator aus **zwei Komponenten**:

1. **Die Domäne** - Sie dient als **erste Ebene der Weiterleitung** von Nachrichten und Interaktionen, ähnlich wie bei E-Mail-Adresse (z.B. `user@domain123.eu`). Sie stellt sicher, dass Nachrichten **an den richtigen Provider** zugestellt werden.
2. **Der Name, Identifikator oder Schlüssel** - Dieser wird durch den Provider zugewiesen und **leitet Kommunikation intern** an die jeweiligen Nutzer. Wichtig ist, dass er **keine privaten Informationen offenlegen muss** und stattdessen Provider-intern verarbeitet werden kann, um gegenüber anderen Providern die **Privatsphäre der Nutzenden zu schützen**.

Föderations arbeitet mit **Server-zu-Server (s2s) Kommunikation**, einer **flexiblen und Privatsphäre-bewussten** Lösung für Interoperabilität. E-Mail ermöglicht es, mit dem Wissen über eine öffentliche Adresse wie `user@domain123.eu` Kommunikation herzustellen, **ohne sensible Details preiszugeben**, wie z.B. die Telefonnummer. Dasselbe Prinzip findet auf föderierte Protokolle wie **XMPP und ActivityPub** Anwendung.


### Wie Föderation Sicherheit & Kontrolle verbessert

Ein häufiges Missverständnis ist, dass **Föderation Sicherheit kompromittieren** würde. In Wahrheit **bietet Föderation starke Sicherheitsmaßnahmen**, erlaubt aber trotzdem **Providern zu moderieren und Kontrolle auszuüben**.

Föderierte Systeme kennen eine **klare Unterscheidung zwischen interner und externer Kommunikation**:


1. **Client-zu-Server (c2s) Protokoll** - Regelt die Kommunikation zwischen **Provider und seinen internen Nutzenden**. Die Nutzenden melden sich hier mit ihren Zugangsdaten an.
2. **Server-to-Server (s2s) Protokoll** - Regelt die **externe Kommunikation zwischen Providern** und stellt damit sicher, dass **interner Traffic der Nutzenden isoliert** von externen Gefahrne bleibt.

Das gibt allen Providern, auch Meta, die Möglichkeit **mehrere Schutzschichten** aufzubauen:

1. **Trennung von internem und externem  Traffic**
   - Interner Nutzenden-Traffic und externe Kommunikation werden **an unterschiedlichen Endpunkten** verarbeitet.
   - In Notfallen können Provider **externen Traffic vollständig blockieren** während **interne Kommunikation funktionabel** bleibt.

2. **Domänen-spezifische Moderation und Blockade**
   - Provider können **externe Domänen bannen**, wenn sie Spam oder schädliches Material verbreiten oder nicht ordentlich moderiert sind.

3. **Verbessertes Monitoring und Durchsetzung von Sicherheit**
   - Provider können **s2s Traffic beobachten**, um **Spam, DoS-Angriffe und andere Sicherheitsbedrohungen zu bekämpfen**.
   - Anders als zentralisierte Systeme, **ermöglicht Föderation den Providern die Implementierung eigener Sicherheitsrichtlinien** ohne auf eine:n einzelne:n Akteur:in angewiesen zu sein.

## Meta, Föderation und XMPP

Es gibt **keine technische Beschränkung**, die Meta davon abhalten könnte, **XMPP** zu verwenden - tatsächlich **hat Meta das in der Vergangenheit bereits**.

### Metas Geschichte mit XMPP: Nachweis der Umsetzbarkeit

Meta hat früher XMPP in seinen Messenger-Produkten verwendet oder unterstützt:

- Der **Facebook Messenger** hat XMPP ursprünglich unterstützt, aber später die Konformität eingestellt. Dieser Umstellung **lagen keine techischen Beschränkungen zugrunde**, sondern es war eine **strategische Entscheidung**, um Nutzende in Metas proprietäres Ökosystem zu drängen, sodass es seine gewaltige Nutzendenbasis in einen Netzwerkeffekt zu seinem Vorteil verwandeln konnte.
- **WhatsApp** basierte ursprünglich auf einem **quelloffenen XMPP-Server** - der noch immer **den Kern seiner Infrastruktur** bildet.
  - Das **von WhatsApp genutzte Protokoll** ist eine **direkte Abwandlung von XMPP**, bei dem die XML-basierten Tags in ein **Binärformat** umgewandelt wurden, um **Kompaktheit** zu gewinnen.
  - Trotz dieser Änderung bleibt das **grundlegende Design und die Semantik identisch zu XMPP**.

### Metas selektive Nutzung von Föderation

Meta hat in der Vergangenheit **Willen zur Föderation** demonstriert - aber **nur wenn es seinen strategischen Interessen dient**.

Ein Beispiel: **Threads**, Metas soziales Netzwerk, hat sich verpflichtet **ActivityPub und das Fediverse-Protokoll zu unterstützen**. Die **Fediverse-Föderation und ihre ID-System** funktionieren **auf dieselbe Weise wie XMPP für Messenger-Föderation**.
Es **stellt sich die Frage**: 
Wenn **Meta gewillt ist, Föderation zu unterstützen**, weil sie im Falle von Threads **Wettbewerb durch Twitter/X und Bluesky** erfahren, warum will es **zögerlich XMPP für Messenger-Interoperabilität** unter dem **DMA** zu nutzen?


Der grundlegende Unterschied ist kein technischer. Es ist Strategie:

- Im Bereich der Messenger genießt Meta **Marktdominanz**, mit Milliarden Nutzenden auf **WhatsApp, Messenger und Instagram**.
- Im Gegensatz dazu **strauchelt Threads gegenüber Twitter/X und Bluesky** - und Meta unterstützt Föderation um gegenüber den anderen Plattformen Boden gut zu machen.

Mit anderen Worten, **Meta unterstützt offene Protokolle wenn es davon profitiert, aber verweigert sich ihnen, wenn sie seine Marktmacht bedrohen**.

Wäre Meta wirklich aufrichtig der **Interoperabilität** verpflichtet, würde es **XMPP als praktikabelstes und erprobtestes Protokoll für föderierte Messenger** anerkennen - wie es das in der Vergangenheit getan hat.

## Die Zukunft der Messenger gestalten

Föderation **ist kein Sicherheitsrisiko - es ist ein skalierbares, Privatsphäre-respektierendes Modell** das längst **in globalen Kommunikationsnetzwerken wie E-Mail und föderierten, sozialen Netzwerken erprobt** wurde. Mit dem **XMPP Server-zu-Server (s2s) Protokoll** können Messenger-Dienste **echte Interoperabilität erreichen** und **Sicherheit, Privatsphäre und Kontrolle** wahren.

### Aufruf an Meta: Baut Euren Interopabilitätsstack auf XMPP

Die XSF hält Meta an, seinen Interoperabilitätsstack auf XMPP-Föderation aufzusetzen.

Wenn Threads das Fediverse-Protokoll implementieren kann, dann gibt es keinen Grund aus dem heraus Meta dasselbe nicht auch mit XMPP für den Facebook Messenger und WhatsApp leisten könnte - insbesondere weil WhatsApp auf XMPP aufgebaut wurde.

### Die XSF begrüßt Kollaboration

Die XSF ist eine offene und inklusive Organisation, die Mitarbeit von Unternehmen, Entwickler:innen, Anbieter:innen und Providern herzlich willkommen heißt. Wir verstehen, dass obwohl "Messenger" und WhatsApp ursprünglich auf XMPP basierten, technische Diskussionen vonnöten sein werden, um die Protokolle und Metas gegenwärtige Bedürfnisse zusammenzubringen.

Falls Meta spezifische Anforderungen haben sollte, wie z.B.:

- Features, die im Facebook Messenger oder in WhatsApp einzigartig sind,
- Skalierungsüberlegungen angesichts der Höhe der Nutzendenzahlen oder
- neue Erweiterungen, die auf Metas spezifischen Anwendungsfall eingehen,

dann ist die XSF der richtige Ort, um diese Diskussionen zu führen. Es ist unsere Mission, föderierte Messenger-Standards weiterzuentwickeln und zu verbessern.


### Tretet der Diskussion um die Zukunft föderierter Messenger bei

Wir gehen davon aus, dass Meta sich in die Entwicklung von XMPP würde einbringen wollen und laden Metas herausragende Messaging-Expert:innen ein, ihre Expertise und Ideen, aber auch ihre Bedenken in die Arbeit der XSF einzubringen.

Lasst uns zusammenarbeiten, um eine wahrhaft interoperable, offene, und kompetetive Zukunft der Messenger zu gestalten!

***

## Kontaktinformationen

Presse- und allgemeine Anfragen: [info@xmpp.org](mailto:info@xmpp.org)

Ralph Meijer  
[Chair of the Board](/about/xsf/people#chair)  
XMPP: [ralphm@ik.nu](xmpp:ralphm@ik.nu)  
Mail: [ralphm@ik.nu](mailto:ralphm@ik.nu)

Matthew Wild  
[Executive Director](/about/xsf/people#executive-director)  
XMPP: [me@matthewwild.co.uk](xmpp:me@matthewwild.co.uk)  
Mail: [me@matthewwild.co.uk](mailto:me@matthewwild.co.uk)

Mickaël Rémond  
Mitglied der XSF und Berichterstatter der XSF für den DMA  
XMPP: [mremond@process-one.net](xmpp:mremond@process-one.net)  
Mail: [mremond@process-one.net](mailto:mremond@process-one.net)
