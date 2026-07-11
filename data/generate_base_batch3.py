#!/usr/bin/env python3
"""Generate ~250 Base quiz questions (batch3) about Accounts, Agents, Apps, B20, x402, Security, Ledgers."""

import json
import random
from collections import Counter
from datetime import datetime, timezone

random.seed(42)

questions = []

def q(question, options, correctIndex):
    questions.append({
        "question": question,
        "options": options,
        "correctIndex": correctIndex
    })

# ======================================================================
# TOPIC 1: BASE ACCOUNTS (~35 questions)
# ======================================================================

# --- Base Accounts as smart accounts / account abstraction ---
q("What are Base Accounts?",
  ["Traditional externally owned wallets",
   "Smart accounts using account abstraction",
   "Hardware wallet addresses",
   "Multi-signature vaults only"], 1)

q("Base Accounts are best described as:",
  ["Smart contract wallets that work across chains",
   "Centralized exchange deposit addresses",
   "Read-only blockchain explorers",
   "Offline cold storage solutions"], 0)

q("What technology powers Base Accounts?",
  ["Merkle tree proofs",
   "Account abstraction (smart contract wallets)",
   "Sharded state channels",
   "Threshold signatures only"], 1)

q("Base Accounts use account abstraction to provide:",
  ["Higher block rewards for miners",
   "Smart wallets for onchain interactions",
   "Faster block propagation",
   "Lower gas costs for validators"], 1)

q("Which of the following is true about Base Accounts?",
  ["They are traditional EOA wallets",
   "They are smart contract wallets that enable account abstraction",
   "They can only be used on testnet",
   "They require a monthly subscription"], 1)

q("What is the main benefit of Base Accounts being smart wallets?",
  ["Higher transaction throughput",
   "Easier onboarding and onchain interactions",
   "Lower energy consumption",
   "Increased block rewards"], 1)

q("Base Accounts can be integrated into apps for what purpose?",
  ["Running validator nodes",
   "Payments and onchain interactions",
   "Mining cryptocurrency",
   "Hosting static websites"], 1)

q("How do Base Accounts improve user onboarding?",
  ["By eliminating gas fees entirely",
   "Through account abstraction that simplifies wallet setup and use",
   "By requiring KYC verification",
   "By using a centralized login system"], 1)

q("Which statement about Base Accounts is FALSE?",
  ["They are smart contract wallets",
   "They use account abstraction technology",
   "They are traditional externally owned accounts (EOAs)",
   "They can work across chains"], 2)

q("Base Accounts are designed primarily as:",
  ["Mining pool accounts",
   "Smart wallets for onchain interactions",
   "Validator staking contracts",
   "Governance voting proxies"], 1)

q("Which of the following is NOT a feature of Base Accounts?",
  ["Smart contract wallet functionality",
   "Account abstraction for onboarding",
   "Integrated Bitcoin mining",
   "Cross-chain compatibility"], 2)

q("What type of wallet does a Base Account represent?",
  ["A custodial wallet controlled by Coinbase",
   "A smart contract wallet using account abstraction",
   "A paper wallet for cold storage",
   "A hardware wallet requiring physical device"], 1)

q("Base Accounts enable developers to:",
  ["Create their own Layer-1 blockchain",
   "Integrate smart wallet functionality into apps for payments",
   "Mint their own native cryptocurrency",
   "Launch validator nodes on Base"], 1)

q("Compared to traditional EOAs, Base Accounts offer:",
  ["Faster transaction finality",
   "Smart wallet capabilities with account abstraction",
   "Lower staking requirements",
   "Higher block rewards"], 1)

q("Base Accounts are smart contract wallets that work:",
  ["Only on Ethereum mainnet",
   "Across multiple chains",
   "Only on Base testnet",
   "Only within a single dApp"], 1)

q("What makes Base Accounts different from regular crypto wallets?",
  ["They use Proof of Work for security",
   "They are smart contract wallets rather than simple EOAs",
   "They require monthly maintenance fees",
   "They can only receive, not send, transactions"], 1)

q("Account abstraction in Base Accounts helps with:",
  ["Higher gas limits",
   "Easier onboarding and more flexible wallet logic",
   "Faster block production",
   "Lower validator counts"], 1)

q("Which use case is specifically mentioned for integrating Base Accounts?",
  ["Running a mining pool",
   "Payments within apps",
   "Operating a domain name service",
   "Managing DNS records"], 1)

q("Base Accounts are an example of what blockchain innovation?",
  ["Sharding",
   "Account abstraction / smart wallets",
   "Zero-knowledge proofs for privacy",
   "DAG-based consensus"], 1)

q("What does account abstraction mean in the context of Base Accounts?",
  ["Accounts are abstracted away and users don't see them",
   "Smart wallets replace simple EOAs with programmable logic and better UX",
   "Accounts are stored in an abstract database off-chain",
   "Account balances are abstract estimates rather than exact"], 1)

q("Base Accounts function as:",
  ["Simple key-value stores",
   "Smart contract wallets with cross-chain capability",
   "Centralized exchange balances",
   "Off-chain payment channels"], 1)

q("Which of the following best describes Base Accounts' cross-chain capability?",
  ["They only work on Base mainnet",
   "They are smart wallets designed to work across chains",
   "They bridge assets automatically without user input",
   "They rely on a centralized relayer network"], 1)

q("How can developers use Base Accounts in their applications?",
  ["By replacing the blockchain entirely",
   "By integrating them for payments and onchain interactions",
   "By using them as database storage",
   "By running them as backend servers"], 1)

q("Which is NOT a characteristic of Base Accounts?",
  ["Smart contract wallet architecture",
   "Account abstraction technology",
   "Proof-of-Work mining capability",
   "Cross-chain operation"], 2)

q("Base Accounts provide smart wallets for:",
  ["Off-chain data storage",
   "Onchain interactions",
   "Hardware device management",
   "Network routing"], 1)

q("What role does account abstraction play in Base Accounts?",
  ["It makes accounts invisible to users",
   "It enables easier onboarding and flexible wallet logic",
   "It restricts accounts to read-only mode",
   "It converts all wallets to multisig"], 1)

q("Base Accounts can be described as:",
  ["Centralized user databases",
   "Smart contract wallets for onchain interactions",
   "Block explorer interfaces",
   "Validator management consoles"], 1)

