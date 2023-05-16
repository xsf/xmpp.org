---
title: The XMPP Newsletter May 2023
date: 2023-05-05
categories: ['Newsletter']
---

Welcome to the XMPP Newsletter, great to have you here again! This issue covers the month of May 2023.
Many thanks to all our readers and all contributors!

Like this newsletter, many projects and their efforts in the XMPP community are a result of people’s voluntary work. If you are happy with the services and software you may be using, please consider saying thanks or help these projects! Interested in supporting the Newsletter team? Read more [at the bottom](#help-us-to-build-the-newsletter).

## XSF Announcements

- If you are interested to become an [XSF member](https://xmpp.org/community/membership/) you can apply during Q3 2023 soon.

### XMPP and Google Summer of Code 2023
The XSF has been [accepted again as hosting organisation at the GSoC 2023 and receive two slots for XMPP Contributors](https://xmpp.org/2023/02/xmpp-at-google-summer-of-code-2023/)!

{{< figure src="/images/logos/gsoc-2023-logo.svg" caption="XSF and Google Summer of Code 2023" >}}

## Add GSoC Projects

### XSF fiscal hosting projects

The XSF offers [fiscal hosting](https://xmpp.org/community/fiscalhost/) for XMPP projects. Please apply via [Open Collective](https://opencollective.com/xmpp). For more information, see the [announcement blog post](https://xmpp.org/2021/09/the-xsf-as-a-fiscal-host/). Current projects:

- [Bifrost bridge: Offline messages exchange between Matrix and XMPP](https://opencollective.com/bifrost-mam)
- [Mellium Co-op](https://opencollective.com/mellium)

## XMPP Events

- [XMPP Office Hours](https://wiki.xmpp.org/web/XMPP_Office_Hours): available on our [YouTube channel](https://www.youtube.com/channel/UCf3Kq2ElJDFQhYDdjn18RuA)
- [Berlin XMPP Meetup (remote)](https://mov.im/?node/pubsub.movim.eu/berlin-xmpp-meetup): monthly meeting of XMPP enthusiasts in Berlin, every 2nd Wednesday of the month
- [FOSSY](https://fossy.us) will have an XMPP track at their conference this summer.
- [XMPP Italian happy hour](https://tube.nicfab.eu/w/3KJMxZPYxRXQDAhXySZgLf): monthly Italian XMPP web meeting, starting May 16th and then every third Tuesday of the month at 7:00 PM. Online event, with web meeting mode and live streaming.

## Articles

_It’s really helpful if you try to give a short summary (<5 lines) of your contribution or of what the link you’re posting is offering. You 
don’t need to write in a formal tone - just be passionate about why this motivates you or about what you are working on!_

## Software news
### Clients and applications

_It’s really helpful if you try to give a short summary (<5 lines) of your contribution or of what the link you’re posting is offering. You 
don’t need to write in a formal tone - just be passionate about why this motivates you or about what you are working on!_

### Servers

_It’s really helpful if you try to give a short summary (<5 lines) of your contribution or of what the link you’re posting is offering. You 
don’t need to write in a formal tone - just be passionate about why this motivates you or about what you are working on!_

### Libraries & Tools

_It’s really helpful if you try to give a short summary (<5 lines) of your contribution or of what the link you’re posting is offering. You 
don’t need to write in a formal tone - just be passionate about why this motivates you or about what you are working on!_


## Extensions and specifications

The XMPP Standards Foundation develops extensions to XMPP in its [XEP series](https://xmpp.org/extensions/) in addition to [XMPP RFCs](https://xmpp.org/rfcs/).

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html). Communication around Standards and Extensions happens in the [Standards Mailing List](https://mail.jabber.org/mailman/listinfo/standards) ([online archive](https://mail.jabber.org/pipermail/standards/)).

### Proposed

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to 
accept this proposal as an Experimental XEP.

- No XEPs proposed this month.

### New

- No new XEPs this month.

### Deferred

If an experimental XEP is not updated for more than twelve months, it will be moved off Experimental to Deferred. If there is another update, it 
will put the XEP back onto Experimental.

- No XEPs deferred this month.

### Updated

- [Version 0.2.0 of XEP-0444 (Message Reactions)](https://xmpp.org/extensions/xep-0444.html)
  - Add emoji rejection mechanism. (NC)
- [Version 0.7.0 of XEP-0359 (Unique and Stable Stanza IDs)](https://xmpp.org/extensions/xep-0359.html)
  - Add security consideration regarding spoofability and reference example (fs)
- [Version 0.12.0 of XEP-0292 (vCard4 Over XMPP)](https://xmpp.org/extensions/xep-0292.html)
  - Removes raw-IQ mode and specifies the reuse of PEP (spw)
- [Version 0.4.0 of XEP-0388 (Extensible SASL Profile)](https://xmpp.org/extensions/xep-0388.html)
  - Bump namespace
  - Add reference to XEP-0440 and RFC 5802
  - Update security considerations and business rules
  - Clarify `<continue/>` and tasks
  - Add expansion point to inline stream resumption and BIND2 (and possibly others)
  - Add optional `<user-agent/>` element
  - Move from Deferred to Experimental
- [Version 0.4.0 of XEP-0386 (Bind 2)](https://xmpp.org/extensions/xep-0386.html)
  - Various changes, made in parallel with working client and server implementation experience, and SASL2 updates.
  - More tightly define the integration with XEP-0388 and several session feature XEPs: XEP-0198, XEP-0280, XEP-0352.
  - Replace the custom latest-id element with the new metadata element from XEP-0313, which also provides richer information.
  - Drop unread tracking, as this is a deep topic not directly related to resource binding. Instead the details of integration with other extensions have been better defined and demonstrated, to allow such functionality when it is fully defined and exists.
  - Adjust proposed namespace on aesthetic grounds and consistency with SASL2's approach. As this protocol may become part of the new preferred connection flow for a long time to come, it makes no sense to include the redundant and potentially confusing '2' when there is no conflict without it. Similarly, the '.0' has been dropped from the XEP's title, as it isn't really a version number.
  - Allow the client some influence over the resulting resource identifier, and define a standard format for these combined identifiers.
  - Specify that servers should terminate old sessions from a client when it binds a new resource.
- [Version 0.2.0 of XEP-0428 (Fallback Indication)](https://xmpp.org/extensions/xep-0428.html)
  - Add 'for' attribute such that entities can discover what the fallback is for.
  - Allow to specify that only one of `<subject>` or `<body` is meant as a fallback.
  - Allow to specify the part of respective text that is meant as fallback where applicable.
  - Don't use encryption example, which should use XEP-0380 instead.

### Last Call

Last calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Stable.

- No Last Call this month.

### Stable

- No XEP moved to stable this month.

### Deprecated

- No XEP deprecated this month.

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

### Newsletter Contributors & Translations

This is a community effort, and we would like to thank translators for their contributions. Volunteers are welcome! Translations of the XMPP Newsletter will be released here (with some delay):

- English (original): [xmpp.org](https://xmpp.org/categories/newsletter/)
  - General contributors: **Adrien Bourmault (neox), Alexander "PapaTutuWawa", Arne, emus, Licaon_Kter, Ludovic Bocquet, melvo, MSavoritias (fae,ve), wurstsalat, XSF iTeam**
- French: [jabberfr.org](https://news.jabberfr.org/category/newsletter/) and [linuxfr.org](https://linuxfr.org/tags/xmpp/public)
  - Translators: **Adrien Bourmault (neox), alkino, anubis, Benoît Sibaud, nyco, Pierre Jarillon, Ppjet6, Ysabeau**
- German: [xmpp.org](https://xmpp.org/categories/newsletter/) and [anoxinon.de](https://anoxinon.de/blog/)
  - Translators: **Jeybe, wh0nix**
- Italian: [notes.nicfab.eu](https://notes.nicfab.eu)
  - Translators: **nicfab**
- Spanish: [xmpp.org](https://xmpp.org/categories/newsletter/)
  - Translators: **daimonduff, TheCoffeMaker**

## Help us to build the newsletter

This XMPP Newsletter is produced collaboratively by the XMPP community. Each month's newsletter issue is drafted in this [simple pad](https://pad.nixnet.services/oHnY_ZvLT8SoFyCqIC2ung). At the end of each month, the pad's content is merged into the [XSF Github repository](https://github.com/xsf/xmpp.org/milestone/3). We are always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. You have a project and want to spread the news? Please consider sharing your news or events here, and promote it to a large audience.

Tasks we do on a regular basis:

- gathering news in the XMPP universe
- *short* summaries of news and events
- summary of the monthly communication on extensions (XEPs)
- review of the newsletter draft
- preparation of media images
- translations
- communication via media accounts

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
