# Post-Quantum Proof of Concept (PoC)

## Dockerized oqs-openssl provider

### How to run as an openssl command (example):
```bash
docker run --rm -itv ./:/home rzepson/oqs-openssl list -kem-algorithms
```
> You can create an alias of the above command.


> You may encounter werid issues wehn using platforms other than amd64. adding --platform=linux/amd64 is recommended.

### How to run in debug mode:
```bash
docker run --entrypoint "" --rm -itv ./:/home rzepson/oqs-openssl bash
```


How to build:
```bash
cd oqs-openssl;
docker buildx build \
--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
--build-arg=GIT_COMMIT=$(git rev-parse --short HEAD) \
--platform linux/386,linux/amd64,linux/arm/v7,linux/arm64,linux/ppc64le,linux/s390x \
-t rzepson/oqs-openssl:1.0 . \
--push
```
