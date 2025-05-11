---
title: O Boletim XMPP - Abril de 2025
date: 2025-05-05
categories: ['Newsletter']
---

{{< figure src="/images/newsletter/xmpp_newsletter_banner.jpg" caption="XMPP Newsletter Banner" >}}

Bem-vindo ao Boletim XMPP! É ótimo tê-lo de volta! 

Esta edição aborda o mês de abril de 2025.

Assim como o boletim mensal, muitos projetos e esforços da comunidade XMPP são resultado do trabalho voluntário de pessoas como você. Se está satisfeito com os serviços e softwares que utiliza, por que não agradecer ou ajudar esses
projetos? Interessado em apoiar a equipe do boletim mensal? Saiba mais [ao final](#help-us-to-build-the-newsletter).

## Comunicados da XSF

### Associação à XSF

Se você tem interesse em se tornar membro da XMPP Standards Foundation, [por favor candidatar-se até 18 de maio de 2025, às 00:00 (UTC)!](https://wiki.xmpp.org/web/Membership_Applications_Q2_2025).

### Projetos de Hospedagem Fiscal da XSF

A XSF oferece [gestão fiscal institucional](/community/fiscalhost/) para projetos XMPP. Canditate-se através do [Open Collective](https://opencollective.com/xmpp). Para mais informações, consulte o [post de anúncio no blog](/2021/09/the-xsf-as-a-fiscal-host/). Confira os projetos atuais que você pode apoiar:

- [Mellium Co-op](https://opencollective.com/mellium)
- [Bifrost bridge](https://opencollective.com/bifrost-mam)
- [Prav](https://opencollective.com/pravapp)
- [diasp.in](https://opencollective.com/diasp-in)

## Eventos XMPP

- [Berlin XMPP Meetup](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup) [DE / EN]: Encontro mensal de entusiastas de XMPP em Berlin, toda 2ª quarta-feira do mês, às 6:00 PM horário local.
- [XMPP Italian happy hour](https://video.xmpp-it.net/c/happyhour/videos) [IT]: Encontro online mensal da comunidade XMPP italiana, toda 3ª segunda-feira do mês, às 7:00 PM horário local (evento online e transmitido em tempo real).
- [XMPP Sprint in Berlin](https://wiki.xmpp.org/web/Sprints/2025-05_Berlin): Na sexta-feira, dia 23, sábado, dia 24 e domingo dia 25 de maio de 2025.

## Artigos sobre XMPP

- [XMPP Foundation Urges Meta to Allow Interoperability Under EU Rules](https://winbuzzer.com/2025/04/02/xmpp-pressures-meta-to-allow-interoperability-under-eu-rules-xcxwbn/) por [Markus Kasanmascheff](https://winbuzzer.com/author/markus/) por [winbuzzer.com](https://winbuzzer.com/)
- [Monocles](https://monocles.eu/more/), o projeto responsável pelo bate-papo Monocles [Web](https://monocles.chat/login) e pelo aplicativo para                             [Android](https://f-droid.org/en/packages/de.monocles.chat/) iniciou uma [campanha de financiamento](https://www.startnext.com/en/monocles). O objetivo principal é criar uma plataforma onde privacidade, soberania digital e sustentabilidade assumam um papel central. Sua privaciade não é negociável. A campanha vai de 28 de março até 30 de junho de 2025. 
- [Prav](https://prav.app) deu o segundo grande passo à caminho de formar uma sociedade vooperativa na Índia. O post no blog ["Finalising our bye-laws"](https://prav.app/blog/finalising-our-bye-laws/) traz detalhes sobre o processo, incluindo formas de ajudar. Trata-se de um passo importante na missão do Prav de implementar mecanismos coletivos de tomada de decisões para seus apps XPP e serviços, além conferir [fundamentação jurídica a esses mecanismos decisórios](https://prav.app/blog/why-register-a-coop/).

## Notícias de Software XMPP

### Clientes e Aplicativos XMPP

- [Cheogram](https://cheogram.com/) lançou sua versão [2.17.10-1](https://git.sr.ht/~singpolyma/cheogram-android/refs/2.17.10-1) para Android. Essa versão introduz uma implementação de Spaces ([XEP-503](https://xmpp.org/extensions/xep-0503.html)), além de outras melhorias, correções e mais!
- [Conversations](https://conversations.im/) lançou as versões [2.18.0](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.18.0), [2.18.1](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.18.1) e [2.18.2](https://codeberg.org/iNPUTmice/Conversations/releases/tag/2.18.2) para Android. Mudanças marcantes incluem a habilidade de escolher um local para fazer o backup, um opção de fazer backup e restaurar para [Quicksy](https://quicksy.im/), e suporte melhorado para mais tipos de  URIs. Este último inclui números de telefone `tel`, endereços de correio eletrônico `mailto` e, notavelmente, o esquema `web+ap` para ActivityPub proposto por [Fedi Links](https://fedilinks.org/).
- [Dino](https://dino.im/) lançou a versão [0.5](https://github.com/dino/dino/releases/tag/v0.5.0) com criptografia OMEMO por padrão, transferência de arquivos melhorada, pré-visualização de imagens e outros detalhes acerca de arquivos antes de efetuar o dowload, bem como dois diálogos totalmente repaginados. Veja o [blog post](https://dino.im/blog/2025/04/dino-0.5-release/) do lançamento para ter todos os detalhes.
  - Concomitantemente, Dino também [recebeu patrocínio](https://nlnet.nl/news/2025/20250422-announcement-grants-CommonsFund.html) da [NLnet](https://nlnet.nl) para dar início ao desenvolvimento de diversas novas funcionalidade. Isso inclui moderação de mensagens nas conversas em grupo, remoção de mensagens locais, gerenciamento de conexão moderno com FAST e SASL2, outras opções de formatação com Message Markup e muito mais! [Visite a página do projeto](https://nlnet.nl/project/Dino-UX/) para ter todos os detalhes.
- [Gajim](https://gajim.org/) lançou as versões [2.1.0](https://gajim.org/post/2025-04-08-gajim-2.1.0-released/) e [2.1.1](https://gajim.org/post/2025-04-17-gajim-2.1.1-released/) com uma nova página para 'Activity feed', melhorias no layout do diálogo 'Iniciar Chat'e  suporte à funcionalidade de 'Message Display Synchronisation' ([XEP-0490](https://xmpp.org/extensions/xep-0490.html)) através de conversar em grupo, dentre outras melhorias e correção de bugs. Dê um pulo no site deles, sob a secção [News](https://gajim.org/post/) para encontrar todos os detalhes.

{{< figure src="/images/newsletter/2025-05-05/gajim-activity-feed.png" caption="Activity feed in Gajim 2.1" >}}

{{< figure src="/images/newsletter/2025-05-05/gajim-account-select.png" caption="Account and status selection in Gajim 2.1" >}}

- [Kaidan](https://www.kaidan.im/) recebeu financiamento [NLnet](https://nlnet.nl)  para [diversas melhorias abrangentes](https://nlnet.nl/project/Kaidan-MUC/), com destaque para conversas em grupo e OMEMO legado. O segundo ponto é relevante, porque enquanto Kaidan usa a versão mais recente do protocolo de criptografia ponta a ponta OMEMO, outros aplicativos populares, incluindo Conversations, Monal e Dino ainda estão usando uma versão antiga. Sendo as duas incompatíveis, significa que usuários de Kaidan não podiam usar criptografia OMEMO como a maioria dos usuários de outros aplicativos. Ao implementar specificações antingas, Kaidan ajudará a preencher essa lacuna.

- [Monocles Chat 2.0.6](https://codeberg.org/monocles/monocles_chat/releases/tag/CodebergRelease-v2.0.6) foi lançado para o sistema operacional Android. Esta versão inclui suporte à legendas de arquivos, a opção de fixar ao topo uma conversa não-criptografada, suporte para lista de provedores e a opção de registrar em seu próprio servidor XMPP, além de outras funcionalidades e melhorias.

{{< figure src="/images/newsletter/2025-05-05/monocles-pin-message.png" caption="Monocles Chat 2.0.6: Initial captions to files and pin message to the top" >}}

{{< figure src="/images/newsletter/2025-05-05/monocles-providers.png" caption="Monocles Chat 2.0.6: Register on your own XMPP server or pick one from the providers list" >}}
 
- [Movim](https://movim.eu/) lançou a versão [0.30](https://mov.im/community/pubsub.movim.eu/Movim/good-news-everyone-movim-0-30-encke-is-there-xMvYPr) (códinome "[Encke](https://en.wikipedia.org/wiki/Comet_Encke)"), a maior evolução do Movim em muitos anos! Este lançamento lançamento traz [chamadas com mútiplos participantes](https://movim.eu/#visio), visibilidade das reações nas mensagens detalhadas, suporte para Unicode 15.1 com uma fartura de emojis novos para usar e avatares que mudam quando um contato adiciona ao seu [Story](https://movim.eu/#stories).

{{< figure src="/images/newsletter/2025-05-05/movim-visio.jpg" caption="Movim 0.30 (Encke): Multi Participant Calls. Bob Cat looking disgruntled by the presence of the 'Hooman' on the lower right of the screen!" >}}

{{< figure src="/images/newsletter/2025-05-05/movim-visio-phone.jpg" caption="Movim 0.30 (Encke): Meow OwO bedazzled by the looks of Multi Participant Calls on his mobile device!" >}}

  - e em seu encalço, [Movim](https://movim.eu/) lançou sua primeira atualização de correções: versão [0.30.1](https://mov.im/community/pubsub.movim.eu/Movim/here-comes-the-new-movim-release-encke-0-30-1-ckTLY4), adicionando suporte a imagens animadas no proxy de imagens, um novo Painel de Configuração de Avatar e Banner, além de implementar a ([XEP-0392](https://xmpp.org/extensions/xep-0392.html)) geração consistente de cores, dentre muitas outras melhorias e correções. Não deixe de conferir o anúnico oficial em [Movim Blog](https://mov.im/community/pubsub.movim.eu/Movim) para ver todos os detalhes!

{{< figure src="/images/newsletter/2025-05-05/movim-avatar-panel.png" caption="Movim 0.30.1: Avatar and banner configuration panel" >}}

- [Prose](https://prose.org/) lançou versões [0.8.0](https://github.com/prose-im/prose-app-web/releases/tag/0.8.0), [0.8.1](https://github.com/prose-im/prose-app-web/releases/tag/0.8.1), [0.8.2](https://github.com/prose-im/prose-app-web/releases/tag/0.8.2), [0.8.3](https://github.com/prose-im/prose-app-web/releases/tag/0.8.3), [0.9.0](https://github.com/prose-im/prose-app-web/releases/tag/0.9.0), [0.9.1](https://github.com/prose-im/prose-app-web/releases/tag/0.9.1) e [0.10.0](https://github.com/prose-im/prose-app-web/releases/tag/0.10.0) de seu frontend na web [prose-web-app](https://github.com/prose-im/prose-app-web).

### Servidores XMPP

- [MongooseIM](https://www.erlang-solutions.com/technologies/mongooseim/) lançou a versão [6.3.3](https://github.com/esl/MongooseIM/releases/tag/6.3.3) de sua Solução Corporativa de Mensagens Instantâneas. Esta pequena atualização inclui várias melhorias e correções. Para maiores informações, confira a [documentação](https://esl.github.io/MongooseDocs/6.3.3).
- [ProcessOne](https://www.process-one.net/) publicou [ejabberd 25.04](https://www.process-one.net/blog/ejabberd-25-04/). Esse lançamento traz uma importante correção de segurança, correçoes de bugs um novo comando API.
- [Prosody IM](https://prosody.im/) tem o prazer de apresentar a versão [13.0.1](https://blog.prosody.im/prosody-13.0.1-released/), uma nova versão secundária (minor release) da=o branch estável mais recente. Esta atualização corrige alguns bugs importantes descobertos após o último lançamento. Leia todos os detalhes no [changelog](https://prosody.im/doc/release/13.0.1). Como sempre, instruções detalhadas de instalação e download estão disponíveis na [página de download](https://prosody.im/download/) para sua conveniência.
- O [app Prosody para  YunoHost](https://github.com/YunoHost-Apps/prosody_ynh) foi atualizado para forner suporte a diversos [XEPs](https://raw.githubusercontent.com/YunoHost-Apps/prosody_ynh/refs/heads/master/xmpp_compliance) por padrão, configurado para todos os usuários YunoHost em somente um click. [YunoHost](https://yunohost.org/) é um conjunto de ferramentas que permitem administrar com facilidade os serviços que você hospeda e, apesar de no passado vir originalmente distribuido com o Metronome, uma derivação do Prosody, recentemente passou a distribuir sua funcionalidade XMPP em um "app" separado, para que as pessoas possam usar outro servidor XMPP de sua escolha.

### Bibliotecas e Ferramentas XMPP

- [go-xmpp](https://github.com/xmppo/go-xmpp) versões [0.2.13](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.13) e [0.2.14](https://github.com/xmppo/go-xmpp/releases/tag/v0.2.14) foram lançadas.
- [libomemo-c](https://github.com/dino/libomemo-c) versão [0.5.1](https://github.com/dino/libomemo-c/releases/tag/v0.5.1) foi lançada.
- [prose-core-client](https://github.com/prose-im/prose-core-client) versões [0.1.103](https://github.com/prose-im/prose-core-client/releases/tag/0.1.103), [0.1.104](https://github.com/prose-im/prose-core-client/releases/tag/0.1.104) e [0.1.105](https://github.com/prose-im/prose-core-client/releases/tag/0.1.105) foram lançadas.
- [python-nbxmpp](https://dev.gajim.org/gajim/python-nbxmpp) versões [6.1.0](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/6.1.0) e [6.1.1](https://dev.gajim.org/gajim/python-nbxmpp/-/releases/6.1.1) foram lançadas.
- [Slidge](https://codeberg.org/slidge/slidge#readme) versões [0.2.9](https://codeberg.org/slidge/slidge/releases/tag/v0.2.9) (codinome "Trixie <3"), [0.2.10](https://codeberg.org/slidge/slidge/releases/tag/v0.2.10), [0.2.11](https://codeberg.org/slidge/slidge/releases/tag/v0.2.11) e [0.2.12](https://codeberg.org/slidge/slidge/releases/tag/v0.2.12) foram lançadas.
- [Tinder](https://www.igniterealtime.org/projects/tinder/) versão [2.1.0](https://github.com/igniterealtime/tinder/releases/tag/tinder_2_1_0) foi lançada.
- [Whack](https://www.igniterealtime.org/projects/whack/) versão [3.0.0](https://github.com/igniterealtime/Whack/releases/tag/v3.0.0) foi lançada.

## Extensões e Especificações

A XMPP Standards Foundation desenvolve extensões ao XMPP em sua [Série XEP](/extensions/) além dos [RFCs XMPP](/rfcs/). Desenvolvedores e outros especialistas em padrões técnicos de todo o mundo colaboram nessas extensões, desenvolvendo novas especificações para práticas emergentes, bem como refinando a práticas já existentes. As extensões podem ser propostas por qualquer pessoa e as bem-sucedidas eventualmente se tornam Final ou Active - dependendo de seu tipo - enquanto outras são cuidadosamente arquivadas como Deferred.
Este ciclo está descrito [XEP-0001](/extensions/xep-0001.html), que contém as definições formais e canônicas dos tipos, estados e processos. [Leia mais sobre o processo dos standards](/about/standards-process.html). Comunicação acerca dos standards e de suas extensões dão-se pelo [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([arquivo online](https://mail.jabber.org/pipermail/standards/)).

### Novos

- Não há XEPs novos nesse mês.

### Propostos

O processo desenvolvimento de um XEP começa pela elaboração de uma ideia e seu envio ao [Editor XMPP](/about/xsf/editor-team/). Dentro de duas semanas, o [Conselho](/about/xmpp-standards-foundation/#council) decide se aceita a proposta como uma XEP Experimental.

- Não há XEPs propostos nesse mês

### Diferidos

Caso um XEP experimental não seja atualizado por mais de doze meses, será movido de Experimental para Diferido. Caso haja alguma outra atualização, retornará ao status Experimental.

- Nenhum XEP foi diferido nesse mês.

### Atualizados

- Versão 1.1.3 do [XEP-0313](https://xmpp.org/extensions/xep-0313.html) (Message Archive Management)
  - Corrigiu erros de digitação (XEP Editor (dg))
- Versão 0.4.0 do [XEP-0377](https://xmpp.org/extensions/xep-0377.html) (Spam Reporting)
  - Adicionou adesão voluntária ao processo de relatoria de spam.
  - Adicionou Guus der Kinderen com coautor. (gdk)
- Versão 1.0.1 do [XEP-0421](https://xmpp.org/extensions/xep-0421.html) (Identificação do usuário para MUCs semi-anônimos)
  - Corrigiu erros de digitação (XEP Editor (dg))
- Versão 0.3.0 do [XEP-0455](https://xmpp.org/extensions/xep-0455.html) (Status de Indisponibilidade do Serviço)
  - Removeu toda sinalização em banda de eventos. (mp)

### Última Chamada

As últimas chamadas são feitas quando todos parecem satisfeitos com o atual estado do XEP. Depois do [Conselho](/about/xmpp-standards-foundation/#council) decidir se o XEP parece prontos, o [Editor XMPP](/about/xsf/editor-team/) publica uma Última Chamada para comentários. As opiniões e comentários coletados durante a Última Chamada podem ajudar a melhorar o XEP antes de sua devolução ao Conselho e posterior promoção ao status de Estável. 

- Nenhuma Última Chamada nesse mês.

### Estável

- Nenhum XEP foi movido ao status de estável nesse mês.

### Deprecada

- Nenhum XEP deprecado nesse mês. 

### Rejeitada

- Nenhuma XEP foi rejeitado nesse mês. 

## Compartilhe as notícias!

Por favor compartilhe essas notícias em outras plataformas:

- [Mastodon](https://fosstodon.org/@xmpp/)
- [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
- [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Instância Lemmy (não oficial)](https://slrpnk.net/c/xmpp)
- [Reddit (não oficial)](https://www.reddit.com/r/xmpp/)
- [Página XMPP no Facebook (não oficial)](https://www.facebook.com/jabber)

{{< newsletter-subscribe >}}

Também dê uma olhada nos nossos [Feeds RSS](/feeds/all.atom.xml)!

Procurando trabalho ou quer contratar um consultor profissional para seu projeto XMPP? Visite nosso [portal de empregos XMPP](https://xmpp.work/).


- Inglês (original): [xmpp.org](/categories/newsletter/)
  - Colaboradores gerais: *Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, Badri Sunderarajan, Benson Muite, cal0pteryx, emus, Federico, Gonzalo Raúl Nemmi, Jonas Stein, Kris "poVoq", Licaon_Kter, Ludovic Bocquet, Mario Sabatino, melvo, MSavoritias (fae,ve), nicola, Schimon Zachary, Simone Canaletti, singpolyma, XSF iTeam*
- Françês: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Tradutores: *Adrien Bourmault (neox), alkino, anubis, Arkem, Benoît Sibaud, mathieui, nyco, Pierre Jarillon, Ppjet6, Ysabeau*
- Italiano: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Tradutores: *nicola*
- Espanhol: [xmpp.org](/categories/newsletter/)
  - Tradutores: *Gonzalo Raúl Nemmi*
- Alemão: [xmpp.org](/categories/newsletter/)
  - Tradutores: *Millesimus*
- Português: [xmpp.org](/categories/newsletter/)
  - Tradutores: *Paulo*

## Ajude-nos a Construir o Boletim XMPP

Esse Boletim XMPP é produzido de forma colaborativa pela comunidade XMPP. O boletim de cada mês é rascunhado neste [simples pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). Ao final de cada mês, o conteúdo do pad é adicionado ao [repositório XSF GitHub](https://github.com/xsf/xmpp.org/milestone/3). Ficamos sempre felizes em receber colaboradores! Não hesite em participar da discussão em nosso [chat Comm-Team (MUC)](xmpp:commteam@muc.xmpp.org?join) e assim ajude-nos a sustentar esse esforço coletivo. Você tem um projeto e quer compartilhar as novidades? Por favor considere compartilhar suas notícias ou eventos aqui e alcance um grande público. 

Tarefas que executamos com frequência:

- clipping de notícias do universo XMPP
- *breves* resumos das notícias e eventos
- resumo das comunicações mensais referentes à extensões (XEPs)
- revisão do rascunho do boletim mensal
- preparação de imagens para a redes sociais
- traduções
- comunicação via redes sociais

## Cancelamento da Inscrição ao Boletim Mensal

Para cancelar sua inscrição, [por favor faça login](https://mail.jabber.org/accounts/login/?next=/postorius/lists/newsletter.xmpp.org/).
Caso não tenha feito o login anteriormente, talvez tenha de criar uma conta com o endereço de e-mail correspondente.

## Licença

Este boletim é publicado sob a [licença CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).

