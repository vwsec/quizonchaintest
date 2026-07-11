#!/usr/bin/env python3
"""Generate ~250 Base quiz questions with EVEN correctIndex distribution (~62 each)."""
import json
import random
from datetime import datetime, timezone
from collections import Counter

random.seed(42)

questions = []
# Track which index to use next for balance
idx_counter = Counter()

def next_idx(target=4):
    """Cycle through indices 0-3 for even distribution."""
    counts = [idx_counter[i] for i in range(4)]
    # Find min count
    min_val = min(counts)
    candidates = [i for i, c in enumerate(counts) if c == min_val]
    chosen = random.choice(candidates) if len(candidates) > 1 else candidates[0]
    idx_counter[chosen] += 1
    return chosen

def q(question, options, correctIndex=None):
    if not question.strip().endswith("?"):
        question = question.rstrip(":.") + "?"
    if correctIndex is None:
        correctIndex = next_idx()
    else:
        idx_counter[correctIndex] += 1
    questions.append({
        "question": question,
        "options": options,
        "correctIndex": correctIndex
    })

# ======================================================================
# TOPIC 1: BASE OVERVIEW (~65 questions)
# ======================================================================

q("What is Base?",
  ["A standalone Layer-1 blockchain",
   "A sidechain secured by Bitcoin",
   "The number one Ethereum Layer 2 (L2), incubated by Coinbase",
   "A zk-rollup for privacy transactions"], 2)

q("Which company incubated Base?",
  ["Binance",
   "Coinbase",
   "Kraken",
   "a16z"])

q("What technology stack is Base built on?",
  ["The Polygon CDK",
   "The OP Stack",
   "The zkSync Era Stack",
   "The Arbitrum Nitro Stack"])

q("Base is classified as which type of blockchain?",
  ["A sovereign L1",
   "An Ethereum Layer 2 (L2) rollup",
   "A sidechain with its own consensus",
   "A validium chain"])

q("What is the mainnet chain ID of Base?",
  ["1",
   "10",
   "8453",
   "42161"])

q("Which of the following best describes Base?",
  ["An independent L1 built from scratch",
   "A Cosmos SDK app-chain",
   "The number one Ethereum L2, built on the OP Stack and incubated by Coinbase",
   "A Solana Virtual Machine L2"])

q("Base is NOT which of the following?",
  ["An Ethereum Layer 2",
   "Built on the OP Stack",
   "Incubated by Coinbase",
   "A standalone Layer-1 blockchain"])

q("How does Base relate to Ethereum?",
  ["Base replaces Ethereum entirely",
   "Base is a fork of Ethereum with its own consensus",
   "Base is an L2 that uses Ethereum for settlement and security",
   "Base is a separate chain with no connection to Ethereum"])

q("Which statement about Base is FALSE?",
  ["Base is an Ethereum L2 built on the OP Stack",
   "Base was incubated by Kraken rather than Coinbase",
   "Base uses the OP Stack for its rollup architecture",
   "Base has a Security Council for protocol upgrades"], 1)

q("Base was incubated by which major cryptocurrency exchange?",
  ["Binance",
   "Coinbase",
   "Kraken",
   "Gemini"])

q("What ranking does Base hold among Ethereum L2s?",
  ["Number 3",
   "Number 5",
   "Number 1",
   "Number 2"])

q("Base is built on which modular framework?",
  ["Arbitrum Nitro Stack",
   "zkSync Era Stack",
   "OP Stack",
   "Polygon Edge"])

q("Base is an L2 built on which technology?",
  ["The OP Stack",
   "Arbitrum Orbit",
   "Polygon CDK",
   "zkSync Hyperchain"], 0)

q("Base is an optimistic rollup. What does that mean?",
  ["Transactions are presumed valid unless challenged via a fraud proof",
   "Every transaction is verified with a zero-knowledge proof",
   "Transactions are processed off-chain and never posted to L1",
   "Only whitelisted users can submit transactions"], 0)

# EVM Equivalence
q("What does it mean that Base is EVM-equivalent?",
  ["It supports only a subset of EVM opcodes",
   "It uses the same bytecode, RPC, and tooling as Ethereum",
   "It requires developers to rewrite Solidity contracts in Viper",
   "It only supports precompiled contracts from Ethereum"])

q("Which of the following is NOT true about Base's EVM equivalence?",
  ["Base uses the same bytecode as Ethereum",
   "Base uses a different RPC specification than Ethereum",
   "Base supports the same developer tooling as Ethereum",
   "Smart contracts can be deployed on Base without modification"])

q("How does Base's EVM compatibility compare to other L2s?",
  ["Base is EVM-equivalent, not just EVM-compatible",
   "Base only supports a subset of EVM opcodes",
   "Base uses a completely different virtual machine",
   "Base requires special compiler toolchains"], 0)

q("Can Ethereum smart contracts be deployed on Base without modification?",
  ["No, they must be rewritten in a different language",
   "Yes, because Base is EVM-equivalent",
   "Only if they use specific OpenZeppelin libraries",
   "No, Base uses a different address scheme"])

q("Which Ethereum developer tools work on Base without changes?",
  ["Only Hardhat",
   "Only Foundry",
   "Standard Ethereum tools like Hardhat, Foundry, and Remix",
   "None — Base requires proprietary tools"])

q("Base's EVM equivalence means it supports which of the following?",
  ["Only the same RPC endpoints as Ethereum",
   "Only the same opcodes as Ethereum",
   "Same bytecode, RPC endpoints, and developer tooling as Ethereum",
   "Only the same address format as Ethereum"])

q("If a Solidity contract compiles on Ethereum, will it deploy on Base without changes?",
  ["No, Base requires Vyper contracts",
   "Yes, because Base is EVM-equivalent",
   "Only if the contract is audited on Ethereum first",
   "No, they use different address formats"])

q("What level of EVM support does Base provide?",
  ["EVM-compatible (most opcodes work with tweaks)",
   "EVM-equivalent (identical behavior at the specification level)",
   "EVM-subset (limited opcode support, many missing)",
   "EVM-incompatible (uses WebAssembly)"], 1)

q("Which programming languages can be used for smart contracts on Base?",
  ["Solidity and Vyper, the same languages as Ethereum",
   "Only Solidity",
   "Only Rust",
   "Only a new language called BaseScript"], 0)

q("If a dApp uses web3.js or ethers.js on Ethereum, can the same code work on Base?",
  ["Yes, because Base is EVM-equivalent and supports the same RPC endpoints",
   "No, Base requires its own proprietary SDK",
   "Only if the code is rewritten from JavaScript to Python",
   "Only if the dApp uses ethers.js version 6 or newer"], 0)

q("What is the canonical token standard on Base?",
  ["ERC-20, the same standard used on Ethereum",
   "BEP-20, Base's proprietary token standard",
   "BRC-20, the Bitcoin Ordinals standard",
   "SPL, the Solana token standard"], 0)

# Chain ID
q("What is the Chain ID for Base mainnet?",
  ["10 (which is Optimism's Chain ID)",
   "42161 (which is Arbitrum's Chain ID)",
   "8453",
   "137 (which is Polygon's Chain ID)"], 2)

q("Which chain uses Chain ID 8453?",
  ["Optimism Mainnet",
   "Arbitrum One",
   "Base Mainnet",
   "Polygon zkEVM"], 2)

q("What Chain ID would you enter to add Base mainnet to your wallet?",
  ["10",
   "8453",
   "42161",
   "1"])

q("In hexadecimal, Base's Chain ID 8453 is represented as what?",
  ["0x1",
   "0xa",
   "0x2105",
   "0x7c"])

q("Which of the following would NOT be correct for Base mainnet's Chain ID?",
  ["8453 in decimal",
   "0x2105 in hexadecimal",
   "10 in decimal (that belongs to Optimism)",
   "Both 8453 and 0x2105 are correct representations"], 2)

# Settlement & Security
q("How does Base achieve security?",
  ["Through its own validator set with native token staking",
   "By using Ethereum for settlement and security",
   "Through a centralized database operated by Coinbase",
   "Through a proof-of-authority model with trusted nodes"])

q("What role does Ethereum play for Base?",
  ["Ethereum is only the data availability layer",
   "Ethereum is the execution layer for Base transactions",
   "Ethereum provides settlement and security for Base",
   "Ethereum has no relationship with Base at all"])

q("Base transactions are ultimately settled on which chain?",
  ["Base's own L1 consensus chain",
   "Ethereum mainnet",
   "Optimism's settlement chain",
   "Solana"])

q("Which chain provides final settlement for Base?",
  ["Coinbase's internal ledger",
   "Ethereum mainnet, where transaction batches are posted",
   "The OP Stack's separate settlement layer",
   "A dedicated settlement chain run by Coinbase"])

q("How does Base post transaction data to Ethereum?",
  ["It posts compressed calldata in batches",
   "It posts each transaction individually to Ethereum",
   "It does not post any data to Ethereum",
   "It uses a side channel for data availability"], 0)

q("What type of data does Base submit to Ethereum for settlement?",
  ["Only merkle roots of transaction batches",
   "Transaction calldata and state roots in compressed batches",
   "Only block headers for each Flashblock",
   "Only fee data and gas usage statistics"])

