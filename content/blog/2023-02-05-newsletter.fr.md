---
title: Lettre d'information XMPP de décembre 2022 et janvier 2023
date: 2023-02-05
categories: ['Newsletter']
---

Bienvenue dans la lettre d'information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre les mois de décembre 2022 et janvier 2023. 
Il s'agit de la première publication après une pause hivernale bien méritée ! Un grand merci à tous nos lectrices et lecteurs et à tous les contributrices et contributeurs !


Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite en bas de page.

# Annonces de la XSF

Si vous souhaitez devenir membre de la XSF, les [listes sont ouvertes jusqu'au 19 février 2023](https://wiki.xmpp.org/web/Membership_Applications_Q1_2023).

## Hébergement fiscal de projets par la XSF

La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Veuillez postuler via [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets actuellement hébergés :

- [Pont Bifrost : échange de messages hors-ligne entre Matrix et XMPP](https://opencollective.com/bifrost-mam)
- [Coopérative Mellium](https://opencollective.com/mellium)

## Google Summer of Code 2023

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF et Google Summer of Code 2023" >}}

Nous envisageons de participer au Google Summer of Code 2023! Si vous êtes intéressés ou interessées, [lire ici](https://wiki.xmpp.org/web/Google_Summer_of_Code_2023).

## Événements XMPP

- [XMPP Summit 25 et FOSDEM 2023](https://xmpp.org/2023/01/xmpp-at-fosdem-2023/)
- [Permanence XMPP](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Rencontres XMPP à Berlin (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les deuxièmes mercredis du mois.

## Conférences XMPP

- [XMPP - Conférence de fin d'année 2022](https://bbb.sfconservancy.org/b/ste-fdo-qen)
- [Chat interopérable, système de santé néerlandais et loi sur les services numériques](https://fosdem.org/2023/schedule/event/interoperable_chat/)  Winfried a partagé les nombreux défis rencontrés lors de l'élaboration d'une norme pour le chat interopérable dans le domaine de la santé, compatible avec les nouvelles réglementations de l'UE.
- [P10K : faire participer 10000 personnes à une réunion Jitsi](https://fosdem.org/2023/schedule/event/jitsi_p10k/), Saúl, de l'équipe Jitsi, nous dévoile son parcours intéressant pour atteindre 10000 participants à une visioconférence sous Jitsi alimentée par XMPP.
- [Moderniser l'authentification et les autorisations dans XMPP](https://fosdem.org/2023/schedule/event/modern_xmpp_auth/): Matthew Wild, fondateur des projets Prosody et Snikket, explique pourquoi il est temps pour nous d'aller au-delà des mots de passe pour l'authentification.

# Articles

Un [test de résistance du serveur de streaming PeerTube](https://www.octopuce.fr/test-de-charge-dun-peertube-en-live-avec-auposte/) incluant un chat en direct basé sur XMPP (Prosody) a été réalisé. Il a permis d'identifier un certain nombre d'optimisations possibles dans le plugin de chat en direct de Peertube. Lisez le [post de l'auteur du plugin](https://john-livingston.fr/foss/article/peertube-chat-plugin-quick-feedbacks-about-a-live-stress-test) pour plus de détails.



![Peertube with XMPP-based live chat](https://news.jabberfr.org/wp-content/uploads/2023/02/peertube.jpg)



Jabber.org, le service de messagerie instantanée XMPP originel, a été [migré vers le serveur de messagerie instantanée Prosody le week-end du 14-15 janvier](http://www.jabber.org/notices.html). Historique complet : jabberd -> ejabberd -> Isode M-Link -> Prosody IM



Un article sur la ["tokenisation de l'immobilier durable dans les villes intelligentes : la monétisation comme base pour la construction, l'autorisation et la neutralisation du carbone dans les CPS (systèmes cyber-physiques)"](https://ieeexplore.ieee.org/document/9968404) (utilisant des techniques basées sur XMPP) a été présenté à IECON2022 et a été publié récemment.



[La lettre d'information de décembre de JMP](https://blog.jmp.chat/b/december-newsletter-2022) parle de la nouvelle structure de la coopérative, d'un important correctif de sécurité dans l'application Android de Cheogram et d'une revue des points forts de 2022.  La [Lettre d'information de janvier de JMP](https://blog.jmp.chat/b/january-newsletter-2023) mentionne une autre nouvelle version comprenant une nouvelle [interface utilisateur pour les dicussions XMPP par threads](https://kumi.tube/w/1LQQp5Uia4u8Pdojxen1y8) et de nouvelles options de paiement pour le service. Enfin et surtout : [écrire un client de chat à partir de zéro](https://blog.jmp.chat/b/2022-chat-client-from-scratch) en Ruby.



Snikket vous informe des [avertissements de sécurité de F-Droid](https://snikket.org/blog/fdroid-security-warning/) et de leur [mise à jour de sécurité](https://snikket.org/blog/fdroid-security-update/). Les problèmes ont déjà été résolus.



[vanitasvitae](https://blog.jabberhead.tk/) écrit sur PGPainless : [utiliser n'importe quel binaire SOP avec SOP-Java et External-SOP](https://blog.jabberhead.tk/2023/01/13/use-any-sop-binary-with-sop-java-and-external-sop/)



nicfab écrit sur la nouvelle [directive NIS 2 de l'UE : s'applique-t-elle à tous ceux qui fournissent des services numériques gratuits en ligne ?](https://notes.nicfab.it/en/posts/nis2/)

# Nouvelles des logiciels
## Clients et applications

[BeagleIM 5.3.2, 5.3.3 et SiskinIM 7.3.1, 7.3.2](https://tigase.org/blog/beagleim-5.3.2-and-siskinim-7.3.1-released/) ont été publiées avec une option permettant de bloquer des domaines entiers et un certain nombre de corrections de bogues en plus de tous nouveaux logos et icônes.



[Les versions 2.11.0 à 2.12.1 de Conversation ont été publiées](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/CHANGELOG.md) ! Elles mettent en œuvre le profil SASL extensible, Bind 2.0 ainsi que Channel Binding et Fast pour des reconnexions plus rapides. De plus, la possibilité de passer d'un appel audio à un appel vidéo, de supprimer son propre avatar et une notification pour les appels manqués ont été ajoutés. Depuis la version 2.12.0, Conversations intègre également un [distributeur UnifiedPush](https://unifiedpush.org/users/distributors/) pour faciliter l'envoi de messages push à d'autres applications compatibles avec UnifiedPush comme Tusky et Fedilab. Les utilisateurs peuvent utiliser le serveur UP fourni par le développeur ou demander à leur administrateur de serveur d'héberger un serveur UP en tant que [composant universel de transport XMPP](https://codeberg.org/iNPUTmice/up) ou de charger le [nouveau module Prosody](https://modules.prosody.im/mod_unified_push). Comme annoncé dans la [newsletter de novembre 2022](https://xmpp.org/2022/12/the-xmpp-newsletter-november-2022/) la version 3.0 a été financée, le développement a donc déjà commencé, vous pouvez suivre son évolution dans la [nouvelle branche de code `c3`](https://codeberg.org/iNPUTmice/Conversations/commits/branch/c3).



[Gajim 1.6.0](https://gajim.org/post/2023-01-07-gajim-1.6.0-released/) et [1.6.1](https://gajim.org/post/2023-01-14-gajim-1.6.1-released/) ont été publiées. Pour Gajim 1.6, les développeurs ont porté la bibliothèque HTTP sous-jacente de Gajim et de python-nbxmpp vers libsoup3. De plus, les aperçus audio sont maintenant plus jolis et permettent un meilleur contrôle (vitesse de lecture, saut). Le rendu des Emoji sur macOS a été réparé et de nombreuses corrections ont été implémentées sous le capot.


Libervia a reçu un [financement du fond NLnet NGI Assure pour l'implémentation d'appels audio/vidéo](https://nlnet.nl/project/Libervia-AV/).



Les versions [Moxxy 0.4.0](https://codeberg.org/moxxy/moxxy/releases/tag/v0.4.0) et [0.4.1](https://codeberg.org/moxxy/moxxy/releases/tag/v0.4.1) ont été publiées. Ces deux versions apportent des autocollants, des réactions, l'enregistrement de messages vocaux et diverses améliorations et corrections de l'interface utilisateur et du code XMPP.



De la communauté ignite realtime :



- [Spark 3.0.1 publiée](https://discourse.igniterealtime.org/t/spark-3-0-1-released/92353)
![Spark 3.0.1](https://news.jabberfr.org/wp-content/uploads/2023/02/spark.png)



- Une vulnérabilité de déni de service dans Smack 4.4 [a été corrigée](https://discourse.igniterealtime.org/t/denial-of-service-vulnerability-in-smack-4-4-if-xmpptcpconnection-is-used-with-stax/92314)
- La communauté Ignite Realtime offre désormais [un service Mastodon](https://discourse.igniterealtime.org/t/new-mastodon-service-for-the-ignite-realtime-community/92389)
- La communauté a lancé un appel à l'aide pour [la traduction de Spark et Openfire](https://discourse.igniterealtime.org/t/help-us-translate-spark-and-openfire/92399)

## Serveurs

[ejabberd 23.01 a été publiée](https://www.process-one.net/blog/ejabberd-23-01/). Près de trois mois après la version précédente, ejabberd 23.01 comprend de nombreuses corrections de bogues, plusieurs améliorations et quelques nouvelles fonctionnalités. Un nouveau module, mod_mqtt_bridge, peut être utilisé pour répliquer les modifications apportées aux sujets MQTT entre les serveurs locaux et distants. Les XEP supportées sont maintenant automatiquement collectés à partir de la documentation du code source afin de fournir un fichier DOAP pour un traitement ultérieur sur [xmpp.org/servers/ejabberd](https://xmpp.org/software/servers/ejabberd/).



[Prosody 0.12.2](https://blog.prosody.im/prosody-0.12.2-released/) et [Prosody 0.11.14](https://blog.prosody.im/prosody-0.11.14-released/) ont été publiées. La version 0.12 apporte des corrections de bogues et des améliorations.



[Le serveur Tigase XMPP 8.3 a été publié](https://tigase.org/blog/tigase-xmpp-server-8.3.0/). Elle inclut Tigase MEET - la version de Tigase des appels vidéo de groupe SFU (Selective Forwarding Unit), la prise en charge de la capacité de type de liaison de canal SASL XEP-0440 ainsi que la prise en charge initiale et anticipée de SASL2 et Bind2 et de nombreuses corrections habituelles.

## Bibliothèques et outils

[omemo_dart](https://github.com/PapaTutuWawa/omemo_dart) est une bibliothèque Dart destinée à aider les développeurs de clients XMPP Dart/Flutter à mettre en œuvre OMEMO dans sa dernière version - actuellement 0.8.3. Elle a été publiée dans la version 0.4.2.



[python-nbxmpp 4.0.0 à 4.1.0 a été publiée](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog). Ces versions apportent le support des Messages de Réaction (XEP-0444) et portent la bibliothèque vers libsoup3.



Un nouvel outil pour les opérateurs et développeurs de serveurs est arrivé : [nbxmpp-client](https://pypi.org/project/nbxmpp-client/) vous permet de vérifier et de tester différentes méthodes de connexion XMPP (et configurations de proxy) tout en gardant un œil sur le flux XML du protocole. La version 2.0.0 vient de sortir, avec un nouveau design (Gtk4+libadwaita).



[Slidge 0.1.0 RC1 a été publié](https://www.nicoco.fr/blog/2023/01/08/slidge-rc1/). Slidge est une collection de composants de passerelle XMPP qui vous permet d'utiliser vos clients XMPP préférés pour chatter avec d'autres réseaux de chat non XMPP et/ou non fédérés (c'est-à-dire WhatsApp, Facebook, Mattermost, Signal, Skype, Steam, Telegram).



Le service [compliance.conversations.im](https://compliance.conversations.im/) de Daniel Gultsch [va être abandonné](https://gultsch.social/@daniel/109653873511471850). Ce vérificateur de conformité en ligne permettait aux administrateurs de serveurs et aux utilisateurs d'identifier les XEP/caractéristiques prises en charge par un fournisseur, et il permettait également de vérifier la prise en charge des XEP dans le temps. Ce service a aidé les utilisateurs à vérifier s'ils créaient un compte à l'épreuve du temps avec un fournisseur de leur choix. En raison de difficultés à maintenir le logiciel, le service sera fermé dans un avenir proche.



[QXmpp 1.5](https://github.com/qxmpp-project/qxmpp/releases/tag/v1.5.0) est disponible ! La bibliothèque XMPP basée sur Qt-/C++ supporte désormais OMEMO 2, le Chiffrement de Contenu des Stanzas et la Gestion Automatique de la Confiance. Beaucoup plus de données qu'avec les anciennes versions d'OMEMO peuvent être chiffrées de bout en bout. Par exemple, les fichiers, y compris les vignettes, sont partagés de manière chiffrée via le Partage de Fichiers sans État. En outre, les réactions aux messages sont prises en charge et l'implémentation PubSub de QXmpp est presque complète.

# Extensions et spécifications

La XMPP Standards Foundation développe des extensions de XMPP dans sa [série de XEPs](https://xmpp.org/extensions/) en plus des [RFCs XMPP](https://xmpp.org/rfcs/).


Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent _finales_ ou _actives_ – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’_ajournées_. Ce cycle de vie est décrit dans la [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).

## Extensions proposées

Le processus de développement XEP commence par la rédaction d’une idée et sa soumission à l’Éditeur XMPP. Dans un délai de deux semaines, le Conseil décide s’il accepte cette proposition en tant que XEP _expérimentale_.



- [Suites de conformité XMPP 2023](https://xmpp.org/extensions/inbox/cs-2023.html)
  - Ce document définit les catégories d'applications XMPP pour différents cas d'utilisation (Core, Web, IM et Mobile), et spécifie les XEPs requises que les logiciels clients et serveurs doivent implémenter pour être conformes aux cas d'utilisation.
- [Annonces de Limites de Flux](https://xmpp.org/extensions/inbox/xep-sla.html)
  - Cette spécification définit un moyen pour une entité XMPP d'annoncer les limites qu'elle appliquera aux données reçues sur un flux.

## Nouvelles extensions

- [Version 0.1.0 de XEP-0477 (Chiffrement ciblé PubSub)](https://xmpp.org/extensions/xep-0477.html)
  - Accepté par vote du Conseil le 30/11/2022. (Éditeur XEP (jsc))
- [Version 0.1.0 de XEP-0476 (Signature PubSub : profil OpenPGP)](https://xmpp.org/extensions/xep-0476.html)
  - Accepté par vote du Conseil le 30/11/2022. (Éditeur XEP (jsc))
- [Version 0.1.0 de XEP-0475 (Signature PubSub)](https://xmpp.org/extensions/xep-0475.html)
  - Accepté par le vote du Conseil le 30/11/2022. (Éditeur XEP (jsc))
- [Version 0.1.0 de XEP-0471 (Événements)](https://xmpp.org/extensions/xep-0471.html)
  - Accepté par le vote du Conseil le 28/09/2022. (Éditeur XEP (jsc))
- [Version 0.1.0 de XEP-0474 (Protection contre la rétrogradation SASL SCRAM)](https://xmpp.org/extensions/xep-0474.html)
  - Accepté par vote du Conseil le 19/10/2022. (Éditeur XEP (jsc))
- [Version 0.1.0 de XEP-0473 (OpenPGP pour XMPP Pubsub)](https://xmpp.org/extensions/xep-0473.html)
  - Accepté par vote du Conseil le 19/10/2022. (Éditeur XEP (jsc))
- [Version 0.1.0 de XEP-0472 (Flux Social PubSub)](https://xmpp.org/extensions/xep-0472.html)
  - Accepté par le vote du Conseil le 19/10/2022. (Éditeur XEP (jsc))
  
## Extensions ajournées

Si une XEP _expérimentale_ n’est pas mise à jour pendant plus de douze mois, elle sera déplacée d’_expérimentale_ à _ajournée_. S’il y a une autre mise à jour, elle remettra la XEP à l'état d'_expérimentale_.

- Aucune XEP ajournée ce mois-ci.

## Extensions mises-à-jour

- [Version 0.2.0 de XEP-0474 (Protection contre la rétrogradation SASL SCRAM)](https://xmpp.org/extensions/xep-0474.html)
  - Ajout d'une description du modèle d'attaque
  - Ajout d'une section définissant l'interaction IETF (tm)
- [Version 0.2.0 de XEP-0461 (Réponses aux messages)](https://xmpp.org/extensions/xep-0461.html)
  - Correction de l'exemple de comptage des caractères. Ajout de la fonction disco. Assouplir les contraintes de l'attribut 'to' (nc)
- [Version 0.1.1 de XEP-0444 (Réactions aux messages)](https://xmpp.org/extensions/xep-0444.html)
  - Ajouter le schéma XML (egp)
- [Version 0.3.0 de XEP-0426 (Comptage des caractères dans les corps de messages)](https://xmpp.org/extensions/xep-0426.html)
  - Ajout d'une section sur les sous-séquences (lmw)
- [Version 0.5.0 de XEP-0353 (Initiation de Message Jingle)](https://xmpp.org/extensions/xep-0353.html)
  - Recommandation de l'utilisation de UUID v4 pour les attributs id. (tm)

## Dernier appel

Les _derniers appels_ sont émis une fois que tout le monde semble satisfait de l’état actuel d’une XEP. Après que le Conseil ait décidé que la XEP est prête, l’éditeur XMPP émet un dernier appel pour recueillir des commentaires. Les commentaires recueillis lors du dernier appel permettent d’améliorer la XEP avant de la renvoyer au Conseil pour qu’il passe à l’état _stable_.

- Pas de dernier appel ce mois-ci.

## Extensions stables

- Aucune XEP n’est passée à stable ce mois-ci.
  
## Extensions dépréciées



- Aucune XEP déclarée dépréciée ce mois-ci.

## Appel à l’expérience

Un _appel à l’expérience_ – comme un _dernier appel_ – est un appel explicite aux commentaires, mais dans ce cas, il s’adresse principalement aux personnes qui ont implémenté, et idéalement déployé, la spécification. Le Conseil vote ensuite pour la faire passer en version _finale_.

-   Pas d’appel à l’expérience ce mois-ci.

# Répandez la nouvelle !

Merci de partager la nouvelle sur d’autres réseaux :



* [Mastodon](https://fosstodon.org/@xmpp/)
* [Twitter](https://twitter.com/xmpp)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Lemmy instance](https://community.xmpp.net/)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)



Consultez également notre [Flux RSS](https://xmpp.org/feeds/all.atom.xml) !



Vous recherchez des offres d’emploi ou vous souhaitez engager un consultant professionnel pour votre projet XMPP ? Visitez notre [tableau d’offres d’emploi XMPP](https://xmpp.work/).

## Contributions et traductions de la lettre d’information



Il s’agit d’un effort communautaire, et nous aimerions remercier les traducteurs et traductrices pour leurs contributions. Les volontaires sont les bienvenus ! Les traductions de la lettre d’information XMPP seront publiées ici (avec un certain retard) :



- Anglais (original) : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Contributeurs généraux : **Alexander "PapaTutuWawa", emus, Licaon_Kter, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), wurstsalat, Zash** 
- Français : [jabberfr.org](https://news.jabberfr.org/category/newsletter/) et [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Traduction : **Adrien Bourmault (neox) et la communauté sur LinuxFR**
- Allemand : [xmpp.org](https://xmpp.org/categories/newsletter/) et [anoxinon.de](https://anoxinon.de/blog/)
  - Traduction : **Jeybe, wh0nix**
- Italien : [nicfab.it](https://www.nicfab.it/)
  - Traduction : **nicfab**
- Espagnol : [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Traduction : **daimonduff, TheCoffeMaker**

# Aidez-nous à créer la lettre d’information

Cette lettre d’information XMPP est produite collaborativement par la communauté XMPP. La lettre d’information de chaque mois est rédigé dans ce [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). À la fin de chaque mois, le contenu du pad est fusionné dans le [dépôt Github de la XSF](https://github.com/xsf/xmpp.org/milestone/3). Nous sommes toujours heureux d’accueillir des contributeurs et contributrices. N’hésitez pas à vous joindre à la discussion dans notre [salon public Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) et ainsi nous aider à soutenir cet effort communautaire. Vous avez un projet et vous voulez en parler ? Pensez à partager vos nouvelles ou vos événements ici, et à les promouvoir auprès d’un large public.



Tâches que nous effectuons régulièrement :



- collecte des nouvelles dans l’univers XMPP ;
- résumés *courts* des nouvelles et des événements ;
- résumé de la communication mensuelle sur les extensions (XEP) ;
- révision de l’ébauche de la lettre d’information ;
- préparation d’images pour les médias ;
- traductions ;
- communication via des comptes de médias.

# Licence

Cette lettre d’information est publiée sous la licence [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).

