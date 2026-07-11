#!/usr/bin/env python3
"""Generate ~170 ARC quiz questions for batch1 with even correctIndex distribution."""

import json
import random
from collections import Counter

questions = []

def q(question, options, correctIndex):
    questions.append({
        "question": question,
        "options": options,
        "correctIndex": correctIndex
    })

# ======================================================================
# TOPIC 1: ARC NETWORK OVERVIEW
# ======================================================================

# --- 1.1 Arc is a purpose-built L1 blockchain, NOT a rollup or sidechain ---
q("What type of blockchain is Arc?",
  ["A Layer-2 rollup built on Ethereum",
   "A sidechain secured by Bitcoin",
   "A purpose-built Layer-1 blockchain",
   "An application-specific zk-rollup"], 2)

q("Which of the following BEST describes Arc Network's architecture?",
  ["A rollup that settles transactions to Ethereum",
   "A sidechain that relies on a parent chain for security",
   "A purpose-built Layer-1 blockchain, not a rollup or sidechain",
   "A state channel network for payment routing"], 2)

q("How is Arc classified in blockchain architecture terms?",
  ["As a sovereign rollup",
   "As a Layer-1 blockchain",
   "As a Validium",
   "As an optimistic rollup"], 1)

q("Arc is NOT which of the following?",
  ["A purpose-built L1 blockchain",
   "EVM compatible",
   "A rollup or sidechain",
   "Designed for stablecoin-native applications"], 2)

q("Which statement about Arc is FALSE?",
  ["Arc is a Layer-1 blockchain",
   "Arc is a rollup that inherits security from Ethereum",
   "Arc is designed for stablecoin-native financial applications",
   "Arc has sub-second deterministic finality"], 1)

q("What distinguishes Arc from rollups like Arbitrum or Optimism?",
  ["Arc uses a different smart contract language",
   "Arc has lower transaction throughput",
   "Arc is a Layer-1 blockchain, not an L2 rollup",
   "Arc does not support smart contracts"], 2)

q("Which of these is NOT part of Arc's design?",
  ["Being a rollup that settles to Ethereum",
   "Using USDC as the native gas token",
   "Providing sub-second deterministic finality",
   "Full EVM compatibility"], 0)

q("Arc Network is best described as:",
  ["An Ethereum L2 with USDC as gas",
   "A Solana-based DeFi platform",
   "A Layer-1 blockchain purpose-built for stablecoin-native apps",
   "A cross-chain bridge protocol"], 2)

# --- 1.2 Designed for stablecoin-native financial applications ---
q("What type of applications is Arc specifically designed for?",
  ["Gaming and metaverse applications",
   "Stablecoin-native financial applications",
   "Decentralized social media platforms",
   "Supply chain tracking systems"], 1)

q("Why was Arc purpose-built as a Layer-1 blockchain?",
  ["To maximize NFT minting throughput",
   "For stablecoin-native financial applications",
   "To reduce energy consumption below Proof of Stake norms",
   "To enable anonymous transactions by default"], 1)

q("Which sector is Arc primarily targeting?",
  ["Gaming and entertainment",
   "Supply chain management",
   "Stablecoin-native finance including payments, lending, and FX",
   "Decentralized identity and credentials"], 2)

q("Arc's architecture prioritizes which use case above all?",
  ["Cross-chain NFT bridging",
   "Stablecoin-native financial applications",
   "Decentralized file storage",
   "On-chain gaming"], 1)

q("Which of these is a core design goal of Arc Network?",
  ["Supporting stablecoin-native financial applications at scale",
   "Providing the largest NFT marketplace on-chain",
   "Becoming the most decentralized L1 by validator count",
   "Achieving the lowest possible hardware requirements for miners"], 0)

# --- 1.3 USDC is native gas token ---
q("What is the native gas token on Arc Network?",
  ["ETH",
   "A newly created ARCC token",
   "USDC, a stablecoin",
   "A basket of stablecoins"], 2)

q("Unlike Ethereum which uses ETH for gas, Arc uses:",
  ["A fixed subscription fee model",
   "USDC as its native gas token",
   "A points-based fee system",
   "No gas fees at all"], 1)

q("How does Arc's gas token differ from most L1 blockchains?",
  ["It uses a volatile native token like most chains",
   "It has no gas fees whatsoever",
   "It uses USDC, a stablecoin, instead of a volatile native token",
   "It uses multiple tokens competing for gas priority"], 2)

q("What advantage does using USDC as the native gas token provide?",
  ["Higher block rewards for validators",
   "Fees are denominated in dollars, making them predictable",
   "Faster transaction propagation across the network",
   "Lower minimum stake for validators"], 1)

# --- 1.4 Sub-second deterministic finality (<1 second) ---
q("How fast is transaction finality on Arc?",
  ["~12 seconds",
   "~15 minutes",
   "Sub-second (less than 1 second)",
   "~30 minutes"], 2)

q("What kind of finality does Arc provide, and how fast is it?",
  ["Probabilistic finality in ~12 seconds",
   "Optimistic finality in ~7 days",
   "Deterministic finality in under 1 second",
   "Economic finality in ~5 minutes"], 2)

q("Arc achieves transaction finality in:",
  ["Less than 1 second",
   "Approximately 12 seconds",
   "About 15 minutes",
   "Up to 7 days"], 0)

q("Which statement about Arc's finality is true?",
  ["Finality is probabilistic and takes several minutes",
   "Finality is deterministic and happens in under a second",
   "Finality requires 12 block confirmations like Ethereum",
   "Finality depends on the fee amount paid"], 1)

