---
title: Newsletter XMPP dicembre 2025
date: 2026-01-05
categories: ['Newsletter']
summary: "In questo numero: Preparate le valigie e tenetevi pronti per l'XMPP Summit 28, prendete parte a uno o a tutti e tre gli eventi XMPP al Fosdem 26 e agli altri due al RHL26. Scoprite i meccanismi interni di Monal IM. Ultima newsletter JMP dell'anno. Aggiornate i vostri client con Cheogram, Conversations, Gajim, Kaidan, Monal, Monocles e Quicksy! Aggiornate i vostri server: MoongooseIM 6.0.5, Openfire 5.0.3. e Snikket Server - dicembre 2025. Notizie XEP - una proposta XEP, due aggiornamenti, due novità, una XEP stabile e un ultimo appello!"
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="Banner della newsletter XMPP" >}}

Benvenuti nella newsletter XMPP, è un piacere avervi di nuovo qui!
Questo numero riguarda il mese di dicembre 2025.

La [Newsletter XMPP](/categories/newsletter/) è offerta dal [Team di comunicazione XSF](/about/xsf/comm-team/).

Proprio come qualsiasi altro prodotto o progetto dell'XSF, la Newsletter è il risultato del lavoro volontario dei suoi membri e collaboratori. Se siete soddisfatti dei servizi e dei software che utilizzate, vi invitiamo a ringraziare o aiutare questi progetti!

