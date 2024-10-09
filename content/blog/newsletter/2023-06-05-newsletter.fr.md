---
title: Lettre d'information XMPP de mai 2023
date: 2023-06-05
categories: ['Newsletter']
---

Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre le mois de mai 2023.
Un grand merci à toutes les personnes qui nous lisent et à toutes les contributrices et tous les contributeurs !



Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite [en bas de page](#aidez-nous-à-créer-la-lettre-dinformation).

## Annonces de la XSF

- Si vous souhaitez devenir [membre de la XSF](https://xmpp.org/community/membership/), vous pourrez bientôt poser votre candidature au cours du troisième trimestre 2023.

### XMPP and Google Summer of Code 2023

La XSF a été [acceptée à nouveau comme organisation hôte du GSoC 2023](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/) !



- Le contributeur GSoC pour Moxxy a publié son [premier billet de blog](https://moxxy.org/posts/2023-05-06-Groupchat-GSoC-Project.html), détaillant le plan d'implémentation de la fonctionnalité de base du groupchat.

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

### Hébergement fiscal de projets par la XSF

La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Veuillez postuler via [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets actuellement hébergés :



- [Pont Bifrost : échange de messages hors-ligne entre Matrix et XMPP](https://opencollective.com/bifrost-mam)
- [Coopérative Mellium](https://opencollective.com/mellium)

## Événements XMPP

- [Permanence XMPP](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Rencontres XMPP à Berlin (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les deuxièmes mercredis du mois.
- [FOSSY](https://fossy.us) will have an XMPP track at their conference this summer from July 13-16th 2023
- [Happy hour XMPP italienne](https://tube.nicfab.eu/w/85RxLsnNTc9FcdFzFgkdsP) : réunion mensuelle XMPP italienne sur le web, à partir du 16 mai et ensuite tous les troisièmes mardis du mois à 19h00 (événement en ligne, avec mode réunion web et streaming en direct).

## Talks

- Le développeur de Libervia a prévu deux conférences informatives à Paris en juin. Ces présentations aborderont divers aspects du projet Libervia et de XMPP. La première conférence est une session de 20 minutes en anglais, qui aura lieu à 15h00 le jeudi 15 juin à [OW2](https://www.ow2con.org/view/2023/Abstract_Community_Day#15061500). Le deuxième exposé sera une discussion plus approfondie de 60 minutes en français, prévue à 17h30 le vendredi 16 juin à [Pas Sage En Seine](https://passageenseine.fr/). Ces sessions sont une excellente occasion de mieux comprendre le projet Libervia et d'interagir avec son développeur.

## Articles

L'autorité de concurrence du gouvernement allemand a publié une [étude sur les services de vidéo et de messagerie](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2023/17_05_2023_SU_MD.html) [DE] dans laquelle la XSF et plusieurs projets XMPP ont fait des déclarations. Lisez le [résumé](https://www.bundeskartellamt.de/SharedDocs/Publikation/DE/Sektoruntersuchungen/Sektoruntersuchung_MessengerVideoDienste_Zusammfassung.pdf?__blob=publicationFile&v=3) [DE] ou le [document complet](https://www.bundeskartellamt.de/SharedDocs/Publikation/DE/Sektoruntersuchungen/Sektoruntersuchung_MessengerVideoDienste.pdf?__blob=publicationFile&v=5) [DE].

## Nouvelles des logiciels
### Clients et applications

- [Gajim 1.8.0](https://gajim.org/post/2023-05-27-gajim-1.8.0-released/) est disponible et intègre le chiffrement OMEMO ! L'intégration du plugin OMEMO permet une meilleure intégration et une meilleure expérience utilisateur. Le menu de chat a été réorganisé et des boutons rapides ont été ajoutés pour plus de commodité. La recherche de messages et l'affichage des conversations de Gajim ont été modifiés et corrigés.

{{< figure src="/images/newsletter/2023-06-05/gajim-chat-banner-group-chat.png" caption="Gajim's chat banner in a group chat" >}}

- Les versions 0.9 et 0.9.1 de [Kaidan](https://www.kaidan.im/2023/05/05/kaidan-0.9.0/) ont été publiées ! Elles ajoutent le support pour OMEMO 2, Automatic Trust Management (ATM), [XMPP Providers](https://providers.xmpp.net/), Message Reactions et bien plus encore.

{{< figure src="/images/newsletter/2023-06-05/kaidan-0.9-horizontal.png" caption="Kaidan's chat view" >}}

- Des développements passionnants se profilent à l'horizon pour [Libervia](https://libervia.org/). Grâce à une subvention de NLnet par le biais du fonds NGI Assure, le travail sur l'implémentation des appels A/V avec Jingle sur plusieurs frontaux est en cours. Cette nouvelle fonctionnalité vise à prendre en charge les appels individuels et multipartites, et prévoit même d'ajouter des capacités de contrôle à distance du bureau. En outre, la passerelle ActivityPub est en cours de stabilisation, ce qui permettra d'améliorer encore les fonctionnalités de Libervia. Pour un aperçu complet de ces mises à jour et d'autres, consultez la dernière note d'avancement sur le [blog de Goffi](https://www.goffi.org/b/libervia-progress-note-2023-w22-x3Wa).



- JMP vous permet d'envoyer et de recevoir des messages texte et image (et des appels) par l'intermédiaire d'un véritable numéro de téléphone depuis votre ordinateur, votre tablette, votre téléphone ou tout autre appareil doté d'un client Jabber. Les réactions côté Jabber sont désormais traduites, dans la mesure du possible, dans la pseudo-syntaxe tapback. Pour en savoir plus, consultez le [blog JMP](https://blog.jmp.chat/b/april-newsletter-2023). [Cheogram Android 2.12.1-6](https://git.singpolyma.net/cheogram-android/refs/2.12.1-6) propose des couleurs et des heures de silence par compte, des aperçus de thumbhash pour les images et de nombreuses corrections de bogues.

### Serveurs

- [MongooseIM 6.1.0](https://www.erlang-solutions.com/blog/mongooseim-6-1-handle-more-traffic-consume-less-resources/) est disponible.



- Le serveur XMPP Openfire a reçu deux nouvelles versions : [Openfire 4.6.8 (old stable)](https://discourse.igniterealtime.org/t/openfire-4-6-8-release) et [Openfire 4.7.5 (stable)](https://discourse.igniterealtime.org/t/openfire-4-7-5-release). En outre, un [CVE sur le contournement de l'authentification de la console d'administration Openfire a été soumis](https://discourse.igniterealtime.org/t/cve-2023-32315-openfire-administration-console-authentication-bypass/92869).

### Bibliothèques et outils

- [omemo-dr](https://dev.gajim.org/gajim/omemo-dr/), une nouvelle bibliothèque cryptographique OMEMO est disponible. `omemo-dr` est une branche de `python-axolotl`, qui est la bibliothèque cryptographique utilisée pour le cryptage OMEMO dans Gajim. En préparation des changements futurs (par exemple la prochaine version d'OMEMO), les développeurs de Gajim ont forké cette bibliothèque.



- Les versions 4.3.0 et 4.3.1 de [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) ont été publiées et apportent plusieurs corrections de bugs concernant OMEMO et la gestion HTTP.

## Extensions et spécifications

La XMPP Standards Foundation développe des extensions XMPP dans sa [série de XEPs](https://xmpp.org/extensions/) en plus des [RFCs XMPP](https://xmpp.org/rfcs/).



Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent _finales_ ou _actives_ – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’_ajournées_. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).

### Extensions proposées

Le processus de développement des XEPs commence par la rédaction d'une idée et sa soumission à l'Éditeur XMPP. Dans les deux semaines qui suivent, le Conseil décide d'accepter ou non cette proposition en tant que XEP expérimentale.



- Pas de nouvelle XEP ce mois-ci.

### Nouvelles extensions

- [Version 0.1.0 de XEP-0480 (SASL Upgrade Tasks)](https://xmpp.org/extensions/xep-0480.html)



Cette spécification fournit un moyen de passer à des mécanismes SASL plus récents en utilisant les tâches SASL2.

- [Version 0.1.0 de XEP-0482 (Call Invites)](https://xmpp.org/extensions/xep-0482.html)



Ce document définit comment inviter quelqu'un à un appel et comment répondre à l'invitation.


- [Version 0.1.0 de XEP-0481 (Content Types in Messages)](https://xmpp.org/extensions/xep-0481.html)



Cette spécification décrit une méthode générique par laquelle le contenu des messages peut être étiqueté comme ayant un type de contenu Internet spécifique. Elle fournit également une méthode pour envoyer le même contenu en utilisant différents types de contenu, en tant que mécanisme de repli lors de la communication entre des clients prenant en charge différents types de contenu.


- [Version 0.1.0 de XEP-0478 (Stream Limits Advertisement)](https://xmpp.org/extensions/xep-0478.html)



Cette spécification définit un moyen pour une entité XMPP d'annoncer les limites qu'elle appliquera aux données reçues sur un flux.


- [Version 0.1.0 de XEP-0479 (XMPP Compliance Suites 2023)](https://xmpp.org/extensions/xep-0479.html)

Ce document définit les catégories d'applications XMPP pour différents cas d'utilisation (Core, Web, IM et Mobile) et spécifie les XEP requis que les logiciels clients et serveurs doivent mettre en œuvre pour être conformes aux cas d'utilisation.


### Extensions ajournées



Si une XEP _expérimentale_ n’est pas mise à jour pendant plus de douze mois, elle sera déplacée d’_expérimentale_ à _ajournée_. S’il y a une autre mise à jour, elle remettra la XEP à l’état d’_expérimentale_.



- Aucune XEP ajournée ce mois-ci.

### Extensions mises-à-jour

- [Version 1.25.0 de XEP-0060 (Publish-Subscribe)](https://xmpp.org/extensions/xep-0060.html)

Ajouter un texte d'information sur le modèle de données dans les notes de mise en œuvre.

Fournir un moyen pour un service PubSub d'indiquer à un client qu'un nœud est plein.

Clarifier le comportement et l'utilisation actuelle de l'option 'pubsub#itemreply'.

Correction de l'approbateur de spécifications

- [Version 1.1.1 de XEP-0223 (Persistent Storage of Private Data via PubSub)](https://xmpp.org/extensions/xep-0223.html)

Ajout de notes sur la vérification de l'origine des événements (en réaction à la CVE-2023-28686). (ka)


- [Version 1.1.0 de XEP-0313 (Message Archive Management)](https://xmpp.org/extensions/xep-0313.html)

Clarification de la réponse aux métadonnées d'archive dans le cas d'une archive vide.

Clarification de la réponse à la requête dans le cas où il n'y a pas de résultats correspondants. (mw)

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
  - Contributeurs généraux : **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, cal0pteryx, emus, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), nicola, XSF iTeam**
- Français : [jabberfr.org](https://news.jabberfr.org/category/newsletter/) et [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Traduction : **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
- Allemand : [xmpp.org](https://xmpp.org/categories/newsletter/) et [anoxinon.de](https://anoxinon.de/blog/)
  - Traduction : **Jeybe, wh0nix**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Traduction : **nicola**
- Espagnol : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Traduction : **daimonduff, TheCoffeMaker**

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