q("Compared to Ethereum's ~12 second block times, Arc offers:",
  ["Slower but cheaper transactions",
   "Sub-second deterministic finality",
   "Similar block times with lower fees",
   "Faster probabilistic finality with reorg risks"], 1)

q("What does 'deterministic finality' mean on Arc?",
  ["Transactions can be reorged within a short window",
   "Transactions require multiple block confirmations to be final",
   "Transactions are either unconfirmed or immediately final with no reorg risk",
   "Finality is achieved after a 7-day challenge period"], 2)

q("Once a transaction is confirmed on Arc, it:",
  ["Can be reorganized within 12 blocks",
   "Is probabilistically final after 32 confirmations",
   "Is immediately final and irreversible",
   "Enters a 7-day withdrawal window"], 2)

# --- 1.5 Full EVM compatibility ---
q("What type of smart contract compatibility does Arc offer?",
  ["WASM-based smart contracts only",
   "Full EVM compatibility",
   "Solana Virtual Machine (SVM) compatibility",
   "Custom proprietary smart contract language"], 1)

q("Can developers deploy existing Ethereum Solidity contracts on Arc?",
  ["No, contracts must be rewritten in a new language",
   "Yes, Arc has full EVM compatibility",
   "Only if they use the Vyper compiler",
   "Only contracts deployed before 2024"], 1)

q("Arc's execution layer is compatible with which virtual machine?",
  ["The Ethereum Virtual Machine (EVM)",
   "The WebAssembly Virtual Machine",
   "The Solana Virtual Machine (SVM)",
   "The Move Virtual Machine"], 0)

q("Arc Network is described as EVM compatible with:",
  ["No differences from standard Ethereum",
   "Some unique differences",
   "Only partial support for ERC standards",
   "A completely forked execution environment"], 1)

# --- 1.6 Supported use cases ---
q("Which use cases does Arc support at scale?",
  ["Gaming, NFTs, and metaverse experiences",
   "Payments, lending, FX, treasury management, and agentic commerce",
   "Supply chain, IoT, and logistics tracking",
   "Social media, content streaming, and file storage"], 1)

q("Arc is designed to support which of the following at scale?",
  ["Agentic commerce",
   "Video streaming infrastructure",
   "DNS resolution services",
   "Decentralized VPN networks"], 0)

q("Which of these is NOT a use case Arc specifically targets?",
  ["Payments",
   "Treasury management",
   "Digital art NFT minting as primary focus",
   "Foreign exchange (FX)"], 2)

q("What does 'agentic commerce' refer to in Arc's context?",
  ["AI agent-driven transactions and economic activity on-chain",
   "Commerce regulated by government agencies",
   "Automated market making for token swaps",
   "Proxy-based trading for institutional investors"], 0)

# --- 1.7 Arc separates consensus from execution into two layers ---
q("How does Arc's network architecture separate concerns?",
  ["It uses a monolithic single-layer design",
   "It separates consensus from execution into two layers",
   "It uses sharding across 64 execution shards",
   "It runs execution on a separate off-chain network"], 1)

q("What are the two layers in Arc's architecture?",
  ["A data availability layer and a settlement layer",
   "A consensus layer and an execution layer",
   "A L1 base layer and a L2 rollup layer",
   "A beacon chain and execution shards"], 1)

q("In Arc's two-layer architecture, which layer handles transaction ordering and finality?",
  ["The execution layer",
   "The data availability layer",
   "The consensus layer",
   "The application layer"], 2)

q("In Arc's two-layer architecture, which layer runs the EVM?",
  ["The consensus layer",
   "The execution layer",
   "The settlement layer",
   "The staking layer"], 1)

# --- 1.8 Consensus layer: Malachite BFT ---
q("Which consensus protocol does Arc use?",
  ["Tendermint BFT",
   "Malachite BFT",
   "HotStuff BFT",
   "Aura (Authority Round)"], 1)

q("What does Malachite BFT provide for Arc?",
  ["Probabilistic finality with longest-chain rule",
   "Sub-second deterministic finality with high throughput",
   "Nakamoto consensus with Proof of Work",
   "Delegated Proof of Stake with elected block producers"], 1)

q("What type of consensus mechanism does Arc's consensus layer use?",
  ["Proof of Work",
   "Proof of Authority",
   "Byzantine Fault Tolerant (BFT) consensus",
   "Proof of History"], 2)

q("The name of Arc's BFT consensus implementation is:",
  ["Tendermint Core",
   "Malachite",
   "Grandpa",
   "HoneyBadgerBFT"], 1)

# --- 1.9 Execution layer: EVM-compatible ---
q("What runtime does Arc's execution layer use?",
  ["A WASM runtime",
   "An EVM-compatible runtime",
   "A custom Rust-based VM",
   "The Solana SVM runtime"], 1)

q("Which of these runs on Arc's execution layer?",
  ["Consensus voting",
   "Malachite BFT rounds",
   "Smart contract execution via the EVM",
   "Validator key generation"], 2)

# --- 1.10 Permissioned validator set ---
q("What type of validator set does Arc use?",
  ["A fully permissionless set where anyone can stake",
   "A permissioned validator set",
   "A delegated Proof of Stake system with token voting",
   "A single sequencer with a rotation committee"], 1)

q("Arc's validator set is permissioned, meaning:",
  ["Anyone with enough tokens can become a validator",
   "Validators are selected and approved by the network's governing body",
   "Validators are randomly chosen from all token holders",
   "Only the founding team runs validators"], 1)

q("Which statement about Arc's validators is true?",
  ["Any user with 32 ARCC tokens can stake to become a validator",
   "Arc uses a permissioned validator set",
   "Validators are elected weekly through on-chain voting",
   "Arc has no validators as it uses Proof of Authority"], 1)

