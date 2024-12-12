- ## Overview
	- A protocol that allows a program to request a service or execute a procedure on a remote system as if it were local.
	- Useful in distributed computing but also introduces significant security concerns.
- ## How It Works
	- 1. A client sends a request to a remote server to execute a function or procedure.
		2. The server processes the request and sends back results.
		3. The communication is abstracted, so the client code appears to call a local procedure.

- ## Key Concepts
	- **RPC implements a stub**: An interface that abstracts away underlying network details.
- ## Security Threats
	- **Man-in-the-Middle (MitM) attacks**
	- **Authentication weaknesses**
	- **Denial of Service (DoS) attacks**
	- **Code injection**
	- **Privilege escalation**
	- **Replay attacks**
- # Threat Detection
	- ## Techniques
		- **Traffic analysis**
		- **Vulnerability scanners**
		- **Penetration testing**
		- **Intrusion Detection Systems (IDS)**
- # Historical Exploits
	- ## EternalBlue (WannaCry)
		- SMB exploit that was RPC-dependent.
	- ## SigRed
		- Exploited Windows DNS, an RPC-related flaw.
	- ## gRPC Exploits
		- Exploits targeting gRPC implementations.