q("Base relies on Ethereum for which of the following?",
  ["Only data availability",
   "Only state storage for account balances",
   "Settlement, security, and data availability",
   "Only transaction execution"])

q("Base posts compressed transaction batches to Ethereum. Why are batches compressed?",
  ["To reduce the amount of data posted to L1, which lowers fees for users",
   "To encrypt transactions for privacy and security",
   "Because Ethereum only accepts compressed calldata format",
   "To comply with data protection regulations"])

# Separation of concerns
q("How does Base separate blockchain concerns like other OP Stack chains?",
  ["It uses sharding for execution and consensus",
   "It separates consensus from execution",
   "It runs all operations on a single monolithic node",
   "It separates storage from networking"])

q("The separation of consensus from execution in the OP Stack means what?",
  ["Different software modules handle transaction ordering versus execution",
   "Consensus is completely skipped on Base — only execution matters",
   "Transactions execute before they are ordered by the sequencer",
   "Base has no execution layer — Ethereum handles all execution"], 0)

q("What is the relationship between Base's execution layer and consensus layer?",
  ["They are combined in a single monolithic node for simplicity",
   "They are separated, like other OP Stack chains",
   "There is no consensus layer — Base is permissioned",
   "Both layers run directly on Ethereum mainnet"])

q("What does 'modular' mean in the context of the OP Stack?",
  ["Different components like execution, settlement, and consensus can be upgraded independently",
   "The chain can scale by adding more validators in a modular fashion",
   "Developers can build modular smart contracts that compose together",
   "Users can choose modular transaction types based on their needs"], 0)

# Ecosystem
q("Which of the following is part of the Base ecosystem?",
  ["Apps, accounts, agents, ledgers, and bridge infrastructure",
   "Only DEXes and lending protocols",
   "Only NFT marketplaces and gaming applications",
   "Only bridges to other L2 rollups"], 0)

q("The Base ecosystem includes all of the following EXCEPT:",
  ["Applications and smart contracts",
   "Automated agents and trading bots",
   "Bridge infrastructure connecting to Ethereum",
   "A native staking token used for L1 consensus on Base"], 3)

q("What does the Base Bridge facilitate?",
  ["Only NFT transfers between different L2 platforms",
   "Asset transfers between Ethereum mainnet and Base",
   "Only ERC-20 token minting on Base",
   "Cross-chain messaging between all Ethereum L2s"])

q("Which infrastructure connects Base to Ethereum for asset transfers?",
  ["The Base Bridge",
   "The Coinbase Wallet",
   "The OP Stack bridge",
   "The Ethereum L1 Bridge"])

# Security Council & Governance
q("Does Base have a Security Council?",
  ["No, Base relies solely on automated monitoring systems",
   "Yes, Base has a Security Council with multisig capabilities",
   "Only on testnet — the mainnet Security Council is planned",
   "The Security Council was proposed but never implemented"])

q("What is the role of Base's Security Council?",
  ["To manage community grants and funding distribution",
   "To act as a multisig for protocol upgrades and emergency actions",
   "To validate transactions on the Base L2 network",
   "To set and adjust gas prices on Base"])

q("Who participates in Base's Security Council?",
  ["Only Coinbase employees",
   "A diverse set of ecosystem participants as multisig signers",
   "Only the Base core development team members",
   "Only Ethereum Foundation council members"])

# Protocol Upgrades
q("What is the latest protocol upgrade for Base?",
  ["Azul",
   "Optimism",
   "Beryl",
   "Cobalt"], 2)

q("Which of these is a Base protocol upgrade?",
  ["Berlin (Ethereum fork)",
   "Beryl",
   "London (Ethereum fork)",
   "Shanghai (Ethereum fork)"])

q("Base protocol upgrades include which of the following?",
  ["Only Beryl",
   "Beryl, Azul, and Optimism",
   "Only Istanbul and Berlin, which are Ethereum forks",
   "Azul and Cobalt only"])

q("Which Base upgrade is named after a gemstone?",
  ["Optimism",
   "Beryl",
   "Azul",
   "All of the above name upgrades after gemstones"])

q("Before Beryl, which of the following was a Base protocol upgrade?",
  ["Azul",
   "Sapphire",
   "Diamond",
   "Ruby"], 0)

q("Which Base protocol upgrade is named after the ecosystem behind the OP Stack?",
  ["Beryl",
   "Azul",
   "Optimism",
   "Cobalt"])

# Builder Support
q("What types of builder support does Base offer?",
  ["Only grants for new projects",
   "Builder Rewards, Grants, Base Batches, and Retroactive Funding",
   "Only venture capital investment from Coinbase",
   "Only hackathon prize money for winners"])

q("What is Base Batches?",
  ["A batch transaction processor for developers",
   "A program supporting builders creating applications on Base",
   "An L2 batch submission mechanism for the sequencer",
   "A collection of pre-deployed smart contract templates"])

q("Base offers Retroactive Funding to which group?",
  ["Only validator operators who run Base nodes",
   "Builders who have already contributed value to the ecosystem",
   "Only established venture capital firms",
   "Only academic researchers publishing papers about Base"])

q("Which programs provide financial support to Base builders?",
  ["Only Base Grants",
   "Builder Rewards exclusively",
   "Builder Rewards, Grants, Base Batches, and Retroactive Funding",
   "Only Retroactive Funding for past contributions"])

q("What is the Base Mentorship Program?",
  ["A program that matches new builders with experienced mentors in the ecosystem",
   "A Coinbase employee training program about blockchain technology",
   "A course teaching developers how to use the OP Stack",
   "A financial advising service for BASE token holders"], 0)

q("What are Builder Rewards on Base?",
  ["A loyalty program for regular Base users",
   "A program that rewards developers for building on Base",
   "A staking rewards program for BASE token holders",
   "A referral bonus program for inviting new users"])

# Dashboard
q("Where can the Base Dashboard be accessed?",
  ["dashboard.ethereum.org",
   "dashboard.base.org",
   "base.dashboard.com",
   "stats.coinbase.com"])

q("What information does the Base Dashboard provide?",
  ["Only current gas price estimates",
   "On-chain metrics, network activity, and ecosystem data",
   "Only total value locked (TVL) figures",
   "Only daily transaction counts"])

q("The Base Dashboard is available at which URL?",
  ["base.org/dashboard",
   "dashboard.base.org",
   "base-scan.org/dashboard",
   "coinbase.com/base/dashboard"])

q("What kind of data can be found on dashboard.base.org?",
  ["Personal wallet private keys and seed phrases",
   "On-chain metrics and ecosystem data for the Base network",
   "Coinbase stock prices and trading volume",
   "Ethereum L1 staking rewards and validator data"])

# ======================================================================
# TOPIC 2: CHAIN ARCHITECTURE (~60 questions)
# ======================================================================

q("What does the OP Stack provide to Base?",
  ["A custom consensus mechanism unique to Base only",
   "The modular framework for building L2 rollups on Ethereum",
   "A proprietary database engine for storing state",
   "A custom smart contract programming language"])

q("Which technology powers Base's rollup architecture?",
  ["Arbitrum Nitro",
   "zkSync Era",
   "The OP Stack",
   "Polygon zkEVM"])

q("Base leverages the OP Stack for what primary purpose?",
  ["Only transaction ordering and sequencing",
   "The modular architecture of its L2 rollup on Ethereum",
   "Only data compression for L1 batches",
   "Only fraud proof mechanism implementation"])

q("How does Base benefit from being built on the OP Stack?",
  ["It has a proprietary consensus mechanism unavailable elsewhere",
   "It inherits Ethereum-grade security through the modular rollup framework",
   "It does not need to post transaction data to Ethereum",
   "It can process transactions without charging gas fees"])

q("The OP Stack enables Base to operate as what kind of network?",
  ["A standalone L1 with its own validator set",
   "A modular L2 rollup built on top of Ethereum",
   "A chain that completely skips the settlement process",
   "A network that operates without a sequencer"])

q("Base's use of the OP Stack means it benefits from what?",
  ["Proprietary algorithms unavailable to other L2 solutions",
   "Shared research, security improvements, and upgrades from the broader OP ecosystem",
   "Exclusive access to Coinbase's order book data",
   "Guaranteed lower fees than any other L2 network"])

q("Which ecosystem does the OP Stack originate from?",
  ["The Arbitrum ecosystem",
   "The Optimism (OP) ecosystem",
   "The zkSync ecosystem",
   "The Polygon ecosystem"])

# Block Structure
q("What is the block time for Base in vanilla mode (without Flashblocks)?",
  ["200 milliseconds",
   "2 seconds",
   "12 seconds",
   "1 second"])

q("How long is a standard Base block time without Flashblocks enabled?",
  ["200 milliseconds",
   "2 seconds",
   "10 seconds",
   "12 seconds"])

q("In vanilla mode, what software builds Base blocks?",
  ["base-builder",
   "base-reth-node",
   "geth (standard Ethereum client)",
   "op-node"])

q("Which node software builds Base blocks in vanilla mode?",
  ["base-builder (which adds Flashblock support)",
   "base-reth-node",
   "op-geth (Optimism's geth fork)",
   "reth (Rust Ethereum implementation)"], 1)

