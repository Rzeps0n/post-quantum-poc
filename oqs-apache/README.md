# Post-Quantum Proof of Concept (PoC)

## Apache2 docker container with self-signed TLS v1.3 X25519MLKEM768 hybrid key exchange enabled
You must have TLS v1.3 and a browser that supports PQC key exchange for that server to work.

### Run with:
```bash
docker run \
--rm \
-itp 8080:80 \
-p 4333:443 \
rzepson/oqs-apache:latest
```
Your service will be available at: https://localhost:4333

> You can passthrough your own website by adding this argument: `-v /your/website/files:/var/www/html/`

### Run with fresh certificates:
```bash
docker run --rm -itv ./:/home rzepson/oqs-openssl ecparam \
-name prime256v1 \
-genkey -noout \
-out server.key && \
openssl req -x509 -new -key server.key \
-out server.crt \
-days 365 \
-subj "/C=PL/ST=Lesser Poland/L=Cracow/O=AGH University of Cracow/CN=localhost" && \
docker run \
--rm \
-itp 8080:80 \
-p 4333:443 \
-v ./server.key:/etc/ssl/apache2/server.key:ro \
-v ./server.crt:/etc/ssl/apache2/server.crt:ro \
rzepson/oqs-apache:latest
```
> Normal openssl binary will work just fine instead of the oqs-openssl docker image.

### Build:
```bash
cd oqs-apache/;
docker buildx build \
--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
--build-arg=GIT_COMMIT=$(git rev-parse --short HEAD) \
--platform linux/386,linux/amd64,linux/arm/v7,linux/arm64,linux/ppc64le,linux/s390x \
-t rzepson/oqs-apache:1.0 . \
-t rzepson/oqs-apache:latest --push
```
