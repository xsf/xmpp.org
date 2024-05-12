Benvenuti alla Newsletter XMPP, è un piacere avervi di nuovo qui! Questo numero copre il mese di aprile 2024.

# Annunci XSF

***

Se siete interessati a far parte della XMPP Standards Foundation come membri, [candidatevi fino al 19 maggio 2024!](https://wiki.xmpp.org/web/Membership_Applications_Q2_2024).

# XMPP e Google Summer of Code 2024

***

L'XSF è stato accettato come [organizzazione ospitante della GSoC nel 2024](https://wiki.xmpp.org/web/Google_Summer_of_Code_2024)! Questi progetti XMPP hanno ricevuto uno slot e sono ora nella fase di creazione della comunità:


*   [Monal](https://monal-im.org/)
    *   [Media Gallery (90 hours, easy)](https://wiki.xmpp.org/web/Gsoc2024/Monal/Media_Gallery)
*   [Prav.app](https://prav.app/)
    *   [Standards compliant SMS OTP based authentication (350 hours, medium)](https://wiki.xmpp.org/web/Gsoc2024/Prav.app/Standards_compliant_SMS_OTP_based_authentication)


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

***

* [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2024-07_Berlin): Da venerdì 12 a domenica 14 luglio 2024.
* [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) \[IT\]: incontro mensile sul web XMPP italiano, ogni terzo lunedì del mese alle 19:00 ora locale (evento online, con modalità web meeting e live streaming).


# Articoli

***

* Monal:
    * [Applicazione iOS bandita dall'Appstore cinese](https://monal-im.org/post/00010-ios-banned/)
    * [Controllo parziale della sicurezza per il client iOS di Monal](https://monal-im.org/post/00011-security-audit-1/): Radically Open Security (ROS) ha eseguito un controllo di sicurezza su alcune parti di Monal.
* L'app Snikket per Android è temporaneamente [non disponibile nel Google Play Store](https://snikket.org/blog/snikket-google-play-removal) (problema già risolto).


# Notizie sul software

## Client e applicazioni

***

* È stato rilasciato [Monal 6.3.0](https://github.com/monal-im/Monal/releases/tag/Build_iOS_900), che porta il supporto per [XEP-0425: Moderated Message Retraction](https://xmpp.org/extensions/xep-0425.html) e [XEP-0490: Message Displayed Synchronization](https://xmpp.org/extensions/xep-0490.html).
* Sono stati rilasciati [Movim 0.24 "#Mueller"](https://mov.im/node/pubsub.movim.eu/Movim/007843a5-5a44-4710-86a1-70ad7e18bd84) e un [0.24.1 bugfix](https://mov.im/node/pubsub.movim.eu/Movim/d71c1b3a-d36a-4eb4-a6fb-ff245123348f).
* Sono stati rilasciati [Psi+ 1.5.1747 - 1.5.1816 installer](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) e [Psi+ 1.5.1768 - 1.5.1819 portable](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/). Ora con Qt6 invece di Qt5.


## Server

***

* È stato rilasciato [MongooseIM 6.2.1](https://github.com/esl/MongooseIM/releases/tag/6.2.1). È ora supportata la versione 1.1.0 di [XEP-0313 Message Archive Management](https://xmpp.org/extensions/xep-0313.html). Il backend di archiviazione in-memory CETS migliorato consente di distribuire, gestire e scalare facilmente l'installazione di MongooseIM nel cloud senza l'onere di volumi persistenti.
* [I documenti di ejabberd ora usano MkDocs](https://www.process-one.net/blog/ejabberd-docs-now-using-mkdocs/)


## Librerie e Tool

***

* È stato rilasciato [Smack 4.4.8](https://discourse.igniterealtime.org/t/smack-4-4-8-released/93807).
* [Slidge v0.1.0](https://sr.ht/~nicoco/slidge/) Slidge è una libreria gateway XMPP (puppeteer) in python. Rende la scrittura di gateway per altre reti di chat (legacy modules) il più semplice possibile.
* [go-xmpp 0.2.0](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.0).
* [go-sendxmpp 0.10.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.10.0).


# Estensioni e specifiche

***

La XMPP Standards Foundation sviluppa estensioni di XMPP nella sua [serie XEP](https://xmpp.org/extensions/), oltre alle [RFC di XMPP](https://xmpp.org/rfcs/).

Sviluppatori e altri esperti di standard di tutto il mondo collaborano a queste estensioni, sviluppando nuove specifiche per le pratiche emergenti e perfezionando i modi di fare esistenti. Le estensioni proposte da chiunque, quelle di particolare successo finiscono per diventare Final o Active - a seconda del loro tipo - mentre altre vengono accuratamente archiviate come Deferred. Questo ciclo di vita è descritto in [XEP-0001] (https://xmpp.org/extensions/xep-0001.html), che contiene le definizioni formali e canoniche per i tipi, gli stati e i processi. [Per saperne di più sul processo degli standard](https://xmpp.org/about/standards-process.html). La comunicazione su standard ed estensioni avviene nella [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([archivio online](https://mail.jabber.org/pipermail/standards/)).


## Proposte

***

Il processo di sviluppo di un XEP inizia scrivendo un'idea e sottoponendola all'Editor XMPP. Entro due settimane, il Consiglio decide se accettare la proposta come XEP sperimentale.

- Questo mese non è stata proposta alcuno XEP.

## Nuove

***

- Nessun nuovo XEP questo mese.

## Differimenti

***

Se uno XEP sperimentale non viene aggiornato per più di dodici mesi, verrà spostato da Experimental a Deferred. Se c'è un altro aggiornamento, lo XEP verrà rimesso su Experimental.

*   Nessuno XEP differito questo mese.

## Aggiornamenti

***

*   Version 0.7.0 of XEP-0333 (Displayed Markers)
    *   Change title to “Displayed Markers”
    *   Bring back Service Discovery feature (dg)
*   Version 0.4.1 of XEP-0440 (SASL Channel-Binding Type Capability)
    *   Recommend the usage of tls-exporter over tls-server-end-point (fs)
*   Version 0.2.1 of XEP-0444 (Message Reactions)
    *   fix grammar and spelling (wb)
*   Version 1.0.1 of XEP-0388 (Extensible SASL Profile)
    *   Fixed typos (md)

## Last Call

***

Last Call sono emesse una volta che tutti sembrano soddisfatti dello stato attuale del XEP. Dopo che il Consiglio decide se lo XEP sembra pronto, l'XMPP Editor emette una Last Call per i commenti. Il feedback raccolto durante la Last Call aiuta a migliorare lo XEP prima di riportarlo al Consiglio per l'avanzamento a Stable.

*   XEP-0398: User Avatar to vCard-Based Avatars Conversion

## Stabile

***

*   Version 1.0.0 of XEP-0386 (Bind 2)
    *   Accept as Stable as per Council Vote from 2024-04-02. (XEP Editor (dg))
*   Version 1.0.0 of XEP-0388 (Extensible SASL Profile)
    *   Accept as Stable as per Council Vote from 2024-04-02. (XEP Editor (dg))
*   Version 1.0.0 of XEP-0333 (Displayed Markers)
    *   Accept as Stable as per Council Vote from 2024-04-17. (XEP Editor (dg))
*   Version 1.0.0 of XEP-0334 (Message Processing Hints)
    *   Accept as Stable as per Council Vote from 2024-04-17 (XEP Editor (dg))


## Deprecato

***

* Nessuno XEP deprecato questo mese.

## Rifiutato

***

* XEP-0360: Nonzas (non sono Stanzas)


# Diffondete la notizia!

***

Condividete la notizia sui "social network":

* [Mastodon](https://fosstodon.org/@xmpp/)
* [Twitter](https://twitter.com/xmpp)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Istanza di Lemmy (non ufficiale)](https://slrpnk.net/c/xmpp)
* [Reddit (non ufficiale)](https://www.reddit.com/r/xmpp/)
* [Pagina Facebook XMPP (non ufficiale)](https://www.facebook.com/jabber)

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

-   Inglese (originale): [xmpp.org](https://xmpp.org/categories/newsletter/)
    -   General contributors: **Adrien Bourmault (neox), Alexander “PapaTutuWawa”, Arne, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris “poVoq”, Licaon\_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Simone Canaletti, XSF iTeam**
-   Francese: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) e [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
    -   Traduttori: **Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
-   Italiano: [notes.nicfab.eu](https://notes.nicfab.eu/)
    -   Traduttori: **nicola**


# Aiutaci a realizzare la newsletter

***

Questa newsletter XMPP è prodotta in collaborazione dalla comunità XMPP. Il numero di ogni mese della newsletter viene redatto in questo [semplice pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Alla fine di ogni mese, il contenuto del blocco viene inserito nel [repository XSF Github](https://github.com/xsf/xmpp.org/milestone/3). Siamo sempre felici di accogliere i collaboratori. Non esitate a partecipare alla discussione nella [chat del gruppo Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) e ad aiutarci così a sostenere questo sforzo della comunità. Avete un progetto e volete diffondere la notizia? Considerate la possibilità di condividere qui le vostre notizie o i vostri eventi e di promuoverli a un vasto pubblico.

Attività che facciamo regolarmente:

* raccogliere notizie nell'universo XMPP
* *brevi* riassunti di notizie ed eventi
* riassunto della comunicazione mensile sulle estensioni (XEP)
* revisione della bozza della newsletter
* preparazione delle immagini dei media
* traduzioni
* comunicazione attraverso gli account social

# Licenza

***

Questa newsletter è pubblicata sotto [licenza CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).