q("How does Base benefit from being on the OP Stack in terms of architecture?",
  ["It has a tightly coupled monolithic node design",
   "It separates execution, settlement, and consensus into modular components",
   "It runs everything on Ethereum L1 for simplicity",
   "It uses a completely custom architecture unrelated to the OP Stack"])

# Sequencer
q("Who operates the Base sequencer?",
  ["A decentralized set of community validators",
   "Coinbase, with plans to decentralize over time",
   "The Optimism Foundation on behalf of Base",
   "A DAO of BASE token holders"])

q("The Base sequencer is responsible for which tasks?",
  ["Only ordering transactions in the mempool",
   "Ordering transactions and building blocks using base-builder",
   "Only executing smart contracts on Base",
   "Only settling batches to Ethereum L1"])

q("Which component builds blocks on Base?",
  ["The proposer role in the OP Stack",
   "The sequencer using base-builder software",
   "The batcher that submits data to Ethereum",
   "The challenger in the fault proof system"])

q("The Base sequencer constructs blocks using which software?",
  ["op-node (the OP Stack node)",
   "base-reth-node (the execution engine)",
   "base-builder (the block building tool)",
   "op-geth (the Optimism geth fork)"])

q("Which statement about the Base sequencer is accurate?",
  ["It is currently operated by Coinbase with decentralization planned over time",
   "It is fully decentralized and operated by a permissionless validator set",
   "It is operated by the Optimism Foundation",
   "It is operated by a DAO of BASE token holders"], 0)

# Security Model
q("What security model does Base use?",
  ["Proof of Stake with its own independent validators",
   "Proof of Authority with trusted Coinbase nodes",
   "Ethereum-based security via the OP Stack optimistic rollup model",
   "Delegated Proof of Stake through token voting"])

q("Base inherits security from which chain?",
  ["Coinbase's internal security infrastructure",
   "Ethereum, through the rollup settlement and fault proof mechanism",
   "A network of Base validators staking BASE tokens",
   "The OP Foundation's multisig governance"])

q("Which of the following is true about Base's security model?",
  ["Base has its own validator set that stakes a native BASE token",
   "Base relies on Ethereum's security for final settlement and data availability",
   "Base uses a proof-of-authority consensus with trusted third-party validators",
   "Base has no security mechanism — it is a permissioned ledger operated by Coinbase"])

q("The fault proof system that protects Base relies on which chain for resolution?",
  ["Base native validators who monitor the chain",
   "Ethereum, through the OP Stack's dispute resolution mechanism",
   "Coinbase's internal infrastructure monitoring team",
   "Third-party security auditors reviewing every batch"])

q("How does Base use Ethereum for security?",
  ["By running Ethereum client software within every Base node",
   "By posting transaction batches and state roots to Ethereum, inheriting its security",
   "By requiring all Base transactions to be approved by Ethereum validators",
   "By using ETH as the native gas token for all transactions on Base"])

q("What kind of rollup is Base?",
  ["Optimistic rollup — transactions are valid unless challenged via fraud proofs",
   "ZK-rollup — every batch includes a zero-knowledge validity proof",
   "Plasma chain — users must exit to L1 within a challenge period",
   "Validium — data is stored off-chain with validity proofs"], 0)

q("What does the optimistic rollup security model assume?",
  ["Transactions are valid unless proven otherwise through a fraud proof challenge",
   "All transactions are immediately final with no possibility of reversal",
   "Every transaction must be individually verified by Ethereum validators",
   "Only Coinbase-approved transactions are valid on the network"], 0)

# EVM & Compatibility
q("What bytecode compatibility does Base offer?",
  ["Compatible with EVM bytecode only for simple ETH transfers",
   "Full EVM bytecode compatibility — same opcodes, same behavior as Ethereum",
   "Partial compatibility — some opcodes like DIFFICULTY behave differently",
   "No EVM compatibility — Base uses WebAssembly (WASM) bytecode"])

q("Base supports the same RPC endpoints as which chain?",
  ["Only Optimism Mainnet",
   "Only Arbitrum One",
   "Ethereum Mainnet",
   "Only Solana Mainnet"])

q("Which standard Ethereum JSON-RPC methods work on Base?",
  ["Only eth_blockNumber and eth_gasPrice",
   "All standard Ethereum JSON-RPC methods",
   "Only eth_sendTransaction and eth_call",
   "None — Base uses a completely different RPC specification"])

q("Which address format is valid on Base?",
  ["0x-prefixed addresses, exactly the same format as Ethereum",
   "bc1-prefixed addresses like Bitcoin",
   "base1-prefixed addresses specific to Base",
   "Only addresses starting with the 0xBASE prefix"], 0)

q("Does Base have a native governance token?",
  ["Yes — it is called BASE and is used for on-chain governance",
   "No — Base does not have a native governance token",
   "Yes — it is called OP, inherited from the Optimism ecosystem",
   "Yes — it is called COIN and is issued by Coinbase"])

q("What is the primary native currency used for gas on Base?",
  ["ETH (Ether bridged from Ethereum mainnet)",
   "BASE (a native network token created for Base)",
   "USDC (the most popular stablecoin on Base)",
   "OP (the Optimism governance token)"])

q("Which address format would you use to receive funds on Base?",
  ["0x-prefixed hexadecimal address (same as Ethereum EOA format)",
   "bc1-prefixed address (Bitcoin bech32 format)",
   "base1-prefixed address (Base's proprietary format)",
   "Any format is valid on the Base network"], 0)

q("A developer migrating from Ethereum to Base would need to change what?",
  ["Nothing — Base is EVM-equivalent, so contracts and tooling work as-is",
   "Their smart contract code from Solidity to Vyper",
   "Their deployment scripts to use a Base-specific SDK",
   "Their entire infrastructure to use Base-only providers"], 0)

# Architecture Comparison
q("What is the main difference between an optimistic rollup like Base and a ZK-rollup?",
  ["Optimistic rollups use fraud proofs with a challenge period; ZK-rollups use validity proofs",
   "Optimistic rollups are always faster and cheaper than ZK-rollups",
   "ZK-rollups are also built on the OP Stack; optimistic rollups are not",
   "There is no meaningful difference in their security models at all"], 0)

q("What is the primary scaling benefit that Base provides over Ethereum L1?",
  ["Higher transaction throughput and lower fees by batching transactions off-chain",
   "Unlimited block size with no gas limit restrictions",
   "Free transactions for all users on the Base platform",
   "Instant transaction finality on Ethereum L1"], 0)

q("What does Base posting state roots to Ethereum allow users to do?",
  ["Verify the state of Base without running a full Base node",
   "Pay lower transaction fees on Base",
   "Operate without needing a sequencer",
   "Mint new tokens directly from Ethereum"], 0)

q("What happens if Ethereum experiences a consensus failure while Base is operating?",
  ["Base would also be affected because it relies on Ethereum for settlement and security",
   "Base would continue operating completely independently without any impact",
   "Base would automatically switch to a different settlement chain",
   "All Base transactions processed during that time would be permanently lost"], 0)

q("What is the OP Stack's approach to rollup architecture?",
  ["A modular framework where execution, settlement, and consensus are separate",
   "A monolithic framework where all components run in a single binary",
   "A proprietary framework only available to Optimism and Base",
   "A framework that requires all chains to use the same governance token"])

q("How has Base benefited from shared OP Stack development?",
  ["It receives security upgrades and improvements developed by the Optimism collective",
   "It has exclusive access to features not available to other OP Stack chains",
   "It pays no fees because the OP Stack is free and open source",
   "It can settle transactions without posting data to Ethereum"], 0)

# ======================================================================
# TOPIC 3: FLASHBLOCKS (~65 questions)
# ======================================================================

q("What are Flashblocks on Base?",
  ["Blocks built every 12 seconds by Ethereum validators",
   "Preconfirmation blocks built every 200ms by the Base sequencer",
   "Blocks submitted to Ethereum every hour for settlement finality",
   "Testnet-only blocks for developer testing purposes"])

q("How often does the Base sequencer build Flashblocks?",
  ["Every 2 seconds",
   "Every 200 milliseconds",
   "Every 12 seconds",
   "Every 1 second"])

q("What is the effective block time with Flashblocks enabled on Base?",
  ["2 seconds",
   "12 seconds",
   "200 milliseconds",
   "1 second"])

q("Flashblocks reduce the effective block time from 2 seconds to what?",
  ["1 second",
   "500 milliseconds",
   "200 milliseconds",
   "100 milliseconds"])

q("Flashblocks are a form of what kind of block?",
  ["On-chain finality mechanism settled on Ethereum",
   "Preconfirmation blocks built by the Base sequencer",
   "L1 settlement batches periodically submitted to Ethereum",
   "Cross-chain message relay blocks for bridging"], 1)

q("What software does Base use to build Flashblocks?",
  ["base-reth-node",
   "op-node",
   "base-builder",
   "geth (Go Ethereum)"])

q("Flashblocks produce preconfirmation blocks at what interval?",
  ["Every 200 milliseconds (5 per second)",
   "Every 2 seconds (0.5 per second)",
   "Every 100 milliseconds (10 per second)",
   "Every 500 milliseconds (2 per second)"], 0)

