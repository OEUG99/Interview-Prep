# CAM Table

## Overview
- A type of memory used in network switches to store **MAC address-to-port mappings**.
### How it works:
  - When a frame enters the switch, it checks the source MAC address and updates the CAM table with the MAC address and port from where the frame came.
  - It then checks the destination MAC address to determine which port to forward the frame.

## Vulnerability
### CAM Table Overflow:
  - An attack or event where the CAM table of a switch is overwhelmed with fake MAC address entries.
  - This causes the switch to fail in its normal operations.
  - Additionally it typically forces the switch into **flooding mode**, where it broadcasts frames to all ports, which can be exploited for **packet sniffing** or **man-in-the-middle (MitM) attacks**.
