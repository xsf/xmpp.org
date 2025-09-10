---
Title: Syncing Message History
layout: single-implementation-guidelines
---

## MAM Strategies

Fetching history from the server is accomplished with [Message Archive
Management][MAM] (MAM).
New XMPP clients frequently use naïve methods of querying history that result in
long wait times for history, or frozen UIs.
However, a robust strategy for fetching history has not been previously
documented.
This section documents strategies used by clients in the wild, as well as
implementation recommendations for MAM.

### Requirements

- Allow the user to send a message in response to history fetched from the
  server as quickly as possible
- Do not generate dozens of notifications for old messages

### Implementation Notes

- Don't treat history like normal incoming messages.
  If querying lots of messages, aggregate and commit them to the data store
  (assuming a transactional database) as a group.
  Do the same for updating the UI and displaying notifications (ie. display one
  notification, not dozens or perhaps hundreds as messages come in).
- Look up the last message _in your datastore before_ sending initial presence,
  otherwise you may receive a message before you get the last ID and end up with
  a gap.
- If using paging, committing one page at a time to the DB/UI is a natural way
  to break up large transactions and provide the user with quicker feeling
  updates.
- If `mam:2#extended` is supported, query using `after-id` and `before-id` and
  fall back to using the time of the last or earliest message (`start` and
  `end`) if not.

### Communiqué

- On client start iterate through all items in the roster
    - If no messages exist in the local archive:
        - Query in reverse order (in case the server breaks it up by page and we
          end up committing pages separately) with `end: now && limit: X` (where
          X is some configurable number or a guess at a page number based on
          screen size, etc.)
    - Else:
        - Query with `after-id: <last message>` or `start: <last message time>`
          (making sure that the last message was pulled from the DB before we
          send initial presence)
- If the user scrolls to the top:
    - Query in reverse order with `before-id: <first message> && limit: X` or
      `end: <first message time> && limit: X`


[MAM]: /extensions/xep-0313.html
