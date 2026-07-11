#!/usr/bin/env python3
"""Generate 200+ unique Base mainnet quiz questions for batch4."""
import json
import random
from collections import Counter

questions = []
qid_counter = [0]  # mutable for closures

def add(q):
    q["id"] = qid_counter[0]
    qid_counter[0] += 1
    questions.append(q)

def QA(question, options, correctIndex):
    add({
        "question": question,
        "options": options,
        "correctIndex": correctIndex
    })

# ============================================================
# TOPIC 1: NODE OPERATIONS (~42 questions)
# ============================================================

QA("Which software runs Base in vanilla mode (2s blocks)?",
   ["base-builder (the sequencer block-building tool)",
    "base-reth-node (the execution engine)",
    "op-node (the consensus layer node)",
    "geth (standard Ethereum execution client)"], 1)

QA("Which software runs Base in Flashblocks mode as the sequencer?",
   ["base-reth-node", "base-builder", "op-geth", "op-node"], 1)

QA("A node operator switching between Flashblocks and vanilla mode changes:",
   ["The physical hardware of the node server",
    "The software from base-builder to base-reth-node or vice versa",
    "The RPC endpoint provider",
    "The Chain ID from 8453 to 84532"], 1)

QA("Which of the following is NOT an available option for running a Base node?",
   ["Running base-reth-node in vanilla mode",
    "Running base-builder in Flashblocks mode",
    "Running a full node with native BASE token staking rewards",
    "Using snapshots for faster sync"], 2)

QA("Which of the following is NOT a service provided by node providers for Base?",
   ["Hosted RPC endpoints for dApps",
    "Performance tuning guidance",
    "Snapshots for faster node sync",
    "Native BASE token staking rewards"], 3)

QA("What is the primary benefit of using snapshots when syncing a Base node?",
   ["It allows the node to mine new BASE tokens",
    "It reduces the time needed to sync from genesis",
    "It increases the block gas limit for the node operator",
    "It enables the node to participate in fault proof challenges"], 1)

QA("Node providers for Base offer which of the following hosted services?",
   ["Only archival node access",
    "Hosted RPC endpoints, snapshots, and performance tuning guides",
    "Only read-only node access",
    "Only validator staking services"], 1)

QA("A developer troubleshooting a Base node issue would consult:",
   ["The Base Troubleshooting Transactions guide only",
    "The Base node troubleshooting documentation and performance tuning guides",
    "The Ethereum Yellow Paper",
    "The Coinbase customer support portal"], 1)

QA("When running a Base node, performance tuning helps achieve:",
   ["Lowering transaction fees for all network users",
    "Optimizing sync speed and resource usage for the node operator",
    "Increasing the block reward for the node",
    "Enabling mining of native BASE tokens"], 1)

QA("Which is a use case for running a base-reth-node?",
   ["Building Flashblocks at 200ms intervals",
    "Operating as an execution engine in vanilla mode",
    "Running priority fee auctions for the network",
    "Minting new tokens on the Base network"], 1)

QA("All of the following are true about Base node snapshots EXCEPT:",
   ["They help new nodes sync faster",
    "They contain a copy of the chain state at a specific block height",
    "They are mandatory for all Base node operators",
    "They are listed as a resource available from node providers"], 2)

QA("The base-builder software is responsible for which task?",
   ["Handling RPC requests from wallets and dApps",
    "Building blocks and running priority fee auctions every 200ms",
    "Posting batch data to Ethereum L1",
    "Validating state roots in the fault proof system"], 1)

QA("How does base-reth-node differ from base-builder in the Base architecture?",
   ["base-reth-node handles execution in vanilla mode; base-builder builds Flashblocks",
    "base-reth-node builds Flashblocks; base-builder handles vanilla mode",
    "They are the same software with different configuration flags",
    "base-reth-node is the consensus layer; base-builder is the execution layer"], 0)

QA("When setting up a Base node, what is recommended for faster initial sync?",
   ["Running the node on a Raspberry Pi",
    "Using snapshots provided by node infrastructure services",
    "Syncing from the genesis block without optimizations",
    "Disabling all network connectivity for security"], 1)

QA("A hosted node provider for Base typically offers all of the following EXCEPT:",
   ["Access to dedicated RPC endpoints",
    "Support for WebSocket connections",
    "Sequencer operation rights and priority fee revenue",
    "Archival data access for historical queries"], 2)

QA("Which statement about running a Base node is correct?",
   ["You must stake BASE tokens to run a node",
    "Both base-reth-node and base-builder are available software options depending on mode",
    "Only Coinbase is permitted to run Base nodes",
    "Node operators receive a share of transaction fees"], 1)

QA("What troubleshooting resource does Base provide for transaction issues?",
   ["The Troubleshooting Transactions guide",
    "A 24/7 phone support hotline",
    "The Ethereum L1 mempool explorer",
    "A Coinbase customer service ticket system"], 0)

QA("Which scenario benefits from Base's node snapshots?",
   ["A dApp developer deploying a new ERC-20 token",
    "A node operator setting up a new Base node for the first time",
    "A user bridging ETH from Ethereum to Base",
    "An auditor reviewing Base smart contract code"], 1)

QA("The base-reth-node in vanilla mode produces blocks at what interval?",
   ["200 milliseconds", "2 seconds", "12 seconds", "1 second"], 1)

QA("Which is NOT a correct statement about Base node operations?",
   ["base-reth-node is used for vanilla mode block production",
    "base-builder is used for Flashblocks mode block production",
    "Snapshots are available to speed up node sync times",
    "Running a Base node earns the operator BASE tokens as block rewards"], 3)

