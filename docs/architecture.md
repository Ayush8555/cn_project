# Architecture - Private Network Service Platform (Phase 1)

## Machine roles

| Mac | Role | Services | IPv6 (global, stable) | Cloud equivalent |
|---|---|---|---|---|
| Mac 1 (Kidrah) | Private DNS + client | dnsmasq (53) | 2409:40d6:1019:a702:c0d:3813:b0fb:bb38 | Route 53 |
| Mac 2 | Edge reverse proxy + LB + TLS | nginx (80/443) | 2409:40d6:1019:a702:1c96:d0e2:bf6a:ae25 | ALB / CDN edge |
| Mac 3 | Backend A | backend.py (3001) | 2409:40d6:1019:a702:1c7f:850d:6b3b:3039 | App server instance A |
| Mac 4 | Backend B + client | backend.py (3002) | 2409:40d6:1019:a702:1826:abf1:25a2:6be4 | App server instance B |

Domain: `app.team1.test`, `api.team1.test` -> Mac 2.

## Why IPv6
The phone hotspot (Jio) is IPv6-only: Macs received only a /32 464XLAT (clat46) IPv4 address, so IPv4 ping between Macs failed. IPv6 ping succeeded (0% loss), so the whole stack runs on IPv6 (AAAA records, `listen [::]`, backends bound to `::`).

## Request flow
Client -> DNS query (UDP 53, Mac 1) -> TCP 3-way handshake (443, Mac 2) -> TLS handshake -> HTTP request -> nginx round-robin -> Backend A (Mac 3:3001) or Backend B (Mac 4:3002) -> response back.

## Layer mapping
| Protocol | Layer |
|---|---|
| DNS, HTTP | Application |
| TLS | Session / between Application and Transport |
| TCP / UDP | Transport |
| IPv6 | Network |
| Wi-Fi (802.11) | Link |

## Topology
TODO: add `topology.png` (draw.io): phone hotspot in the centre, four Macs attached, role + IPv6 on each.