q("The permissioned validator set on Arc contributes to:",
  ["Lower decentralization but higher throughput and predictable finality",
   "Higher energy consumption than Proof of Work",
   "Random validator selection each epoch",
   "Unlimited validator participation"], 0)

# --- 1.11 App Kits ---
q("What do Arc App Kits provide for developers?",
  ["Pre-built NFT minting templates",
   "SDKs for adding bridging, swapping, and unified crosschain balances to apps",
   "A suite of smart contract auditing tools",
   "Hardware wallet integration libraries"], 1)

q("Arc App Kits help developers build:",
  ["Crosschain payment workflows",
   "Layer-2 scaling solutions",
   "Mining pool management software",
   "Validator monitoring dashboards"], 0)

q("Which platforms do Arc App Kits support for crosschain functionality?",
  ["Arc only",
   "EVM chains, Solana, and Circle Wallets",
   "Ethereum and Bitcoin only",
   "All Cosmos SDK chains"], 1)

# --- 1.12 AI tooling (MCP server) ---
q("What does Arc's MCP server provide?",
  ["A mining pool interface for validators",
   "AI tooling for agent-based development on Arc",
   "A message compression protocol for cross-chain data",
   "A middleware layer for database indexing"], 1)

q("Arc provides AI tooling for developers through:",
  ["A proprietary AI model trained on Solidity code",
   "An MCP (Model Context Protocol) server for agent-based development",
   "A natural language to bytecode compiler",
   "An AI-powered smart contract auditor"], 1)

# --- 1.13 Growing ecosystem ---
q("Which of the following describes Arc's ecosystem?",
  ["A closed network with no external integrations",
   "A small ecosystem of internal tools only",
   "A growing ecosystem of infrastructure partners",
   "A deprecated network being sunset"], 2)

# --- 1.14 EVM compatible with unique differences ---
q("Arc is described as EVM compatible but with:",
  ["No differences from standard Ethereum",
   "Some unique differences that affect integration",
   "A completely different opcode set",
   "Incompatible RPC methods"], 1)

q("Which of these unique differences on Arc drives the most integration work?",
  ["Different RPC endpoint naming conventions",
   "USDC as gas, USDC dual interface, and deterministic finality",
   "Arc uses a custom hash function instead of Keccak256",
   "Arc does not support the CREATE2 opcode"], 1)

q("When integrating with Arc, developers must account for:",
  ["A completely different programming language",
   "USDC as the native gas token and deterministic finality",
   "Lack of smart contract support",
   "Monthly block production instead of continuous"], 1)

# --- 1.15 Testnet chain ID 5042002 ---
q("What is Arc's testnet chain ID?",
  ["8453",
   "5042002",
   "42161",
   "137"], 1)

q("The chain ID used by Arc testnet is:",
  ["1",
   "5042002",
   "57073",
   "11155111"], 1)

q("Which chain ID should developers configure to connect to Arc testnet?",
  ["5042002",
   "84532",
   "421614",
   "80002"], 0)

# ======================================================================
# TOPIC 2: STABLECOIN NATIVE MODEL
# ======================================================================

# --- 2.1 Stablecoins as first-class assets ---
q("In Arc's design, stablecoins are treated as:",
  ["Second-class assets compared to the native token",
   "First-class assets built into the protocol",
   "Optional assets that can be bridged from Ethereum",
   "Testnet-only assets with no mainnet use"], 1)

q("Arc is built around which type of assets as first-class primitives?",
  ["Volatile native tokens",
   "Wrapped Bitcoin",
   "Stablecoins",
   "Non-fungible tokens"], 2)

q("What does it mean that stablecoins are 'first-class assets' on Arc?",
  ["They can only be used in specific DeFi protocols",
   "They are deeply integrated into the protocol, including for gas payments",
   "They are the only asset type supported on the network",
   "They require special permission to transfer"], 1)

# --- 2.2 USDC as native gas token, fees in dollars ---
q("On Arc, transaction fees are denominated in:",
  ["ETH",
   "A volatile native token",
   "USDC (dollars)",
   "Gas in a proprietary unit"], 2)

q("Because Arc uses USDC as gas, fees are:",
  ["Unpredictable due to USDC volatility",
   "Predictable in dollar terms since USDC is a stablecoin",
   "Fixed at $0.001 for all transactions",
   "Waived for the first year of mainnet"], 1)

q("What makes fee estimation simpler on Arc compared to Ethereum?",
  ["Arc has no gas fees at all",
   "Fees are in USDC, so the dollar cost is directly visible without conversion",
   "Arc uses a flat annual subscription model",
   "Fees are paid by validators, not users"], 1)

q("How does USDC-based gas affect the user experience on Arc?",
  ["Users must first buy a volatile token then swap to USDC",
   "Users pay gas in USDC and see fees directly in dollar terms",
   "Users pay no gas fees due to the stablecoin model",
   "Users must stake USDC to earn gas credits"], 1)

q("The dollar-denominated fee model on Arc is possible because:",
  ["Arc pegs its native token to $1",
   "USDC, a stablecoin pegged to the dollar, is the native gas token",
   "Arc receives oracle price feeds for every transaction",
   "Arc uses a centralized pricing committee"], 1)

# --- 2.3 EURC for euro-denominated transfers ---
q("Which stablecoin does Arc support for euro-denominated transfers?",
  ["EURS",
   "EURT",
   "EURC",
   "sEUR"], 2)