QA("Performance tuning guidance for Base nodes is most useful for:",
   ["dApp developers writing frontend code",
    "Node operators optimizing hardware and sync configuration",
    "Token holders trying to stake their tokens",
    "Users trying to reduce their transaction fees"], 1)

QA("Which software is responsible for the execution environment (EVM) on Base?",
   ["base-builder", "base-reth-node (based on reth)", "op-batcher", "op-proposer"], 1)

QA("The listed node providers for Base include:",
   ["Alchemy, Infura, and QuickNode",
    "Coinbase Cloud exclusively",
    "Only self-hosted nodes",
    "Amazon Web Services blockchain service only"], 0)

QA("A Base node operator troubleshooting sync issues would use:",
   ["The Base performance tuning and troubleshooting documentation",
    "The Ethereum L1 consensus specification",
    "The Coinbase exchange API documentation",
    "The Optimism token economics whitepaper"], 0)

QA("Which of the following best describes base-reth-node?",
   ["A reth-based execution engine customized for Base and OP Stack chains",
    "A block explorer for viewing Base transaction data",
    "A wallet application for managing Base assets",
    "A mining tool for producing new blocks"], 0)

QA("All of the following are node providers for Base EXCEPT:",
   ["Alchemy", "Infura", "QuickNode", "Binance Smart Chain"], 3)

QA("A node operator who wants historical state data should consider:",
   ["Running an archival node with access to full historical state",
    "Only running a pruned node with the most recent 100 blocks",
    "Using the Base Dashboard for all historical queries",
    "Contacting Coinbase for historical data access"], 0)

QA("Base node snapshots solve what specific problem?",
   ["High Ethereum L1 gas costs for posting data",
    "Long sync times when setting up a new full node from genesis",
    "Smart contract deployment failures",
    "Wallet connectivity issues"], 1)

# ============================================================
# TOPIC 2: INTEGRATION (~42 questions)
# ============================================================

QA("Which chain ID should be used when adding Base mainnet to MetaMask?",
   ["10 (Optimism's chain ID)", "42161 (Arbitrum's chain ID)", "8453 (Base's chain ID)", "1 (Ethereum's chain ID)"], 2)

QA("To connect a wallet like MetaMask to Base, what must be configured?",
   ["A new blockchain network with Chain ID 8453 and Base's RPC URL",
    "Only the wallet address without any network configuration",
    "A VPN connection routed through Coinbase's servers",
    "A one-time registration with the Base Security Council"], 0)

QA("Which block explorer is the canonical one for Base mainnet?",
   ["Etherscan", "Basescan", "Solscan", "Arbiscan"], 1)

QA("CCTP on Base is designed for transferring which type of asset?",
   ["Native ETH between chains",
    "Any ERC-20 token",
    "Native USDC across supported chains using Circle's infrastructure",
    "NFTs between L2 networks"], 2)

QA("Exchanges that support Base deposits and withdrawals allow users to:",
   ["Only deposit, never withdraw Base assets",
    "Move funds between the exchange wallet and Base mainnet directly",
    "Only trade Base assets within the exchange without onchain movement",
    "Mine BASE tokens through the exchange platform"], 1)

QA("When integrating Base into a wallet application, which standard should be followed?",
   ["A proprietary Base wallet SDK that replaces Ethereum JSON-RPC",
    "Standard Ethereum JSON-RPC with Chain ID 8453 and Base RPC URL",
    "The Solana wallet adapter standard",
    "The Bitcoin BIP-44 standard only"], 1)

QA("What is the standard RPC URL format for connecting to Base mainnet?",
   ["https://mainnet.base.org or a provider-specific endpoint",
    "https://ethereum.org/base",
    "https://base.optimism.io",
    "https://coinbase.com/base-rpc"], 0)

QA("Data indexers on Base allow developers to:",
   ["Query and index onchain data efficiently for dApps",
    "Run Base sequencer nodes",
    "Mint new BASE tokens",
    "Validate Base blocks directly"], 0)

QA("CCTP (Cross-Chain Transfer Protocol) is operated by which company?",
   ["Coinbase", "Circle", "Optimism Foundation", "Base DAO"], 1)

QA("Which is NOT a standard way to integrate Base into a project?",
   ["Adding Base as a custom network in MetaMask with Chain ID 8453",
    "Using a third-party provider like Alchemy or Infura for RPC access",
    "Replacing all Ethereum JSON-RPC calls with a Base-specific proprietary protocol",
    "Using Basescan to verify deployed smart contracts"], 2)

QA("A dApp developer using Basescan can verify what?",
   ["The balance of any wallet on Ethereum L1",
    "Transactions, contracts, and wallet activity on Base mainnet",
    "The real-time price of the BASE token",
    "The status of Bitcoin transactions"], 1)

QA("The recommended approach for a wallet to support Base mainnet is:",
   ["Use any standard Ethereum RPC provider and set Chain ID to 8453",
    "Deploy a custom bridge from the wallet to Base",
    "Run a full Base node inside the wallet application",
    "Register the wallet with Coinbase for approval"], 0)

QA("For cross-chain USDC transfers involving Base, CCTP provides what advantage?",
   ["Native USDC transfers without wrapping or liquidity pools",
    "Lower fees than any other method on all chains",
    "Instant finality with no challenge period",
    "Support for all ERC-20 tokens, not just USDC"], 0)

QA("A centralized exchange supporting Base enables:",
   ["Direct deposits and withdrawals between the exchange and Base mainnet",
    "Free transaction processing on Base",
    "Exclusive access to Base node operation",
    "Priority fee refunds on Base transactions"], 0)