Ti interessa contribuire al [Team di comunicazione XSF](/about/xsf/comm-team/)? Per saperne di più, leggi [in fondo alla pagina](#help-us-to-build-the-newsletter).

## Annunci XSF

### XMPP Summit 28 & FOSDEM 2026

L'XSF sta organizzando l'[XMPP Summit 28](/2025/11/xmpp-summit-28/), che si terrà giovedì 29 e venerdì 30 gennaio 2026 a Bruxelles (Belgio, Europa). Dopo il Summit, l'XSF prevede anche di partecipare al [FOSDEM 2026](https://fosdem.org/2026/), che si terrà sabato 31 gennaio e domenica 1 febbraio 2026. Trovate tutti i dettagli nel nostro [Wiki](https://wiki.xmpp.org/web/Conferences/Summit_28). Se avete intenzione di partecipare, vi preghiamo di iscrivervi subito, poiché questo ci aiuta nell'organizzazione. L'evento è ovviamente aperto a tutti coloro che sono interessati a partecipare. Diffondete la notizia tra le vostre conoscenze!

### Adesione alla XSF

Se siete interessati ad aderire alla XMPP Standards Foundation come membri, [inviate la vostra candidatura entro il 15 febbraio 2026, alle 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q1_2026).

### Logo XMPP e Font Awesome

L'XSF è orgogliosa di annunciare che il logo ufficiale XMPP è stato [accettato](https://github.com/FortAwesome/Font-Awesome/discussions/21069#discussioncomment-15220358) in [Font Awesome](https://fontawesome.com/start) e sarà incluso nel loro tarball sorgente a partire dalla prossima versione!

## Eventi XMPP

- [XMPP al FOSDEM26](/2025/11/xmpp-at-fosdem-2026/): Si tratta di conferenze relative a XMPP che si terranno nell'ambito del [Decentralised Communication](https://fosdem.org/2026/schedule/track/decentralised-communication/). Questi interventi si terranno nella sala [AW1.126](https://fosdem.org/2026/schedule/room/aw1126/) domenica 31 gennaio 2026. È anche possibile [partecipare alla conversazione](https://chat.fosdem.org/#/room/#2026-decentralised-communication:fosdem.org) o guardare i video in diretta su [aw1126](https://live.fosdem.org/watch/aw1126).
  - [Engineering XMPP Federation: Building Messaging, Voice & Social Features Across Independent Projects](https://fosdem.org/2026/schedule/event/7XJL9E-engineering_xmpp_federation_building_messaging_voice_social_features_across_inde/): L'[XSF](https://xmpp.org) è un ente di standardizzazione che si trova al centro di un ecosistema di sviluppo di implementazioni indipendenti da parte di diversi individui e organizzazioni che lavorano effettivamente insieme, tutti altamente interoperabili, che rilasciano nuove funzionalità a un ritmo elevato. Questo intervento, tenuto da [Jérôme Sautret](https://fosdem.org/2026/schedule/speaker/jerome_sautret/), illustrerà come funzionano le cose su questa scala e sarà presentato congiuntamente da uno sviluppatore di server e uno di client, che mostreranno come collaborano per mettere a punto le loro implementazioni. Questo intervento inizierà alle 13:15 e terminerà alle 13:45 (UTC+1:00).
  - [Movim: Costruire un social network decentralizzato su XMPP](https://fosdem.org/2026/schedule/event/EVSXLA-movim-building-decentralized-social-network-xmpp/): In questo intervento, [Timothée Jaussoin](https://fosdem.org/2026/schedule/speaker/timothee_jaussoin/) presenterà come [Movim](https://movim.eu/) sfrutta lo standard XMPP e le sue estensioni per offrire le funzionalità che gli utenti si aspettano dalle moderne piattaforme social (comunità, messaggistica istantanea, chat di gruppo, videochiamate, blog e una piattaforma di pubblicazione completa in un'esperienza unificata), senza cedere i propri dati a una piattaforma centralizzata, pur rimanendo completamente federato, interoperabile con altri client XMPP come [Conversations](https://conversations.im/) e [Dino](https://dino.im/) e in grado di collegarsi a piattaforme centralizzate come Discord, Telegram e WhatsApp! Questo intervento inizia alle 13:45 e termina alle 14:15 (UTC+1:00).
  - [Cosa stai ascoltando adesso?: Implementazione della funzione "Now Playing" nell'XMPP moderno](https://fosdem.org/2026/schedule/event/8EDWJT-now-playing-revisited/): In questo intervento, [Özcan Oğuz](https://fosdem.org/2026/schedule/speaker/ozcan_oguz/) condividerà il percorso della sua ricerca sull'implementazione di questa funzione nei client XMPP moderni, i protocolli di alcuni sistemi operativi per leggere i media attualmente in riproduzione, lo stato attuale del supporto di [XEP-0118](/extensions/xep-0118.html) (User Tune) e il PoC di una moderna funzionalità "Now Playing". Questo intervento inizierà alle 14:15 e terminerà alle 14:45 (UTC+1:00).
- [XMPP at RHL26](https://rencontreshivernalesdulibre.ch/): questo evento francofono dedicato alla libertà del software si terrà dal 23 al 27 gennaio in Svizzera e ospiterà due conferenze su XMPP. [Codimp](https://social.lithio.fr/users/codimp/) ospiterà la presentazione ['XMPP ou comment ne pas réinventer la roue : messagerie fédérée et sécurisée en 2026'](https://rencontreshivernalesdulibre.ch/timetable/event/xmpp-ou-comment-ne-pas-reinventer-la-roue-messagerie-federee-et-securisee-en-2026/) sui [miglioramenti apportati al protocollo, ai server e ai client negli ultimi cinque anni](https://social.lithio.fr/notice/B1BfCk6RE0mEj9EMds/), mentre [neox](https://forge.a-lec.org/neox/) ospiterà la presentazione ['L'hébergement éthique comme Commun'](https://rencontreshivernalesdulibre.ch/timetable/event/lhebergement-ethique-comme-commun/) sui modi in cui l'organizzazione no profit [Libre en Communs](https://toot.a-lec.org/@a_lec) ha costruito la propria infrastruttura come [common](https://en.wikipedia.org/wiki/Commons) attorno a software completamente libero e hardware compatibile al fine di ospitare progetti e in particolare un servizio XMPP pubblico, che costituisce il nucleo di comunicazione per gestirlo insieme.
- [XMPP al 39C3 CCC](/2025/12/xmpp-at-chaos-communication-congress-39c3/): il [Critical Decentralisation Cluster (CDC)](https://decentral.community/39C3/) è tornato al [39° Chaos Communication Congress](https://events.ccc.de/congress/2025/infos/startpage.html) ad Amburgo (Germania) dal 27 al 30 dicembre 2025. Il CDC ha offerto uno spazio accogliente per discussioni e scambi su tecnologia e politica con altre comunità che lavorano per la decentralizzazione. L'assemblea XMPP ne ha fatto parte grazie al coinvolgimento attivo di [neox](https://forge.a-lec.org/neox) e [mathieui](https://blog.mathieui.net/en/pages/about.html), con quest'ultimo responsabile degli scintillanti adesivi XMPP!

{{< figure src="/images/newsletter/2026-01-05/stickers_39C3.jpg" caption="A sinistra: gli **ambitissimi** adesivi scintillanti XMPP! A destra: l'assemblea XMPP al 39C3 Critical Decentralisation Cluster!" >}}

## Video e conferenze

- [Devuan 6 Excalibur instalamos el cliente xmpp Gajim](https://fediverse.tv/w/gibf1uo3PtNEG2pCNSk1Re) di [gnuxero](@gnuxero@fediverse.tv). [ES]

## Articoli su XMPP

- [Esplorando XMPP ed Ejabberd: Um Estudo Profundo](https://blog.dmarkinfo.com.br/post/explorando-xmpp-e-ejabberd-um-estudo-profundo) di [Eduardo Marques](https://www.dmarkinfo.com.br/novosite/) per [DMarkInfo Blog](https://blog.dmarkinfo.com.br/). [PT_BR]
- [Monal Internals - Serializable Promise framework](https://monal-im.org/post/00015-monal-internals-promise-framework/) di Matthew Fennell per il [Monal IM Blog](https://monal-im.org/post/).
- [Movim](https://movim.eu/): Alcuni di voi potrebbero aver riscontrato [difficoltà nell'aprire Movim come Progressive Web App sul proprio dispositivo Android](https://mov.im/community/pubsub.movim.eu/Movim/some-of-you-might-have-experienced-difficulties-to-open-movim-as-a-progressive-l3bnom). Si tratta di un problema noto su Chrome. Una soluzione alternativa è stata inserita nella versione master, quindi cancella la cache dell'applicazione per implementarla!
- [Riflessioni sul 2025: un anno di crescita, collaborazione e comunità](https://discourse.igniterealtime.org/t/reflecting-on-2025-a-year-of-growth-collaboration-community/96280) di [guus](https://discourse.igniterealtime.org/u/guus/summary) per la [Ignite Realtime Community](https://discourse.igniterealtime.org/).
- [Newsletter JMP - Altre app Cheogram](https://blog.jmp.chat/b/december-newsletter-2025): quest'ultima edizione del tuo aggiornamento pseudo-mensile [JMP](https://jmp.chat/) ti porta notizie sul PIN self-service per il trasferimento della linea, la registrazione solo dati, una raccolta di recenti [Cheogram](https://cheogram.com/) per Android, un consiglio su alcune modifiche al meccanismo di distribuzione ufficiale delle app Cheogram e tutto ciò che c'è da sapere sui tanto attesi client **Cheogram WWW** e **Cheogram iOS** basati su [Borogove](https://snikket.org//blog/borogove-the-new-snikket-sdk/)!
- Il newsgroup XMPP su Usenet: il protocollo NNTP è ancora in uso ed esiste un gruppo Usenet attivo sull'argomento XMPP/Jabber all'indirizzo `alt.chat-programs.jabber`. [NNTP](https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol) è un protocollo standard a livello di applicazione che consente lo scambio di messaggi in sistemi distribuiti come [Usenet](https://en.wikipedia.org/wiki/Usenet) — un protocollo che vale la pena rivisitare. Sono disponibili alcuni server pubblici gratuiti; uno di questi è [Eternal September](https://www.eternal-september.org), che offre una registrazione gratuita aperta. È possibile utilizzare [Thunderbird](https://www.thunderbird.net/en-US/thunderbird/all/), [PAN](https://gitlab.gnome.org/GNOME/pan/-/blob/master/README.org?ref_type=heads) o [TIN](http://www.tin.org/) come client.

## Notizie sul software XMPP

### Client e applicazioni XMPP

- [Cheogram](https://cheogram.com/) ha rilasciato la versione [2.19.0-4](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.19.0-4) per Android. Una versione di bugfix che introduce correzioni alla visualizzazione su tablet, filtri account per avviare nuove chat, alcuni bug che causavano crash, WASM in WebXDC, mostra un ulteriore elemento di contesto sullo stato/fallimento della chiamata, allinea la dimensione del testo dei messaggi con la prossima versione [Snikket](https://snikket.org/), e molto altro ancora! Assicurati di controllare l'[elenco delle modifiche](https://git.sr.ht/~singpolyma/cheogram-android/refs) per tutti i dettagli sulle versioni.
- [Conversations](https://conversations.im/) ha rilasciato le versioni [2.19.6](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.6) e [2.19.7](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.7) per Android. Questa versione introduce un'impostazione per utilizzare sempre i relay, invia le conferme di consegna per impostazione predefinita e attiva l'impostazione "Conferme di lettura" e risolve il problema della cache degli avatar e il DNS che occasionalmente non risolve quando il DNS privato è abilitato. È possibile consultare il [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) per tutti i dettagli.
- [Gajim](https://gajim.org/) ha rilasciato la versione [2.4.1](https://gajim.org/posts/2025-12-13-gajim-2.4.1-released/) della sua app di chat gratuita e completa per XMPP. Questa versione introduce l'anteprima per GIF e formati di file animati simili, oltre a numerose piccole modifiche e correzioni di bug. Grazie per tutti i vostri contributi! Potete consultare il [changelog](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) per tutti i dettagli.

{{< figure src="/images/newsletter/2026-01-05/animated-previews.png" caption="Anteprime animate in Gajim." >}}

- [Kaidan](https://www.kaidan.im/) ha rilasciato la versione [0.14.0](https://www.kaidan.im/2026/01/01/kaidan-0.14.0/) che include alcune nuove fantastiche funzionalità e correzioni! Condivisione multimediale avanzata, filtraggio dei provider XMPP per la creazione di account, messaggi evidenziati, URI XMPP e molte altre nuove funzionalità e correzioni di bug! È possibile trovare un elenco dettagliato delle nuove funzionalità, delle correzioni di bug e delle note nel [changelog](https://invent.kde.org/network/kaidan/-/blob/master/NEWS.md).
- [Monal](https://monal-im.org/) ha rilasciato le versioni [6.4.15](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1067) e [6.4.16](https://github.com/monal-im/Monal/releases/tag/Build_iOS_1069) per iOS e macOS.
- [Monocles](https://monocles.eu/more) ha rilasciato la versione [2.0.18](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.18) del suo client di chat per Android. Ed è ricca di novità! Introduce un editor di profili VCard4, un generatore di codici QR VCard per l'editor degli account, la possibilità di riordinare gli account con il drag and drop, migliora la visibilità del colore del testo nei campi di immissione, aggiunge un'opzione per salvare i file multimediali nella cartella dei download nel visualizzatore multimediale, introduce il calendario della cronologia delle chat, aggiorna l'impostazione TLSv1.3 (attiva di default), aggiunge l'estensione wasm e il MIME application/wasm e molto altro ancora! Assicuratevi di dare un'occhiata al [changelog](https://codeberg.org/monocles/monocles_chat/src/branch/master/fastlane/metadata/android/en-US/changelogs/19504.txt) per tutti i dettagli!
- [Quicksy](https://quicksy.im/) ha rilasciato le versioni [1.17.0](https://github.com/monal-im/Monal/releases/tag/Quicksy_Build_iOS_20) e [1.21.0](https://github.com/monal-im/Monal/releases/tag/Quicksy_Build_iOS_21) per iOS.
- Lo sviluppo iniziale di [MankalaNextGen](https://invent.kde.org/srisharanvs/mankalanextgen), un'interfaccia utente grafica per giocare a [Mancala](https://en.wikipedia.org/wiki/Mancala) è stato realizzato durante il Google Summer of Code 2025 da [Srisharan VS](https://srisharanvs.github.io/). L'applicazione utilizza [QXMPP](https://invent.kde.org/libraries/qxmpp) per consentire il gioco in remoto.

### Server XMPP

- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) ha rilasciato la versione [6.5.0](https://github.com/esl/MongooseIM/releases/tag/6.5.0) della sua soluzione di messaggistica istantanea aziendale. Questa versione introduce nuove funzionalità, modifiche, varie correzioni e miglioramenti. Per ulteriori informazioni, consultare il [changelog](https://github.com/esl/MongooseIM/blob/6.5.0/CHANGELOG.md) e la [documentazione](https://esl.github.io/MongooseDocs/6.5.0/).
- La [comunità Ignite Realtime](https://www.igniterealtime.org/) è lieta di annunciare il rilascio di [Openfire 5.0.3](https://discourse.igniterealtime.org/t/openfire-5-0-3-release/96265)! Questa versione apporta una serie di miglioramenti alla stabilità e correzioni di bug. In particolare, sono stati apportati numerosi miglioramenti alle chat multiutente (MUC). Per ulteriori dettagli, consultare il [changelog completo](https://download.igniterealtime.org/openfire/docs/latest/changelog.html).
- [Snikket Server - Versione dicembre 2025](https://snikket.org/blog/snikket-server-dec-2025/): Snikket conclude l'anno con un'altra piccola versione del suo software lato server. Lo scopo principale di questa versione è quello di correggere un paio di piccoli bug che sono stati scoperti e segnalati dopo l'annuncio della versione precedente. Alcune modifiche degne di nota includono la compatibilità dei messaggi offline e le informazioni di debug del portale web.

### Librerie e strumenti XMPP

- [go-xmpp](https://github.com/xmppo/go-xmpp/blob/master/README.md) versioni [0.3.0](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.0), [0.3.1](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.1) e [0.3.2](https://github.com/xmppo/go-xmpp/releases/tag/v0.3.2).
- [go-sendxmpp](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/README.md?ref_type=heads), uno strumento per inviare messaggi a un contatto XMPP o MUC ispirato a [sendxmpp](https://sendxmpp.hostname.sk/), versioni [0.15.2](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.2), [0.15.3](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.3) [0.15.4](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.4) e [0.15.5](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.15.5). Tutti i dettagli sono disponibili nel [changelog](https://salsa.debian.org/mdosch/go-sendxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- [nbxmpp-client](https://dev.gajim.org/gajim/nbxmpp-client), un piccolo client di prova [GTK](https://www.gtk.org/) per testare vari modi di connettersi a un server, versione [2.0.1](https://dev.gajim.org/gajim/nbxmpp-client/-/tags/v2.0.1) è stato rilasciato. Tutti i dettagli sono disponibili nel [changelog](https://dev.gajim.org/gajim/nbxmpp-client/-/blob/master/CHANGELOG.md?ref_type=heads).
- [peertube-plugin-livechat](https://github.com/JohnXLivingston/peertube-plugin-livechat/blob/main/README.md), un plugin pensato per fornire un sistema di chat per i video [Peertube](https://joinpeertube.org/), versione [14.0.2](https://github.com/JohnXLivingston/peertube-plugin-livechat/releases/tag/v14.0.2) è stato rilasciato.
- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md?ref_type=heads), una libreria Python che fornisce alle applicazioni Python un modo per utilizzare la rete XMPP, versione [7.0.0](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/7.0.0). Tutti i dettagli sono disponibili nel [changelog](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- È stata rilasciata la versione [1.13.0] di [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md?ref_type=heads), la libreria multipiattaforma C++ per client e server XMPP(https://invent.kde.org/libraries/qxmpp/-/tags/v1.13.0) è stata rilasciata. Tutti i dettagli sono disponibili nel [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- Sono state rilasciate le versioni [0.3.4](https://codeberg.org/slidge/slidge/releases/tag/v0.3.4) "speciale Natale" e [0.3.5](https://codeberg.org/slidge/slidge/releases/tag/v0.3.5) di [Slidge](https://slidge.im/). Queste versioni includono la conversione degli adesivi animati vettoriali in formato [lottie](https://lottiefiles.com/) in webp. [Slidgram](https://codeberg.org/slidge/slidgram/) e [slidcord](https://codeberg.org/slidge/slidcord/) effettuavano già tale conversione, ma ora viene eseguita tramite una dipendenza opzionale ("extra") di slidge: [rlottie-python](https://pypi.org/project/rlottie-python/), che semplifica il packaging/la distribuzione. E molte altre funzionalità, miglioramenti e correzioni di bug! È possibile consultare il [changelog](https://codeberg.org/slidge/slidge/releases/tag/v0.3.4) della versione o i changelog intermedi dalla [0.3.3 alla 0.3.5](https://codeberg.org/slidge/slidge/compare/v0.3.3...v0.3.5) per l'elenco completo delle modifiche.
  - [matridge](https://codeberg.org/slidge/matridge#readme), il gateway da [Matrix](https://matrix.org/) a XMPP basato su Slidge e [nio](https://matrix-nio.readthedocs.io/en/latest/), è stata rilasciata la versione [0.3.2](https://codeberg.org/slidge/matridge/releases/tag/v0.3.2).
  - [matteridge](https://codeberg.org/slidge/matteridge#readme), il gateway da [Mattermost](https://mattermost.com/) a XMPP basato su Slidge e [mattermost-api-reference-client](https://git.sr.ht/~nicoco/mattermost-api-reference-client), versione [0.3.2](https://codeberg.org/slidge/matteridge/releases/tag/v0.3.2) è stata rilasciata.
  - [slidcord](https://codeberg.org/slidge/slidcord#readme), il gateway da [Discord](https://discord.com/) a XMPP basato su Slidge e [discord.py-self](https://discordpy-self.readthedocs.io/en/latest/), versione [0.3.1](https://codeberg.org/slidge/slidcord/releases/tag/v0.3.1), è stato rilasciato.
  - [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp#readme), il gateway da [WhatsApp](https://www.whatsapp.com/) a XMPP basato su [Slidge](https://slidge.im/) e [whatsmeow](https://github.com/tulir/whatsmeow), versione [0.3.9](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.9) è stato rilasciato.
  - [slidgram](https://codeberg.org/slidge/slidgram#readme), il gateway da [Telegram](https://telegram.org/) a XMPP basato su Slidge e [Pyrofork](https://pyrofork.wulan17.dev/main/), versione [0.3.1](https://codeberg.org/slidge/slidgram/releases/tag/v0.3.1), è stato rilasciato.
- [xmpp-ap-bridge](https://github.com/Barbapulpe/xmpp-ap-bridge/blob/main/README.md), un'implementazione leggera da Fediverse a XMPP basata su bot client per consentire conversazioni simili a chat tra qualsiasi applicazione Fediverse e qualsiasi client XMPP, dalle normali applicazioni client, versioni [0.7.3](https://github.com/Barbapulpe/xmpp-ap-bridge/releases/tag/v0.7.3) e [0.7.4](https://github.com/Barbapulpe/xmpp-ap-bridge/releases/tag/v0.7.4).
- [xmpp-dns](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/README.md?ref_type=heads), uno strumento CLI per controllare i record SRV XMPP, versione [0.5.5](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.5.5). Tutti i dettagli sono disponibili nel [changelog](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/CHANGELOG.md?ref_type=heads).

## Estensioni e specifiche

La XMPP Standards Foundation sviluppa estensioni per XMPP nella sua [serie XEP](/extensions/) oltre alle [RFC XMPP](/rfcs/). Sviluppatori ed altri esperti di standard provenienti da tutto il mondo collaborano a queste estensioni, sviluppando nuove specifiche per pratiche emergenti e perfezionando i metodi esistenti. Proposte da chiunque, quelle di particolare successo finiscono per diventare definitive o attive, a seconda del loro tipo, mentre altre vengono accuratamente archiviate come differite. Questo ciclo di vita è descritto in [XEP-0001](/extensions/xep-0001.html), che contiene le definizioni formali e canoniche dei tipi, degli stati e dei processi. [Maggiori informazioni sul processo di standardizzazione](/about/standards-process.html). La comunicazione relativa agli standard e alle estensioni avviene nella [mailing list degli standard](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([archivio online](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposta

Il processo di sviluppo XEP inizia con la stesura di un'idea e la sua presentazione all'[XMPP Editor](/about/xsf/editor-team/). Entro due settimane, il [Consiglio](/about/xmpp-standards-foundation/#council) decide se accettare questa proposta come XEP sperimentale.

- [Pipelining dell'autenticazione iniziale](/extensions/inbox/iap.html)
  - Questa specifica definisce un protocollo per scoprire se il SASL2 `<authenticate>` può essere pipelinato in modo sicuro insieme allo stream aperto e, in tal caso, consente al client di eseguire questo pipelining in modo sicuro.

### Novità

- Versione 0.1.0 di [XEP-0508](/extensions/xep-0508.html) (Forum)
  - Accettato come sperimentale dal voto del consiglio (dg)
- Versione 0.1.0 di [XEP-0509](/extensions/xep-0509.html) (Pipelining dell'autenticazione iniziale)
  - Accettata come sperimentale con voto del consiglio (dg)

### Rinviato

Se un XEP sperimentale non viene aggiornato per più di dodici mesi, verrà spostato da Sperimentale a Rinviato. Se ci sarà un altro aggiornamento, lo XEP tornerà a Sperimentale.

- Nessun XEP rinviato questo mese.

### Aggiornato

- Versione 1.35.3 di [XEP-0045](/extensions/xep-0045.html) (Chat multiutente)
  - `muc#roomconfig_allowinvites` non limita i proprietari, ma abilita autorizzazioni aggiuntive per i membri. (spw)
- Versione 0.7.0 di [XEP-0353](/extensions/xep-0353.html) (Avvio di messaggi jingle)
  - Rimuovere la ridefinizione locale dell'elemento jingle `<reason/>` nello schema XML e fare riferimento a quello esistente.
  - Rendere facoltativo l'uso dell'elemento `<reason/>` nello schema, come specificato nel testo.
  - Aggiungere la definizione mancante del tipo "vuoto" nello schema XML. (lnj)

### Ultima chiamata

Le ultime chiamate vengono emesse quando tutti sembrano soddisfatti dello stato attuale dello XEP. Dopo che il [Consiglio](/about/xmpp-standards-foundation/#council) ha deciso se lo XEP sembra pronto, l'[XMPP Editor](/about/xsf/editor-team/) emette un'ultima chiamata per i commenti. Il feedback raccolto durante l'ultima chiamata può aiutare a migliorare lo XEP prima di restituirlo al Consiglio per il passaggio allo stato Stabile.

- [Ultima chiamata](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/thread/MNUPKCA2NR7ARCOU7MOQVQMTWFG77E3T/) per commenti su [XEP-0377](/extensions/xep-0377.html) (Segnalazione di spam)
  - Questa ultima chiamata inizia il 12-12-2025 e terminerà alla chiusura delle attività il 05-01-2026.

### Stabile

- Versione 1.0.0 di [XEP-0440](/extensions/xep-0440.html) (Funzionalità SASL Channel-Binding Type)
  - Accettata come stabile in base al voto del Consiglio del 18 novembre 2025 (XEP Editor (dg))

### Obsoleta

- Nessun XEP deprecato questo mese.

### Rifiutati

- Nessun XEP è stato rifiutato questo mese.

## Diffondi la notizia

Condividi la notizia su altri social network:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp-official.bsky.social)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Istanza Lemmy (non ufficiale)](https://slrpnk.net/c/xmpp)
- [Reddit (non ufficiale)](https://www.reddit.com/r/xmpp/)
- [Pagina Facebook XMPP (non ufficiale)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Dai un'occhiata anche al nostro [feed RSS](/feeds/all.atom.xml)!

Cerchi offerte di lavoro o desideri assumere un consulente professionista per il tuo progetto XMPP? Visita la nostra [bacheca dei lavori XMPP](https://xmpp.work/).

### Collaboratori e traduttori della newsletter

Questo è un progetto comunitario e desideriamo ringraziare i traduttori per il loro contributo. Volontari e altre lingue sono i benvenuti! Le traduzioni della newsletter XMPP saranno pubblicate qui (con un certo ritardo):

- Collaboratori:
  - A [questo numero](/categories/newsletter/): *emus, cal0pteryx, Gonzalo Raúl Nemmi, Adrien 'neox' Bourmault, Ludovic Bocquet, Benson Muite, Mario Sabatino, XSF iTeam*

- Traduzioni:
  - [Francese](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
  - [Tedesco](/categories/newsletter/): *Millesimus*
  - [Italiano](/categories/newsletter/): *Mario Sabatino, Roberto Resoli*
  - [Portoghese](/categories/newsletter/): *Paulo*
  
## Aiutaci a realizzare la newsletter

Questa newsletter XMPP è prodotta in collaborazione dalla comunità XMPP. Ogni numero mensile della newsletter viene redatto in questo [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Alla fine di ogni mese, il contenuto del pad viene inserito nel [repository GitHub dell'XSF](https://github.com/xsf/xmpp.org/milestone/3). Siamo sempre lieti di accogliere nuovi collaboratori. Non esitate a partecipare alla discussione nella nostra [chat di gruppo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) e ad aiutarci così a sostenere questo progetto come sforzo collettivo della comunità. Avete un progetto e volete diffondere la notizia? Considerate la possibilità di condividere qui le vostre notizie o i vostri eventi e promuoverli a un vasto pubblico.

Attività che svolgiamo regolarmente:

- raccolta di notizie nell'universo XMPP
- *brevi* sintesi di notizie ed eventi
- sintesi della comunicazione mensile sulle estensioni (XEP)
- revisione della bozza della newsletter
- preparazione delle immagini per i media
- traduzioni
- comunicazione tramite account dei media

## Annullare l'iscrizione alla newsletter XMPP

Per questa newsletter, [accedi qui](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/) e cancella l'iscrizione o invia semplicemente un'e-mail a newsletter-leave@xmpp.org.
(Se non hai mai effettuato l'accesso in precedenza, potrebbe essere necessario creare un account con l'indirizzo e-mail appropriato).

## Licenza

Questa newsletter è pubblicata con [licenza CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
