---
title: Blockchain Layer 1
type: concept
status: draft
confidence: low
cluster: blockchain
domain: [blockchain]
sources: []
updated: 2025-08-27
tags: [Architecture, Blockchain]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# 🌐 What is a **Blockchain**?

A **blockchain** is a **distributed database (ledger)** that records transactions in a way that is:

- **Immutable** → once data is written, it cannot be altered without consensus.
- **Cryptographically secure** → uses hashes, signatures, public/private keys.
- **Decentralized** → maintained by a network of peer nodes (no central authority).

Transactions are grouped into **blocks**, each cryptographically linked to the previous one, forming a **chain of blocks**.

👉 It enables a **shared, verifiable ledger** without a trusted third party.

---

# ⚡ What is a **Blockchain Layer 1 (L1)?**

A **Layer 1** is the **base blockchain protocol** – the foundation of the system.

It defines:

- How transactions are validated (consensus mechanism).
- How blocks are produced.
- How accounts and global state are managed.

👉 Examples: **Bitcoin, Ethereum, Solana, Cardano, Avalanche, Tezos.**

By contrast, a **Layer 2 (L2)** is built **on top of a Layer 1** to improve scalability (throughput), cost (fees), and latency (speed), while relying on the L1 for security.

👉 Examples: **Lightning Network (Bitcoin), Arbitrum/Optimism/zkSync (Ethereum).**

---

# 🏗️ Architecture of a Layer 1 Blockchain

A typical **Layer 1** has four main technical layers:

1. **Network Layer (P2P network)**
    - Node-to-node communication.
    - Propagation of transactions and blocks.
    - Protocols: gossip, P2P networking.
2. **Consensus Layer**
    - Defines how nodes agree on transaction ordering.
    - Examples:
        - **Proof of Work (PoW)** → Bitcoin.
        - **Proof of Stake (PoS)** → Ethereum, Cardano.
        - **Byzantine Fault Tolerance (BFT)** variants → Tendermint (Cosmos).
3. **Data Layer (ledger and storage)**
    - Organizes transactions into blocks.
    - Uses cryptographic linking (hash chains, Merkle trees).
    - Maintains the **global state** (UTXO in Bitcoin, state trie in Ethereum).
4. **Application Layer (execution / smart contracts)**
    - Environment for decentralized applications (dApps).
    - Examples:
        - **Bitcoin Script** (limited scripting).
        - **Ethereum Virtual Machine (EVM)** (Turing-complete).
        - **Solana Sealevel**, **Move VM** (Aptos, Sui).

---

## 📊 Simplified L1 Architecture Diagram

```
+-------------------------------+
| Application Layer             | <- dApps, smart contracts
+-------------------------------+
| Execution Layer               | <- VM (EVM, WASM…), state machine
+-------------------------------+
| Consensus Layer               | <- PoW, PoS, BFT...
+-------------------------------+
| Network Layer (P2P)           | <- peer-to-peer communication
+-------------------------------+
| Data Layer (Blocks, Ledger)   | <- blockchain storage (tx + state)
+-------------------------------+
```

👉 A **Layer 1** blockchain = a **full infrastructure stack** (network + consensus + storage + execution) for decentralized and secure applications.