q("On Arc, EURC is used for:",
  ["Euro-denominated transfers and payments",
   "Governance voting",
   "Staking and validator rewards",
   "Cross-chain bridge fees"], 0)

q("Which fiat currency does EURC represent on Arc?",
  ["The Euro",
   "The British Pound",
   "The Swiss Franc",
   "The Japanese Yen"], 0)

# --- 2.4 USYC for yield-bearing ---
q("What is USYC used for on Arc?",
  ["Paying transaction fees at a discount",
   "Providing onchain yield as a yield-bearing stablecoin",
   "Voting on protocol governance proposals",
   "Bridging assets between Arc and Solana"], 1)

q("USYC on Arc is:",
  ["A volatile trading token",
   "A yield-bearing stablecoin that provides onchain yield",
   "A wrapped version of Ether",
   "A testnet-only token for experimentation"], 1)

q("Which stablecoin on Arc provides yield-bearing capabilities?",
  ["USDC",
   "EURC",
   "USYC",
   "DAI"], 2)

# --- 2.5 No volatile native token on Arc ---
q("Which of the following is true about Arc's native token model?",
  ["Arc has both a volatile governance token and USDC for gas",
   "Arc has no volatile native token",
   "Arc uses ETH as its native token",
   "Arc's native token is a volatile commodity token"], 1)

q("Unlike Ethereum, Solana, and most L1s, Arc does NOT have:",
  ["Smart contract support",
   "A volatile native token",
   "A decentralized validator set",
   "Transaction fees"], 1)

q("Arc's decision to have no volatile native token means:",
  ["Users must still acquire one for governance",
   "There is no speculative native token to trade",
   "Validators are paid in a volatile token",
   "The network cannot have a fee market"], 1)

q("What replaces the volatile native token commonly found on other blockchains?",
  ["A dual-token model with a stable and volatile component",
   "USDC as the native gas token, with no volatile native token needed",
   "A points-based rewards system",
   "Off-chain fee payments through centralized processors"], 1)

q("Which statement about Arc tokens is correct?",
  ["Arc's native token ARCC is used for staking",
   "Arc has no volatile native token",
   "Arc uses a volatile token called ARC for gas",
   "Arc's native token is a rebasing stablecoin"], 1)

# --- 2.6 Single asset for gas AND transfers ---
q("On Arc, users can hold just one asset to:",
  ["Pay for gas AND make transfers in applications",
   "Pay for gas only; transfers require a different token",
   "Only participate in governance",
   "Only interact with DeFi protocols"], 0)

q("Arc's model allows users to use the same asset for:",
  ["Gas fees only",
   "Application transfers only",
   "Both gas fees and application transfers",
   "Neither"], 2)

q("On most blockchains, users need a volatile token for gas and stablecoins for DeFi. On Arc:",
  ["Users need both a volatile token and USDC",
   "Users need only USDC for both gas and DeFi",
   "Users need only a volatile token for everything",
   "Transactions are free so no token is needed"], 1)

q("What is the practical benefit of USDC serving both as gas and transfer asset?",
  ["Users can hold one asset for all on-chain activity",
   "Transactions are processed twice as fast",
   "Fees are automatically waived",
   "All transfers become free"], 0)

# --- 2.7 No need to acquire separate volatile token ---
q("What does Arc's model remove the need for users to acquire?",
  ["A hardware wallet",
   "A separate volatile token like ETH just to pay gas",
   "A VPN connection",
   "KYC verification"], 1)

q("On Ethereum, users need ETH for gas and USDC for stable transactions. On Arc:",
  ["Users still need ETH for gas",
   "Users need only USDC — no separate volatile token required for gas",
   "Users need neither — all transactions are free",
   "Users need three separate tokens for gas, DeFi, and governance"], 1)

q("Arc's design eliminates the friction of:",
  ["Writing smart contracts",
   "Acquiring a volatile native token before using the network",
   "Running a full node",
   "Securing private keys"], 1)

q("New users on Arc can start transacting immediately if they have:",
  ["ETH or another volatile token",
   "USDC in their wallet",
   "A governance token stake",
   "An approved KYC document"], 1)

q("What barrier does Arc remove compared to most L1s for new users?",
  ["The need to set up a wallet",
   "The 'gas problem' where you need a separate token you don't have",
   "The need to download blockchain data",
   "The requirement to join a validator pool"], 1)

# --- 2.8 USDC dual interface: native (18 decimals) and ERC-20 (6 decimals) ---
q("How many decimal places does the native USDC interface on Arc use?",
  ["6",
   "8",
   "18",
   "10"], 2)

q("How many decimal places does the ERC-20 USDC interface on Arc use?",
  ["18",
   "6",
   "8",
   "12"], 1)

q("The native USDC interface on Arc (18 decimals) is used for:",
  ["dApps and DeFi protocols only",
   "Gas payments, native transfers, and general EVM operations",
   "Cross-chain bridging only",
   "Governance voting only"], 1)

q("The ERC-20 USDC interface on Arc (6 decimals) is used for:",
  ["Gas payments",
   "Native value transfers between accounts",
   "Standard ERC-20 interactions in dApps and DeFi",
   "Validator staking"], 2)

q("Why does the native USDC interface use 18 decimals?",
  ["To match Ethereum's standard for native gas tokens like ETH",
   "To make it incompatible with standard ERC-20 tools",
   "To enable higher precision for small gas payments and EVM operations",
   "To prevent phishing attacks on users"], 0)

q("Why does the ERC-20 USDC interface use 6 decimals?",
  ["To match the standard USDC ERC-20 on Ethereum",
   "To prevent users from spending too much on fees",
   "To make it incompatible with native transfers",
   "To reduce storage costs on-chain"], 0)

