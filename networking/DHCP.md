# Understanding DHCP

- **Dynamic Host Configuration Protocol**:
  - Automatically assigns IP addresses, subnet masks, default gateways, etc.

## DHCP Components
1. **DHCP Server**:
   - Manages the pool of IP addresses and configuration data.

2. **DHCP Clients**:
   - Request configuration details (typically phones, PCs, etc.).

3. **DHCP Relay Agents**:
   - Forwards requests between clients and a DHCP server when they are not on the same subnet.

---

# DHCP Process (DORA)

1. **Discovery**:
   - Client broadcasts a DHCPDISCOVER to find a server.

2. **Offer**:
   - DHCP Server responds with a DHCPOFFER containing an available IP.

3. **Request**:
   - The client replies with a DHCPREQUEST to accept the offered configuration.

4. **Acknowledgement**:
   - The server confirms with a DHCPACK, finalizing the lease.

---

# DHCP Modes

- **Automatic Allocation**:
  - Permanent IP assigned to a client out of a pool of available IPs.
  - Remains the same unless DHCP configuration changes.

- **Dynamic Allocation**:
  - IP assigned to a client temporarily. After it times out, it either renews or releases.

- **Manual Allocation**:
  - Set by an administrator.
