# Broadcast Domains and Collision Domains

## Broadcast Domain
- A Broadcast domain is a segment of a network where a broadcast frame (aka a packet sent to all devices in the net) is forwarded. 
- Devices within the same broadcast domain can receive these broadcasts.
- Downsides:
  - The more devices in a domain, the more packets get forwarded.
- VLANs can be used to create separate domains.
- **Example:** ARP uses broadcast frames/domains.

## Collision Domain
- Collision domains are network segments where data can "collide" during transmission.
- Collisions cause retransmissions, reducing network efficiency.
- Modern technology uses multiplexing to mitigate collisions.
- **Example:** Think retro phone lines, how two people can't use the line at once without an issue.
