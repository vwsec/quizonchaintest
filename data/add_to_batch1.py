#!/usr/bin/env python3
"""Add ~14 more questions to batch1 to reach ~170."""

import json
from collections import Counter

# Read existing file
with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc-batch1.json') as f:
    data = json.load(f)

existing_ids = {q['question'] for q in data['quizzes']}

new_questions = [
    {
        "question": "Arc separates consensus from execution into two layers. What advantage does this provide?",
        "options": [
            "Each layer can be independently optimized for its specific function",
            "It reduces the total number of validators needed",
            "It eliminates the need for transaction fees",
            "It makes the network compatible with Bitcoin"
        ],
        "correctIndex": 0
    },
    {
        "question": "Which of these is a reason Arc uses a permissioned validator set?",
        "options": [
            "To enable anyone in the world to validate transactions",
            "To achieve higher throughput and faster finality with known validators",
            "To make the network completely decentralized",
            "To allow token holders to vote on block production"
        ],
        "correctIndex": 1
    },
    {
        "question": "What type of AI development tooling does Arc provide?",
        "options": [
            "A neural network for price prediction",
            "An MCP (Model Context Protocol) server for agent-based development",
            "An AI-powered block explorer",
            "A machine learning model for fraud detection"
        ],
        "correctIndex": 1
    },
    {
        "question": "Arc App Kits support crosschain payment workflows across which ecosystems?",
        "options": [
            "Ethereum only",
            "EVM chains, Solana, and Circle Wallets",
            "Bitcoin and Litecoin only",
            "All Cosmos IBC chains"
        ],
        "correctIndex": 1
    },
    {
        "question": "On Arc, the ERC-20 USDC interface at 6 decimals is primarily designed for:",
        "options": [
            "Native gas transfers between accounts",
            "Seamless integration with existing Ethereum DeFi protocols",
            "Validator staking rewards",
            "Cross-chain messaging"
        ],
        "correctIndex": 1
    },
    {
        "question": "On Arc, the native USDC interface at 18 decimals is primarily designed for:",
        "options": [
            "Integration with Ethereum DeFi protocols",
            "Gas payments and general EVM operations requiring higher precision",
            "Governance voting weight calculation",
            "Validator key generation"
        ],
        "correctIndex": 1
    },
    {
        "question": "How does Arc's fee model differ from a standard EIP-1559 chain?",
        "options": [
            "Arc uses a flat fee with no adjustments",
            "Arc uses USDC-denominated fees with EWMA smoothing instead of step-function base fee changes",
            "Arc has no base fee mechanism",
            "Arc uses a first-price auction for every block"
        ],
        "correctIndex": 1
    },
    {
        "question": "What is the primary purpose of Arc's growing ecosystem of infrastructure partners?",
        "options": [
            "To provide tooling, wallets, oracles, and integrations for developers",
            "To market Arc as a consumer brand",
            "To run the Arc validator set",
            "To audit all smart contracts deployed on Arc"
        ],
        "correctIndex": 0
    },
    {
        "question": "Which statement best describes the relationship between consensus and execution layers on Arc?",
        "options": [
            "The consensus layer runs Malachite BFT; the execution layer runs the EVM",
            "Both layers run the EVM for redundancy",
            "The execution layer runs Malachite BFT; the consensus layer runs the EVM",
            "Both layers run Malachite BFT in parallel"
        ],
        "correctIndex": 0
    },
    {
        "question": "Which of these is a benefit of Arc being a Layer-1 blockchain rather than a rollup?",
        "options": [
            "Lower security guarantees",
            "No dependency on an underlying chain for finality or security",
            "Automatic access to Ethereum's user base",
            "Simpler smart contract deployment"
        ],
        "correctIndex": 1
    },
    {
        "question": "What is the native USDC interface on Arc optimized for?",
        "options": [
            "Large institutional transfers over $1M",
            "Gas accounting and native value transfers with 18-decimal precision",
            "Cross-chain swaps exclusively",
            "Staking in the consensus layer"
        ],
        "correctIndex": 1
    },
    {
        "question": "Which of these correctly describes a feature of Arc's Malachite BFT consensus?",
        "options": [
            "Probabilistic finality with 12-second block times",
            "Sub-second deterministic finality with a permissioned validator set",
            "Proof of Work mining with adjustable difficulty",
            "Delegated Proof of Stake with token-weighted voting"
        ],
        "correctIndex": 1
    },
    {
        "question": "What is one key difference between native USDC transfers on Arc and ERC-20 USDC transfers on Ethereum?",
        "options": [
            "On Arc, USDC transfers are native and don't require a contract call; on Ethereum, they require an ERC-20 call",
            "On Ethereum, USDC transfers are free; on Arc they cost more",
            "On Arc, USDC transfers are batched hourly; on Ethereum they are instant",
            "On Ethereum, USDC transfers cannot be reversed; on Arc they can"
        ],
        "correctIndex": 0
    },
    {
        "question": "When using Arc as a developer, which of these workflow changes must you account for?",
        "options": [
            "Deploying contracts in a new language",
            "Handling deterministic finality (no reorgs) and USDC as the native gas token",
            "Running a custom fork of Hardhat",
            "Paying higher gas fees than on Ethereum"
        ],
        "correctIndex": 1
    },
    {
        "question": "Which of the following accurately describes Arc's approach to transaction fees?",
        "options": [
            "Fees are paid in a volatile token whose dollar value fluctuates",
            "Fees are paid in USDC and are predictable in dollar terms",
            "Fees are zero for all transactions on the network",
            "Fees are deducted from a prepaid subscription balance"
        ],
        "correctIndex": 1
    },
    {
        "question": "Arc Network supports which of the following stablecoins as part of its native model?",
        "options": [
            "USDC only",
            "USDC and DAI",
            "USDC, EURC, and USYC",
            "USDT, USDC, and DAI"
        ],
        "correctIndex": 2
    },
    {
        "question": "What is the relationship between Arc's testnet and the chain ID 5042002?",
        "options": [
            "5042002 is the chain ID for Arc testnet",
            "5042002 is the block time in milliseconds",
            "5042002 is the maximum number of validators",
            "5042002 is the gas limit per block"
        ],
        "correctIndex": 0
    },
    {
        "question": "Which of these is a benefit of deterministic finality for Arc developers?",
        "options": [
            "Simpler transaction lifecycle without needing to handle chain reorganizations",
            "Lower smart contract deployment costs",
            "Faster Solidity compilation times",
            "Access to Ethereum mainnet liquidity"
        ],
        "correctIndex": 0
    }
]

# Filter out duplicates
new_unique = []
for q in new_questions:
    if q['question'] not in existing_ids:
        new_unique.append(q)
        existing_ids.add(q['question'])

print(f"Adding {len(new_unique)} new questions")

# Compute next ID
next_id = max(q['id'] for q in data['quizzes']) + 1

# Add them and assign IDs
for q in new_unique:
    q['id'] = next_id
    next_id += 1
    data['quizzes'].append(q)

# Update totals
data['meta']['totalQuizzes'] = len(data['quizzes'])
data['meta']['batchId'] = 'arc-2026-07-11-batch1'

# Write back
with open('/home/elmardi/Documents/Web3/quizonchain/data/quizzes-arc-batch1.json', 'w') as f:
    json.dump(data, f, indent=2)

dist = Counter(q['correctIndex'] for q in data['quizzes'])
print(f"Total: {len(data['quizzes'])} questions")
print(f"Distribution: {dict(sorted(dist.items()))}")