q("Flashblock preconfirmations give users what type of feedback?",
  ["L1-level finality guaranteed within 200 milliseconds",
   "A fast signal that their transaction has been ordered ahead of full block finality",
   "A guaranteed inclusion in any Flashblock regardless of priority fee paid",
   "A full refund on their gas fee if the transaction ultimately fails"])

q("Preconfirmations via Flashblocks are useful for what kind of application?",
  ["Only institutional trading platforms with high volume",
   "Any application that benefits from fast transaction feedback, such as DEXes and gaming",
   "Only NFT minting applications that need instant confirmation",
   "Only cross-chain bridge protocols waiting for finality"])

q("How does the Flashblock system provide faster transaction feedback to users?",
  ["By building preconfirmation blocks every 200ms instead of waiting 2 seconds for a full block",
   "By skipping the mempool entirely and executing transactions instantly",
   "By reducing the number of validators needed to approve each block",
   "By batching all pending transactions into a single submission to Ethereum L1"], 0)

# 10 Per Full Block
q("How many Flashblocks make up one full Base block?",
  ["5",
   "10",
   "20",
   "2"])

q("There are how many Flashblocks per full block?",
  ["Two, each with 200M gas budgets",
   "Ten, each with incrementally increasing gas budgets",
   "One single Flashblock containing the entire block gas limit",
   "Five Flashblocks of 80M gas each"])

q("Each full Base block is composed of how many Flashblocks?",
  ["2 Flashblocks of 200M gas each",
   "10 Flashblocks with incrementally increasing gas budgets",
   "1 single Flashblock with the full block gas limit",
   "5 Flashblocks of 80M gas each"])

q("How many Flashblocks are created between two full Base blocks?",
  ["10 Flashblocks in the 2-second window",
   "5 Flashblocks in the 2-second window",
   "20 Flashblocks in the 2-second window",
   "2 Flashblocks in the 2-second window"], 0)

q("In the Flashblock system, how many priority fee auctions occur before a full block is completed?",
  ["1 auction per full block",
   "10 auctions, one per Flashblock in the 2-second cycle",
   "5 auctions, one per every 2 Flashblocks built",
   "The number varies based on network congestion levels"], 1)

# Gas Budget
q("What is the gas budget of Flashblock 1?",
  ["Approximately 40M gas, which is 1/10 of the block gas limit",
   "Approximately 80M gas, which is 2/10 of the block gas limit",
   "Approximately 200M gas, which is 1/2 of the block gas limit",
   "Approximately 400M gas, which is the full block gas limit"], 0)

q("Flashblock 1 has a gas budget of approximately how much?",
  ["80M gas",
   "40M gas",
   "200M gas",
   "400M gas"])

q("What is the gas budget of Flashblock 2?",
  ["Approximately 40M gas (1/10 of the block gas limit)",
   "Approximately 80M gas (2/10 of the block gas limit)",
   "Approximately 120M gas (3/10 of the block gas limit)",
   "Approximately 100M gas (1/4 of the block gas limit)"], 1)

q("Flashblock 2 has a gas budget of approximately how much?",
  ["40M gas",
   "80M gas",
   "120M gas",
   "400M gas"])

q("What is the gas budget of Flashblock 10?",
  ["Approximately 40M gas",
   "Approximately 200M gas",
   "Approximately 400M gas, which is the full block gas limit",
   "Approximately 80M gas"])

q("The gas budget of Flashblock 10 is which of the following?",
  ["1/10 of the full block gas limit",
   "1/2 of the full block gas limit",
   "The full block gas limit of approximately 400M gas",
   "2/10 of the full block gas limit"])

q("How does the gas budget change across Flashblocks 1 through 10?",
  ["It stays constant at 400M gas for every Flashblock",
   "It decreases from 400M down to 40M as blocks fill up",
   "It increases incrementally from approximately 40M to approximately 400M gas",
   "It randomly varies between 40M and 400M based on mempool activity"])

q("Flashblock 1 has approximately 40M gas budget, which represents what fraction?",
  ["1/10 of the block gas limit",
   "1/2 of the block gas limit",
   "The full block gas limit",
   "1/5 of the block gas limit"], 0)

q("Flashblock 5 would have a gas budget approximately between which two values?",
  ["40M and 80M",
   "160M and 200M (between 4/10 and 5/10 of the limit)",
   "80M and 120M",
   "200M and 400M"])

q("The incrementally increasing gas budget across Flashblocks means what?",
  ["Each Flashblock has exactly the same gas budget available for transactions",
   "Flashblock 1 starts at approximately 40M and Flashblock 10 reaches approximately 400M",
   "Gas budgets decrease as the Flashblock number increases over time",
   "Gas budgets are randomly assigned by the sequencer each round"])

q("What fraction of the total block gas limit does Flashblock 1 represent?",
  ["1/2",
   "1/4",
   "1/10",
   "1/5"])

q("What fraction of the total block gas limit does Flashblock 2 represent?",
  ["1/10",
   "2/10 (which is 1/5)",
   "3/10",
   "5/10 (which is 1/2)"], 1)

q("By Flashblock 5, what fraction of the total block gas limit is available cumulatively?",
  ["5/10 (which is 1/2)",
   "1/10",
   "3/10",
   "10/10 (the full limit)"], 0)

# Per-transaction gas maximum
q("What is the per-transaction gas maximum on Base?",
  ["Approximately 40M gas (the entire Flashblock 1 budget)",
   "Approximately 400M gas (the full block gas limit)",
   "Approximately 16.7M gas, which fits in Flashblock 1's approximately 40M budget",
   "Approximately 80M gas (the Flashblock 2 budget)"], 2)

q("Why is the per-transaction gas maximum on Base approximately 16.7M?",
  ["Because Ethereum L1's block gas limit is also 16.7M gas",
   "So that at least 2 transactions can fit in Flashblock 1's approximately 40M budget",
   "Because the OP Stack hard-codes a maximum of 16.7M gas per transaction",
   "Because priority fee auctions automatically cap all transactions at this level"]) 

q("The per-transaction gas maximum of approximately 16.7M on Base ensures what?",
  ["A single transaction cannot entirely fill Flashblock 1's approximately 40M gas budget",
   "Multiple transactions can fit in even the smallest Flashblock during operation",
   "Transactions are always routed to Flashblock 10 for efficient packing",
   "Both A and B — it prevents single-tx saturation and allows multiple txs per Flashblock"], 3)

q("What would happen if a transaction exceeds the approximately 16.7M per-transaction gas maximum?",
  ["The transaction is rejected by the Base sequencer before inclusion",
   "The transaction is automatically split across multiple Flashblocks",
   "It is redirected to Flashblock 10 which has the largest budget",
   "It gets posted directly to Ethereum L1 instead of being processed on Base"], 0)

# Priority Fee Auctions
q("How often do priority fee auctions occur in Base's Flashblock system?",
  ["Every 2 seconds, synchronized with full blocks",
   "Every 200 milliseconds, synchronized with each Flashblock",
   "Every 12 seconds, synchronized with Ethereum L1",
   "Every 5 seconds, regardless of block production"])

q("Base uses priority fee auctions every 200ms for what purpose?",
  ["To determine the final settlement batch for submission to Ethereum",
   "To determine which transactions are included in each Flashblock",
   "To set the reference gas price for the entire Ethereum L1 network",
   "To elect the sequencer operator for the next round of block production"])

q("In each priority fee auction every 200ms, which transactions win inclusion?",
  ["The largest transactions ranked by calldata byte size",
   "The transactions offering the highest priority fees",
   "The oldest pending transactions in the mempool",
   "Transactions from accounts with the highest ETH balances"])

q("A priority fee auction repeats every 200ms on Base. How many rounds per full block?",
  ["Only one auction per full block cycle",
   "10 auction rounds, one per Flashblock in the 2-second full block cycle",
   "The auction frequency depends entirely on network congestion levels",
   "Auctions only occur when the mempool holds 100 or more transactions"])

q("How does the 200ms priority fee auction affect MEV dynamics on Base?",
  ["It completely eliminates all MEV opportunities on the network",
   "It creates frequent auction opportunities every 200ms for searchers to compete for order flow",
   "It makes MEV impossible because transaction ordering is locked on arrival",
   "It only affects cross-chain MEV, not intra-chain MEV between users"])

q("During a priority fee auction, what role does the priority fee play?",
  ["It determines which transactions are selected for inclusion in the Flashblock",
   "It determines the gas budget allocated to each Flashblock",
   "It determines the settlement priority on Ethereum L1",
   "It determines the exchange rate between ETH and BASE"])

# Dynamic Mempool
q("What does the dynamic mempool in Base's Flashblock system do?",
  ["It rejects all new transactions until the next full block is completed",
   "It continuously accepts new transactions while the builder constructs Flashblocks",
   "It only accepts transactions at the very start of each full block cycle",
   "It uses a fixed queue that is cleared and reset every 2 seconds"])

q("The dynamic mempool allows the Base builder to do what?",
  ["Lock the mempool for 2 seconds to finalize the complete block construction",
   "Continuously accept new transactions while building Flashblocks over the 2-second cycle",
   "Only process transactions from whitelisted addresses for security",
   "Reject low-fee transactions from entering the mempool entirely"])

