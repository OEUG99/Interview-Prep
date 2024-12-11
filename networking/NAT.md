# NAT

**NAT**: is a method to map private IP addresses within a local network to a single public IP address for communication with external devices such as the internet.

## How it Works:

1. **Private IP Usage**: Devices inside a local network use private IP addresses that are not routable on the internet.

2. **Translation Process**:
   - **Step 1**: The router replaces the private IP address in the packet's source field with the router's public IP address.
   - **Step 2**: The router keeps a record of the translation in a NAT table, associating the private IP and port number with the public IP and a temporary external port.
   - **Reverse Translation**: When a response comes back, the router consults its NAT table to forward the response to the correct private IP address inside the network.

## Types of NAT:

1. **Static NAT**: 
   - One-to-one mapping between a private IP and a public IP.

2. **Dynamic NAT**:
   - Uses a pool of public IP addresses and assigns them to private IPs on demand.

3. **PAT (Port Address Translation)**:
   - The most common type. Maps multiple private IPs to a single public IP using unique port numbers to differentiate connections.

## Why NAT is Useful:

1. **IP Address Conservation**:
   - Helps conserve IPv4 addresses by allowing multiple devices to share a single public IP address.

2. **Security**:
   - Hides internal IP addresses from external networks.

3. **Flexibility**:
   - Internal IPs can change without affecting external-facing IPs.
