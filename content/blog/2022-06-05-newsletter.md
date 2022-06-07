---
title: The XMPP Newsletter May 2022
date: 2022-06-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of May 2022.

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, especially throughout the current situation, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more at the bottom.

### Newsletter translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
- Italian: [nicfab.it](https://www.nicfab.it/)
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)

## XSF Announcements

![XSF and Google Summer of Code 2022](/images/logos/GSoC_2022_Logo.png "XSF and Google Summer of Code 2022")

- The Google Summer of Code 2022 is about to lift off and coding starts soon! Welcome the two new contributors Patiga and PawBud who will work on open-source software projects in the XMPP environment!
  - **Patiga** will work on [more flexible file transfers in Dino](https://summerofcode.withgoogle.com/programs/2022/projects/z9ixHTWZ). Mentors will be **fiaxh** and **Marvin W.** - many thanks to both of you!
  - **PawBud** will work towards [adding support for A/V communication via Jingle in ConverseJS](https://summerofcode.withgoogle.com/programs/2022/projects/0nRwZN19). Mentors will be **JC Brand** and **vanitasvitae** - many thanks to both of you, too!

  Feel free to spread the word via [Mastodon](https://fosstodon.org/@xmpp/108358826402429966) or [Twitter](https://mobile.twitter.com/xmpp/status/1529199174729728000). More details in our [designated page at xmpp.org](https://xmpp.org/community/gsoc-2022/).

- The current XSF member [voting period is ongoing](https://wiki.xmpp.org/web/Membership_Applications_Q2_2022). If you are an XSF member, please take your chance to vote. If your are interest to apply visit our [related page](https://xmpp.org/community/membership/).

## XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month

## Articles

Bifrost bridge fork at aria-net.org implemented offline messages support for matrix rooms accessed via the bridge
XMPP users connecting to Matrix rooms via Bifrost bridge did not get offline messages, because group chat (MUC) history support was not implemented in the XMPP server implementation of the 
bridge (based on xmpp-js). Thanks to great work done by Maranda, we can now have history and also message history (MAM) support for Matrix to XMPP bridged rooms. See [this post for complete instructions](https://opencollective.com/bifrost-mam/updates/maranda-from-aria-net-org-implements-mam-support-in-bifrost-bridge) to use this feature.

[The JMP Newsletter](http://blog.jmp.chat/b/may-newsletter-2022) announces a new release of the Cheogram Android client, SMS-only phone 
number ports, deeper integration with Snikket, and a [new project for social instance hosting](https://blog.jmp.chat/b/togethr-sopranica-social).

## Software news

### Clients and applications

[Gajim 1.4.0](https://gajim.org/post/2022-05-11-gajim-1.4.0-released/), [1.4.1](https://gajim.org/post/2022-05-21-gajim-1.4.1-released/), [1.4.2](https://gajim.org/post/2022-05-25-gajim-1.4.2-released/), and [1.4.3](https://gajim.org/post/2022-06-01-gajim-1.4.3-released/) have been released! After more than a year of development, it’s finally time to announce the release of Gajim 1.4! Gajim 1.4 series comes with a completely redesigned message window and conversation management. Workspaces allow you to organize your chats to keep matters separate where needed. These changes were only possible by touching a lot of Gajim’s code base, and we appreciate all the feedback we got from you.

![Gajim’s new user interface](/images/newsletter/2022-06/gajim-window-1-4.png "Gajim’s new user interface")

[Psi+ portable 11.5.1627 (2022-05-21)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/tehnick/) and [Psi+ installer 11.5.1629 (2022-05-31)](https://sourceforge.net/projects/psiplus/files/Windows/Personal-Builds/KukuRuzo/) have been released.

Go-sendxmpp [0.5.0](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.5.0) with Ox (OpenPGP for XMPP) improvements has been released, followed by a bugfix release [0.5.1](https://salsa.debian.org/mdosch/go-sendxmpp/-/releases/v0.5.1).

The Soprani.ca project has released a small tool hosted on their Cheogram infrastructure to [easily compute an equivalent Matrix ID for your Jabber ID](https://cheogram.com/matrix/) via known bridges.

![Cheogram ID conversion](/images/newsletter/2022-06/cheogram.png "Cheogram ID conversion")

## Servers

[ejabberd 22.05](https://www.process-one.net/blog/ejabberd-22-05/) has been released. This version includes five months of work, 200 commits, including many improvements (MQTT, MUC, PubSub, …) and bug fixes.

```erlang
mod_opt_type(bosh_service_url) ->
    econf:either(auto, econf:binary());
mod_opt_type(websocket_url) ->
    econf:either(auto, econf:binary());
mod_opt_type(conversejs_resources) ->
    econf:either(undefined, econf:directory());
mod_opt_type(conversejs_options) ->
    econf:map(econf:binary(), econf:either(econf:binary(), econf:int()));
mod_opt_type(conversejs_script) ->
    econf:binary();
mod_opt_type(conversejs_css) ->
    econf:binary();
mod_opt_type(default_domain) ->
    econf:binary().

mod_options(_) ->
    [{bosh_service_url, auto},
     {websocket_url, auto},
     {default_domain, <<"@HOST@">>},
     {conversejs_resources, undefined},
     {conversejs_options, []},
     {conversejs_script, auto},
     {conversejs_css, auto}].
```

[Jackal 0.60.0](https://github.com/ortuman/jackal) has been released.

## Libraries

[python-nbxmpp versions 3.0.0 to 3.1.0](https://dev.gajim.org/gajim/python-nbxmpp/-/blob/master/ChangeLog) have been released, bringing support for Message Moderation, Bookmarks extensions, and many bug fixes.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

By the way, xmpp.org features [a new page about XMPP RFCs](https://xmpp.org/rfcs/).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   No XEPs proposed this month.

### New

-   Version 0.1.0 of [XEP-0465](https://xmpp.org/extensions/xep-0465.html) (Pubsub Public Subscriptions)
    -   Accepted by vote of Council on 2022-04-13. (XEP Editor (jsc))
-   Version 0.1.0 of [XEP-0466](https://xmpp.org/extensions/xep-0466.html) (Ephemeral Messages)
    -   Accepted by vote of Council on 2022-05-03. (XEP Editor (jsc))

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   No XEPs deferred this month.

### Updated

-   Version 0.3 of [XEP-0365](https://xmpp.org/extensions/xep-0365.html) (Server to Server communication over STANAG 5066 ARQ)
    -   Make use of SLEP Streaming service, which was not available for 0.1. This provides a better service mapping than direct use of 5066 and provides compression. (sek)

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

-   No Last Call this month.

### Stable

-   No XEPs advanced to Stable this month.

### Deprecated

-   No XEP deprecated this month.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   No Call for Experience this month.

## Spread the news!

Please share the news on other networks:

* [Mastodon](https://fosstodon.org/@xmpp/)
* [Twitter](https://twitter.com/xmpp)
* [YouTube](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
* [Lemmy instance](https://community.xmpp.net/)
* [Reddit](https://www.reddit.com/r/xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)

{{< newsletter-subscribe >}}

Also check out our [RSS Feed](https://xmpp.org/feeds/all.atom.xml)!

Looking for job offers or want to hire a professional consultant for your XMPP project? Visit our [XMPP job board](https://xmpp.work/).

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Therefore, we would like to thank **Adrien Bourmault (neox), anubis, Anoxinon e.V., Benoît Sibaud, daimonduff, emus, Holger, Ludovic Bocquet, Licaon_Kter, Martin, mathieui, MattJ, nicfab, Pirate Praveen, Ppjet6, Sam Whited, singpolyma, TheCoffeMaker, wurstsalat, Ysabeau, Zash** for their support and help in creation, review, translation and deployment. Many thanks to all contributors and their continuous support!

Each month's newsletter issue is drafted in this [simple pad](https://yopad.eu/p/xmpp-newsletter-365days). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