q("How does the dynamic mempool affect transaction inclusion timing?",
  ["Only transactions submitted before the first Flashblock can be included in the cycle",
   "New transactions can be accepted even while the builder is constructing later Flashblocks",
   "Transactions are only accepted in batches every 2 seconds on the second",
   "The mempool becomes read-only during the entire block construction process"])

q("Without a dynamic mempool, what would happen to a transaction submitted midway through a block cycle?",
  ["It would be included in the current cycle regardless of submission time",
   "It would have to wait for the next full block cycle to begin for inclusion",
   "It would be permanently rejected by the Base sequencer",
   "It would replace a lower-fee transaction already in the mempool"])

# Tradeoffs
q("What is the main tradeoff of Flashblocks on Base?",
  ["Slower block finality in exchange for higher throughput capacity",
   "Faster inclusion at the cost of occasionally breaking expected PGA ordering",
   "Lower transaction capacity in exchange for lower user fees",
   "Increased latency in exchange for better decentralization"])

q("Flashblocks provide faster inclusion at the cost of what tradeoff?",
  ["Higher gas fees on Ethereum L1 for settlement",
   "Occasionally breaking expected priority fee auction (PGA) ordering",
   "Reducing the total block capacity available per full block cycle",
   "Longer overall settlement times on Ethereum L1"])

q("What is a potential downside of the Flashblock system for users?",
  ["Blocks are produced more slowly than the advertised 200ms target",
   "A later-arriving higher-fee transaction cannot be inserted into an already-broadcast earlier Flashblock",
   "Flashblocks are not compatible with ERC-20 token transfers on Base",
   "Each Flashblock costs real ETH to produce and broadcast on L1"])

q("Why might a high-fee transaction end up in a later Flashblock rather than an earlier one?",
  ["The sequencer deliberately delays high-fee transactions for fairness",
   "The transaction arrived after earlier Flashblocks were already built and broadcast",
   "High-fee transactions are always routed by default to Flashblock 10",
   "The builder reorders transactions by calldata size instead of by fee"])

# Ordering Locked
q("Once a Flashblock is built and broadcast, what happens to its transaction ordering?",
  ["It can be reordered when the next Flashblock is subsequently built",
   "It remains flexible and adjustable until the full block is assembled",
   "The ordering is permanently locked within that specific Flashblock",
   "Transactions can be removed by the sequencer at any time before full block submission"])

q("After a Flashblock is broadcast, its transaction order undergoes what change?",
  ["It can be changed by a higher priority fee arriving later from another user",
   "It is locked — later-arriving transactions cannot be inserted into that Flashblock",
   "It is re-evaluated when the full block is assembled and submitted to L1",
   "It is re-determined by the next Flashblock in the sequence"])

q("Transaction ordering is locked within a Flashblock once it reaches which state?",
  ["Submitted to Ethereum L1 for settlement finality",
   "Built and broadcast by the sequencer after the 200ms auction",
   "Included in the dynamic mempool waiting for selection",
   "Signed by the user's wallet and broadcast to the network"])

q("What happens to a higher-fee transaction that arrives after the current Flashblock is already built?",
  ["It replaces the lowest-fee transaction in the current Flashblock",
   "It is included in a later Flashblock instead of the current one",
   "It causes the current Flashblock to be rebuilt from scratch with the new fee",
   "It is permanently rejected by the Base sequencer"])

q("Can a later-arriving higher-fee transaction be inserted into an earlier Flashblock?",
  ["Yes, if the priority fee is high enough to justify the reordering",
   "No, once a Flashblock is built and broadcast, its contents are locked",
   "Yes, but only during the first 100ms of the 200ms auction window",
   "No, unless the transaction originates from a whitelisted address"])

# Vanilla vs Flashblocks
q("In vanilla mode (without Flashblocks), how long are Base blocks?",
  ["200 milliseconds",
   "2 seconds",
   "12 seconds",
   "1 second"])

q("Vanilla mode on Base produces blocks at what interval?",
  ["Every 200ms with Flashblock-like preconfirmations",
   "Every 2 seconds by base-reth-node",
   "Every 12 seconds like Ethereum L1",
   "Every 10 seconds as configured by the sequencer"])

q("What is the key difference between vanilla mode and Flashblocks on Base?",
  ["Vanilla mode has 2s blocks ordered by priority fee; Flashblocks has 200ms preconfirmation blocks",
   "Vanilla mode has higher throughput capacity than Flashblocks mode",
   "Flashblocks has 2s blocks while vanilla mode has 200ms blocks",
   "There is no meaningful difference between the two modes of operation"], 0)

q("Flashblocks use base-builder, while vanilla mode uses which software?",
  ["op-batcher for submitting data to L1",
   "base-reth-node for vanilla block production",
   "geth the standard Ethereum execution client",
   "op-proposer for proposing state roots"])

q("Which mode provides users with faster transaction confirmation on Base?",
  ["Vanilla mode with 2-second blocks",
   "Flashblocks mode with 200ms preconfirmations",
   "Both modes offer the same confirmation speed to users",
   "Neither mode provides fast confirmation at any point"])

q("How many Flashblocks fit within one 2-second vanilla block window?",
  ["5 Flashblocks",
   "20 Flashblocks",
   "10 Flashblocks",
   "2 Flashblocks"])

q("A transaction in Flashblock 1 is confirmed approximately how much faster than in a vanilla 2s block?",
  ["10 seconds faster",
   "Up to 1.8 seconds faster (2 seconds minus 200 milliseconds)",
   "2 seconds faster (exactly one full block time)",
   "No difference — both confirm at the same time"])

q("Which system runs priority fee auctions more frequently?",
  ["Vanilla mode with its 2-second block window",
   "Flashblocks mode with 200ms preconfirmation blocks",
   "Both systems have the same auction frequency",
   "Neither system runs any priority fee auctions at all"])

# Flashblock comparisons
q("How does the 200ms Flashblock interval compare to Ethereum L1's 12-second block time?",
  ["Flashblocks are 60 times faster than Ethereum L1 blocks",
   "Flashblocks are the same speed as Ethereum L1 blocks",
   "Flashblocks are actually slower than Ethereum L1 blocks",
   "Flashblocks are 6 times faster than Ethereum L1 blocks"], 0)

q("For a dApp needing sub-second transaction feedback, what does Base with Flashblocks provide?",
  ["200ms preconfirmations, fast enough for most interactive applications",
   "No preconfirmation — users must wait the full 2 seconds minimum",
   "Preconfirmations only available to whitelisted dApps",
   "12-second confirmation like Ethereum L1 with no acceleration"])

q("The transition between vanilla mode and Flashblocks mode on Base is what kind of change?",
  ["A configuration choice — Flashblocks is an optional feature of base-builder",
   "A permanent switch — Flashblocks completely replaced vanilla mode",
   "Only available on testnet, never enabled on mainnet",
   "Only available for institutional and whitelisted users"], 0)

# ======================================================================
# TOPIC 4: TRANSACTION ORDERING (~60 questions)
# ======================================================================

q("How are transactions ordered on Base?",
  ["By transaction hash value in alphabetical order",
   "By priority fee and arrival time at the sequencer",
   "By gas limit only, from lowest to highest",
   "By sender account age and account balance"])

q("What two factors primarily determine transaction ordering on Base?",
  ["Transaction size and transaction type (EOA versus contract)",
   "Priority fee offered and arrival time at the sequencer",
   "Sender address and transaction nonce number",
   "Gas price and gas limit combined"])

q("Priority fee is the primary factor for ordering on Base. What is the secondary factor?",
  ["Transaction hash, sorted in lexicographic order",
   "Arrival time at the sequencer, with earlier arrivals getting priority",
   "Calldata byte size, with smaller transactions going first",
   "Contract address being called, sorted by address numerically"])

q("If two transactions have the same priority fee on Base, how are they ordered?",
  ["By gas limit, with the lower gas limit transaction going first",
   "By arrival time, with the earlier arriving transaction getting priority",
   "By transaction hash, sorted in lexicographic order",
   "By sender address, sorted alphabetically by address"])

q("What is the first-come-first-served aspect of Base's transaction ordering?",
  ["When priority fees are equal, earlier arriving transactions are ordered first",
   "All transactions are processed strictly in order of arrival regardless of fee",
   "Arrival time is never considered — only the priority fee matters",
   "The very first transaction in each 200ms window gets guaranteed inclusion"], 0)

# Flashblock Assignment
q("How does transaction ordering determine which Flashblock a transaction lands in?",
  ["Higher priority fee transactions tend to land in the earlier Flashblocks",
   "Transactions are randomly assigned to Flashblocks by the sequencer software",
   "All transactions go to Flashblock 10 first and are then redistributed",
   "Transactions are assigned based solely on their calldata byte size"]) 

q("A transaction with a very high priority fee submitted early will likely land in which Flashblock?",
  ["Flashblock 10, the last and largest Flashblock",
   "One of the earliest Flashblocks, such as 1 or 2",
   "The next vanilla block only, skipping Flashblocks entirely",
   "It is randomly assigned to any of the 10 available Flashblocks"])

