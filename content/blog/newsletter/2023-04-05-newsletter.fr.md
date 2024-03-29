---
title: Lettre d'information XMPP de mars 2023
date: 2023-04-05
categories: ['Newsletter']
---

Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre le mois de mars 2023. Un grand merci à toutes les personnes qui nous lisent et à toutes les contributrices et tous les contributeurs !

Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite [en bas de page](#aidez-nous-à-créer-la-lettre-dinformation).

## Annonces de la XSF

xmpp.org dispose d'une nouvelle section logiciels ! Vous recherchez des logiciels XMPP, c’est-à-dire des clients, des serveurs, des bibliothèques, des composants et des outils ? Consultez la nouvelle [section logiciels](https://xmpp.org/software/) de [xmpp.org](https://xmpp.org/), qui vous permet de filtrer les logiciels selon vos propres critères. Vous recherchez un client fonctionnant sous Android et prenant en charge les appels audio/vidéo ? Vous recherchez une bibliothèque qui prend en charge la [XEP-0461 : Message Replies](https://xmpp.org/extensions/xep-0461.html) ? Appliquez simplement le filtre et voyez ce que vous obtenez !

{{< figure src="/images/newsletter/2023-03-05/xmpp-software-section.png" caption="La nouvelle section logiciels de xmpp.org" >}}

- Si vous souhaitez devenir [membre de la XSF](https://xmpp.org/community/membership/), vous pouvez [soumettre votre candidature au cours de ce trimestre jusqu'au 21 mai 2023 à 00h00 UTC](https://wiki.xmpp.org/web/Membership_Applications_Q2_2023).

### XMPP et le Google Summer of Code 2023

La XSF a été [acceptée à nouveau comme organisation d’accueil du GSoC 2023](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/) !

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="La XSF et le Google Summer of Code 2023" >}}

### Hébergement fiscal de projets par la XSF

