import json
from datetime import datetime, timezone
from collections import Counter

with open("/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch4.json") as f:
    data = json.load(f)

# Remove duplicates
seen = set()
clean = []
for q in data['quizzes']:
    key = q['question'].lower().strip()
    if key not in seen:
        clean.append(q)
        seen.add(key)

# Additional questions to fill gaps
extra_questions = [
    "Base is built on which software stack?",
    "The OP Stack is maintained by:",
    "Base uses Ethereum for:",
    "Flashblocks are built using:",
    "Vanilla mode blocks on Base are built by:",
    "The GasPriceOracle predeploy enables:",
    "B20 tokens on Base can be used for:",
    "Basescan provides:",
    "Base mainnet chain ID is:",
    "MetaMask connects to Base via:",
    "EVM equivalence on Base means bytecode:",
    "Base contract verification happens on:",
    "CCTP is specifically for:",
    "Compared to Solana, Base offers:",
    "Base is part of the Superchain, meaning it:",
    "Builder Rewards on Base are:",
    "Base Dashboard URL is:",
    "The Configuration Changelog tracks:",
    "The Beryl upgrade introduced:",
    "Base separates consensus from execution, meaning:",
    "Base sequencer role is performed by:",
    "To verify a contract on Base:",
    "Base developer tools include:",
    "Base Foundation provides grants to:",
    "The Base Mentorship program:",
    "Base can be added to any wallet supporting:",
    "The Azul upgrade refers to:",
    "Base's relationship to the OP Stack is:",
    "Flashblocks preconfirmations arrive every:",
    "The Jovian upgrade introduced:",
    "Cross-chain USDC on Base uses:",
    "MetaMask users add Base by specifying:",
    "Developers deploy to Base the same way as Ethereum because of:",
    "Base account abstraction enables:",
    "Base Batches are:",
    "Base Retroactive Funding rewards:",
    "Block explorers for Base include:",
    "Data indexers on Base can track:",
    "The Base status page URL is:",
    "Base is the number one Ethereum L2 by:",
    "Base incubator is:",
    "Base bridges enable:",
    "Base notifications in apps are:",
    "Base Base Fee on Base is set by:",
    "Base Builder Codes are available for:",
    "Base Ledgers are for:",
    "Base Solana Bridge enables:",
    "Base Security Council:",
    "Protocol upgrades on Base include:",
    "Base Grants program:",
]