QA("When adding Base to a wallet like MetaMask, which field must match Chain ID 8453?",
   ["The RPC URL", "The chain ID in the network configuration", "The block explorer URL", "The wallet's derivation path"], 1)

QA("Basescan provides all of the following features EXCEPT:",
   ["Transaction search and lookup",
    "Smart contract source code verification",
    "Real-time trading of BASE tokens",
    "Wallet address balance checks"], 2)

QA("Which is the standard RPC endpoint style people use for Base?",
   ["A standard Ethereum JSON-RPC endpoint pointed at Base mainnet",
    "A custom GraphQL endpoint only available from Coinbase",
    "A REST API that differs from the Ethereum JSON-RPC standard",
    "A WebSocket-only connection with no HTTP fallback"], 0)

QA("Data indexers on Base are used primarily to:",
   ["Make onchain data searchable and queryable for dApps and analytics",
    "Validate transactions on the Base network",
    "Execute trades automatically on DEXes",
    "Store user passwords securely onchain"], 0)

QA("Integrating CCTP into a dApp on Base allows for:",
   ["Seamless native USDC transfers between Base and other CCTP-supported chains",
    "Free transaction processing for all users",
    "Direct token swaps between any ERC-20 and USDC",
    "Access to Coinbase's order book for trading"], 0)

QA("A user wants to bridge ETH from Ethereum to Base. Which method is correct?",
   ["Use CCTP (it supports all assets including ETH)",
    "Use the Base Bridge (which uses Optimism's standard bridge contracts)",
    "Use the Solana Bridge",
    "Send ETH directly to a Base address without any bridge"], 1)

QA("Which of the following node providers offers hosted RPC services for Base?",
   ["Alchemy", "Infura", "QuickNode", "All of the above"], 3)

QA("When integrating Base into a custom wallet, which method is NOT standard JSON-RPC?",
   ["eth_blockNumber", "eth_sendTransaction", "base_getFlashblockStatus", "eth_getBalance"], 2)

QA("To verify a deployed contract on Base, which tool would a developer use?",
   ["Basescan's contract verification feature",
    "The Ethereum L1 Etherscan",
    "Solscan contract verification",
    "The Coinbase exchange"], 0)

QA("When adding Base to MetaMask manually, all of the following are required EXCEPT:",
   ["RPC URL for Base mainnet",
    "Chain ID 8453",
    "Currency symbol (ETH)",
    "A valid Coinbase API key"], 3)

QA("A wallet that already supports Ethereum mainnet can connect to Base by:",
   ["Adding Base as a custom network with chain ID 8453 and appropriate RPC URL",
    "Installing a separate wallet application specifically for Base",
    "Using the same configuration as Ethereum mainnet with no changes",
    "Contacting Coinbase support for integration instructions"], 0)

QA("The Base Bridge on base.org enables transfers between:",
   ["Base and Solana",
    "Ethereum L1 and Base",
    "Base and Bitcoin",
    "Base and Arbitrum"], 1)

# ============================================================
# TOPIC 3: SMART CONTRACTS / DEPLOY (~42 questions)
# ============================================================

QA("What is the address of the GasPriceOracle predeploy contract on Base?",
   ["0x420000000000000000000000000000000000000F",
    "0x00000000000000000000000000000000000000F",
    "0x42000000000000000000000000000000000000FF",
    "0x4200000000000000000000000000000000000010"], 0)

QA("Which is a predeployed contract on Base inherited from the OP Stack?",
   ["The L1StandardBridge on Base L2",
    "The Uniswap V3 Router",
    "The Chainlink Price Oracle",
    "The Aave Lending Pool"], 0)

QA("Why can Ethereum smart contracts be deployed on Base without modification?",
   ["Base uses a compatibility layer that translates EVM bytecode",
    "Base is EVM-equivalent, supporting the same bytecode and opcodes as Ethereum",
    "Base automatically rewrites contracts during deployment",
    "Base runs a modified EVM with backward compatibility"], 1)

QA("The GasPriceOracle predeploy provides which method for L1 fee estimation?",
   ["getNativeTokenPrice()",
    "getL1Fee(bytes) for computing L1 data fees",
    "estimateDeploymentCost()",
    "getBlockReward()"], 1)

QA("Which development framework can be used to deploy smart contracts on Base?",
   ["Only Hardhat",
    "Hardhat, Foundry, and Remix — the same tools as Ethereum",
    "Only Remix",
    "Only a Base-specific SDK called BaseForge"], 1)

QA("The GasPriceOracle method 'baseFeeScalar()' returns:",
   ["The L2 base fee scalar for computing execution costs",
    "The scalar used to calculate L1 fee based on the Ethereum base fee",
    "The minimum priority fee scalar for Flashblock inclusion",
    "The withdrawal fee scalar for L1 settlement"], 1)

QA("Which standard Optimism predeploy is available on Base?",
   ["L2StandardBridge (for L1<->L2 token bridging)",
    "Uniswap V3 Factory",
    "OpenZeppelin Proxy Admin",
    "Chainlink VRF Coordinator"], 0)

QA("When deploying a smart contract to Base using Foundry, what must be configured?",
   ["The RPC endpoint for Base mainnet and the chain ID (8453)",
    "A special Base-specific compiler flag",
    "A Coinbase API key for deployment authorization",
    "A Foundry plugin that rewrites Solidity for Base"], 0)

QA("All of the following are standard Optimism predeploys available on Base EXCEPT:",
   ["GasPriceOracle", "L1Block", "L2StandardBridge", "UniswapV3Factory"], 3)

