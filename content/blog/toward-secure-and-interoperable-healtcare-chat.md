---
title: "Towards Secure and Interoperable Healthcare Chat"
date: 2025-10-28
author: "Guus der Kinderen"
categories: ["XSF", "Open Letter", "Miscellaneous"]
---

*Supporting the development of the Dutch NTA 7532 standard with lessons from international practice*

## Who We Are and Why This Matters

The XMPP Standards Foundation (XSF) is an independent, non-profit organization that promotes and advances open standards for real-time communication and collaboration. The XSF oversees the development of extensions to the Extensible Messaging and Presence Protocol (XMPP) and fosters an open, secure, and decentralized ecosystem for messaging technologies across the Internet.

In healthcare, chat and messaging have become essential for coordination between doctors, nurses, general practitioners, and patients. Yet many existing tools are consumer-grade, not designed to meet healthcare’s strict requirements for **privacy, auditability, and compliance**.

The Netherlands is taking major steps to address this gap through the upcoming NTA 7532 technical specification for healthcare chat, part of the broader NEN 7516 framework on secure communication. This initiative has strong potential to align national practice with international standards - if built on proven, open technologies.

## What Is XMPP - in Simple Terms

XMPP (Extensible Messaging and Presence Protocol) is an open standard for secure messaging that allows different chat systems to talk to each other. You can think of it as email for chat: anyone can host their own service, and as long as both sides follow the same rules, messages flow securely and reliably between organizations.

Because XMPP is built on core Internet Engineering Task Force (IETF) standards, it works hand-in-hand with the technologies that power the Internet itself: like TLS for encryption, SASL for authentication, and DNS for service discovery. This means XMPP isn’t just compatible - it’s part of the Internet's DNA.

XMPP is already used by government, defense, and healthcare networks in several countries, proving that open protocols can deliver high-assurance, privacy-compliant communication at scale.

## A Quick Example from Healthcare

Imagine a nurse in a hospital who needs to consult a specialist in another organization about a patient’s medication plan. With a secure XMPP-based chat system following the NTA 7532 standard:

1. The nurse can send a message from her hospital’s system.
2. The specialist receives it instantly on their organization’s system.
3. Both systems verify each other’s identity, encrypt the message, and log it for audit purposes.
4. No one needs to use consumer apps or insecure messaging.

This is the type of trusted, interoperable communication the Dutch healthcare system aims to achieve, and where XMPP offers a proven foundation.

## Security and Interoperability in Healthcare Messaging, A Context for XMPP

Instant messaging has become an essential tool in healthcare, supporting communication among professionals and between care providers and patients. However, clear and consistent **security and interoperability standards** are still lacking. Without these, users often rely on generic consumer platforms that do not meet healthcare’s privacy, compliance, and auditability requirements.

The Netherlands is taking important steps to address this challenge. A security framework for healthcare messaging already exists in the form of **NTA 7516**, which is now being revised and elevated to **NEN 7516**. This will serve as the overarching functional standard, supported by two technical specifications: one for **email (NTA 7531)** and one for **chat (NTA 7532)**.

NTA 7532 will define essential areas such as encryption, authentication, user transparency, archiving, and audit logging. These standards are being developed collaboratively by healthcare organizations, IT vendors, and the Ministry of Health, with a public consultation and pilot implementations to follow.

## XMPP as a Foundation for Secure and Interoperable Chat

Many of the goals described in the Dutch **NTA 7532** standard align closely with what the **Extensible Messaging and Presence Protocol (XMPP)** already provides.

From its very beginning, XMPP was designed for **federation**, meaning that independent systems (for example, different hospitals or care providers) can exchange messages securely, just like email servers do today. This makes XMPP a natural fit for a national healthcare messaging standard that needs security, interoperability, and local control.

### How XMPP Supports NTA 7532 Objectives

XMPP offers a modular, standards-based foundation where essential capabilities such as authentication, encryption, message delivery, and federation are already well-defined. This allows healthcare chat systems to meet functional and security requirements without reinventing the underlying technology.

