# Post-Quantum Proof of Concept (PoC)

This student project demonstrates the application of quantum-safe tunnels using a combination of [KCPTun](https://github.com/xtaci/kcptun) and a simple chat application. The goal is to showcase how modern cryptographic techniques can establish secure communication channels that are resistant to potential future attacks by quantum computers.

---

## Components

- **[KCPTun](https://github.com/xtaci/kcptun):** A fast, encrypted UDP-based tunneling protocol that demonstrates post-quantum cryptographic techniques to secure communication.
- **[Chat-Room](https://github.com/cuinjune/chat-room):** A basic web-based chat application that communicates over a quantum-safe tunnel established by KCPTun.
- **Docker Compose:** Orchestrates the setup, ensuring both the KCPTun tunnel and Chat-Room service are running and properly networked.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose plugin
- Docker Buildx plugin (optional)
- Golang (optional)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rzeps0n/post-quantum-poc.git
   cd post-quantum-poc
   ```

2. **Ensure the database file exists:**

   The chat-room stores messages in a `data.json` file located in the `db/` folder. Create one if it doesn't already exist:

   ```bash
   mkdir db
   echo '{"numVisitors": 0, "data": []}' > ./db/data.json
   ```

3. **Build and start the services:**

   Use Docker Compose to build and start both the KCPTun and Chat-Room services:

   ```bash
   docker-compose up -d
   ```

4. **Access the Chat-Room:**

   Once the services are up, you can access the chat-room application at:

   ```
   http://your-endpoint:3000
   ```

   The chat-room will be securely tunneled over a quantum-safe channel through KCPTun, using UDP port 4000.

---

## Stopping the Services

To stop the running services, use the following command:

```bash
docker-compose down
```

---

## Connecting from the Client-Side

To connect to the KCPTun server from a client machine, follow these steps:

1. **Build the KCPTun client (optional):**

   You can either build the client from source or download a pre-built binary from the [KCPTun releases page](https://github.com/xtaci/kcptun/releases).

   To build from source:

   ```bash
   git clone https://github.com/xtaci/kcptun.git
   cd kcptun
   go build -mod=vendor -ldflags "-X main.VERSION=$(date -u +%Y%m%d) -s -w" -o client github.com/xtaci/kcptun/client
   ```

3. **Run the KCPTun client:**

   Replace `your-endpoint` with your actual server endpoint (the public IP or domain name of the machine running KCPTun). The `-r` flag specifies the remote server's address and port, while the `-l` flag defines the local port the client listens on.

   ```bash
   ./client -r 'your-endpoint:4000' -l ':3000' -mode fast3 -nocomp -crypt Salsa20 -QPP -QPPCount 101 -smuxver 2
   ```

    or you can use docker!

    ```bash
    docker run -d --name kcptun-client --restart unless-stopped -p 3000:3000/udp -e TUNNELED_IP=localhost -e TUNNELED_PORT=4000 rzepson/kcptun-client:1.0
  ```

   Once the client is running, it will establish a secure tunnel to the KCPTun server on the specified endpoint. You can now interact with the Chat-Room service securely via `localhost:3000`.

---

## Project Purpose

This project demonstrates the potential of quantum-safe encryption techniques in modern applications. As quantum computers continue to advance, many existing cryptographic protocols (like RSA and ECC) may become vulnerable. Exploring and developing quantum-resistant systems is critical to securing future communication.

By using [KCPTun](https://github.com/xtaci/kcptun), this project highlights the feasibility of secure, quantum-resistant communication tunnels, ensuring privacy even in a post-quantum world.