extra_options = [
    ["Klaytn", "OP Stack", "Arbitrum Nitro", "zkSync Era"],
    ["Coinbase", "Ethereum Foundation", "OP Labs", "Base Foundation"],
    ["Transaction execution", "Block production", "Settlement and security", "Token minting"],
    ["base-reth-node", "op-reth", "base-builder", "op-node"],
    ["base-builder", "op-batcher", "base-reth-node", "op-node"],
    ["Token swaps", "Block production", "Transaction ordering", "L1 fee estimation"],
    ["Governance only", "NFT minting", "Bridge fees", "Gas payments"],
    ["Block exploration only", "Contract verification only", "Transaction lookups only", "All of the above"],
    ["10", "42161", "8453", "1"],
    ["Base plugin", "Coinbase extension", "Custom RPC with Chain ID 8453", "EIP-3085 wallet_addEthereumChain"],
    ["Is compatible without modification", "Needs recompilation", "Uses custom opcodes", "Is incompatible"],
    ["Etherscan", "Base Dashboard", "Coinbase API", "Basescan"],
    ["General token bridging", "NFT bridging", "Message passing", "USDC cross-chain transfers"],
    ["Higher TPS", "Lower fees", "Proof-of-History consensus", "EVM-equivalent development"],
    ["Is isolated from other chains", "Has its own security model", "Interoperates with other OP Stack chains", "Does not bridge to Ethereum"],
    ["NFT badges", "Discord roles", "License to build", "Financial incentives for developers"],
    ["docs.base.org", "status.base.org", "dashboard.base.org", "base.org/dashboard"],
    ["Code commits", "Blog posts", "Community events", "Parameter changes over time"],
    ["Flashblocks", "EIP-1559", "Minimum base fee", "B20 token standard"],
    ["Only one node type exists", "Execution happens off-chain", "Consensus is skipped", "Different software handles each role"],
    ["base-reth-node", "op-node", "base-builder", "op-proposer"],
    ["Use Etherscan", "Use Coinbase dashboard", "Use Base CLI", "Use Basescan verification tool"],
    ["Only Hardhat", "Only Foundry", "Only Remix", "All of the above"],
    ["Coinbase employees only", "OP Labs only", "Ethereum Foundation", "Projects building on Base"],
    ["Provides free RPC", "Offers contract auditing", "Runs validator nodes", "Pairs new builders with experienced ones"],
    ["Only Coinbase Wallet", "Only MetaMask", "Custom proprietary protocol", "Standard Ethereum RPC"],
    ["The latest Beryl upgrade", "A testnet only feature", "A wallet feature", "A previous protocol upgrade"],
    ["Built without it", "Competing with it", "Unrelated to it", "Built on it"],
    ["2s", "500ms", "1s", "200ms"],
    ["Flashblocks", "B20 token standard", "EIP-1559", "Minimum base fee"],
    ["CCIP", "LayerZero", "Wormhole", "CCTP"],
    ["Only a network name", "Only an RPC URL", "A Coinbase API key", "Chain ID 8453 and an RPC URL"],
    ["Same chain ID", "Coinbase tooling", "OP Stack compatibility", "EVM equivalence"],
    ["Native token minting", "Flashblock sequencing", "L1 settlement", "Smart wallets on Base"],
    ["Batch transactions", "Validator groups", "Transaction bundles", "Community events"],
    ["Future proposals", "Validator operations", "Bridge usage", "Past contributions to Base ecosystem"],
    ["Solscan", "BscScan", "PolygonScan", "Basescan"],
    ["Only token prices", "Only NFT sales", "Only governance votes", "Smart contract events and transactions"],
    ["docs.base.org", "base.org", "dashboard.base.org", "status.base.org"],
    ["Market cap", "Total value locked", "Developer activity", "TVL and user adoption"],
    ["OP Labs", "Ethereum Foundation", "a16z", "Coinbase"],
    ["Only ERC-20 transfers", "Only NFT transfers", "Only message passing", "Asset transfers between L1 and Base"],
    ["Sent via email", "Require SMS", "Onchain push notifications", "Built into the blockchain protocol"],
    ["The Ethereum L1 base fee", "The Base sequencer", "EIP-1559 mechanism", "GasPriceOracle"],
    ["App developers only", "Wallet developers only", "Agent developers only", "All of the above"],
    ["Retail trading only", "NFT marketplace only", "DeFi routing only", "Institutional onchain capital markets"],
    ["Solana to Ethereum transfers", "Solana to Base transfers", "Base to Solana NFT transfers only", "Token swaps on Solana"],
    ["Governs protocol upgrades", "Runs the network", "Manages treasury", "Writes code"],
    ["Flashblocks only", "Minimum base fee only", "B20 standard only", "Beryl, Azul, and Optimism"],
    ["Funds Coinbase projects", "Only for US companies", "For projects building on Base ecosystem", "Only for DeFi protocols"],
]

extra_correct = [1, 2, 2, 2, 2, 3, 3, 3, 2, 2, 0, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 0, 2, 2, 2]

for i in range(len(extra_questions)):
    q = {
        "question": extra_questions[i],
        "options": list(extra_options[i]),
        "correctIndex": extra_correct[i]
    }
    clean.append(q)

# Renumber
for i, q in enumerate(clean):
    q['id'] = i

# Round-robin rebalance
targets = [0,1,2,3] * (len(clean) // 4 + 1)
for i, q in enumerate(clean):
    old_idx = q['correctIndex']
    correct_text = q['options'][old_idx]
    del q['options'][old_idx]
    target_idx = targets[i % 4]
    q['options'].insert(target_idx, correct_text)
    q['correctIndex'] = target_idx
    q['id'] = i

dist = Counter(q['correctIndex'] for q in clean)
print(f"Total: {len(clean)} questions")
print(f"Distribution: {dict(sorted(dist.items()))}")

# Check duplicates
seen2 = set()
dupes = []
for q in clean:
    key = q['question'].lower().strip()
    if key in seen2:
        dupes.append(key)
    seen2.add(key)
print(f"Duplicates: {len(dupes)}")
if dupes:
    for d in dupes[:5]:
        print(f"  - {d}")

final = {
    "meta": {
        "ecosystem": "Base",
        "batchId": "base-2026-07-11-batch4",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totalQuizzes": len(clean),
        "questionsPerSession": 5
    },
    "quizzes": clean
}

with open("/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch4.json", "w") as f:
    json.dump(final, f, indent=2)
print("Written successfully")