| **Purpose**                             | **What It Means in Practice**                                                                                                                         | **XMPP / Internet Standard**                        |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **Base protocol**                       | All message exchange between chat service providers uses the XMPP protocol to ensure interoperability.                                                | RFC 6120, RFC 6121, RFC 7590, RFC 7622              |
| **Addressing and federation**           | Users and organizations are identified in a globally unique format (`user@organization.tld`), supporting secure cross-domain communication.           | RFC 7622                                            |
| **Server discovery**                    | Systems automatically locate other trusted servers using DNS SRV records.                                                                             | RFC 2782, RFC 6120                                  |
| **Sender verification**                 | The authenticity of servers is validated through DNSSEC and DANE, combined with TLS certificates.                                                     | RFC 4033 (DNSSEC), RFC 6698 (DANE)                  |
| **Transport encryption**                | All traffic between servers and clients is encrypted with modern TLS (1.2 or 1.3).                                                                    | RFC 5246, RFC 8446, RFC 7590                        |
| **Data-at-rest encryption**             | Stored messages are encrypted using AES with a 256-bit key to protect message history and attachments.                                                | AES-256                                             |
| **Delivery confirmation**               | Servers confirm successful receipt of each message, ensuring reliability and auditability.                                                            | XEP-0184 (Message Delivery Receipts)                |
| **Attachments**                         | Files or images are exchanged through secure HTTPS links protected by TLS.                                                                            | XEP-0363 (HTTP File Upload), RFC 2818 (HTTPS)       |
| **Digital signatures**                  | Messages or metadata can be digitally signed to verify integrity and origin.                                                                          | ETSI TS 101 903 (XAdES)                             |
| **Group chat**                          | Multi-user conversations across organizations, with invitation and moderation capabilities.                                                           | XEP-0045, XEP-0249, XEP-0410                        |
| **Message correction / retraction**     | Users can edit or withdraw sent messages where supported.                                                                                             | XEP-0308, XEP-0424, XEP-0425                        |
| **Read receipts**                       | Participants can indicate that a message has been read.                                                                                               | XEP-0085 (Chat State Notifications)                 |
| **Publishing contact info and avatars** | Professionals can share verified contact details and profile images.                                                                                  | XEP-0054 (vCard-temp), XEP-0084 (User Avatar)       |
| **Interoperability and registry model** | Each organization can operate its own trusted service provider, discoverable through DNS, enabling secure federation between systems.                 | Core XMPP federation and DNS-based trust mechanisms |
| **Confidentiality and access labeling** | Messages can carry structured confidentiality labels (as recommended by FHIR) to indicate sensitivity levels, access restrictions, or handling rules. | XEP-0258 (Security Labels in XMPP)                  |


*Note: End-to-end encryption (e.g., OMEMO or OpenPGP) is possible within XMPP but may be applied selectively, as healthcare messaging often requires auditable storage and controlled access for compliance.*

This mapping illustrates how an open, extensible protocol can meet functional and security goals while allowing national specifications such as NTA 7532 to define **which features and policies are mandatory** for certified systems.

## Why This Matters for Healthcare

Using XMPP doesn’t mean reinventing the wheel. Instead, NTA 7532 can build on **mature, international standards**, simply defining **which XMPP features and policies are required** for certified systems.

This approach ensures:
- **Predictable interoperability**: Different vendors’ systems can communicate reliably.
- **Security by design**: Proven encryption and authentication methods are reused, not re-created.
- **Vendor independence**: Hospitals and care providers can choose any compliant system without losing connectivity.

In short, XMPP already provides the technical foundation. NTA 7532 defines the **rules of engagement** for Dutch healthcare, ensuring all participants use it safely and consistently.

## Interoperability and Vendor Independence

One of the biggest strengths of XMPP is its federated and open architecture. In simple terms, this means every healthcare organization, whether a hospital, general practice, or mental health provider, can run its own chat system, while still communicating securely with others. Messages flow across organizational boundaries just as emails do, but with **modern security controls** and **fine-grained authentication**.

### How This Helps Healthcare Providers

In practice, this means:

- A hospital’s internal chat server can communicate securely with a general practitioner’s system, even if each uses a different vendor.
- Authentication can rely on digital certificates or other trusted credentials, so both sides know who they’re talking to.
- Each organization keeps control over its own infrastructure and data, meeting national privacy requirements.

This design directly supports the core goals of NTA 7532 (interoperability, traceability, and security) without forcing all parties onto one platform or vendor.

### The Role of a Shared Profile

To make interoperability truly seamless, participating systems must agree on how they use XMPP’s many features. That’s where NTA 7532 comes in: it can define a shared national profile, specifying which XMPP extensions and settings are mandatory, recommended, or optional.

Such a profile ensures:

- **Predictable behavior** between implementations
- **Reliable message delivery** across systems
- **Verified compliance** through testing and certification

### Vendor Independence and Open Innovation

Because XMPP is **open, royalty-free, and supported by dozens of implementations**, no single company controls it. Any vendor can build or extend XMPP-based products, whether open-source or commercial, while still remaining compatible with others. This enables true vendor independence: healthcare organizations can switch suppliers or integrate new tools without losing interoperability.

