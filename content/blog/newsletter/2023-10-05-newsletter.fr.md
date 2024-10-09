---
title: Lettre d'information XMPP de septembre 2023
date: 2023-10-05
categories: ['Newsletter']
---



Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre le mois de septembre 2023.

Un grand merci à toutes les personnes qui nous lisent et à toutes les contributrices et tous les contributeurs !



Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite [en bas de page](#aidez-nous-à-créer-la-lettre-dinformation).




### XMPP et le Google Summer of Code 2023



La XSF a été [acceptée à nouveau comme organisation hôte du GSoC 2023 et a reçu deux places pour les contributeurices XMPP] (https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/) !


Pour Dino :

- [Prise en charge de Windows pour Dino](https://hrxi.github.io/gsoc/blog/windows-support-for-dino)
- [Les malheurs de Windows](https://hrxi.github.io/gsoc/blog/windows-woes)


Pour Moxxy :

- Le [premier article de blog](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), détaillant le plan de mise en œuvre d'une fonctionnalité de base de discussion de groupe.
- Le [deuxième article de blog](https://moxxy.org/posts/2023-06-17-XEP-0045-In-Moxxmpp.html), décrivant les plans pour apporter une implémentation de base de la [XEP-0045](https://xmpp.org/extensions/xep-0045.html) dans la bibliothèque XMPP de Moxxy, moxxmpp.
- Le [troisième article de blog](https://moxxy.org/posts/2023-07-24-Join-MUC-With-Moxxy.html), esquissant le plan d'implémentation du frontend.
- Le [quatrième article de blog](https://moxxy.org/posts/2023-08-20-Moxxy-MUC-GSoC-Final-Report.html), concluant sur le support MUC de Moxxy.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}




### Hébergement fiscal de projets par la XSF



La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Veuillez postuler via [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets actuellement hébergés :



- [Coopérative Mellium](https://opencollective.com/mellium)




## Événements XMPP



- [Permanence XMPP](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)

- [Rencontres XMPP à Berlin (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les deuxièmes mercredis du mois.

- [XMPP Italian happy hour](https://tube.nicfab.eu/c/xmpp) : réunion mensuelle XMPP italienne sur le web, à partir du 16 mai et ensuite tous les troisièmes mardis du mois à 19h00 (événement en ligne, avec mode réunion web et streaming en direct).

- [TroLUG XMPP Workshop](http://trolug.de/termine.html) : le TroLUG organise le deuxième atelier sur XMPP en langue allemande le 2023-09-07. Il se déroulera sous forme de conférence audio via BBB. Toutes les personnes intéressées sont invitées à participer à l'atelier.

- L'administrateur de l'organisation GSoC participera cette année au sommet des mentors de Google à Sunnyvale !


## Vidéos



Il y a eu tout un fil rouge sur XMPP au [FOSSY2023] (https://2023.fossy.us/schedule/) avec de nombreux exposés :

- [XMPP Connectivity & Security](https://archive.org/details/fossy2023_XMPP_Connectivity__Security) est une introduction aux XEPs de connectivité XMPP comme XEP-0368 (Direct TLS), XEP-0467 (QUIC), XEP-0468 (WebSocket S2s) et les aspects internes de xmpp-proxy, un proxy forward+reverse, et d'autres.

- [XMPP Introduction and Overview](https://archive.org/details/fossy2023_XMPP_Introduction_and_Overview) est un bref historique et une introduction au protocole XMPP pour les personnes ayant peu d'expérience en programmation.

- [My XMPP Past, Present, and Future](https://archive.org/details/fossy2023_My_XMPP_Past_Present_and_Futur) est un point de vue sur l'évolution de l'écosystème XMPP depuis 2004. Il explique comment il a été affecté par des événements majeurs tels que le déclin des services de messagerie instantanée traditionnels, le début de l'ère des smartphones et des nouveaux services de chat, et plus encore.

- [Building open standards-based ecosystems] (https://archive.org/details/fossy2023_Building_open_standardsbased_e) est un exposé sur la façon dont XMPP, en tant que communauté et protocole, s'est adapté au changement, et sur le rôle que la XSF a joué dans sa continuité, mais aussi une discussion générale sur la durabilité des écosystèmes ouverts et des réseaux ouverts.

## Articles

- [JMP Newsletter : Summer in Review](https://blog.jmp.chat/blog/view/blog.jmp.chat/@/id/septermber-newsletter-2023). JMP vous permet d'envoyer et de recevoir des messages textes et images (et des appels) par l'intermédiaire d'un véritable numéro de téléphone depuis votre ordinateur, votre tablette, votre téléphone ou tout autre appareil doté d'un client Jabber.  JMP présente notamment les caractéristiques suivantes : votre numéro de téléphone sur chaque appareil ; plusieurs numéros de téléphone, une seule application, libre comme dans "liberté" [et pas gratuit, NDT], partager un numéro avec plusieurs personnes.

- [État du Snikket 2023 : financement] (https://snikket.org/blog/snikket-2023-funding/). Ce billet de la série couvre les aspects financiers du projet.


## Nouvelles des logiciels

### Clients et applications


- [Moxxy 0.5.0](https://codeberg.org/moxxy/moxxy/releases/tag/v0.5.0) est disponible. Cette version apporte des améliorations au niveau des notifications, de la sélection des images et des traductions. Le travail initial sur les groupchats a été commencé, grâce au Google Summer of Code 2023.



{{< figure src="/images/newsletter/2023-10-05/moxxy-muc-demo.gif" caption="Moxxy Group Chat (MUC) Demo" >}}




### Serveurs


- [Prosody 0.12.4](https://blog.prosody.im/prosody-0.12.4-released/) a été publiée.




### Bibliothèques et outils


- [XMPP Account Exporter](https://migrate.modernxmpp.org/) a reçu une mise à jour qui apporte de nombreuses améliorations de la présentation et la prise en charge de l'exportation des signets.

- [Script d'authentification ejabberd pour Lemmy](https://f-hub.org/Solarpunk/ejabberd-auth-lemmy), pour apporter un chat sécurisé aux utilisateurs de votre [alternative fédérée à Reddit](https://join-lemmy.org/). Ceci étend une collection d'[intégrations du Fédivers sur JoinJabber.org](https://joinjabber.org/tutorials/integration/).





## Extensions et spécifications



La XMPP Standards Foundation développe des extensions XMPP dans sa [série de XEPs](https://xmpp.org/extensions/) en plus des [RFCs XMPP](https://xmpp.org/rfcs/).



Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent _finales_ ou _actives_ – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’_ajournées_. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).




### Extensions proposées



Le processus de développement d'une XEP commence par la rédaction d'une idée et sa soumission à l'Éditeur XMPP. Dans les deux semaines qui suivent, le Conseil décide d'accepter ou non cette proposition en tant que XEP _expérimentale_.



- Pas de XEP proposée ce mois-ci.




### Nouvelles extensions



- Pas de nouvelle XEP ce mois-ci.




### Extensions ajournées



Si une XEP _expérimentale_ n'est pas mise à jour pendant plus de douze mois, elle sera déplacée d'_expérimentale_ à _ajournée_. Si une nouvelle mise à jour est effectuée, la XEP redeviendra _expérimentale_.



- Aucune XEP ajournée ce mois-ci.




### Extensions mises-à-jour


- Pas de XEP mises à jour ce mois-ci.



### Dernier appel



Les _derniers appels_ sont lancés une fois que tout le monde semble satisfait de l'état actuel d'une XEP. Une fois que le Conseil a décidé que la XEP semblait prête, l'Éditeur XMPP lance un _dernier appel_ pour recueillir des commentaires. Les commentaires recueillis lors du _dernier appel_ peuvent permettre d'améliorer la XEP avant de la renvoyer au Conseil pour qu'il la passe à l'état _stable_.



- Pas de dernier appel ce mois-ci.




### Extensions stables



- Aucune XEP n’est passée à stable ce mois-ci.




### Extensions dépréciées



- Aucune XEP déclarée dépréciée ce mois-ci.




## Spread the news



N'hésitez pas à partager les nouvelles sur d'autres réseaux :



- [Mastodon](https://fosstodon.org/@xmpp/)

- [Twitter](https://twitter.com/xmpp)

- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)

- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

- [Lemmy instance (unofficial)](https://slrpnk.net/c/xmpp)

- [Reddit (unofficial)](https://www.reddit.com/r/xmpp/)



{{< newsletter-subscribe >}}



Consultez également notre [Flux RSS] (https://xmpp.org/feeds/all.atom.xml) !



Vous recherchez des offres d'emploi ou souhaitez engager une consultante ou un consultant pour votre projet XMPP ? Visitez notre [XMPP job board](https://xmpp.work/).




### Nouvelles extensionssletter Contributors & Translations



Il s’agit d’un effort communautaire, et nous aimerions remercier les traducteurs et traductrices pour leurs contributions. Les volontaires sont les bienvenus ! Les traductions de la lettre d’information XMPP seront publiées ici (avec un certain retard) :



- anglais (original) : [xmpp.org](https://xmpp.org/categories/newsletter/)

  - contributeurs généraux : **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), nicola, XSF iTeam**

- français : [jabberfr.org](https://news.jabberfr.org/category/newsletter/) et [linuxfr.org](https://linuxfr.org/tags/xmpp/public)

  - traduction : **Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau**

- allemand : [xmpp.org](https://xmpp.org/categories/newsletter/) et [anoxinon.de](https://anoxinon.de/blog/)

  - traduction : **Jeybe, wh0nix**

- italien : [notes.nicfab.eu](https://notes.nicfab.eu)

  - traduction : **nicola**

- espagnol : [xmpp.org](https://xmpp.org/categories/newsletter/)

  - traduction : **daimonduff, TheCoffeMaker**




## Aidez-nous à créer la lettre d’information



Cette lettre d’information XMPP est produite collaborativement par la communauté XMPP. La lettre d’information de chaque mois est rédigé dans ce [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). À la fin de chaque mois, le contenu du pad est fusionné dans le [dépôt Github de la XSF](https://github.com/xsf/xmpp.org/milestone/3). Nous sommes toujours heureux d’accueillir des contributeurs et contributrices. N’hésitez pas à vous joindre à la discussion dans notre [salon public Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) et ainsi nous aider à soutenir cet effort communautaire. Vous avez un projet et vous voulez en parler ? Pensez à partager vos nouvelles ou vos événements ici, et à les promouvoir auprès d’un large public.



Tâches que nous effectuons régulièrement :

- rassembler les nouvelles dans l'univers XMPP

- brefs résumés de nouvelles et d'événements

- résumé de la communication mensuelle sur les extensions (XEP)

- révision du projet de bulletin d'information

- préparation d'images pour les médias

- traductions

- communication via les comptes médias


## Licence



Cette lettre d’information est publiée sous la licence [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