QA("The GasPriceOracle method 'l1BaseFee()' on Base returns:",
   ["The L2 execution base fee in wei",
    "The current Ethereum L1 base fee as seen by the L2",
    "The minimum priority fee for Flashblock inclusion",
    "The total fee for the most recent Base block"], 1)

QA("What does EVM equivalence on Base mean for smart contract bytecode?",
   ["Bytecode compiled for Ethereum will not run on Base without recompilation",
    "Smart contract bytecode behaves identically on both Ethereum and Base",
    "Base uses a different bytecode format translated at runtime",
    "Only certain Solidity versions produce compatible bytecode"], 1)

QA("The GasPriceOracle predeploy contract lives at which address range?",
   ["The standard Ethereum precompile address range (0x01-0x09)",
    "The OP Stack predeploy address range starting with 0x4200...",
    "A random address chosen at contract deployment",
    "The zero address 0x0000...0000"], 1)

QA("Which method on the GasPriceOracle provides a quick L1 fee estimate without a fully encoded tx?",
   ["getL1Fee(bytes)", "getL1FeeUpperBound(uint256)", "l1BaseFee()", "blobBaseFee()"], 1)

QA("A developer using Hardhat to deploy on Base needs to modify which configuration?",
   ["hardhat.config.js to add Base as a network with Chain ID 8453",
    "The Solidity compiler to output Base-compatible bytecode",
    "The contract source code to be Base-specific",
    "The deployment script to use a Base-only SDK"], 0)

QA("The GasPriceOracle method 'blobBaseFee()' on Base returns:",
   ["The L2 blob base fee for EIP-4844 transactions",
    "The current blob base fee on Ethereum L1 as seen by the L2",
    "The minimum fee for blob-carrying transactions on Base",
    "The total blob storage cost for the current block"], 1)

QA("All of the following are predeployed contracts on Base EXCEPT:",
   ["GasPriceOracle at 0x420000000000000000000000000000000000000F",
    "L1Block at a standard OP Stack predeploy address",
    "L2StandardBridge at a standard OP Stack predeploy address",
    "Uniswap V2 Router at a standard predeploy address"], 3)

QA("When deploying a Solidity contract from Remix to Base, what must be selected?",
   ["The Injected Web3 provider with MetaMask pointed at Base mainnet",
    "The Base-specific compiler version",
    "The Vyper language option",
    "The IPFS deployment method"], 0)

QA("The L2StandardBridge predeploy on Base facilitates:",
   ["Swapping tokens on decentralized exchanges",
    "Bridging standard ERC-20 tokens between L1 Ethereum and Base",
    "Deploying new smart contracts to Base",
    "Running the Fault Proof system for withdrawals"], 1)

QA("GasPriceOracle methods available on Base include all EXCEPT:",
   ["getL1Fee(bytes)", "l1BaseFee()", "blobBaseFee()", "getL2Fee()"], 3)

QA("Base's EVM equivalence means a contract compiled with solc for Ethereum will:",
   ["Fail to deploy on Base due to different address formatting",
    "Deploy and run identically on Base without any code changes",
    "Require recompilation with a Base-specific solc version",
    "Only work if it does not use any precompiled contracts"], 1)

QA("Which address format is used for smart contracts on Base?",
   ["The standard Ethereum 0x-prefixed 40-character hex address",
    "A bech32 format similar to Cosmos chains",
    "A base58 format similar to Bitcoin",
    "A 64-character hex format without the 0x prefix"], 0)

QA("B20 token deployment on Base enables what kind of functionality?",
   ["A new token standard for Base-native assets",
    "DeFi protocol interactions using B20 as an intermediate asset",
    "A native token for gas fee payments on Base",
    "A governance token for the Base protocol"], 1)

QA("The L1Block predeploy contract on Base provides information about:",
   ["The current block's timestamp and number on L2",
    "The current Ethereum L1 block number and base fee",
    "The total hash rate of the Ethereum network",
    "The latest NFT minting data"], 1)

QA("To get the exact L1 fee for a transaction on Base, which GasPriceOracle method should be called?",
   ["getL1Fee(bytes) with the fully RLP-encoded transaction bytes",
    "getL1FeeUpperBound(uint256) with an estimated gas budget",
    "l1BaseFee() with no arguments",
    "blobBaseFee() with the blob versioned hash"], 0)

QA("A developer deploying to Base with Foundry's 'forge create' command must specify:",
   ["The --rpc-url pointing to Base and --chain-id 8453",
    "The --base-mode flag to enable Flashblocks support",
    "The --compiler version to use Base-specific optimizations",
    "The --private-key of the Coinbase exchange"], 0)

# ============================================================
# TOPIC 4: FLASHBLOCKS API (~20 questions)
# ============================================================

QA("The Flashblocks API on Base includes custom endpoints beyond which standard?",
   ["The GraphQL API specification",
    "Standard Ethereum JSON-RPC",
    "The REST API specification from Coinbase",
    "The WebSocket protocol"], 1)

QA("The Debug API for node troubleshooting is part of which system?",
   ["The Flashblocks API suite",
    "The Ethereum L1 consensus layer",
    "The Coinbase internal monitoring system",
    "The Basescan block explorer"], 0)

QA("Which of the following is a custom Flashblocks API endpoint beyond standard JSON-RPC?",
   ["eth_sendRawTransaction",
    "eth_getBlockByNumber",
    "An endpoint for querying Flashblock-specific preconfirmation status",
    "net_version"], 2)

QA("The Flashblocks Debug API would be used by a developer to:",
   ["Deploy new smart contracts to Base",
    "Troubleshoot issues with Flashblock preconfirmations and node behavior",
    "Swap tokens on a decentralized exchange",
    "Bridge assets between Ethereum and Base"], 1)

