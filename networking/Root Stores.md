# Root Stores
## Definition
- Root Stores are repositories of trust and root certificates used by operating systems, browsers, and other software to verify authenticity and trustworthiness of digital certificates.

## Root Certificates
- Digital Certificates issued by trusted entities called Certificate Authorities.
- Act as a "anchor" for a chain of trust. They are self-signed by the CA.

## Purpose
- A root store ensures that applications and systems trust only those digital certificates verified by trusted CA's in the store.

## Management
- Typically managed organizationally:
  - Windows' root store -> Microsoft
  - Chrome's root store -> Google

## Importance
- This is an integral part of validating SSL certificates for websites.
