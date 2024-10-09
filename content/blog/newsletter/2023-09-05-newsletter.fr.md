---
title: Lettre d'information XMPP d'août 2023
date: 2023-09-05
categories: ['Newsletter']
---

Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre le mois d'août 2023.
Un grand merci à toutes les personnes qui nous lisent et à toutes les contributrices et tous les contributeurs !

Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite [en bas de page](#aidez-nous-à-créer-la-lettre-dinformation).

### XMPP and Google Summer of Code 2023

La XSF a été [acceptée à nouveau comme organisation hôte du GSoC 2023 et a reçu deux places pour les contributeurices XMPP] (https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/) !

Sur Dino :

- [Support de Windows pour Dino](https://hrxi.github.io/gsoc/blog/windows-support-for-dino)
- [Les malheurs de Windows](https://hrxi.github.io/gsoc/blog/windows-woes)

Sur Moxxy :

- Le [premier billet de blog](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), détaillant le plan d'implémentation d'une fonctionnalité basique de discussion de groupe.
- Le [deuxième billet de blog](https://moxxy.org/posts/2023-06-17-XEP-0045-In-Moxxmpp.html), décrivant les plans pour apporter une implémentation de base de la [XEP-0045](https://xmpp.org/extensions/xep-0045.html) dans la bibliothèque XMPP de Moxxy, moxxmpp.
- Le [troisième billet de blog](https://moxxy.org/posts/2023-07-24-Join-MUC-With-Moxxy.html), esquissant le plan d'implémentation du frontend.
- Le [quatrième billet de blog](https://moxxy.org/posts/2023-08-20-Moxxy-MUC-GSoC-Final-Report.html), concluant sur le support MUC de Moxxy.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### Hébergement fiscal de projets par la XSF

La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Veuillez postuler via [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets actuellement hébergés :

- [Pont Bifrost : échange de messages hors-ligne entre Matrix et XMPP](https://opencollective.com/bifrost-mam)
- [Coopérative Mellium](https://opencollective.com/mellium)

## Événements XMPP

- [Permanence XMPP](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Rencontres XMPP à Berlin (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les deuxièmes mercredis du mois.
- [XMPP Italian happy hour](https://tube.nicfab.eu/c/xmpp): réunion mensuelle italienne XMPP, à partir du 16 mai et ensuite tous les troisièmes mardis du mois à 19h00 (événement en ligne, avec mode réunion web et streaming en direct).
- [TroLUG XMPP Workshop](http://trolug.de/termine.html) : le TroLUG organise le deuxième atelier sur XMPP en langue allemande le 2023-09-07. Il se déroulera en audioconférence via BBB. Toutes les personnes intéressées sont invitées à participer à l'atelier.

## Videos

Il y a eu tout un fil rouge sur XMPP au [FOSSY2023] (https://2023.fossy.us/schedule/) avec de nombreux exposés :

- [XMPP Connectivity & Security](https://archive.org/details/fossy2023_XMPP_Connectivity__Security) est une introduction aux XEPs de connectivité XMPP comme XEP-0368 (Direct TLS), XEP-0467 (QUIC), XEP-0468 (WebSocket S2s) et les aspects internes de xmpp-proxy, un proxy forward+reverse, et d'autres.
- [XMPP Introduction and Overview](https://archive.org/details/fossy2023_XMPP_Introduction_and_Overview) est un bref historique et une introduction au protocole XMPP pour les personnes ayant peu d'expérience en programmation.
- [My XMPP Past, Present, and Future](https://archive.org/details/fossy2023_My_XMPP_Past_Present_and_Futur) est un point de vue sur l'évolution de l'écosystème XMPP depuis 2004. Il explique comment il a été affecté par des événements majeurs tels que le déclin des services de messagerie instantanée traditionnels, le début de l'ère des smartphones et des nouveaux services de chat, et plus encore.
- [Building open standards-based ecosystems] (https://archive.org/details/fossy2023_Building_open_standardsbased_e) est un exposé sur la façon dont XMPP, en tant que communauté et protocole, s'est adapté au changement, et sur le rôle que la XSF a joué dans sa continuité, mais aussi une discussion générale sur la durabilité des écosystèmes ouverts et des réseaux ouverts.

## Articles

- Pas d'articles ce mois-ci.

## Nouvelles des logiciels

### Clients et applications

- [Converse 10.1.6](https://github.com/conversejs/converse.js/releases/tag/v10.1.6) a été publiée. Elle corrige deux bogues graphiques.
- [Gajim 1.8.1](https://dev.gajim.org/gajim/gajim/-/releases/1.8.1) est disponible avec de nombreuses corrections de bugs. Notez que le plugin OMEMO de Gajim a été intégré au noyau de Gajim avec Gajim 1.8.0. Vous n'avez plus besoin de ce plugin.
- [monocles chat 1.7.3](https://codeberg.org/Arne/monocles_chat/releases/tag/v1.7.3) est disponible sur f-droid avec quelques corrections et de nombreuses nouvelles fonctionnalités de Cheogram.
- [Profanity 0.14.0](https://github.com/profanity-im/profanity/releases/tag/0.14.0) est disponible.
- [L'état de Snikket en 2023 : les applications](https://snikket.org/blog/state-of-snikket-2023-the-apps/).

{{< figure src="/images/newsletter/2023-09-05/snikket-logo.png" caption="Snikket - Chat that is simple, secure, and private" width="200" alt="Snikket Logo" >}}

### Serveurs

- [Metronome IM 4.0.3](https://github.com/maranda/metronome/releases/tag/v4.0.3) a été publié !

### Bibliothèques et outils

- [libstrophe 0.12.3](https://github.com/strophe/libstrophe/releases/tag/0.12.3) a été publié.
- [python-nbxmpp 4.3.2](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/4.3.2) et [4.3.3](https://dev.gajim.org/gajim/python-nbxmpp/-/tags/4.3.3) ont été publiés avec des corrections de bugs.
- [XMPP Providers](https://providers.xmpp.net) a mis en place un nouveau [bot web](https://fosstodon.org/@xmpp_providers/110802431627220360) et un [bot XMPP](https://fosstodon.org/@xmpp_providers/110968568856872183) mettant à jour plusieurs propriétés des fournisseurs.

{{< figure src="/images/newsletter/2023-09-05/xmpp-providers-logo.png" caption="XMPP Providers - Which XMPP provider suits you best? It’s your choice." width="150" alt="XMPP Providers Logo" >}}

## Extensions et spécifications

La XMPP Standards Foundation développe des extensions XMPP dans sa [série de XEPs](https://xmpp.org/extensions/) en plus des [RFCs XMPP](https://xmpp.org/rfcs/).

Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent _finales_ ou _actives_ – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’_ajournées_. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).

### Extensions proposées

Le processus de développement XEP commence par la rédaction d'une idée et sa soumission à l'éditeur XMPP. Dans les deux semaines qui suivent, le Conseil décide d'accepter ou non cette proposition en tant que XEP expérimentale.

- [MUC Token Invite] (https://xmpp.org/extensions/inbox/muc-token-invite.html)
  - Cette spécification fournit un moyen de générer des jetons pour inviter des utilisateurs dans une salle MUC.

### Nouvelles extensions

- Pas de nouvelle XEP ce mois-ci.

### Extensions ajournées

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

- Aucune XEP ajournée ce mois-ci.

### Extensions mises-à-jour

- Version 0.2.1 de la XEP-0458 [Code de conduite de la communauté](https://xmpp.org/extensions/xep-0458.html)
  - Ajouter des ancres à chaque section, pour faciliter la création de liens.  Correction d'une coquille (egp).
- [Version 0.4.1 de la XEP-0333 (Chat Markers)](https://xmpp.org/extensions/xep-0333.html)
  - Modification de l'exemple de découverte pour utiliser les JIDs des clients. (gdk)
- [Version 1.1.0 de la XEP-0459 (XMPP Compliance Suites 2022)](https://xmpp.org/extensions/xep-0459.html)
  - Remplacement de la XEP-0411 (obsolète) par la XEP-0402 dans Advanced Group Chat. (egp)

### Dernier appel

Les derniers appels sont lancés une fois que tout le monde semble satisfait de l'état actuel du XEP. Une fois que le Conseil a décidé si le XEP semble prêt, l'éditeur XMPP lance un dernier appel pour recueillir des commentaires. Les commentaires recueillis lors du dernier appel peuvent permettre d'améliorer le XEP avant de le renvoyer au Conseil pour qu'il passe à l'état stable.

- Pas de dernier appel ce mois-ci.

### Extensions stables

- Aucune XEP n’est passée à stable ce mois-ci.

### Extensions dépréciées

- Aucune XEP déclarée dépréciée ce mois-ci.

## Spread the news

Merci de partager les nouvelles sur d’autres réseaux :

- [Mastodon](https://fosstodon.org/@xmpp/)
- [Twitter](https://twitter.com/xmpp)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Lemmy instance](https://community.xmpp.net/)
- [Reddit](https://www.reddit.com/r/xmpp/)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

{{< newsletter-subscribe >}}

Consultez également notre [Flux RSS] (https://xmpp.org/feeds/all.atom.xml) !

Vous recherchez des offres d'emploi ou souhaitez engager un consultant professionnel pour votre projet XMPP ? Visitez notre [XMPP job board](https://xmpp.work/).

### Contributions et traductions de la lettre d’information

Il s’agit d’un effort communautaire, et nous aimerions remercier les traducteurs et traductrices pour leurs contributions. Les volontaires sont les bienvenus ! Les traductions de la lettre d’information XMPP seront publiées ici (avec un certain retard) :

- Anglais (original) : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Contributeurs généraux : **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Jonas Stein, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), nicola, XSF iTeam**
- Français : [jabberfr.org](https://news.jabberfr.org/category/newsletter/) et [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Traduction : **Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
- Allemand : [xmpp.org](https://xmpp.org/categories/newsletter/) et [anoxinon.de](https://anoxinon.de/blog/)
  - Traduction : **Jeybe, wh0nix**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Traduction : **nicola**
- Espagnol : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Traduction : **daimonduff, TheCoffeMaker**

## Aidez-nous à créer la lettre d’information

Cette lettre d’information XMPP est produite collaborativement par la communauté XMPP. La lettre d’information de chaque mois est rédigé dans ce [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). À la fin de chaque mois, le contenu du pad est fusionné dans le [dépôt Github de la XSF]](https://github.com/xsf/xmpp.org/milestone/3). Nous sommes toujours heureux d’accueillir des contributeurs et contributrices. N’hésitez pas à vous joindre à la discussion dans notre [salon public Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) et ainsi nous aider à soutenir cet effort communautaire. Vous avez un projet et vous voulez en parler ? Pensez à partager vos nouvelles ou vos événements ici, et à les promouvoir auprès d’un large public.

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
