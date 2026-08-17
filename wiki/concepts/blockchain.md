---
title: Blockchain
type: concept
status: active
confidence: high
cluster: blockchain
domain: [blockchain]
sources: []
updated: 2025-08-27
tags: [Architecture, Blockchain]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
## 📌 Technical Definition

A **blockchain** is a **distributed, append-only database**, structured as a sequence of **cryptographically linked blocks**, and replicated across a **peer-to-peer (P2P) network**.

Each node maintains a full (or partial) copy of the ledger and validates new transactions through a **consensus mechanism** (e.g., Proof of Work, Proof of Stake).

---

## ⚙️ Internal Architecture

1. **Block**
    - A block consists of:
        - **Header**:
            - Hash of the previous block → ensures immutability
            - Timestamp
            - Merkle root (hash of all transactions in the block)
            - Metadata (block number, difficulty, nonce, etc.)
        - **Body**: list of validated transactions.
    - Typical Bitcoin header:
        
        ```
        BlockHeader {
          version
          prev_block_hash
          merkle_root
          timestamp
          difficulty_target
          nonce
        }
        
        ```
        
2. **Transactions**
    - Signed with private keys (asymmetric cryptography, usually **ECDSA secp256k1** or **Ed25519**).
    - Guarantees:
        - Authenticity (the rightful owner issued it),
        - Non-repudiation,
        - Integrity.
3. **Cryptographic Linking**
    - Each block is **hashed** (e.g., SHA-256 for Bitcoin, Keccak-256 for Ethereum).
    - The hash of the previous block is embedded, making the chain immutable—any change invalidates subsequent blocks.

---

## 🔑 Core Properties

- **Immutability**: altering data requires recomputing the entire chain → computationally infeasible.
- **Decentralization**: no single point of control.
- **Byzantine Fault Tolerance (BFT)**: the system remains safe even with malicious nodes.
- **Consensus mechanisms**:
    - **PoW** → security through computational work (hashrate).
    - **PoS** → security through economic stake.
    - Variants: DPoS, PBFT, hybrid approaches.

---

## 📡 Software Engineering View

A blockchain system includes:

- **P2P network** (gossip protocols) for block/tx propagation.
- **State machine or VM**:
    - Bitcoin → UTXO model (simple ledger).
    - Ethereum → EVM (general-purpose state machine).
- **Clients**: full nodes, light clients, archive nodes.
- **Observability stack**: logs, metrics, traces (as in distributed systems).
- **Scalability mechanisms**: sharding, rollups, L2 solutions, DAG-based approaches (Avalanche, IOTA).

---

## 🚀 In Crypto (Practical Usage)

- **Decentralized ledger** for digital assets (BTC, ETH, stablecoins).
- **Smart contracts** (Ethereum, Solana, etc.): self-executing code on the blockchain.
- **Trust via math**: cryptography + consensus replace central authorities.

---

👉 **In short**:

A blockchain is a **distributed, immutable log**, validated collectively via **cryptographic consensus**, serving as the **substrate for trustless systems**.
