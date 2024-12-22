# [NostrRelay]

This is a [nostr](https://github.com/nostr-protocol/nostr) relay,
written in Rust.  It currently supports the entire relay protocol and
persists data with SQLite.  There is experimental support for
Postgresql.

Most of the code comes from with a few changes I added to make it more usable: [GitHub](https://github.com/scsibug/nostr-rs-relay).

## Features

[NIPs](https://github.com/nostr-protocol/nips) with a relay-specific implementation are listed here.

- [x] NIP-01: [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md)
  * Core event model
  * Hide old metadata events
  * Id/Author prefix search
- [x] NIP-02: [Contact List and Petnames](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [ ] NIP-03: [OpenTimestamps Attestations for Events](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [x] NIP-05: [Mapping Nostr keys to DNS-based internet identifiers](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [x] NIP-09: [Event Deletion](https://github.com/nostr-protocol/nips/blob/master/09.md)
- [x] NIP-11: [Relay Information Document](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [x] NIP-12: [Generic Tag Queries](https://github.com/nostr-protocol/nips/blob/master/12.md)
- [x] NIP-15: [End of Stored Events Notice](https://github.com/nostr-protocol/nips/blob/master/15.md)
- [x] NIP-16: [Event Treatment](https://github.com/nostr-protocol/nips/blob/master/16.md)
- [x] NIP-20: [Command Results](https://github.com/nostr-protocol/nips/blob/master/20.md)
- [x] NIP-22: [Event `created_at` limits](https://github.com/nostr-protocol/nips/blob/master/22.md) (_future-dated events only_)
- [ ] NIP-26: [Event Delegation](https://github.com/nostr-protocol/nips/blob/master/26.md) (_implemented, but currently disabled_)
- [x] NIP-28: [Public Chat](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [x] NIP-33: [Parameterized Replaceable Events](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [x] NIP-40: [Expiration Timestamp](https://github.com/nostr-protocol/nips/blob/master/40.md)
- [x] NIP-42: [Authentication of clients to relays](https://github.com/nostr-protocol/nips/blob/master/42.md)

## Additions to take note of 

1. Added the Docker-Compose.yml this enables us to call docker to compose up and start our relay that way.
2. Also the pythonClient.py, is for testing only. Just to verify I can send messages to my relay.


## To start it up

1. Need to install docker and have login
2. Need to CD into Nostr directory if not already there
3. Need to build the file: "docker build -t nostr-rs-relay ." needs to be done anytime there are changes
4. Then run: "docker compose up"
5. Recommend: Getting Docker-Desktop to view the relay and its analytics


