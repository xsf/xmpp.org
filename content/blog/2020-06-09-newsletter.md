---
title: XMPP@home - 9 June 2020
date: 2020-06-09
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/06/newsletter/"
---

Welcome to the XMPP newsletter covering the month of May 2020.

## Subscribe to the newsletter

We suggest you [Subscribe](https://tinyletter.com/xmpp) to receive the next editions in your inbox as soon as it is published! Promote this newsletter to whoever may be interested.

## Help us to build the newsletter

We started drafting every new issue in the [XSF Github repository](https://github.com/xsf/xmpp.org/pulls). 
And we are always happy to welcome contributors. Just join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) and thereby help us sustain this as a community effort. 

You have a project and (want to) write about it? Please consider sharing your news or events here, and promote it to a large audience! Even if you can only spend a few minutes, these would already be helpful.

Tasks which need to be done on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the draft
- Translations: especially French, German and Spanish


### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- [German](https://www.jabber.de/)
- [French](https://linuxfr.org/tags/xmpp/public)
- [Spanish](https://www.jabber.de/)

## Software releases

It has been almost a year since the release of Gajim 1.1.3. A year of developing new features, cleaning up old code, and fixing bugs. This month, it is finally the time for a [first beta release of Gajim 1.2](https://gajim.org/post/2020-05-08-gajim-1.2.0-beta1-released/). Highlights are (amongst others): improved group chat system, completely rewritten network code, and a new account creation assistant. But there is much more to discover.

Log in:
![Gajim 1.2.0-beta1 log in](https://gajim.org/img/news/account-creation-1.png)

Sign up:
![Gajim 1.2.0-beta1 sign up](https://gajim.org/img/news/account-creation-2.png)

Create account:
![Gajim 1.2.0-beta1 create account](https://gajim.org/img/news/account-creation-3.png)

### Clients and applications

[Gajim Development News May 2020](https://gajim.org/post/2020-05-26-development-news-may/): New account badges and the great plugin overhaul. In preparation of the upcoming 1.2 release, many plugins have been revisited. Check out the new file preview!

Goffi released [Salut à Toi progress note for calendar week 21](https://www.goffi.org/b/kmebCba3m38dr9sgzgGrkp/progress-note)!

[Poezio](https://poez.io) released 0.13.0 and 0.13.1 which now requires python 3.7. These versions bring Poezio into the club of OMEMO supporting clients and also enable HTTP upload via dedicated plugins. Check the full [changelog](https://lab.louiz.org/poezio/poezio/-/blob/master/CHANGELOG) to look at all the improvements of these versions.

[Biboumi](https://biboumi.louiz.org/), the XMPP/IRC gateway, was released in version 0.8.5, fixing compilation issues with GCC 10.

The python based XMPP automatic file sender [Errol has been updated to v2.0.1](https://blog.agayon.be/errol_update1.html) which modernizes its async I/O calls and adds more privacy. By moving from 'aionotify' to the better maintained 'watchdog', Errol theoretically extends its support (from Linux only) to Windows, Mac OS X and FreeBSD.

## Services

blabber.im now [supports IPv6](https://blabber.im/blabber-im-ist-nun-ipv6-tauglich/). The service operators created an [invitation link which works for their server but also for every other ID](https://blabber.im/en/i-moved/). If you moved to an XMPP based chat client, you can now conveniently put this link into the status of your previous non-XMPP chat clients. This link offers your contacts all the necessary infos to be able to reach you and (if they want to) follow you into the XMPP world.

![Jabber.org](https://www.jabber.org/jabber.png)

jabber.org migrates its server to Prosody. [Stay informed!](https://www.jabber.org/notices.html)

yaxim.org rolled out [new anti-spam measures](https://yaxim.org/blog/2020/05/12/new-anti-spam-measures/). You may be interested in the '[The Jabber Spam Fighting Manifesto](https://github.com/JabberSPAM/jabber-spam-fighting-manifesto)', too.

## Libraries

The XMPP library for Python 3.7+, [Slixmpp](https://lab.louiz.org/poezio/slixmpp), was [updated to version 1.5.0](https://mail.jabber.org/pipermail/jdev/2020-May/090424.html), with minor releases 1.5.1 and 1.5.2. The [changelog]( https://lab.louiz.org/poezio/slixmpp/-/tags/slix-1.5.0) shows improvements of numerous XEPs and preliminary support for OMEMO.

Quite some time has past since the last official Smack release. Now there are some very early alpha releases of Smack 4.4.
Among additional support for more than a dozen new XEPs, the new release will contain a new architecture for modular transports, as well as a modified API that applies the builder pattern to stanza types.
A date for the final release is not yet known, but it is now time to give feedback to make sure to get your changes into the next stable Smack release!
[Read the detailed list of changes](https://github.com/igniterealtime/Smack/wiki/Smack-4.4-Readme-and-Upgrade-Guide).

## Google Summer of Code

Since beginning of May students all over the world are working on many open-source projects within the Google Summer of Code Season. We would like to introduce the students who work on [GSoC XMPP projects](https://summerofcode.withgoogle.com/organizations/5474262808264704/#6018598289539072) and share their first blog posts:

[Aditya Borikar](https://adiaholic.github.io/gsoc2020/2020/05/16/Chapter-0-Introduction.html) is working on WebSocket support for Smack. Blog history: 
- [Chapter 1: Handshake](https://adiaholic.github.io/gsoc2020/2020/05/24/Chapter-1-Handshake.html)
- [Chapter 2: Modular Shift](https://adiaholic.github.io/gsoc2020/2020/05/31/Chapter-2-Modular-Shift.html)

[Anmol (wolfie_anmol)](https://wolfieanmol.github.io/gsoc-blog/) is working on implementing Real Time Texting in Dino ([XEP-0301](https://xmpp.org/extensions/xep-0301.html)). Blog history:
- [GSoC 2020 begins - Introduction to RTT](https://wolfieanmol.github.io/gsoc-blog/introduction/)
- [RTT stanza and message comparision](https://wolfieanmol.github.io/gsoc-blog/rtt-stanza-and-message-comparision/)

Thank you for joining GSoC XMPP projects and keep up the good work! To be continued.

## Extensions and specifications

### Updated

- Version 0.4.0 of [XEP-0414](https://xmpp.org/extensions/xep-0414.html) (Cryptographic Hash Function Recommendations
for XMPP)
  - Make Blake2b-256 SHOULD and Blake2b 512 MUST (rion)

- Version 1.1.0 of [XEP-0402](https://xmpp.org/extensions/xep-0402.html) (PEP Native Bookmarks)
  -Add schema + other editorial changes (mb)

- Version 0.5.0 of [XEP-0389](https://xmpp.org/extensions/xep-0389.html) (Extensible In-Band Registration)
  -Overhaul document for readability.
  -Add JID and username information to success element.
  -Always require disco/caps feature.
  -More examples. (ssw)

- Version 1.3.0 of [XEP-0068](https://xmpp.org/extensions/xep-0068.html) (Field Standardization for Data Forms)
  -Clarify field type handling of the FORM_TYPE field on submission forms. (fs)

- Version 0.2.0 of [XEP-0436](https://xmpp.org/extensions/xep-0436.html) (MUC presence versioning)
  -Incorporate feedback from the standards list
  -Create a separate tag for sending the version number.
  -Include a reset token.
  -Remove the "Additional measures" section and merge parts into "Requirements".
  -Mandate that presences are always sent for affiliated users. (jcb)

- Version 0.2.0 of [XEP-0437](https://xmpp.org/extensions/xep-0437.html) (Room Activity Indicators)
  -Assign urn:xmpp namespace instead of xmpp:prosody.im namespace (this was missed during acceptance) (XEP Editor (jsc))

- Version 0.1.1 of [XEP-0438](https://xmpp.org/extensions/xep-0438.html) (Best practices for password hashing and storage)
  -Fix reference to external document (ssw)

- Version 1.2.0 of [XEP-0167](https://xmpp.org/extensions/xep-0167.html) (Jingle RTP Sessions)
  -Introduce `<rtcp-mux/>` element to signal the ability to multiplex RTP Data and Control Packets. (dg)

- Version 2.10.0 of [XEP-0004](https://xmpp.org/extensions/xep-0004.html) (Data Forms)
  -Clarify that fields which are not required may be omitted on submission. (fs)

### Proposed

The XMPP Extensions Editor has received proposals for new XEPs.

- [SASL Channel-Binding Type Capability](https://xmpp.org/extensions/inbox/xep-sasl-cb-types.html)
  -This specification allows servers to annouce their supported SASL channel-binding types to clients.

- [Channel Binding Pseudomechanisms](https://xmpp.org/extensions/inbox/cb-pseudomechanisms.html)
  -A method for advertising and negotiating types of channel binding supported by SCRAM based SASL mechanisms.

### Miscellaneous

**Experimental**

- Version 0.1.0 of [XEP-0439](https://xmpp.org/extensions/xep-0439.html) (Quick Response)
  -Quickly respond to automated messages.
  -Accepted by vote of Council on 2020-04-22. (XEP Editor (jsc))

- Version 0.1.0 of [XEP-0437](https://xmpp.org/extensions/xep-0437.html) (Room Activity Indicators)
  -This specification describes a lightweight mechanism for activity notifications in MUCs
  -Accepted by vote of Council on 2020-04-15. (XEP Editor (jsc))

- Version 0.1.0 of [XEP-0436](https://xmpp.org/extensions/xep-0436.html) (MUC presence versioning)
  -This specification defines a versioning mechanism which reduces the amount of presence traffic in a XEP-0045 MUC
  -Accepted by vote of Council on 2020-04-01. (XEP Editor (jsc))

**Draft**

- Version 1.0.0 of [XEP-0320](https://xmpp.org/extensions/xep-0320.html) (Use of DTLS-SRTP in Jingle Sessions)
  -Move to Draft as per Council vote from 2020-05-20. (XEP Editor (jsc))

- Version 1.0.0 of [XEP-0339](https://xmpp.org/extensions/xep-0339.html) (Source-Specific Media Attributes in Jingle)
  -Move to Draft as per Council vote from 2020-05-20. (XEP Editor (jsc))


## Thanks all!

This XMPP Newsletter is produced collaboratively by the community.

Thanks to emus, nyco, pmaziere, SouL, vanitasvitae, wurstsalat3000 for their help in creating it!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
