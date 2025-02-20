---
title: The XMPP Newsletter June 2024
date: 2024-07-06
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Benvenuti alla Newsletter XMPP, è un piacere avervi di nuovo qui! Questo numero copre il mese di giugno 2024.

# XMPP e Google Summer of Code 2024

L'XSF è stato accettato come [organizzazione ospitante alla GSoC del 2024](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024)! Questi progetti XMPP hanno ricevuto uno slot e hanno iniziato la loro attività di coding:

- [Monal](https://monal-im.org/)
    - [Modern Monal onboarding e Media gallery (175 ore, medio)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
        - [Blog post 1](https://thevaidik.medium.com/google-summer-of-code-gsoc-my-experience-1-xmpp-standards-foundation-da781ac95560)
- [Prav.app](https://prav.app/)
    - [Autenticazione basata su SMS OTP conforme agli standard (350 ore, medio)](https://wiki.xmpp.org/web/Gsoc2024/Prav.app/Standards_compliant_SMS_OTP_based_authentication)
        - [Blog post 1](https://write.as/assu/gsoc-and-open-source-my-first-steps-into-xmpp)

{{< figure src="/images/logos/gsoc2024_logo.svg" caption="XSF and Google Summer of Code 2024" >}}


# Progetti di hosting fiscale XSF

 

L'XSF offre [hosting fiscale](https://xmpp.org/community/fiscalhost/) per progetti XMPP. Fai domanda tramite [Open Collective](https://opencollective.com/xmpp). Per maggiori informazioni, vedi [l’annuncio sul blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Progetti in corso:

* [Mellium Co-op](https://opencollective.com/mellium)
* [Prav iOS](https://opencollective.com/prav-ios)


# Eventi XMPP

- [XMPP Track at FOSSY](https://2024.fossy.us/): 1-4 agosto 2024 - Università statale di Portland
- [XMPP Sprint a Berlino](https://wiki.xmpp.org/web/Sprints/2024-07_Berlin): Da venerdì 12 a domenica 14 luglio 2024.
- [Berlino XMPP Meetup](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup)\[DE / EN\]: Incontro mensile degli appassionati di XMPP a Berlino, ogni 2° mercoledì del mese.
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) \[IT\]: Incontro mensile di appassionati di XMPP a Berlino, ogni terzo lunedì del mese alle 19:00 ora locale (evento online, con modalità web meeting e live streaming).

# Video XMPP

- [Debian and XMPP in Wind and Solar Measurement](https://saimei.ftp.acc.umu.se/pub/debian-meetings/2024/MiniDebConf-Berlin/38-debian-and-xmpp-in-wind-and-solar-measurement.webm) intervento alla MiniDebConf di Berlino 2024.

# Articoli su XMPP

- [Understanding messaging protocols: XMPP and Matrix](https://www.process-one.net/blog/xmpp-matrix/)



# Notizie sul software

## Client e applicazioni



- Sono stati rilasciati [Psi+ 1.5.1947 through 1.5.2012 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) e [Psi+ 1.5.1979 through 1.5.2000 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/).
    
- Sono stati rilasciati [Gajim 1.9.0](https://gajim.org/post/2024-06-10-gajim-1.9.0-released/) e [1.9.1](https://gajim.org/post/2024-06-22-gajim-1.9.1-released/). A metà anno dall'ultimo rilascio, Gajim 1.9.0 è finalmente arrivato. Questa versione offre il tanto atteso supporto per le risposte ai messaggi e le reazioni ai messaggi. Anche la moderazione dei messaggi è stata migliorata. Salutate i messaggi vocali!

{{< figure src="/images/newsletter/2024-07-05/gajim-message-reactions.png" caption="Gajim message reactions" >}}


- È stato rilasciato [Monal 6.4.0](https://github.com/monal-im/Monal/releases/tag/Build_iOS_911) per iOS e macOS, con un elenco impressionante di miglioramenti. Monal stava anche conducendo una [campagna di raccolta fondi](https://monal-im.org/post/00012-funding-iphone13/).
    
- Sono stati rilasciati [Movim 0.25 “Nagata”](https://mov.im/node/pubsub.movim.eu/Movim/195d732f-a7b7-44ba-b0cc-caa68b6b4426) e [0.25.1 small bugfix](https://mov.im/node/pubsub.movim.eu/Movim/c0f66f93-9c2c-452c-97cc-bd36ebe19858).


## Server




- [Rilasciato Tigase XMPP Server 8.4.0](https://tigase.org/blog/tigase-xmpp-server-8.4.0/) - Le caratteristiche più rilevanti sono il supporto per il Portable Import/Export Format (XEP-0227), la possibilità di configurare gli utenti con dispositivi push per mostrarli come `away`, la possibilità di moderare i MUC e il supporto per xmppbl.org.
- [ejabberd 24.06: Rilascio di profondo lavoro!](https://www.process-one.net/blog/ejabberd-24-06/) - Con quattro mesi di lavoro, quasi 200 commit, tra cui diversi miglioramenti minori nel nucleo di ejabberd e molti miglioramenti nelle parti amministrative di ejabberd, come il WebAdmin e nuovi comandi API.
    
{{< figure src="/images/newsletter/2024-07-05/ejabberd-webadmin2.png" caption="ejabberd WebAdmin interface" >}}



## Librerie e Tool



- Sono stati rilasciati [nbxmpp 5.0.0](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/5.0.0) e [5.0.1](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/5.0.1), che portano il supporto per XEP-0490 (Sincronizzazione dei messaggi visualizzati), XEP-0317 (Cappelli), XEP-0424 (Ritrattamento dei messaggi) e aggiornano XEP-0425 (Moderazione dei messaggi) alla sua ultima versione.
- Comunità Ignite Realtime:
    - È stato rilasciato [Botz framework for Openfire 1.3.0](https://github.com/igniterealtime/Botz/releases/tag/v1.3.0). La libreria Botz aggiunge alla già ricca ed estensibile Openfire la possibilità di creare bot interni all'utente. In questa versione è stata risolta la compatibilità con Openfire 4.8.0 e successivi. Grazie a Sheldon Robinson per averci aiutato a risolvere il problema!
    - [Versione 1.11.0 del plugin Openfire restAPI](https://discourse.igniterealtime.org/t/openfire-restapi-plugin-version-1-11-0-release/94161)
- KaikOut: [Un bot di moderazione per la rete di comunicazione XMPP](https://git.xmpp-it.net/sch/Kaikout)


# Estensioni e specifiche



La XMPP Standards Foundation sviluppa estensioni di XMPP nella sua [serie XEP](https://xmpp.org/extensions/), oltre alle [RFC di XMPP](https://xmpp.org/rfcs/).

Sviluppatori e altri esperti di standard di tutto il mondo collaborano a queste estensioni, sviluppando nuove specifiche per le pratiche emergenti e perfezionando i modi di fare esistenti. Le estensioni proposte da chiunque, quelle di particolare successo finiscono per diventare Final o Active - a seconda del loro tipo - mentre altre vengono accuratamente archiviate come Deferred. Questo ciclo di vita è descritto in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), che contiene le definizioni formali e canoniche per i tipi, gli stati e i processi. [Per saperne di più sul processo degli standard](https://xmpp.org/about/standards-process.html). La comunicazione su standard ed estensioni avviene nella [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([archivio online](https://mail.jabber.org/pipermail/standards/)).


## Proposte



Il processo di sviluppo di un XEP inizia scrivendo un'idea e sottoponendola all'Editor XMPP. Entro due settimane, il Consiglio decide se accettare la proposta come XEP sperimentale.

- [Chat notification settings](https://xmpp.org/extensions/inbox/notification-filter.html)
    - Questo documento definisce un'estensione del protocollo XMPP per sincronizzare le impostazioni di notifica per chat tra diversi client.
- [WebXDC](https://xmpp.org/extensions/inbox/webxdc.html)
    - Questo documento definisce un'estensione del protocollo XMPP per comunicare i widget WebXDC e i loro aggiornamenti di stato.


## Nuove



- Version 0.1.0 of XEP-0491 (WebXDC)
    - Promoted to Experimental (XEP Editor: dg)


## Differimenti



Se uno XEP sperimentale non viene aggiornato per più di dodici mesi, verrà spostato da Experimental a Deferred. Se c'è un altro aggiornamento, lo XEP verrà rimesso su Experimental.

-   Nessuno XEP differito questo mese.

## Aggiornamenti



- Version 0.2.0 of XEP-0421 (Anonymous unique occupant identifiers for MUCs)
    -   Make explicit that one can’t just hash the real JID.
    -   Expand security considerations.
    -   Add schema.
    -   Fix some examples captions and casing (mw)
-   Version 1.1.1 of XEP-0153 (vCard-Based Avatars)
    -   XEP-0054 says “Email addresses MUST be contained in a `<USERID>` element”. (egp)
-   Version 1.2.2 of XEP-0107 (User Mood)
    -   Fixed typo (XEP Editor (dg))


## Last Call



Last Call sono emesse una volta che tutti sembrano soddisfatti dello stato attuale del XEP. Dopo che il Consiglio decide se lo XEP sembra pronto, l'XMPP Editor emette una Last Call per i commenti. Il feedback raccolto durante la Last Call aiuta a migliorare lo XEP prima di riportarlo al Consiglio per l'avanzamento a Stable.

- Nessuna last call questo mese.

## Stabile



- Nessun XEP è passato a Stabile questo mese.

## Deprecato



- Nessuno XEP deprecato questo mese.

## Non ammessi



- Nessun XEP non ammesso questo mese.


# Diffondete la notizia!



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


# Collaboratori della newsletter e traduzioni

Si tratta di uno sforzo comunitario e vorremmo ringraziare i traduttori per il loro contributo. I volontari sono i benvenuti! Le traduzioni della newsletter XMPP saranno pubblicate qui (con un certo ritardo):

-   Inglese (originale): [xmpp.org](https://xmpp.org/categories/newsletter/)
    -   General contributors: _Adrien Bourmault (neox), Alexander “PapaTutuWawa”, Arne, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris “poVoq”, Licaon\_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, singpolyma, XSF iTeam_
-   Francese: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) e [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
    -   Traduttori: _Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau_
-   Italiano: [notes.nicfab.eu](https://notes.nicfab.eu/)
    -   Traduttori: _nicola_
-   Spagnolo: [xmpp.org](https://xmpp.org/categories/newsletter/])
    -   Traduttori: _Gonzalo Raúl Nemmi_


# Aiutaci a realizzare la newsletter



Questa newsletter XMPP è prodotta in collaborazione dalla comunità XMPP. Il numero di ogni mese della newsletter viene redatto in questo [semplice pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Alla fine di ogni mese, il contenuto del blocco viene inserito nel [repository XSF Github](https://github.com/xsf/xmpp.org/milestone/3). Siamo sempre felici di accogliere i collaboratori. Non esitate a partecipare alla discussione nella [chat del gruppo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) e ad aiutarci così a sostenere questo sforzo della comunità. Avete un progetto e volete diffondere la notizia? Considerate la possibilità di condividere qui le vostre notizie o i vostri eventi e di promuoverli a un vasto pubblico.

Attività che facciamo regolarmente:

- raccogliere notizie nell'universo XMPP
- _brevi_ riassunti di notizie ed eventi
- riassunto della comunicazione mensile sulle estensioni (XEP)
- revisione della bozza della newsletter
- preparazione delle immagini dei media
- traduzioni
- comunicazione attraverso gli account social

# Cancellazione dalla newsletter XMPP

Per annullare l'iscrizione a questa lista, [effettuare prima il login](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/). Se in precedenza non si è effettuato il login, potrebbe essere necessario creare un account con un idoneo indirizzo e-mail.

# Licenza

Questa newsletter è pubblicata sotto [licenza CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).