q("The assignment of transactions across Flashblocks is determined by what?",
  ["A lottery system run by the sequencer every 200ms",
   "Priority fee rank at each 200ms auction and submission arrival time",
   "The number of token transfers contained within each transaction",
   "The total ETH value being transferred in the transaction"])

q("What determines whether a transaction lands in Flashblock 1 versus Flashblock 5?",
  ["Only the transaction's calldata size determines its placement",
   "Its priority fee ranking at each 200ms auction and when it arrived at the sequencer",
   "The sender's address determines placement (0x addresses go first)",
   "Random assignment by the sequencer software without consideration of fee"])

q("A transaction submitted early with a medium priority fee might end up where?",
  ["An earlier Flashblock if the earlier auctions are less competitive",
   "Always in Flashblock 10 regardless of mempool conditions",
   "In a separate queue that only processes every 2 seconds",
   "In the next vanilla block, never in a Flashblock"], 0)

q("The sequencer's ordering of transactions directly determines which outcome?",
  ["Which Ethereum validators approve the Base block for settlement",
   "Which Flashblock each transaction is included in during the cycle",
   "The gas price on Ethereum L1 for the settlement batch",
   "The USD exchange rate for ETH traded on Coinbase"])

q("What happens if the mempool is empty when a Flashblock auction occurs?",
  ["The Flashblock is skipped entirely for that 200ms interval",
   "The Flashblock is still built, potentially with fewer or zero transactions",
   "The system pauses and waits until the mempool has at least one transaction",
   "The auction window is extended by another 200ms"], 1)

# Gas Allocation
q("How is gas allocated across the 10 Flashblocks?",
  ["Equally — each Flashblock independently receives 40M gas",
   "Cumulatively — Flashblock 1 has 40M, Flashblock 10 has 400M gas available",
   "Randomly — each Flashblock is assigned a random gas budget",
   "Decreasing — Flashblock 1 gets the most gas, Flashblock 10 gets the least"])

q("The cumulative gas allocation across Flashblocks means what exactly?",
  ["Each Flashblock has an independent 40M gas budget that resets after each one",
   "Gas budgets stack, so Flashblock 10 can hold transactions totaling approximately 400M gas",
   "Gas is split evenly into 10 equal pieces of 40M gas each with no carryover",
   "Only 4 out of 10 Flashblocks actually receive any gas allocation at all"])

q("By Flashblock 5, the cumulative gas budget available is approximately how much?",
  ["40M gas",
   "200M gas, which is 5/10 of the block gas limit",
   "400M gas, which is the full block gas limit",
   "80M gas, which is 2/10 of the block gas limit"])

q("By Flashblock 3, the cumulative gas budget is approximately how much?",
  ["40M gas",
   "80M gas",
   "120M gas, which is 3/10 of the block gas limit",
   "400M gas, which is the full block gas limit"])

q("By Flashblock 7, the cumulative gas budget is approximately how much?",
  ["80M gas",
   "280M gas, which is 7/10 of the block gas limit",
   "400M gas, which is the full block gas limit",
   "40M gas"])

q("Under the cumulative gas model, if Flashblock 1 uses 30M gas, what is available for Flashblock 2?",
  ["Only 10M gas remaining from the original 40M allocation",
   "Up to 80M gas, since the cumulative budget for Flashblock 2 is 2/10 of the total",
   "Only 40M gas regardless of how much Flashblock 1 actually used",
   "No gas at all — Flashblock 2 is skipped if Flashblock 1 used gas"])

q("Gas is allocated cumulatively across Flashblocks. What happens to unused budget?",
  ["Each Flashblock can use up to its cumulative fraction, and unused gas rolls forward",
   "Each Flashblock has a strict fixed budget that resets every 200ms",
   "Only Flashblock 10 can ever access the full 400M gas budget",
   "Unused gas is burned and cannot be used by any later Flashblocks"], 0)

q("The cumulative gas budget means by Flashblock N, available gas is approximately what?",
  ["N times 40M gas, which is N/10 of the full block gas limit",
   "40M gas regardless of the value of N",
   "(10 minus N) times 40M gas, decreasing as N increases",
   "400M divided by N, divided evenly among remaining Flashblocks"], 0)

q("If Flashblocks 1 through 4 consume 30M gas each (120M total), what remains for Flashblock 5?",
  ["200M minus 120M equals 80M (remaining up to the 5/10 cumulative budget)",
   "40M (the independent budget just for Flashblock 5)",
   "400M (the full block limit minus the 120M already consumed)",
   "40M + 80M + 120M + 160M, all divided by 4"], 0)

q("With 10 Flashblocks per full block, what does the cumulative gas model ensure?",
  ["Full blocks can reach total capacity while earlier Flashblocks get proportional shares",
   "Only Flashblock 10 can ever include large or complex transactions",
   "Gas limits strictly decrease after Flashblock 5 to save room",
   "Each Flashblock must use exactly its allocated gas or lose it"], 0)

# Transaction Flow & Practical Implications
q("Which sequence correctly describes transaction flow on Base?",
  ["User submits to mempool, priority fee auction, sequencer builds Flashblock, block broadcast",
   "User submits to sequencer, sequencer includes in block, Ethereum confirms, Flashblock built",
   "User submits to Ethereum L1, Ethereum validates, Base executes, Flashblock broadcast",
   "User submits to Coinbase, Coinbase approves, mempool processes, Flashblock built"], 0)

q("A user who submits a transaction right at the end of a 200ms auction window can expect what?",
  ["Inclusion in the current Flashblock if their fee wins the active auction",
   "They must wait for the next Flashblock auction 200ms later to compete",
   "They pay a penalty fee for submitting late to the current auction",
   "Their transaction is automatically included in Flashblock 10"], 0)

q("What is a practical implication of the ordering lock in Flashblocks for searchers?",
  ["They can reliably front-run any transaction at any point in the cycle",
   "They must ensure their transactions arrive before the Flashblock auction closes",
   "They can submit profitable transactions after the auction and still get priority",
   "They can freely reorder transactions after the Flashblock is already broadcast"])

q("Under the Flashblock system, how many distinct priority fee auctions occur per full block?",
  ["1 auction per full block cycle",
   "10 auctions, one for each Flashblock in the 2-second cycle",
   "5 auctions, one per every 2 Flashblocks built",
   "The number varies based on how congested the network is"])

q("What ordering rule applies when the mempool has many high-fee transactions at the start of a cycle?",
  ["All go to Flashblock 1 regardless of their specific fee levels",
   "They are ranked by priority fee, with the highest fees entering the earliest Flashblocks",
   "They are queued and processed in the vanilla 2-second block instead",
   "The system switches from Flashblock mode to simple FIFO ordering"])

q("How does the priority fee auction interact with Flashblock gas budgets?",
  ["The auction selects which transactions fill each Flashblock up to its gas budget capacity",
   "The auction only runs once per full block and Flashblocks are filled afterward",
   "The auction determines the gas budgets themselves, not transaction inclusion",
   "The auction runs independently and does not consider gas budgets at all"], 0)

q("What happens to leftover gas budget from an earlier Flashblock under the cumulative model?",
  ["It rolls forward and becomes available to later Flashblocks in the same cycle",
   "It is permanently burned and cannot be recovered by any later Flashblock",
   "It is returned to the sequencer as profit for the operator",
   "It is distributed as a gas rebate to users in the earlier Flashblocks"], 0)

q("A user submits a transaction with a low priority fee when the mempool is nearly empty. Where does it go?",
  ["It may be included in an early Flashblock since there is little competition",
   "It always goes to Flashblock 10 regardless of competition levels",
   "It is rejected for having too low a priority fee",
   "It waits for the next vanilla 2-second block and skips Flashblocks"], 0)

q("What ordering behavior can users expect when Base is operating in vanilla mode?",
  ["Transactions are ordered by priority fee in 2-second blocks built by base-reth-node",
   "Transactions are ordered randomly in 200ms blocks built by base-builder",
   "Transactions are ordered by size in 12-second blocks like Ethereum L1",
   "Transactions are ordered by sender reputation"], 0)

q("If a user's transaction is not included in Flashblock 1, what determines whether it goes to Flashblock 2?",
  ["Its priority fee ranking in the second 200ms auction relative to new arrivals",
   "It automatically rolls over to Flashblock 2 regardless of fee or competition",
   "It is kicked out of the Flashblock system entirely",
   "It must be resubmitted by the user with a higher fee"], 0)

# ======================================================================
# TOPIC 5: "Which is NOT" and Edge Cases (~15 more)
# ======================================================================

q("Which of the following is NOT a factor in Base transaction ordering?",
  ["Priority fee offered by the transaction sender",
   "Arrival time at the Base sequencer",
   "Sender's BASE token wallet balance",
   "Which Flashblock is currently being constructed by the sequencer"], 2)

q("Which is NOT a component of the Base Flashblock system?",
  ["base-builder software for constructing blocks",
   "Priority fee auctions occurring every 200ms",
   "Validators staking native BASE tokens for consensus participation",
   "10 Flashblocks per full block with cumulative gas budgets"], 2)

q("All of the following are true about Flashblocks EXCEPT:",
  ["They are built every 200 milliseconds by the Base sequencer",
   "They use the base-builder software to construct blocks",
   "They require validators to stake tokens for the network",
   "There are 10 Flashblocks per full block on Base"], 2)

