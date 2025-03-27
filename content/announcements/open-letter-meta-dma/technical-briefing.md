---
title: "Detailed technical briefing: The Case for XMPP – Why Meta Must Embrace True Messaging Interoperability"
layout: single_open_letter_meta_dma
date: 2025-03-27
author: XMPP Standards Foundation
---

## Introduction

The European **[Digital Markets Act (DMA)](https://digital-markets-act.ec.europa.eu/about-dma_en)** was introduced to ensure fair competition and prevent large technology companies from exploiting their dominant positions. A key aspect of the DMA is the requirement for **Number-Independent Interpersonal Communication Services (NIICS)**—which includes messaging platforms like WhatsApp and Messenger—to provide true interoperability with third-party services. This requirement is essential to breaking down walled gardens, promoting user choice, and fostering a more competitive digital ecosystem.

The **[XMPP Standards Foundation](https://xmpp.org/about/xmpp-standards-foundation/)** has been closely following the implementation of the Digital Markets Act (DMA) in the European Union, with a specific focus on **messaging interoperability**. As an organization dedicated to open messaging standards, we are committed to helping stakeholders navigate the principles and technical realities of interoperable messaging.

For over 25 years, we have developed and refined the **eXtensible Messaging and Presence Protocol (XMPP)**—a robust, extensible, and open standard that has fostered messaging interoperability worldwide. The XSF, through its membership requirements, and XMPP as a whole, by way of the distributed extensibility of the protocol, are independent of any vendor. Some of our members have been involved since XMPP’s inception in 1999, and several have already provided guidance to the European Union, serving as neutral experts to highlight the extensive resources and expertise our Foundation has cultivated.

However, we now feel compelled to raise our voice more strongly. The direction taken by major gatekeepers of proprietary messaging networks raises serious concerns. Their proposed interoperability solutions appear, at best, as half-measures designed to maintain the status quo and, at worst, as deliberate strategies to reinforce their market dominance under the guise of compliance.

Meta, designated as a [gatekeeper under the DMA](https://digital-markets-act.ec.europa.eu/gatekeepers_en), is the only company in the messaging sector subject to these new interoperability requirements, given its control over WhatsApp and Messenger. Yet, Meta’s current DMA proposal falls short of the European Union’s objectives. Instead of fostering true interoperability, it risks further entrenching Meta’s dominance—strengthening its hold on user data and reinforcing network effects that stifle competition.

With this open letter, we call for a course correction—one that ensures genuine competition and user choice in the messaging space, benefiting individuals, businesses, and the broader digital ecosystem.

## The Role of the XMPP Standards Foundation in the Rise of XMPP

As stated on the XSF website:

> The XMPP Standards Foundation (also known as the XSF and formerly the Jabber Software Foundation) is an independent, nonprofit standards development organisation whose primary mission is to define open protocols for presence, instant messaging, and real-time communication and collaboration on top of the IETF’s Extensible Messaging and Presence Protocol (XMPP).
>
> The XSF also provides information and infrastructure to the worldwide community of Jabber/XMPP developers, service providers, and end users.

### Origins and Early Development

In 1999, the goal of the original designers of XMPP was to create an open specification that would enable the emergence of a fully interoperable, federated messaging network. These designers took a pragmatic approach, ensuring that the protocol supported a transition period by supporting server-side bridging. This gateway feature enabled users to merge their legacy communication accounts—at the time primarily ICQ, Yahoo! Messenger, and Microsoft Messenger—into XMPP (then still known as Jabber) as a pivot format. The development and the maintaince of the gateways would happen on the server to adapt to quick change of protocol, but also to ensure the client could use multiple accounts in the most efficient way.

This [Jabber initiative was a success](https://xmpp.org/about/history/). Developers from around the world contributed to making messaging interoperability a reality. As a result, multiple compliant servers and clients were developed, many of them as Open Source software, leading to the emergence of a vast federated network spanning thousands of domains.

### Standardization and Industry Adoption

XMPP was submitted to the **Internet Engineering Task Force (IETF)** and officially became a standard in 2004 under the XMPP name with the publication of **RFC 3920 and RFC 3921**.

Several internet service providers across Europe, including **Libertysurf, SAPO, and 1&1**, deployed XMPP-based clients and services. The protocol gained further momentum in 2005 when **Google Talk** adopted XMPP in a federated setup, enabling large-scale messaging interoperability.

In **May 2008**, **Facebook announced the launch of an XMPP interface** for its Chat service, allowing users to connect via **standard desktop XMPP clients**. While Facebook's internal protocol differed, it still provided a [standards-based Jabber/XMPP interface](https://web.archive.org/web/20100318030410/https://developers.facebook.com/news.php?blog=1&story=361). At the time, **Facebook's XMPP chat documentation** was fully available on its developer pages, reinforcing the significance of XMPP in mainstream communication services ([archived documentation](https://web.archive.org/web/20111006161206/https://developers.facebook.com/docs/chat/)).

In **2009**, **Google placed XMPP at the core of its collaborative editing tool, Google Wave**, further demonstrating the protocol’s adaptability beyond instant messaging. Meanwhile, **social networks across the world embraced XMPP**, with notable implementations by **Yandex in Russia** and **StudiVZ in Germany**.

### A Proven Standard for Messaging Interoperability

XMPP has played a crucial role in shaping the modern messaging landscape. Its success demonstrates that **true interoperability is achievable through open, federated protocols**, and that major technology companies—including Google and Facebook—have previously recognized its value. As the DMA now mandates interoperability for messaging services, XMPP remains the most viable and battle-tested solution to meet these requirements.

## Smartphones, WhatsApp, and the Gatekeeping Strategy

Despite XMPP’s success, technical advantages, and suitability for messaging interoperability, its adoption slowed as the messaging landscape evolved. The shift toward proprietary platforms coincided with the rise of smartphones, which led to growing financial stakes in messaging services and increased efforts by dominant players to consolidate control over their networks.

### The Shift to Mobile and the Rise of Proprietary Networks

In **2007**, Apple launched the iPhone, ushering in the smartphone era and the widespread adoption of mobile internet. By **2009**, the introduction of both the App Store and push notification services paved the way for the launch of **WhatsApp**. Messaging, which had previously been limited to SMS on mobile, quickly became a **rich and ubiquitous communication tool**.

WhatsApp took a strategic approach by leveraging a public resource—the phone number system—as a unique user identifier. Combined with easy access to users’ phone contacts in modern smartphone operating systems, and starting out as an **XMPP service with a locked-in client**, WhatsApp was able to build an extensive **proprietary** messaging network. In essence, it **became the new ICQ**, but at an even larger scale. As the service grew, it positioned itself **in direct competition with mobile carriers**, as **over-the-top (OTT) messaging**—services that bypass traditional carrier networks by leveraging the open internet. At the time, **net neutrality** was seen as a safeguard ensuring that carriers could not abuse their control over communication infrastructure, but it also allowed closed proprietary messaging services to thrive.

### The Pivotal Year: 2014 and the Rise of Messaging Gatekeeping

The year **2014** marked a critical turning point—one that was especially significant for Meta (formerly Facebook). That year:

- **Facebook acquired WhatsApp for $19 billion**, despite the company's financial losses, signaling the strategic importance of controlling messaging at scale.
- **Facebook deprecated XMPP support in Facebook Messenger** and in **2015, completely removed its XMPP-based interoperability tool**.

When Facebook eliminated XMPP support, they simultaneously [announced the Messenger Platform at their F8 conference](https://developers.facebook.com/blog/post/2015/03/25/introducing-messenger-platform-and-businesses-on-messenger/), introducing a new ecosystem where **businesses could engage with users under Facebook’s controlled environment**. The move to deprecate XMPP was not a technical necessity but a strategic decision—by restricting APIs and interoperability, Facebook ensured that businesses had no choice but to operate within its platform, using its own tools, while Facebook retained complete control over user engagement and data monetization.

### The Consequences: A Fully Closed Messaging Landscape

Facebook was not alone in this strategy, but it played an **instrumental role in locking down messaging communication** before full interoperability could be realized. What makes this situation even more frustrating is that:

- **Facebook Messenger originally supported XMPP**.
- **WhatsApp has always been built on an XMPP-based server**—its **internal logic remains rooted in XMPP**, yet it operates as a completely closed system.
- Both used the same open source XMPP server to bootstrap their infrastructure.

As a result, we have **regressed to a fragmented messaging landscape reminiscent of 1999**, before the emergence of federated interoperability. Today, **multiple closed messaging ecosystems compete to dominate the communication space**, including:

- **Facebook Messenger**
- **WhatsApp**
- **Instagram private messaging**
- **Telegram**
- **WeChat**
- **LinkedIn Messaging**
- **Various Google messaging services**
- And many more

Each of these services **operates in isolation**, forcing users to either create accounts on multiple platforms to stay in touch with all their contacts or rely on a single provider—driving further concentration in the sector. If a user chooses to focus on just one app, they must convince all their contacts to do the same, effectively reinforcing a **global-scale monopoly** in communication.

### Beyond Messaging: The Broader Lock-In of Communication

What is worst, is that this issue is no longer limited to text-based messaging. Modern messengers have expanded to **voice and video calls**, effectively **controlling digital communication as a whole**. If we do not change course, the endgame is clear, as we are stuck in a race toward a **global monopoly on internet communication**, where a handful of gatekeepers could dictate their terms, limiting competition and user freedom.

## The European Commission and the Digital Markets Act

To prevent extreme concentration of power in the messaging sector, the **European Commission included it firmly within the scope of the Digital Markets Act (DMA)**. Its goal is to ensure that communication remains **open, fair, and competitive**, preventing a future where global messaging is controlled by a **monopoly, duopoly, or, at best, an oligopoly**. Enforcing interoperability is the only way to allow users to **freely choose their preferred messaging provider** rather than being locked into dominant platforms.

In this spirit—enabling a truly **competitive market** where users can select messaging providers that align with their **budget, business model, and privacy preferences**—we must return to the **core principle of interoperability: the adoption of open communication standards**.

This is the intent behind the DMA’s requirements.

## Why the XSF is Concerned About Meta’s Proposal and Why XMPP is the Solution

Now that Meta has submitted its proposal for messaging interoperability to the European Commission, we have serious concerns that their approach could not only **preserve the status quo** but also **give Meta even more control over user data**.

### Key Concerns with Meta’s Interoperability Proposal

#### 1. Restrictive Access Through NDAs and Agreements

Meta requires companies to **sign a non-disclosure agreement (NDA)** to access their interoperability detailed documents and likely demands an agreement before enabling interoperability between networks. This effectively **keeps companies in a gatekeeper relationship**, just as Meta did when launching *Messenger for Businesses* to control interactions and ensure benefits flowed primarily to them. 

For competitors, **signing an agreement with Meta grants them disproportionate leverage** due to their massive user base. This is **not true interoperability**—it is a **negotiated privilege**, reinforcing Meta’s dominant position.

Requiring an NDA **prevents non-profit organizations like the XSF** from evaluating or contributing to the interoperability mechanism. It **blocks open-source developers from implementing interoperability** in their software, severely limiting innovation.

#### 2. API-Based Approach Instead of Open Protocols

Meta’s proposal appears to be based on **APIs rather than open protocols**. This is a fundamental problem because:

- **Protocols** are designed for **interoperability and cooperation**, ensuring long-term stability.
- **APIs** are controlled by the provider and offer a **limited set of features**, with associated **usage limits, fees, and restrictions** that can change over time.

The industry has already seen the dangers of relying on APIs—as seen with Twitter, Facebook, and Reddit, where API access was restricted or monetized, disrupting their entire ecosystems. **No sustainable business or long-term project can be built on API access alone.**

#### 3. Client-Side Approach Risks User Tracking

Meta’s approach appears to **force external users to behave as if they are Meta users**, meaning:

- Their **identifiers** would exist within Meta’s system.
- Through the metadata flowing to their platform, **Meta could track external users**, even if they are not Meta users.
- If **phone numbers are required as identifiers**, it would enable **cross-platform tracking** and **user matching**, further consolidating Meta’s data collection practices.

This raises serious privacy concerns, particularly for users who explicitly **do not want to be part of Meta’s ecosystem**.

#### 4. The Scalability Problem: API Bridges Do Not Work

Relying on APIs for interoperability is inefficient and **does not scale**. Consider this scenario:

- If a messaging service wants to interoperate with 10 providers, it must **develop and maintain 10 separate API bridges**.
- This approach is **not sustainable**, as the cost and maintenance overhead would deter smaller players from participating.
- Worse, **platforms could exploit this loophole to avoid true interoperability**. For example, if Meta and Telegram each offer APIs but neither is willing to implement the other's API, they can both claim they are open to interoperability—while **ensuring that nothing actually happens**. This **completely undermines the intent of the DMA**.

### Understanding federation: A Telephone Analogy: Why Meta’s Approach is Flawed

This is why the **XMPP Standards Foundation (XSF) steps in** and propose to enable interoperability on federation principles which are at the hearth of the Internet majors protocols and allowed it to stay open.

To better understand the shortcomings of Meta’s proposal, we can compare it to another essential communication system: **the global phone network**.

Today, phone networks are **interoperable and federated**. No matter which provider you use, you can call anyone on another network—whether it's a landline or mobile service. **You do not need an account with every provider to communicate.** This seamless federation is possible because:

1. **A standardized common protocol** ensures universal communication.
2. **A distributed ID attribution system** allows calls to be routed correctly between providers.

The **same model can and should be applied to messaging interoperability**. 

The XMPP Standards Foundation has already done the heavy lifting: by **adopting the XMPP S2S (server-to-server) protocol as the interoperability standard**, we can **achieve the same seamless communication in messaging**.

## Interoperability Through XMPP Federation

The most effective approach to achieving interoperability is **federation**. This is the principle that underpins **email** and **decentralized federated social networks**, such as those using **ActivityPub (e.g., Mastodon)** or custom approaches like **Bluesky**.

Meta argues against **messaging federation**, claiming that they need to **protect their users from spam, abuse, and security threats**. While user protection is important, this **does not mean federation is inherently unsafe**. In fact, **XMPP was designed with these concerns in mind**—its goal is to support a **sustainable, global-scale federated messaging network** with **built-in security, moderation, and control mechanisms**.

### How Federation Works

In a federated system, a user identifier consists of **two components**:

1. **The domain name** – This serves as the **first level of routing** for messages and interactions, much like an email address (e.g., `user@domain123.eu`). It ensures that messages are **delivered to the correct provider**.
2. **The username, identifier, or key** – This is assigned by the domain’s provider and **routes communication internally** to the specific user. Importantly, **it does not need to expose private information** and can be processed internally to **protect user privacy**.

Federation enables **server-to-server (s2s) communication**, providing a **flexible and privacy-focused** solution for interoperability. With email, knowing a public address (e.g., `user@domain123.eu`) allows communication **without exposing sensitive details** like the user phone number. The same principle applies to federated protocols like **XMPP and ActivityPub**.

### How Federation Enhances Security & Control

A common misconception is that **federation compromises security**. In reality, **federation offers strong safeguards** while still allowing **providers to enforce moderation and control**. 

Federated systems use a **clear separation between internal and external communication**:

1. **Client-to-Server (c2s) Protocol** – Manages communication between **a provider and its internal users**. Users authenticate through this endpoint with their credentials.
2. **Server-to-Server (s2s) Protocol** – Handles **external communication between providers**, ensuring that **internal user traffic remains isolated** from external threats.

This gives all providers, including Meta, the opportunity to put **multiple layers of protection** in place:

1. **Separation of internal and external traffic**  
   - Internal user traffic and external communication are processed **on separate endpoints**.
   - In emergencies, providers can **completely block external traffic** while **keeping internal messaging functional**.

2. **Domain-level moderation and blocking**  
   - Providers can **ban external domains** that engage in spam, harmful content, or lack proper moderation.  

3. **Improved monitoring and security enforcement**  
   - Providers can **thoroughly monitor s2s traffic** to **combat spam, DoS attacks, and other security threats**.
   - Unlike centralized systems, **federation empowers providers to implement their own security policies** without relying on a single entity.

## Meta, Federation, and XMPP

There is no **technical limitation** preventing Meta from supporting **XMPP**—in fact, **Meta has already done so in the past**.

### Meta’s History with XMPP: Proof of Feasibility

Meta (formerly Facebook) has previously supported XMPP in its messaging products:

- **Facebook Messenger** originally supported XMPP but later discontinued compliance. This shift was **not due to technical constraints**, but rather a **strategic decision** to push users into Meta’s proprietary ecosystem, leveraging its massive user base to create a **network effect** in its favor.
- **WhatsApp** was originally built using an **open-source XMPP server**—which still **forms the core of its infrastructure** today. 
  - The **protocol used by WhatsApp** is a **direct derivative of XMPP**, where the XML-based tag system was converted into a **binary format** for **compactness**.  
  - Despite this change, the **fundamental design and semantics remain identical to XMPP**.

### Meta’s Selective Adoption of Federation

Meta has demonstrated a **willingness to adopt federation**—but **only when it suits its strategic interests**.  

For example, **Threads**, Meta’s social media platform, has committed to **supporting ActivityPub and the Fediverse protocol**. The **Fediverse federation and ID system** function in **the same way that XMPP enables messaging federation**.  
This **raises an important question**:
If **Meta is willing to embrace federation** for Threads when facing **competition from Twitter/X and Bluesky**, why is it **reluctant to adopt XMPP for messaging interoperability** under the **Digital Markets Act (DMA)?**

The fundamental difference here is not technical. It is strategic:

- In **messaging**, Meta enjoys **market dominance**, with billions of users across **WhatsApp, Messenger, and Instagram**.  
- In contrast, **Threads is struggling against Twitter/X and Bluesky**—so Meta is embracing federation as a way to level the playing field and gain market share.  

In other words, **Meta embraces open protocols when it benefits from them, but resists them when they threaten its market control**.  

If Meta were genuinely committed to **interoperability**, it would recognize **XMPP as the most viable and proven protocol for federated messaging**—just as it has in the past.

## Building the Future of Messaging

Federation **is not a security risk—it is a scalable, privacy-friendly model** that has already been **proven in global communication networks** like **email and federated social media**. By leveraging the **XMPP server-to-server (s2s) protocol**, messaging services can **achieve true interoperability** while maintaining **security, user privacy, and control**.

### A Call to Meta: Build Your Interoperability Stack on XMPP

We at the XMPP Standards Foundation (XSF) urge Meta to build its interoperability framework on top of XMPP federation.  

If Threads can implement the Fediverse protocol, there is no reason why Meta cannot do the same with XMPP for Facebook Messenger and WhatsApp—especially since WhatsApp itself was originally built on XMPP.

### The XSF Welcomes Collaboration

The XSF is an open and inclusive organization, welcoming contributions from companies, developers, vendors, and network operators. We recognize that, while Messenger and WhatsApp were originally based on XMPP, there may still be technical discussions needed to align the protocol with Meta’s current needs.

If Meta has specific requirements, such as:

- Features unique to Facebook Messenger or WhatsApp
- Scalability considerations due to the size of Meta’s user base  
- New extensions to address Meta’s specific use cases  

The XSF is the right place to have these discussions. Our mission is to evolve and improve federated messaging standards.

### Join the Conversation on the Future of Federated Messaging

We understand that Meta may wish to contribute to the development of XMPP, and we would welcome Meta’s most prominent messaging experts to bring their expertise, concerns, and ideas into the work of the XMPP Standards Foundation.

Let’s work together to build a truly interoperable, open, and competitive messaging future.

***

## Contact Information

Press and general inquiries: [info@xmpp.org](mailto:info@xmpp.org)

Ralph Meijer  
[Chair of the Board](/about/xsf/people#chair)  
XMPP: [ralphm@ik.nu](xmpp:ralphm@ik.nu)  
Mail: [ralphm@ik.nu](mailto:ralphm@ik.nu)

Matthew Wild  
[Executive Director](/about/xsf/people#executive-director)  
XMPP: [me@matthewwild.co.uk](xmpp:me@matthewwild.co.uk)  
Mail: [me@matthewwild.co.uk](mailto:me@matthewwild.co.uk)

Mickaël Rémond  
Member and Rapporteur to the XSF on the DMA  
XMPP: [mremond@process-one.net](xmpp:mremond@process-one.net)  
Mail: [mremond@process-one.net](mailto:mremond@process-one.net)
