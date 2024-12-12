# SSL/TLS

- **SSL/TLS** is a cryptographic protocol that provides secure communication over the internet.
- It involves **C.I.A**:
  1. **Confidentiality**
  2. **Integrity**
  3. **Authentication**

## How SSL/TLS Works

- **TLS Handshake**: The process of setting up a secure communication channel between the client (e.g., browser) and the server.  
  - The point is to:
    1. Agree on encryption parameters.
    2. Authenticate the server.
    3. Generate a shared session key for encrypting data.

# TLS Handshake Step by Step

## 1. Client Hello
- The client starts the handshake by sending:
  1. Supported encryption algorithms.
  2. Random data used for creating session keys.
  3. TLS version.

*Essentially, this starts negotiating.*

## 2. Server Hello
- The server picks an encryption algorithm that works and sends:
  - Random data (used with client data for key generation).

## 3. Server Certificate
- The server sends its **digital certificate**, issued by a trusted Certificate Authority (CA).  
- The certificate contains:
  1. **Server's public key**
  2. **Domain name** (to verify identity)
  3. **CA's digital signature**

*This proves the server's identity to the client.*

## 4. Key Exchange
- The client generates a **pre-master secret** (random number) and encrypts it with the server's **public key** (from the certificate).  
- The encrypted data is sent to the server.  
- This allows the client and server to securely derive a shared session key that no one can compute, even if they intercept the handshake.

## 5. Session Key Generation
- Both the client and server use the pre-master key and random numbers to compute the **session key**, which will be used for **symmetric encryption**.

## 6. Handshake Completion
- Both parties send **"Finished"** messages encrypted with the session key to verify that encryption/decryption is working.