q("All of the following are Base protocol upgrades EXCEPT:",
  ["Beryl (the latest upgrade)",
   "Azul (a prior upgrade)",
   "Optimism (a prior upgrade)",
   "Berlin (an Ethereum fork name)"], 3)

q("Which of these is NOT part of Base's builder support programs?",
  ["Builder Rewards for developers on Base",
   "Base Grants for new projects and builders",
   "BASE token staking rewards for network validators",
   "Base Batches supporting builders in the ecosystem"], 2)

q("All of the following are true about Flashblock gas budgets EXCEPT:",
  ["Flashblock 1 has approximately 40M gas available",
   "Flashblock 2 has approximately 80M gas available",
   "Flashblock 10 has approximately 400M gas (the full block limit)",
   "Flashblock 1 has approximately 400M gas (the full block limit)"], 3)

q("Which of the following is NOT a benefit of Base's EVM equivalence?",
  ["Developers can deploy existing Ethereum contracts without modification",
   "Standard Ethereum tooling like Hardhat and Foundry works on Base",
   "Base introduces new EVM opcodes that are not available on Ethereum",
   "Developers do not need to learn a new programming language for Base"], 2)

q("Base's Flashblock system does NOT do which of the following?",
  ["Produce blocks every 200 milliseconds as preconfirmations",
   "Require priority fee auctions for transaction inclusion in blocks",
   "Guarantee that every transaction reaches L1 finality within 200ms",
   "Use base-builder software to construct Flashblocks"], 2)

q("Which is NOT part of the Base ecosystem?",
  ["Applications and decentralized apps running on Base",
   "Automated agents and bots interacting with smart contracts",
   "A native BASE governance token used for on-chain staking and consensus",
   "Bridge infrastructure connecting Base to Ethereum mainnet"], 2)

q("In the Base Flashblock system, ordering is NOT determined by which factor?",
  ["Priority fee offered by each competing transaction",
   "Arrival time at the Base sequencer",
   "The sender's past transaction history or on-chain reputation",
   "Which Flashblock slot is currently being built"], 2)

q("All of the following are correct about the per-tx gas maximum on Base EXCEPT:",
  ["It is approximately 16.7 million gas units per transaction",
   "It fits within Flashblock 1's approximately 40M gas budget comfortably",
   "It equals the full block gas limit of approximately 400M gas",
   "It ensures multiple transactions can fit in even the smallest Flashblock"], 2)

q("Which of these is NOT a program offered by Base for builder support?",
  ["Builder Rewards for developers building on Base",
   "Retroactive Funding for past ecosystem contributions",
   "Base Batches as a builder support program",
   "Validator Delegation Rewards based on staking activity"], 3)

q("Which of the following does NOT describe Base's EVM equivalence?",
  ["Same bytecode as Ethereum for smart contract execution",
   "Same RPC endpoints as Ethereum for tooling compatibility",
   "Same consensus mechanism as Ethereum (fully Proof of Stake)",
   "Same developer tooling as Ethereum (Hardhat, Foundry, Remix)"], 2)

q("Which of these is NOT a correct pairing for Base?",
  ["Chain ID in decimal: 8453",
   "Block time in vanilla mode: 2 seconds",
   "Block time with Flashblocks enabled: 200 milliseconds",
   "Block time with Flashblocks enabled: 12 seconds"], 3)

q("Which of the following is NOT part of Base's upgrade history?",
  ["Beryl (the latest protocol upgrade)",
   "Azul (a prior Base protocol upgrade)",
   "Optimism (a prior Base protocol upgrade)",
   "Constantinople (an Ethereum mainnet fork)"], 3)

q("Which of the following is NOT a feature of Flashblock preconfirmations?",
  ["Fast feedback that a transaction has been ordered by the sequencer",
   "A signal before the full block reaches finality on Ethereum L1",
   "Instant L1-level finality guarantee within 200 milliseconds",
   "Useful for applications that benefit from sub-second transaction feedback"], 2)

q("Which of the following does Base NOT use for its security?",
  ["Posting transaction calldata to Ethereum for settlement",
   "Inheriting Ethereum security through the OP Stack rollup mechanism",
   "A Proof of Stake validator set operating directly on the Base L2",
   "A fault proof system to challenge invalid state transitions"], 2)

# ======================================================================
# ADDITIONAL QUESTIONS TO REACH ~250
# ======================================================================

q("How does Base's architecture differ from a monolithic L1 blockchain?",
  ["Base separates execution from settlement, while monolithic L1s do everything on one chain",
   "Base is faster but less secure than monolithic L1 blockchains",
   "Base has no execution layer unlike monolithic L1 blockchains",
   "Base and monolithic L1s have identical architecture"])

q("What happens when a Flashblock's cumulative gas budget is exceeded?",
  ["Remaining transactions are deferred to the next Flashblock in the cycle",
   "The Flashblock is discarded and rebuilt with fewer transactions",
   "The block gas limit is automatically increased",
   "All exceeding transactions are permanently rejected"], 0)

q("Which statement about Base's chain ID 8453 is accurate?",
  ["It is unique to Base mainnet and distinguishes it from other L2s and L1 Ethereum",
   "It is shared with Optimism mainnet for compatibility",
   "It is the same as the Ethereum mainnet chain ID",
   "It changes with every protocol upgrade"])

q("What is the main benefit of Base being built on the OP Stack rather than a proprietary stack?",
  ["It benefits from shared security research, standards, and improvements across the OP ecosystem",
   "It can process an unlimited number of transactions per second",
   "It does not require any sequencer to operate properly",
   "It has exclusive access to Coinbase's user base of millions"])

q("If a dApp needs to interact with Base from a frontend, which library would it use?",
  ["Standard Ethereum libraries like ethers.js or web3.js pointed at Base's RPC endpoint",
   "A proprietary Base-specific JavaScript library",
   "The Coinbase Wallet SDK exclusively",
   "The Optimism SDK for OP Stack chains"])

q("How does the Base ecosystem support ledgers as part of its infrastructure?",
  ["Through on-chain accounting and record-keeping that tracks balances and state transitions",
   "Through physical hardware wallets sold by Coinbase",
   "Through accounting firms that audit Base transactions",
   "Through a specific type of smart contract for double-entry bookkeeping"], 0)

q("What distinguishes Base's approach to L2 scaling from other approaches?",
  ["It combines EVM equivalence, the OP Stack, Coinbase's support, and Flashblock technology",
   "It is the only L2 that does not post data to Ethereum L1",
   "It is the only L2 that uses a centralized sequencer",
   "It is the only L2 that does not support smart contracts"], 0)

q("Which of these correctly describes the Base ecosystem's components?",
  ["Apps (decentralized applications), accounts (user wallets), agents (automated bots), ledgers (state records), and bridges",
   "Only apps and accounts with no other infrastructure",
   "Only bridges to other L2 rollup networks",
   "Only agent infrastructure for automated trading"]) 

q("A transaction is submitted to Base with a very high priority fee but arrives 150ms into a 200ms Flashblock auction. What happens?",
  ["It competes in the current auction and may be included if its fee is the highest",
   "It waits for the next Flashblock auction since it missed the cutoff",
   "It is automatically included in Flashblock 10",
   "It bypasses the auction and replaces a lower-fee transaction already selected"], 0)

q("What is the practical effect of having 10 Flashblocks per full block?",
  ["It provides more granular transaction ordering and faster preconfirmation feedback",
   "It slows down the overall block production rate on Base",
   "It reduces the total number of transactions that can be processed",
   "It eliminates the need for priority fee auctions entirely"], 0)

q("How does Base's per-transaction gas maximum of ~16.7M compare to Ethereum L1's limits?",
  ["It is similar to Ethereum L1's per-transaction gas limit, making large contract calls feasible on both",
   "It is much smaller than Ethereum L1's per-transaction gas limit",
   "It is much larger than Ethereum L1's per-transaction gas limit",
   "It has no relation to Ethereum L1's gas mechanics"], 0)

q("Which of the following is the correct relationship between Flashblock number and gas budget?",
  ["Flashblock N has approximately N/10 of the total 400M full block gas limit available cumulatively",
   "Flashblock N has approximately (10-N)/10 of the gas limit available",
   "All Flashblocks have exactly 40M gas regardless of their number",
   "Flashblock N has a random gas budget unrelated to N"], 0)

q("Why does Base offer Builder Rewards as part of its ecosystem?",
  ["To incentivize developers to build applications and grow the Base ecosystem",
   "To reward users who hold BASE tokens in their wallets",
   "To compensate validators who run Base nodes",
   "To fund Ethereum L1 research and development"])

q("What makes Base's Flashblock system different from traditional block production?",
  ["It produces preconfirmation blocks every 200ms before the full block is assembled",
   "It produces blocks directly on Ethereum L1 instead of on the L2",
   "It does not use any sequencer for ordering transactions",
   "It uses a completely different virtual machine than Ethereum"])

q("How does Base's separation of consensus from execution benefit developers?",
  ["Execution can be upgraded independently without changing the consensus mechanism",
   "Developers must learn two different programming paradigms",
   "Consensus runs faster but execution is slower",
   "There is no benefit — it adds unnecessary complexity"], 0)