QA("Flashblocks API custom endpoints enable what functionality?",
   ["Sub-second preconfirmation queries beyond basic JSON-RPC",
    "Direct Ethereum L1 mining from Base",
    "Native BASE token staking through the API",
    "Automated smart contract deployment"], 0)

QA("Accessing Flashblock-specific information requires:",
   ["Only standard JSON-RPC methods like eth_getBlockByNumber",
    "The custom Flashblocks API endpoints beyond standard JSON-RPC",
    "The Coinbase Pro trading API",
    "The Base Discord bot"], 1)

QA("The Debug API available through the Flashblocks API helps diagnose:",
   ["Gas price estimation errors on Ethereum L1",
    "Node-level issues with Flashblock construction and broadcast",
    "Smart contract security vulnerabilities",
    "Token price volatility on exchanges"], 1)

QA("A developer building a dApp that relies on Flashblock preconfirmations would use:",
   ["The Flashblocks API custom endpoints for sub-second feedback",
    "Only the eth_getTransactionReceipt method",
    "The Coinbase exchange order book API",
    "The Ethereum beacon chain API"], 0)

QA("Which best describes the Flashblocks API's relationship to JSON-RPC?",
   ["It replaces JSON-RPC entirely with a faster protocol",
    "It extends JSON-RPC with custom endpoints for Flashblock-specific data",
    "It is incompatible with JSON-RPC and uses a different transport layer",
    "It is only available on testnet, not on mainnet"], 1)

QA("A node operator using the Debug API on Base can monitor:",
   ["Real-time cryptocurrency prices",
    "Flashblock construction, broadcast timing, and potential issues",
    "User wallet balances across all chains",
    "Daily active user metrics for dApps"], 1)

QA("The custom endpoints in the Flashblocks API are most relevant for:",
   ["Querying historical transaction data from genesis",
    "Getting near-instant feedback on transaction preconfirmation status",
    "Calculating long-term average gas prices",
    "Submitting batch transactions for DeFi strategies"], 1)

QA("When troubleshooting a node not broadcasting Flashblocks correctly, which tool helps?",
   ["The Flashblocks Debug API for node diagnostics",
    "The Basescan API for block exploration",
    "The Coinbase exchange API for market data",
    "The Ethereum JSON-RPC API for L1 queries"], 0)

QA("Which statement about the Flashblocks API is correct?",
   ["It only provides historical data with no real-time capabilities",
    "It includes custom endpoints beyond standard JSON-RPC and a Debug API",
    "It is a paid, subscription-only service from Coinbase",
    "It is deprecated and replaced by the standard Ethereum API"], 1)

QA("The Flashblocks API custom endpoints provide information about:",
   ["Flashblock ordering, gas budgets, and preconfirmation details",
    "Ethereum L1 validator balances",
    "Coinbase exchange order books",
    "Cross-chain bridge liquidity"], 0)

QA("All of the following are accessible via Flashblocks API EXCEPT:",
   ["Custom endpoints for preconfirmation data",
    "Debug API for node troubleshooting",
    "Real-time Flashblock auction status",
    "Ethereum L1 miner reward calculation"], 3)

QA("The Debug API component of the Flashblocks API is primarily used for:",
   ["Writing and deploying new smart contracts",
    "Diagnosing and troubleshooting node-level operational issues",
    "Querying historical transaction data",
    "Trading tokens on decentralized exchanges"], 1)

# ============================================================
# TOPIC 5: COMPARISON (~42 questions)
# ============================================================

QA("Base vs Ethereum L1: Which statement is correct about their relationship?",
   ["Base and Ethereum L1 are competing L1 blockchains",
    "Base is an L2 that uses Ethereum for security and settlement",
    "Base replaces Ethereum entirely for all users",
    "Base is a fork of Ethereum with an independent validator set"], 1)

QA("Base vs Ethereum L1: How do transaction fees compare?",
   ["Base transactions are more expensive than Ethereum L1",
    "Base transactions are significantly cheaper due to L2 efficiency and batching",
    "Both have identical fee structures and costs",
    "Ethereum L1 is free; Base has fees"], 1)

QA("Base vs Ethereum L1: How does block time compare?",
   ["Base at 2 seconds is faster than Ethereum L1 at ~12 seconds",
    "Both have the same 12-second block time",
    "Ethereum L1 at 2 seconds is faster than Base at 12 seconds",
    "Base blocks are produced every 200ms, matching Flashblocks"], 0)

QA("Base vs Ethereum L1: A key limitation of Base compared to Ethereum L1 is:",
   ["Base has a 7-day withdrawal delay for L1 withdrawals due to fault proofs",
    "Base cannot process token transfers",
    "Base does not support smart contracts",
    "Base requires a different programming language than Ethereum"], 0)

QA("Base vs other L2s: What makes Flashblocks unique to Base among OP Stack chains?",
   ["Flashblocks are a standard feature on all OP Stack chains",
    "Flashblocks (200ms preconfirmations) are a Base-specific enhancement to the OP Stack",
    "Flashblocks are available on Optimism but not on Base",
    "Flashblocks are a testnet-only feature on all L2s"], 1)

QA("Base vs Solana: Which statement about EVM compatibility is correct?",
   ["Both Base and Solana are EVM-equivalent",
    "Base is EVM-equivalent; Solana is NOT EVM-compatible",
    "Solana is EVM-equivalent; Base is NOT EVM-compatible",
    "Neither Base nor Solana supports the EVM"], 1)

