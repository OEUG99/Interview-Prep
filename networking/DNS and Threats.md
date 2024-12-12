# How DNS Works
- **DNS** translates human-readable domain names into machine-readable IP addresses.

## The DNS Query Process
1. **Browser Cache**: The browser checks if the domain is cached locally.
2. **Operating System Cache**: The OS checks its cache for the domain.
3. **Recursive Resolver**: Acts as an intermediary, fetching DNS information on behalf of the client.
4. **Root Name Server**: 
   - The recursive resolver queries the Root Name Server.
   - The Root Name Server doesn't return an IP but directs to the appropriate TLD (Top-Level Domain) Name Server (e.g., `.com`, `.org`).
5. **TLD Name Server**: Directs the resolver to the **Authoritative Name Server** responsible for the specific domain.
6. **Authoritative Name Server**: Has the actual DNS records for the domain and responds with the IP address.

## Types of DNS Queries
1. **Recursive Query**: The resolver performs all steps to return the final answer to the client.
2. **Iterative Query**: The resolver queries multiple DNS servers step-by-step, asking for partial results.
3. **Non-recursive Query**: Used when the answer is already cached.

## Types of DNS Records
- **A**: Maps a domain to an IPv4 address.
- **AAAA**: Maps a domain to an IPv6 address.
- **CNAME**: An alias for another domain.
- **MX**: Specifies the mail server for the domain.
- **NS**: Indicates the Authoritative Name Server.
- **PTR**: Maps an IP to a domain (Reverse DNS lookup).
- **TXT**: Arbitrary text used for verification or other purposes.
- **SRV**: Specifies the location of services.
- **SOA**: Contains administrative information about the domain, including versioning.

## DNS Caching
- **Caching**: DNS servers cache responses to reduce query time and lower loads.
- **TTL (Time to Live)**: Determines how long a DNS record remains cached.

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
