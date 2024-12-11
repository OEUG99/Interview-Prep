# Understanding the OSI Model

The OSI model provides for different computer systems to communicate with each other. It consists of **7 abstract layers**, each responsible for a specific function and communicating with the layer below it.

## The Layers

### #7 - Application Layer
- Only layer that directly interacts with data from the user.

### #6 - Presentation Layer
- Responsible for preparing data so it can be used by the application layer.
- **Functions**:
  - Encryption
  - Compression
  - Translation

### #5 - Session Layer
- Responsible for opening and closing communication between two devices.

### #4 - Transport Layer
- Responsible for end-to-end communication between devices.
- **Functions**:
  - Breaks data from the application layer into **segments**.
  - Transfers these segments using protocols like **TCP**.
  - Provides error detection using checksums.
- Employs **Windowing** to match sender's speed with receiver's capacity.
- **Multiplexing and Demultiplexing**:
  - Allows multiple applications to send and receive data simultaneously using port numbers.

#### TCP (Transmission Control Protocol)
- Ensures reliable transmission of packets.
- Designed to prevent:
  - Loss of packets
  - Out-of-order packets
  - Duplicate packets
- **Establishes a connection**, making it suitable for large, ordered data.

#### UDP (User Datagram Protocol)
- Connectionless protocol that sends messages, called **datagrams**, without establishing a connection.
- **Characteristics**:
  - No guarantee of delivery, order, or error-checking.
  - Lightweight and has lower latency.
  - Supports sending to multiple recipients more efficiently.

### #3 - Network Layer
- Responsible for determining how data is routed, transmitted, and received across different networks.
- **Functions**:
  - Assigns logical addresses (**IP addresses**) to devices.
  - Determines the best path for data to travel across the network (**routing**).
  - Forwards packets based on destination IP addresses.
- **Packet Handling**:
  - Packets contain headers with destination IP addresses.
  - **Routers and switches** use this information to send/forward packets.

### #2 - Data Link Layer
- Facilitates reliable communication between directly connected devices.
- **Functions**:
  - Employs the use of **frames**.
  - Utilizes **MAC addresses**:
    - Assigned to network interfaces.
    - Used to deliver frames to the correct device.
  - Manages media access to physical mediums to avoid collisions and ensures orderly communication.
  - Detects errors but does not correct them.
- **Common Protocols**:
  - Ethernet
  - Wi-Fi

### #1 - Physical Layer
- Responsible for transmitting raw binary data across physical mediums.