q("When would a transaction with a medium priority fee be included in Flashblock 1 rather than Flashblock 3?",
  ["If the mempool has relatively few high-fee transactions at the time of the first auction",
   "Never — medium-fee transactions always go to later Flashblocks",
   "Only if the transaction is submitted by a whitelisted address",
   "Only if the transaction size is smaller than 21,000 gas"], 0)

q("What is the role of agents in the Base ecosystem?",
  ["Automated programs that interact with Base smart contracts, such as trading and automation bots",
   "Human representatives of Coinbase who manually approve transactions",
   "AI systems that validate blocks on the Base L2 network",
   "Third-party auditors who review smart contract code"], 0)

q("Which feature of the OP Stack allows Base to post batches to Ethereum?",
  ["The batch submission mechanism that compresses and posts calldata to L1",
   "The fraud proof mechanism that validates state transitions",
   "The sequencer that orders transactions every 200ms",
   "The execution engine that runs EVM bytecode"], 0)

q("Why does Base have a Security Council rather than fully automated governance?",
  ["To provide a human-in-the-loop for emergency situations and protocol upgrades",
   "Because automated governance is not technically possible on the OP Stack",
   "Because Coinbase requires manual approval for all protocol changes",
   "To replace the need for fraud proofs in the security model"], 0)

q("What is the relationship between Base's vanilla mode and its Flashblocks mode?",
  ["Both are valid configurations — Flashblocks is an enhanced option using base-builder for faster preconfirmations",
   "Vanilla mode replaced Flashblocks due to performance issues",
   "Flashblocks replaced vanilla mode permanently and cannot be disabled",
   "They are the same thing with different marketing names"], 0)

q("In the context of Flashblocks, what does 'preconfirmation' mean exactly?",
  ["A commitment from the sequencer that a transaction has been ordered in a specific Flashblock slot",
   "A confirmation from Ethereum L1 that the transaction has been settled",
   "A guarantee that the transaction will never be reverted",
   "A signal that the transaction has been broadcast to the mempool"], 0)

q("What advantage does Base's EVM equivalence provide in terms of tooling?",
  ["Developers can use the exact same Hardhat, Foundry, or Remix setup they use for Ethereum",
   "Developers must set up entirely new tooling pipelines for Base",
   "Only Truffle framework is compatible with Base's EVM",
   "Developers need to compile their contracts twice for Ethereum and Base separately"], 0)

q("Which of the following accurately describes Base's upgrade history?",
  ["Previous upgrades include Azul and Optimism, with Beryl being the latest",
   "Previous upgrades include Berlin and London, with Beryl being the latest",
   "The only upgrade to date has been the Beryl upgrade",
   "Base has never undergone a protocol upgrade since launch"], 0)

q("What is the maximum theoretical gas per full block on Base?",
  ["Approximately 400M gas, achieved when Flashblock 10 is filled completely",
   "Approximately 40M gas, the budget of Flashblock 1",
   "Approximately 16.7M gas, the per-transaction maximum",
   "There is no maximum — blocks can be arbitrarily large"])

q("If a user wants to verify Base's state without running a full node, what can they use?",
  ["State roots posted to Ethereum, allowing light verification of the L2 state",
   "They must run a Base full node to verify any state",
   "They can use Coinbase's API for state verification",
   "State verification is not possible on the Base network"], 0)

q("What determines the order in which Flashblocks are constructed within a 2-second window?",
  ["Flashblocks are built sequentially every 200ms, numbered 1 through 10",
   "Flashblocks are built in reverse order, starting from Flashblock 10",
   "Flashblocks are built randomly within the 2-second window",
   "Flashblocks are built all at once and then numbered arbitrarily"], 0)

q("How does Flashblock technology improve the user experience on Base?",
  ["By reducing wait times for transaction preconfirmations from 2 seconds to 200ms",
   "By reducing transaction fees to zero for all users",
   "By increasing the block gas limit to unlimited",
   "By removing the need for users to pay priority fees"], 0)

q("Which of these best describes Base's position in the L2 ecosystem?",
  ["The number one Ethereum L2 by various metrics, incubated by Coinbase",
   "A minor L2 with limited adoption compared to competitors",
   "A testnet-only chain that has not launched on mainnet",
   "A competitor to Ethereum rather than an L2 built on top of it"], 0)

q("What is the primary purpose of Base's Bridge?",
  ["To facilitate the movement of assets between Ethereum mainnet and Base",
   "To connect Base to non-Ethereum chains like Solana",
   "To swap tokens within the Base ecosystem",
   "To provide a fiat on-ramp for purchasing crypto"], 0)

q("How does Base ensure that its Flashblock ordering is fair?",
  ["By using priority fee auctions every 200ms where all transactions compete equally based on fee",
   "By rotating through user addresses in alphabetical order",
   "By using a lottery system that gives every transaction equal chance",
   "By allowing Coinbase to manually order all transactions"])

q("What problem does the dynamic mempool solve in the Flashblock system?",
  ["It prevents the mempool from being locked during block construction, allowing continuous transaction acceptance",
   "It eliminates the need for priority fee auctions entirely",
   "It reduces the total gas available per block",
   "It prevents all front-running and MEV on the network"], 0)

q("Which of the following would be an invalid use case for Base's EVM equivalence?",
  ["Deploying a Solana Rust program directly on Base without modification",
   "Deploying a Solidity smart contract originally written for Ethereum",
   "Using Hardhat to test and deploy contracts on Base",
   "Using ethers.js to interact with a smart contract on Base"], 0)

q("How does the Base ecosystem's agent infrastructure benefit developers?",
  ["Developers can deploy automated programs that interact with smart contracts for trading, monitoring, and automation",
   "Only Coinbase can deploy agents on Base",
   "Agents replace smart contracts entirely on Base",
   "Agents are only available on testnet, not on mainnet"], 0)

q("What is the key trade-off between vanilla mode and Flashblocks mode on Base?",
  ["Flashblocks offers faster preconfirmations but may occasionally break expected ordering; vanilla is simpler but slower",
   "Vanilla mode is faster but less secure than Flashblocks",
   "Flashblocks mode reduces total throughput compared to vanilla",
   "There is no trade-off — Flashblocks is strictly better in all ways"], 0)

q("What is the role of the base-builder software in Base's architecture?",
  ["It builds blocks, conducts priority fee auctions every 200ms, and produces Flashblocks",
   "It settles transactions to Ethereum L1",
   "It runs the execution engine for EVM bytecode",
   "It provides the RPC endpoint for user wallets"])

q("How do Base's Flashblocks fit into the broader OP Stack ecosystem?",
  ["Flashblocks are a Base-specific enhancement to the standard OP Stack block production mechanism",
   "Flashblocks are a standard OP Stack feature available on all OP Stack chains",
   "Flashblocks are not compatible with the OP Stack at all",
   "Flashblocks are an Ethereum L1 feature inherited by Base"], 0)

# ======================================================================
# FINAL: Shuffle and output
# ======================================================================

random.shuffle(questions)

# Assign sequential IDs
for i, quiz in enumerate(questions):
    quiz["id"] = i

# Count distribution
idx_dist = Counter(q["correctIndex"] for q in questions)
print(f"Total questions: {len(questions)}")
print(f"Correct index distribution: {dict(sorted(idx_dist.items()))}")

# Create output
output = {
    "meta": {
        "ecosystem": "Base",
        "batchId": "base-2026-07-11-batch1",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totalQuizzes": len(questions),
        "questionsPerSession": 5
    },
    "quizzes": questions
}

output_path = "/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch1.json"
with open(output_path, "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

import os
file_size = os.path.getsize(output_path)
print(f"\nWritten to: {output_path}")
print(f"File size: {file_size} bytes")

# === VALIDATION ===
print("\n=== VALIDATION ===")
errors = []
for q_item in questions:
    if len(q_item["options"]) != 4:
        errors.append(f"Question {q_item['id']}: {len(q_item['options'])} options instead of 4")
    if q_item["correctIndex"] not in [0, 1, 2, 3]:
        errors.append(f"Question {q_item['id']}: invalid correctIndex {q_item['correctIndex']}")
    if not q_item["question"].strip().endswith("?"):
        errors.append(f"Question {q_item['id']}: missing question mark: {q_item['question'][:70]}")
    for i, opt in enumerate(q_item["options"]):
        if isinstance(opt, list):
            errors.append(f"Question {q_item['id']}: option {i} is a nested list!")
        if not isinstance(opt, str):
            errors.append(f"Question {q_item['id']}: option {i} is not a string: {type(opt)}")

# Check for duplicate questions
seen = {}
for q_item in questions:
    txt = q_item["question"].lower().strip()
    if txt in seen:
        errors.append(f"Duplicate question: IDs {q_item['id']} and {seen[txt]}: {q_item['question'][:70]}")
    seen[txt] = q_item["id"]

if errors:
    print(f"Found {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
else:
    print("All validations passed!")

# JSON validity
try:
    json_str = json.dumps(output)
    json.loads(json_str)
    print("JSON is valid!")
except json.JSONDecodeError as e:
    print(f"JSON INVALID: {e}")
