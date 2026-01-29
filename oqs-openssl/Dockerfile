FROM debian:stable-slim AS builder

RUN apt update && \
    apt install -y \
        astyle \
        cmake \
        gcc \
        ninja-build \
        libssl-dev \
        python3-pytest \
        python3-pytest-xdist \
        unzip \
        xsltproc \
        doxygen \
        graphviz \
        python3-yaml \
        valgrind \
        git

WORKDIR /opt
RUN git clone -b main \
    https://github.com/open-quantum-safe/oqs-provider.git

WORKDIR oqs-provider
RUN bash scripts/fullbuild.sh
RUN bash scripts/runtests.sh

FROM debian:stable-slim

COPY --from=builder /opt/oqs-provider/.local/lib/* /usr/local/lib/
COPY --from=builder /usr/bin/openssl /usr/bin/
COPY --from=builder /opt/oqs-provider/scripts/openssl-ca.cnf /etc/ssl/
COPY --from=builder /opt/oqs-provider/_build/lib/* /usr/lib/ssl/

ENV LD_LIBRARY_PATH=/usr/local/lib
ENV OPENSSL_APP=/usr/bin/openssl
ENV OPENSSL_CONF=/etc/ssl/openssl-ca.cnf
ENV OPENSSL_MODULES=/usr/lib/ssl/

WORKDIR /home

ENTRYPOINT ["openssl"]
