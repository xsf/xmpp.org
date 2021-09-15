---
Title: Intermediate Certificate Authority
Url: about/xsf/records/proposals/intermediate-certificate-authority
---

Author: Peter Saint-Andre
Version:    1.0
Date:   2006-11-28
Status: Approved

### 1.0 Introduction

The Jabber/XMPP community has always cared about privacy and security. In particular, when the XML wire protocols used by Jabber technologies were formalized within the IETF (under the name XMPP), they were subject to rigorous security review, resulting in the use of Transport Layer Security (TLS) for channel encryption. Unfortunately, it can be both difficult and expensive for administrators of XMPP servers to obtain proper X.509 certificates for use in securing communications with TLS. This proposal addresses that problem by establishing an intermediate certification authority (ICA) for the network of XMPP servers.

### 2.0 Background

Currently, server administrators who care about securing communications tend to create self-signed certificates. Unfortunately, self-signed certificates do not engender strong trust in the network, since anyone can create a self-signed certificate. The traditional approach to securing communication channels in a high-trust manner is to ensure that server certificates are issued by a certification authority (CA) that completes some level of due diligence regarding the identity of the server administrator before issuing the certificate. The resulting certificate can be issued by a root CA (which is at the “root” of the trust chain or “tree”), or by an intermediate CA (which depends on the root CA but administers a specialized branch of the trust chain).

Eventually, we hope that all providers of X.509 certificates will issue certificates for XMPP servers. However, XMPP server certificates that conform to the format specified in Section 5.1 of RFC 3920 include information that is not yet standard in certificates for, say, HTTP servers. For this reason, CAs must complete some development work in order to issue fully conforming certificates for XMPP servers. Because major CAs such as Verisign and Thawte probably do not have an interest in completing such work without a demonstrated market need, it makes sense for XMPP server administrators to work on the necessary processes and procedures with some of the smaller, more flexible CAs first. (Another approach would be for XMPP server administrators to form their own certification authority, probably under the auspices of the Jabber Software Foundation (JSF); however, running a CA is far outside the core competency of the JSF.)

Therefore, the initial goal of this proposal is for the Jabber Software Foundation to work with one or two CAs who already issue free or low-cost certificates while still adhering to industry standards regarding identity verification. Research into certification authorities indicates that the most likely candidates are CAcert and StartCom. CAcert is a loosely-knit volunteer organization built on something akin to the open-source model, which issues server certificates based on acquisition of sufficient points in its web of trust. StartCom is a commercial entity whose main business is offering a Linux distribution, but which issues server certificates in the more traditional manner based on presentation and validation of individual credentials (e.g., government-issued identification) and association with the relevant domain (e.g., whois lookups).

### 3.0 Choice of Provider

The author of this proposal has been involved with CAcert since late 2004 and with StartCom since early 2006. Both are well-intentioned organizations in which honest, hard-working, security-minded individuals are working to make the Internet a more high-trust environment.

The JSF’s choice of one CA with which to work initially should be driven by the JSF’s requirements at this stage in the evolution of the Jabber/XMPP network. For the purposes of this proposal, the JSF’s requirements regarding the choice of an initial CA are:

- Must conform to industry practices regarding identity verification and certificate issuance.
- Must already issue free or low-cost server certificates.
- Must support the XMPP object identifier specified in Section 5.1 of RFC 3920, or be willing and able to add such support (including the ability to specify multiple XMPP OIDs, e.g., for virtual domains and XMPP server components).
- Must be organizationally viable, such that the JSF can form a long-term relationship with the CA.
- Should have its root certificate included in well-known operating systems (e.g., various Unices, MacOS, Windows) and certificate “bundles” (e.g., Mozilla), or be well on the way to such inclusion.
- Should enable the JSF to function as an intermediate certification authority (ICA) for the Jabber/XMPP network.
- CAcert issues free server certificates (upon gaining sufficient points in its web of trust) and StartCom issues low-cost server certificates. Through work with the author of this proposal and several XMPP server administrators, CAcert supports the XMPP object identifer, and StartCom has stated that it is willing and able to add such support. Although CAcert offers “organizational assurance”, it does not presently enable organizations to function as ICAs, whereas StartCom has an ICA program in place. Regarding organizational viability, commercial entities can go out of business and community projects can wither away, so there is no guarantee of continued viability in either case.

The major differentiating factor between the two CAs is conformance with industry practices, in large measure as indicated by inclusion of the CA’s root certificate in operating systems and certificate bundles (because the JSF has not performed an audit of either CA and is not in a position to do so, we must trust that other organizations have performed appropriate due diligence). To our knowledge, CAcert has not passed an independent audit and CAcert’s root certificate has not gained inclusion in any operating system or certificate bundle. By contrast, StartCom has passed an independent audit (performed by WE Consulting Group of Israel, see report) and has been included various web browsers, in theMozilla certificate bundle (including Firefox 2), in KDE, in OpenSSL, and in Mac OS X 10.5 (Leopard).