q("The smart wallet nature of Base Accounts means they:",
  ["Can only send, not receive",
   "Support programmable logic for custom transaction rules",
   "Require a bank account to operate",
   "Are limited to testnet use"], 1)

q("Which statement about integrating Base Accounts into apps is true?",
  ["It requires forking the Base blockchain",
   "It enables payment functionality within the app",
   "It converts the app into a blockchain node",
   "It only works with ERC-721 tokens"], 1)

q("Base Accounts enable onchain interactions via:",
  ["Physical hardware tokens",
   "Smart contract wallets with account abstraction",
   "Centralized API gateways",
   "Email-based transaction signing"], 1)

# ======================================================================
# TOPIC 2: BASE AGENTS (~35 questions)
# ======================================================================

q("What are Base Agents?",
  ["Automated trading bots",
   "AI agents that can transact autonomously onchain",
   "Centralized order matching engines",
   "Smart contract auditing tools"], 1)

q("Base Agents are best described as:",
  ["AI agents capable of autonomous onchain transactions",
   "Manual trading interfaces",
   "Block explorer plugins",
   "Validator monitoring dashboards"], 0)

q("What enables Base Agents to transact?",
  ["Manual user approval for every step",
   "Autonomous onchain transaction capabilities",
   "A centralized exchange API key",
   "Off-chain database queries"], 1)

q("What is the Base MCP Server?",
  ["A mining control protocol server",
   "AI tooling for agent-based development on Base",
   "A message compression protocol",
   "A middleware layer for database indexing"], 1)

q("Base MCP Server provides:",
  ["Validator staking interfaces",
   "AI tooling for building agent-based applications",
   "Network monitoring dashboards",
   "Cross-chain bridge infrastructure"], 1)

q("What does MCP stand for in Base MCP Server?",
  ["Mining Control Protocol",
   "Model Context Protocol",
   "Message Compression Protocol",
   "Multi-Chain Protocol"], 1)

q("Base Agents can autonomously perform which action?",
  ["Mining new blocks",
   "Swapping tokens via agent interactions",
   "Running validator infrastructure",
   "Processing fiat withdrawals"], 1)

q("What payment mechanism is supported with Base Agents?",
  ["Credit card payments only",
   "x402 payments (HTTP 402 Payment Required)",
   "ACH bank transfers",
   "PayPal integration"], 1)

q("Base Agents can make and receive:",
  ["Email notifications",
   "Payments autonomously",
   "Text messages",
   "Governance votes only"], 1)

q("Which resources are available for AI agent development on Base?",
  ["Only a single API endpoint",
   "MCP server, static docs files, and a prompt library",
   "A proprietary AI model trained on Solidity",
   "A natural language to bytecode compiler"], 1)

q("What does x402 enable for Base Agents?",
  ["Free unlimited API access",
   "Pay-per-request API access using crypto",
   "Bulk discounted rate plans",
   "Monthly subscription billing"], 1)

q("Which of the following is a resource for Base AI agent development?",
  ["Mobile SDK for iOS",
   "Static docs files",
   "Unity game engine plugin",
   "Java enterprise library"], 1)

q("Base Agents represent a fusion of:",
  ["Blockchain and artificial intelligence",
   "Traditional banking and DeFi",
   "Gaming and NFTs",
   "Supply chain and IoT"], 0)

q("Through Base Agents, token swaps happen via:",
  ["Centralized exchange order books",
   "Agent-to-agent interactions",
   "Manual peer-to-peer negotiation",
   "Off-chain settlement networks"], 1)

q("What type of payments can Base Agents process autonomously?",
  ["Only ERC-20 transfers",
   "Both making and receiving payments",
   "Only fiat currency payments",
   "Only governance proposal fees"], 1)

q("The Base MCP Server is designed for:",
  ["Block production optimization",
   "Agent-based development and AI tooling",
   "Liquidity pool management",
   "Cross-chain message passing"], 1)

q("Which statement about Base Agents is FALSE?",
  ["They are AI agents that can transact autonomously",
   "They can make and receive payments",
   "They require manual human approval for every transaction",
   "They can swap tokens via agent interactions"], 2)

q("What is the relationship between x402 and Base Agents?",
  ["x402 is a token standard unrelated to agents",
   "x402 payments are supported with Base Agents for pay-per-request access",
   "x402 replaces the need for agents entirely",
   "x402 is a wallet type for storing agent funds"], 1)

q("Base Agents can autonomously:",
  ["Stake ETH on Ethereum",
   "Transact, swap tokens, and make/receive payments",
   "Modify the Base protocol parameters",
   "Deploy new Layer-2 rollups"], 1)

q("Which of the following is NOT a resource available for Base AI agent development?",
  ["MCP server",
   "Static docs files",
   "Proprietary trading algorithms",
   "Prompt library"], 2)

q("The Base MCP Server provides AI tooling for:",
  ["Hardware wallet integration",
   "Agent-based development",
   "Mining pool coordination",
   "DNS record management"], 1)

q("How do Base Agents handle payments?",
  ["Through a centralized payment processor",
   "Autonomously, without manual human intervention",
   "Via bank wire transfers only",
   "Through quarterly settlement cycles"], 1)

q("What model does x402 enable for API access?",
  ["Unlimited flat-rate access",
   "Pay-per-request using crypto",
   "Free tier with ads",
   "Barter system with tokens"], 1)

q("Base Agents are:",
  ["Centralized server bots",
   "AI agents that can transact autonomously on Base",
   "Simple smart contract functions",
   "Off-chain data processors"], 1)

q("The prompt library for Base AI development contains:",
  ["Legal documents",
   "Prompts for AI agent development on Base",
   "Validator configuration files",
   "Token sale terms"], 1)

q("Static docs files are available for AI developers on Base as:",
  ["Downloadable reference documentation",
   "Interactive video tutorials",
   "Live coding workshops",
   "Printed manuals"], 0)

q("Which HTTP status code is associated with x402 payments?",
  ["HTTP 200 OK",
   "HTTP 402 Payment Required",
   "HTTP 404 Not Found",
   "HTTP 500 Internal Server Error"], 1)