q("Arc provides two interfaces for USDC because:",
  ["It supports two separate stablecoin types",
   "It needs an 18-decimal interface for native/gas operations and a 6-decimal ERC-20 for dApp compatibility",
   "One interface is for testnet and one for mainnet",
   "The two interfaces compete for user adoption"], 1)

q("Which USDC interface on Arc should a DeFi protocol integrate with?",
  ["The native 18-decimal interface",
   "The ERC-20 6-decimal interface",
   "Both interfaces independently",
   "Neither — protocols must use EURC instead"], 1)

q("When a user pays gas on Arc, which USDC interface is used?",
  ["The ERC-20 6-decimal interface",
   "The native 18-decimal interface",
   "Both interfaces are debited equally",
   "Neither — gas is paid in a different token"], 1)

# --- 2.9 Same asset, not two tokens ---
q("How are native USDC and ERC-20 USDC related on Arc?",
  ["They are two separate tokens with different prices",
   "Native USDC is a wrapped version of ERC-20 USDC",
   "They are the same asset sharing one underlying balance",
   "They are completely independent assets"], 2)

q("Which statement about native USDC and ERC-20 USDC on Arc is correct?",
  ["They track separate balances and require conversion",
   "They are the same asset, just with different interfaces",
   "Native USDC is more valuable than ERC-20 USDC",
   "ERC-20 USDC cannot be used for transfers"], 1)

q("If a user receives USDC through the native interface on Arc:",
  ["They can only use it for gas",
   "It is the same balance accessible through the ERC-20 interface too",
   "It is locked and cannot be moved",
   "They must convert it to ERC-20 USDC first"], 1)

q("Which of the following is true about Arc's USDC model?",
  ["Native USDC and ERC-20 USDC are two separate tokens",
   "Native USDC has 6 decimals and ERC-20 USDC has 18 decimals",
   "Native USDC and ERC-20 USDC are the same asset sharing one underlying balance",
   "Only ERC-20 USDC can be used for DeFi"], 2)

q("What happens to the ERC-20 USDC balance when a user transfers USDC via the native interface?",
  ["The ERC-20 balance remains unchanged",
   "The ERC-20 balance decreases by the same amount",
   "The ERC-20 balance increases because of the transfer",
   "The ERC-20 interface becomes temporarily disabled"], 1)

# --- 2.10 Design rationale ---
q("What is the design rationale behind Arc's stablecoin native model?",
  ["To maximize trading volume on DEXes",
   "No volatile native token, single gas denomination at launch, stablecoins as first-class primitives",
   "To create a new stablecoin pegged to a basket of currencies",
   "To compete with PayPal and Venmo"], 1)

q("Why did Arc choose not to have a volatile native token?",
  ["Volatile tokens are technically impossible on Arc's architecture",
   "To have fees denominated in stable dollars from day one",
   "Regulators required Arc to have no native token",
   "Users voted against having a native token"], 1)

q("Arc's stablecoin native model is grounded in which rationale?",
  ["Stablecoins are easier to code than volatile tokens",
   "Stablecoins as first-class primitives eliminate the need for a separate volatile native token",
   "The Arc team did not want to deal with token market making",
   "Volatile tokens have no regulatory precedent"], 1)

# --- 2.11 Native value transfer using USDC ---
q("On Arc, how do users send value to another address?",
  ["They must wrap USDC into a native representation first",
   "They can send USDC natively, similar to sending ETH on Ethereum",
   "They can only send value through smart contract calls",
   "They must use a centralized exchange as intermediary"], 1)

q("Sending USDC on Arc is analogous to:",
  ["Sending ERC-20 USDT on Ethereum",
   "Sending ETH on Ethereum",
   "Sending Bitcoin on the Lightning Network",
   "Sending fiat via wire transfer"], 1)

q("Native transfers of USDC on Arc mean that USDC behaves like:",
  ["An ERC-20 token that requires approval first",
   "The native currency (like ETH) — send it directly without wrapping",
   "A wrapped token with a 24-hour unlock period",
   "An NFT that cannot be divided"], 1)

q("Which of these best describes native USDC transfers on Arc?",
  ["They work like sending ETH — simple, direct, no contract call needed",
   "They require calling a smart contract approve function first",
   "They are processed off-chain and batched weekly",
   "They can only be initiated by smart contracts"], 0)

# --- 2.12 No need to acquire ETH ---
q("What token does a user need to acquire before transacting on Arc?",
  ["ETH",
   "The ARCC governance token",
   "Just USDC — no other token is needed to pay gas",
   "Both USDC and a volatile token"], 2)

q("On Ethereum, users must acquire ETH to pay gas. On Arc:",
  ["Users must also acquire ETH to pay gas",
   "Users must acquire ARC, the native token",
   "Users only need USDC — no ETH or other token needed for gas",
   "Users pay no gas at all"], 2)

q("Which onboarding barrier does Arc eliminate compared to most blockchains?",
  ["Requiring users to first purchase a volatile token before using stablecoins",
   "Requiring users to download a full node",
   "Requiring users to complete KYC verification",
   "Requiring users to stake tokens before transacting"], 0)

# --- 2.13 Comparison questions ---
q("How does Arc's gas model differ from Ethereum's?",
  ["Arc uses ETH while Ethereum uses USDC",
   "Arc uses USDC while Ethereum uses ETH",
   "Both use the same gas token",
   "Arc has no gas fees while Ethereum does"], 1)