Because of the wider acceptance of the StartCom root certificate and the ability of the JSF to run an ICA under StartCom’s auspices, it seems appropriate to choose StartCom as the initial provider of certificates for the Jabber/XMPP network, while continuing to monitor the progress of CAcert and other CAs with an eye to working with them in the future.

Note well that the JSF’s choice of an initial CA is decidedly not exclusive. That is, the JSF could (and very well might) form relationships with other CAs. In part, the purpose of this proposal is to gain experience with the issuance of X.509 certificates to XMPP server administrators. That experience will help the JSF understand the requirements for discussions with other CAs in the future.

### 4.0 Proposal

The Jabber Software Foundation (JSF) proposes to engage with the StartCom Free SSL Certification Authority (SFSCA) in establishing an Intermediate Certification Authority (ICA) that shall issue digital certificates for use by XMPP server administrators (and potentially also by XMPP end users). The ICA will be operated at the “XMPP Federation” website controlled by the JSF (probably to be moved to <https://certs.xmpp.org/>), and will issue certificates only for use on the XMPP network (e.g., it will not issue certificates for HTTP servers). The issued certificates will be “Class 1″ certificates that require only email verification via one of the canonical addresses listed in RFC 2142.

In accordance with StartCom’s CA Policy & Practices document along with its ICA Policy Appendix, the division of responsibilities shall be as described below.

The SFSCA shall:

- Issue an intermediate certification authority certificate to the JSF.
- Provide a complete Internet-based online solution for the signing and management of XMPP Federation members and of certificates issued by the XMPP Federation.
- Provides an additional Internet-based interface for straightforward and customized integration into the XMPP Federation website.
- Respect and maintain the privacy of all JSF principals and XMPP Federation members, for example by keeping all gathered information strictly confidential.
- Issue Class 1 server certificates (and potentially) Class 1 personal certificates on behalf of the XMPP Federation.
- Notify XMPP Federation members of certificate issuance.
- Accept revocation requests from the XMPP Federation.
- Issue Certificate Revocation Lists (CRL) and publish the CRLs issued.
- Provide an Online Certificate Status Protocol (OCSP) service.
- Inform XMPP Federation members of certificate revocation.
- Keep audit logs of the certificate issuance process.
- Maintain the highest security standards possible.

The JSF (through its XMPP Federation initiative) shall:

- Authorize certificate issuance only to registered members of the XMPP Federation and provide details of issued certificates to the SFSCA.
- Accept revocation requests only from registered members of the XMPP Federation and inform the SFSCA of all revocation requests.
- Use only the website interface provided by the SFSCA for certificate issuance.
- Protect private and individual all data obtained.
- Maintain the highest security standards possible.
- Accept the requirements and conform to the policies and practices of the SFSCA.
- Defend, indemnify, save and hold StartCom Ltd. harmless from any demands, liabilities, losses, costs and claims.

The foregoing description of responsibilities is descriptive; the ruling documents shall be the above-referenced policy documents as supplemented or amended by a formal agreement between the JSF and the SFSCA.

### 5.0 Projected Costs

The JSF shall issue certificates free of charge to XMPP Federation members. That is, the JSF shall subsidize issuance of certificates to server administrators in order to secure the open network of XMPP servers.

The exact costs of the ICA activity to the JSF are yet to be determined, since they will depend on the final agreement negotiated between the JSF and the SFSCA as well as the number of certificates issued.

It is unknown how many certificates the XMPP Federation will be requested to issue. A reasonable number of certificates to expect in the first year of operation is probably 500. However, it is hoped that over time nearly all administrators of XMPP servers that communicate regularly over the open Internet will obtain server certificates. While that number too is unknown, it is probably at least 10,000 at present, and is expected to rise as XMPP technologies become more popular.

Over the long haul, the per-certificate cost is expected to average perhaps as low as $1 if the ICA issues a large number of certificates (say, 5000 a year). The per-certificate cost would be higher if a smaller number of certificates is issued (to cover basic costs of the ICA program) but if the ICA issues a large number of certificates then the per-certificate costs would decline. Clearly, the absolute cost of offering free certificates could eventually become significant. However, if XMPP server certificates become that popular then it is also expected that the JSF would be able to raise the necessary monies in order to continue the ICA activity (since increased interest in XMPP technologies would likely result in an increased number of JSF sponsors as well as the potential for new and creative ways to raise the necessary monies). In short, issuing a large number of server certificates is a problem we would like to have.

### 6.0 Oversight and Reporting

Oversight of the ICA activity shall be the overall responsibility of the Executive Director of the JSF, but day-to-day management may be performed by a dedicated work team of the JSF as defined in the JSF Bylaws. The Executive Director of the JSF (or the leader of the appropriate work team) shall provide a quarterly report of ICA activities to the JSF Board of Directors, including the number of certificates issued and revoked as well as a full accounting of all costs incurred.

END