q("What makes Base Agents autonomous?",
  ["They can transact onchain without manual human intervention for each step",
   "They run on a separate blockchain",
   "They are owned by autonomous organizations",
   "They use renewable energy sources"], 0)

q("Base Agents can swap tokens via:",
  ["A centralized exchange API",
   "Agent-to-agent interactions onchain",
   "Off-chain over-the-counter deals",
   "Manual atomic swaps only"], 1)

q("The x402 payment model with Base Agents is described as:",
  ["Subscription-based access",
   "Pay-as-you-go for APIs",
   "Freemium with premium tiers",
   "Ad-supported free usage"], 1)

# ======================================================================
# TOPIC 3: BASE APPS (~35 questions)
# ======================================================================

q("Which Quickstart guides are available for Base?",
  ["Build an app on Base and Deploy on Base",
   "Mine Bitcoin on Base and Stake ETH",
   "Run a validator and create a token",
   "Launch a DEX and build a lending protocol"], 0)

q("Base provides notifications to:",
  ["Replace email entirely",
   "Add notifications to apps built on Base",
   "Send SMS marketing messages",
   "Broadcast block rewards"], 1)

q("Developers building on Base can accept:",
  ["Only ETH payments",
   "B20 token payments in their apps",
   "Only credit card payments",
   "Only fiat currency"], 1)

q("What guide is available for existing applications on Base?",
  ["Migrate from Web2 to Web3 guide",
   "Migrate to Standard Web App guide",
   "Migrate to Mobile App guide",
   "Migrate to Desktop App guide"], 1)

q("Builder Codes on Base are available for:",
  ["End users only",
   "App developers, wallet developers, and agent developers",
   "Only enterprise customers",
   "Only validator operators"], 1)

q("What rewards program exists for Base builders?",
  ["A token airdrop for all users",
   "A Rewards program for builders",
   "A mining rewards pool",
   "A staking yield program"], 1)

q("Base Apps can leverage which payment method?",
  ["B20 payments for accepting B20 tokens",
   "Only traditional bank transfers",
   "Only PayPal integration",
   "Only cash deposits"], 0)

q("The Quickstart to Build an app on Base helps developers:",
  ["Create their own Layer-1 blockchain",
   "Start building applications on Base",
   "Audit smart contracts automatically",
   "Launch a cryptocurrency exchange"], 1)

q("Base notifications allow app developers to:",
  ["Mine new blocks",
   "Add notification functionality to their Base apps",
   "Validate transactions",
   "Create new tokens"], 1)

q("Builder Codes on Base support which types of developers?",
  ["Only smart contract developers",
   "App developers, wallet developers, and agent developers",
   "Only frontend developers",
   "Only backend developers"], 1)

q("Which of the following is a Quickstart option on Base?",
  ["Build a Layer-1 blockchain",
   "Deploy on Base",
   "Create a cryptocurrency exchange",
   "Launch a hardware wallet"], 1)

q("What is the purpose of the Migrate to Standard Web App guide?",
  ["To help existing apps migrate to a standard web app architecture on Base",
   "To migrate from Ethereum to Solana",
   "To convert desktop apps to mobile",
   "To upgrade database schemas"], 0)

q("Base Rewards program is designed for:",
  ["All users who hold Base tokens",
   "Builders on the Base ecosystem",
   "Only institutional investors",
   "Only NFT collectors"], 1)

q("Base Apps can accept B20 payments, meaning:",
  ["Apps must use a centralized payment gateway",
   "Apps can integrate B20 token as a payment method",
   "Apps can only accept Ethereum payments",
   "Apps must convert all payments to fiat"], 1)

q("Which guide helps developers get started with Base applications?",
  ["Build an app on Base Quickstart",
   "Build a Mining Rig guide",
   "Deploy a Validator guide",
   "Launch a Token guide"], 0)

q("Base notifications enable apps to:",
  ["Notify users about onchain events and updates",
   "Mine blocks in the background",
   "Auto-trade user portfolios",
   "Modify blockchain parameters"], 0)

q("Builder Codes are designed for which of the following?",
  ["App developers, wallet developers, and agent developers",
   "Only institutional partners",
   "Only Coinbase employees",
   "Only security auditors"], 0)

q("Which statement about Base Apps is FALSE?",
  ["Developers can use the Build an app on Base Quickstart",
   "Apps can accept B20 payments",
   "Base provides a guide to migrate to Standard Web App",
   "Base apps cannot use notifications"], 3)

q("The Deploy on Base Quickstart helps developers:",
  ["Deploy their applications on the Base network",
   "Deploy a Bitcoin mining operation",
   "Deploy a cloud server",
   "Deploy a DNS system"], 0)

q("Base Builder Codes are part of what?",
  ["The Base rewards and developer support ecosystem",
   "The Base mining protocol",
   "The Base consensus mechanism",
   "The Base staking system"], 0)

q("Which type of developer can use Builder Codes?",
  ["Only smart contract engineers",
   "Wallet developers",
   "Only frontend designers",
   "Only database administrators"], 1)

q("What payment integration is specifically highlighted for Base Apps?",
  ["ACH transfers",
   "B20 token payments",
   "Wire transfers",
   "PayPal"], 1)

q("Base notifications feature allows apps to:",
  ["Send onchain alerts to users",
   "Create new blockchain networks",
   "Generate blocks automatically",
   "Modify consensus parameters"], 0)

q("The Rewards program on Base is tied to:",
  ["Token staking",
   "Building and contributing to the ecosystem",
   "Running validator nodes",
   "Mining blocks"], 1)

q("Base offers Quickstart guides for which two activities?",
  ["Build an app on Base and Deploy on Base",
   "Mine Bitcoin and stake Ether",
   "Create a token and launch a DEX",
   "Run a node and become a validator"], 0)

q("What is the Migrate to Standard Web App guide for?",
  ["Converting Web2 apps to blockchain dApps",
   "Helping existing apps transition to a standard web app model on Base",
   "Upgrading from HTTP to HTTPS",
   "Moving from cloud to on-premise hosting"], 1)

q("Which of these is NOT a focus area for Base Builder Codes?",
  ["App developers",
   "Wallet developers",
   "Mining pool operators",
   "Agent developers"], 2)

q("Base Apps can integrate payments using:",
  ["Only cryptocurrency, no fiat options mentioned",
   "B20 tokens as a payment method",
   "Only through third-party processors",
   "Only via credit cards"], 1)

