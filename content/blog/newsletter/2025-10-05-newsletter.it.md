---
title: Newsletter XMPP settembre 2025
date: 2025-10-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="Banner della newsletter XMPP" >}}

Benvenuti alla newsletter XMPP, è un piacere avervi di nuovo con noi!
Questo numero copre il mese di settembre 2025.

La [Newsletter XMPP](/categories/newsletter/) è offerta dal [Team di comunicazione XSF](/about/xsf/comm-team/).

Proprio come qualsiasi altro prodotto o progetto dell'XSF, la Newsletter è il risultato del lavoro volontario dei suoi membri e collaboratori. Se siete soddisfatti dei servizi e dei software che utilizzate, vi invitiamo a ringraziare o aiutare questi progetti!

Ti interessa contribuire al [Team di comunicazione XSF](/about/xsf/comm-team/)? Per saperne di più, leggi [in fondo alla pagina](#help-us-to-build-the-newsletter).

## Annunci XSF

### Adesione alla XSF

Se siete interessati ad aderire alla XMPP Standards Foundation come membri, [inviate la vostra candidatura entro il 23 novembre 2025, alle 00:00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q4_2025).

### Elezioni del consiglio di amministrazione e del comitato consultivo XSF 2025

La [XMPP Standards Foundation](/about/xmpp-standards-foundation/) sta cercando persone che entrino a far parte del [Consiglio di amministrazione](/about/xmpp-standards-foundation/#board) e membri che facciano parte del [Consiglio XMPP](/about/xmpp-standards-foundation/#council) per il periodo 2025/2026. Se siete interessati a candidarvi per il Consiglio di Amministrazione o il Consiglio XMPP, aggiungete una [pagina wiki](https://wiki.xmpp.org/web/Main_Page) sulla vostra candidatura in una o entrambe le sezioni sopra menzionate [entro il 2 novembre 2025, 00:00 UTC](https://wiki.xmpp.org/web/Board_and_Council_Elections_2025).

Partecipa alle decisioni dell'organizzazione XMPP Standards Foundation e alle specifiche che pubblichiamo!

**Nota**: i membri del Consiglio XMPP devono essere [membri eletti](/about/xsf/members/) della XSF; tuttavia, non vi è alcuna restrizione di questo tipo per il Consiglio di Amministrazione.

## Video e conferenze
- [XMPP Tutorials DE](https://makertube.net/c/xmpp_tutorials_de/videos) di [eversten.net](https://makertube.net/a/eversten.net/video-channels). 
  - [Conversazioni (XMPP) - Risolvere i problemi di connessione dopo l'aggiornamento](https://makertube.net/w/8yXjHWpVd77tz5vRySpJeH). [DE]
  - [Quicksy - Il modo più semplice per iniziare con XMPP (versione iOS)](https://makertube.net/w/7osSvECKBQvFPTYkjP9kz5). [DE]
- [UnifiedPush](https://gultsch.video/w/85UeGATR1i13E7j6eKzq2r): una [conferenza](https://talks.datenspuren.de/ds25/talk/3783DB/) di [Daniel Gultsch](https://gultsch.de/) al [Datenspuren 2025](https://www.datenspuren.de/2025/). [DE]

## Articoli XMPP

- [ProcessOne ](https://www.process-one.net/)
  - [Perché la proposta europea sul "controllo delle chat" danneggerà il settore delle comunicazioni europeo senza riuscire a proteggere i minori](https://www.process-one.net/blog/chat-control-2025/) di [Mickaël Rémond ](https://www.process-one.net/author/mremond/) per il [blog di ProcessOne](https://www.process-one.net/blog/).
- [Test di interoperabilità XMPP](https://xmpp-interop-testing.github.io/)
  - [Molte più opzioni!](https://xmpp-interop-testing.github.io/2025/09/14/lots-more-options.html): sono stati aggiunti numerosi nuovi sistemi CI. Questa volta l'obiettivo erano sistemi CI open source che rispettassero la libertà per i vostri progetti open source (tra cui [Jenkins](https://www.jenkins.io/), [Drone](https://www.drone.io/), [Harness](https://www.harness.io/) e [Woodpecker](https://woodpecker-ci.org/) ). Questo porta il numero totale di sistemi CI in cui è possibile eseguire test di interoperabilità XMPP a ben UNDICI, oltre a qualsiasi altro luogo in cui è possibile eseguire container. Se c'è un sistema CI che state utilizzando e vorreste vedere supportato, o se è già supportato ma avete difficoltà, [unitevi al loro MUC](xmpp:interop@conference.igniterealtime.org?join) o [apri una segnalazione su GitHub](https://github.com/XMPP-Interop-Testing/smack-sint-server-extensions). Di [Dan Caseley](https://xmpp-interop-testing.github.io/contact) per il [blog XMPP Interop Testing](https://xmpp-interop-testing.github.io/blog).
  - [Due nuove funzionalità per test più chiari](https://xmpp-interop-testing.github.io/2025/09/26/new-features-for-clearer-testing.html): è stata rilasciata la versione 1.7.1 di tutti i suoi test runner. Questa versione aggiunge due miglioramenti per rendere i test di interoperabilità più rigorosi e più facili da configurare! Ora è possibile configurare la suite in modo da considerare i test impossibili come falliti, assicurando che un risultato positivo significhi realmente che tutti i test configurati sono stati eseguiti e superati. Ora è possibile scegliere tra tre metodi di provisioning:
- Account amministratore che utilizza [XEP-0133](/extensions/xep-0133.html) (Amministrazione del servizio) per creare account di test.
- Account di test espliciti configurati in anticipo.
    - Registrazione in banda tramite [XEP-0077](/extensions/xep-0077.html) (Registrazione in banda).
Scegliete l'approccio più adatto alla vostra configurazione. È disponibile una [documentazione](https://xmpp-interop-testing.github.io/documentation/provisioning-accounts) che vi consentirà di esaminare i dettagli più specifici!
- [Suggerimenti CLI Libervia](https://mastodon.social/@Goffi/tagged/tips): sapevi che [Liverbia](https://libervia.org/) ha una [CLI](https://libervia.org/__b/doc/backend/libervia-cli/) che puoi usare per fare praticamente tutto? Ebbene sì, è proprio così, e [Goffi](https://mastodon.social/@Goffi), il suo autore, ha pubblicato una serie di tweet su Mastodon per aiutarti a sfruttarla al meglio! Condividi file, pubblica post sul blog, invia messaggi crittografati, effettua chiamate audio/video, crittografa un nodo pubsub, automatizza le attività con comandi ad hoc, ecc. Tutto comodamente dal tuo terminale!
- [FastCGI Authorizer](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/#fastcgi-authorizer-implementing-xep_0070-xmpp-confirmation) che implementa [XEP-0070](/extensions/xep-0070.html) (Verifica delle richieste HTTP tramite XMPP) Conferma XMPP da parte di [PulkoMandy](https://mastodon.tetaneutral.net/@pulkomandy) per i [repository Git pulkomandy.tk](https://pulkomandy.tk/gerrit/plugins/gitiles/?format=HTML). [[FR](https://linuxfr.org/users/pulkomandy/journaux/authentifiez-vous-sans-mot-de-passe-grace-a-xmpp-10-ans-plus-tard)]
- [Montando un WhatsApp gateway desde XMPP con Slidge](https://portal.mozz.us/gemini/z3r0.maverick-hq.org/gemlog/montando-un-whatsapp-gateway-desde-xmpp-con-slidge.gmi) di [z3r0](https://gts.maverick-hq.org/@z3r0) tramite [SMOLNET PORTAL](https://portal.mozz.us/about). [ES]
- [Messaggistica moderna: eseguire il proprio server XMPP](https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server/) di [Holger](https://hachyderm.io/@theaitch) per [codedge](https://www.codedge.de/).
- [Installare Slidgram in NetBSD](https://eugene-andrienko.com/it/2025/09/20/slidgram-netbsd-install-howto.html) di [Eugene](https://eugene-andrienko.com/about.html) per [Dragon's notes](https://eugene-andrienko.com/).
- XMPP Brasil [festeggia il suo primo anniversario](https://mastodon.social/@xmppbrasil/115232713992094928) fornendo account gratuiti alla comunità brasiliana e il suo nuovo status di [Category Provider A](https://providers.xmpp.net/provider/xmpp.eco.br/) da parte di [XMPP Providers](https://providers.xmpp.net/). [PT]

## Notizie sul software XMPP

### Client e applicazioni XMPP

- [Cheogram](https://cheogram.com/) ha rilasciato la versione [2.19.0-2](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.19.0-2) per Android. Si tratta di una versione di correzione dei bug che risolve i problemi relativi alla registrazione e alla scoperta (corregge le opzioni di blocco) sulle istanze [Snikket](https://snikket.org/), corregge ulteriori inserimenti sull'ultima versione di Android e lo scorrimento di "Gestisci account" con molti account, tra le altre cose. Assicurati di controllare il [changelog](https://git.sr.ht/~singpolyma/cheogram-android/tree/master/item/CHANGELOG.md) per tutti i dettagli.
- [Conversations](https://conversations.im/) ha rilasciato la versione [2.19.5](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.19.5) per Android, con **messaggi di errore migliorati per i server che non supportano TLS 1.3** e problemi risolti con la rotazione del dispositivo, oltre a molte altre [correzioni e miglioramenti](https://codeberg.org/iNPUTmice/Conversations/compare/2.19.4...2.19.5). È possibile consultare il [changelog](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) per tutti i dettagli.
- [Convo](https://git.disroot.org/badrihippo/convo) Il client XMPP per [KaiOS](https://www.kaiostech.com/) ha rilasciato la versione [0.2.0](https://git.disroot.org/badrihippo/convo/releases/tag/0.2.0) con nome in codice "Eyes Only" che supporta la crittografia end-to-end basata su OMEMO! È la prima volta che XMPP con OMEMO è disponibile su un telefono a tasti. Tutti gli annunci sono disponibili [nella pagina di rilascio](https://git.disroot.org/badrihippo/convo/releases/).

{{< figure src="/images/newsletter/2025-10-05/convo.png" caption="Convo 0.2.0: supporto per la crittografia end-to-end con OMEMO." >}}

- [Gajim](https://gajim.org/) ha rilasciato le versioni [2.3.5](https://gajim.org/posts/2025-09-11-gajim-2.3.5-released/) e [2.3.6](https://gajim.org/posts/2025-09-30-gajim-2.3.6-released/) della sua app di chat gratuita e completa per XMPP. Questa versione offre impostazioni dell'account riorganizzate, un nuovissimo gestore di scorciatoie, più informazioni sui contatti, anteprime video, miglioramenti delle prestazioni e molte correzioni di bug. L'ultimo aggiornamento risolve alcuni problemi relativi alle anteprime video e alla generazione delle anteprime, nonché alcuni problemi relativi al caricamento delle icone. È possibile consultare il [changelog](https://dev.gajim.org/gajim/gajim/-/blob/master/ChangeLog) per tutti i dettagli. Grazie per tutti i vostri contributi!

{{< figure src="/images/newsletter/2025-10-05/main-window.png" caption="Gajim 2.3.5 raggruppa le preferenze e le impostazioni dell'account!" >}}

- [Kaidan](https://www.kaidan.im/) ha rilasciato la versione [0.13.0](https://www.kaidan.im/2025/09/21/kaidan-0.13.0/) della sua app di chat moderna e intuitiva per XMPP. Questa nuova versione offre il supporto per l'utilizzo simultaneo di più account, l'attivazione/disattivazione degli account, l'inoltro dei messaggi, l'applicazione di criteri coerenti per la correzione di tutti i messaggi, l'archiviazione sicura delle password, la possibilità di provare tutti i provider in caso di errore di connessione durante la registrazione automatica e molte altre nuove funzionalità e correzioni di bug! È possibile trovare un elenco dettagliato delle nuove funzionalità, delle correzioni di bug e delle note nel [changelog](https://invent.kde.org/network/kaidan/-/blob/Kaidan/0.13/NEWS.md?ref_type=heads).

{{< figure src="/images/newsletter/2025-10-05/kaidan.png" caption="Kaidan 0.13.0: supporto multi-account con interruttore di attivazione/disattivazione." >}}

- [Monocles](https://monocles.eu/) ha rilasciato le versioni [2.0.14](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.14) e [2.0.15](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.15) del suo client di chat per Android. Questi aggiornamenti introducono la possibilità di fissare immagini e file nella parte superiore della finestra di chat, il supporto per gli URI geografici nei messaggi fissati e nelle anteprime delle risposte, l'anteprima video per i messaggi fissati e la visualizzazione dell'icona dei file audio per i messaggi audio fissati, oltre ad altri miglioramenti relativi al fissaggio. Consentono inoltre di rispondere a se stessi, inviare risposte con OMEMO e passare al messaggio toccando la risposta con il nuovo scorrimento per rispondere, oltre a molte altre funzionalità e numerose correzioni. Assicuratevi di dare un'occhiata al [changelog](https://codeberg.org/monocles/monocles_chat/src/branch/master/fastlane/metadata/android/en-US/changelogs/19101.txt) per tutti i dettagli!
- [Psi+](https://sourceforge.net/projects/psiplus/) ha rilasciato la versione [1.5.2117 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) del suo ramo di sviluppo di [Psi](https://sourceforge.net/projects/psi/), il client XMPP multipiattaforma progettato per utenti esperti.
- Il client XMPP [Renga](http://pulkomandy.tk/projects/renga) per [Haiku](https://www.haiku-os.org/) ha rilasciato la versione 1.28, con alcuni miglioramenti al supporto MUC e un'implementazione di [XEP-0070](/extensions/xep-0070.html) (Verifica delle richieste HTTP tramite XMPP) per l'autenticazione HTTP utilizzando XMPP. Potete leggere tutti i dettagli su questa versione nelle [ultime notizie](https://pulkomandy.tk/projects/renga#Latestnews) al riguardo.
- [xmpp-web](https://github.com/nioc/xmpp-web/blob/master/README.md) ha rilasciato la versione [0.10.7](https://github.com/nioc/xmpp-web/releases/tag/0.10.7) del suo client di chat web leggero per server XMPP.
- [XOWS](https://github.com/iquercorb/xows/blob/main/README.md) ha rilasciato la versione [0.9.9c](https://github.com/iquercorb/xows/releases/tag/0.9.9c) del suo client web XMPP Over WebSocket, con routine di recupero avatar rifattorizzate, alcune ottimizzazioni di aggiornamento DOM del browser, correzioni al crash del processo di registrazione dell'account e alla duplicazione degli occupanti MUC.

### Server XMPP

- La [comunità Ignite Realtime](https://www.igniterealtime.org/) è lieta di annunciare il rilascio di [Openfire 5.0.2](https://discourse.igniterealtime.org/t/openfire-5-0-2-release/95982)! Questa versione risolve una vulnerabilità di sicurezza recentemente identificata ([CVE-2025-59154](https://github.com/igniterealtime/Openfire/security/advisories/GHSA-w252-645g-87mp)). Il problema consentiva un potenziale spoofing dell'identità tramite l'analisi non sicura dell'attributo Common Name. Per ulteriori informazioni, leggere l'[avviso di sicurezza completo](https://github.com/igniterealtime/Openfire/security/advisories/GHSA-w252-645g-87mp). Questa versione migliora anche gli script basati su SystemD, rimuovendo alcuni fastidiosi inconvenienti introdotti in Openfire 5.0.1. Per ulteriori dettagli, consultare il [changelog completo](https://download.igniterealtime.org/openfire/docs/latest/changelog.html).

### Librerie e strumenti XMPP

- È stata rilasciata la versione [6.3.1](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/6.3.1) di [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/README.md?ref_type=heads). Tutti i dettagli sono disponibili nel [changelog](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog?ref_type=heads).
- È stata rilasciata la versione [1.11.2](https://invent.kde.org/libraries/qxmpp/-/tags/v1.11.2) di [QXmpp](https://invent.kde.org/libraries/qxmpp/-/blob/master/README.md?ref_type=heads). Tutti i dettagli sono disponibili nel [changelog](https://invent.kde.org/libraries/qxmpp/-/blob/master/CHANGELOG.md?ref_type=heads).
- Sono state rilasciate le versioni [0.3.0](https://codeberg.org/slidge/slidge/releases/tag/v0.3.0) e [0.3.1](https://codeberg.org/slidge/slidge/releases/tag/v0.3.1) di [Slidge](https://slidge.im/). **La migrazione dalla serie 0.2 non è supportata, la directory home di slidge deve essere eliminata e gli utenti devono registrarsi nuovamente**. Sono state introdotte nuove funzionalità e miglioramenti, principalmente: supporto per i fallback delle reazioni (opzionale) (per i client XMPP meno recenti che non supportano le reazioni), molte impostazioni a livello di gateway sono state spostate nelle impostazioni specifiche dell'utente, controlla il comando "preferenze" (ad hoc o in stile chatbot) e il supporto per i pronomi nelle VCards. È possibile consultare i log delle modifiche intermedie da [0.2.12 a 0.3.0](https://codeberg.org/slidge/slidge/compare/v0.2.12...v0.3.0) per l'elenco completo delle modifiche.
  - [slidge-whatsapp](https://codeberg.org/slidge/slidge-whatsapp#readme), il gateway da [WhatsApp](https://www.whatsapp.com/) a XMPP basato su Slidge e [whatsmeow](https://github.com/tulir/whatsmeow), sono state rilasciate le versioni [0.3.0beta](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.0beta) e [0.3.0](https://codeberg.org/slidge/slidge-whatsapp/releases/tag/v0.3.0).
  - [sleamdge](https://codeberg.org/slidge/sleamdge#readme), il gateway da [Steam](https://steamcommunity.com/) a XMPP basato su Slidge e [steamio](https://steam-py.github.io/docs/latest/), è stata rilasciata la versione [0.3.0](https://codeberg.org/slidge/sleamdge/releases/tag/v0.3.0).
  - [matteridge](https://codeberg.org/slidge/matteridge#readme), il gateway da [Mattermost](https://mattermost.com/) a XMPP basato su Slidge e [mattermost-api-reference-client](https://git.sr.ht/~nicoco/mattermost-api-reference-client), versione [0.3.0](https://codeberg.org/slidge/matteridge/releases/tag/v0.3.0) è stata rilasciata.
  - [slidcord](https://codeberg.org/slidge/slidcord#readme), il gateway da [Discord](https://discord.com/) a XMPP basato su Slidge e [discord.py-self](https://discordpy-self.readthedocs.io/en/latest/), versione [0.3.0](https://codeberg.org/slidge/slidcord/releases/tag/v0.3.0), è stato rilasciato.
  - [matridge](https://codeberg.org/slidge/matridge#readme), il gateway da [Matrix](https://matrix.org/) a XMPP basato su Slidge e [nio](https://matrix-nio.readthedocs.io/en/latest/), sono state rilasciate le versioni [0.3.0](https://codeberg.org/slidge/matridge/releases/tag/v0.3.0) e [0.3.1](https://codeberg.org/slidge/matridge/releases/tag/v0.3.1).
  - [slidgram](https://codeberg.org/slidge/slidgram#readme), il gateway da [Telegram](https://telegram.org/) a XMPP basato su Slidge e [Pyrofork](https://pyrofork.wulan17.dev/main/), versione [0.3.0](https://codeberg.org/slidge/slidgram/releases/tag/v0.3.0), è stato rilasciato.
- È stata rilasciata la versione [1.11.0](https://codeberg.org/poezio/slixmpp/releases/tag/slix-1.11.0) di [Slixmpp](https://codeberg.org/poezio/slixmpp). Per tutti i dettagli, è possibile consultare l'[annuncio ufficiale del rilascio](https://blog.mathieui.net/en/slixmpp-1.11.html).
- Sono state rilasciate le versioni [xmpp-dns](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/README.md?ref_type=heads) [0.5.2](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.5.2) e [0.5.3](https://salsa.debian.org/mdosch/xmpp-dns/-/releases/v0.5.3). Tutti i dettagli sono disponibili nel [changelog](https://salsa.debian.org/mdosch/xmpp-dns/-/blob/master/CHANGELOG.md?ref_type=heads).
- [xmpp-fastcgi-authorizer](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer), un FastCGI Authorizer che implementa [XEP-0070](/extensions/xep-0070.html) (Verifica delle richieste HTTP tramite XMPP) per consentire l'accesso ai siti web utilizzando un account XMPP, sono state rilasciate le versioni [0.1](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/+/refs/tags/v0.1) e [0.2](https://pulkomandy.tk/gerrit/plugins/gitiles/xmpp-fcgi-authorizer/+/refs/tags/v0.2) sono state rilasciate.

## Estensioni e specifiche

La XMPP Standards Foundation sviluppa estensioni per XMPP nella sua [serie XEP](/extensions/) oltre alle [RFC XMPP](/rfcs/). Sviluppatori ed altri esperti di standard provenienti da tutto il mondo collaborano a queste estensioni, sviluppando nuove specifiche per pratiche emergenti e perfezionando i metodi esistenti. Proposte da chiunque, quelle di particolare successo finiscono per diventare definitive o attive, a seconda del loro tipo, mentre altre vengono accuratamente archiviate come differite. Questo ciclo di vita è descritto in [XEP-0001](/extensions/xep-0001.html), che contiene le definizioni formali e canoniche dei tipi, degli stati e dei processi. [Maggiori informazioni sul processo di standardizzazione](/about/standards-process.html). La comunicazione relativa agli standard e alle estensioni avviene nella [mailing list degli standard](https://mail.jabber.org/postorius/lists/standards.xmpp.org/) ([archivio online](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/)).

### Proposta

Il processo di sviluppo XEP inizia con la stesura di un'idea e la sua presentazione all'[XMPP Editor](/about/xsf/editor-team/). Entro due settimane, il [Consiglio](/about/xmpp-standards-foundation/#council) decide se accettare questa proposta come XEP sperimentale.

- [Pubsub Node Bookmark](/extensions/inbox/pubsub-node-bookmark.html)
  - Questa specifica definisce un elemento segnalibro che punta a un nodo Pubsub.

### Novità

- Nessun nuovo XEP questo mese.

### Rinviati

Se un XEP sperimentale non viene aggiornato per più di dodici mesi, verrà spostato da Sperimentale a Rinviato. Se ci sarà un altro aggiornamento, lo XEP tornerà a Sperimentale.

- Nessun XEP rinviato questo mese.

### Aggiornato

- Versione 0.3.1 di [XEP-0317](/extensions/xep-0317.html) (Cappelli)
  - Errori di battitura, completamento di alcuni esempi e chiarimenti nei paragrafi grazie al feedback di badlop. (tj)
- Versione 0.2.0 di [XEP-0503](/extensions/xep-0503.html) (Spazi lato server)
  - Riscrittura utilizzando la semantica pubsub. (nc)

### Ultima chiamata

Le ultime chiamate vengono emesse quando tutti sembrano soddisfatti dello stato attuale dell'XEP. Dopo che il [Consiglio](/about/xmpp-standards-foundation/#council) ha deciso se l'XEP sembra pronto, l'[XMPP Editor](/about/xsf/editor-team/) emette un'ultima chiamata per i commenti. Il feedback raccolto durante l'ultima chiamata può aiutare a migliorare l'XEP prima di restituirlo al Consiglio per il passaggio allo stato Stabile.

- Nessuna ultima chiamata questo mese.

### Stabile

- Nessun XEP è stato spostato a Stabile questo mese.

### Obsoleto

- Nessun XEP è stato deprecato questo mese.

### Rifiutati

- Nessun XEP è stato rifiutato questo mese.

## Canali pubblici XMPP

Ogni giorno vengono creati nuovi room e canali pubblici sulla rete XMPP. Quindi, se sei alla ricerca di nuovi ed entusiasmanti canali pubblici a cui partecipare, assicurati di controllare il [Motore di ricerca dei canali pubblici](https://search.jabber.network/search) per trovare gruppi o comunità che condividono i tuoi interessi!

- Se desideri elencare tutti i canali, puoi trovarli [qui](https://search.jabber.network).
- Se sei interessato a qualcosa in particolare, [cerca per tag](https://search.jabber.network/tags/)!
- Se desideri elencare solo le stanze in una lingua particolare, aggiungi semplicemente `lang:xx` nella casella di ricerca, come in questo esempio per la [lingua spagnola](https://search.jabber.network/search?q=lang%3Aes&f=y&sinaddr=on&sindescr=on&sinname=on). Assicurati di sostituire `es` con la lingua desiderata (ad esempio `lang:fr`, `lang:de`, `lang:pt` e così via).

## Diffondi la notizia

Condividi la notizia su altri social network:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Movim](https://mov.im/community/news.xmpp.org/News)
- [Bluesky](https://bsky.app/profile/xmpp.org)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Istanza Lemmy (non ufficiale)](https://slrpnk.net/c/xmpp)
- [Reddit (non ufficiale)](https://www.reddit.com/r/xmpp/)
- [Pagina Facebook XMPP (non ufficiale)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Dai un'occhiata anche al nostro [feed RSS](/feeds/all.atom.xml)!

Cerchi offerte di lavoro o desideri assumere un consulente professionista per il tuo progetto XMPP? Visita la nostra [bacheca dei lavori XMPP](https://xmpp.work/).

### Sezione Collaboratori e traduzioni della newsletter:

Questo è un progetto comunitario e desideriamo ringraziare i traduttori per il loro contributo.
I volontari e altre lingue sono i benvenuti!
Le traduzioni della newsletter XMPP saranno pubblicate qui (con un certo ritardo):

Collaboratori alla newsletter di questo mese:
*emus, Badri Sunderarajan, cal0pteryx, Gonzalo Raúl Nemmi, Kris "poVoq", Ludovic Bocquet, XSF iTeam*

Collaboratori alla traduzione:
- [Francese](https://linuxfr.org/tags/xmpp/public): *Adrien Bourmault (neox), anubis, Benoît Sibaud, Julien Jorge seveso, Pierre Jarillon*
- [Tedesco](/categories/newsletter/): *Millesimus*
- [Italiano](/categories/newsletter/): *Mario Sabatino, Roberto Resoli*
  - Disponibile, da Giugno 2025, anche su: [XMPP-IT Italian Community](https://www.xmpp-it.net/tag/newsletter/)
- [Portoghese](/categories/newsletter/): *Paulo*

## Aiutaci a creare la newsletter

Questa newsletter XMPP è prodotta in collaborazione dalla comunità XMPP. Ogni numero mensile della newsletter viene redatto in questo [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Alla fine di ogni mese, il contenuto del pad viene inserito nel [repository GitHub dell'XSF](https://github.com/xsf/xmpp.org/milestone/3). Siamo sempre lieti di accogliere nuovi collaboratori. Non esitate a partecipare alla discussione nella nostra [chat di gruppo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) e ad aiutarci così a sostenere questo progetto come sforzo collettivo della comunità. Avete un progetto e volete diffondere la notizia? Considerate la possibilità di condividere qui le vostre notizie o i vostri eventi e promuoverli a un vasto pubblico.

Attività che svolgiamo regolarmente:

- raccolta di notizie nell'universo XMPP
- *brevi* sintesi di notizie ed eventi
- sintesi della comunicazione mensile sulle estensioni (XEP)
- revisione della bozza della newsletter
- preparazione delle immagini per i media
- traduzioni
- comunicazione tramite account dei media

## Progetti di hosting fiscale XSF

L'XSF offre [hosting fiscale](/community/fiscalhost/) per i progetti XMPP. Si prega di fare domanda tramite [Open Collective](https://opencollective.com/xmpp). Per ulteriori informazioni, consultare il [post sul blog dell'annuncio](/2021/09/the-xsf-as-a-fiscal-host/). Progetti attuali che è possibile sostenere:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav](https://opencollective.com/pravapp)
- [diasp.in](https://opencollective.com/diasp-in)

## Annullare l'iscrizione alla newsletter XMPP

Per annullare l'iscrizione a questa lista, [effettua prima il login](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/).
Se non hai mai effettuato il login, potrebbe essere necessario creare un account con l'indirizzo email appropriato.

## Licenza

Questa newsletter è pubblicata con [licenza CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
