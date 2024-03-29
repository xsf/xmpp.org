---
title: Lettre d'information XMPP d'octobre 2022
date: 2022-11-05
categories: ['Newsletter']
---



Bienvenue dans la lettre d’information XMPP, nous sommes ravis de vous retrouver ici ! Ce numéro couvre le mois d’octobre 2022.



Comme la présente lettre d’information, de nombreux projets et leurs efforts au sein de la communauté XMPP sont le résultat du travail bénévole de personnes. Si vous êtes satisfait des services et des logiciels que vous utilisez, surtout dans la situation actuelle, pensez à dire merci ou à aider ces projets ! Vous souhaitez soutenir l’équipe de la lettre d’information ? Lisez la suite en bas de page.

# Contributions et traductions de la lettre d’information



Il s’agit d’un effort communautaire, et nous aimerions remercier les traducteurs pour leurs contributions. Les volontaires sont les bienvenus ! Les traductions de la lettre d’information XMPP seront publiées ici (avec un certain retard) :


- Anglais (original) : [xmpp.org](https://xmpp.org/categories/newsletter/)
    - Contributeurs généraux : **emus, Licaon_Kter, Ludovic Bocquet, MattJ, MSavoritias (fae,ve), wurstsalat, Zash** 
- Français : [jabberfr.org](https://news.jabberfr.org/category/newsletter/) et [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
    - Traducteurs : **Adrien Bourmault (neox), Benoît Sibaud, Ysabeau et anubis**
- Allemand : [xmpp.org](https://xmpp.org/categories/newsletter/) et [anoxinon.de](https://anoxinon.de/blog/)
    - Traducteurs : **Jeybe, wh0nix**
- Italien : [nicfab.it](https://www.nicfab.it/)
    - Traducteurs : **nicfab**
- Espagnol : [xmpp.org](https://xmpp.org/categories/newsletter/)
    - Traducteurs : **daimonduff, TheCoffeMaker**


# Annonces de la XSF


- La période de demande d’adhésion à XSF pour le quatrième trimestre 2022 est actuellement ouverte. Si vous souhaitez devenir membre de XSF, vous pouvez [demander l’adhésion](https://wiki.xmpp.org/web/Membership_Applications_Q4_2022). Veuillez soumettre votre demande avant le 27 novembre 2022.



## Google Summer of Code 2022


{{< figure src="/images/logos/GSoC_2022_Logo.png" caption="La XSF et le Google Summer of Code 2022" >}}


Le Google Summer of Code 2022 est terminé ! Les deux nouveaux contributeurs Patiga et PawBud ont travaillé sur des projets de logiciels libres dans l’environnement XMPP. Lisez les derniers billets de blog de la collection :


- **Patiga** travaillait sur [des transferts de fichiers plus flexibles dans Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ). Les mentors furent **fiaxh** et **Marvin W.**.
- [Projet GSoC sur le partage de fichiers sans état](https://dino.im/blog/2022/06/stateless-file-sharing-gsoc-project/)
- [Projet Partage de fichiers sans état : premières étapes](https://dino.im/blog/2022/06/project-stateless-file-sharing-first-steps/)
- [Partage de fichiers sans état : Implémentation de base](https://dino.im/blog/2022/08/stateless-file-sharing-base-implementation/)
- [Partage de fichiers sans état : Sources et compatibilité](https://dino.im/blog/2022/08/stateless-file-sharing-sources-and-compatibility/)
- **PawBud** travaillait sur [l'ajout d’un support pour la communication audiovisuelle via Jingle dans ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19). Les mentors étaient **JC Brand** et **vanitasvitae**.
- [Expérience d'intégration avec la XSF (Converse)](https://xmpp.org/2022/06/on-boarding-experience-with-xsf-converse/)
- [ConverseJS : Une vue approfondie de mon projet GSoC'22](https://xmpp.org/2022/07/conversejs-an-in-depth-view-into-my-gsoc22-project/)
- [Google Summer of Code 2022 à la XSF : Converse.js - Mise à jour de l’évaluation à mi-parcours](https://xmpp.org/2022/08/google-summer-of-code-2022-at-xsf-converse.js-mid-term-evaluation-update/)

## Hébergement fiscal de projets par la XSF



La XSF propose un [hébergement fiscal](https://xmpp.org/community/fiscalhost/) pour les projets XMPP. Veuillez postuler via [Open Collective](https://opencollective.com/xmpp). Pour plus d’informations, consultez l'[annonce blog](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Projets en cours :



- [Pont Bifrost : échange de messages hors ligne entre Matrix et XMPP](https://opencollective.com/bifrost-mam)
- [Coopérative Mellium](https://opencollective.com/mellium)


# Événements



- [Permanence XMPP](https://wiki.xmpp.org/web/XMPP_Office_Hours) : disponible sur notre [chaîne YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Rencontres XMPP à Berlin (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) : réunion mensuelle des passionnés de XMPP à Berlin, tous les deuxièmes mercredis du mois.
- [Capitole du Libre](https://capitoledulibre.org) : Des membres des associations « JabberFR » et « Libre en Communs » seront présents à Toulouse les 19 et 20 novembre.



# Articles



ejabberd a ajouté le [support du protocole Matrix](https://www.process-one.net/blog/matrix-protocol-added-to-ejabberd/), apportant son expérience de la mise à l’échelle de XMPP et MQTT à cette nouvelle voie de messagerie. Dans un premier temps, un sous-ensemble du protocole sera mis en œuvre, agissant comme un pont entre les protocoles. Les clients professionnels pourront d’abord y goûter, avant de l'intégrer à l’édition communautaire.



La [Lettre d’information JMP](https://blog.jmp.chat/b/october-newsletter-2022) présente une nouvelle version importante du client Cheogram pour Android, avec des fonctionnalités telles que XHTML-IM, Bits of Binary, une forme de rétraction des messages, le marquage des contacts, etc.  Ils parlent également d’une [intégration de canal XMPP qu’ils ont construite](https://github.com/chatwoot/chatwoot/pull/5587) pour le logiciel de support Chatwoot, et proposent aux projets communautaires d’utiliser leur instance pour l’essayer. Ce mois-ci, ils ont également écrit un article sur la [vérification de compte par SMS](https://blog.jmp.chat/b/2022-sms-account-verification) et son impact sur l’écosystème.



PGPainless : [Mise en œuvre de la validation de la séquence des paquets à l’aide d’automates Pushdown](https://blog.jabberhead.tk/2022/10/26/implementing-packet-sequence-validation-using-pushdown-automata/)



Une nouvelle technique de test automatisé a récemment été adoptée pour aider les développeurs de Prosody dans leur travail quotidien de développement : [Test de mutation dans Prosody](https://blog.prosody.im/mutation-testing-in-prosody/)



La modernisation du protocole d’authentification est en cours autour de la communauté, mot clé « SASL ». Les deux derniers bulletins d’information ont donné de multiples indications sur ce travail, dans les mises à jour de [libs](https://xmpp.org/2022/09/the-xmpp-newsletter-august-2022/#libraries) et de [XEP](https://xmpp.org/2022/10/the-xmpp-newsletter-september-2022/#updated) et dans les nouvelles de [funding](https://xmpp.org/2022/10/the-xmpp-newsletter-september-2022/#articles). Il concerne plusieurs clients, plusieurs plateformes et au moins un serveur. Thilo Molitor, le développeur de Monal, a parlé sur son blog de l’état _cassé_ actuel, des propriétés idéales du système et [des solutions sur lesquelles il travaille](https://monal-im.org/post/00004-sasl/). Il s’agit d’une lecture de 30 minutes, mais elle sera certainement utile lorsque d’autres nouvelles sur les implémentations SASL commenceront à apparaître des autres projets impliqués.


# Nouvelles des logiciels



## Clients et applications



ConverseJS a publié la [version 10.0.0](https://github.com/conversejs/converse.js/releases/tag/v10.0.0) avec de nombreuses améliorations et une mise à jour des fonctionnalités.



[Dino 0.3.1](https://github.com/dino/dino/releases/tag/v0.3.1) a été publié, il s’agit d’une version de maintenance pour le support de libsoup3 et la correction de bogues.



Les versions [Gajim 1.5.2](https://gajim.org/post/2022-10-08-gajim-1.5.2-released/) et [1.5.3](https://gajim.org/post/2022-10-31-gajim-1.5.3-released/) ont été publiées. Ces versions apportent une nouvelle amélioration des performances, de meilleurs emojis, la sélection de plusieurs messages, et de nombreuses corrections de bogues.


{{< figure src="/images/newsletter/2022-11-07/gajim-emoji-shortcodes.png" caption="Codes court pour emoji dans Gajim" >}}


[Profanity 0.13.1](https://github.com/profanity-im/profanity/releases/tag/0.13.1) est disponible avec une gestion améliorée des plugins.



[Psi+ 1.5.1641 (2022-09-24)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) a été publié.



Monal 5.3.3 est [en ligne dans l’AppStore](https://apps.apple.com/app/id317711500) depuis un moment maintenant, et même si elle n’apporte pas encore les améliorations SASL mentionnées ci-dessus ou les capacités d’appels audio et vidéo tant attendues [financées le mois dernier](https://xmpp.org/2022/10/the-xmpp-newsletter-september-2022/#articles), elle comporte plusieurs corrections pour les enregistrements, le partage de captures d’écran et les marqueurs de lecture.



aTalk a été publié avec [une cadence presque mensuelle](https://github.com/cmeng-git/atalk-android/blob/master/aTalk/ReleaseNotes.txt). Chaque nouvelle version apporte plus d’améliorations, comme les vues de localisation/carte, les appels, les mises à jour des bibliothèques et la mise à jour des nouvelles exigences d’Android. Le plus gros obstacle à son adoption reste malheureusement toujours présent et provient d’une interface utilisateur obsolète qui précède l’interface matérielle d’Android 5.



## Serveurs



La version [ejabberd 22.10](https://www.process-one.net/blog/ejabberd-22-10/) comprend six mois de travail, plus de 140 commits, y compris des améliorations pertinentes dans MIX, MUC, SQL, et les installateurs, et des corrections de bogues comme d’habitude.



[Jackal 0.62.3](https://github.com/ortuman/jackal/releases/tag/v0.62.3) est sortie apportant 3 corrections pour le stockage/archivage et les stances s2s.



## Bibliothèques et outils



[python-nbxmpp 3.2.4 et 3.2.5](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) ont été publiées, apportant des corrections de bogues et des améliorations internes.



# Extensions et spécifications



Les développeurs et développeuses, et autres experts ou expertes en normes du monde entier collaborent à ces extensions, en développant de nouvelles spécifications pour les pratiques émergentes et en affinant les façons de faire existantes. Proposées par n’importe qui, les plus réussies finissent Finales ou Actives – selon leur type – tandis que les autres sont soigneusement archivées en tant qu’Ajournées. Ce cycle de vie est décrit dans [XEP-0001](https://xmpp.org/extensions/xep-0001.html), qui contient les définitions formelles et canoniques des types, états et processus. [Pour en savoir plus sur le processus de normalisation](https://xmpp.org/about/standards-process.html). La communication autour des normes et des extensions se fait sur la [liste de diffusion des normes](https://mail.jabber.org/mailman/listinfo/standards) ([archive en ligne](https://mail.jabber.org/pipermail/standards/)).



Par ailleurs, xmpp.org propose également [une page sur les RFC XMPP](https://xmpp.org/rfcs/).



## Extensions proposées



Le processus de développement XEP commence par la rédaction d’une idée et sa soumission à l’éditeur XMPP. Dans un délai de deux semaines, le Conseil décide s’il accepte cette proposition comme un XEP expérimental.



- [PubSub Social Feed](https://xmpp.org/extensions/inbox/pubsub-social-feed.html)
- Cette spécification définit un moyen de publier du contenu social via XMPP.
- [SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/inbox/xep-downgrade-prevention.html)
- Cette spécification fournit un moyen de sécuriser les prises de contact SASL et SASL2 contre les déclassements de méthode et de liaison de canal.
- [OpenPGP pour XMPP Pubsub](https://xmpp.org/extensions/inbox/pubsub-encryption.html)
- Spécifie un profil OpenPGP pour XMPP (XEP-0373) pour le cas d’utilisation pubsub.


## Nouvelles extensions



- Pas de nouvelle XEP ce mois-ci.



## Extensions ajournées



Si une XEP expérimentale n’est pas mise à jour pendant plus de douze mois, elle sera déplacée d’_expérimentale_ à _ajournée_. S’il y a une autre mise à jour, elle remettra la XEP sur _expérimentale_.



- Aucune XEP ajournée ce mois-ci.



## Extensions mises-à-jour



- Aucune XEP mise-à-jour ce mois-ci.



## Dernier appel



Les derniers appels sont émis une fois que tout le monde semble satisfait de l’état actuel d’une XEP. Après que le Conseil ait décidé que la XEP est prête, l’éditeur XMPP émet un dernier appel pour recueillir des commentaires. Les commentaires recueillis lors du dernier appel permettent d’améliorer la XEP avant de la renvoyer au Conseil pour qu’il passe à l’état stable.



- Pas de dernier appel ce mois-ci.



## Extensions stables



- Aucune XEP n’est passée à stable ce mois-ci.



## Extensions dépréciées



- Aucune XEP dépréciée ce mois-ci.



## Appel à l’expérience



Un appel à l’expérience – comme un dernier appel, est un appel explicite aux commentaires, mais dans ce cas, il s’adresse principalement aux personnes qui ont implémenté, et idéalement déployé, la spécification. Le Conseil vote ensuite pour la faire passer en version finale.



- Pas d’appel à l’expérience ce mois-ci.



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



# Aidez-nous à construire la lettre d’information



Cette lettre d’information XMPP est produite en collaboration par la communauté XMPP. Nous tenons donc à remercier **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, cpm, daimonduff, emus, Gooya, Holger, *IM*, Ludovic Bocquet, martin, MattJ, MSavoritias (fae,ve), nicfab, Pierre Jarillon, Sam Whited, TheCoffeMaker, wh0nix, vanitasvitae, wurstsalat, Zash** pour leur soutien et leur aide à la création, la révision, la traduction et le déploiement. Un grand merci à tous les contributeurs et à leur soutien continu !



Le bulletin d’information de chaque mois est rédigé dans ce [simple pad](https://yopad.eu/p/xmpp-newsletter-365days). À la fin de chaque mois, le contenu du pad est fusionné dans le [dépôt Github XSF](https://github.com/xsf/xmpp.org/milestone/3). Nous sommes toujours heureux d’accueillir des contributeurs. N’hésitez pas à vous joindre à la discussion dans notre [salon public Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) et ainsi nous aider à soutenir cet effort communautaire. Vous avez un projet et vous voulez en parler ? Pensez à partager vos nouvelles ou vos événements ici, et à les promouvoir auprès d’un large public.


Tâches que nous effectuons régulièrement :



- collecte des nouvelles dans l’univers XMPP
- résumés *courts* des nouvelles et des événements
- résumé de la communication mensuelle sur les extensions (XEP)
- révision de l’ébauche de la lettre d’information
- préparation d’images pour les médias
- traductions

# Licence



Cette lettre d’information est publiée sous la licence [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
