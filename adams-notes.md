# xmpp.org website

## Proposed site structure and content

```
(ordered alphabetically)

xmpp.org/                 // featured content
â”‚
â”œâ”€â”€ about/                // overview of xmpp
â”‚   â”‚
â”‚   â”œâ”€â”€ benefits
â”‚   â”œâ”€â”€ faq
â”‚   â”œâ”€â”€ federation
â”‚   â”œâ”€â”€ history
â”‚   â”œâ”€â”€ resources
â”‚   â””â”€â”€ standards         // high-level on standards (details at standards.xmpp.org)
â”‚
â”œâ”€â”€ blog/
â”‚
â”œâ”€â”€ community/            // events, mailing lists, mucs, GitHub, logs
â”‚
â”œâ”€â”€ contact
â”‚
â”œâ”€â”€ howto/                // howto articles
â”‚
â”œâ”€â”€ software/             // featured software
â”‚   â”‚
â”‚   â”œâ”€â”€ clients
â”‚   â”œâ”€â”€ libraries
â”‚   â”œâ”€â”€ projects
â”‚   â””â”€â”€ servers
â”‚
â”œâ”€â”€ uses/
â”‚   â”‚
â”‚   â”œâ”€â”€ enterprise
â”‚   â”œâ”€â”€ im
â”‚   â”œâ”€â”€ iot
â”‚   â”œâ”€â”€ social
â”‚   â”œâ”€â”€ web
â”‚   â””â”€â”€ webrtc
â”‚
â””â”€â”€ xsf/                  // description of the xsf and its relationship to xmpp
    â”‚
    â”œâ”€â”€ board
    â”œâ”€â”€ council
    â”œâ”€â”€ members
    â””â”€â”€ sponsors
```
## Proposed split of the site

- Let's clarify the relationship of the XSF to both XMPP and the standards process by:
  - making XMPP and what it can help people do take center stage on xmpp.org
  - putting standards and the standards process the focus of a new site (__standards.xmpp.org__)
- Describe how the standards process works on standards.xmpp.org and help people get involved.
- Move protocols and xeps to standards.xmpp.org
- Contextualize the XSF and standards for each audience
  - xmpp.org/standards would describe the standards process high-level, point to standards.xmpp.org for more details on getting involved
  - standards.xmpp.org/xsf would describe the xsf and its role in the standards process.
  - xmpp.org/xsf would describe the xsf and its relationship to xmpp

## Proposed home page strategy

- Incredibly approachable language, focused on users
- Making the case for XMPP from the first moment they're on the site
- Long-scroll page, not trying to cram everything "above the fold"
- Primary "hero" section is about the value of XMPP, getting started with XMPP, and software projects using XMPP
- Some combination of WebRTC, IoT, IM, Social use cases featured + links to others
- Section with links to recent articles
- One sentence about XMPP + links
- One sentence about XSF + links to standards.xmpp.org

## Sample home page content

Here's an example of the kind of copy and an approachable, simple voice that I think we should use on the main section of the site. (Assume that the following would also have links throughout it.)

> *XMPP is the Internet standard for messaging and presence.*
> 
> *In the best spirit of the Internet, it is private, secure, and independent.*
> 
> *No one owns XMPP. It's free and open for everyoneâ€”and has been since 1999. (Back then, it was called "Jabber".)*
> 
> *XMPP is used by millions of people like you and me to connect to what matters. (It's also used by Google, Facebook, Microsoft, Apple.)*
> 
> *It's a living standard. Internet engineers are actively extending and improving it. (Right now!)*
> 
> *XMPP has proved useful for emerging areas of tech like Internet of Things (IoT), WebRTC, and social media. New XMPP projects emerge every day. Is yours next?*

## Proposed technical details

- Markdown content
- [Pelican](http://getpelican.com) static site generator
- [Bootstrap](http://getbootstrap.com) design

## Proposed path forward 

- Agree on site content and structure.
- Identify a subset of content to target for initial site.
- Begin converting and assembling markdown content in a pelican repo.
- Evaluate design options when we have this content.


# xmpp.org blog

## Proposed blog process

__Goals__
- Aim to publish two articles a month initially.
- Long-term goal is four articles per month.
- Use blog posts as drafts for future content for sections of the site.

__Topics__
- "How to" articles
- "Why it's this way"
- Technical explanations
- Debunk myths about XMPP
- Comment on / point to other newsworthy articles
- "Position papers" on key topics

__Editorial policy__
- The XSF should publish regularly. In order to do so, not all posts will reflect the views of all members.
- The XSF should be generally positive and constructive in its posts, but polite criticism is acceptable.
- Politically / strategically controversial topics should be published at the discretion of the board.
- Technically controversial topics should be published at the discretion of the council.
- Submitted posts will have a week for comment and editing, from their initial draft.
- XSF members interested in reviewing, commenting on, and editing posts may subscribe to the GitHub repo for these blog posts. 
- If there are no objections after a week, a post may be published at any time.
- By board approval, any post may be published at any time.

__Editorial process__
- Blog posts are proposed/nominated by creating new GitHub issues on the site repo. These can be full suggested posts or just stubs like: 
  - "Someone should write a post about why we still care about federation"
  - "How to set up and configure your own Prosody server on Digital Ocean"
  - "Respond to matrix.org criticism of XMPP"
- Whoever is nominated to write a post *and accepts* is assigned that post in GitHub.
- First drafts are submitted via pull request.
- A week is allowed for comment and review (unless the board chooses otherwise).
- Posts that have not been identified as controversial are published without board and/or council approval.
- Posts that have been identified as controversial may be published at the discretion of the board and/or council.