q("Base provides a Rewards program for:",
  ["All token holders regardless of activity",
   "Builders contributing to the ecosystem",
   "Only large institutional investors",
   "Only Coinbase employees"], 1)

q("To start building on Base, developers should use:",
  ["The Build an app on Base Quickstart",
   "The Base Bitcoin mining tutorial",
   "The Base hardware wallet setup guide",
   "The Base staking dashboard"], 0)

q("Which of the following can Builder Codes be used by?",
  ["App developers, wallet developers, and agent developers",
   "Only enterprise accounts",
   "Only Coinbase One subscribers",
   "Only verified KYC users"], 0)

# ======================================================================
# TOPIC 4: B20 NATIVE TOKEN STANDARD (~40 questions)
# ======================================================================

q("B20 is a native token standard for which network?",
  ["Ethereum",
   "Base",
   "Solana",
   "Polygon"], 1)

q("B20 is part of which Base upgrade?",
  ["Beethoven upgrade",
   "Beryl upgrade",
   "Catalyst upgrade",
   "Denali upgrade"], 1)

q("What does the B20 standard enable for tokens?",
  ["Tokens to be treated as native assets (like ETH) rather than just ERC-20s",
   "Tokens to be mined like Bitcoin",
   "Tokens to be used only for governance",
   "Tokens to remain as off-chain receipts"], 0)

q("What does B20 simplify for developers?",
  ["Block production",
   "Token management",
   "Validator node setup",
   "Network monitoring"], 1)

q("How can B20 tokens be used on Base?",
  ["For gas, similar to how ETH works on Ethereum",
   "Only for staking",
   "Only for governance voting",
   "Only for NFT purchases"], 0)

q("What upgrade introduced the B20 standard?",
  ["The Beryl upgrade",
   "The Frontier upgrade",
   "The Genesis upgrade",
   "The Horizon upgrade"], 0)

q("B20 tokens differ from standard ERC-20 tokens because B20 tokens are:",
  ["Not compatible with Ethereum wallets",
   "Treated as native assets on Base, similar to how ETH works on Ethereum",
   "Only usable on testnet",
   "Non-transferable by design"], 1)

q("Which statement about B20 is correct?",
  ["B20 is a sidechain for token transfers",
   "B20 is a native token standard for Base that enables tokens to be treated as native assets",
   "B20 is a decentralized exchange on Base",
   "B20 is a wallet provider for Base"], 1)

q("B20 tokens can be accepted in apps as:",
  ["Governance votes only",
   "Payments within applications",
   "Only for NFT minting",
   "Only for gas fee refunds"], 1)

q("What makes B20 tokens native on Base?",
  ["They are pre-mined by the Base team",
   "They can be treated like ETH as a first-class asset, not just as ERC-20 tokens",
   "They have no smart contract behind them",
   "They are only available on testnet"], 1)

q("In what way are B20 tokens similar to ETH on Ethereum?",
  ["They can be mined through Proof of Work",
   "They can be used for gas on Base",
   "They have a fixed supply cap",
   "They are deflationary by design"], 1)

q("B20 simplifies token management for:",
  ["End users only",
   "Developers building on Base",
   "Only exchange operators",
   "Only regulatory compliance officers"], 1)

q("Which of the following is NOT true about B20?",
  ["It is part of the Beryl upgrade",
   "It is a native token standard for Base",
   "It enables tokens to be treated as native assets",
   "It is a Layer-2 scaling solution"], 3)

q("The B20 standard treats tokens as:",
  ["Second-class assets compared to the native coin",
   "Native assets like ETH rather than just ERC-20s",
   "Off-chain IOU receipts",
   "Non-transferable credits"], 1)

q("What use case does B20 enable for tokens in apps?",
  ["Gas fee payments and merchant acceptance",
   "Only governance voting",
   "Only NFT metadata storage",
   "Only oracle price feeds"], 0)

q("B20 is a token standard that makes tokens:",
  ["Mineable with specialized hardware",
   "First-class native assets on Base",
   "Non-transferable by default",
   "Only available to institutional investors"], 1)

q("The Beryl upgrade on Base introduced:",
  ["The B20 native token standard",
   "A new consensus mechanism",
   "A hard cap on total supply",
   "A new programming language"], 0)

q("B20 tokens can be used for gas. This means:",
  ["Users pay gas fees in B20 tokens rather than only in ETH",
   "B20 tokens replace all other fee tokens",
   "Gas fees are eliminated on Base",
   "Only B20 tokens can be transferred"], 0)

q("How does B20 benefit developers?",
  ["By requiring less code to deploy tokens",
   "By simplifying token management through native asset treatment",
   "By eliminating the need for smart contracts",
   "By providing free hosting for dApps"], 1)

q("What is the relationship between B20 and ERC-20?",
  ["B20 is an alternative to ERC-20 that makes tokens native assets on Base",
   "B20 is an extension of ERC-20 that adds more functions",
   "B20 is a security audit for ERC-20 tokens",
   "B20 converts ERC-20 tokens to NFTs"], 0)

q("Which upgrade brought native token standard capabilities to Base?",
  ["The Beryl upgrade",
   "The Holland upgrade",
   "The Istanbul upgrade",
   "The Shanghai upgrade"], 0)

q("B20 tokens being treated as native assets means:",
  ["They are minted directly by the protocol rather than through contract calls",
   "They have first-class status similar to ETH on Ethereum",
   "They cannot be transferred between wallets",
   "They exist only off-chain"], 1)

q("What can developers do with B20 tokens in their apps?",
  ["Accept B20 payments from users",
   "Only display B20 balances without transactions",
   "Only use B20 for testing purposes",
   "Convert B20 to fiat currency automatically"], 0)

q("B20 simplifies token management by:",
  ["Eliminating the need for wallets",
   "Treating tokens as native assets instead of just ERC-20 contracts",
   "Automatically converting all tokens to ETH",
   "Removing the need for private keys"], 1)

q("What type of standard is B20?",
  ["A privacy standard",
   "A native token standard",
   "A consensus mechanism",
   "A wallet encryption standard"], 1)

