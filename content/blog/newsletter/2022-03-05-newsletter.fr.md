---
title: Lettre d'information XMPP de février 2022
author: XMPP Community
date: 2022-03-05
categories: ['Newsletter']
---

_N. D. T. — Ceci est une traduction de la lettre d’information publiée régulièrement par l’équipe de communication de la XSF, essayant de conserver les tournures de phrase et l’esprit de l’original. Elle est publiée conjointement sur les sites [LinuxFr.org](https://linuxfr.org/tags/xmpp/public) et [JabberFR.org](https://news.jabberfr.org/category/newsletter/)._

Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre le mois de février 2022.

Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, surtout dans la situation actuelle, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite en bas de page.

[Cette lettre d'information de février 2022 en anglais](https://xmpp.org/2022/03/the-xmpp-newsletter-february-2022/)
[Toutes les lettres d'information en version originale](https://xmpp.org/blog/)
[Souscrire à la lettre d'information en version originale par courriel](https://xmpp.org/newsletter/)
[Flux RSS de la lettre d'information en version originale](https://xmpp.org/feeds/all.atom.xml)
[XMPP/Jabber sur LinuxFr](https://linuxfr.org/tags/xmpp/public)

# Annonces XSF

![XSF et Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF und Google Summer of Code 2022")

- La XSF prévoit de participer au [Google Summer of Code 2022 (GSoC)](https://xmpp.org/community/gsoc-2022/). Si vous êtes intéressé par une participation en tant qu’étudiant, mentor ou pour un projet en général, veuillez [ajouter vos idées et nous contacter](https://wiki.xmpp.org/web/Google_Summer_of_Code_2022).
- Tous les membres de la XSF sont appelés à voter pour les [candidatures de membres](https://wiki.xmpp.org/web/Membership_Applications_Q1_2022).

# Projets d’hébergement fiscal XSF

La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Merci de postuler via la plateforme [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce dans le blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets actuels :

- [Passerelle Bifrost : échange de messages hors ligne entre Matrix et XMPP](https://opencollective.com/bifrost-mam)
- [Coopérative Mellium](https://opencollective.com/mellium)

# Événements

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les 2ᵉ mercredis du mois.

# Articles

- JMP.chat [décrit dans leur blog](http://blog.jmp.chat/b/2022-bidirectional-gateways) en quoi les passerelles, et surtout les passerelles bidirectionnelles, entre XMPP et les autres protocoles sont si utiles. [Leur bulletin d’information](http://blog.jmp.chat/b/february-newsletter-2022) annonce également le lancement des appels mondiaux et l’évolution de la charte graphique.

![JMP.chat passerelles bidirectionnelles](/images/newsletter/2022-02-05/JMP_bidirectional.png "JMP.chat passerelles bidirectionnelles")

- Erik Bärwaldt, du _Linux Magazin_ allemand [a évalué les messageries instantanées, y compris Conversations pour XMPP](https://www.linux-magazin.de/ausgaben/2022/02/bitparade/) [DE].
- [Communiqué de Mellium Dev](https://opencollective.com/mellium/updates/dev-communique-for-february-2022) : ce mois-ci, plusieurs nouveaux paquets ont été publiés, notamment des tests d’intégration pour Slixmpp, la prise en charge des signets natifs PEP, une meilleure prise en charge de divers hachages cryptographiques et la prise en charge des capacités d’entités.


# Nouvelles des logiciels

## Clients et applications

[Dino `0.3` a été publié](https://dino.im/blog/2022/02/dino-0.3-release/) : appels et conférences vidéo – chiffrés et pairs-à-pairs. Dino supporte maintenant les appels entre deux ou plusieurs personnes !

![Dino calls](/images/newsletter/2022-02-05/dino_conference_call.png "Dino calls")

[Nouvelles du développement de Gajim](https://gajim.org/post/2022-02-24-development-news-february/) : février a apporté une fenêtre unifiée de détails de chat de groupe, qui offre tous les boutons de configuration dont vous avez besoin. Également ce mois-ci : moins de fuites de mémoire et des codes QR OMEMO améliorés.

Monal a réussi une [campagne de financement](https://monal.im/blog/funding-campaign-mac-mini-for-faster-monal-development/) pour un serveur d’automatisation de construction, qui réduira considérablement le temps de compilation. [Plus d’informations sur le développement de Monal](https://monal.im/blog/insights-into-monal-development/) : Monal abandonnera la prise en charge d’iOS 12 et 13, ainsi que de macOS Catalina. L’équipe de Monal est à la recherche d’un développeur SwiftUI, et ils ont besoin d’aide pour construire un nouveau site Web simplifié.

De grandes nouvelles de Movim : [Movim `0.20` "Skiff"](https://mov.im/?node/pubsub.movim.eu/Movim/dd90cd1c-4bcd-45a5-88a3-220fd4280b21) a été publié, avec le support d’OMEMO, des améliorations de l’interface graphique et une meilleure gestion des discussions de groupe.

![Movim GUI update](/images/newsletter/2022-02-05/movim_publish.png "Movim GUI update")

[Psi+ `1.5.1605`](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) a été publié avec des corrections OMEMO.

[Poezio `0.13.2` a été publié](https://github.com/poezio/poezio/releases/tag/v0.13.2), cette version corrige seulement la compatibilité avec la nouvelle version slixmpp `1.8.0`, mais une version beaucoup plus intéressante est à venir bientôt.

Les développeurs de Profanity ont écrit un [article de blog](https://profanity-im.github.io/blog/post/profanity-on-pinephone/) sur la façon de faire fonctionner leur client sur les Pinephones.

Tigase a publié [BeagleIM `5.1`](https://github.com/tigase/beagle-im/releases/tag/5.1) et [SiskinIM `7.1`](https://github.com/tigase/siskin-im/releases/tag/7.1) avec un support OMEMO amélioré.


## Serveurs

[Jackal `0.57.0`](https://github.com/ortuman/jackal/releases/tag/v0.57.0), un serveur XMPP écrit en Go, a été publié.

Openfire annonce la sortie de [Openfire `4.7.1`](https://discourse.igniterealtime.org/t/openfire-4-7-1-released/91365) : les corrections notables comprennent des mises à jour de sécurité pour les pilotes de base de données intégrés, des corrections de la configuration de la journalisation, et une correction importante pour les utilisateurs rencontrant des problèmes avec les utilisateurs qui se font déconnecter des salles de chat de groupe. En outre, [Openfire Pàdé `1.6.1`](https://discourse.igniterealtime.org/t/openfire-pade-1-6-1-released/91366) a été publié. [REST API Openfire plugin `1.7.1`](https://discourse.igniterealtime.org/t/rest-api-openfire-plugin-1-7-1-released/91358) a également été publié.

Snikket a publié une mise à jour importante pour les utilisateurs de leur [logiciel serveur pour les machines ARM, y compris les cartes Raspberry Pi](https://snikket.org/blog/server-updates-for-arm/).

Le [serveur Tigase XMPP `8.2.0`](https://github.com/tigase/tigase-server/releases/tag/tigase-server-8.2.0) a été publié.

## Bibliothèques

La coopérative Mellium a publié les versions [`v0.21.0`](https://pkg.go.dev/mellium.im/xmpp@v0.21.0) et [`v0.21.1`](https://pkg.go.dev/mellium.im/xmpp@v0.21.1) de la bibliothèque [melium.im/xmpp](https://mellium.im/xmpp/) pour Go ! Les points forts de cette version sont le support de base de PubSub et PEP ainsi que les _Bytestreams In-Band_. Vous trouverez plus d’informations dans l'[annonce de la publication](https://opencollective.com/mellium/updates/new-release-mellium-im-xmpp-v0-21-0). La version 0.21.1 corrige un problème de sécurité qui a été découvert dans le paquet _websocket_ et doit être privilégiée lors de la mise à jour. Pour plus d’informations, voir [CVE-2022-24968](https://mellium.im/cve/cve-2022-24968/).

[Slixmpp `1.8.0`](https://lab.louiz.org/poezio/slixmpp/-/releases/slix-1.8.0) a été publié, ce qui ajoute la compatibilité avec python 3.10, ainsi que de nombreuses améliorations liées au typage et à l’asynchronisme sous le capot.

Tigase a publié plusieurs versions pour ses produits : [Halcyon `0.0.17`](https://github.com/tigase/halcyon/releases/tag/v0.0.17), [JaXMPP `3.5.0`](https://github.com/tigase/jaxmpp/releases/tag/3.5.0), [Tigase Swift `3.1.0`](https://github.com/tigase/tigase-swift/releases/tag/3.1.0), et [Tigase Swift-OMEMO `2.1.0`](https://github.com/tigase/tigase-swift-omemo/releases/tag/2.1.0).

# Extensions et spécifications

Les développeurs et autres experts en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes, et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent en tant que Finales ou Actives – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’Ajournées. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).

## Proposed (Extensions proposées)

Le processus de développement d’une XEP commence par la rédaction d’une idée et sa soumission à l’éditeur XMPP. Dans un délai de deux semaines, celui-ci décide d’accepter ou non cette proposition en tant que XEP expérimentale.

- [PubSub Type Filtering](https://xmpp.org/extensions/inbox/pubsub-filter.html)
    - Cette spécification fournit un moyen de filtrer les noeuds PubSub dans une requête disco.

- [MUC Affiliations Versioning](https://xmpp.org/extensions/inbox/muc-affiliations)
    - Cette spécification fournit un moyen de réduire le nombre de requêtes nécessaires pour rester à jour avec les affiliations dans un salon MUC.

## New (Nouvelles extensions)

- Aucune nouvelle extension ce mois-ci.

## Obsolete (Extensions ajournées)

Si une XEP expérimentale n’est pas mise à jour pendant plus de douze mois, elle sera déplacée d’Expérimentale à Ajournée. S’il y a une autre mise à jour, la XEP redeviendra Expérimentale.

- Aucune XEP ajournée ce mois-ci.

## Updated (Mises à jour)

- Version `2.13.0` de [XEP-0004](https://xmpp.org/extensions/xep-0004.html) (Formulaires de données)
    - Ajout de la gestion des formulaires de soumission incomplets (melvo)

- Version `1.24.1` de [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    - Ajout d’une astuce pour le traitement des formulaires de soumission incomplets (melvo)

- Version `1.24.0` de [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    - Annonce de la prise en charge de la publication d'éléments
    - Remplacer "allow" par "allows" (melvo)

- Version `1.23.0` de [XEP-0060](https://xmpp.org/extensions/xep-0060.html) (Publish-Subscribe)
    - Clarifier (redéfinir) le champ pubsub#type. (edhelas, pep)

## Last call (Dernier appel)

Les derniers appels sont émis une fois que tout le monde semble satisfait de l’état actuel du XEP. Après que le Conseil ait décidé si le XEP semble prêt, l’éditeur XMPP émet un dernier appel pour les commentaires. Les commentaires recueillis lors du dernier appel permettent d’améliorer le XEP avant de le renvoyer au Conseil pour qu’il passe à l’état stable.

- Pas de Dernier Appel ce mois-ci.


## Stable (anciennement connu sous le nom de "Draft" (Brouillons))

Info : La XSF a décidé de renommer "Draft" (Brouillons) en "Stable". (Pour en savoir plus, cliquez ici.) (https://github.com/xsf/xeps/pull/1100)

- Aucune XEP n’a avancé vers Stable ce mois-ci.

## Depreciated (Dépréciées)

- Aucune XEP dépréciée ce mois-ci.

## Call for experience (Appel à l’expérience)

Un appel à l’expérience - comme un dernier appel, est un appel explicite aux commentaires, mais dans ce cas, il est principalement destiné aux personnes qui ont mis en œuvre, et idéalement déployé, la spécification. Le Conseil vote ensuite pour la faire passer en version finale.

- Pas d’appel à l’expérience ce mois-ci.


# Répandez la nouvelle !

Veuillez partager la nouvelle sur d’autres réseaux :

* [Mastodon](https://fosstodon.org/@xmpp/)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Twitter](https://twitter.com/xmpp)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

Consultez également notre [Flux RSS](https://xmpp.org/feeds/all.atom.xml) !

Vous recherchez des offres d’emploi ou souhaitez engager un consultant professionnel pour votre projet XMPP ? Visitez notre [tableau d’offres d’emploi XMPP](https://xmpp.work/).

# Aidez-nous à construire la lettre d’information

Cette lettre d’information XMPP est produite en collaboration par la communauté XMPP. Nous tenons donc à remercier **Adrien Bourmault (neox), alkino, anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Ludovic Bocquet, Licaon_Kter, marevalo, mathieui, MattJ, nicfab, seveso, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat,xdelatour, Ysabeau** pour leur soutien et leur aide à la création, la révision et la traduction. Un grand merci à tous les contributeurs et à leur soutien continu !

Le numéro de la lettre d’information de chaque mois est rédigé dans ce [bloc-notes simple](https://yopad.eu/p/xmpp-newsletter-365days). À la fin de chaque mois, le contenu du pad est fusionné dans le [dépôt Github XSF](https://github.com/xsf/xmpp.org/milestone/3). Nous sommes toujours heureux d’accueillir des contributeurs. N’hésitez pas à rejoindre la discussion dans notre [Salon de discussion Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) et ainsi nous aider à soutenir cet effort communautaire. Vous avez un projet et vous voulez faire connaître la nouvelle ? Pensez à partager vos nouvelles ou vos événements ici, et à les promouvoir auprès d’un large public.

Tâches que nous effectuons régulièrement :

- collecte des nouvelles dans l’univers XMPP
- résumés *courts* des nouvelles et des événements
- résumé de la communication mensuelle sur les extensions (XEPs)
- révision de l’ébauche de la lettre d’information
- préparation d’images pour les médias
- traductions

# Licence

Cette lettre d’information est publiée sous licence [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