QA("Base vs Solana: How does the development experience differ?",
   ["Both use Solidity for smart contract development",
    "Base uses Solidity/Vyper (EVM); Solana uses Rust/C (non-EVM)",
    "Base uses Rust; Solana uses Solidity",
    "Both use the same programming languages"], 1)

QA("Base is part of which broader ecosystem of OP Stack chains?",
   ["The Ethereum Superchain ecosystem of OP Stack L2s",
    "The Cosmos Interchain ecosystem",
    "The Polkadot parachain ecosystem",
    "The Avalanche subnet ecosystem"], 0)

QA("Base vs other L2s: What infrastructure does Base share with Optimism?",
   ["The same sequencer infrastructure and operators",
    "Standard bridge contracts and the OP Stack framework",
    "The same native token (OP) for governance",
    "The same RPC endpoints and chain ID"], 1)

QA("How does Base's security model compare to Ethereum L1's?",
   ["Base has stronger security than Ethereum L1 due to additional validation layers",
    "Base inherits Ethereum L1 security through data posting and fault proofs",
    "Base has completely independent security with its own validator set",
    "Base has no security model"], 1)

QA("Which is a correct comparison between Base and Solana?",
   ["Both are EVM-equivalent Layer 2 solutions",
    "Base is an EVM-equivalent L2 on Ethereum; Solana is a non-EVM L1 with its own runtime",
    "Solana is an L2 on Ethereum; Base is an L1",
    "Both are built on the OP Stack framework"], 1)

QA("A key advantage of Base over Ethereum L1 for dApp deployment is:",
   ["Developers must rewrite contracts in a new language",
    "No changes needed — EVM equivalence means same code, same tools, but lower fees",
    "Base offers higher security than Ethereum L1",
    "Base has no gas limits unlike Ethereum L1"], 1)

QA("Base vs Solana: Which has lower transaction fees typically?",
   ["Solana typically has sub-cent fees; Base fees vary but are low for L2 standards",
    "Base is always free to use",
    "Solana fees are significantly higher than Base fees",
    "Both have identical fee structures"], 0)

QA("As part of the Superchain, Base benefits from:",
   ["A shared sequencer with all other Superchain L2s",
    "Shared research, infrastructure, and security improvements across OP Stack chains",
    "A shared native token used by all Superchain members",
    "Shared validator set with Ethereum L1"], 1)

QA("Base vs other L2s: How does Base's block gas limit of 400M compare?",
   ["It is smaller than most other L2s' gas limits",
    "It is larger than Ethereum L1's 30M and competitive with other L2s",
    "It is the same as Ethereum L1's block gas limit",
    "It is unlimited — there is no block gas limit on Base"], 1)

QA("Base vs Solana: What is true about their settlement chains?",
   ["Both settle to Ethereum L1 for finality",
    "Base settles to Ethereum L1; Solana is an L1 that settles its own transactions",
    "Solana settles to Ethereum L1; Base settles itself",
    "Both settle to a shared settlement layer"], 1)

QA("Which is NOT a valid comparison between Base and Ethereum L1?",
   ["Base has 2-second blocks; Ethereum L1 has ~12-second blocks",
    "Base uses the OP Stack; Ethereum L1 uses its own consensus mechanism",
    "Base has a 7-day withdrawal delay; Ethereum L1 has no such delay for native transfers",
    "Base charges in BASE tokens for gas; Ethereum L1 charges in ETH"], 3)

QA("Base vs other L2s: What is the Superchain vision?",
   ["A single L2 that replaces all other L2s",
    "A network of interconnected OP Stack L2s sharing security and communication layers",
    "A Layer 3 built on top of all existing L2s",
    "A cross-chain DEX aggregator"], 1)

QA("Base vs Solana: How does the account model differ?",
   ["Base uses the Ethereum account model (EOAs + contracts); Solana uses a different model",
    "Both use the Ethereum account model",
    "Both use the Solana account model",
    "Base uses the Solana account model; Solana uses the Ethereum model"], 0)

QA("A developer choosing between Base and Solana considers what key tradeoff?",
   ["Base offers EVM compatibility with Ethereum tools; Solana offers higher throughput with Rust",
    "Base has no DeFi ecosystem; Solana has all DeFi protocols",
    "Solana requires no learning curve; Base requires learning Rust",
    "Base and Solana are identical in all aspects"], 0)

QA("How does Base's fee model differ from Ethereum L1's?",
   ["Base has an L2 execution fee plus an L1 security fee; Ethereum L1 has only execution fees",
    "Both have identical fee structures",
    "Ethereum L1 has L2 fees; Base has only L1 fees",
    "Base has no fees at all"], 0)

QA("Which statement about Base vs other OP Stack chains is FALSE?",
   ["Base uses the same OP Stack framework as Optimism",
    "All OP Stack chains have identical block times and gas limits",
    "Flashblocks are a Base-specific feature not standard on all OP Stack chains",
    "Base inherits Optimism's standard bridge contracts"], 1)

QA("Base vs Ethereum L1: What advantage does Base offer for high-frequency trading dApps?",
   ["Slower blocks but stronger finality guarantees",
    "Faster blocks (2s) and Flashblocks (200ms preconfirmations) with lower fees",
    "Identical performance to Ethereum L1",
    "Lower security but higher throughput than any other option"], 1)

QA("As part of the Superchain, Base can interoperate with other ecosystem chains through:",
   ["A shared liquidity pool across all Superchain L2s",
    "Standardized cross-chain messaging and bridge infrastructure",
    "A single global sequencer processing all Superchain transactions",
    "A unified token standard that replaces all ERC-20 tokens"], 1)

