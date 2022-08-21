---
title: "Google Summer of Code 2022 at XSF: Converse.js - Mid Term Evaluation Update"
date: 2022-08-13
author: PawBud
categories: ["Google Summer of Code"]
aliases:
    - "/2022/08/mid-term-evaluation-updates/"
---

It's been a month since I wrote my [last blog](https://xmpp.org/2022/07/conversejs-an-in-depth-view-into-my-gsoc22-project/). For those of you who have been following my blogs, thanks a lot for taking the time to read them. In this blog, I will give the updates post mid-term evaluation and the challenges that I have been facing and how I overcame some of them.

### The Mid-Term Evaluation

For those of you who don't know much about GSoC, a mid-term evaluation was scheduled, where as a contributor you have to fill out a form which had some questions related to your experience with your mentor and the organization administrator so far and the project itself. It barely took me 5-10 minutes to complete the form so there's that.

### Project Updates & Challenges Faced

I have been working on the jingle message retraction feature and the jingle chat history feature. Let me explain:

If you have gone through [XEP-0353](https://xmpp.org/extensions/xep-0353.html), you might be knowing about the [retraction feature](https://xmpp.org/extensions/xep-0353.html#retract). If not, then the below two diagrams are my best attempts to explain it, and to be honest it is pretty simple.

![jingle_retraction](/images/blog/retraction_working.png) 

Ok, now, let me show you another diagram which took me around 2 weeks to visualize:

![jingle_message_passing_in_detail](/images/blog/message-passing.png) 

This is what confused me the most and took a lot of my time. If you look at the way I have written my code (and I won't link it, since I believe that the link might break in the future due to the constant changes in the codebase that are yet to come):

```
    // Responder's Side Parser
    function parseJingleMessage(stanza, attrs) {
    const jingle_propose_type = getJingleProposeType(stanza);
    return { ...attrs, ...{ 'jingle_propose': jingle_propose_type, 'jingle_retraction_id': getJingleRetractionID(stanza), 'template_hook': (attrs['template_hook']) ? 'getJingleTemplate' : undefined, 'jingle_status': attrs['jingle_status'] }
    }
    }

    // Initiator's Side
    function retractCall(context) {
    const initiator_message = context.model.messages.findWhere({ 'media': 'audio' });
    const propose_id = initiator_message.attributes.propose_id;
    const message_id = u.getUniqueId();
        api.send(
            $msg({
            'from': _converse.bare_jid,
            'to': context.jid,
            'type': 'chat',
            id: message_id
            }).c('retract', { 'xmlns': Strophe.NS.JINGLEMESSAGE, 'id': propose_id })
            .c('reason', { 'xmlns': Strophe.NS.JINGLE })
            .c('cancel', {}).up()
            .t('Retracted').up().up()
            .c('store', { 'xmlns': Strophe.NS.HINTS })
        });
        const attrs = {
            'from': _converse.bare_jid,
            'to': context.jid,
            'type': 'chat',
            'jingle_retraction_id': propose_id, 
            'msg_id': message_id,
            'jingle_status': context.model.get('jingle_status'),
            'template_hook': 'getJingleTemplate'
        }
        context.model.messages.create(attrs);
    }
```

I borrowed this code from a single file called "utils.js" which as the name suggests contains all the miscellaneous functions of a plugin that are needed for it to function. It doesn't take much thinking to realize how big the problem becomes once the codebase is large enough. I must say it's thanks to my mentor, I was able to differentiate the two sides, and i am now able to move on. Though, I still get confused but fortunately, I feel like its becoming more infrequent.

Ohh, and by the way, the [create](https://backbonejs.org/#Collection-create) function creates an instance of the message model, and if you didn't understand this statement, I highly recommend going through the [backbone.js documentation](https://backbonejs.org/#).

So, lessons to learn:

* Comment or possibly document your code from day one.
* Don't keep random variable names.
* Speak up to your mentor!! Period. I can assure you a lot of JC's time could have been saved had I spoken up about my thought process sooner.

Ahemmm..... let's move on now.

### Message Chat History Rendering for Jingle

Now, when you get a missed call, you usually get a timestamp. It is no different in a jingle call, but I do need to have a discussion regarding it's actual implementation with JC. The actual message content should be pretty straightforward and if you want to see how I implemented/am implementing it, I will straight up point towards [JC's explanation of it](https://github.com/conversejs/converse.js/issues/447#issuecomment-1198217084).

### Non-Technical Corner of this blog

Hmmmm enough about the project, now for some unnecessary life updates. I will be leaving for my master's program in a week's time. My schedule is packed with various things right now. Going to a new country on your own is scary for the first time, especially when you know that there is no one who can help you there but GSoC seems like a perfect distraction from the nervousness. JC seems to be doing fine, speaking of whom, did I mention he took a hiatus last week? I really hope he enjoyed his time off. There were nights in the last week, which made me wonder if I did actually stress him out or something, but I am pretty sure I am just overthinking it. I value his patience out of all things and I am not joking when I say he has a lot of it. I mean, if I as a mentor would meet another PawBud, I would have probably quit by now and to be honest, that's one of the million reasons why I am not a mentor right now. I feel so embarrassed about the little things JC has to repeat every time because I was distracted or too lazy to note them down. I hate inconsistency and love to be direct about things, so if you have made it this far, I would like to say that there is a good chance that this project might end with the implementation of XEP-0353 given my slow pace.

I do know that there are many people who are expecting this feature to be implemented, but yeah it is what it is. JC has somehow motivated me, to do what I do perfectly and I couldn't agree more. Let's see what the future holds now, I am giving it everything, and I will try to implement it as much as I can effectively. 

Thanks for reading my blog.

Regards,
PawBud
