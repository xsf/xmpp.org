---
title: The XMPP Newsletter July 2024
date: 2024-08-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Benvenuti alla Newsletter XMPP, è un piacere avervi di nuovo qui! Questo numero copre il mese di luglio 2024.


## Annunci XSF

Se sei interessato a diventare membro della XMPP Standards Foundation, [fai domanda entro il 18 agosto 2024!](https://wiki.xmpp.org/web/Membership_Applications_Q3_2024)


### XMPP e Google Summer of Code 2024

L'XSF è stato accettato come [organizzazione ospitante della GSoC nel 2024](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024)! Questi progetti XMPP hanno ricevuto uno slot e hanno iniziato la loro attività di coding:

- [Monal](https://monal-im.org/)
    - [Modern Monal onboarding e Media gallery (175 ore, medio)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
        - [Post del blog 1](https://thevaidik.medium.com/google-summer-of-code-gsoc-my-experience-1-xmpp-standards-foundation-da781ac95560)
        - [Post del blog 2](https://thevaidik.medium.com/google-summer-of-code-gsoc-my-experience-2-midterm-evaluations-xmpp-standards-foundation-3be8b27dc653)
- [Prav.app](https://prav.app/)
    - INFO: Purtroppo la valutazione intermedia non è stata superata e il progetto è stato interrotto.
    - [Autenticazione basata su SMS OTP conforme agli standard (350 ore, medio)](https://wiki.xmpp.org/web/Gsoc2024/Prav.app/Standards_compliant_SMS_OTP_based_authentication)
        - [Post sul blog 1](https://write.as/assu/gsoc-and-open-source-my-first-steps-into-xmpp)

{{< figure src="/images/logos/gsoc2024_logo.svg" caption="XSF and Google Summer of Code 2024" >}}


### Progetti di hosting fiscale XSF 

L'XSF offre [hosting fiscale](https://xmpp.org/community/fiscalhost/) per progetti XMPP. Fai domanda tramite [Open Collective](https://opencollective.com/xmpp). Per maggiori informazioni, vedi [l’annuncio sul blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Progetti in corso:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav iOS](https://opencollective.com/prav-ios)
- [diasp.in](https://opencollective.com/diasp-in)

## Eventi XMPP

- [XMPP Sprint a Worcester, UK](https://wiki.xmpp.org/web/Sprints/2024-09_Worcester_UK): 21-22 settembre 2024 - The Hive, Worcester
- [XMPP Track at FOSSY](https://2024.fossy.us/): 1-4 agosto 2024 - Portland State University
- [Berlino XMPP Meetup](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) \[DE / EN\]: Incontro mensile degli appassionati di XMPP a Berlino, ogni secondo mercoledì del mese.
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) \[IT\]: Incontro mensile di appassionati di XMPP a Berlino, ogni terzo lunedì del mese alle 19:00 ora locale (evento online, con modalità web meeting e live streaming).

## Articoli su XMPP

-   [Rivista](https://git.xmpp-it.net/sch/Rivista) è un nuovo sistema di pubblicazione che crea un sito dinamico a partire da nodi XMPP PubSub; Rivista è compatibile con i lettori di notizie Atom/RSS e con i browser HTML.
-   [Un blogpost di Haiku-OS sull'XMPP Sprint di Berlino del 20 luglio 2024](https://www.haiku-os.org/blog/nephele/2024-07-21_xmpp_coding_sprint_berlin). [Trovate anche l'elenco dei progetti dello Sprint XMPP di luglio a Berlino](https://wiki.xmpp.org/web/Sprints/2024-07\_Berlin#Attendees) sui quali si è lavorato!
-   [JMP.chat: Calls from SIP and a potential new SIM plan](https://blog.jmp.chat/b/july-newsletter-2024)
-   [ProcessOne: Breaking Down the Costs of Large Messaging Services](https://www.process-one.net/blog/breaking-down-the-costs-of-large-messaging-services/)

## Notizie sul software XMPP

### Client e applicazioni XMPP

- È stato rilasciato [Rivista 0.1](https://git.xmpp-it.net/sch/Rivista).
- È stato rilasciato [Psi+ 1.5.2033 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/).
- Sono stati rilasciati [Psi+ 1.5.2029 - 1.5 2038 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/).
- È stato rilasciato [Gajim 1.9.2](https://gajim.org/post/2024-07-19-gajim-1.9.2-released/) con un'importante correzione della crittografia OMEMO, notifiche native su Windows e miglioramenti all'usabilità. È stato inoltre rilasciato [Gajim 1.9.3](https://gajim.org/post/2024-07-29-gajim-1.9.3-released/), che risolve un problema con il programma di installazione di MS Store e apporta alcuni miglioramenti.
- È stato rilasciato [Monal 6.4.1](https://github.com/monal-im/Monal/releases/tag/Build_iOS_941) con alcune correzioni e traduzioni aggiornate. ATTENZIONE, questa è l'ultima release che supporterà macOS 11 + 12 e l'ultima release che supporterà iOS 14 + 15. Inoltre, [Monal IM](https://monal-im.org/) è stato selezionato in [un'altra tornata di finanziamenti](https://nlnet.nl/project/Monal-IM-UI/) dalla [NGI dell'UE](https://ngi.eu) tramite il [NLnet Foundation NGI0 Entrust Fund](https://nlnet.nl/entrust/) per lavorare su alcune importanti funzionalità. In particolare: Implementare il Dialpad, riscrivere l'interfaccia utente della chat, implementare le reazioni ai messaggi, le risposte ricche e gli adesivi, lavorare su XSF e documentare gli interni di Monal. Per saperne di più è possibile consultare il post [Monal IM Blog](https://monal-im.org/post/00013-nlnet-funding2/).
- È stato rilasciato [Movim 0.26](https://github.com/movim/movim/releases/tag/v0.26). Presenta Emoji personalizzate, supporto Codeblock nei messaggi, migliore gestione dei messaggi di spam, aggiornamento della moderazione e della ritrattazione dei messaggi e anche alcune correzioni di bug. [Movim](https://movim.eu/) è inoltre lieta di annunciare di essere stata selezionata dalla [NLnet Foundation](https://nlnet.nl/) per ricevere fondi attraverso il [NGI0 Core](https://nlnet.nl/core/) per lavorare su una [vasta serie di interessanti funzionalità](https://mov.im/node/pubsub.movim.eu/Movim/f619c49c-ccd3-4487-8c2e-20b6d3555da2) relative alle [videoconferenze](https://nlnet.nl/project/Movim-E2EE-video/) sulla piattaforma, comprese le chiamate audio e video uno-a-molti. Prossimamente verranno pubblicati alcuni post più specifici e tecnici sul blog.
    
{{< figure src="/images/newsletter/2024-08-05/movim-0.26.png" caption="Movim 0.26 with custom emojis" >}}

### Server XMPP

- Sono stati rilasciati [openfire 4.8.2](https://discourse.igniterealtime.org/t/openfire-4-8-2-release/94171) e [4.8.3](https://discourse.igniterealtime.org/t/openfire-4-8-3-release/94194).
- È stato rilasciato [ejabberd 24.07](https://www.process-one.net/blog/ejabberd-24-07/).
    - Pubblicazione di uno script ejabberd [extauth per il flusso di concessione della password OIDC](https://codeberg.org/Natureshadow/ejabberd-extauth-oidc-password)    


### Librerie e Tool

- Sono stati rilasciati [nbxmpp 5.0.2](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/5.0.2) e [5.0.3](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/5.0.3).
- Sono stati rilasciati [QXmpp 1.7.1](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.7.1) (con supporto migliorato per [OMEMO](https://xmpp.org/extensions/xep-0384.html)) e [1.8.0](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.8.0) (con supporto per [SRV records](https://xmpp.org/extensions/xep-0368.html), [Bind 2](https://xmpp.org/extensions/xep-0386.html), [FAST](https://xmpp.org/extensions/xep-0484.html), [XMPP URIs](https://xmpp.org/extensions/xep-0147.html) e migrazione di account su un altro server).

## Estensioni e specifiche

La XMPP Standards Foundation sviluppa estensioni di XMPP nella sua [serie XEP](https://xmpp.org/extensions/), oltre alle [RFC di XMPP](https://xmpp.org/rfcs/).

Sviluppatori e altri esperti di standard di tutto il mondo collaborano a queste estensioni, sviluppando nuove specifiche per le pratiche emergenti e perfezionando i modi di fare esistenti. Le estensioni proposte da chiunque, quelle di particolare successo finiscono per diventare Final o Active - a seconda del loro tipo - mentre altre vengono accuratamente archiviate come Deferred. Questo ciclo di vita è descritto in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), che contiene le definizioni formali e canoniche per i tipi, gli stati e i processi. [Per saperne di più sul processo degli standard](https://xmpp.org/about/standards-process.html). La comunicazione su standard ed estensioni avviene nella [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([archivio online](https://mail.jabber.org/pipermail/standards/)).


### Proposte

Il processo di sviluppo di un XEP inizia scrivendo un'idea e sottoponendola all'Editor XMPP. Entro due settimane, il Consiglio decide se accettare la proposta come XEP sperimentale.

- Nessuno XEP proposto questo mese.

### Nuove

- Version 0.1.0 of XEP-0492 (Chat notification settings)
    - Promoted to Experimental (XEP Editor: dg)

### Differimenti

Se uno XEP sperimentale non viene aggiornato per più di dodici mesi, verrà spostato da Experimental a Deferred. Se c'è un altro aggiornamento, lo XEP verrà rimesso su Experimental.

-   Nessuno XEP differito questo mese.

### Aggiornamenti

-   Version 0.1.1 of XEP-0484 (Fast Authentication Streamlining Tokens)
    -   Link to latest draft version (09) of the HT SASL mechanism. (lnj)
-   Version 0.2.0 of XEP-0484 (Fast Authentication Streamlining Tokens)
    -   Added an XML Schema.
    -   Fixed text where ‘count’ was assumed to be an element, not an attribute.
    -   Fixed indentation in a few examples. (egp)
-   Version 0.4.2 of XEP-0440 (SASL Channel-Binding Type Capability)
    -   Add an XML schema.
    -   Mention that this specification does add a new namespace that should go to the registrar.
    -   Fix indentation, typos, misuse of `''` vs. `</>` for elements, etc. (egp)
-   Version 0.1.2 of XEP-0491 (WebXDC)
    -   Suggest what to use for selfAddr
    -   Add acknowledgements (spw)

### Last Call

Last Call sono emesse una volta che tutti sembrano soddisfatti dello stato attuale del XEP. Dopo che il Consiglio decide se lo XEP sembra pronto, l'XMPP Editor emette una Last Call per i commenti. Il feedback raccolto durante la Last Call aiuta a migliorare lo XEP prima di riportarlo al Consiglio per l'avanzamento a Stable.

- Nessuna last call questo mese.

### Stabile

- Nessun XEP è passato a Stabile questo mese.

### Deprecato

- Nessuno XEP deprecato questo mese.

### Non ammessi

- Nessun XEP non ammesso questo mese.

## Diffondete la notizia!

Condividete la notizia sui "social network":

-   [Mastodon](https://fosstodon.org/@xmpp/)
-   [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
-   [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
-   [Istanza di Lemmy (non ufficiale)](https://slrpnk.net/c/xmpp)
-   [Reddit (non ufficiale)](https://www.reddit.com/r/xmpp/)
-   [Pagina Facebook XMPP (non ufficiale)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Controlla anche il nostro [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Cerchi offerte di lavoro o vuoi assumere un consulente professionale per il tuo progetto XMPP? Visita la nostra [bacheca delle offerte di lavoro XMPP](https://xmpp.work/).


### Collaboratori della newsletter e traduzioni

Si tratta di uno sforzo comunitario e vorremmo ringraziare i traduttori per il loro contributo. I volontari sono i benvenuti! Le traduzioni della newsletter XMPP saranno pubblicate qui (con un certo ritardo):

-   Inglese (originale): [xmpp.org](https://xmpp.org/categories/newsletter/)
    -   General contributors: _Adrien Bourmault (neox), Alexander “PapaTutuWawa”, Arne, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris “poVoq”, Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Schimon Zachary, Simone Canaletti, singpolyma, XSF iTeam_
-   Francese: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) e [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
    -   Traduttori: _Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau_
-   Italiano: [notes.nicfab.eu](https://notes.nicfab.eu/)
    -   Traduttori: _nicola_
-   Spagnolo: [xmpp.org](https://xmpp.org/categories/newsletter/)
    -   Traduttori: _Gonzalo Raúl Nemmi_


## Aiutaci a realizzare la newsletter

Questa newsletter XMPP è prodotta in collaborazione dalla comunità XMPP. Il numero di ogni mese della newsletter viene redatto in questo [semplice pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Alla fine di ogni mese, il contenuto del blocco viene inserito nel [repository XSF Github](https://github.com/xsf/xmpp.org/milestone/3). Siamo sempre felici di accogliere i collaboratori. Non esitate a partecipare alla discussione nella [chat del gruppo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) e ad aiutarci così a sostenere questo sforzo della comunità. Avete un progetto e volete diffondere la notizia? Considerate la possibilità di condividere qui le vostre notizie o i vostri eventi e di promuoverli a un vasto pubblico.

Attività che facciamo regolarmente:

- raccogliere notizie nell'universo XMPP
- _brevi_ riassunti di notizie ed eventi
- riassunto della comunicazione mensile sulle estensioni (XEP)
- revisione della bozza della newsletter
- preparazione delle immagini dei media
- traduzioni
- comunicazione attraverso gli account social


## Cancellazione dalla newsletter XMPP

Per annullare l'iscrizione a questa lista, [effettuare prima il login](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/). Se in precedenza non si è effettuato il login, potrebbe essere necessario creare un account con un idoneo indirizzo e-mail.

## Licenza

Questa newsletter è pubblicata sotto [licenza CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