QA("Base vs Ethereum L1: Which chain has higher throughput for simple token transfers?",
   ["Ethereum L1 — it processes more transactions per second",
    "Base — its larger block gas limit and faster block time provide higher throughput",
    "Both have identical throughput",
    "Neither can process token transfers"], 1)

QA("Base vs Solana: Which ecosystem would a developer choose for EVM tool compatibility?",
   ["Solana — it has broader EVM tool support",
    "Base — as an EVM-equivalent L2, it supports all standard Ethereum developer tools",
    "Neither supports Ethereum developer tools",
    "Both support Hardhat, Foundry, and Remix equally"], 1)

QA("Base vs other L2s: One difference between Base and Optimism mainnet is:",
   ["Optimism has Flashblocks; Base uses standard 2-second blocks",
    "Base has Flashblocks; Flashblocks is a Base-specific enhancement not standard on all OP Stack chains",
    "Optimism has a higher block gas limit than Base",
    "Both have identical feature sets with no differences"], 1)

QA("Base vs Ethereum L1: A user withdrawing from Base to Ethereum must wait 7 days, but:",
   ["This same restriction applies to all Ethereum L1 native transfers",
    "Ethereum L1 has no such withdrawal delay for native value transfers",
    "Waiting 7 days is optional and can be bypassed with extra fees",
    "Ethereum L1 has a 14-day withdrawal period for all transfers"], 1)

# ============================================================
# TOPIC 6: MISC (~42 questions)
# ============================================================

QA("Which website is the official portal for Base ecosystem information?",
   ["base.org", "base.xyz", "coinbase.com/base", "optimism.io/base"], 0)

QA("Where can developers find the Base community for support and discussion?",
   ["Base Discord server",
    "Only through email support",
    "The Coinbase subreddit only",
    "There is no community channel for Base"], 0)

QA("Base's open-source code is hosted on which platform?",
   ["GitLab", "GitHub", "Bitbucket", "SourceForge"], 1)

QA("What information does the Base Dashboard provide to the community?",
   ["Personalized trading recommendations",
    "Chain metrics, network activity, and ecosystem data",
    "Coinbase stock price and financial reports",
    "Weather forecasts and news updates"], 1)

QA("The Configuration Changelog on Base documents what type of changes?",
   ["Changes to the base.org website design",
    "Parameter changes and protocol configuration updates over time",
    "Changes to the Coinbase exchange fee schedule",
    "Daily transaction volume statistics"], 1)

QA("The Troubleshooting Transactions guide on Base helps users with:",
   ["Debugging failed or stuck transactions on the Base network",
    "Troubleshooting their internet connection",
    "Resolving Coinbase account issues",
    "Fixing hardware wallet connectivity problems"], 0)

QA("Base's official website (base.org) provides all of the following EXCEPT:",
   ["Documentation for developers",
    "Links to the Base GitHub repository",
    "A cryptocurrency exchange for buying BASE tokens",
    "Information about the Base ecosystem and builders"], 2)

QA("The Base Dashboard includes real-time data on which of the following?",
   ["Total Value Locked (TVL) and daily transaction counts",
    "Personal portfolio performance across all chains",
    "Coinbase account balances and transaction history",
    "Bitcoin mining difficulty and hash rate"], 0)

QA("Where can users find the official Base Discord community link?",
   ["On the official Base website (base.org)",
    "Through a Coinbase email newsletter",
    "On the Ethereum Foundation website",
    "There is no official Base Discord server"], 0)

QA("The Base Configuration Changelog is useful for:",
   ["Tracking network parameter changes such as gas limits or fee configurations",
    "Viewing changes to the base.org website layout",
    "Monitoring Coinbase exchange listing announcements",
    "Reviewing Base community proposal results"], 0)

QA("A developer looking for the Base GitHub repository would find:",
   ["Base's open-source code including documentation and node software",
    "Only the Base marketing materials",
    "The Coinbase exchange trading algorithm source code",
    "Only archived and deprecated Base projects"], 0)

QA("The Troubleshooting Transactions guide on Base covers which scenario?",
   ["What to do when a transaction is stuck in pending status",
    "How to recover lost BASE tokens from a scam",
    "How to dispute Coinbase credit card charges",
    "How to mine BASE tokens on a home computer"], 0)

QA("The Base Dashboard can be accessed from which URL domain?",
   ["dashboard.base.org",
    "coinbase.com/dashboard",
    "basescan.org",
    "superchain.eco"], 0)

QA("All of the following are official Base resources EXCEPT:",
   ["Base.org website", "Base Discord community", "Base GitHub organization", "Base Telegram trading bot"], 3)

QA("The Configuration Changelog on Base helps users understand:",
   ["When and why protocol parameters like gas targets were modified",
    "Which developers contributed code to the Base repository",
    "The latest NFT drops on the Base network",
    "The current price of ETH in USD"], 0)

QA("Which of the following is NOT a resource available on base.org?",
   ["Developer documentation and guides",
    "Links to the Base GitHub for open-source code",
    "A built-in cryptocurrency wallet",
    "Ecosystem information about builders and applications"], 2)

QA("The Base Dashboard provides metrics primarily for:",
   ["Monitoring Base network health and activity statistics",
    "Executing trades on decentralized exchanges",
    "Managing personal cryptocurrency portfolios",
    "Deploying smart contracts to Base"], 0)

QA("Developers can find Base's smart contract examples on:",
   ["The Base GitHub organization and developer documentation",
    "The Coinbase Pro API documentation only",
    "The Ethereum Foundation website only",
    "The Solana developer portal"], 0)

