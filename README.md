# Computer Networks Project - Private Network Service Platform

Team: team1 | Domain: `*.team1.test`

Phase 1: DNS (dnsmasq) -> nginx edge (LB + TLS) -> two Python backends, on a private hotspot LAN over IPv6.

## Layout
- `docs/` architecture, topology
- `backend/` backend source (`python3 backend.py A 3001`, `python3 backend.py B 3002`)
- `config/` dnsmasq.conf, nginx.conf, TLS notes
- `scripts/` test helpers
- `evidence/phase1/` screenshots and pcapng per task
- `phase2/` added later

## Run
1. Mac 3: `python3 backend/backend.py A 3001`
2. Mac 4: `python3 backend/backend.py B 3002`
3. Mac 1: apply `config/dnsmasq.conf`, `sudo brew services start dnsmasq`
4. Mac 2: apply `config/nginx.conf`, `nginx -t && sudo nginx`
5. Client: `scripts/lb-test.sh`

Private keys are never committed (see `.gitignore`).