q("B20 tokens can be used for gas on Base, similar to:",
  ["How ETH works on Ethereum",
   "How SOL works on Solana",
   "How MATIC works on Polygon",
   "How BNB works on BNB Chain"], 0)

q("Which of these is a key feature of the B20 standard?",
  ["Proof of Work mining",
   "Tokens as native assets on Base",
   "Anonymous transactions by default",
   "Automatic yield generation"], 1)

q("What does the B20 standard enable for payment acceptance?",
  ["Apps can accept B20 payments",
   "Only native ETH payments are supported",
   "All payments must go through centralized exchanges",
   "Payments require multi-sig approval"], 0)

q("B20 is part of the Beryl upgrade, which is associated with:",
  ["Base",
   "Ethereum",
   "Solana",
   "Arbitrum"], 0)

q("How does B20 change the developer experience on Base?",
  ["It requires more complex token deployment",
   "It simplifies token management by making tokens native assets",
   "It removes smart contract capabilities entirely",
   "It forces all tokens to be identical"], 1)

q("B20 tokens enable gas fee payments because:",
  ["They are treated as native assets like ETH on Base",
   "They have a special gas exemption",
   "They are always worth exactly $1",
   "They are minted by validators on demand"], 0)

q("What distinguishes B20 from standard ERC-20 tokens?",
  ["B20 tokens don't have smart contracts",
   "B20 tokens are treated as native assets on Base, not just as contract-managed tokens",
   "B20 tokens can only be used for NFTs",
   "B20 tokens are only for testnet use"], 1)

q("The Beryl upgrade on Base introduced the:",
  ["B20 native token standard",
   "Base token sale",
   "Base decentralized exchange",
   "Base governance token"], 0)

q("Which of the following can B20 tokens be used for?",
  ["Gas payments on Base and acceptance in apps",
   "Only as collectible NFTs",
   "Only as governance tokens for a single DAO",
   "Only as wrapped Bitcoin on Base"], 0)

q("What does native asset mean for B20 tokens?",
  ["They are assets native to the Base blockchain, with first-class status like ETH",
   "They are mined directly from blocks",
   "They exist only in a centralized database",
   "They require special permissions to transfer"], 0)

q("B20 token standard was introduced to:",
  ["Replace ERC-20 entirely on all chains",
   "Make token management simpler on Base",
   "Eliminate gas fees on Base",
   "Create a new consensus mechanism"], 1)

# ======================================================================
# TOPIC 5: SECURITY (~35 questions)
# ======================================================================

q("What is the Security Council for Base responsible for?",
  ["Managing user passwords",
   "Governing protocol upgrades",
   "Running validator nodes",
   "Processing fiat withdrawals"], 1)

q("Security Council members on Base are responsible for:",
  ["Marketing and community growth",
   "Protocol safety and governing upgrades",
   "Token price stabilization",
   "Writing application code for dApps"], 1)

q("What guide helps developers avoid issues on Base?",
  ["Avoid Common Smart Contract Bugs guide",
   "Avoid Malicious Flags guide",
   "Avoid High Gas Fees guide",
   "Avoid Network Congestion guide"], 1)

q("What programs does Base offer for security issues?",
  ["Report a Vulnerability program and Bug bounty program",
   "Insurance claims program and refund program",
   "Token recovery program and account freeze program",
   "Dispute resolution program and arbitration program"], 0)

q("The Base Security Council governs:",
  ["Token prices on exchanges",
   "Protocol upgrades",
   "User account passwords",
   "dApp content moderation"], 1)

q("How are Security Council members expected to act?",
  ["In their own financial self-interest",
   "Responsibly for protocol safety",
   "By maximizing trading volume",
   "By promoting specific dApps"], 1)

q("Which program allows security researchers to report issues?",
  ["Report a Vulnerability program",
   "Referral rewards program",
   "Bug bounty retainer program",
   "Security consulting program"], 0)

q("What does the Bug bounty program on Base offer?",
  ["Rewards for finding and reporting security vulnerabilities",
   "Free tokens for all participants",
   "Guaranteed employment at Coinbase",
   "Exclusive NFT access"], 0)

q("Which of the following is NOT part of Base security ecosystem?",
  ["Security Council",
   "Report a Vulnerability program",
   "Token price insurance",
   "Bug bounty program"], 2)

q("The Security Council governs protocol upgrades, meaning:",
  ["They approve or reject changes to the Base protocol",
   "They set token prices for exchanges",
   "They manage user wallet passwords",
   "They create marketing campaigns"], 0)

q("What is the Avoid Malicious Flags guide for?",
  ["Helping developers avoid being flagged as malicious",
   "A guide for reporting malicious users",
   "A guide for creating malicious smart contracts",
   "A guide for network monitoring"], 0)

q("Base encourages security researchers to:",
  ["Keep vulnerabilities private without reporting",
   "Report vulnerabilities through the official program",
   "Exploit vulnerabilities for profit",
   "Sell vulnerability information to third parties"], 1)

q("Who comprises the Base Security Council?",
  ["Elected community members",
   "Members responsible for protocol safety and governance of upgrades",
   "Randomly selected token holders",
   "External auditors only"], 1)

q("What is the purpose of Base Bug bounty program?",
  ["To reward developers for building popular dApps",
   "To incentivize finding and responsibly disclosing security vulnerabilities",
   "To distribute governance tokens to users",
   "To fund marketing campaigns"], 1)

q("The Security Council plays a role in:",
  ["Day-to-day trading of Base tokens",
   "Protocol upgrades and network safety",
   "Marketing and business development",
   "User interface design"], 1)

q("What does Avoid Malicious Flags help developers do?",
  ["Get better search engine rankings",
   "Ensure their applications are not mistakenly flagged as malicious",
   "Create more profitable trading strategies",
   "Reduce gas costs for users"], 1)

q("Base provides a Report a Vulnerability program for:",
  ["Reporting security flaws in the Base protocol",
   "Reporting poor user experiences",
   "Reporting spam messages",
   "Reporting market manipulation"], 0)

q("Which is NOT a responsibility of the Security Council?",
  ["Governing protocol upgrades",
   "Ensuring protocol safety",
   "Setting token listing fees for exchanges",
   "Voting on protocol changes"], 2)

