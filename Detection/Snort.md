## Snort (IDS/IPS)
- **Snort** is a powerful IDS (Intrusion Detection System) and IPS (Intrusion Prevention System).

### Three main operational modes:
1. **Packet Sniffing**:  
   Collects and displays network traffic, similar to Wireshark.
2. **Packet Logging**:  
   Collects and logs network traffic to a file.
3. **Network Intrusion Detection**:  
   Analyzes packets and matches traffic against signatures to detect intrusions.

### Snort Rules
- Snort rules are very similar to typical firewall rules.

### Snort Rule Syntax
- **Structure**:
  ```plaintext
  Action | Protocol | Source Address/Source Port -> Direction | Destination Address/Destination Port | Rule Options
  ```
