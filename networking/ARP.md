# What is ARP?

- **Address Resolution Protocol**:
  - Fundamental networking protocol that plays a crucial role in enabling communication within local area networks (LANs).
  
- It is a network protocol used for mapping an IP address to a physical MAC address.

- ARP works in the data link layer (Layer 2).

- ARP is stateless, and requests typically broadcast to all devices on a network because the requesting device does not initially know the MAC address of the target device.

---

# How does ARP work?

## Steps:
1. **Request**: When a device wants to send data to another device on the same LAN, it first sends an ARP request, broadcasting a message like:
   - "Who has IP address x.x.x.x? Tell MAC address y.y.y.y."

2. **Response**: The device with the requested IP address responds with an ARP reply, providing its MAC address.

3. **Cache**: Both devices cache the mapping of IP address to MAC in their ARP tables to avoid repeated unnecessary broadcasts.

---

# ARP Threats and Attack Vectors

- **ARP spoofing/poisoning**:
  - Attackers manipulate ARP tables via false requests.
- **ARP spoofing** can be used for MITM (Man-in-the-Middle) attacks as well as DoS (Denial of Service).

- **Reconnaissance**:
  - `arp-scan` can discover live devices on the network by identifying MAC and IP addresses.

---

# ARP Threat Mitigation

- **Static ARP entries**:
  - For critical devices or small networks, static mappings can be used to prevent manipulation.

- **Dynamic ARP Inspection**:
  - Many managed network switches offer this feature that verifies ARP packets against a trusted database.

- **Network Segmentation**:
  - Isolate sensitive devices into separate VLANs to reduce exposure to ARP attacks.

- **Encryption**:
  - End-to-end encryption like HTTPS/VPNs ensures confidentiality.

- **Gratuitous ARP Filtering**:
  - Configuring network equipment to block unsolicited ARP responses.

---

# CLI Commands

- `arp` – View and manipulate ARP tables.
- `ip neigh` – Manages neighbor discovery.
- `nmap` – Scans devices on the network and identifies ARP-based details.
- `arp-scan` – ARP discovery tool.

---

# Attack Tools

- `ettercap`, `arpspoof`, `Cain & Abel`:
  - All commonly used for ARP spoofing.

---

# Monitoring Tools

- **Wireshark**:
  - Analyze ARP packets for anomalies.

- **ARPWatch**:
  - Detect ARP spoofing or changes in ARP tables.

- **ARP Table Monitoring**:
  - Helps locate compromised devices.