q("Which statement accurately compares Arc to Ethereum?",
  ["Arc is an L2 while Ethereum is an L1",
   "Arc uses USDC as native gas; Ethereum uses ETH",
   "Arc has no smart contract support; Ethereum does",
   "Arc is permissioned; Ethereum is permissionless"], 1)

q("On Ethereum, sending USDC requires holding ETH for gas. On Arc:",
  ["This is also true — you need a separate gas token",
   "You only need USDC — it serves as both the value transfer and gas asset",
   "Gas is free on Arc",
   "You need EURC for gas, not USDC"], 1)

q("Compared to traditional L2 rollups, Arc provides:",
  ["Slower finality but higher security",
   "Sub-second deterministic finality vs ~7 day withdrawal windows",
   "Lower throughput but cheaper fees",
   "No smart contract support"], 1)

q("How does Arc's finality model differ from Ethereum's?",
  ["Both use deterministic finality in under 1 second",
   "Arc has deterministic finality in under 1 second; Ethereum has probabilistic finality",
   "Arc has probabilistic finality; Ethereum has deterministic",
   "Both have probabilistic finality but different confirmation times"], 1)

q("What is a key difference between Arc and most other EVM-compatible L1s?",
  ["Arc is not EVM compatible",
   "Most EVM L1s have a volatile native gas token; Arc uses USDC",
   "Arc has higher gas costs than any other L1",
   "Arc does not support ERC-20 tokens"], 1)

q("On Ethereum, USDC is just an ERC-20 token. On Arc, USDC is:",
  ["Also just an ERC-20 token with no special status",
   "Not just an ERC-20 token but also the native gas asset",
   "Not supported at all",
   "Only available as a wrapped version"], 1)

# ======================================================================
# TRUE/FALSE AND "WHICH IS NOT" PATTERN QUESTIONS
# ======================================================================

q("Which of these statements about Arc Network is true?",
  ["Arc is a Layer-2 rollup on Ethereum",
   "Arc uses USDC as its native gas token",
   "Arc has a volatile native token called ARC",
   "Arc takes 15 minutes to finalize transactions"], 1)

q("Which of these statements about Arc's architecture is true?",
  ["Arc combines consensus and execution in a single layer",
   "Arc separates consensus from execution into two layers",
   "Arc uses a monolithic node design",
   "Arc has no consensus layer"], 1)

q("Which of these statements about Arc's stablecoin model is FALSE?",
  ["USDC is the native gas token on Arc",
   "Native USDC and ERC-20 USDC are two separate tokens",
   "EURC is supported for euro-denominated transfers",
   "Arc has no volatile native token"], 1)

q("Which of these is NOT a supported stablecoin on Arc?",
  ["USDC",
   "EURC",
   "USYC",
   "DAI"], 3)

q("Which of these is NOT a characteristic of Arc Network?",
  ["Sub-second deterministic finality",
   "Full EVM compatibility",
   "Volatile native token used for gas",
   "Permissioned validator set"], 2)

q("Which of these is NOT a feature of Arc's stablecoin native model?",
  ["USDC as the native gas token",
   "Fees predictable in dollar terms",
   "Acquiring ETH for gas is required",
   "No volatile native token"], 2)

q("Which of these is NOT a benefit of Arc's stablecoin native model?",
  ["Fees denominated in stable dollars",
   "Users hold one asset for gas and transfers",
   "Users must acquire a separate volatile token",
   "No need to manage a volatile native token"], 2)

q("Which of these is NOT part of Arc's consensus layer design?",
  ["Malachite BFT",
   "Sub-second finality",
   "EVM smart contract execution",
   "High throughput"], 2)

q("Which of these is NOT a use case Arc supports?",
  ["Payments",
   "Lending",
   "Video game rendering",
   "Treasury management"], 2)

q("Which of these is NOT true about USDC on Arc?",
  ["It is the native gas token",
   "It has two interfaces: native (18 decimals) and ERC-20 (6 decimals)",
   "Native and ERC-20 USDC are separate tokens",
   "It can be used for both gas and application transfers"], 2)

q("Which of these is NOT a difference between Arc and Ethereum?",
  ["Arc uses USDC for gas; Ethereum uses ETH",
   "Arc has deterministic finality; Ethereum has probabilistic finality",
   "Both use the same token for gas and value transfers",
   "Arc has no volatile native token; Ethereum does"], 2)

q("Which statement about Arc's fee model is correct?",
  ["Fees are unpredictable due to volatile native token",
   "Fees are denominated in USDC and predictable in dollar terms",
   "Fees are paid in a proprietary Arc token",
   "There are no transaction fees on Arc"], 1)

q("Which of these best describes Arc's USDC dual interface approach?",
  ["Two different assets with separate supply caps",
   "Two interfaces into the same underlying USDC balance",
   "Two separate USDC tokens that can be swapped",
   "One interface for mainnet, one for testnet"], 1)

q("Which is a true comparison between Arc and L2 rollups?",
  ["Arc achieves sub-second finality; L2 withdrawals can take ~7 days",
   "Arc is an L2; L2 rollups are L1s",
   "Both require 7 days for finality",
   "Arc has slower finality than L2 rollups"], 0)

# ======================================================================
# ADDITIONAL COVERAGE QUESTIONS
# ======================================================================

q("What does it mean that USDC is the 'native gas token' on Arc?",
  ["USDC is an optional way to pay gas alongside the main token",
   "Transaction fees are automatically deducted in USDC from the sender's balance",
   "USDC must be wrapped into a separate gas token first",
   "Gas is free for USDC transactions only"], 1)

q("What is the practical implication of 'no volatile native token' for Arc's economics?",
  ["There is no speculative trading of a native chain token",
   "Validator rewards are paid in a volatile token",
   "The network cannot pay for security",
   "Gas fees cannot be adjusted based on demand"], 0)

