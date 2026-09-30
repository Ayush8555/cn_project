# Evidence checklist (Phase 1)
- [ ] A-lan: IP of each Mac, 12 pings (0% loss)
- [ ] B-dns: dig app, dig api (SERVER line visible), nslookup, scutil --dns
- [ ] C-backends: curl Backend A and B (X-Backend header)
- [ ] D-loadbalancing: A,B,A,B loop output
- [ ] E-tls: curl -v without -k, openssl s_client (Verify return code: 0), padlock
- [ ] F-caching: curl -I (Cache-Control, ETag), 304 response
- [ ] G-wireshark: .pcapng for DNS, TCP handshake, TLS handshake + screenshots
- [ ] failures: wrong DNS, wrong record, one backend down, both down (502), wrong port
