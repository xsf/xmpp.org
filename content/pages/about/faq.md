---
Title: FAQ
Url: about/faq
Save_as: about/faq.html
Parent_id: about
Top_menu_show: false
Top_Menu_order: -1
Dropdown_menu_show: false
Footer_show: false
Sidebar_menu_show: true
Sidebar_menu_title: About XMPP
Sidebar_menu_size: 7
Sidebar_menu_elem_name_1: History
Sidebar_menu_elem_url_1: about/history
Sidebar_menu_elem_name_2: Overview
Sidebar_menu_elem_url_2: about/technology-overview
Sidebar_menu_elem_name_3: Myths & Legends
Sidebar_menu_elem_url_3: about/myths
Sidebar_menu_elem_name_4: Standards Process
Sidebar_menu_elem_url_4: about/standards-process
Sidebar_menu_elem_name_5: The XSF
Sidebar_menu_elem_url_5: about/xmpp-standards-foundation
Sidebar_menu_elem_name_6: Specifications
Sidebar_menu_elem_url_6: extensions/index
Sidebar_menu_elem_name_7: FAQ
Sidebar_menu_elem_url_7: about/faq
Content_layout: multiple-columns
---

## What is XMPP?

XMPP is a powerful, open, secure, standards-based protocol. It is a freely-available technology for real-time communication, which powers a wide range of applications including instant messaging, presence, collaboration, voice and video calling, Internet of Things, tactical military messaging, mobile cloud push, and more.

That's like the chat network? Right?

Right! There is a federated chat network running on XMPP, consisting of thousands of servers owned by enterprises, hosting companies, and individual users.

But XMPP is also well suited to machine-to-machine signalling systems, and other use-cases where internet-wide federation isn’t important. For example, Joachim (one of our members) has developed an internet-of-things system that uses XMPP to control everything from heating systems to multi-coloured lights.

But the two can be combined - the XSF has run demonstrations of controlling light-bulbs over the existing federated chat network.

## Who owns XMPP?

XMPP is an open technology, so the simple answer is: no one.

It is not a programming language, or a tool you can download and use. You can’t buy it or pay for a licence to use it.

It is a protocol (a set of standards) that the XMPP Standards Foundation maintains. There is also an active community of open-source and commercial developers who produce a wide variety of XMPP-based software.

In essence, XMPP belongs to the vibrant community that develops and cares for it.

## Who uses XMPP?

Google use it for their Google Cloud Messaging. Facebook use it for Facebook Chat integration. NATO use it for tactical chat. Thousands of companies use it for their enterprise instant messaging. Millions of devices use it to interconnect. The IETF use it in their meetings. One of our Board members uses it to talk to his mother.

## How can I use XMPP?

If you aren’t already using XMPP (chances are, you are; you just didn’t know it) then you can access all the technical resources you need [here](/software).

Anyone can put together their own XMPP service and easily federate with other organisations' implementations. Because XMPP is an open protocol, implementations can be developed using any software license; although many server, client, and library implementations are distributed as free and open-source software, numerous freeware and commercial software implementations also exist - and they’ll all work together.

## Where did XMPP come from?

XMPP is the name for the streaming XML protocol that emerged from the Jabber open source community in 1999. When that community submitted the protocol to the Internet Engineering Task Force (IETF) in 2002, it chose to use the name “XMPP” instead of “Jabber” to eliminate the possibility of confusion with the open source community and the commercial Jabber.com company (since acquired by Cisco Systems, Inc.)

You can read more about the history of XMPP [here](/about/history.html).

## How secure is XMPP?

Security is a moving target, and a vague term. In general terms, XMPP security is substantially better than web security, both from a capability standpoint and the deployed base, and the community is highly active in this area.

XMPP has had its security vetted by the experts at the IETF, and so has native support for pluggable authentication (via SASL) and leading-edge security (via TLS). Moreover, XMPP has been leading the charge on deployment, too - most XMPP client stacks will support SCRAM, for example, and projects like the [IM Observatory](http://xmpp.net) are pushing the community toward better security. The deployed base of XMPP on the internet is seeing the beginnings of DNSSEC deployment, with some DANE records available.

In terms of end-to-end security, though there has been deployment of OTR and other proprietary extensions, the XMPP community has yet to settle on a particular method. This is in part because of the security benefits of being able to run your own server, which heavily mitigate against the attacks end-to-end cryptography would prevent - remember, XMPP servers talk to each other and your client across heavily encrypted links.

## What's wrong with Skype/WhatsApp/Google Hangouts/whatever? Why should I use XMPP?

If every contact you want to talk to is on Skype already, and you only want to talk to people using whatever facilities Skype offers, then Skype is the one for you.

If you only need to talk to people on mobile handsets who already have WhatsApp, then that’s perfect for you.

Google Hangouts actually still has XMPP under the hood in places, but similar rules apply.

The interesting question is where you need something more. Maybe your contacts all want to run their own server. Maybe you need better security. Maybe you need to exchange arbitrary data. Maybe you’re not happy with one company knowing all your secrets.

## How many users are there in the community?

With both an open protocol and a distributed network, that’s almost an impossible question to answer. We know that for the server at jabber.org, there are several thousand servers connected, but there’s no way of telling how many users exist on the network.


## What’s the XSF?

[The XMPP Standards Foundation](/about/xmpp-standards-foundation.html) is a non-profit organization which acts as a central point for the maintenance of the existing specifications, and the creation of new ones. It’s a membership organization, made of volunteers who help run the standards process.

There’s no need to join to work on the specifications, nor to develop with XMPP, but volunteers willing to help work on how standards are made are always welcome.
