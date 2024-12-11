# Firewalls

## What are they?
Firewalls are fundamental components of network security that monitor, filter, and control inbound and outbound traffic based on defined security policies.

- They act like a checkpoint between networks, often between private and public ones.
- Not only are firewalls good at regulating what goes in and what goes out, they can also be used to segment internal networks into distinct security zones.

### Types of Firewalls
- **Packet Filtering Firewalls**:  
  Examines basic packet headers for IP addresses, ports, and protocol types.

- **Stateful Inspection Firewalls**:  
  Tracks ongoing/active connections and only allows packets that are part of a known, ongoing session to be a part of an already established TCP session. Without any prior record of the initial SYN handshake, the firewall becomes suspicious.

- **Deep Packet Inspection (DPI)**:  
  Some advanced firewalls examine packet payloads, not just headers. DPI inspects application-layer data to block malware signatures, suspicious patterns, or application misuse.

- **NAT and PAT**:  
  - Many firewalls also serve as NAT gateways, allowing for the rewrite of source and destination addresses in packets.  
  - This allows multiple hosts to share one public IP and hides internal network structure from external entities.

- **Application Layer Firewalls**:  
  Terminate and inspect traffic at the application protocol level (HTTP headers, SMTP commands). They can rewrite requests and responses.

- **Next-generation Firewalls (NGFWs)**:  
  Combine traditional firewalling with intrusion prevention, application awareness, identity-based policies, SSL/TLS traffic inspection, and advanced threat detection.

- **FaaS (Firewall-as-a-Service)**:  
  Delivered via cloud, useful for microservice designs, etc.

### State Tables
Stateful firewalls track active sessions by maintaining state tables.

### TCP Handshake Awareness
A stateful firewall knows about the three-way handshake in TCP. It keeps track of the state of active connections. When a packet arrives claiming to be part of an already established TCP session without any prior record of the initial SYN handshake, the firewall becomes suspicious.
