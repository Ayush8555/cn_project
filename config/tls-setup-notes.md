# TLS setup (run on Mac 2)

Private keys (`*.key`) are NEVER committed. Only `ca.crt` / `app.crt` may be shared.

```bash
mkdir -p ~/certs && cd ~/certs
openssl genrsa -out ca.key 4096
openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 -subj "/CN=Team1 Local CA" -out ca.crt
openssl genrsa -out app.key 2048
openssl req -new -key app.key -subj "/CN=app.team1.test" -out app.csr
cat > san.ext <<'EOF'
subjectAltName = DNS:app.team1.test, DNS:api.team1.test
basicConstraints = CA:FALSE
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
EOF
openssl x509 -req -in app.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out app.crt -days 365 -sha256 -extfile san.ext
```

Trust on a client (unmanaged Macs):
```bash
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ca.crt
```
Managed Mac: use `curl --cacert ca.crt` instead of installing into the system trust store.