q("The Bug bounty program is part of Base:",
  ["Marketing strategy",
   "Security and vulnerability management approach",
   "Token distribution plan",
   "Validator rewards system"], 1)

q("How can developers avoid being flagged as malicious?",
  ["By following the Avoid Malicious Flags guide",
   "By not deploying smart contracts",
   "By only using testnet",
   "By registering with a centralized authority"], 0)

q("The Security Council for Base is involved in:",
  ["Approving protocol upgrades to ensure network safety",
   "Managing user funds directly",
   "Setting cryptocurrency exchange rates",
   "Writing application code for all dApps"], 0)

q("Which of these is true about the Base Bug bounty program?",
  ["It rewards researchers for finding vulnerabilities",
   "It requires a subscription fee to participate",
   "It only covers smart contract bugs, not protocol bugs",
   "It pays in fiat currency only"], 0)

q("Security Council members are responsible for:",
  ["Protocol safety and governance",
   "Running marketing campaigns",
   "Managing social media accounts",
   "Designing user interfaces"], 0)

q("The Avoid Malicious Flags guide is part of Base:",
  ["Developer documentation to help apps stay in good standing",
   "Consensus mechanism documentation",
   "Tokenomics whitepaper",
   "Staking guide"], 0)

q("Base Report a Vulnerability program is for:",
  ["Reporting protocol and security issues responsibly",
   "Reporting lost private keys",
   "Reporting transaction delays",
   "Reporting high gas fees"], 0)

q("What role does the Security Council play in Base governance?",
  ["They manage the community treasury",
   "They govern protocol upgrades for safety and security",
   "They set the price of gas fees",
   "They develop all dApps on Base"], 1)

q("The Bug bounty program aims to:",
  ["Improve network security by incentivizing vulnerability discovery",
   "Distribute tokens to the community",
   "Increase transaction throughput",
   "Reduce validator requirements"], 0)

q("Which statement about Base Security Council is FALSE?",
  ["They govern protocol upgrades",
   "They are responsible for protocol safety",
   "They set gas prices on the network",
   "They include members responsible for protocol governance"], 2)

q("What should researchers do if they find a security vulnerability?",
  ["Report it via the Report a Vulnerability program",
   "Post it publicly on social media",
   "Sell it to the highest bidder",
   "Keep it secret indefinitely"], 0)

q("The Avoid Malicious Flags guide helps ensure:",
  ["Applications are not mistakenly marked as malicious",
   "Transactions process faster",
   "Token prices remain stable",
   "Validators earn more rewards"], 0)

q("Base security approach includes:",
  ["Security Council, vulnerability reporting, and bug bounties",
   "Only smart contract audits",
   "Only third-party insurance",
   "Only community monitoring"], 0)

q("How often does the Security Council govern upgrades?",
  ["When protocol upgrades are proposed and need approval",
   "Daily through automated processes",
   "Only during network emergencies",
   "Never, upgrades are automatic"], 0)

q("What is the primary goal of Base Bug bounty program?",
  ["To enhance platform security through community participation",
   "To replace traditional security audits",
   "To distribute tokens equitably",
   "To market Base to security firms"], 0)

q("Base Report a Vulnerability program expects:",
  ["Responsible disclosure of security issues",
   "Immediate public disclosure of all bugs",
   "Payment in exchange for bug reports",
   "Legal action against reporters"], 0)

q("The Security Council governance of protocol upgrades ensures:",
  ["Changes are reviewed for safety before deployment",
   "Updates happen automatically without review",
   "All upgrades are rejected by default",
   "Only the Base team can propose changes"], 0)

# ======================================================================
# TOPIC 6: BASE LEDGERS (~20 questions)
# ======================================================================

q("What are Base Ledgers?",
  ["Personal finance tracking tools",
   "Institutional-grade onchain capital markets",
   "Simple accounting spreadsheets",
   "Validator reward calculators"], 1)

q("Base Ledgers are similar to which existing product but onchain?",
  ["Coinbase Prime but onchain",
   "PayPal but onchain",
   "Venmo but onchain",
   "Robinhood but onchain"], 0)

q("Who are Base Ledgers designed for?",
  ["Individual retail traders",
   "Institutions and large-scale capital markets",
   "Casual NFT collectors",
   "Small business owners"], 1)

q("Base Ledgers provide:",
  ["Personal budgeting tools",
   "Institutional-grade onchain capital markets",
   "Gaming leaderboards",
   "Social media feeds"], 1)

q("What does institutional-grade mean for Base Ledgers?",
  ["Designed for individual retail users",
   "Built to meet the standards and needs of institutions and large-scale capital markets",
   "Available only to accredited investors by law",
   "Requires a minimum of $1M to use"], 1)

q("How do Base Ledgers compare to Coinbase Prime?",
  ["Base Ledgers are the onchain version of similar institutional services",
   "Base Ledgers have nothing in common with Coinbase Prime",
   "Base Ledgers replace Coinbase Prime entirely",
   "Base Ledgers are a subset of Coinbase Prime features"], 0)

q("Which of the following BEST describes Base Ledgers?",
  ["A consumer crypto wallet",
   "Institutional-grade onchain capital markets",
   "A blockchain explorer",
   "An NFT marketplace"], 1)

q("Base Ledgers target which market segment?",
  ["Retail DeFi users",
   "Institutions and large-scale capital markets",
   "Gaming communities",
   "Social media platforms"], 1)

q("What is the relationship between Base Ledgers and Coinbase Prime?",
  ["Base Ledgers are similar to Coinbase Prime but fully onchain",
   "Base Ledgers are a competitor to Coinbase Prime",
   "Base Ledgers are powered by Coinbase Prime backend",
   "Base Ledgers are older than Coinbase Prime"], 0)

q("Base Ledgers are designed for:",
  ["Institutional-grade onchain capital markets",
   "Peer-to-peer lending",
   "Decentralized social networks",
   "Supply chain tracking"], 0)

q("Which statement about Base Ledgers is FALSE?",
  ["They are institutional-grade onchain capital markets",
   "They are similar to Coinbase Prime but onchain",
   "They are designed for individual retail traders",
   "They target institutions and large-scale capital markets"], 2)

q("What does onchain capital markets mean for Base Ledgers?",
  ["Capital markets activities executed on the blockchain",
   "A stock exchange running on Base",
   "A tokenized version of NASDAQ",
   "A centralized order book synced to the blockchain"], 0)

