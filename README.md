# Using Quantum-Safe TLS for HTTPS - Proof of Concept

A student project exploring post-quantum cryptography implementation for TLS in HTTPS connections.

## Overview

This PoC demonstrates quantum-resistant cryptographic algorithms integrated with:
- **OQS-OpenSSL**: Quantum-safe TLS implementation
- **Apache HTTP Server**: Configured with post-quantum cryptography
- **Performance Benchmarks**: Latency, throughput, and handshake measurements

## Project Structure

- `oqs-openssl/` - Dockerized OpenSSL with quantum-safe algorithms
- `oqs-apache/` - Dockerized Apache2 server pre-configured for PQC TLSv1.3
- `benchmarks/` - Performance tests data and visualization scripts

---

> For legacy PoC - please checkout [kcptun](https://github.com/Rzeps0n/post-quantum-poc/tree/kcptun) branch
