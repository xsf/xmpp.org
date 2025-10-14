---
Title: Standards Process
Url: about/standards-process
aliases:
    - "/about/standards-process.html"
    - "/xmpp-protocols/xmpp-extensions/submitting-a-xep"
mermaid: true
---

The XSF develops extensions to XMPP through a lightweight standards process centered around XMPP Extension Protocols (XEPs).

The XEP series contains around 350 specifications, covering everything outside of the core of XMPP (which is worked on within the IETF). These specifications are liberally licensed under the XSF's [IPR Policy](/about/xsf/ipr-policy) for wide implementation. Developers and other standards experts from around the world collaborate on these, developing new specifications for emerging practises, and refining existing ways of doing things. Proposed by anyone, the particularly successful ones end up as Final or Active - depending on their type - while others are carefully archived as Deferred. This life cycle is described in [XEP-0001](/extensions/xep-0001.html), which contains the formal and canonical definitions for the types, states, and processes. Similarly, there is [XEP-0143](/extensions/xep-0143.html) which contains the canonical guidelines for how to write XEPs, how to submit, and how to maintain them.

This page will only look at XEPs aiming to become a Final Standard, which is what most people would want.

So if you have an idea for a new extension in XMPP, what do you do?

Importantly, you don't need to be an XSF member to propose new XEPs or work on existing ones, because discussion occurs on the open [standards@xmpp.org discussion list](https://mail.jabber.org/mailman/listinfo/standards).

#### Write your proposed extension

The first thing to do is to write up your idea. XEPs are written in an XML format that's pretty simple and straightforward - it's really just a very simplified HTML. The syntax is formally described in XEP-0001, but the key here is to ensure everyone knows the general shape of the problem and solution by reading it, so there's no need - yet - to get everything perfect. Once you're happy that it looks reasonable, then send this XML document to the "XMPP Editor".

The XMPP Editor isn't actually one person, but a team of amazingly hard working XSF members. To send them a proposed new XEP, just send it in an email to them - but because that's a list, and would be drowned in spam, you'll need to get the subject line right.

#### Submit your extension{#submitting-a-xep}

Here's how to submit a proposal to the XMPP Standards Foundation for consideration as an [XMPP Extension Protocol](/extensions):