q("Base Ledgers are described as similar to Coinbase Prime but:",
  ["Onchain",
   "Faster",
   "Cheaper",
   "More decentralized"], 0)

q("Which type of organization would use Base Ledgers?",
  ["Individual retail investors",
   "Institutions needing onchain capital market infrastructure",
   "Small online stores",
   "Social media influencers"], 1)

q("Base Ledgers bring what type of markets onchain?",
  ["Prediction markets",
   "Capital markets for institutions",
   "NFT marketplaces",
   "Gaming marketplaces"], 1)

q("Base Ledgers are:",
  ["Institutional-grade onchain capital markets for Base",
   "Personal finance applications",
   "Educational blockchain simulators",
   "Community governance tools"], 0)

q("The phrase onchain capital markets refers to:",
  ["Traditional stock trading on the blockchain",
   "Capital market infrastructure built on a blockchain",
   "A tokenized real estate platform",
   "A cryptocurrency index fund"], 1)

q("Base Ledgers target which audience primarily?",
  ["Individual retail users",
   "Institutions and large-scale capital market participants",
   "NFT artists and collectors",
   "Blockchain developers"], 1)

q("What product is Base Ledgers comparable to?",
  ["Coinbase Prime, but executed onchain",
   "MetaMask, but institutional grade",
   "OpenSea, but for capital markets",
   "Uniswap, but for institutions"], 0)

q("Which of these would find Base Ledgers most useful?",
  ["A retail user making small transfers",
   "An institution managing large-scale onchain capital market operations",
   "An artist minting NFTs",
   "A gamer earning in-game rewards"], 1)

# ======================================================================
# TOPIC 7: x402 PAYMENTS (~25 questions)
# ======================================================================

q("What does x402 stand for?",
  ["A cross-chain bridge protocol",
   "HTTP 402 Payment Required status code",
   "A token standard for Base",
   "A wallet encryption method"], 1)

q("x402 refers to which HTTP status code?",
  ["HTTP 200 OK",
   "HTTP 402 Payment Required",
   "HTTP 403 Forbidden",
   "HTTP 404 Not Found"], 1)

q("What does x402 enable?",
  ["Free unlimited API access",
   "Pay-per-request API access using cryptocurrency",
   "Bulk discount pricing for APIs",
   "Monthly API subscription plans"], 1)

q("x402 is described as what kind of model for APIs?",
  ["Subscription-based model",
   "Pay-as-you-go model",
   "Freemium model",
   "Ad-supported model"], 1)

q("Which technology supports x402 payments on Base?",
  ["Base Ledgers",
   "Base Agents",
   "Base Accounts",
   "B20 tokens"], 1)

q("The number 402 in x402 refers to:",
  ["The block number where it was activated",
   "The HTTP status code for Payment Required",
   "The number of tokens required to use it",
   "The version number of the standard"], 1)

q("x402 enables pay-per-request access to:",
  ["Validator nodes",
   "APIs using cryptocurrency",
   "Blockchain storage",
   "Domain name registration"], 1)

q("What type of payment model does x402 use?",
  ["Pay-per-request (each API call costs a small crypto payment)",
   "Annual flat fee",
   "Ad-supported monetization",
   "Donation-based access"], 0)

q("Which of the following is the HTTP status code for Payment Required?",
  ["402",
   "401",
   "403",
   "404"], 0)

q("x402 is supported with which Base technology?",
  ["Base Agents",
   "Base Ledgers",
   "Base Accounts",
   "Builder Codes"], 0)

q("What problem does x402 solve?",
  ["Slow block finality",
   "Enabling micropayments for API access without subscriptions",
   "High gas fees on mainnet",
   "Lack of smart contract support"], 1)

q("x402 payments use which medium?",
  ["Credit cards",
   "Cryptocurrency",
   "Bank transfers",
   "Gift cards"], 1)

q("The pay-as-you-go model of x402 means users pay:",
  ["A flat monthly fee",
   "For each API request they make",
   "An annual subscription",
   "A one-time lifetime access fee"], 1)

q("How does x402 relate to Base Agents?",
  ["x402 payments are supported with Base Agents for autonomous payments",
   "x402 replaces Base Agents entirely",
   "x402 is unrelated to Base Agents",
   "x402 requires Base Agents to function"], 0)

q("Which of these is NOT true about x402?",
  ["It is based on the HTTP 402 status code",
   "It enables pay-per-request API access",
   "It is a new token standard for Base",
   "It is supported with Base Agents"], 2)

q("The HTTP 402 status code means:",
  ["OK",
   "Payment Required",
   "Forbidden",
   "Not Found"], 1)

q("x402 enables API access to be:",
  ["Paid per request rather than through subscription plans",
   "Completely free for all users",
   "Restricted to whitelisted addresses only",
   "Available only during business hours"], 0)

q("What is the x402 payment model best compared to?",
  ["A library subscription (pay annually)",
   "A vending machine (pay per item/request)",
   "A buffet (pay once, eat all)",
   "A tip jar (voluntary payments)"], 1)

q("Which Base feature integrates with x402 for payments?",
  ["Base Accounts",
   "Base Agents",
   "Base Ledgers",
   "Builder Codes"], 1)

q("x402 is specifically mentioned as being:",
  ["A regulatory framework",
   "Supported with Base Agents",
   "A consensus mechanism",
   "A staking protocol"], 1)

q("The pay-as-you-go model of x402 is ideal for:",
  ["Long-term subscriptions",
   "APIs where users pay per request with crypto",
   "Enterprise license agreements",
   "Unlimited data plans"], 1)

q("x402 leverages which existing web standard?",
  ["HTTP status codes",
   "DNS records",
   "SSL certificates",
   "HTML markup"], 0)

q("What makes x402 different from traditional API billing?",
  ["It uses cryptocurrency for per-request micropayments instead of subscriptions",
   "It is more expensive than traditional billing",
   "It requires manual invoicing",
   "It only works on weekends"], 0)

q("x402 payments are designed for:",
  ["Large bulk transactions only",
   "API access where each request can be paid for individually",
   "One-time setup fees",
   "Quarterly billing cycles"], 1)

