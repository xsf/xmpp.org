---
title: Lettre d'information XMPP de juin & juillet 2023
date: 2023-08-11
categories: ['Newsletter']
---

Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre les mois de juin et juillet 2023.
Un grand merci à toutes les personnes qui nous lisent et à toutes les contributrices et tous les contributeurs !

Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite en bas de page.

### XMPP et le Google Summer of Code 2023

La XSF a été [acceptée à nouveau comme organisation hôte du GSoC 2023 et a reçu deux places pour les contributeurs XMPP] (https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/) !

Sur Dino :
 - [Support de Windows pour Dino](https://hrxi.github.io/gsoc/blog/windows-support-for-dino)
 - [Les malheurs de Windows](https://hrxi.github.io/gsoc/blog/windows-woes)

Sur Moxxy :
- Le [premier billet de blog](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), détaillant le plan d'implémentation d'une fonctionnalité basique de chat de groupe.
- Le [deuxième article de blog](https://moxxy.org/posts/2023-06-17-XEP-0045-In-Moxxmpp.html), décrivant les plans pour apporter une implémentation de base de [XEP-0045](https://xmpp.org/extensions/xep-0045.html) dans la bibliothèque XMPP de Moxxy, moxxmpp.
- Le [troisième article de blog](https://moxxy.org/posts/2023-07-24-Join-MUC-With-Moxxy.html), esquisse le plan d'implémentation du frontend.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### Hébergement fiscal de projets par la XSF

La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Veuillez postuler via [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets actuellement hébergés :

- [Pont Bifrost : échange de messages hors-ligne entre Matrix et XMPP](https://opencollective.com/bifrost-mam)
- [Coopérative Mellium](https://opencollective.com/mellium)

## Événements XMPP

- [Permanence XMPP](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Rencontres XMPP à Berlin (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les deuxièmes mercredis du mois.
- [XMPP Italian happy hour](https://tube.nicfab.eu/c/xmpp): réunion mensuelle XMPP Italie, depuis le 16 mai, chaque 3e jeudi du mois à 19h (événement en ligne avec diffusion en direct).

## Talks

- [Une messagerie instantanée qui respecte vos libertés ?](https://www.a-lec.org/actus/2023-06-23-conference-xmpp-bourbon-archambault/)[FR] : A travers un bref historique du web, afin de dépeindre sa centralisation actuelle et ses problèmes, Adrien Bourmault, membre de la XMPP Standards Foundation, vous présentera les problèmes posés par la messagerie instantanée non libre, basée sur des applications et des services centralisés. Il explorera également les solutions offertes par la décentralisation et les logiciels libres avec XMPP.  Voir la vidéo prochainement.

# Videos

- [Libervia: the Universal Communication Ecosystem](https://www.yewtu.be/watch?v=EkkiKn0TONs)

## Articles

- [Un nouvel endroit pour poezio et slixmpp](https://blog.mathieui.net/en/new-home-for-poezio-slixmpp.html).

- [Elbe-Sprint Hamburg 2023 : Post-Sprint Summary](https://xmpp.org/2023/08/elbe-sprint-hamburg-2023-post-sprint-summary/)

- OpenPGP & PGPainless
  - [PGPainless rencontre le Web-of-Trust](https://blog.jabberhead.tk/2023/07/25/pgpainless-meets-the-web-of-trust/)

- Deux réflexions sur l'élimination des réseaux décentralisés :
  - [Comment tuer un réseau décentralisé (tel que Fediverse)](https://ploum.net/2023-06-23-how-to-kill-decentralised-networks.html)
  - [Un fil de discussion sur cet article de MattJ](https://floss.social/@mattj/110595483224579575)

- [XMPP - Teil 2 - XMPP etwas genauer](https://anoxinon.media/blog/xmpp2/) [DE]

## Nouvelles des logiciels
### Clients et applications

- [JMP est lancé et sort de la version bêta](https://blog.jmp.chat/b/launch-2023)
- [Cheogram Android version `2.12.1-6`](https://git.singpolyma.net/cheogram-android/refs/2.12.1-6) ajoute des couleurs par compte, des heures de silence par compte, des aperçus des fichiers non téléchargés, et plus encore.
- [Libervia progress note 2023-W22](https://www.goffi.org/b/libervia-progress-note-2023-w22-x3Wa) sur l'implémentation A/V, ActivityPub Gateway et plus encore.
- [Dino 0.4.3](https://github.com/dino/dino/releases/tag/v0.4.3) a été publié.
- [Movim 0.22.2 est disponible](https://mov.im/node/pubsub.movim.eu/Movim/1d407d21-989d-404b-9a39-aa9b328882d1).

### Serveurs

- Le module ejabberd [mod_s3_upload](https://github.com/processone/ejabberd-contrib/tree/master/mod_s3_upload) a gagné [la prise en charge de l'utilisation d'un hôte de téléchargement séparé](https://github.com/processone/ejabberd-contrib/pull/320). Cela permet aux clients de télécharger du contenu multimédia à partir d'un panier S3 hébergé de manière statique. Au départ, cette fonctionnalité a été proposée pour permettre à ejabberd de s'intégrer à [Garage](https://garagehq.deuxfleurs.fr/), un service de stockage d'objets distribués open-source conçu pour l'auto-hébergement.

### Bibliothèques et outils

- Nouveau site web et [sortie de la version 0.4 de xmpp.rs](https://xmpp.rs/blog/release-xmpp-0-4/) : Après plus de trois ans et demi depuis la dernière version (version 0.3 en septembre 2019), les développeurs de xmpp-rs sont heureux d'annoncer la version 0.4.0 de xmpp-rs. Si vous ne connaissez pas xmpp-rs, ce sont des crates Rust pour des applications interopérables et fédérées de messagerie instantanée et autres réseaux sociaux.
- [omemo_dart](https://github.com/PapaTutuWawa/omemo_dart) a publié [la version 0.5.0](https://github.com/PapaTutuWawa/omemo_dart/releases/tag/v0.5.0), qui permet enfin à [Moxxy](https://moxxy.org/) d'établir des sessions OMEMO:2 stables entre deux clients Moxxy.
- [Le plugin Openfire inVerse v10.1.4-1 a été publié](https://discourse.igniterealtime.org/t/openfire-inverse-plugin-v10-1-4-1-release/92969)
- [Une passerelle de marionnettisation Matrix vers XMPP riche en fonctionnalités, basée sur slidge et nio](https://git.sr.ht/~nicoco/matridge)
- De la communauté ignite realtime :
  - [Le plugin Candy pour Openfire 2.2.0 Release 4 est maintenant disponible](https://discourse.igniterealtime.org/t/candy-plugin-for-openfire-2-2-0-release-4-now-available/93042)
  - [Sortie du plugin Search Openfire 0.7.4](https://discourse.igniterealtime.org/t/search-openfire-plugin-0-7-4-release/93043)
  - [Lancement du plugin Push Notification Openfire 0.9.2](https://discourse.igniterealtime.org/t/push-notification-openfire-plugin-0-9-2-released/93044)
- De la communauté ignite realtime :
  - [Le plugin Candy pour Openfire 2.2.0 Release 4 est maintenant disponible](https://discourse.igniterealtime.org/t/candy-plugin-for-openfire-2-2-0-release-4-now-available/93042)
  - [Sortie du plugin Search Openfire 0.7.4](https://discourse.igniterealtime.org/t/search-openfire-plugin-0-7-4-release/93043)
  - [Lancement du plugin Push Notification Openfire 0.9.2](https://discourse.igniterealtime.org/t/push-notification-openfire-plugin-0-9-2-released/93044)
  - [Publication du plugin JmxWeb pour Openfire 0.9.1](https://discourse.igniterealtime.org/t/jmxweb-plugin-for-openfire-0-9-1-release/93045)
  - [Sortie du plugin Agent Information pour Openfire 1.0.1](https://discourse.igniterealtime.org/t/agent-information-plugin-for-openfire-release-1-0-1/93057/1)
  - [Lancement du plugin Jabber Browsing Openfire 1.0.1](https://discourse.igniterealtime.org/t/jabber-browsing-openfire-plugin-1-0-1-released/93059)

## Extensions et spécifications

La XMPP Standards Foundation développe des extensions XMPP dans sa [série de XEPs](https://xmpp.org/extensions/) en plus des [RFCs XMPP](https://xmpp.org/rfcs/).

Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent _finales_ ou _actives_ – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’_ajournées_. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).

### Extensions proposées

Le processus de développement XEP commence par la rédaction d'une idée et sa soumission à l'Éditeur XMPP. Dans les deux semaines qui suivent, le Conseil décide d'accepter ou non cette proposition en tant que XEP expérimentale.

- [Signalement d'affiliation de compte](https://xmpp.org/extensions/inbox/xep-reporting-account-affiliations.html)
  - Cette spécification documente un moyen pour un serveur XMPP de signaler à d'autres entités la relation qu'il a avec un utilisateur de son domaine.

### Nouvelles extensions

- Pas de nouvelle XEP ce mois-ci.

### Extensions ajournées

Si une XEP expérimentale n'est pas mise à jour pendant plus de douze mois, elle sera déplacée d'expérimentale à différée. Si une nouvelle mise à jour est effectuée, la XEP sera à nouveau classée dans la catégorie expérimentale.

 - Aucune XEP ajournée ce mois-ci.

### Extensions mises-à-jour

- [Version 0.2.0 de la XEP-0317 (Hats)](https://xmpp.org/extensions/xep-0317.html)
  - Choix d'une syntaxe pour les hats. (mw)
- [Version 0.1.2 de la XEP-0453 (DOAP usage in XMPP)](https://xmpp.org/extensions/xep-0453.html)
  - Correction d'une typo XMLNS (spw)

### Dernier appel

Les derniers appels sont lancés une fois que tout le monde semble satisfait de l'état actuel d'une XEP. Une fois que le Conseil a décidé que la XEP semble prête, l'éditeur XMPP lance un dernier appel pour recueillir des commentaires. Les commentaires recueillis lors du dernier appel peuvent permettre d'améliorer la XEP avant de la renvoyer au Conseil pour qu'il la passe à l'état stable.

- Pas de dernier appel ce mois-ci.

### Extensions stables

- Aucune XEP n’est passée à stable ce mois-ci.

### Extensions dépréciées

- Aucune XEP déclarée dépréciée ce mois-ci.

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
  - Contributeurs généraux : **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), nicola, XSF iTeam**
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
