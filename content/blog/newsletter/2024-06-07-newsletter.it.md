Benvenuti alla Newsletter XMPP, è un piacere avervi di nuovo qui! Questo numero copre il mese di maggio 2024.

# XMPP e Google Summer of Code 2024

L'XSF è stato accettato come [organizzazione ospitante alla GSoC del 2024](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024)! Questi progetti XMPP hanno ricevuto uno slot e inizieranno ora il coding:

- [Monal](https://monal-im.org/)
    - [Modern Monal onboarding e Media gallery (175 ore, medio)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
- [Prav.app](https://prav.app/)
    - [Standards compliant SMS OTP based authentication (350 ore, medio)](https://wiki.xmpp.org/web/Gsoc2024/Prav.app/Standards_compliant_SMS_OTP_based_authentication)

<center>
<figure>
  <img src="/images/xmpp/2024/04-2024/gsoc2024_logo.svg">
  <figcaption>XSF e Google Summer of Code 2024</figcaption>
</figure>
</center>


# Progetti di hosting fiscale XSF

*** 

L'XSF offre [hosting fiscale](https://xmpp.org/community/fiscalhost/) per progetti XMPP. Fai domanda tramite [Open Collective](https://opencollective.com/xmpp). Per maggiori informazioni, vedi [l’annuncio sul blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Progetti in corso:

* [Mellium Co-op](https://opencollective.com/mellium)
* [Prav iOS](https://opencollective.com/prav-ios)


# Eventi XMPP

- [XMPP Track at FOSSY](https://2024.fossy.us/): L'invito a presentare proposte scade il 14 giugno!
- [XMPP Sprint a Berlino](https://wiki.xmpp.org/web/Sprints/2024-07_Berlin): Da venerdì 12 a domenica 14 luglio 2024.
- [Berlino XMPP Meetup](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup)\[DE / EN\]: Incontro mensile degli appassionati di XMPP a Berlino, ogni 2° mercoledì del mese.
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) \[IT\]: Incontro mensile di appassionati di XMPP a Berlino, ogni terzo lunedì del mese alle 19:00 ora locale (evento online, con modalità web meeting e live streaming).

# Video XMPP

- [Debian and XMPP in Wind and Solar Measurement](https://saimei.ftp.acc.umu.se/pub/debian-meetings/2024/MiniDebConf-Berlin/38-debian-and-xmpp-in-wind-and-solar-measurement.webm) intervento alla MiniDebConf di Berlino 2024.

# Articoli su XMPP

- Nella [JMP Newsletter](http://blog.jmp.chat/b/may-newsletter-2024) si parla dei nuovi percorsi SMS in arrivo, di una futura opzione di gateway da XMPP a RCS e della release Cheogram Android 2.15.3-1.
- Aaron P. MacSween [ha annunciato l'evoluzione di webxdc](https://cryptography.dog/blog/announcing-webxdc-evolve/). Oltre ad altre cose, è stato anche effettuato il porting al [servizio Cheogram] basato su XMPP (https://cheogram.com/).


# Notizie sul software

## Client e applicazioni

***

- Sono stati rilasciati [Psi+ 1.5.1947 through 1.5.2012 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) e [Psi+ 1.5.1979 through 1.5.2000 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/).
    

- È stato rilasciato [Psi+ 1.5.1844 through 1.5 1930 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/).
- È stato rilasciato [Psi+ 1.5.1834 through 1.5 1937 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/).



## Server

***

- [Scaling up with MongooseIM 6.2.1](https://xmpp.org/2024/05/scaling-up-with-mongooseim-6.2.1/).
- XMPP Web è un webclient di terze parti disponibile come [plugin per Openfire](https://discourse.igniterealtime.org/t/new-openfire-plugin-xmpp-web/93982)!


<center>
<figure>
  <img src="/images/xmpp/2024/05-2024/openfire_xmpp_web.png">
  <figcaption>XMPP Web as Openfire plugin</figcaption>
</figure>
</center>


## Librerie e Tool

***

- [Annuncio pubblico iniziale di Slixfeed News Bot](https://slixfeed.woodpeckersnest.space/posts/slixfeed-news-bot/).

<center>
<figure>
  <img src="/images/xmpp/2024/05-2024/slixfeed.png">
  <figcaption>Slixfeed News Bot</figcaption>
</figure>
</center>

- Sono state rilasciate le versioni di QXmpp [1.6.1](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.6.1) (con supporto fisso per le chat di gruppo OMEMO) e [1.7.0](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.7.0) (con [MIX](https://xmpp.org/extensions/xep-0369.html), [SASL2](https://xmpp.org/extensions/xep-0388.html) e [SFS](https://xmpp.org/extensions/xep-0447.html) aggiornato per la compatibilità con i protocolli distribuiti).
- [go-xmpp 0.2.1](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.1).
- [go-sendxmpp 0.11.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.11.0).


# Estensioni e specifiche

***

La XMPP Standards Foundation sviluppa estensioni di XMPP nella sua [serie XEP](https://xmpp.org/extensions/), oltre alle [RFC di XMPP](https://xmpp.org/rfcs/).

Sviluppatori e altri esperti di standard di tutto il mondo collaborano a queste estensioni, sviluppando nuove specifiche per le pratiche emergenti e perfezionando i modi di fare esistenti. Le estensioni proposte da chiunque, quelle di particolare successo finiscono per diventare Final o Active - a seconda del loro tipo - mentre altre vengono accuratamente archiviate come Deferred. Questo ciclo di vita è descritto in [XEP-0001] (https://xmpp.org/extensions/xep-0001.html), che contiene le definizioni formali e canoniche per i tipi, gli stati e i processi. [Per saperne di più sul processo degli standard](https://xmpp.org/about/standards-process.html). La comunicazione su standard ed estensioni avviene nella [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([archivio online](https://mail.jabber.org/pipermail/standards/)).


## Proposte

***

Il processo di sviluppo di un XEP inizia scrivendo un'idea e sottoponendola all'Editor XMPP. Entro due settimane, il Consiglio decide se accettare la proposta come XEP sperimentale.

- Nessuna proposta questo mese.

## Nuove

***

- Nessun nuovo XEP questo mese.

## Differimenti

***

Se uno XEP sperimentale non viene aggiornato per più di dodici mesi, verrà spostato da Experimental a Deferred. Se c'è un altro aggiornamento, lo XEP verrà rimesso su Experimental.

-   Nessuno XEP differito questo mese.

## Aggiornamenti

***

- Version 2.5.0 of XEP-0030 (Service Discovery)
    - Add note about some entities not advertising the feature. (pep)
- Version 1.34.6 of XEP-0045 (Multi-User Chat)
    - Remove contradicting keyword on sending subject in §7.2.2. (pep)


## Last Call

***

Last Call sono emesse una volta che tutti sembrano soddisfatti dello stato attuale del XEP. Dopo che il Consiglio decide se lo XEP sembra pronto, l'XMPP Editor emette una Last Call per i commenti. Il feedback raccolto durante la Last Call aiuta a migliorare lo XEP prima di riportarlo al Consiglio per l'avanzamento a Stable.

-   XEP-0421: Anonymous unique occupant identifiers for MUCs
-   XEP-0440: SASL Channel-Binding Type Capability

## Stabile

***

- Version 1.0.0 of XEP-0398 (User Avatar to vCard-Based Avatars Conversion)
    - Accept as Stable as per Council Vote from 2024-04-30. (XEP Editor (dg))


## Deprecato

***

- Nessuno XEP deprecato questo mese.

## Non ammessi

***

- Nessun XEP non ammesso questo mese.


# Diffondete la notizia!

***

Condividete la notizia sui "social network":

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Twitter](https://twitter.com/xmpp)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [Istanza di Lemmy (non ufficiale)](https://slrpnk.net/c/xmpp)
- [Reddit (non ufficiale)](https://www.reddit.com/r/xmpp/)
- [Pagina Facebook XMPP (non ufficiale)](https://www.facebook.com/jabber)


<br>

<center>
    
<div id="rectangle" style="padding: 5px; border: 2px solid blue; border-radius: 10px;">
<font size="+2"><strong>Iscriviti alla newsletter mensile XMPP</strong></font>
<style>
    button {
            color: #ffffff;
            background-color: #2d63c8;
            font-size: 25px;
            border: 1px solid #2d63c8;
            border-radius: 10px;
            padding: 6px 25px;
            cursor: pointer
              }
    button:hover {
            color: #2d63c8;
            background-color: #ffffff;
                }
</style>
<body>
<p><p><p><a href="https://mail.jabber.org/mailman/listinfo/newsletter"><button type="button" name="myButton">Iscriviti</button>
</body>
</a></p></p></p></body></div></center>

<br>
<br>


Controlla anche il nostro [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Cerchi offerte di lavoro o vuoi assumere un consulente professionale per il tuo progetto XMPP? Visita la nostra [bacheca delle offerte di lavoro XMPP](https://xmpp.work/).


# Collaboratori della newsletter e traduzioni

Si tratta di uno sforzo comunitario e vorremmo ringraziare i traduttori per il loro contributo. I volontari sono i benvenuti! Le traduzioni della newsletter XMPP saranno pubblicate qui (con un certo ritardo):

- Inglese (originale): [xmpp.org](https://xmpp.org/categories/newsletter/)
    - General contributors: _Adrien Bourmault (neox), Alexander “PapaTutuWawa”, Arne, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris “poVoq”, Licaon\_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, singpolyma, XSF iTeam_
- Francese: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) e [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
    - Traduttori: _Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau_
- Italiano: [notes.nicfab.eu](https://notes.nicfab.eu/)
    - Traduttori: _nicola_
- Spagnolo: 
    - Traduttori: _Gonzalo Raúl Nemmi_


# Aiutaci a realizzare la newsletter

***

Questa newsletter XMPP è prodotta in collaborazione dalla comunità XMPP. Il numero di ogni mese della newsletter viene redatto in questo [semplice pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Alla fine di ogni mese, il contenuto del blocco viene inserito nel [repository XSF Github](https://github.com/xsf/xmpp.org/milestone/3). Siamo sempre felici di accogliere i collaboratori. Non esitate a partecipare alla discussione nella [chat del gruppo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) e ad aiutarci così a sostenere questo sforzo della comunità. Avete un progetto e volete diffondere la notizia? Considerate la possibilità di condividere qui le vostre notizie o i vostri eventi e di promuoverli a un vasto pubblico.

Attività che facciamo regolarmente:

- raccogliere notizie nell'universo XMPP
- _brevi_ riassunti di notizie ed eventi
- riassunto della comunicazione mensile sulle estensioni (XEP)
- revisione della bozza della newsletter
- preparazione delle immagini dei media
- traduzioni
- comunicazione attraverso gli account social

# Licenza

***

Questa newsletter è pubblicata sotto [licenza CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).