La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Veuillez postuler via [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets actuellement hébergés :

- [Pont Bifrost : échange de messages hors-ligne entre Matrix et XMPP](https://opencollective.com/bifrost-mam)
- [Coopérative Mellium](https://opencollective.com/mellium)

## Événements XMPP

- [Permanence XMPP](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Rencontres XMPP à Berlin (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les deuxièmes mercredis du mois.

## Articles

- Les responsables des paquets Debian donnent [un résumé](https://xmpp-team.pages.debian.net/blog/2023/03/xmpp-whats-new-in-bookworm.html) des paquets XMPP qui seront disponibles dans la prochaine version stable de Debian (Debian 12 "Bookworm").
- Cheogram Android [introduit des autocollants](http://blog.jmp.chat/b/cheogram-android-stickers-2023).
- IgniteRealtime : [des traductions partout !](https://discourse.igniterealtime.org/t/translations-everywhere/92628)
- Carl Schwan écrit sur [l'atelier sur la loi sur le marché numérique à Bruxelles](https://carlschwan.eu/2023/03/02/digital-market-act-workshop-in-brussels/).

{{< figure src="/images/newsletter/2023-04-05/dma_brussels.jpg" caption="Atelier sur la loi sur le marché numérique à Bruxelles" >}}

- L'IETF a approuvé [la publication de Messaging Layer Security (MLS)](https://www.ietf.org/blog/mls-secure-and-usable-end-to-end-encryption/), une nouvelle norme de sécurité de bout en bout qui permettra aux applications de fournir facilement le plus haut niveau de sécurité à leurs utilisateurs. Le chiffrement de bout en bout est une fonction de sécurité de plus en plus importante dans les applications Internet. Il permet de protéger les informations des utilisateurs même si le service en nuage qu'ils utilisent a été violé.

## Nouvelles des logiciels
### Clients et applications

- [Cheogram Android 2.12.1-4](https://git.singpolyma.net/cheogram-android/refs/2.12.1-4) a été publiée avec la prise en charge de l'envoi de réponses et de réactions aux messages, du glissé-pour-répondre, du contact "note à soi-même", de la visualisation des profils vcard4 et des pings MUC occasionnels.
- La [version 1.7.2 de Gajim](https://gajim.org/post/2023-03-09-gajim-1.7.2-released/) est disponible. Cette version apporte de nombreuses corrections de bogues et quelques améliorations utiles. Gajim vous permet maintenant de supprimer les messages de votre historique local (dans le cas de méchants messages de spam). De plus, la détection des fichiers audio WAV a été améliorée et vous pouvez maintenant cliquer sur la forme d'onde pour passer à un timestamp spécifique dans un message vocal.
- [monocles chat 1.6.3](https://codeberg.org/Arne/monocles_chat) a reçu la prise en charge de la modération des messages ([XEP-0425](https://xmpp.org/extensions/xep-0425.html)) et bénéficiera également de nouvelles fonctionnalités de Cheogram Android.
- [Movim 0.21 "Whipple"](https://mov.im/?node/pubsub.movim.eu/Movim/81f7e9d0-8cb6-47d7-a5d4-f3324c6aa306) a été publié, et il contient une tonne de nouvelles fonctionnalités. Réponses aux messages, Web Push, messages vocaux, nouveaux emojis, et bien plus encore.
- [SiskinIM 7.3.3](https://github.com/tigase/siskin-im/releases/tag/7.3.3) et [BeagleIM 5.3.4](https://github.com/tigase/beagle-im/releases/tag/5.3.4) de [Tigase](https://tigase.org/) ont été publiés.
- [Spark 3.0.2](https://igniterealtime.org/projects/spark/) de [Ignite Realtime](https://igniterealtime.org/) a été publié.

{{< figure src="/images/newsletter/2023-04-05/movim_replies.png" caption="Movim supports replies" >}}

### Serveurs

- Metronome IM [4.0.2](https://github.com/maranda/metronome/releases/tag/v4.0.2) apporte quelques corrections de bugs.

### Bibliothèques et outils

- [python-nbxmpp 4.2.1 et 4.2.2](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) ont été publiées. Elles corrigent certains bogues de la bibliothèque HTTP de python-nbxmpp.
- [QXmpp 1.5.1](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.1) et [QXmpp 1.5.2](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.2) ont été publiées en février et [QXmpp 1.5.3](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.3) en mars ! Elles corrigent d'importants bogues.
- [xmppbl.org](https://xmppbl.org) fournit un service de liste de bannissement en temps réel (RTBL) pour XMPP.
- [XmppDotNet](https://www.ag-software.net/2023/03/22/xmppdotnet-announcement/) est le nouveau nom et la nouvelle génération de la bibliothèque XMPP MatriX vNext.

De la communauté ignite realtime :
- [Openfire MUC Real-Time Block List plugin 1.1.0](https://discourse.igniterealtime.org/t/release-v1-1-0-of-the-muc-real-time-block-list-plugin-for-openfire/) a été publiée.
- [Openfire EXI plugin](https://discourse.igniterealtime.org/t/developing-openfire-efficient-xml-interchange-exi-functionality/) est en cours de développement.
- [Botz 1.2.0](https://discourse.igniterealtime.org/t/botz-version-1-2-0-release/) a été publiée.
- Le plugin [Openfire HTTP File Upload plugin 1.2.2](https://discourse.igniterealtime.org/t/http-file-upload-v1-2-2-released/) est disponible.

## Extensions et spécifications

La XMPP Standards Foundation développe des extensions XMPP dans sa [série de XEPs](https://xmpp.org/extensions/) en plus des [RFCs XMPP](https://xmpp.org/rfcs/).

Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent _finales_ ou _actives_ – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’_ajournées_. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).

### Extensions proposées

Le processus de développement XEP commence par la rédaction d’une idée et sa soumission à l’Éditeur XMPP. Dans un délai de deux semaines, le Conseil décide s’il accepte cette proposition en tant que XEP _expérimentale_.

- Pas de nouvelle XEP ce mois-ci.

### Nouvelles extensions

- Pas de nouvelle XEP ce mois-ci.

### Extensions ajournées

Si une XEP _expérimentale_ n’est pas mise à jour pendant plus de douze mois, elle sera déplacée d’_expérimentale_ à _ajournée_. S’il y a une autre mise à jour, elle remettra la XEP à l'état d'_expérimentale_.

- Aucune XEP ajournée ce mois-ci.

### Extensions mises-à-jour

- [Version 0.2.0 de XEP-0444 (Message Reactions)](https://xmpp.org/extensions/xep-0444.html)
  - Ajout d'un mécanisme de rejet des emojis. (NC)
- [Version 0.7.0 de XEP-0359 (Unique and Stable Stanza IDs)](https://xmpp.org/extensions/xep-0359.html)
  - Ajout de considérations de sécurité concernant l'usurpation d'identité et un exemple de référence.
- [Version 0.12.0 de XEP-0292 (vCard4 Over XMPP)](https://xmpp.org/extensions/xep-0292.html)
  - Suppression du mode raw-IQ et spécification de la réutilisation de la PEP (spw)
- [Version 0.4.0 de XEP-0388 (Extensible SASL Profile)](https://xmpp.org/extensions/xep-0388.html)
  - Mise à jour de l'espace de noms
  - Ajout d'une référence à la XEP-0440 et RFC 5802
  - Mise à jour des considérations de sécurité et des règles commerciales
  - Clarification de `<continue/>` et des tâches
  - Ajout d'un point d'expansion pour la reprise de flux en ligne et BIND2 (et éventuellement d'autres)
  - Ajout d'un élément optionnel `<user-agent/>`.
  - Déplacement de "Deferred" (différé) à "Experimental" (expérimental)
- [Version 0.4.0 de XEP-0386 (Bind 2)](https://xmpp.org/extensions/xep-0386.html)
  - Diverses modifications, effectuées parallèlement à l'expérience de mise en œuvre des clients et des serveurs, et aux mises à jour de SASL2.
  - Définition plus précise de l'intégration avec XEP-0388 et plusieurs XEP de fonctionnalités de session : XEP-0198, XEP-0280, XEP-0352.
  - Remplacer l'élément personnalisé latest-id par le nouvel élément de métadonnées de XEP-0313, qui fournit également des informations plus riches.
  - Abandonner le suivi des messages non lus, car il s'agit d'un sujet profond qui n'est pas directement lié à la liaison de ressources. En revanche, les détails de l'intégration avec d'autres extensions ont été mieux définis et démontrés, afin de permettre une telle fonctionnalité lorsqu'elle sera entièrement définie et existera.
  - Ajuster l'espace de noms proposé pour des raisons esthétiques et de cohérence avec l'approche de SASL2. Étant donné que ce protocole pourrait faire partie du nouveau flux de connexion préféré pendant longtemps, il n'est pas logique d'inclure le "2" redondant et potentiellement déroutant alors qu'il n'y a pas de conflit sans lui. De même, le ".0" a été supprimé du titre de la XEP, car il ne s'agit pas vraiment d'un numéro de version.
  - Permettre au client d'avoir une certaine influence sur l'identifiant de ressource résultant et définir un format standard pour ces identifiants combinés.
  - Spécifier que les serveurs doivent mettre fin aux anciennes sessions d'un client lorsqu'il lie une nouvelle ressource.
- [Version 0.2.0 de XEP-0428 (Fallback Indication)](https://xmpp.org/extensions/xep-0428.html)
  - Ajouter l'attribut "for" pour que les entités puissent savoir à quoi sert le "fallback".
  - Permet de spécifier que seul l'un des éléments `<subject>` ou `<body` est censé servir de repli.
  - Permettre de spécifier la partie du texte respectif qui est censée servir de solution de repli, le cas échéant.
  - Ne pas utiliser l'exemple de chiffrement, qui devrait utiliser XEP-0380 à la place.

### Dernier appel

Les _derniers appels_ sont émis une fois que tout le monde semble satisfait de l’état actuel d’une XEP. Après que le Conseil ait décidé que la XEP est prête, l’éditeur XMPP émet un dernier appel pour recueillir des commentaires. Les commentaires recueillis lors du dernier appel permettent d’améliorer la XEP avant de la renvoyer au Conseil pour qu’il passe à l’état _stable_.

- Pas de dernier appel ce mois-ci.

### Extensions stables

- Aucune XEP n’est passée à stable ce mois-ci.

### Extensions dépréciées

- Aucune XEP déclarée dépréciée ce mois-ci.

### Appel à l’expérience

Un _appel à l’expérience_ – comme un _dernier appel_ – est un appel explicite aux commentaires, mais dans ce cas, il s’adresse principalement aux personnes qui ont implémenté, et idéalement déployé, la spécification. Le Conseil vote ensuite pour la faire passer en version _finale_.

-   Pas d’appel à l’expérience ce mois-ci.

## Répandez les nouvelles !

Merci de partager les nouvelles sur d’autres réseaux :

* [Mastodon](https://fosstodon.org/@xmpp/)
* [Twitter](https://twitter.com/xmpp)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Lemmy instance](https://community.xmpp.net/)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

Consultez également notre [Flux RSS](https://xmpp.org/feeds/all.atom.xml) !

Vous recherchez des offres d’emploi ou vous souhaitez engager un consultant professionnel pour votre projet XMPP ? Visitez notre [tableau d’offres d’emploi XMPP](https://xmpp.work/).

### Contributions et traductions de la lettre d’information

Il s’agit d’un effort communautaire, et nous aimerions remercier les traducteurs et traductrices pour leurs contributions. Les volontaires sont les bienvenus ! Les traductions de la lettre d’information XMPP seront publiées ici (avec un certain retard) :

- anglais (original) : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - contributeurs généraux : **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, emus, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), wurstsalat, XSF iTeam**
- français : [jabberfr.org](https://news.jabberfr.org/category/newsletter/) et [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - traduction : **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, Pierre Jarillon, Ppjet6, Ysabeau**
- allemand : [xmpp.org](https://xmpp.org/categories/newsletter/) et [anoxinon.de](https://anoxinon.de/blog/)
  - traduction : **Jeybe, wh0nix**
- italien : [notes.nicfab.eu](https://notes.nicfab.eu)
  - traduction : **nicfab**
- espagnol : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - traduction : **daimonduff, TheCoffeMaker**

## Aidez-nous à créer la lettre d’information

Cette lettre d’information XMPP est produite collaborativement par la communauté XMPP. La lettre d’information de chaque mois est rédigé dans ce [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). À la fin de chaque mois, le contenu du pad est fusionné dans le [dépôt Github de la XSF](https://github.com/xsf/xmpp.org/milestone/3). Nous sommes toujours heureux d’accueillir des contributeurs et contributrices. N’hésitez pas à vous joindre à la discussion dans notre [salon public Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) et ainsi nous aider à soutenir cet effort communautaire. Vous avez un projet et vous voulez en parler ? Pensez à partager vos nouvelles ou vos événements ici, et à les promouvoir auprès d’un large public.

Tâches que nous effectuons régulièrement :

- collecte des nouvelles dans l’univers XMPP
- résumés *courts* des nouvelles et des événements
- résumé de la communication mensuelle sur les extensions (XEP)
- révision de l’ébauche de la lettre d’information
- préparation d’images pour les médias
- traductions
- communication à travers des comptes de médias

## Licence

Cette lettre d’information est publiée sous la licence [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