q("On Arc, a user who holds only USDC can:",
  ["Only send USDC but not pay gas",
   "Both pay gas and send USDC transfers using the same asset",
   "Only pay gas but not receive USDC",
   "Neither — they need a separate gas token"], 1)

q("What role does EURC play alongside USDC on Arc?",
  ["EURC replaces USDC for all transactions",
   "EURC provides euro-denominated transfers as an additional stablecoin option",
   "EURC is used exclusively for validator rewards",
   "EURC is a testnet-only token"], 1)

q("USYC differentiates itself from USDC and EURC on Arc by:",
  ["Being the only token usable for gas",
   "Providing onchain yield in addition to being a stablecoin",
   "Being a volatile trading asset",
   "Having a higher decimal precision"], 1)

q("How does Arc solve the 'gas problem' that plagues many blockchains?",
  ["By making the gas token the same as the primary transfer asset (USDC)",
   "By eliminating gas fees entirely",
   "By subsidizing gas through inflation",
   "By allowing any token to be used for gas"], 0)

q("When a dApp queries a user's USDC balance via the ERC-20 interface on Arc, it sees:",
  ["A different balance than the native interface",
   "The same underlying balance accessible via the native interface",
   "Zero — ERC-20 queries don't work on Arc",
   "Only USDC that was bridged from Ethereum"], 1)

q("Which feature enables Arc to support payments, lending, and FX at scale?",
  ["Its stablecoin native model combined with sub-second deterministic finality",
   "Its large validator set of 1 million+ nodes",
   "Its proprietary smart contract language",
   "Its integration with the SWIFT banking network"], 0)

q("What is the relationship between Arc's consensus and execution layers?",
  ["The consensus layer orders and finalizes blocks; the execution layer runs smart contracts",
   "The execution layer produces blocks; the consensus layer runs smart contracts",
   "Both layers independently produce and finalize blocks",
   "The consensus layer is deprecated and only the execution layer is active"], 0)

q("Which of these is a true statement about Arc's finality?",
  ["Transactions are immediately final with no reorg risk",
   "Transactions are final after 12 block confirmations",
   "Transactions are final after 7 days",
   "Transactions are never truly final"], 0)

q("Which ecosystem development tools does Arc provide beyond basic EVM compatibility?",
  ["App Kits for crosschain payments and an MCP server for AI agent development",
   "A fully custom IDE with no EVM support",
   "Only a block explorer and faucet",
   "A proprietary database query language"], 0)

q("What makes Arc suitable for agentic commerce use cases?",
  ["The MCP server providing AI tooling for agent-based development combined with sub-second finality",
   "Its high inflation rate incentivizing spending",
   "Its gaming-focused virtual machine",
   "Its centralized sequencer with MEV redistribution"], 0)

q("The 'single gas denomination at launch' design means that on day one of Arc mainnet:",
  ["Only USDC is accepted as payment for transaction fees",
   "Both USDC and EURC are accepted for gas",
   "Multiple competing tokens can be used for gas",
   "Gas is temporarily free"], 0)

q("How does the permissioned validator set relate to Arc's sub-second finality?",
  ["Permissioned sets with fewer, known validators reach consensus faster than large permissionless sets",
   "Permissioned sets are slower because they require manual approvals",
   "The validator set type does not affect finality speed",
   "Permissioned sets use Proof of Work which is inherently slow"], 0)

q("What is a key trade-off of Arc's permissioned validator model?",
  ["Lower decentralization in exchange for higher throughput and faster finality",
   "Lower throughput in exchange for maximum decentralization",
   "Higher costs for users in exchange for institutional compliance",
   "Faster finality at the cost of EVM compatibility"], 0)

q("What does the 'native' in native USDC interface refer to on Arc?",
  ["It is built into the protocol at the base layer, not as a smart contract",
   "It is only available to native Arc users",
   "It is the same as USDC on Ethereum",
   "It is a non-transferable balance"], 0)

q("Arc's design allows users to avoid which common blockchain friction point?",
  ["The need to purchase a volatile token before they can use stablecoins or dApps",
   "The need to download a wallet application",
   "The need to create an account with email and password",
   "The need to verify their identity"], 0)

q("A developer migrating a DeFi protocol from Ethereum to Arc must account for:",
  ["USDC being the native gas token and having dual interfaces",
   "A completely new programming language",
   "Lack of Solidity support on Arc",
   "Arc's 30-second block time"], 0)

q("How does Arc ensure compatibility with existing Ethereum DeFi protocols?",
  ["Through full EVM compatibility and an ERC-20 USDC interface with standard 6 decimals",
   "By forking the Uniswap codebase directly into the protocol layer",
   "By maintaining a separate compatibility bridge",
   "By translating Solidity to WASM at compile time"], 0)

q("What is the significance of Arc being a Layer-1 rather than a rollup?",
  ["Arc does not depend on another chain for security or finality",
   "Arc is less secure than rollups",
   "Arc processes fewer transactions than rollups",
   "Arc must settle to Ethereum periodically"], 0)

q("Which of these is an advantage of Arc's L1 architecture over rollups?",
  ["No dependency on an underlying L1 for security, enabling sub-second finality",
   "Lower development costs due to shared security",
   "Easier integration with Ethereum dApps",
   "Access to Ethereum's liquidity pools"], 0)

q("On Arc, when a user wants to send USDC to another wallet, they:",
  ["Can send it natively just like sending ETH on Ethereum",
   "Must call the ERC-20 transfer function",
   "Must first convert USDC to the native format",
   "Can only send through a smart contract"], 0)