Existing compliance and interoperability test suites for XMPP further support this independence, helping vendors validate that their systems behave consistently and securely.

In short, XMPP provides not just a technical foundation but also a **healthy market ecosystem**: one that fosters collaboration, innovation, and long-term sustainability in healthcare communication.

## Alignment with International and European Practice

Across the world, governments and public institutions are choosing **open, standards-based messaging protocols** to support secure, interoperable communication, especially in sectors where trust and reliability are critical.

The Extensible Messaging and Presence Protocol (XMPP) has already proven itself in these environments. It underpins communication systems for organizations such as the **U.S. Department of Defense**, **NATO**, and several **European government and public-safety networks**. Within the UK, the **National Health Service (NHS)** employs XMPP-compatible systems for messaging and notifications.

These real-world deployments demonstrate that XMPP can deliver:

- **High assurance** - meeting strict security and auditability requirements
- **Operational resilience** - functioning across multiple infrastructures and jurisdictions
- **Scalability** - supporting large networks with millions of users

### A Natural Fit with European Priorities

The open nature of XMPP aligns closely with European digital policy objectives, particularly around:

- **Digital sovereignty** - reducing dependency on proprietary or non-European technology providers.
- **Open standards and interoperability** - ensuring systems from different vendors or sectors can work together.
- **Transparency and trust** - through openly developed, publicly available specifications.

By basing healthcare chat interoperability on XMPP, the Netherlands not only meets its **national goals** for security and compliance, but also contributes to **Europe’s broader vision** of an open and connected digital ecosystem.

### Learning from International Practice

Adopting and aligning with internationally proven standards like XMPP offers clear advantages:

- Dutch implementers can **reuse tested building blocks** instead of designing everything from scratch.
- The national profile defined in **NTA 7532** can stay compatible with international healthcare or government messaging systems.
- Future collaboration, whether with European neighbors or global health initiatives, becomes far simpler.

In short, the Netherlands has the opportunity to **lead by example**, demonstrating how open standards can support secure, sovereign, and future-proof communication in healthcare.

## Collaboration Opportunities

The development of **NTA 7532** is more than a technical exercise: it’s a chance to shape the **future of secure, interoperable communication in Dutch healthcare.**

To make this a lasting success, collaboration between the **Dutch standards community** and the **XMPP Standards Foundation (XSF)** will be essential. The XSF works transparently and welcomes cooperation with all. By engaging directly with the XSF, Dutch experts and healthcare stakeholders can ensure that NTA 7532 remains aligned with international best practice while addressing national needs.

We invite the NTA 7532 working group and stakeholders to engage directly with the us!

### Areas for Collaboration

Here are some concrete ways to work together:

- **Share healthcare use cases and requirements** with XSF technical groups, ensuring that future protocol extensions reflect real-world healthcare needs.
- **Participate in joint workshops or liaison roles**, creating a two-way channel between the Dutch NEN/NTA community and XSF developers.
- **Run pilot implementations** that test interoperability between systems, contributing results back to both Dutch and international standardization efforts.
- **Collaborate on testing and certification**, leveraging existing XMPP validation tools to support NTA 7532 compliance.

Such collaboration would ensure that the technical realization of NTA 7532 remains **future-proof, internationally aligned, and interoperable** by design.

### How to Get Involved
The XSF welcomes contributions from anyone interested in secure, standards-based communication. There are several easy ways to engage:

- Visit our website: https://xmpp.org
- Join our discussion list: https://mail.jabber.org/mailman/listinfo/standards
- Chat with us: https://xmpp.org/community/chat/
- Contact us directly: https://xmpp.org/contact/

Participation is open, free, and designed to lower barriers for new contributors.

Together, we can ensure that Dutch healthcare messaging (and by extension, European healthcare communication) is **secure, interoperable, and sustainable** for years to come.

## Conclusion

The Dutch **NTA 7532** initiative marks a pivotal step toward **trusted, interoperable digital communication** in healthcare. By defining a clear, open, and verifiable framework for secure chat, the Netherlands is setting a benchmark for how national standards can align with international innovation.

The **Extensible Messaging and Presence Protocol (XMPP)** provides a ready-made foundation for this effort:

- It is **mature and battle-tested** in demanding environments.
- It is **open and royalty-free**, fostering vendor independence and innovation.
- It is **flexible and extensible**, ready to adapt to evolving clinical and regulatory needs.

By working closely with the **XMPP Standards Foundation** and the wider international community, the NTA 7532 working group can ensure that its standard remains **technically sound, future-proof, and globally compatible**.

In short: **XMPP supports the secure, interoperable communication that Dutch healthcare needs today, and lays the groundwork for the trusted systems of tomorrow.**
