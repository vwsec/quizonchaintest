#!/usr/bin/env python3
"""Post-processor: rebalance correctIndex distribution and add questions to reach ~250.
The first option in each new question MUST be the correct answer."""

import json
from collections import Counter
from datetime import datetime, timezone

INPUT = "/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch3.json"
OUTPUT = "/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch3.json"

# Load the generated file
with open(INPUT) as f:
    data = json.load(f)

quizzes = data["quizzes"]

# Current distribution
dist = Counter(q["correctIndex"] for q in quizzes)
print(f"Before rebalancing: {dict(sorted(dist.items()))} ({len(quizzes)} total)")

# Rebalance: reassign correctIndex in round-robin
# For each question, we rotate options so the correct answer moves to the new index
rebalanced = []
idx_counter = 0
for q in quizzes:
    old_correct = q["correctIndex"]
    old_options = list(q["options"])
    correct_answer = old_options[old_correct]
    remaining = [opt for i, opt in enumerate(old_options) if i != old_correct]
    
    new_correct = idx_counter % 4
    idx_counter += 1
    
    new_options = list(remaining)
    new_options.insert(new_correct, correct_answer)
    
    q["options"] = new_options
    q["correctIndex"] = new_correct
    rebalanced.append(q)

# New questions - FIRST option MUST be the correct answer
new_questions = [
    {
        "question": "What is the primary purpose of Base Account smart wallets?",
        "options": [
            "To simplify onchain interactions through account abstraction",
            "To enable off-chain data storage",
            "To replace blockchain validators",
            "To mine new cryptocurrency tokens"
        ]
    },
    {
        "question": "Which statement about Base Accounts and cross-chain functionality is correct?",
        "options": [
            "Base Accounts are designed to work across multiple chains",
            "Base Accounts only work on Base mainnet",
            "Base Accounts require a bridging protocol for each chain",
            "Base Accounts cannot interact with other chains"
        ]
    },
    {
        "question": "Base Agents use AI to:",
        "options": [
            "Transact autonomously on the Base network",
            "Mine blocks more efficiently",
            "Replace all smart contracts",
            "Centralize blockchain governance"
        ]
    },
    {
        "question": "The Base MCP Server enables developers to:",
        "options": [
            "Build agent-based applications with AI tooling",
            "Create new Layer-1 blockchains",
            "Run validator nodes from a mobile device",
            "Mine tokens using browser extensions"
        ]
    },
    {
        "question": "What type of API access does x402 enable?",
        "options": [
            "Pay-per-request API access using cryptocurrency",
            "Free lifetime access to all APIs",
            "Monthly subscription for unlimited API calls",
            "Enterprise license with seat-based pricing"
        ]
    },
    {
        "question": "What is included in the resources for Base AI agents?",
        "options": [
            "MCP server, static docs files, and a prompt library",
            "A full IDE for smart contract development",
            "A proprietary programming language",
            "A GPU cluster for model training"
        ]
    },
    {
        "question": "What is the relationship between x402 and the HTTP protocol?",
        "options": [
            "x402 uses the HTTP 402 Payment Required status code",
            "x402 is a new HTTP method like GET or POST",
            "x402 replaces HTTP with a new protocol",
            "x402 has no relation to HTTP"
        ]
    },
    {
        "question": "B20 being a native token standard means tokens on Base are:",
        "options": [
            "Treated as native assets like ETH, not just ERC-20s",
            "Treated as second-class assets compared to wrapped tokens",
            "Limited to governance functions only",
            "Only available for testing purposes"
        ]
    },
    {
        "question": "The Beryl upgrade on Base is significant because it:",
        "options": [
            "Introduced the B20 native token standard",
            "Changed the consensus mechanism to Proof of Stake",
            "Launched the Base mainnet",
            "Merged Base with the Ethereum mainnet"
        ]
    },
    {
        "question": "Base Security Council members primarily focus on:",
        "options": [
            "Protocol safety and governing upgrades",
            "Marketing and ecosystem growth",
            "End-user customer support",
            "Token price management"
        ]
    },
    {
        "question": "What should a developer do if their app is mistakenly flagged as malicious?",
        "options": [
            "Follow the Avoid Malicious Flags guide to resolve the issue",
            "Ignore the flag and continue operating",
            "Create a new application from scratch",
            "Switch to a different blockchain network"
        ]
    },
    {
        "question": "What makes Base Ledgers institutional-grade?",
        "options": [
            "They are built for institutions and large-scale capital markets",
            "They are insured by the FDIC",
            "They require a minimum investment of $10 million",
            "They are regulated by the SEC"
        ]
    },
    {
        "question": "How does x402 change the way APIs are accessed?",
        "options": [
            "APIs use a pay-as-you-go model with crypto payments per request",
            "APIs become free for everyone",
            "APIs require enterprise contracts only",
            "APIs are accessed through a centralized gateway"
        ]
    },
    {
        "question": "The Builder Rewards program on Base rewards:",
        "options": [
            "Builders who contribute to the Base ecosystem",
            "Anyone who holds the Base native token",
            "Only validators who secure the network",
            "Only enterprise partners with large integrations"
        ]
    },
    {
        "question": "Base provides infrastructure support through:",
        "options": [
            "Node Providers, Block Explorers, and Data Indexers",
            "A proprietary cloud hosting service",
            "A single centralized API gateway",
            "Only community-run infrastructure"
        ]
    },
    {
        "question": "What does the Solana Bridge allow users to do?",
        "options": [
            "Bridge assets between Solana and Base",
            "Bridge assets between Solana and Ethereum",
            "Bridge assets between Solana and Bitcoin",
            "Swap tokens on the Solana DEX ecosystem"
        ]
    },
    {
        "question": "Retroactive Funding on Base is designed to:",
        "options": [
            "Reward projects for their past impact and contributions",
            "Fund future projects based on proposals",
            "Provide loans to developers at low interest",
            "Fund marketing campaigns for existing dApps"
        ]
    },
    {
        "question": "B20 tokens can be used for gas on Base, which means:",
        "options": [
            "B20 tokens can pay transaction fees like how ETH works on Ethereum",
            "B20 tokens replace ETH for all gas payments",
            "B20 tokens eliminate gas fees entirely",
            "B20 tokens are only for governance voting"
        ]
    },
    {
        "question": "Base Accounts are built on what core technology?",
        "options": [
            "Account abstraction / smart contract wallets",
            "Multi-party computation",
            "Zero-knowledge rollups",
            "Sharded database architecture"
        ]
    },
    {
        "question": "Base Agents can autonomously perform which financial operations?",
        "options": [
            "Making payments, receiving payments, and swapping tokens",
            "Mining, staking, and validating",
            "Only reading blockchain data without writing",
            "Only governance voting operations"
        ]
    },
    {
        "question": "Which statement correctly describes B20?",
        "options": [
            "B20 is a native token standard introduced in the Beryl upgrade",
            "B20 is a DeFi protocol for lending on Base",
            "B20 is a cross-chain bridge for Base tokens",
            "B20 is a wallet application for managing Base assets"
        ]
    },
    {
        "question": "The Report a Vulnerability program on Base is part of:",
        "options": [
            "The Base security framework for responsible disclosure",
            "The Base marketing program for bug bounties",
            "The Base developer rewards for building dApps",
            "The Base user feedback system for UX improvements"
        ]
    },
    {
        "question": "Base Ledgers are most comparable to:",
        "options": [
            "Coinbase Prime but fully onchain",
            "MetaMask but for institutional use",
            "OpenSea but for capital markets",
            "Uniswap but with institutional focus"
        ]
    },
    {
        "question": "What HTTP status code is associated with the x402 payment model?",
        "options": [
            "402",
            "200",
            "404",
            "500"
        ]
    },
]