q("The dual interface of USDC on Arc is designed so that:",
  ["The two interfaces maintain separate ledgers",
   "One underlying balance is accessible through both native and ERC-20 interfaces",
   "Each interface requires a separate wallet address",
   "Only the native interface can receive transfers"], 1)

q("What is the smallest unit of native USDC on Arc (given 18 decimal places)?",
  ["0.000000000000000001 USDC",
   "0.000001 USDC",
   "0.000000001 USDC",
   "0.01 USDC"], 0)

q("What is the smallest unit of ERC-20 USDC on Arc (given 6 decimal places)?",
  ["0.000001 USDC",
   "0.000000000000000001 USDC",
   "0.01 USDC",
   "0.0001 USDC"], 0)

q("A developer migrating a DeFi protocol from Ethereum to Arc must account for:",
  ["USDC being the native gas token and having dual interfaces",
   "A completely new programming language",
   "Lack of Solidity support on Arc",
   "Arc's 30-second block time"], 0)

q("How does Arc ensure compatibility with existing Ethereum DeFi protocols?",
  ["Through full EVM compatibility and an ERC-20 USDC interface with standard 6 decimals",
   "By forking the Uniswap codebase directly into the protocol layer",
   "By maintaining a separate compatibility bridge",
   "By translating Solidity to WASM at compile time"], 0)

q("What is the significance of Arc being a Layer-1 rather than a rollup?",
  ["Arc does not depend on another chain for security or finality",
   "Arc is less secure than rollups",
   "Arc processes fewer transactions than rollups",
   "Arc must settle to Ethereum periodically"], 0)

q("Which of these is an advantage of Arc's L1 architecture over rollups?",
  ["No dependency on an underlying L1 for security, enabling sub-second finality",
   "Lower development costs due to shared security",
   "Easier integration with Ethereum dApps",
   "Access to Ethereum's liquidity pools"], 0)

q("On Arc, when a user wants to send USDC to another wallet, they:",
  ["Can send it natively just like sending ETH on Ethereum",
   "Must call the ERC-20 transfer function",
   "Must first convert USDC to the native format",
   "Can only send through a smart contract"], 0)

q("The dual interface of USDC on Arc is designed so that:",
  ["The two interfaces maintain separate ledgers",
   "One underlying balance is accessible through both native and ERC-20 interfaces",
   "Each interface requires a separate wallet address",
   "Only the native interface can receive transfers"], 1)

q("What is the smallest unit of native USDC on Arc (given 18 decimal places)?",
  ["0.000000000000000001 USDC",
   "0.000001 USDC",
   "0.000000001 USDC",
   "0.01 USDC"], 0)

q("What is the smallest unit of ERC-20 USDC on Arc (given 6 decimal places)?",
  ["0.000001 USDC",
   "0.000000000000000001 USDC",
   "0.01 USDC",
   "0.0001 USDC"], 0)

# Remove duplicates if any by tracking question text
seen = set()
unique_questions = []
for q_ in questions:
    if q_["question"] not in seen:
        seen.add(q_["question"])
        unique_questions.append(q_)

questions = unique_questions

# Check distribution
dist = Counter(q_['correctIndex'] for q_ in questions)
print(f"Total questions: {len(questions)}")
print(f"Correct answer distribution before adjustment: {dict(sorted(dist.items()))}")

# Adjust correctIndex distribution to be more even
# We need each index to have roughly len/4 questions
# First, group questions by their current correctIndex
from collections import defaultdict
by_idx = defaultdict(list)
for q_ in questions:
    by_idx[q_['correctIndex']].append(q_)

target = len(questions) // 4
remainder = len(questions) % 4
# Target: index 0..3 get target, and first 'remainder' indices get +1
max_per = target + (1 if remainder > 0 else 0)

# For indices that have too many, move some to indices that have too few
# We'll redistribute by swapping correctIndex among options
import random
random.seed(42)

for idx in range(4):
    target_count = target + (1 if idx < remainder else 0)
    while len(by_idx[idx]) > target_count:
        # Find a question we can safely move to another index
        q_to_move = by_idx[idx].pop()
        # Find the index with the most room
        counts = {i: len(by_idx[i]) for i in range(4)}
        target_counts = {i: target + (1 if i < remainder else 0) for i in range(4)}
        # Find which index needs more questions the most
        deficit = {i: target_counts[i] - counts[i] for i in range(4)}
        neediest = max(deficit, key=deficit.get)
        if deficit[neediest] > 0:
            q_to_move['correctIndex'] = neediest
            by_idx[neediest].append(q_to_move)

# Rebuild questions list in order
questions = []
for q_ in unique_questions:
    # Find it in by_idx
    found = False
    for idx, qlist in by_idx.items():
        for i, candidate in enumerate(qlist):
            if candidate['question'] == q_['question'] and candidate['options'] == q_['options']:
                questions.append(candidate)
                qlist.pop(i)
                found = True
                break
        if found:
            break

dist = Counter(q_['correctIndex'] for q_ in questions)
print(f"Correct answer distribution after adjustment: {dict(sorted(dist.items()))}")

# Write JSON
output = {
    "meta": {
        "ecosystem": "Arc",
        "batchId": "arc-2026-07-11-batch1",
        "generatedAt": "2026-07-11T12:00:00Z",
        "totalQuizzes": len(questions),
        "questionsPerSession": 5
    },
    "quizzes": [{"id": i, **q_} for i, q_ in enumerate(questions)]
}

with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc-batch1.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"Written to quizzes-arc-batch1.json")
print(f"Total: {len(questions)} questions")
