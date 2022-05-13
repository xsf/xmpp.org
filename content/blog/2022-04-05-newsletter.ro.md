---
titlu: Buletinul informativ XMPP Martie 2022
autor: Echipa de comunicare XMPP și colaboratorii
data: 2022-04-05
categorii: ['Newsletter']
---

Bine ați venit la Buletinul informativ XMPP, ne bucurăm să vă avem din nou aici! Această ediție acoperă luna martie 2022.

La fel ca acest buletin informativ, multe proiecte și eforturile lor în comunitatea XMPP sunt rezultatul muncii voluntare a oamenilor. Dacă sunteți mulțumit de serviciile și software-ul pe care este posibil să le utilizați, mai ales în toată situația actuală, vă rugăm să luați în considerare posibilitatea de a mulțumi sau de a ajuta aceste proiecte! Sunteți interesați să sprijiniți echipa Newsletter? Citiți mai multe în partea de jos.

### Traduceri ale buletinului informativ

Acesta este un efort al comunității și dorim să mulțumim traducătorilor pentru contribuțiile lor. Voluntarii sunt bineveniți! Traducerile Buletinului informativ XMPP vor fi publicate aici (cu o oarecare întârziere):

- Franceză: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) și [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- Germană: [xmpp.org](https://xmpp.org/categories/newsletter/) și [anoxinon.de](https://anoxinon.de/blog/)
- Italiană: [nicfab.it](https://www.nicfab.it/)
- Spaniolă: [xmpp.org](https://xmpp.org/categories/newsletter/)

## Anunțuri XSF

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

- XSF a fost acceptată ca organizație gazdă la [Google Summer of Code 2022 (GSoC)](https://xmpp.org/community/gsoc-2022/). Dacă sunteți interesat să participați ca student, mentor sau ca proiect în general, vă rugăm să [adăugați ideile dvs. și să ne contactați](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022). Perioada de înscriere a contributorilor a început deja, așa că fiți rapizi!
- Buletinul XMPP prin poștă: Am migrat la [propriul nostru server de mail-list](https://mail.jabber.org/mailman/listinfo/newsletter) și am încetat să mai folosim Tinyletter. Este doar pentru citire și veți primi lunar buletinul informativ XMPP. De asemenea, se elimină problemele de confidențialitate cu Tinyletter.

## Proiecte de găzduire fiscală XSF

XSF oferă [găzduire fiscală](https://xmpp.org/community/fiscalhost/) pentru proiectele XMPP. Vă rugăm să aplicați prin intermediul [Open Collective](https://opencollective.com/xmpp). Pentru mai multe informații, consultați [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Proiecte actuale:

- [Bifrost bridge: Schimb de mesaje offline între Matrix și XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Evenimente

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): disponibil pe [canalul nostru YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): întâlnire lunară a entuziaștilor XMPP din Berlin, în fiecare a doua miercuri din lună.

## Articole

Dezvoltatorii Profanity au postat un ghid rapid despre cum se utilizează [OpenPGP pentru XMPP (OX)](https://profanity-im.github.io/blog/post/openpgp-for-xmpp-ox/).

[Buletinul informativ al JMP](https://blog.jmp.chat/b/march-newsletter-2022) anunță un nou client pentru Android (bazat pe Conversations) care se concentrează pe îmbunătățirea UX pentru utilizatorii de gateway-uri conforme cu standardele.

![Cheograma JMP](/images/newsletter/2022-03/cheograma-screenshot.png "Cheograma JMP")

Comunicatul [Mellium Dev Communiqué for March 2022](https://opencollective.com/mellium/updates/dev-communique-for-march-20222) a fost publicat! Această versiune include modificări la bara laterală din clientul TUI Communiqué și îmbunătățiri la diverse pachete din modulul principal mellium.im/xmpp.

## Noutăți în materie de software

### Clienți și aplicații

[Gajim development news](https://gajim.org/post/2022-03-24-development-news-march/): Luna martie aduce un nou sistem de raportare a problemelor și multe îmbunătățiri de performanță atât pentru Gajim, cât și pentru python-nbxmpp. Plugin-ul OMEMO al Gajim vine și el cu câteva îmbunătățiri. Nu în ultimul rând, a existat o problemă de securitate în python-nbxmpp, care a fost rezolvată în versiunea `2.0.6`.

Au fost lansate [Openfire Pàdé `1.5.7` și `1.6.3`](https://discourse.igniterealtime.org/t/openfire-pade-1-6-3-released/91536) și [Openfire Pàdé 1.6.2](https://discourse.igniterealtime.org/t/openfire-pade-1-6-2-released/91424).

A fost lansat [Profanity `0.12.0`](https://github.com/profanity-im/profanity/releases), cu înregistrare a contului în bandă și suport pentru starea de spirit a utilizatorului, temă nouă, experiență de utilizare OX îmbunătățită (așa cum arată articolul de mai sus) și o mulțime de corecturi și caracteristici îmbunătățite.

[Psi+ `1.5.1615` și Psi+ `1.5.1618`](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) au fost lansate.

[Conversații `2.10.5`](https://github.com/iNPUTmice/Conversations/blob/master/CHANGELOG.md) a fost lansat, aducând o reconectare mai bună a apelurilor după schimbarea rețelei, afișarea JID-ului apelantului și a JID-ului contului în ecranul apelurilor primite, adaptarea locațiilor de stocare a fișierelor conform noilor cerințe Android 11 și o corecție de securitate care afectează descărcările de fișiere. Rețineți că versiunea F-Droid rămâne în urmă, din cauza unor probleme care nu au legătură cu aceasta, dar `2.10.2.1` a fost lansată și include doar corecția de securitate. De asemenea, a fost anunțat faptul că de acum înainte conturile de pe conversations.im sunt gratuite.

## Servere

[Jackal `0.58.0`](https://github.com/ortuman/jackal/releases/tag/v0.58.0) a fost lansat și a adăugat tipul de depozit BoltDB.

După trei ani de dezvoltare [Prosody `0.12.0`](https://blog.prosody.im/prosody-0.12.0-released/) a fost lansat. Actualizarea acoperă conformitatea XMPP, optimizări pentru mobil și conectivitate, partajarea de fișiere HTTP actualizată, suport îmbunătățit pentru apeluri audio/video, Direct TLS și multe altele - felicitări! 

![Prosody](/images/newsletter/2022-03/grafana-screenshot.png "Prosody")

[Tigase #XMPP Server `8.2.0`](https://github.com/tigase/tigase-server/releases/tag/tigase-server-8.2.0) a fost lansat! Cea mai mare caracteristică este suportul pentru protocolul #MIX, care oferă o experiență mai bună de chat în grup, în special pe dispozitivele mobile. 
Chat-ul de grup (MUC) nu a fost lăsat să fie și a primit și el o mulțime de corecturi. În plus, am îmbunătățit conectivitatea server-la-server, am adăugat opțiunea de a stoca certificate în depozit (foarte util în implementările de tip cluster) și multe altele!

Comunitatea Ignite Realtime are plăcerea de a anunța disponibilitatea imediată a versiunii de întreținere `2.2.3` a [plugin-ului GoJara pentru Openfire]. GoJara oferă o implementare a [XEP-0321 "Remote Roster Management"](https://xmpp.org/extensions/xep-0321.html) și ajută la monitorizarea [Spectrum 2](https://spectrum.im/).

## Biblioteci

a fost lansată versiunea [`1.8.1`](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.8.1) a lui slixmpp, care rezolvă o problemă de compatibilitate cu biblioteca standard python din cauza introducerii defusedxml în versiunea `1.8.0`.

au fost lansate versiunile [`2.0.5` și `2.0.6`](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/nbxmpp_2.0/ChangeLog) de python-nbxmpp, care rezolvă o problemă de securitate în rezolvarea URI-urilor websocket.

Au fost lansate versiunile [Smack `4.4.5` și `4.5.0-alpha1`](https://discourse.igniterealtime.org/t/smack-4-4-5-and-4-5-0-alpha1-released/91437).

## Extensii și specificații

Dezvoltatorii și alți experți în standarde din întreaga lume colaborează la aceste extensii, dezvoltând noi specificații pentru practicile emergente și perfecționând modalitățile existente de a face lucrurile. Propuse de oricine, cele care au un succes deosebit ajung ca Final sau Active - în funcție de tipul lor - în timp ce altele sunt arhivate cu grijă ca Deferred. Acest ciclu de viață este descris în [XEP-0001](https://xmpp.org/extensions/xep-0001.html), care conține definițiile formale și canonice ale tipurilor, stărilor și proceselor. [Citiți mai multe despre procesul de elaborare a standardelor](https://xmpp.org/about/standards-process.html). Comunicarea în legătură cu standardele și extensiile are loc în [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([arhiva online](https://mail.jabber.org/pipermail/standards/)).

### Propus

Procesul de dezvoltare a XEP începe prin redactarea unei idei și trimiterea acesteia către editorul XMPP. În termen de două săptămâni, acesta decide dacă acceptă sau nu această propunere ca XEP experimental.

- Nu există niciun XEP propus în această lună.

### Nou

- Versiunea 0.1.0 a [XEP-0462](https://xmpp.org/extensions/xep-0462.html) (PubSub Type Filtering)
    - Acceptată prin votul Consiliului la 2022-02-09.

- Versiunea 0.1.0 a [XEP-0463](https://xmpp.org/extensions/xep-0463.html) (Versionarea afilierilor MUC)
    - Acceptată prin votul Consiliului din 2022-02-16.

### Deferit

În cazul în care un XEP experimental nu este actualizat timp de mai mult de douăsprezece luni, acesta va fi mutat din Experimental în Deferred. În cazul în care se efectuează o altă actualizare, XEP-ul va fi readus la Experimental.

- Nu există niciun XEP amânat în această lună.

### Actualizat

- Versiunea 1.6.0 a [XEP-0115](https://xmpp.org/extensions/xep-0115.html) (Entity Capabilities)
    - Menționarea explicită a atacurilor preimaginare (ssw)

- Versiunea 1.4.0 a [XEP-0156](https://xmpp.org/extensions/xep-0156.html) (Descoperirea metodelor alternative de conectare XMPP)
    - Eliminați metoda DNS `_xmppconnect` din cauza unei vulnerabilități de securitate. (tjb)

### Ultimul apel

Ultimele apeluri sunt emise după ce toată lumea pare mulțumită de starea actuală a XEP. După ce Consiliul decide dacă XEP pare pregătit, editorul XMPP emite un ultim apel pentru comentarii. Comentariile adunate în timpul ultimului apel ajută la îmbunătățirea XEP înainte de a-l retrimite Consiliului pentru avansarea la Stabil.

- Nu există niciun ultim apel în această lună.

### Stable (cunoscut anterior sub numele de Draft)

Info: XSF a decis să redenumească "Draft" în "Stable". [Citiți mai multe despre asta aici](https://github.com/xsf/xeps/pull/1100)

- Niciun XEP nu a avansat la Stable în această lună.

### Depreciat

- Niciun XEP depreciat în această lună.

### Obsoleted

- [XEP-0008](https://xmpp.org/extensions/xep-0008.html) (Avataruri bazate pe IQ)
    - Obsoleted datorită a două specificații care îl înlocuiesc (egp)

- [XEP-0038](https://xmpp.org/extensions/xep-0038.html) (Stiluri de pictograme)
    - Caducă din cauza omniprezenței emoji Unicode, precum și a autocolantelor Bits of Binary. (egp)

- [XEP-0051](https://xmpp.org/extensions/xep-0051.html) (Transfer de conexiuni)
    - Caducă deoarece această caracteristică a fost integrată în nucleul XMPP, a se vedea secțiunea 4.9.3.19 din RFC6120, care descrie eroarea de flux <see-other-host/>. (egp)

- [XEP-0138](https://xmpp.org/extensions/xep-0138.html) (Compresie flux)
    - Caducă din cauza unei vulnerabilități de securitate. (tjb)

- [XEP-0229](https://xmpp.org/extensions/xep-0229.html) (Compresie de flux cu LZW)
    - Caducă din cauza unei vulnerabilități de securitate. (tjb)

### Apel pentru experiență

Un apel la experiență - la fel ca un ultim apel, este un apel explicit la comentarii, dar în acest caz este adresat în principal persoanelor care au implementat și, în mod ideal, au implementat specificația. Consiliul votează apoi pentru a o trece la Final.

- Luna aceasta nu există niciun apel la experiență.

## Răspândiți vestea!

Vă rugăm să distribuiți știrile pe alte rețele:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

Aici vă puteți [subscribe via email](https://mail.jabber.org/mailman/listinfo/newsletter). Acesta este doar pentru citire și doar buletinul informativ vă va fi trimis lunar.

De asemenea, verificați [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Căutați oferte de muncă sau doriți să angajați un consultant profesionist pentru proiectul dumneavoastră XMPP? Vizitați [XMPP job board](https://xmpp.work/).

## Ajutați-ne să construim buletinul informativ

Acest buletin informativ XMPP este realizat în colaborare de către comunitatea XMPP. Prin urmare, dorim să mulțumim **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, MattJ, nicfab, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat, Ysabeau, Zash** pentru sprijinul și ajutorul acordat la creare, revizuire, traducere și implementare. Multe mulțumiri tuturor contribuitorilor și sprijinului lor continuu!

Numărul din fiecare lună al buletinului informativ este redactat în acest [simple pad](https://yopad.eu/p/xmpp-newsletter-365days). La sfârșitul fiecărei luni, conținutul pad-ului este îmbinat în [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). Suntem întotdeauna bucuroși să primim contribuitori. Nu ezitați să vă alăturați discuției în grupul nostru de chat [Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) și, astfel, să ne ajutați să susținem acest efort comunitar. Aveți un proiect și doriți să răspândiți vestea? Vă rugăm să luați în considerare posibilitatea de a vă împărtăși știrile sau evenimentele aici și de a le promova la un public larg.

Sarcini pe care le facem în mod regulat:

- colectarea de noutăți în universul XMPP
- *scurte* rezumate ale noutăților și evenimentelor
- rezumatul comunicării lunare privind extensiile (XEP)
- revizuirea proiectului de buletin informativ
- pregătirea imaginilor media
- traduceri

## Licență

Acest buletin informativ este publicat sub licența [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