QA("Which of the following is NOT part of Base's off-chain community resources?",
   ["Base Discord for developer discussions",
    "Base GitHub for code contributions",
    "A native BASE token staking dashboard with rewards calculator",
    "Base.org for documentation and ecosystem information"], 2)

QA("The Troubleshooting Transactions guide is likely to recommend for a stuck transaction:",
   ["Increasing the priority fee by sending a replacement transaction with a higher gas price",
    "Contacting Coinbase customer support",
    "Deleting and reinstalling your wallet",
    "Waiting indefinitely with no action possible"], 0)

QA("Base's official GitHub organization contains what type of repositories?",
   ["Node software, protocol specifications, and developer tools",
    "Only marketing and documentation repositories",
    "Coinbase exchange trading algorithms",
    "Personal cryptocurrency wallets for end users"], 0)

QA("The Base community primarily communicates through which channel?",
   ["The official Base Discord server",
    "A private email mailing list",
    "The Coinbase phone support line",
    "A Reddit forum with no official affiliation"], 0)

QA("Which of the following about the Base Dashboard is FALSE?",
   ["It displays Total Value Locked (TVL) on Base",
    "It shows daily transaction counts and active addresses",
    "It allows users to execute trades directly on Base",
    "It provides visibility into Base network health"], 2)

QA("Base's documentation on base.org is aimed at which audience?",
   ["Developers building on Base and users learning about the network",
    "Only Coinbase internal employees",
    "Only institutional investors",
    "Only academic researchers"], 0)

QA("The Base Configuration Changelog ensures:",
   ["Transparency about network parameter changes over time",
    "A record of all Coinbase employee salaries",
    "A log of every dApp deployed on Base",
    "A changelog of the base.org website design"], 0)

QA("Basescan is an example of what type of tool for Base?",
   ["A block explorer for viewing onchain data on Base mainnet",
    "A wallet application for storing BASE tokens",
    "A development framework for deploying contracts",
    "A node monitoring tool for Base operators"], 0)

QA("Which statement about base.org is correct?",
   ["It is the official website for Base ecosystem information and developer docs",
    "It is a third-party community site not affiliated with Base",
    "It only provides a link to download the Coinbase app",
    "It is the official Ethereum L1 documentation portal"], 0)

QA("The Troubleshooting Transactions guide on Base helps with:",
   ["Understanding why a transaction was dropped or failed to be included",
    "Setting up a Base validator node from scratch",
    "Deploying a cross-chain bridge on Base",
    "Writing smart contract code in Solidity"], 0)

QA("The Base Discord server serves what primary purpose?",
   ["Community discussion, developer support, and ecosystem announcements",
    "Only memes and non-technical chat",
    "Coinbase customer support ticket filing",
    "Automated trading signal distribution"], 0)

QA("Configuration changelogs on Base document parameter changes such as:",
   ["Gas limits, fee parameters, and other protocol-level configuration values",
    "The daily menu at the Coinbase cafeteria",
    "Personal wallet transaction histories",
    "Smart contract source code diffs"], 0)

QA("The Base Dashboard is useful for:",
   ["Tracking real-time network metrics without running a full node",
    "Executing high-frequency trades on Base DEXes",
    "Deploying new smart contracts through a web interface",
    "Managing Coinbase exchange account settings"], 0)

QA("On base.org, developers can find all of the following EXCEPT:",
   ["Smart contract deployment guides",
    "RPC endpoint connection details",
    "A live chat support agent for debugging code",
    "Information about the Base ecosystem and tools"], 2)

QA("Which of the following is a Base ecosystem resource?",
   ["The Base Dashboard for chain metrics",
    "A native BASE token faucet for mainnet users",
    "A centralized exchange operated by the Base Foundation",
    "A Base-branded hardware wallet"], 0)

QA("The Base GitHub organization is important for:",
   ["Contributing to and reviewing open-source Base software",
    "Buying and selling BASE tokens",
    "Staking tokens to earn rewards",
    "Creating Base Discord accounts"], 0)

# ============================================================
# SHUFFLE AND OUTPUT
# ============================================================

random.shuffle(questions)

# Reassign sequential IDs
for i, q in enumerate(questions):
    q["id"] = i

# Build the output
output = {
    "meta": {
        "ecosystem": "Base",
        "batchId": "base-2026-07-11-batch4",
        "generatedAt": "2026-07-11T07:15:00Z",
        "totalQuizzes": len(questions),
        "questionsPerSession": 5
    },
    "quizzes": questions
}

print(f"Total questions generated: {len(questions)}")

# Verify correctIndex distribution
ci_dist = Counter(q["correctIndex"] for q in questions)
print(f"correctIndex distribution: {dict(sorted(ci_dist.items()))}")

# Check for duplicates by question text
texts = [q["question"] for q in questions]
dupes = [t for t in texts if texts.count(t) > 1]
if dupes:
    print(f"WARNING: Found {len(dupes)} duplicate questions!")
    for d in set(dupes):
        print(f"  - {d}")
else:
    print("No duplicate questions found.")

# Check all questions have 4 options
bad_opts = [q for q in questions if len(q["options"]) != 4]
if bad_opts:
    print(f"WARNING: {len(bad_opts)} questions don't have 4 options!")
    for q in bad_opts:
        print(f"  ID {q['id']}: {len(q['options'])} options")
else:
    print("All questions have exactly 4 options.")

# Check correctIndex is valid
bad_ci = [q for q in questions if q["correctIndex"] not in [0, 1, 2, 3]]
if bad_ci:
    print(f"WARNING: {len(bad_ci)} questions have invalid correctIndex!")
else:
    print("All correctIndex values are valid (0-3).")

output_path = "/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch4.json"
with open(output_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"Written to {output_path}")
