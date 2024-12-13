The following data used was mocked, but shows hte steps used investigating potential threats.


# Splunk Queries and Results

## Query 1: Retrieve All Events
**Query:**
```spl
index=security_logs
```
**Result:**
| **_time**           | **src_ip**     | **dest_ip**     | **action** | **threat_level** |
|----------------------|----------------|-----------------|------------|------------------|
| 2024-12-13 10:00:00 | 192.168.1.1    | 10.0.0.5        | allowed    | 2                |
| 2024-12-13 10:05:00 | 192.168.1.2    | 10.0.0.6        | blocked    | 8                |
| 2024-12-13 10:10:00 | 192.168.1.3    | 10.0.0.7        | blocked    | 7                |
| 2024-12-13 10:15:00 | 192.168.1.4    | 10.0.0.8        | allowed    | 3                |
| 2024-12-13 10:20:00 | 192.168.1.2    | 10.0.0.6        | blocked    | 9                |
| 2024-12-13 10:25:00 | 192.168.1.5    | 10.0.0.9        | allowed    | 4                |
| 2024-12-13 10:30:00 | 192.168.1.6    | 10.0.0.10       | blocked    | 6                |
| 2024-12-13 10:35:00 | 192.168.1.2    | 10.0.0.7        | blocked    | 10               |

---

## Query 2: High Threat Events
**Query:**
```spl
index=security_logs threat_level>=7
```
**Result:**
| **_time**           | **src_ip**     | **dest_ip**     | **action** | **threat_level** |
|----------------------|----------------|-----------------|------------|------------------|
| 2024-12-13 10:05:00 | 192.168.1.2    | 10.0.0.6        | blocked    | 8                |
| 2024-12-13 10:10:00 | 192.168.1.3    | 10.0.0.7        | blocked    | 7                |
| 2024-12-13 10:20:00 | 192.168.1.2    | 10.0.0.6        | blocked    | 9                |
| 2024-12-13 10:35:00 | 192.168.1.2    | 10.0.0.7        | blocked    | 10               |

---

## Query 3: Count Events by Source IP
**Query:**
```spl
index=security_logs | stats count by src_ip
```
**Result:**
| **src_ip**     | **count** |
|----------------|-----------|
| 192.168.1.1    | 1         |
| 192.168.1.2    | 3         |
| 192.168.1.3    | 1         |
| 192.168.1.4    | 1         |
| 192.168.1.5    | 1         |
| 192.168.1.6    | 1         |

---

## Query 4: Investigate Specific Source IP
**Query:**
```spl
index=security_logs src_ip=192.168.1.2
```
**Result:**
| **_time**           | **src_ip**     | **dest_ip**     | **action** | **threat_level** | **protocol** | **dest_port** | **user_agent**             | **country** |
|----------------------|----------------|-----------------|------------|------------------|--------------|---------------|----------------------------|-------------|
| 2024-12-13 10:05:00 | 192.168.1.2    | 10.0.0.6        | blocked    | 8                | TCP          | 22            | SSH-2.0-OpenSSH_7.6p1     | Russia      |
| 2024-12-13 10:20:00 | 192.168.1.2    | 10.0.0.6        | blocked    | 9                | TCP          | 3389          | Remote Desktop Protocol    | Russia      |
| 2024-12-13 10:35:00 | 192.168.1.2    | 10.0.0.7        | blocked    | 10               | TCP          | 23            | Telnet                     | Russia      |

---

## Query 5: Filter by Protocol (Telnet)
**Query:**
```spl
index=security_logs protocol=telnet
```
**Result:**
| **_time**           | **src_ip**     | **dest_ip**     | **action** | **threat_level** | **protocol** | **dest_port** | **user_agent** | **country** |
|----------------------|----------------|-----------------|------------|------------------|--------------|---------------|----------------|-------------|
| 2024-12-13 10:35:00 | 192.168.1.2    | 10.0.0.7        | blocked    | 10               | TCP          | 23            | Telnet         | Russia      |

---

## Query 6: Filter by Protocol (UDP)
**Query:**
```spl
index=security_logs protocol=udp
```
**Result:**
| **_time**           | **src_ip**     | **dest_ip**     | **action** | **threat_level** | **protocol** | **dest_port** | **user_agent** | **country** |
|----------------------|----------------|-----------------|------------|------------------|--------------|---------------|----------------|-------------|
| 2024-12-13 10:10:00 | 192.168.1.3    | 10.0.0.7        | blocked    | 7                | UDP          | 53            | -              | Germany     |
| 2024-12-13 10:30:00 | 192.168.1.6    | 10.0.0.10       | blocked    | 6                | UDP          | 161           | SNMP/2c        | China       |

---
## Query 7: Events by Destination Port
**Query:**
```spl
index=security_logs | stats count by dest_port
```
**Result:**
| **dest_port** | **count** |
|---------------|-----------|
| 22            | 1         |
| 23            | 1         |
| 53            | 1         |
| 161           | 1         |
| 3389          | 1         |
| 443           | 2         |
| 80            | 1         |

---

## Query 8: Timechart of Events by Protocol
**Query:**
```spl
index=security_logs | timechart count by protocol
```
**Result:**
| **_time**           | **TCP** | **UDP** |
|----------------------|---------|---------|
| 2024-12-13 10:00:00 | 1       | 0       |
| 2024-12-13 10:05:00 | 1       | 0       |
| 2024-12-13 10:10:00 | 0       | 1       |
| 2024-12-13 10:15:00 | 1       | 0       |
| 2024-12-13 10:20:00 | 1       | 0       |
| 2024-12-13 10:25:00 | 1       | 0       |
| 2024-12-13 10:30:00 | 0       | 1       |
| 2024-12-13 10:35:00 | 1       | 0       |

---

# Recommendations
- Hardening vulnerable protocols (e.g., Telnet, SNMP), and setting alerts for repeated attacks in future.
- No breaches observed, but `192.168.1.2`  is a high-priority threat. block at firewall level to prevent further attempts.
- Blocking traffic from the country as a whole could also be a potential step IF our buisness does not operate there. 