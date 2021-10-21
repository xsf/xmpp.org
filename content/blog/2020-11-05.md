---
title: The XMPP Newsletter October 2020
date: 2020-11-05
author: emus
categories: ["Newsletter"]
aliases:
    - "/2020/10/newsletter-10-october/"
---

Welcome to the XMPP newsletter covering the month of October 2020.

### Newsletter translations

Translations of the XMPP Newsletter will be released here:

- French on [linuxfr.org](https://linuxfr.org/tags/xmpp/public) and [jabberfr.org](https://news.jabberfr.org/category/newsletter/)

## XSF Announcements

The XSF started the application period for its annual board & council elections. Applicants for the council must be elected XSF members, while board seats are open to everyone. If you are interested in applying for any of these positions please visit the [application page](https://wiki.xmpp.org/web/Board_and_Council_Elections_2020).

The Q4 2020 XSF membership application period is open as well. If you are interested to become an XSF member you can [apply](https://wiki.xmpp.org/web/Membership_Applications_Q4_2020) before 8th November.

## Articles

MongooseIM takes advantage of the extensibility of XMPP to allow its users to customise their solution based on their needs. A great example of this is their [case study with Pando Health](https://www.erlang-solutions.com/resources/case-studies.html#replacing-whatsapp-and-legacy-pagers-with-mongooseim-in-healthcare-29-doc), an award-winning chat system for health care that is now the most used offering in the United Kingdom National Health Service (NHS).

The DBJR (German Federal Youth Council) tries to educate their member organisations about open source and open standards. In our digital tools' blog, Jonah from the Kaidan project [wrote an article](https://tooldoku.dbjr.de/2020/10/kaidan-auf-dem-weg-zur-einfachen-sicheren-und-dezentralen-chat-app/) (German) for less tech-savvy people to explain why they develop Kaidan XMPP client.

When [Snikket](https://snikket.org/) launched back at FOSDEM 2020 in February its website was rather basic, so the team just added a blog section and the very first two posts expanding on the [introduction](https://snikket.org/blog/introducing-snikket/) and announcing the [Snikket CIC](https://snikket.org/blog/snikket-cic/), a legal company that backs Snikket. The post has the gritty legal details, but one thing stands out, it now allows Snikket to get funded via donations and grants. In good tradition there's also a [blog RSS feed](https://snikket.org/blog/index.xml) so you can stay up to date.

The IETF (yes, the Internet Engineering Task Force) deployed a trial instance of an XMPP service for their operational experience with local registration, guest account access, and provides a web client. These services are available at [xmpp-trial1.ietf.org](https://xmpp-trial1.ietf.org/). Great thanks to the XSF members supporting to make this happen! You can read more about the background and configuration of the deployment on the [Prosody blog](https://blog.prosody.im/xmpp-at-the-ietf/).

## Software news

### Clients and applications

[Gajim Development News](https://gajim.org/post/2020-10-28-development-news-october/): This October brings better message styling, XMPP link handling for Windows, and first improvements to get Voice/Video calls working again (but not yet compatible with Conversations, Siskin or Movim).

The Ignite Realtime Community has released [Spark 2.9.3 as a maintenance release](https://discourse.igniterealtime.org/t/spark-2-9-3-released/89016).

A new useful feature has been merged into Movim recently. It will also be part of the [upcoming 0.19 release](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/reply-to-chat-messages-a-new-movim-feature-coming-soon-dB0P1v). This change relies on the standard [XEP-0201: Best Practices for Message Threads](https://xmpp.org/extensions/xep-0201.html) and allows you to reply to a chat message using any XMPP account using Movim. On supported messages, click on the reply button and a little preview will appear next to the chat box input, fill in your message, publish, et voilà! There is also ongoing work [implementing SIP calling](https://twitter.com/MovimNetwork/status/1297570000790867974).

![Movim](/images/newsletter/october2020/movim_thread.png "Movim")

Pix-Art Messenger and blabber.im join together: The messenger will take over the [branding and layout from blabber.im](https://blabber.im/aus-pix-art-messenger-wird-blabber-im/) (German).

## Servers

Prosody had a minor release to [version 0.11.7 which also contains a security fix](https://blog.prosody.im/prosody-0.11.7-released/).

The MongooseIM team have released MongooseIM 4.0, the friendly Mongoose. This release makes MongooseIM more accessible and easy-to-use than ever before
with a TOML configuration, Kubernetes-ready Helm charts and structured logging. [See the full list of new and improved features in the blog post
accompanying MongooseIM 4.0 release](https://www.erlang-solutions.com/blog/what-s-new-in-mongooseim-4-0-the-friendly-mongoose.html). To celebrate the release of MongooseIM 4.0 the team put together [a guide to the common considerations companies go through when deciding on a chat solution](https://www.erlang-solutions.com/blog/the-complete-guide-to-instant-messaging-and-in-application-chat.html), this includes whether to build their own or buy a product-as-a-service
and what features users most commonly want.

Shortly after the release of [Openfire 4.5.4](https://discourse.igniterealtime.org/t/openfire-4-5-4-is-released/88896) there is also the release of [Openfire 4.6.0](https://discourse.igniterealtime.org/t/openfire-4-6-0-is-released/88971) already! The new release version contains improvements of Pubsub and PEP, federated multi-user chat for constrained environments (see [XEP-0289](https://xmpp.org/extensions/xep-0289.html)) as well as 80 closed issues!

## Other

The owner of the [joinxmpp.org](https://joinxmpp.org) domain is lacking time. They wrote a short description of the original goals and say they are now looking for somebody motivated to take on the project.

## Extensions and specifications

Developers and other standards experts from around the world collaborate on these extensions, developing new specifications for emerging practices, and refining existing ways of doing things. Proposed by anybody, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](https://xmpp.org/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. [Read more about the standards process](https://xmpp.org/about/standards-process.html).

### Proposed Extensions

The XEP development process starts by writing up an idea and submitting it to the XMPP Editor. Within two weeks, the Council decides whether to accept this proposal as an Experimental XEP.

-   No Proposed Extensions this month.

### New

-   Version 0.1.0 of [XEP-0444](https://xmpp.org/extensions/xep-0444.html) (Message Reactions)
    -   Accepted by vote of Council on 2020-10-07.

-   Version 0.1.0 of [XEP-0443](https://xmpp.org/extensions/xep-0443.html) (XMPP Compliance Suites 2021)
    -   Accepted by vote of Council on 2020-09-30.

### Deferred

If an experimental XEP is not updated for more than six months, it will be moved off Experimental to Deferred. If there is another update, it will put the XEP back onto Experimental.

-   [XEP-0353](https://xmpp.org/extensions/xep-0353.html) (Jingle Message Initiation)

-   [XEP-0292](https://xmpp.org/extensions/xep-0292.html) (vCard4 Over XMPP)

### Updated

-   Version 0.3 of [XEP-0371](https://xmpp.org/extensions/xep-0371.html) (Jingle ICE Transport Method)
    -   Replaced RFC 5245 with RFC 8445
    -   Introduced ice2 transport attribute for backward compatibility
    -   Clarified ICE restart procedure
    -   Clarified remote-candidate usage
    -   Changed remote-candidate notification procedure (sent all at once now)
    -   Replaced wrong reference to RFC 6455 with correct one: RFC 6544
    -   Allow sharing `<gathering-complete/>` element with remaining candidates

-   Version 1.3.0 of [XEP-0050](https://xmpp.org/extensions/xep-0050.html) (Ad-Hoc Commands)
    -   Clarify illegal uses of 'execute'.

-   Version 0.7.0 of [XEP-0384](https://xmpp.org/extensions/xep-0384.html) (OMEMO Encryption)
    -   Various fixes, clarifications and general improvements.

### Last Call

Last Calls are issued once everyone seems satisfied with the current XEP status. After the Council decides whether the XEP seems ready, the XMPP Editor issues a Last Call for comments. The feedback gathered during the Last Call help improving the XEP before returning it to the Council for advancement to Draft.

-   [XEP-0443](https://xmpp.org/extensions/xep-0443.html) (XMPP Compliance Suites 2021)

### Draft

-   Version 1.0.0 of [XEP-0411](https://xmpp.org/extensions/xep-0411.html) (Bookmarks Conversion)
    -   Accepted as Draft by vote of Council on 2020-10-14.

-   Version 1.0.0 of [XEP-0352](https://xmpp.org/extensions/xep-0352.html) (Client State Indication)
    -   Accepted as Draft as per Council vote from 2020-08-26.

-   Version 1.0.0 of [XEP-0393](https://xmpp.org/extensions/xep-0393.html) (Message Styling)
    -   Accepted as Draft as per Council vote from 2020-10-07.

### Call for Experience

A Call For Experience - like a Last Call, is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. The Council then votes to move it to Final.

-   [XEP-0363](https://xmpp.org/extensions/xep-0363.html) (HTTP File Upload)

## Thanks all!

This XMPP Newsletter is produced collaboratively by the XMPP community.

Thanks to edhelas, emus, erszcz, guusdk, licaon-kter, mwild1 and wurstsalat3000 for their help in creating it!

## Spread the news!

Please share the news on "social networks":

* [Twitter](https://twitter.com/xmpp)
* [Mastodon](https://fosstodon.org/@xmpp/)
* [LinkedIn](https://www.linkedin.com/company/xmpp-standards-foundation/)
* [Facebook](https://www.facebook.com/jabber/)
* [Reddit](https://www.reddit.com/r/xmpp/)

Find and place job offers in the [XMPP job board](https://xmpp.work/).

## Subscribe to the newsletter

We suggest you [Subscribe](https://tinyletter.com/xmpp) to receive the next editions in your inbox as soon as it is published! 
Promote this newsletter to whoever may be interested.

## Help us to build the newsletter

We started drafting every new issue in the [XSF Github repository](https://github.com/xsf/xmpp.org/pulls) and we are 
always happy to welcome contributors. Do not hesitate to join the discussion in our [Comm-Team group chat (MUC)](xmpp:commteam@muc.xmpp.org?join) 
and thereby help us sustain this as a community effort. 

You have a project and write about it? Please consider sharing your news or events here, and promote it to a large audience! 
Even if you can only spend a few minutes, these would already be helpful!

Tasks which need to be done on a regular basis are for example:

- Aggregation of news in the XMPP universe
- Short formulation of news and events
- Summary of the monthly communication on extensions (XEP)
- Review of the newsletter draft
- Preparation for media images
- Translations: especially German and Spanish

## License

This newsletter is published under [CC BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).