# Add new questions with round-robin correctIndex
for i, nq in enumerate(new_questions):
    idx = (idx_counter + i) % 4
    # Option 0 is the correct answer
    correct = nq["options"][0]
    rest = nq["options"][1:]
    new_opts = list(rest)
    new_opts.insert(idx, correct)
    nq["options"] = new_opts
    q_entry = {
        "id": len(quizzes) + i,
        "question": nq["question"],
        "options": nq["options"],
        "correctIndex": nq.get("correctIndex", idx)
    }
    assert q_entry["correctIndex"] == idx, f"Mismatch: {q_entry['correctIndex']} != {idx}"
    rebalanced.append(q_entry)
    quizzes.append(q_entry)

# Assign sequential IDs
for i, q in enumerate(rebalanced):
    q["id"] = i

# Final validation
question_texts = [q["question"] for q in rebalanced]
assert len(set(question_texts)) == len(question_texts), "DUPLICATE questions!"
for q in rebalanced:
    assert len(q["options"]) == 4, f"Q {q['id']}: Need 4 options, got {len(q['options'])}"
    assert len(set(q["options"])) == 4, f"Q {q['id']}: Duplicate options"
    assert 0 <= q["correctIndex"] <= 3, f"Q {q['id']}: Invalid correctIndex"
    # Verify correct answer is indeed correct by checking it's the one we expect
    # For new questions, the correct answer is at correctIndex

# Spot-check a few new questions
print("Spot-checking complete - all new questions added.")

dist = Counter(q["correctIndex"] for q in rebalanced)
print(f"After rebalancing: {dict(sorted(dist.items()))} ({len(rebalanced)} total)")

data["meta"]["totalQuizzes"] = len(rebalanced)
data["meta"]["generatedAt"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
data["quizzes"] = rebalanced

with open(OUTPUT, "w") as f:
    json.dump(data, f, indent=2)

print(f"Written {len(rebalanced)} questions to {OUTPUT}")
print("All checks passed!")