q("Which protocol is x402 built upon?",
  ["FTP",
   "HTTP",
   "WebSocket",
   "gRPC"], 1)

# ======================================================================
# TOPIC 8: OTHER / ECOSYSTEM (~25 questions)
# ======================================================================

q("What does the Base Bridge allow users to do?",
  ["Bridge assets between L1 and Base",
   "Bridge between Base and Solana only",
   "Convert fiat to cryptocurrency",
   "Stake tokens for rewards"], 0)

q("The Solana Bridge allows bridging between:",
  ["Solana and Ethereum",
   "Solana and Base",
   "Solana and Bitcoin",
   "Solana and Arbitrum"], 1)

q("What is the Base Batches program?",
  ["A batch transaction processing tool",
   "Community events organized by Base",
   "A token airdrop mechanism",
   "A smart contract batching library"], 1)

q("Base offers Grants for:",
  ["Funding projects and building in the ecosystem",
   "Personal loans for users",
   "Validator hardware purchases",
   "Marketing agency retainers"], 0)

q("What is Retroactive Funding on Base?",
  ["Funding for projects that have already shown impact",
   "Pre-paid grants for future work",
   "Loans that must be repaid with interest",
   "Insurance for smart contract failures"], 0)

q("What types of infrastructure are available on Base?",
  ["Node Providers, Block Explorers, and Data Indexers",
   "Only a single block explorer",
   "Only centralized infrastructure",
   "No infrastructure, developers build from scratch"], 0)

q("Where can developers find contract addresses for Base?",
  ["Contract addresses are available for reference",
   "Contract addresses are not disclosed",
   "Contract addresses are randomized daily",
   "Contract addresses require paid access"], 0)

q("What programming resources are available for AI development on Base?",
  ["Static Docs Files and a Prompt Library",
   "Only API documentation",
   "Only video tutorials",
   "Only community forums"], 0)

q("Base has a Bridge for which two ecosystems?",
  ["Base Bridge (L1 to Base) and Solana Bridge (Solana to Base)",
   "Base Bridge and Bitcoin Bridge",
   "Base Bridge and Ethereum Bridge only",
   "Only a single bridge"], 0)

q("Builder Rewards program on Base is designed for:",
  ["Validators",
   "Builders contributing to the ecosystem",
   "Only enterprise customers",
   "Only Coinbase employees"], 1)

q("Base Batches are described as:",
  ["Community events",
   "Software development kits",
   "Token standards",
   "Consensus mechanisms"], 0)

q("What is available for developers who need to reference Base contracts?",
  ["Contract addresses for reference",
   "Encrypted contract code only",
   "Contract addresses require NDA",
   "No contract information is public"], 0)

q("Data Indexers are available on Base for:",
  ["Indexing and querying blockchain data efficiently",
   "Mining new blocks",
   "Storing files permanently",
   "Running validator nodes"], 0)

q("Node Providers on Base offer:",
  ["Access to Base nodes for dApp development",
   "Mining hardware for sale",
   "Cloud storage services",
   "Domain name registration"], 0)

q("Block Explorers on Base enable users to:",
  ["View transactions, blocks, and addresses on the network",
   "Submit transactions manually",
   "Create new wallets",
   "Stake tokens directly"], 0)

q("Which of these is an infrastructure offering on Base?",
  ["Block Explorers",
   "Email hosting",
   "Social media management",
   "Video streaming"], 0)

q("What does the Base Bridge facilitate?",
  ["Asset transfers between Layer-1 and Base",
   "Token swaps on decentralized exchanges",
   "Smart contract compilation",
   "Wallet recovery"], 0)

q("The Solana Bridge is specifically for bridging between:",
  ["Solana and Ethereum",
   "Solana and Base",
   "Solana and Arbitrum",
   "Solana and Polygon"], 1)

q("Retroactive Funding on Base rewards:",
  ["Projects based on their past contributions and impact",
   "Future development proposals",
   "Validators for block production",
   "Users for transaction volume"], 0)

q("Base Grants program is for:",
  ["Projects building within the Base ecosystem",
   "Personal use grants for individuals",
   "Hardware purchase subsidies",
   "Travel expenses for events"], 0)

q("Which of the following is NOT an infrastructure category on Base?",
  ["Node Providers",
   "Block Explorers",
   "Email Service Providers",
   "Data Indexers"], 2)

q("The Prompt Library on Base is a resource for:",
  ["AI development and agent creation",
   "Smart contract templates",
   "Validator configuration",
   "UI component design"], 0)

q("Static Docs Files on Base are intended for:",
  ["AI and agent-based development reference",
   "Printed marketing materials",
   "Legal compliance documents",
   "User onboarding pamphlets"], 0)

q("Builder Rewards on Base are for:",
  ["Builders who contribute to the Base ecosystem",
   "All users who hold Base tokens",
   "Only validators who run nodes",
   "Only enterprise partners"], 0)

q("Base Batches are best described as:",
  ["Community events for the Base ecosystem",
   "Batch transaction processing tool",
   "Validator batch signing protocol",
   "Token airdrop mechanism"], 0)

# ======================================================================
# FINAL ASSEMBLY
# ======================================================================

# Assign sequential IDs
for i, q_item in enumerate(questions):
    q_item["id"] = i

# Verify uniqueness
question_texts = [q_item["question"] for q_item in questions]
assert len(set(question_texts)) == len(question_texts), f"DUPLICATE questions found! {len(question_texts)} vs {len(set(question_texts))}"

# Check correctIndex distribution
dist = Counter(q_item["correctIndex"] for q_item in questions)
print(f"Total questions: {len(questions)}")
print(f"CorrectIndex distribution: {dict(sorted(dist.items()))}")

# Verify each question has 4 unique options
for q_item in questions:
    assert len(q_item["options"]) == 4, f"Q {q_item['id']}: Need 4 options, got {len(q_item['options'])}"
    assert len(set(q_item["options"])) == 4, f"Q {q_item['id']}: Duplicate options"

# Build output
output = {
    "meta": {
        "ecosystem": "Base",
        "batchId": "base-2026-07-11-batch3",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totalQuizzes": len(questions),
        "questionsPerSession": 5
    },
    "quizzes": questions
}

output_path = "/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch3.json"
with open(output_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"\nWritten to {output_path}")
print("All validation passed!")