1. Write your proposal following the guidelines described in [XEP-0143: Guidelines for Authors of XMPP Extension Protocols](/extensions/xep-0143.html).
2. Make sure you read, understand, and agree to the XSF’s [IPR Policy](/about/xsf/ipr-policy) before you submit your proposal!
3. Make a GitHub Pull Request putting your new XML file into the "inbox" directory, as described in [Submitting a Proposal](/extensions/xep-0143.html#submit). (If you don't have a GitHub account, you can email it to the Standards SIG mailing list)

Note: It is the author’s responsibility to provide a properly-formatted source file (see the [template](https://raw.githubusercontent.com/xsf/xeps/master/xep-template.xml) file maintained under [source control](/about/xsf/source-control)). Proposals submitted in HTML, TXT, MS Word, Open Document Format, etc. will be returned to the proposal author for proper formatting.

#### Editor creates a ProtoXEP

The Editor then takes the document, corrects any minor formatting errors, puts it in source control, and announces it to the list. During this time, they'll also verify with you that you're in a position to transfer any ownership in the document to the XSF, and willing to do so. At this point, your document now becomes a "ProtoXEP".

#### ProtoXEP added to XMPP Council agenda

Once announced on the Standards List, the Editor also places it on the agenda for the XMPP Council. The XMPP Council is a group of XSF members elected by the membership to act as a technical committee. They meet (usually once a week) in order to make various decisions based around the XEP process, as well as have more detailed technical conversations about more general issues. Their meetings are open to all, and if you've proposed a new XEP, it's really advisable to join in - the meetings are held over XMPP, in the council@muc.xmpp.org chatroom.

#### A XEP’s Lifecycle

{{< mermaid >}}
flowchart LR
  start(( ))
  exp[Experimental]
  prp[Proposed]
  stb[Stable]
  fin[Final]
  def([Deferred])
  dep(Deprecated)
  obs([Obsolete])
  rej([Rejected])
  rtd([Retracted])

  subgraph XEP Lifecycle
  start-->exp
  exp-->prp
  prp-->exp
  prp-->stb
  stb-->fin
  end

  def-..->exp
  def-.->prp
  exp-.->def
  exp-.->rtd
  prp-.->rej
  stb-.->dep
  fin-.->dep
  dep-.->obs
{{< /mermaid >}}

#### Experimental XEP

The Council decides on accepting a ProtoXEP by voting (you need a majority of Council members to agree it's a good idea), but in this case, any Council member can also veto a XEP for any reason. Previous reasons have been that a proposal overlaps with existing protocols, or that the proposal has architectural problems, but in principle a Council member can reject a proposal for any reason. If there's a remedy, the Council member will write this up and send it to the list, but it's usually worth catching them online and asking them about it.

Assuming the Council accepts it, then it now becomes an Experimental XEP, and gains a number. Although "Experimental" sounds like quite an unstable state, people can go ahead and try implementing it and seeing what happens even now; the XSF uses XML namespacing carefully to avoid early implementors being penalized as the protocol changes. And it almost certainly will; protocols have even changed back to earlier versions during the Experimental phase as people discover that what was thought to be a good change causes more problems that it solved. Every time you change your XEP, you'll provide the new version to the XMPP Editor, who'll update the version on the website and send out an announcement to the list. If this isn't done for more than 12 months, then the XEP will be moved off Experimental to Deferred - if this happens, another update will put it back onto Experimental.

#### Stable

Once everyone seems satisfied that the XEP is "right", you can ask Council to start the process to move it to Stable. This happens in three phases - first, the Council decides whether the XEP seems ready, and agrees on whether to move it on. This is generally treated as a pure majority vote. The XEP then enters Proposed state, and the Editor issues a Last Call for comments. You might consider this a "Beta" state. A Last Call is typically two weeks, though this period is a minimum, and the Editor can keep it going as long as they think is right, for example if there are still conversations happening. Once all this dies down, a few further changes might be needed to the XEP. Once the new version is announced, the Editor will either reissue a Last Call, or else return the XEP to Council for advancement.

#### Release Candidate

The Council then votes once more, on moving the XEP to Stable. If Proposed is "Beta", Stable might be considered a "Release Candidate" specification - at this point the XEP is under careful control. Changes which might alter the protocol itself need discussion on the list, and approval by the Council before the XEP can be updated. Breaking changes, while not outright banned, are certainly frowned upon. Because of this, there's again a veto option for Council members, in case it's felt that the XEP needs further, more informal work before advancing.

#### Release

Eventually, the XEP hopefully stabilizes to the point where no further changes are expected, and the community is essentially reliant on the extension's stability. Once this is the case, the XEP can be advanced to Final - though never until at least 6 months after the move to Stable. Final means that there is no expectation of the XEP ever changing in any incompatible way. Although optional parts can in theory be added, in general it's much easier to write an entirely new XEP, since any change to a Final XEP will be very carefully scrutinized by the Council. The XEP is, essentially, "released", and considered to have been proven in the field.

The process is a somewhat more relaxed version of the move to Stable, and the goal is just to ensure that the XEP really is stable, and the community really does like it. To check this, the Editor puts out a Call For Experience - like a Last Call, this is an explicit call for comments, but in this case it's mostly directed at people who've implemented, and ideally deployed, the specification. Again, this might cause a few updates to clarify the XEP. Also, the specification must have been implemented by at least two different codebases, one of which has to be Open Source. Once all this has been done, the Council then votes to move it to Final.

#### In conclusion

Although this process can take a while, the entire process has been refined over the years to make sure that any XEP, in any stage, can safely be implemented, even at Experimental. Achieving Stable shows the community as a whole has enormous confidence in the specification, and has carefully examined it. A XEP in Final state has in addition been implemented multiple times and deployed, and checked over by subject experts in numerous projects and companies. All this means that the XEP series is both simple to write, and extremely beneficial to the community.

__So if you've an idea for a new extension in XMPP? Just write a XEP!__
