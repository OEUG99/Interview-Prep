- # What is DNS?
	- DNS translates human readable domain names into machine
	  readable IP addresses.  
	- ## The DNS Query Process:
		- 1. Browser Cache
			2. Operating System Cache
			3. Recursive Resolver:

			- Acts as an intermediary fetching DNS info on behalf of the client.
		- 4. Root Name Server:
			- The resolver from step 3 queries to a root name server.
			- The query doesn’t return the IP, instead, it directs to the appropriate TLD name server based on the extension (.com).
		- 5. TLD Name Server:
			- Directs the resolver to the authoritative name server responsible for the specific domain.
		- 6. Authoritative Name Server:
			- Has the actual DNS records for the domain.
			- It responds with the IP address.
	- There are different types of ways to query:
		1. Recursive Query
		2. Iterative:

		- Tries multiple DNS servers step by step.
			3. Non-recursive:

		- When the answer is already cached.
	- ## Types of DNS Records:
		- A: Maps a domain to an IPv4.
		- AAAA: Maps a domain to IPv6.
		- CNAME: An alias for another domain.
		- MX: Specifies the mail server.
		- NS: Indicates the authoritative name server.
		- PTR: Maps IP to domain (Reverse DNS lookup).
		- TXT: Arbitrary text used for verification.
		- SRV: Specifies location of services.
		- SOA: Contains administration information about the domain, including versioning.
	- ## DNS Caching:
		- DNS sources cache responses to reduce query times and lower loads.
		- TTL (Time to Live): Determines how long a record remains cached.
	- ## DNS Threats:
		- 1. DNS Spoofing/Poisoning:
			- Attackers inject fake DNS records into the cache of a resolver, redirecting traffic to malicious sites.
		- 2. DNS Tunneling:
			- A method of bypassing firewalls by encoding information within DNS queries.
			- Since DNS is vital, this is a sneaky way to transmit data.
			- Tool Example: DNSCAT2 for command and control.
			- Use case: Can be used as a VPN to bypass captive portals since auth servers aren’t typically blocked.
	- ## Threat Mitigation
		- Detecting Tunneling:
			- Use security onion and other SIEM tools.
		- Defense:
			- DNS filtering but limited by filter lists.
			- OpenDNS filters as an example.
		- DDoS on DNS:
			- Attackers overwhelm DNS servers with massive traffic, disrupting services.
		- DNS Hijacking:
			- Attackers redirect DNS queries by compromising DNS settings at the client, ISP, or domain registrar level.
		- Typo-Squatting:
			- Related but not entirely a DNS issue.
			- DNS filtering can help prevent redirects from similar names.
		- Cache Poisoning:
			- Manipulate the cache of a DNS resolver to serve incorrect IP addresses.
		- Domain Generation Algorithms:
			- Explained earlier with tunneling, this is essentially the same thing but the algorithm name is used in malware.
		- DNSSEC (DNS Security Extension):
			- Adds a layer of authentication to DNS by using cryptographic signatures.
			- Ensures data integrity and authenticity but does not encrypt DNS traffic.
			- This prevents spoofing like DNS cache poisoning.
