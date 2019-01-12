---
Title: Social
Url: uses/social
Save_as: uses/social.html
Parent_id: uses
Top_menu_show: false
Top_Menu_order: -1
Dropdown_menu_show: false
Footer_show: false
Sidebar_menu_show: true
Inherit_sidebar: uses
Content_layout: multiple-columns
---

## Realtime Social

XMPP's core messaging can be extended to create group sharing and social networking apps (for example ATOM-formatted feeds).

Three features make XMPP a great choice for powering social projects:

Firstly, because each user connects with their username (in XMPP-speak, their `JID`), a social service can always be sure that only the right user is getting the right information. This baked-in security means XMPP is particularly a great fit for building secure group sharing applications.  

Secondly, XMPP's realtime nature means users of a social service will receive immediate updates when another user does something that involves them (for example: `you were @mentioned in tybalts-party@capulet.lit`).

Finally XMPP's publish-subscribe constructs make a great foundation for building activity-feed type applications. Users can post to their feed, and XMPP will take care of propogating the updates to that user's subscribers in a secure way.

## Projects using XMPP Social

All of these projects make use of XMPP to enhance their social networking functionality.

| Users        | Company                                      | Use                | Description                            |
|--------------|----------------------------------------------|--------------------|----------------------------------------|
| ~1.5 billion | [Google](https://google.com)                 | Push Notifications | Google provides an [XMPP Interface](https://developers.google.com/cloud-messaging/server) to their push notification service. It's also been rumoured that push notifications are delivered to the device via a proprietary binary XMPP protocol. | 
| ~500 million | [Apple](http://apple.com)                    | Push Notifications | Apple uses [XMPP to deliver push notifications](https://www.quora.com/What-technology-does-the-iOS-Apple-Push-Notification-Service-APNS-use-to-maintain-a-persistent-connection-with-each-device-to-receive-such-fast-push-notifications) to client devices. |
|              | [Catapush](http://catapush.com)              | Push Notifications | Reliable and traceable Push Notification service on dedicated XMPP channel for Android/iOS/Windows. |
|              | [Buddycloud Core](http://buddycloud.com/core)|                    | The [Buddycloud Core](http://buddycloud.com/core) messaging stack is a set of social services that include help developers build a complete social application and includes user-onboarding, content recommendation and media sharing features. |
|              | [Jappix](https://jappix.org)                 |                    | [Jappix](https://jappix.org) a Javascript XMPP client with social features. |
|              | [Movim](https://movim.eu/)                   |                    | [Movim](https://movim.eu/) is a PHP based distributed social networking platform. |
|              | [Salut à Toi](http://salut-a-toi.org)        |                    | [Salut à Toi](http://salut-a-toi.org) a Python based multi-frontends XMPP client featuring (micro)blogging, file sharing, games, etc. [Libervia](https://libervia.org) is its web frontend. |
