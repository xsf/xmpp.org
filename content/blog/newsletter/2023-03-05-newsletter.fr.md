---
title: Lettre d'information XMPP de février 2023
date: 2023-03-05
categories: ['Newsletter']
---

Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre le mois de février 2023.
Un grand merci à toutes les personnes qui nous lisent et à toutes les contributrices et tous les contributeurs !

Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite [en bas de page](#aidez-nous-à-créer-la-lettre-dinformation).

## Annonces de la XSF

xmpp.org a une nouvelle section de logiciels ! Vous recherchez des logiciels XMPP, c’est-à-dire des clients, des serveurs, des bibliothèques, des composants et des outils ? Consultez la nouvelle [section logiciels](https://xmpp.org/software/) de [xmpp.org](https://xmpp.org/), qui vous permet de filtrer les logiciels selon vos propres critères. Vous recherchez un client fonctionnant sous Android et prenant en charge les appels audio/vidéo ? Vous recherchez une bibliothèque qui prend en charge la [XEP-0461 : Message Replies](https://xmpp.org/extensions/xep-0461.html) ? Appliquez simplement le filtre et voyez ce que vous obtenez !

{{< figure src="/images/newsletter/2023-03-05/xmpp-software-section.png" caption="La nouvelle section logiciels de xmpp.org" >}}

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

## Vidéos XMPP

- Cheogram offre une nouvelle [chaîne PeerTube](https://kumi.tube/c/cheogram) pour les vidéos sur les nouvelles fonctionnalités de son client XMPP et de ses passerelles. Également disponible [sur YouTube](https://YouTube.com/@cheogram).

## Articles

- [nicfab](https://notes.nicfab.eu) a écrit un article sur le [Digital Service Act : questions et réponses de la Commission européenne sur l’identification et le comptage des destinataires actifs du service dans le cadre de la DSA](https://notes.nicfab.eu/en/posts/dsa-faq/).



- [Digital Markets Act : le deuxième atelier des parties prenantes sur l’interopérabilité organisé par la Commission européenne](https://notes.nicfab.eu/en/posts/dmaworkshop/) un article de nicfab sur le récent atelier des parties prenantes de la DMA sur « l’interopérabilité entre les services de messagerie ».



- [New Profanity Old System](https://profanity-im.github.io/blog/post/distrobox/) par jubalh : Ce blog explique comment faire fonctionner correctement les dernières versions de Profanity sur des systèmes vieux de plusieurs années.



- La [lettre d’information JMP couvrant février 2023](https://blog.jmp.chat/b/february-newsletter-2023) a été publié. Ainsi qu’une [entrée de blog sur l’implémentation technique des autocollants](https://blog.jmp.chat/b/cheogram-android-stickers-2023) dans Cheogram Android.

## Nouvelles des logiciels
### Clients et applications

- [Converse 10.1.1](https://github.com/conversejs/converse.js/releases/tag/v10.1.1) et [10.1.2](https://github.com/conversejs/converse.js/releases/tag/v10.1.2) ont été publiés et corrigent toutes deux quelques bogues. Converse est un client web de discussion XMPP/Jabber.



- [Dino 0.4.0 'Ilulissat'](https://dino.im/blog/2023/02/dino-0.4-release/) et 0.4.1 ont été publiés. La version 0.4 ajoute le support des réactions et des réponses aux messages. Dino est également passé de GTK3 à GTK4 et utilise désormais libadwaita.



![Dino 0.4 supporte à présent les XEPs Message Replies et Message Reactions](https://news.jabberfr.org/wp-content/uploads/2023/03/dino-reaction.png)



- [Gajim 1.7.0](https://gajim.org/post/2023-02-03-gajim-1.7.0-released/) et [1.7.1](https://gajim.org/post/2023-02-08-gajim-1.7.1-released/) ont été publiés. Ces versions apportent une meilleure intégration de KeepassXC, de meilleures valeurs par défaut pour les discussions de groupe créées avec ejabberd, et quelques corrections de bogues importantes.



- [Psi+ 1.5.1645](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) et [1.5.1646](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) ont été publiés.

### Serveurs

- [Prosody 0.12.3](https://blog.prosody.im/prosody-0.12.3-released/) a été publié.
- [Openfire inVerse plugin 10.1.2](https://discourse.igniterealtime.org/t/inverse-openfire-plugin-10-1-2-1-released/92591) a été publié.
- Un nouveau plugin pour Openfire, le [MUC Real-Time Block List plugin](https://discourse.igniterealtime.org/t/new-openfire-muc-real-time-block-list-plugin/92587) a été publié. Il permet de modérer les salons de discussion, notamment pour les services fédérés.
- [Cobalt 1.3](https://www.isode.com/company/wordpress/cobalt-1-3-release-features/) est disponible.

### Bibliothèques et outils

- [nbxmpp 4.2.0](https://dev.gajim.org/gajim/python-nbxmpp) a été publiée, apportant une prise en charge de la [XEP-0461](https://xmpp.org/extensions/xep-0461.html) Message Replies et un profil pour SASLprep.

## Extensions et spécifications

La XMPP Standards Foundation développe des extensions XMPP dans sa [série de XEPs](https://xmpp.org/extensions/) en plus des [RFCs XMPP](https://xmpp.org/rfcs/).



Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent _finales_ ou _actives_ – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’_ajournées_. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).

### Extensions proposées

Le processus de développement XEP commence par la rédaction d’une idée et sa soumission à l’Éditeur XMPP. Dans un délai de deux semaines, le Conseil décide s’il accepte cette proposition en tant que XEP _expérimentale_.



- Pas de XEP proposée ce mois-ci.

### Nouvelles extensions

- Pas de nouvelle XEP ce mois-ci.

### Extensions ajournées

Si une XEP _expérimentale_ n’est pas mise à jour pendant plus de douze mois, elle sera déplacée d’_expérimentale_ à _ajournée_. S’il y a une autre mise à jour, elle remettra la XEP à l'état d'_expérimentale_.



- Aucune XEP ajournée ce mois-ci.

### Extensions mises-à-jour

- Aucune XEP mise-à-jour ce mois-ci.

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



- Anglais (original) : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Contributeurs généraux : **Adrien Bourmault (neox), Alexander "PapaTutuWawa", emus, Licaon_Kter, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), wurstsalat, Zash**
- Français : [jabberfr.org](https://news.jabberfr.org/category/newsletter/) et [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Traduction : **Adrien Bourmault (neox) et la communauté sur LinuxFr.org**
- Allemand : [xmpp.org](https://xmpp.org/categories/newsletter/) et [anoxinon.de](https://anoxinon.de/blog/)
  - Traduction : **Jeybe, wh0nix**
- Italien: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Traduction : **nicfab**
- Espagnol : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Traduction : **daimonduff, TheCoffeMaker**
## Aidez-nous à créer la lettre d’information

Cette lettre d’information XMPP est produite collaborativement par la communauté XMPP. La lettre d’information de chaque mois est rédigé dans ce [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung) _(N. D. T. : nouvelle adresse par rapport à l’année dernière, pensez à mettre à jour votre marque-page le cas échéant !)_. À la fin de chaque mois, le contenu du pad est fusionné dans le [dépôt Github de la XSF](https://github.com/xsf/xmpp.org/milestone/3). Nous sommes toujours heureux d’accueillir des contributeurs et contributrices. N’hésitez pas à vous joindre à la discussion dans notre [salon public Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) et ainsi nous aider à soutenir cet effort communautaire. Vous avez un projet et vous voulez en parler ? Pensez à partager vos nouvelles ou vos événements ici, et à les promouvoir auprès d’un large public.


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

