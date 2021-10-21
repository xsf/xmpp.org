---
Title: XSF IPR Policy
Url: about/xsf/ipr-policy
aliases:
    - "/about/ipr-policy"
    - "/about/xsf/ipr-policy.html"
    - "/about/xsf/xsf-ipr-policy"
layout: single_xsf
---

This document defines the official policy of the XMPP Standards Foundation regarding intellectual property rights (IPR) pertaining to XMPP Extension Protocol specifications (XEPs).

Version 1.4

---------

## Table of Contents

1. [Introduction](#intro)  
1.1. [History](#intro-history)  
1.2. [Purpose](#intro-role)  
2. [Terms](#terms)  
2.1. [XMPP](#xmpp)  
2.2. [XMPP Extension Protocol](#extension)  
2.3. [Implementation](#implementation)  
2.4. [Intellectual Property Claim](#claim)
3. [Terms of Contributing to XMPP Extensions](#contributing)  
3.1. [Ownership](#contrib-ownership)  
3.2. [Approval of XMPP Extensions](#contrib-approval)  
3.3. [A Note about Private Extensions](#contrib-private)
4. [Legal Notice](#legal)

----------

## 1\. Introduction{#intro}

This document defines the official policy of the XMPP Standards Foundation (XSF) regarding intellectual property rights (IPR) as they pertain to extensions to XMPP in the form of XMPP Extension Protocol specifications (XEPs). [[1](#note1)]

### 1.1 History{#intro-history}

The Jabber/XMPP protocols have been under development since 1998 and have been discussed and documented in public forums since January 1999 in the open-source projects that were a precursor to the XSF. Through force of history and activity since its founding in the summmer of 2001, the XSF has assumed responsibility for managing the evolution of the Jabber/XMPP protocols in two ways: (1) through working with the IETF to standardize the core protocols under the name Extensible Messaging and Presence Protocol (XMPP); and (2) through the definition of extensions to the core protocol in the XSF's XMPP Extension Protocol (XEP) specification series. Through this work, the XSF has in effect "homesteaded" the domain of XMPP Extensions and has acted as a trusted third party or "intellectual property conservancy" [[2](#note2)] to which new and established participants in the Jabber/XMPP developer community have entrusted their XMPP Extensions.

### 1.2 Purpose{#intro-role}

The XSF does not seek to disparage the legitimate rights of any individual or organization to assert ownership over an Implementation or Deployment of XMPP or of any XMPP Extension. However, the XSF must ensure that XMPP Extensions do not pollute the free and open nature of the protocols. Preventing such pollution means that in perpetuity any entity may independently, and without payment or hindrance, create, use, sell, distribute, or dispose of implementations of XMPP and of any XMPP Extension. Such is the intent of this policy.

## 2\. Terminology{#terms}

### 2.1 XMPP{#xmpp}

The core XML streaming, instant messaging, and presence protocols developed by the Jabber/XMPP developer community have been contributed by the XSF to the Internet Engineering Task Force (IETF) under the name Extensible Messaging and Presence Protocol (XMPP). XMPP is all and only these core protocols, as currently defined in [RFC 6120](http://www.ietf.org/rfc/rfc6120.txt) and [RFC 6121](http://www.ietf.org/rfc/rfc6121.txt).

### 2.2 XMPP Extension{#extensions}

For the purposes of this IPR policy, an XMPP Extension is any specification approved by, or submitted for approval or consideration by, the XSF or its constituent committees (most particularly the [XMPP Council](https://xmpp.org/council/)). Such a specification must exist in the form of a standards-track XMPP Extension Protocol (XEP) specification in order to be considered an official submission. (Also referred to as an Extension.)

### 2.3 Implementation{#implementation}

Any software program that implements the functionality defined in the core XMPP specifications or in XMPP Extension Protocols for the purpose of providing the functionality defined by the relevant specification(s).

### 2.4 Deployment{#deployment}

Any service deployed over a network that offers the capabilities defined in the core XMPP specifications or in XMPP Extension Protocols.

### 2.5 Intellectual Property Claim{#claim}

Any patent, copyright, or other proprietary claim or claims made by an entity regarding an XMPP Extension. (Also referred to as a Claim.)

## 3\. Terms of Contributing an XMPP Extension{#contributing}

The XSF recognizes the possibility that the creator of an XMPP Extension may make an Intellectual Property Claim regarding an XMPP Extension. Therefore, the XSF takes the following positions:

### 3.1 Ownership{#contrib-ownership}

By submitting an XMPP Extension for consideration by the XSF, the author of the Extension shall assign any ownership rights or other Claims asserted over the Extension to the XSF. This does not apply to Claims regarding any Implementations or Deployments of the Extension, but rather to the Extension itself as represented in a protocol or data format. Any documentation of the Extension (in the form of a XEP specification) shall be copyrighted by the XSF. Once an author assigns ownership to the XSF, the XSF shall in turn make the Extension available to all entities so that they may create, use, sell, distribute, or dispose of Implementations or Deployments of XMPP and all XMPP Extensions in perpetuity and without payment or hindrance.

### 3.2 Approval of Extensions{#contrib-approval}

No Extension shall be approved by the XSF or its constituent committees if there are Claims to the Extension itself, or any Claims that would prevent perpetual, unrestricted, royalty-free use of the Extension in a compliant Implementation or Deployment by any interested party. If Claims preventing such use are discovered, the XSF shall immediately seek to replace the Extension with unencumbered protocols that may be implemented without condition by any entity.

### 3.3 A Note about Private Extensions{#contrib-private}

By its nature as XML, XMPP enables implementers to create their own private extensions to XMPP by means of custom XML namespaces. Such extensions may be kept private, and there is no compulsion for implementers to contribute such extensions to the Jabber/XMPP developer community. It is only when an implementer seeks to have an extension standardized through the XSF's public standards process that ownership over such an extension must be transferred to the XSF. If an implementer wishes to keep its extensions private, it may simply refrain from submitting them to the XSF. However, private extensions exist outside the boundaries of XMPP and approved XMPP Extensions and must not be considered or described as part of XMPP or XSF-approved XMPP Extensions.

## 4\. Legal Notices{#legal}

All XMPP Extension Protocol (XEP) specifications shall contain the following Legal Notices:

> ### Copyright
> 
> This XMPP Extension Protocol is copyright (c) 1999 - 2011 by the XMPP Standards Foundation (XSF).
> 
> ### Permissions
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy of this specification (the "Specification"), to make use of the Specification without restriction, including without limitation the rights to implement the Specification in a software program, deploy the Specification in a network service, and copy, modify, merge, publish, translate, distribute, sublicense, or sell copies of the Specification, and to permit persons to whom the Specification is furnished to do so, subject to the condition that the foregoing copyright notice and this permission notice shall be included in all copies or substantial portions of the Specification. Unless separate permission is granted, modified works that are redistributed shall not contain misleading information regarding the authors, title, number, or publisher of the Specification, and shall not claim endorsement of the modified works by the authors, any organization or project to which the authors belong, or the XMPP Standards Foundation.
> 
> ### Disclaimer of Warranty
> 
> \#\# NOTE WELL: This Specification is provided on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. In no event shall the XMPP Standards Foundation or the authors of this Specification be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Specification or the implementation, deployment, or other use of the Specification. \#\#
> 
> ### Limitation of Liability
> 
> In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall the XMPP Standards Foundation or any author of this Specification be liable for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising out of the use or inability to use the Specification (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if the XMPP Standards Foundation or such author has been advised of the possibility of such damages.
> 
> ### IPR Conformance
> 
> This XMPP Extension Protocol has been contributed in full conformance with the XSF's Intellectual Property Rights Policy (a copy of which can be found at [xmpp.org/about/xsf/ipr-policy](https://xmpp.org/about/xsf/ipr-policy) or obtained by writing to XSF, P.O. Box 1641, Denver, CO 80201 USA).

## Notes

### Note 1{#note1}

For information about XMPP Extension Protocols, see ([xmpp.org/protocols/xmpp-extensions/](https://xmpp.org/xmpp-protocols/xmpp-extensions/)) and [XEP-0001](https://xmpp.org/extensions/xep-0001.html).

### Note 2{#note2}

For information about intellectual property conservancies, see as well as M. van Houweling, "Cultivating Open Information Platforms: A Land Trust Model." Journal of Telecommunications & High Technology Law 1, no. 1 (2002): 309-23.

## Acknowledgements

Many thanks to Lawrence Lessig and Molly van Houweling for their assistance in formulating this policy.

## Changelog

Version 1.4 (2008-01-23): Updated legal notices to use modified MIT License rather than Creative Commons Attribution License for the purpose of enabling wider distribution of XEP text and examples, including incorporation into free software; added Disclaimer of Warranty and Limitation of Liability.

Version 1.3 (2007-01-16): Modified terminology to reflect organizational name change from Jabber Software Foundation (JSF) to XMPP Standards Foundation (XSF).

Version 1.2 (2006-10-04): Modified terminology to reflect protocol branding change from Jabber to XMPP (e.g., Jabber Enhancement Proposal to XMPP Extension Protocol).

Version 1.1 (2005-10-04): Replaced Open Publication License with Creative Commons Attribution License.

Version 1.0 (2002-10-29): Initial version approved by XSF Board of Directors.
