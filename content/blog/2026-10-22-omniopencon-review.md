---
title: XMPP Stand/Talk at OmniOpenCon 2026 Review
date: 2026-10-22
author: Polarian
categories: ['Events', 'XMPP Community']
summary: "Review of the XMPP stand and talk at OmniOpenCon 2026"
---

## XMPP Stand

As a bit of background, I have been to a few XMPP stands organised by
others, at FOSDEM and FrOSCon, seeing their strengths and where I felt they
were weaker. This was my first attempt at organising a stand, and to my
surprise it was more successful than I could have ever dreamed of.

We had a large proportion of the conference come over and chat, not just
take stickers, and leaflets like many other stands at other conferences, but
full on in-depth discussions, which inevitably led to the XMPP stand becoming
a hackerspace of sorts, the organisers suggesting we pull more tables over
to the end so that people could hack at the end of the stand and not block
the main stand.

We also trialled some new ideas, which I haven't seen at any other stands so
far. I will also cover the ideas which are common at every stand.

{{< figure src="/images/blog/omniopencon2026-devices-stand.webp" caption="OmniOpenCon 2026 Devices stand" >}}

### Stickers

Like every stand, we had stickers. This in my opinion doesn't really help
too much with getting people interested in XMPP, most people end up throwing
stickers into a box at home. This doesn't mean they are a waste of time,
people who are passionate about XMPP love to be able to decorate their
devices with stickers, which then helps with making XMPP more mainstream and
familiar.

### Leaflets

[para](https://para.mohrie.net) designed new leaflets for the conference,
these were more popular than the stickers for newcomers, because it explained
exactly what XMPP is, and on the back explained how to try XMPP, even the
organisers of the conference were taking a look at the leaflets, and could
potentially play with XMPP in the future.

Leaflets are also ridiculously cheap to print (compared to stickers) making
them much more disposable, allowing you to spread XMPP to more people for
less.

### Device demos

The device demos we picked were to target the most platforms possible, so
that anyone who came over to the stand could see the interop between
different clients and devices. We had an iPhone with Monal IM, two Androids
with Conversations and Cheogram and a Linux laptop with Gajim (which would
also run on Windows as well).

As with all conferences, the device demos were popular, and people like
playing with them. However they are much more of a "woah cool" rather than a
method of getting people onto XMPP.

{{< figure src="/images/blog/omniopencon2026-devices.webp" caption="OmniOpenCon 2026 Devices Close-up" >}}

### Protocol diagrams (NEW)

Edward designed two example diagrams showing at a high level how servers
federate, and users message across different servers. This also was
invaluable in my talk to describing how the XMPP protocol functioned. These
diagrams made it far easier to explain to people who were less tech-savvy
how XMPP is beneficial to them, and why it would suit their use case.

On top of this, para had rendered an A3 image of the XMPP operators graph,
as this is so big and hard to render on the web that under conference
conditions it's hard to have it on hand. Having it printed on paper allowed
us to use it as a high level overview of how many servers (which publish
themselves) are federating within the network, with the protocol diagrams
being a "slice" of that network.

{{< figure src="/images/blog/omniopencon2026-diagram-stand.webp" caption="OmniOpenCon 2026 Diagram Stand" >}}

### Public MUC to onboard (NEW)

I have not yet seen this as at any stand personally. I have seen the use of
a demo MUC hosting on hardware at the conference, but not an actual public
MUC with a QR code for people to join as they walked past the stand.

This was probably the most successful part of the stand, those who already
used XMPP or had dabbled in it came past and joined the MUC and were
chatting throughout the conference, and even days later theres been regular
activity after the conference. This has allowed people to make new
connections, which is something XMPP has always struggled with providing due
to the limited number of communities outside of XMPP development.

We printed the XMPP URI off as a QR code stuck it in the middle of the
stand.

### Operator invite links (NEW)

We had two operators (other than myself) who were at the stand. We had
already decided in advance to try to break the cycle of people coming over,
speaking and then forgetting about XMPP, that we would hand out invite links
along with the leaflets they could collect, so they could easily install the
app on their phone at the stand, and scan a QR code, make a username and
then immediately join the MUC.

This had some success, some people still decided to use random providers as
is their freedom to, but we also saw a few people sign up via the invite
links.

The invite links were printed off and then cut up into sticker-sized QR codes
which people could take away with them.

Unfortunately, due to a mistake, half way through the day the invite link
was invalidated, and all the invite links distributed in the morning had to
be discarded. For this reason, we can not draw a definite conclusion whether
this method of onboarding is actually successful or not. Better luck next
time.

## Talk

Unfortunately, I was given the last talk slot before the closing notes. This
meant a lot of people had already left by the time my talk was up, and I
don't feel like it properly reached the audience I intended. The talk was
focused at sparking interest in XMPP, rather than a deep dive into some
topic within XMPP. However the majority of the audience already used XMPP.

Nevertheless, it was a fun talk, and at the bare minimum I got to thank
everyone who had been involved in making the stand possible.

The stand was definitely the highlight fo the conference, it drew many more
people towards it, and was far better at onboarding and getting new people
interested in XMPP.

You can see the slides
[here](https://polarian.dev/assets/slides/omniopencon2026.pdf).

### Talk material

Most talks are just people standing at the front speaking about something
for the allotted time, however we instead handed out XMPP leaflets, and
invite links to everyone who attended. This provided them with the
information to go away after the talk and look into it more if they were
interested.

Due to the few people who attended the talk, I can't say if this would be
effective if scaled, but 1-2 people who attended my talk and got the leaflet
ended up making an account and messaging me after the conference, so at the
limited scale I had, it was successful.

## Sponsors

* [XMPP Standards Foundation (XSF)](https://xmpp.org) - stickers and
  leaflets
* [Cheogram](https://cheogram.com/) - stickers
* [Monal IM](https://monal-im.org/) - stickers

## Special thanks to

* [Singpolyma](https://singpolyma.net/) - Cheogram stickers funding
* [Thilo Molitor](https://github.com/tmolitor-stud-tu) - Monal stickers
* [Guus](https://github.com/guusdk) and [stpeter](https://stpeter.im/) -
  XMPP stickers and leaflets funding from XSF
* [Emus](https://github.com/Echolon) - Support from XSF commsteam for
  outreach.
* [OmniOpenCon](https://omniopencon.org) - Providing the XMPP project a
  stand, and me a talk slot

### Stand volunteers

* [para](https://para.mohrie.net/) - Designed the leaflets and wrote the
  Makefile to render the XMPP graph for printing.
* Alexandru Nicolae - Handled logistics Romania side, including shipping and
  collection of intentional packages. Also donated the laptop for the stand
  running Gajim on [Endeavour OS](https://endeavouros.com/).
* [Rareș](https://fzorb.xyz/) - Donation of the Cheogram phone running
  [LineageOS](https://lineageos.org/), along with providing power to the
  stand.
* Edward - Donation of the Conversations phone and the Monal IM phone.

