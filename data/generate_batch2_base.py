#!/usr/bin/env python3
"""
Generate ~250 Base quiz questions about Finality, Fees, Throughput, Bridging.
Output: quizzes-base-batch2.json
"""

import json
import random
import datetime
from collections import Counter

random.seed(42)

questions = []

def q(question, options, correctIndex):
    questions.append({
        "question": question,
        "options": options,
        "correctIndex": correctIndex
    })

# ======================================================================
# TOPIC 1: TRANSACTION FINALITY (~70 questions)
# ======================================================================

# --- 1.1 Finality definition and basics ---
q("What does 'finality' mean in the context of blockchain transactions?",
  ["The point at which a transaction is included in a block",
   "The point at which a transaction becomes irreversible",
   "The point at which a transaction is broadcast to the network",
   "The point at which a transaction is signed by the user"], 1)

q("How does finality for regular Base L2 transactions differ from withdrawal transactions?",
  ["They are the same — both wait 7 days",
   "Regular L2 transactions finalize quickly; only withdrawals must wait 7 days",
   "Withdrawals finalize in seconds; regular transactions wait 7 days",
   "Both finalize in approximately 2 minutes"], 1)

q("Regular Base L2 transactions such as swaps and sends do NOT need to:",
  ["Pay gas fees",
   "Wait 7 days to finalize",
   "Be signed by the user's private key",
   "Pass through the sequencer"], 1)

q("Only which type of Base transaction must wait 7 days?",
  ["Regular token swaps on Base",
   "Withdrawals from Base to Ethereum",
   "Deposits from Ethereum to Base",
   "Flashblock preconfirmations"], 1)

q("How many stages of increasing finality exist for L2 transactions on Base?",
  ["Two",
   "Three",
   "Four",
   "Five"], 2)

# --- 1.2 Stage 1: Flashblock Inclusion (~200ms) ---
q("What is the first stage of finality for a Base L2 transaction?",
  ["L2 Block Inclusion",
   "L1 Batch Inclusion",
   "Flashblock Inclusion",
   "L1 Batch Finality"], 2)

q("How quickly does Flashblock Inclusion occur on Base?",
  ["Approximately 200 milliseconds",
   "Approximately 2 seconds",
   "Approximately 2 minutes",
   "Approximately 20 minutes"], 0)

q("During Flashblock Inclusion, by whom is the transaction included in a preconfirmation block?",
  ["The validator set",
   "The sequencer",
   "The Ethereum L1",
   "The fault proof challenger"], 1)

q("What is the reorg probability for a transaction that has achieved Flashblock Inclusion?",
  ["Under 5%",
   "Under 1%",
   "Under 0.001%",
   "Over 5%"], 2)

q("A transaction that has been included in a Flashblock preconfirmation block has a reorg probability of:",
  ["Under 0.001%",
   "Under 0.1%",
   "Under 1%",
   "Under 10%"], 0)

# --- 1.3 Stage 2: L2 Block Inclusion (~2s) ---
q("What is the second stage of finality for a Base L2 transaction?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "L1 Batch Inclusion",
   "L1 Batch Finality"], 1)

q("How long does L2 Block Inclusion typically take on Base?",
  ["~200 milliseconds",
   "~2 seconds",
   "~2 minutes",
   "~20 minutes"], 1)

q("At the L2 Block Inclusion stage, the sequencer has built the transaction into an L2 block and distributed it to:",
  ["The Ethereum L1 contract",
   "Validator nodes",
   "The user's wallet",
   "The bridge contract"], 1)

q("What is the reorg probability for a transaction that has reached L2 Block Inclusion?",
  ["Near 0%",
   "Under 0.001%",
   "Approximately 5%",
   "Between 1-5%"], 0)

q("After L2 Block Inclusion, the transaction has been built into an L2 block and distributed to validator nodes. The reorg probability is:",
  ["Under 0.001%",
   "Near 0%",
   "Under 0.1%",
   "Approximately 0.5%"], 1)

# --- 1.4 Stage 3: L1 Batch Inclusion (~2m) ---
q("What is the third stage of finality for a Base L2 transaction?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "L1 Batch Inclusion",
   "L1 Batch Finality"], 2)

q("How long does L1 Batch Inclusion typically take?",
  ["~200 milliseconds",
   "~2 seconds",
   "~2 minutes",
   "~20 minutes"], 2)

q("At L1 Batch Inclusion, what has occurred?",
  ["The sequencer included the tx in a Flashblock",
   "The Base batch has been posted to Ethereum",
   "The transaction has been distributed to validator nodes",
   "The 7-day challenge period has expired"], 1)

q("A Base batch posted to Ethereum has effectively what level of reorg probability?",
  ["Effectively 0% reorg",
   "Near 0% reorg",
   "Under 0.001% reorg",
   "Under 1% reorg"], 0)

q("What does 'L1 Batch Inclusion' refer to?",
  ["Including a transaction in a preconfirmation block",
   "Posting a Base batch to Ethereum",
   "Waiting for two L1 epochs to pass",
   "Completing the 7-day withdrawal period"], 1)

# --- 1.5 Stage 4: L1 Batch Finality (~20m) ---
q("What is the fourth and final stage of finality for a Base L2 transaction?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "L1 Batch Inclusion",
   "L1 Batch Finality"], 3)

q("How long does L1 Batch Finality take?",
  ["~200 milliseconds",
   "~2 seconds",
   "~2 minutes",
   "~20 minutes"], 3)

q("What condition must be met for a batch to achieve L1 Batch Finality?",
  ["It must be included in a Flashblock",
   "It must be older than 2 epochs (64 L1 blocks)",
   "It must pass the 7-day challenge period",
   "It must be signed by all validators"], 1)

q("Two epochs on Ethereum L1 equals approximately how many L1 blocks?",
  ["32",
   "64",
   "128",
   "256"], 1)

q("At L1 Batch Finality, a batch must be older than:",
  ["1 epoch (32 L1 blocks)",
   "2 epochs (64 L1 blocks)",
   "3 epochs (96 L1 blocks)",
   "4 epochs (128 L1 blocks)"], 1)

# --- 1.6 Stages comparison ---
q("Which stage of finality is the fastest for a Base L2 transaction?",
  ["L1 Batch Finality",
   "L2 Block Inclusion",
   "Flashblock Inclusion",
   "L1 Batch Inclusion"], 2)

q("Which stage of finality takes approximately 20 minutes for a Base L2 transaction?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "L1 Batch Inclusion",
   "L1 Batch Finality"], 3)

q("Arrange the stages of finality from fastest to slowest:",
  ["L1 Batch Inclusion, Flashblock Inclusion, L2 Block Inclusion, L1 Batch Finality",
   "Flashblock Inclusion, L2 Block Inclusion, L1 Batch Inclusion, L1 Batch Finality",
   "L2 Block Inclusion, Flashblock Inclusion, L1 Batch Finality, L1 Batch Inclusion",
   "L1 Batch Finality, L1 Batch Inclusion, L2 Block Inclusion, Flashblock Inclusion"], 1)

q("Which stage of finality involves posting a batch to Ethereum?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "L1 Batch Inclusion",
   "All of the above"], 2)

q("Which two stages of finality are considered to have effectively 0% reorg probability?",
  ["Flashblock Inclusion and L2 Block Inclusion",
   "L2 Block Inclusion and L1 Batch Inclusion",
   "L1 Batch Inclusion and L1 Batch Finality",
   "Flashblock Inclusion and L1 Batch Finality"], 2)

q("The time range from Flashblock Inclusion (~200ms) to L1 Batch Finality (~20m) spans approximately:",
  ["1 minute",
   "5 minutes",
   "20 minutes",
   "7 days"], 2)

# --- 1.7 Deposits and Withdrawals finality ---
q("How long do deposits (transactions from L1 to Base) typically take to finalize?",
  ["~200 milliseconds",
   "~2 seconds",
   "~2 minutes",
   "~7 days"], 2)

q("Deposits from Ethereum to Base finalize in approximately:",
  ["200 milliseconds",
   "2 seconds",
   "2 minutes",
   "20 minutes"], 2)

q("Withdrawals from Base to Ethereum require a challenge period of:",
  ["~2 minutes",
   "~20 minutes",
   "~7 days",
   "~30 days"], 2)

q("The 7-day withdrawal period for Base to Ethereum withdrawals exists for which purpose?",
  ["To give users time to change their minds",
   "To allow the Fault Proof system to provide high security for bridged funds",
   "To batch multiple withdrawals together for efficiency",
   "To accumulate enough fees to cover L1 posting costs"], 1)

q("The 7-day challenge period for withdrawals allows:",
  ["Users to cancel their withdrawal at any time",
   "The Fault Proof system to detect and challenge invalid withdrawals",
   "Validators to vote on the withdrawal",
   "The sequencer to optimize batch ordering"], 1)

# --- 1.8 Reorgs and disputes ---
q("What happens to Base if Ethereum experiences a reorg?",
  ["Base remains unaffected",
   "It can cause a reorg on Base",
   "Base shuts down temporarily",
   "Base increases its block time"], 1)

q("If a challenger wins a dispute game on Base's fault proof system, what can happen?",
  ["The withdrawal is processed faster",
   "The L2 chain can reorg",
   "The challenger receives a penalty",
   "The transaction fee is refunded"], 1)

q("The 7-day period for withdrawals gives the Fault Proof system time to:",
  ["Process the transaction off-chain",
   "Detect and challenge invalid state transitions",
   "Generate the L1 proof",
   "Sync with Ethereum validators"], 1)

q("Which of these could potentially cause a reorg on Base?",
  ["A user sending a large transaction",
   "An Ethereum L1 reorg",
   "A validator going offline",
   "High gas prices on L2"], 1)

q("Which is NOT one of the four stages of finality for Base L2 transactions?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "7-Day Challenge Completion",
   "L1 Batch Inclusion"], 2)

q("Which scenario can trigger a reorg of the L2 chain on Base?",
  ["A challenger winning a dispute game",
   "A user paying too little gas",
   "The sequencer producing blocks too quickly",
   "A L1 batch being posted on time"], 0)

# --- 1.9 More stage-specific questions ---
q("What does a 'Flashblock' refer to on Base?",
  ["A block produced every 2 seconds",
   "A preconfirmation block by the sequencer (~200ms)",
   "A batch posted to Ethereum",
   "A finalized block on L1"], 1)

q("Approximately how much time passes between Flashblock Inclusion and L2 Block Inclusion?",
  ["~200ms",
   "~1.8 seconds (from 200ms to 2s)",
   "~2 minutes",
   "~20 minutes"], 1)

q("Approximately how much time passes between L1 Batch Inclusion and L1 Batch Finality?",
  ["~200ms",
   "~2 seconds",
   "~18 minutes (from 2m to 20m)",
   "~7 days"], 2)

q("Which stage of finality occurs at the ~2 second mark?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "L1 Batch Inclusion",
   "L1 Batch Finality"], 1)

q("A dApp developer wants to show users a confirmation as quickly as possible after sending a transaction. Which stage of finality is sufficient for most user-facing purposes?",
  ["Only L1 Batch Finality",
   "L1 Batch Inclusion or earlier stages since reorg risk is minimal",
   "Only after 7 days",
   "None — Base transactions cannot be considered final"], 1)

q("A trader wants to wait until the reorg probability is effectively 0% before considering a transaction settled. Which stages satisfy this?",
  ["Flashblock Inclusion only",
   "L2 Block Inclusion only",
   "L1 Batch Inclusion and L1 Batch Finality",
   "Only L1 Batch Finality"], 2)

q("What is the reorg probability classification for Flashblock Inclusion?",
  ["Under 0.001%",
   "Near 0%",
   "Effectively 0%",
   "Over 0.1%"], 0)

q("What is the reorg probability classification for L2 Block Inclusion?",
  ["Under 0.001%",
   "Near 0%",
   "Effectively 0%",
   "Under 5%"], 1)

q("What is the reorg probability classification for L1 Batch Inclusion?",
  ["Under 0.001%",
   "Near 0%",
   "Effectively 0%",
   "Under 0.1%"], 2)

q("What is the reorg probability classification for L1 Batch Finality?",
  ["Under 0.001%",
   "Near 0%",
   "Effectively 0%",
   "Under 1%"], 2)

q("Which statement about transaction finality on Base is TRUE?",
  ["All transactions on Base require 7 days to finalize",
   "Regular L2 transactions achieve finality through a series of stages ranging from ~200ms to ~20m",
   "Base transactions never achieve finality because of potential reorgs",
   "Only deposits from Ethereum achieve finality within seconds"], 1)

q("Which statement about the 7-day period on Base is FALSE?",
  ["It applies only to withdrawals from Base to Ethereum",
   "It allows the Fault Proof system to provide security",
   "It applies to all regular L2 token transfers",
   "It exists to protect bridged funds"], 2)

q("Which of the following requires the longest time to achieve finality on Base?",
  ["A regular token swap on a Base DEX",
   "A withdrawal from Base to Ethereum L1",
   "A deposit from Ethereum L1 to Base",
   "An NFT mint on Base"], 1)

q("The four stages of finality on Base apply to which type of transactions?",
  ["Withdrawal transactions only",
   "Deposit transactions only",
   "Regular Base L2 transactions",
   "All transactions including withdrawals"], 2)

# ======================================================================
# TOPIC 2: NETWORK FEES (~70 questions)
# ======================================================================

# --- 2.1 Two-cost structure ---
q("Every Base transaction has how many distinct costs?",
  ["One — the execution fee",
   "Two — an L2 execution fee and an L1 security fee",
   "Three — execution, storage, and data fees",
   "Four — gas, priority, bridge, and protocol fees"], 1)

q("What are the two costs associated with every Base transaction?",
  ["A base fee and a priority fee",
   "An L2 (execution) fee and an L1 (security) fee",
   "A transaction fee and a bridge fee",
   "A protocol fee and a sequencer fee"], 1)

q("The L2 (execution) fee on Base covers:",
  ["The cost of posting the transaction to Ethereum",
   "The cost of executing the transaction on the L2",
   "The cost of bridging assets between chains",
   "The cost of block space on Ethereum"], 1)

q("The L1 (security) fee on Base covers:",
  ["The cost of executing the transaction on the L2",
   "The estimated cost of publishing the transaction on L1",
   "The fee paid to validators for block production",
   "The cost of running the sequencer infrastructure"], 1)

q("Which fee is typically higher for a Base transaction?",
  ["L2 execution fee",
   "L1 security fee",
   "They are always equal",
   "It varies unpredictably based on L2 congestion"], 1)

q("The L1 security fee is typically higher than:",
  ["The withdrawal fee",
   "The bridge fee",
   "The L2 execution fee",
   "The deposit fee"], 2)

# --- 2.2 L1 fee dependency ---
q("The L1 security fee varies with what factor?",
  ["L2 block size",
   "L1 congestion",
   "The number of Base validators",
   "The price of USDC"], 1)

q("When can a user save on the L1 security fee?",
  ["By submitting during low L1 gas",
   "By using a larger gas limit",
   "By adding a higher priority fee",
   "By waiting for a holiday"], 0)

q("Users can save on Base transaction costs by:",
  ["Using a different wallet",
   "Submitting transactions when L1 gas prices are low",
   "Always setting the highest priority fee",
   "Batching transactions through a third-party relayer"], 1)

q("The L1 security fee varies with L1 congestion because:",
  ["Base uses Ethereum for data availability",
   "The sequencer is on L1",
   "L1 validators process Base transactions",
   "ETH is the native gas token of Base"], 0)

# --- 2.3 L2 fee / EIP-1559 ---
q("The L2 execution fee on Base adjusts with demand using which mechanism?",
  ["First-price auction",
   "EIP-1559",
   "A fixed fee schedule",
   "Proof of Work difficulty adjustment"], 1)

q("Base uses EIP-1559 for adjusting which fee?",
  ["The L1 security fee",
   "The L2 execution fee",
   "The bridge fee",
   "The withdrawal fee"], 1)

q("What upgrade introduced the minimum base fee on Base?",
  ["Regolith upgrade",
   "Jovian upgrade",
   "Bedrock upgrade",
   "Canyon upgrade"], 1)

q("The Jovian upgrade introduced which feature to Base?",
  ["Flashblocks",
   "Minimum base fee",
   "Cross-chain messaging",
   "Native account abstraction"], 1)

# --- 2.4 Minimum base fee ---
q("What is the minimum base fee for Base Mainnet?",
  ["500,000 wei (0.0005 gwei)",
   "5,000,000 wei (0.005 gwei)",
   "50,000,000 wei (0.05 gwei)",
   "500,000,000 wei (0.5 gwei)"], 1)

q("The minimum base fee on Base Mainnet is:",
  ["0.0005 gwei",
   "0.005 gwei",
   "0.05 gwei",
   "0.5 gwei"], 1)

q("At ETH=$2000, a minimum base fee of 0.005 gwei for a 200k gas transaction would cost approximately:",
  ["$0.00002",
   "$0.002",
   "$0.02",
   "$0.20"], 1)

q("Which is NOT a benefit of the minimum base fee introduced by the Jovian upgrade?",
  ["Faster transaction inclusion",
   "More predictable fees",
   "Spam prevention",
   "Lower L1 security fees"], 3)

q("The minimum base fee helps prevent what on Base?",
  ["Flashblock creation",
   "Spam transactions",
   "Withdrawal delays",
   "Bridge disputes"], 1)

q("The minimum base fee contributes to faster transaction inclusion by:",
  ["Increasing block size",
   "Discouraging extremely low-fee transactions that delay inclusion",
   "Reducing the number of validators",
   "Bypassing the EIP-1559 mechanism"], 1)

# --- 2.5 EIP-1559 parameters ---
q("What is the Elasticity Multiplier for EIP-1559 on Base?",
  ["2",
   "6",
   "8",
   "12"], 1)

q("What is the Base Fee Change Denominator for EIP-1559 on Base?",
  ["100",
   "125",
   "200",
   "250"], 1)

q("The maximum base fee increase per block on Base is:",
  ["(Elasticity - 1) / Denominator = 4%",
   "Elasticity / Denominator = 4.8%",
   "Denominator / Elasticity = 20.8%",
   "(Elasticity + 1) / Denominator = 5.6%"], 0)

q("The maximum base fee increase per block on Base is approximately:",
  ["1%",
   "2%",
   "4%",
   "8%"], 2)

q("The minimum amount of time to double the base fee on Base is:",
  ["9 blocks × 2s = 18 seconds",
   "18 blocks × 2s = 36 seconds",
   "36 blocks × 2s = 72 seconds",
   "72 blocks × 2s = 144 seconds"], 1)

q("How many blocks are needed at minimum to double the base fee on Base?",
  ["9 blocks",
   "18 blocks",
   "36 blocks",
   "72 blocks"], 1)

q("At a 2-second block time, how long does it take at minimum to double the base fee?",
  ["9 seconds",
   "18 seconds",
   "36 seconds",
   "72 seconds"], 2)

# --- 2.6 GasPriceOracle ---
q("What is the address of the GasPriceOracle predeploy on Base?",
  ["0x420000000000000000000000000000000000000F",
   "0x4200000000000000000000000000000000000010",
   "0x000000000000000000000000000000000000000F",
   "0x4200000000000000000000000000000000000042"], 0)

q("Which contract provides gas price estimation on Base?",
  ["The L1 CrossDomainMessenger",
   "The GasPriceOracle at 0x420000000000000000000000000000000000000F",
   "The BaseFee Vault contract",
   "The Sequencer Fee Vault"], 1)

q("The GasPriceOracle predeploy is located at which address?",
  ["0x420000000000000000000000000000000000000F",
   "0x42000000000000000000000000000000000000F",
   "0x000000000000000000000000000000000000000F",
   "0x42000000000000000000000000000000000000FF"], 0)

q("Which GasPriceOracle method is used for a quick L1 fee estimate before the transaction is fully constructed?",
  ["getL1Fee(bytes)",
   "getL1FeeUpperBound(uint256)",
   "l1BaseFee()",
   "blobBaseFee()"], 1)

q("Which GasPriceOracle method provides the exact L1 fee for a fully RLP-encoded transaction?",
  ["getL1Fee(bytes)",
   "getL1FeeUpperBound(uint256)",
   "l1BaseFee()",
   "baseFeeScalar()"], 0)

q("The getL1FeeUpperBound method is best used when:",
  ["The transaction has already been signed and RLP-encoded",
   "A quick estimate is needed before the transaction is fully constructed",
   "The user wants to know the blob base fee",
   "The user needs to estimate L2 execution costs"], 1)

q("The getL1Fee method is best used when:",
  ["A quick upper bound estimate is needed",
   "The transaction has been fully RLP-encoded and you need the exact fee",
   "The user wants to know the minimum base fee",
   "The developer wants to check L1 congestion"], 1)

q("Which GasPriceOracle method returns the current L1 base fee?",
  ["getL1Fee(bytes)",
   "getL1FeeUpperBound(uint256)",
   "l1BaseFee()",
   "baseFeeScalar()"], 2)

q("Which GasPriceOracle method returns the blob base fee?",
  ["getL1Fee(bytes)",
   "blobBaseFee()",
   "l1BaseFee()",
   "baseFeeScalar()"], 1)

q("Which GasPriceOracle method returns the base fee scalar?",
  ["getL1Fee(bytes)",
   "blobBaseFee()",
   "baseFeeScalar()",
   "getL1FeeUpperBound(uint256)"], 2)

q("Which GasPriceOracle method returns the blob base fee scalar?",
  ["blobBaseFeeScalar()",
   "blobBaseFee()",
   "baseFeeScalar()",
   "getL1FeeUpperBound(uint256)"], 0)

q("How many methods are available on the GasPriceOracle predeploy on Base?",
  ["Three",
   "Four",
   "Five",
   "Six"], 3)

q("The GasPriceOracle predeploy provides methods including:",
  ["getL1Fee, getL1FeeUpperBound, l1BaseFee, blobBaseFee, baseFeeScalar, blobBaseFeeScalar",
   "getL2Fee, getL2FeeUpperBound, l2BaseFee",
   "getBridgeFee, getWithdrawalFee, getDepositFee",
   "estimateGas, gasPrice, maxFeePerGas"], 0)

# --- 2.7 More fee comparison questions ---
q("Which statement about Base transaction fees is TRUE?",
  ["The L2 execution fee is always higher than the L1 security fee",
   "The L1 security fee is typically higher than the L2 execution fee",
   "Both fees are equal for every transaction",
   "Base transactions have no L1 security fee"], 1)

q("The L1 security fee exists on Base because:",
  ["Base pays Ethereum for data availability",
   "Ethereum validators secure the Base chain",
   "The Base sequencer runs on Ethereum",
   "Base is a private blockchain"], 0)

q("Unlike standalone L1 blockchains, Base transactions include an L1 security fee because:",
  ["Base is a Layer-2 that posts transaction data to Ethereum",
   "Base uses Ethereum miners to verify transactions",
   "Base charges extra fees to increase revenue",
   "The L1 fee goes to Base validators as rewards"], 0)

q("What happens to the L1 security fee when Ethereum gas prices are high?",
  ["It decreases to compensate users",
   "It increases because posting data becomes more expensive",
   "It remains unchanged",
   "It is waived entirely"], 1)

q("What happens to the L1 security fee when Ethereum gas prices are low?",
  ["It decreases, making Base cheaper to use",
   "It increases to maintain sequencer revenue",
   "It remains unchanged",
   "It is replaced by an L2 execution fee surcharge"], 0)

q("Which is NOT a method on the GasPriceOracle predeploy?",
  ["getL1Fee",
   "getL1FeeUpperBound",
   "getL1FeeLowerBound",
   "blobBaseFee"], 2)

q("When a user submits a transaction on Base during high L1 congestion periods:",
  ["Only the L2 execution fee increases",
   "The L1 security fee increases due to higher L1 data posting costs",
   "Fees are capped at a maximum amount",
   "The transaction is rejected"], 1)

q("The EIP-1559 mechanism on Base adjusts the L2 execution fee based on:",
  ["L1 gas prices", 
   "L2 demand for block space",
   "The number of active validators",
   "The USDC exchange rate"], 1)

# ======================================================================
# TOPIC 3: THROUGHPUT AND LIMITS (~40 questions)
# ======================================================================

# --- 3.1 Block gas limit ---
q("What is the block gas limit for Base L2 blocks?",
  ["100M gas",
   "200M gas",
   "400M gas",
   "800M gas"], 2)

q("The maximum gas per L2 block on Base is:",
  ["100 million",
   "200 million",
   "400 million",
   "800 million"], 2)

q("Flashblocks on Base have access to what gas budget?",
  ["Half the block gas limit",
   "The full 400M gas block limit",
   "100M gas per Flashblock",
   "Only the remaining gas after the sequencer fee is deducted"], 1)

q("The 400M gas block limit on Base applies to:",
  ["Only the sequencer's blocks",
   "Flashblocks — they have access to the full budget",
   "Only withdrawal transactions",
   "Only L1 batch submissions"], 1)

# --- 3.2 Per-transaction gas limit ---
q("What is the per-transaction gas limit on Base?",
  ["~4.2M",
   "~8.4M",
   "~16.7M",
   "~33.4M"], 2)

q("The per-transaction gas limit of ~16.7M is designed to:",
  ["Fill an entire block in one transaction",
   "Fit in a single Flashblock",
   "Be the maximum allowed by Ethereum",
   "Be half of the block gas limit"], 1)

q("A single transaction on Base can use at most approximately how much gas?",
  ["4.2M",
   "8.4M",
   "16.7M",
   "33.4M"], 2)

q("Why is the per-transaction gas limit set to ~16.7M on Base?",
  ["To match Ethereum's per-transaction limit exactly",
   "To ensure each transaction can fit in a Flashblock",
   "To maximize sequencer revenue per transaction",
   "To allow complex multi-contract interactions"], 1)

# --- 3.3 Target gas per block ---
q("What is the target gas per block on Base?",
  ["~30-40M",
   "~60-70M",
   "~90-100M",
   "~200M"], 1)

q("Blocks on Base target approximately how much gas usage?",
  ["40 million",
   "60-70 million",
   "100 million",
   "200 million"], 1)

q("The target gas per block on Base is achieved via:",
  ["The EIP-1559 elasticity mechanism",
   "The sequencer's manual adjustment",
   "Validator voting on block size",
   "L1 gas price oracle inputs"], 0)

q("The target gas per block of ~60-70M is less than the 400M gas limit because:",
  ["The remaining gas is reserved for bridge transactions",
   "The elasticity mechanism targets a lower utilization to manage fee volatility",
   "Half the block gas is allocated to L1 data posting",
   "The sequencer caps block production at 60-70M"], 1)

# --- 3.4 Block time ---
q("What is the target block time on Base?",
  ["200 milliseconds",
   "2 seconds",
   "12 seconds",
   "2 minutes"], 1)

q("With Flashblocks enabled, Base blocks are produced every:",
  ["200 milliseconds",
   "2 seconds",
   "12 seconds",
   "200 microseconds"], 0)

q("The target block time of 2 seconds on Base compares to Ethereum's block time of approximately:",
  ["2 seconds",
   "12 seconds",
   "15 seconds",
   "20 minutes"], 1)

q("Base blocks are produced faster than Ethereum blocks. Base's target block time is:",
  ["2 seconds vs Ethereum's 12 seconds",
   "200ms vs Ethereum's 2 seconds",
   "12 seconds vs Ethereum's 2 seconds",
   "200ms vs Ethereum's 12 seconds"], 0)

# --- 3.5 Combined throughput questions ---
q("With a 400M gas limit and 2-second block time, Base can process a large amount of transactions. This throughput is further enhanced by:",
  ["Larger per-transaction gas limits",
   "Flashblocks which provide 200ms preconfirmations",
   "Reducing the block gas limit",
   "Increasing the EIP-1559 denominator"], 1)

q("Which parameter determines how much the base fee can increase per block on Base?",
  ["Block gas limit / target gas per block",
   "(Elasticity Multiplier - 1) / Base Fee Change Denominator",
   "Maximum priority fee / minimum base fee",
   "L1 base fee × L2 gas used"], 1)

q("The Elasticity Multiplier of 6 and Base Fee Change Denominator of 125 on Base mean:",
  ["The block can fill up to 6x the target before fees increase sharply",
   "The base fee can never increase",
   "Each block produces 6 transactions maximum",
   "The minimum base fee is multiplied by 125"], 0)

q("If the L2 base fee on Base doubles (minimum 36 seconds at full blocks), this shows:",
  ["The EIP-1559 mechanism responding to high demand",
   "A network failure",
   "The minimum base fee being applied",
   "The L1 security fee overriding the L2 fee"], 0)

q("The combination of 400M gas limit and ~60-70M target gas provides:",
  ["Headroom for sudden demand spikes without extreme fee increases",
   "A hard cap on total transactions per day",
   "A guarantee that fees never increase",
   "A mechanism to reduce block time below 2 seconds"], 0)

q("What is the relationship between Flashblocks (200ms) and the 2-second block time on Base?",
  ["Flashblocks replace the 2-second blocks entirely",
   "Flashblocks provide preconfirmations at 200ms while full L2 blocks are produced every 2 seconds",
   "Flashblocks are unrelated to block production",
   "Flashblocks are only available for high-fee transactions"], 1)

q("How does the per-transaction gas limit of ~16.7M relate to the block gas limit of 400M?",
  ["Approximately 24 transactions could fit in a full block",
   "Exactly 400 transactions could fit in a full block",
   "Only 1 transaction fits per block",
   "The per-transaction limit is irrelevant to the block limit"], 0)

q("Which is NOT a throughput-related parameter on Base?",
  ["Block gas limit of 400M",
   "Per-transaction gas limit of ~16.7M",
   "Target gas per block of ~60-70M",
   "Maximum withdrawal amount of 100 ETH"], 3)

# --- 3.6 More throughput questions ---
q("If a developer deploys a contract that uses 20M gas, what happens on Base?",
  ["The transaction succeeds normally",
   "The transaction is rejected because it exceeds the ~16.7M per-tx gas limit",
   "The transaction uses multiple Flashblocks",
   "The gas limit is automatically increased"], 1)

q("The block gas limit of 400M on Base allows for:",
  ["Very large blocks that can include many transactions or complex operations",
   "Only simple token transfers",
   "Maximum one smart contract interaction per block",
   "Blocks that are smaller than Ethereum's"], 0)

q("At 2-second block times, approximately how many blocks can Base produce per minute?",
  ["5 blocks",
   "15 blocks",
   "30 blocks",
   "60 blocks"], 2)

# ======================================================================
# TOPIC 4: BRIDGING AND WITHDRAWALS (~70 questions)
# ======================================================================

# --- 4.1 Base Bridge ---
q("What is the primary bridge for transferring assets between L1 Ethereum and Base?",
  ["The Solana Bridge",
   "The Base Bridge",
   "The Polygon Bridge",
   "The Arbitrum Bridge"], 1)

q("The Base Bridge enables transfers between:",
  ["Base and Solana",
   "Base and Arbitrum",
   "L1 Ethereum and Base",
   "Base and Optimism"], 2)

q("What type of bridge contracts does the Base Bridge use?",
  ["Custom proprietary bridge contracts",
   "Optimism's standard bridge contracts",
   "Circle's CCTP contracts",
   "Wormhole bridge contracts"], 1)

q("The Base Bridge uses standard bridge contracts from which ecosystem?",
  ["Arbitrum",
   "Optimism",
   "Polygon",
   "zkSync"], 1)

# --- 4.2 Withdrawal period ---
q("How long is the withdrawal period for L2 to L1 transfers on Base?",
  ["~2 minutes",
   "~20 minutes",
   "~7 days",
   "~30 days"], 2)

q("Withdrawals from Base to Ethereum L1 require a waiting period of:",
  ["2 minutes",
   "20 minutes",
   "7 days",
   "14 days"], 2)

q("The 7-day withdrawal period on Base is a security measure that:",
  ["Prevents users from withdrawing too frequently",
   "Allows time for the Fault Proof system to detect invalid withdrawals",
   "Generates interest on the withdrawn funds",
   "Gives the sequencer time to process the request"], 1)

q("Which type of transfer on Base requires a 7-day waiting period?",
  ["L1 to L2 deposits",
   "L2 to L1 withdrawals",
   "L2 to L2 token swaps",
   "L2 NFT transfers"], 1)

# --- 4.3 Deposits ---
q("How long does a deposit from L1 Ethereum to Base typically take?",
  ["~200 milliseconds",
   "~2 seconds",
   "~2 minutes",
   "~7 days"], 2)

q("Deposits from Ethereum to Base are faster than withdrawals because:",
  ["Deposits don't require fault proof validation",
   "Deposits use a different blockchain",
   "Deposits skip the sequencer",
   "Deposits are processed in batches"], 0)

q("A user depositing ETH from Ethereum to Base can expect the funds to arrive in approximately:",
  ["200 milliseconds",
   "2 seconds",
   "2 minutes",
   "20 minutes"], 2)

q("The deposit time of ~2 minutes from L1 to Base is faster than the 7-day withdrawal because:",
  ["Deposits have no challenge period",
   "Deposits use a priority queue",
   "Deposits bypass the EIP-1559 mechanism",
   "Deposits are processed by a separate sequencer"], 0)

# --- 4.4 Solana Bridge ---
q("Which bridge enables transfers between Solana and Base?",
  ["Wormhole",
   "Solana Bridge",
   "CCTP",
   "The Base Bridge"], 1)

q("The Solana Bridge is used for transfers between:",
  ["Ethereum and Base",
   "Solana and Base",
   "Solana and Ethereum",
   "Base and Arbitrum"], 1)

q("Besides Ethereum, Base has a bridge connecting it to which other major blockchain?",
  ["Bitcoin",
   "Solana",
   "Polygon",
   "Avalanche"], 1)

# --- 4.5 CCTP ---
q("CCTP stands for:",
  ["Cross-Chain Transfer Protocol",
   "Cross-Chain Transaction Processing",
   "Cross-Chain Token Protocol",
   "Cross-Chain Transfer Payment"], 0)

q("CCTP is used on Base for transferring which asset cross-chain?",
  ["ETH",
   "USDC",
   "DAI",
   "WBTC"], 1)

q("Circle's CCTP enables:",
  ["Native USDC transfers between supported chains including Base",
   "Any token transfer between any chains",
   "Smart contract calls across chains",
   "NFT bridging between L2s"], 0)

q("Which asset does CCTP specialize in transferring?",
  ["USDC",
   "ETH",
   "BTC",
   "SOL"], 0)

q("CCTP (Cross-Chain Transfer Protocol) works by:",
  ["Locking and minting USDC across supported chains including Base",
   "Wrapping tokens through a bridge contract",
   "Using atomic swaps between users",
   "Batching all transfers through a central relayer"], 0)

# --- 4.6 Fault Proof System ---
q("The 7-day challenge period exists to allow:",
  ["Users to claim refunds",
   "The Fault Proof system to detect and challenge invalid state transitions",
   "Validators to earn staking rewards",
   "The sequencer to batch transactions"], 1)

q("What security mechanism protects bridged funds during the withdrawal window?",
  ["Multi-signature wallets",
   "The Fault Proof system",
   "Insurance funds",
   "Third-party auditors"], 1)

q("If the Fault Proof system detects an invalid withdrawal, it:",
  ["Automatically approves the withdrawal",
   "Challenges it through a dispute game",
   "Routes the withdrawal through a different bridge",
   "Increases the withdrawal fee"], 1)

q("The Fault Proof system on Base is designed to:",
  ["Speed up all transactions",
   "Provide high security for bridged funds by allowing challenges within the 7-day period",
   "Reduce gas fees for all users",
   "Eliminate the need for the Base sequencer"], 1)

q("What happens if a challenger successfully proves a withdrawal is invalid?",
  ["The withdrawal is processed anyway",
   "The L2 chain can reorg to correct the state",
   "The challenger is banned from the network",
   "The withdrawal fee is refunded to the user"], 1)

# --- 4.7 More bridging comparison questions ---
q("Which is faster on Base?",
  ["A withdrawal from Base to Ethereum",
   "A deposit from Ethereum to Base",
   "Both take the same amount of time",
   "Neither is possible on Base"], 1)

q("Deposits to Base (~2 minutes) are faster than withdrawals (~7 days) because:",
  ["Deposits go through a separate high-speed bridge",
   "Deposits don't require fault proof challenge periods since moving value onto an L2 is safe",
   "Deposits bypass the sequencer entirely",
   "Deposits use CCTP while withdrawals use the standard bridge"], 1)

q("Which bridge would you use to transfer USDC between Base and another chain using Circle's infrastructure?",
  ["The Base Bridge",
   "The Solana Bridge",
   "CCTP",
   "LayerZero"], 2)

q("Which would you use to transfer ETH between Ethereum L1 and Base?",
  ["CCTP",
   "The Base Bridge",
   "Solana Bridge",
   "Any DEX on Base"], 1)

q("If a user wants to move USDC from Solana to Base, which bridge should they use?",
  ["The Base Bridge",
   "Solana Bridge",
   "CCTP directly",
   "Any of the above"], 1)

q("The Base Bridge uses Optimism's standard bridge contracts. This means:",
  ["Base's bridge is completely different from Optimism's",
   "Base reuses well-tested bridge infrastructure from the Optimism ecosystem",
   "Base and Optimism share the same liquidity pool",
   "Base cannot operate independently of Optimism's bridge"], 1)

q("Which of the following requires a 7-day challenge period?",
  ["A withdrawal from Base to Ethereum via the Base Bridge",
   "A deposit from Ethereum to Base via the Base Bridge",
   "A USDC transfer from Base to Solana via CCTP",
   "A token swap on a Base DEX"], 0)

q("What distinguishes CCTP from the Base Bridge?",
  ["CCTP is slower than the Base Bridge",
   "CCTP is a Circle-operated protocol for native USDC transfers, while the Base Bridge handles general L1↔L2 transfers",
   "CCTP only works on testnet",
   "The Base Bridge only supports USDC"], 1)

q("Which statement about Base bridging is TRUE?",
  ["The Base Bridge and CCTP serve the same purpose for all tokens",
   "The Base Bridge handles L1↔L2 transfers (any asset) while CCTP handles native USDC cross-chain transfers",
   "CCTP is exclusive to Solana↔Base transfers",
   "The Base Bridge only supports ETH transfers"], 1)

q("Which statement about Base bridging is FALSE?",
  ["Deposits from L1 to Base take approximately 2 minutes",
   "Withdrawals from Base to L1 take 7 days",
   "Deposits from L1 to Base take 7 days",
   "CCTP can be used for USDC transfers"], 2)

q("The Fault Proof system's 7-day challenge period provides high security for:",
  ["All regular L2 transactions",
   "Bridged funds during withdrawal",
   "Flashblock preconfirmations",
   "L1 batch submissions"], 1)

q("The Base Bridge 7-day withdrawal period is a security measure that applies to which direction of transfer?",
  ["L1 to L2 deposits only",
   "L2 to L1 withdrawals only",
   "Both deposits and withdrawals",
   "Neither — the 7-day period applies to all Base transactions"], 1)

# --- Additional finality and comparison questions ---

q("The four stages of finality on Base in order are:",
  ["L2 Block Inclusion, Flashblock Inclusion, L1 Batch Inclusion, L1 Batch Finality",
   "Flashblock Inclusion, L2 Block Inclusion, L1 Batch Inclusion, L1 Batch Finality",
   "L1 Batch Inclusion, L1 Batch Finality, Flashblock Inclusion, L2 Block Inclusion",
   "Flashblock Inclusion, L2 Block Inclusion, L1 Batch Finality, L1 Batch Inclusion"], 1)

q("Which of the following best describes Base's finality model?",
  ["A single instant finality checkpoint",
   "Four increasing stages of finality from ~200ms to ~20 minutes",
   "Probabilistic finality over 7 days",
   "A two-phase commit protocol"], 1)

q("Base L2 transactions achieve different levels of finality depending on:",
  ["The transaction fee paid",
   "How many stages of the finality pipeline have been completed",
   "The size of the transaction",
   "The type of wallet used"], 1)

q("Which finality stage is most appropriate for a merchant accepting on-chain payments on Base?",
  ["Only L1 Batch Finality is acceptable",
   "Flashblock Inclusion or L2 Block Inclusion for most use cases given the near-zero reorg risk",
   "The 7-day withdrawal finality",
   "No stage is sufficient for merchant use"], 1)

q("A user withdrawing $1M USDC from Base to Ethereum should be aware that:",
  ["The transfer is instant and irreversible",
   "The withdrawal will take at least 7 days due to the fault proof challenge period",
   "The withdrawal must be split into multiple transactions",
   "The withdrawal incurs no fees"], 1)

q("Flashblock Inclusion happens at ~200ms. What fraction of a second is 200ms?",
  ["One-tenth",
   "One-fifth",
   "One-half",
   "Three-quarters"], 1)

# --- More fee questions ---
q("The GasPriceOracle predeploy method 'l1BaseFee()' returns:",
  ["The current L1 base fee on Ethereum",
   "The minimum base fee on Base L2",
   "The total fee for a specific transaction",
   "The L2 base fee on Base"], 0)

q("The GasPriceOracle predeploy method 'blobBaseFee()' returns:",
  ["The L2 base fee on Base",
   "The blob base fee for EIP-4844 blob data",
   "The minimum base fee on Base",
   "The priority fee for the next block"], 1)

q("The GasPriceOracle predeploy method 'baseFeeScalar()' returns:",
  ["The scalar used to calculate the L1 fee based on L1 base fee",
   "The L2 base fee value",
   "The minimum base fee in gwei",
   "The EIP-1559 elasticity multiplier"], 0)

q("The GasPriceOracle predeploy method 'blobBaseFeeScalar()' returns:",
  ["The L2 execution fee scalar",
   "The scalar used to calculate the L1 fee based on blob base fee",
   "The minimum priority fee",
   "The withdrawal fee scalar"], 1)

# --- More bridging ---
q("Which bridge infrastructure does Base rely on for L1↔L2 transfers?",
  ["Arbitrum's standard bridge contracts",
   "Optimism's standard bridge contracts",
   "zkSync's standard bridge contracts",
   "Custom proprietary bridge contracts"], 1)

q("The Base Bridge uses standard bridge contracts from Optimism. This means:",
  ["The Base Bridge and Optimism Bridge share the same address",
   "The Base Bridge is built on well-audited, battle-tested code from the OP Stack",
   "Transactions on the Base Bridge must go through Optimism's sequencer",
   "Base bridge fees are set by the Optimism Foundation"], 1)

q("The 7-day withdrawal period on Base protects users by:",
  ["Charging interest on withdrawn funds",
   "Allowing time for the Fault Proof system to verify and challenge the withdrawal",
   "Giving the sequencer time to batch the withdrawal",
   "Running automated security scans on the user's wallet"], 1)

q("If the Fault Proof system identifies an invalid state transition during a withdrawal, what happens?",
  ["The withdrawal is automatically approved to avoid delays",
   "A dispute game is initiated, and if the challenger wins, the L2 chain can reorg",
   "The withdrawal fee is returned to the user",
   "The Base network pauses all transactions"], 1)

# --- Fee comparison questions ---
q("The L1 security fee on Base is important because:",
  ["It pays for Base's sequencer infrastructure",
   "It covers the cost of publishing transaction data to Ethereum for security",
   "It funds the Base developer grants program",
   "It is distributed as rewards to L2 validators"], 1)

q("The L2 execution fee on Base is determined primarily by:",
  ["L1 gas prices",
   "The L2 EIP-1559 mechanism which adjusts based on L2 demand",
   "The number of validators online",
   "The amount of value being transferred"], 1)

q("When Ethereum gas prices spike, Base transactions become:",
  ["Cheaper because users switch to L2",
   "More expensive because the L1 security fee increases",
   "Unaffected — L2 fees are independent of L1",
   "Free — fees are waived during high congestion"], 1)

q("The Jovian upgrade's minimum base fee of 5,000,000 wei helps prevent:",
  ["Withdrawal delays",
   "Economic denial-of-service attacks through spam transactions",
   "Cross-chain messaging failures",
   "Validator stake slashing"], 1)

q("Base's minimum base fee ensures that:",
  ["All transactions cost the same amount",
   "There is a floor price for L2 execution, preventing spam and ensuring predictable fees",
   "The L1 security fee is always lower than the L2 fee",
   "Transactions are processed in FIFO order"], 1)

# --- More finality ---
q("Which of the following about Base finality stages is correct?",
  ["All four stages have the same reorg probability",
   "Reorg probability decreases with each successive stage of finality",
   "Later stages have higher reorg probability than earlier stages",
   "Reorg probability is not relevant for L2 transactions"], 1)

q("Flashblock Inclusion reorg probability is described as 'Under 0.001%'. This means:",
  ["1 in 100 transactions might reorg",
   "Fewer than 1 in 100,000 transactions might reorg",
   "Approximately 1 in 10,000 transactions might reorg",
   "Reorgs are guaranteed to never happen"], 1)

q("L2 Block Inclusion reorg probability is described as 'Near 0%'. This means:",
  ["Reorgs are theoretically possible but extremely unlikely",
   "Reorgs happen approximately 1% of the time",
   "The transaction is guaranteed to never reorg",
   "Reorg probability equals Ethereum's reorg probability"], 0)

# --- More thorough throughput ---
q("Flashblocks on Base allow for:",
  ["Only high-value transactions to be included",
   "Preconfirmation of transactions within ~200ms with access to the full 400M gas block budget",
   "Blocks that are submitted directly to Ethereum",
   "Transactions that skip the EIP-1559 fee mechanism"], 1)

q("The EIP-1559 elasticity mechanism on Base targets approximately how much gas per block?",
  ["200M gas",
   "60-70M gas",
   "400M gas",
   "16.7M gas"], 1)

q("A Base block can use up to 400M gas, but the elasticity mechanism targets ~60-70M gas. The headroom of ~330M gas allows for:",
  ["Higher fees for validators",
   "Sudden demand spikes to be handled without extreme base fee increases",
   "Larger transactions than Ethereum allows",
   "More blocks per second"], 1)

q("The 2-second block time on Base combined with 400M gas limit gives a theoretical maximum throughput of:",
  ["200M gas per second",
   "400M gas per second",
   "200M gas per block",
   "800M gas per second"], 0)  # 400M / 2s = 200M gas per second

q("The block time of 2 seconds on Base means there are approximately how many blocks per day?",
  ["43,200 blocks",
   "7,200 blocks",
   "86,400 blocks",
   "720,000 blocks"], 0)  # 86400 / 2 = 43200

# --- Bridge ecosystem questions ---
q("Which of the following is a valid way to bridge assets to Base from Ethereum?",
  ["Use the Base Bridge which uses Optimism's standard bridge contracts",
   "Only through centralized exchanges",
   "Only through CCTP for all assets",
   "There is no way to bridge assets to Base"], 0)

q("Which of the following is a valid way to bridge USDC to Base from another chain?",
  ["Only the Base Bridge",
   "CCTP for native USDC transfers across supported chains",
   "Only through third-party bridges",
   "USDC cannot be bridged to Base"], 1)

q("The Solana Bridge enables which cross-chain flow?",
  ["Ethereum L1 to Base",
   "Solana to Base",
   "Base to Arbitrum",
   "Optimism to Solana"], 1)

q("CCTP is operated by which company?",
  ["Coinbase",
   "Circle",
   "Optimism",
   "Jump Crypto"], 1)

q("Base was built by which company?",
  ["Optimism Foundation",
   "Coinbase",
   "Ethereum Foundation",
   "Circle"], 1)

# --- More minimum base fee & Jovian ---
q("The Jovian upgrade's minimum base fee of 5,000,000 wei is denominated in:",
  ["ETH",
   "Gwei",
   "Wei",
   "USDC"], 2)

q("At ETH=$2000, the minimum base fee of 0.005 gwei translates to a minimum fee of approximately:",
  ["$0.00002 for a simple transfer",
   "$0.002 for a 200k gas transaction",
   "$0.02 for a typical swap",
   "$0.20 for a complex contract interaction"], 1)

q("5,000,000 wei is equivalent to:",
  ["0.0005 gwei",
   "0.005 gwei",
   "0.05 gwei",
   "0.5 gwei"], 1)

# --- More EIP-1559 ---
q("If the Base Fee Change Denominator is 125, this means the base fee can change by at most:",
  ["1/125th of the current base fee per block (0.8%)",
   "1/125th of the current base fee per block with the elasticity multiplier making the max increase 4%",
   "125 times the current base fee per block",
   "125 wei per block"], 1)

q("The EIP-1559 elasticity multiplier of 6 on Base means:",
  ["The block target can be exceeded by up to 6x before the fee increase formula changes",
   "The base fee is multiplied by 6 every block",
   "6 transactions fit in each block",
   "The block gas limit is 6 times the Ethereum block gas limit"], 0)

q("If L2 demand on Base suddenly spikes, the base fee can increase by at most:",
  ["6% per block",
   "4% per block",
   "12.5% per block",
   "1% per block"], 1)

# --- More stage-specific ---
q("At the Flashblock Inclusion stage, the transaction has been:",
  ["Finalized on Ethereum L1",
   "Included in a preconfirmation block by the sequencer",
   "Distributed to all validator nodes",
   "Posted to an L1 batch"], 1)

q("At the L2 Block Inclusion stage, the transaction has been:",
  ["Included in a preconfirmation block",
   "Built into an L2 block and distributed to validator nodes",
   "Posted to Ethereum as a batch",
   "Finalized after 2 L1 epochs"], 1)

q("At the L1 Batch Inclusion stage, the transaction's batch has been:",
  ["Preconfirmed by the sequencer",
   "Distributed to validator nodes",
   "Posted to Ethereum",
   "Waited for 2 L1 epochs"], 2)

q("At the L1 Batch Finality stage, the batch is:",
  ["Included in a Flashblock",
   "Older than 2 epochs on L1",
   "Newly posted to Ethereum",
   "Awaiting the challenge period"], 1)

# ======================================================================
# BALANCING ADDITIONS — target indices 0, 2, 3
# ======================================================================

q("Which of the following is required for a transaction to achieve L1 Batch Inclusion?",
  ["The Base batch must be posted to Ethereum",
   "The transaction must wait 7 days",
   "The sequencer must include it in a Flashblock",
   "The user must pay an additional bridge fee"], 0)

q("After a transaction achieves L2 Block Inclusion, what is the next stage of finality?",
  ["Flashblock Inclusion",
   "L1 Batch Inclusion",
   "L1 Batch Finality",
   "Withdrawal Finality"], 1)

q("How long does it take for a Base batch to go from being posted to Ethereum (L1 Batch Inclusion) to being considered final (L1 Batch Finality)?",
  ["~200ms",
   "~2 seconds",
   "~18 minutes",
   "~7 days"], 2)

q("The GasPriceOracle predeploy on Base provides developers access to:",
  ["L1 fee estimation methods for understanding the total transaction cost",
   "A live price feed for ETH/USD",
   "Validator selection information",
   "Sequencer uptime statistics"], 0)

q("What is the primary purpose of the L1 security fee on Base?",
  ["To generate profit for the sequencer",
   "To cover the estimated cost of publishing transaction data to Ethereum",
   "To pay Base developers",
   "To fund the Fault Proof system"], 1)

q("Which parameter determines the minimum base fee on Base Mainnet?",
  ["The Jovian upgrade set a minimum base fee of 5,000,000 wei",
   "The EIP-1559 elasticity multiplier",
   "The L1 base fee on Ethereum",
   "Voting by Base validators"], 0)

q("What is the purpose of the per-transaction gas limit of ~16.7M on Base?",
  ["To match Ethereum's block gas limit exactly",
   "To ensure each transaction can fit within a single Flashblock",
   "To limit the total transactions per day",
   "To reduce the computational load on validators"], 1)

q("How does Base's block time compare to Ethereum's block time?",
  ["Base blocks are produced every 2 seconds, much faster than Ethereum's ~12 seconds",
   "Base blocks are produced every 12 seconds, matching Ethereum",
   "Base blocks are produced every 200ms, matching Flashblocks",
   "Base blocks are produced every 20 minutes, much slower than Ethereum"], 0)

q("What security guarantee does the 7-day withdrawal period provide?",
  ["It ensures enough time for the Fault Proof system to detect invalid withdrawals",
   "It guarantees the sequencer collects maximum fees",
   "It allows users to cancel their withdrawal at any point",
   "It enables batch processing to reduce L1 costs"], 0)

q("CCTP (Cross-Chain Transfer Protocol) can be used to transfer USDC between which chains?",
  ["Between any supported chains including Base, Ethereum, Solana, and others",
   "Only between Ethereum and Base",
   "Only between Solana and Base",
   "Only between Ethereum mainnet and testnet"], 0)

q("How does the Fault Proof system protect funds during a Base withdrawal?",
  ["By allowing any participant to challenge invalid withdrawals within the 7-day window",
   "By requiring two-factor authentication from the user",
   "By holding funds in a multi-signature wallet",
   "By auditing all transactions before the bridge processes them"], 0)

q("What is the relationship between the 400M block gas limit and the ~60-70M target gas per block?",
  ["The block gas limit is a hard ceiling; the target is a lower utilization point for stable fee markets",
   "The target is a minimum; blocks must always reach 60-70M gas",
   "The block gas limit and target are identical values",
   "The target is updated every block based on sequencer preference"], 0)

q("Which statement about Flashblock Inclusion is accurate?",
  ["It is the fastest stage of finality, occurring at approximately 200ms",
   "It is the slowest stage of finality, occurring after 7 days",
   "It has the highest reorg probability of all four stages",
   "It only applies to high-value transactions"], 0)

q("A developer building on Base needs to estimate the L1 security fee for a transaction. Which GasPriceOracle method should they use for a quick estimate?",
  ["getL1FeeUpperBound for a quick upper bound estimate before the tx is fully built",
   "getL1Fee for a quick estimate on unsigned transactions",
   "l1BaseFee which returns the complete fee",
   "blobBaseFee which returns the L2 execution fee"], 0)

q("What does it mean that Base's per-transaction gas limit is ~16.7M?",
  ["A single transaction cannot consume more than approximately 16.7M gas",
   "Each block can hold at most 16.7M gas",
   "The maximum transaction fee is 16.7M gwei",
   "A transaction must use at least 16.7M gas to be processed"], 0)

q("Base's EIP-1559 parameters include an Elasticity Multiplier of 6 and a Base Fee Change Denominator of 125. Together these mean:",
  ["The base fee can increase up to 4% per block when blocks are full",
   "The base fee is multiplied by 6 every 125 blocks",
   "The base fee never increases because 6 is less than 125",
   "The base fee doubles every 6 blocks"], 0)

q("The Fault Proof system on Base is designed to protect which type of transaction?",
  ["L2 to L1 withdrawals during the 7-day challenge period",
   "All L2 regular transactions",
   "L1 to L2 deposits",
   "CCTP transfers only"], 0)

q("What is the significance of 64 L1 blocks in Base's finality model?",
  ["A batch must be older than 2 epochs (64 L1 blocks) to achieve L1 Batch Finality",
   "64 L1 blocks equals approximately 7 days",
   "Each L2 batch contains exactly 64 L1 blocks",
   "The sequencer must wait 64 L1 blocks before posting a batch"], 0)

q("Which of the following is NOT a method available on the GasPriceOracle predeploy?",
  ["getL1Fee",
   "getL1FeeUpperBound",
   "getL2FeeEstimate",
   "blobBaseFee"], 2)

q("A user bridges USDC from Solana to Base. Which infrastructure do they use?",
  ["The Solana Bridge for Solana↔Base transfers",
   "The Base Bridge which connects to all chains",
   "CCTP which is restricted to Ethereum↔Base only",
   "An Optimism bridge via a detour through Ethereum"], 0)

q("If Ethereum's L1 base fee increases significantly, how does this affect Base users?",
  ["Their Base transactions cost more because the L1 security fee is higher",
   "Their Base transactions become cheaper as users move to L2",
   "There is no effect — L2 fees are completely independent",
   "Base transactions are rejected until L1 fees drop"], 0)

q("Which of these scenarios describes a correct use of the Base Bridge?",
  ["Transferring ETH from Ethereum L1 to Base (a deposit)",
   "Swapping tokens on a Base DEX",
   "Minting an NFT on Base",
   "Deploying a smart contract to Base"], 0)

q("How does the 7-day withdrawal period on Base compare to the finality of regular L2 transactions?",
  ["Regular L2 transactions finalize in stages from ~200ms to ~20m; only withdrawals have a 7-day wait",
   "Both regular transactions and withdrawals have a 7-day wait",
   "Regular transactions finalize in 7 days; withdrawals finalize instantly",
   "Neither regular transactions nor withdrawals have any wait period"], 0)

q("What happens when a Flashblock is produced?",
  ["The sequencer includes transactions in a preconfirmation block at ~200ms",
   "The full L2 block is finalized on Ethereum",
   "Validators vote on block validity",
   "The 7-day challenge period begins"], 0)

q("The minimum base fee of 5,000,000 wei (0.005 gwei) on Base was introduced by:",
  ["The Jovian upgrade",
   "The Regolith upgrade",
   "The Bedrock upgrade",
   "An Ethereum hard fork"], 0)

q("What is the role of the GasPriceOracle predeploy at 0x420000000000000000000000000000000000000F?",
  ["It provides L1 fee estimation methods for Base transactions",
   "It stores the current ETH/USD price for fee conversion",
   "It manages the sequencer's fee vault",
   "It executes token swaps for gas payments"], 0)

q("If a Base block uses exactly 400M gas (the maximum), what happens to subsequent blocks?",
  ["The base fee increases by up to 4% in the next block due to EIP-1559",
   "The block is automatically split into two blocks",
   "The next block is limited to 200M gas",
   "The sequencer pauses block production for 2 seconds"], 0)

q("Which of the following correctly describes a scenario where Flashblock Inclusion is NOT the finality stage needed?",
  ["A user wants to see their swap result in under a second",
   "A user is withdrawing USDC from Base to Ethereum and should expect a 7-day wait",
   "A dApp shows a transaction as confirmed after the sequencer preconfirms it",
   "A developer considers a transaction final after 200ms"], 1)

q("Which GasPriceOracle method should be called to retrieve the current L1 base fee on Ethereum?",
  ["l1BaseFee()",
   "getL1Fee()",
   "getL1FeeUpperBound()",
   "blobBaseFee()"], 0)

q("The Base Bridge uses standard bridge contracts from which rollup framework?",
  ["Optimism's OP Stack",
   "Arbitrum's Nitro stack",
   "zkSync's Era stack",
   "StarkNet's stack"], 0)

q("Which of the following is NOT a GasPriceOracle method on Base?",
  ["getL1Fee",
   "l1BaseFee",
   "blobBaseFee",
   "getTotalL1Fee"], 3)

q("Why should users submit Base transactions when L1 gas is low?",
  ["The L1 security fee component of Base transactions will be lower",
   "The L2 execution fee is waived during low L1 gas periods",
   "Only high-value transactions are processed when L1 gas is high",
   "Base blocks are produced faster when L1 gas is low"], 0)

q("The 7-day withdrawal challenge period exists because:",
  ["Moving value from L2 to L1 requires security guarantees via the Fault Proof system",
   "The Base sequencer needs time to accumulate enough funds",
   "Ethereum requires a minimum 7-day wait for all cross-chain transfers",
   "Users should have time to reconsider their withdrawal"], 0)

q("What is the difference between L1 Batch Inclusion and L1 Batch Finality?",
  ["L1 Batch Inclusion occurs when the batch is posted (~2m); L1 Batch Finality occurs 2 L1 epochs later (~20m)",
   "They are the same thing with different names",
   "L1 Batch Finality occurs at ~2m; L1 Batch Inclusion occurs at ~20m",
   "L1 Batch Inclusion requires the batch to be older than 2 epochs on L1"], 0)

q("Base's Jovian upgrade introduced a minimum base fee. What problem does this solve?",
  ["Spam prevention and more predictable transaction fees",
   "Reducing the per-transaction gas limit",
   "Increasing the block time",
   "Removing the L1 security fee"], 0)

q("A dApp wants to display a fee breakdown to users. What are the two fee components they should show?",
  ["The L2 execution fee and the L1 security fee",
   "The base fee and the priority fee",
   "The sequencer fee and the validator fee",
   "The deposit fee and the withdrawal fee"], 0)

q("When would a Base user benefit most from using CCTP instead of the Base Bridge?",
  ["When transferring USDC natively between Base and other supported chains without wrapping",
   "When transferring ETH between L1 and Base",
   "When transferring any ERC-20 token between L1 and Base",
   "When performing a token swap on a Base DEX"], 0)

q("The four stages of finality on Base provide:",
  ["Increasing levels of confirmation security from ~200ms to ~20 minutes",
   "Four separate blockchains that each must confirm the transaction",
   "A single checkpoint at the 20-minute mark",
   "A choice between speed and security for each transaction"], 0)

q("What is the minimum base fee in gwei on Base Mainnet?",
  ["0.0005 gwei",
   "0.005 gwei",
   "0.05 gwei",
   "0.5 gwei"], 1)

q("At ETH=$2000, how much would the minimum base fee cost for a 200k gas transaction?",
  ["~$0.0002",
   "~$0.002",
   "~$0.02",
   "~$0.20"], 1)

q("What is the EIP-1559 Base Fee Change Denominator on Base?",
  ["100",
   "125",
   "200",
   "250"], 1)

q("How does depositing from Ethereum to Base (deposit) differ from withdrawing from Base to Ethereum?",
  ["Deposits finalize in ~2 minutes; withdrawals take 7 days due to the fault proof challenge period",
   "Deposits and withdrawals both take 7 days",
   "Deposits take 7 days; withdrawals finalize in ~2 minutes",
   "Both deposits and withdrawals finalize in ~2 minutes"], 0)

q("A Base transaction's L1 security fee varies directly with:",
  ["L1 congestion — when Ethereum gas is high, the L1 security fee increases",
   "L2 block utilization — when L2 is busy, the L1 fee increases",
   "The transaction's gas limit on L2",
   "The number of Base validators"], 0)

q("Which of the following scenarios would NOT trigger a reorg on Base?",
  ["An Ethereum L1 reorg",
   "A challenger winning a dispute game",
   "A user sending a transaction with a low gas price",
   "A successful challenge in the Fault Proof system"], 2)

q("The per-transaction gas limit of ~16.7M on Base is approximately what fraction of the block gas limit?",
  ["1/4 (one quarter)",
   "1/24 (one twenty-fourth)",
   "1/2 (one half)",
   "1/10 (one tenth)"], 1)  # 16.7 / 400 ≈ 1/24

q("If an Ethereum reorg occurs, what could happen to Base?",
  ["Nothing — Base is completely independent of Ethereum's consensus",
   "It can cause a reorg on Base because Base depends on Ethereum for data availability",
   "Base increases its block time to compensate",
   "Base pauses block production until Ethereum stabilizes"], 1)

q("The 7-day withdrawal period allows the Fault Proof system to:",
  ["Process the withdrawal off-chain for faster finality",
   "Provide high security for bridged funds by enabling challenges",
   "Generate interest on the withdrawn amount",
   "Batch multiple withdrawals into a single transaction"], 1)

q("What is the EIP-1559 Elasticity Multiplier on Base?",
  ["2",
   "6",
   "8",
   "12"], 1)  # correctIndex 1

# --- More index 3 targeting ---
q("Which of the following would NOT cause a reorg on Base?",
  ["Ethereum L1 reorg",
   "A successful fault proof challenge",
   "A challenger winning a dispute game",
   "A user paying the minimum base fee"], 3)

q("Which of the following is NOT a valid bridge option for Base?",
  ["The Base Bridge for L1↔L2 transfers",
   "CCTP for native USDC transfers",
   "Solana Bridge for Solana↔Base transfers",
   "Arbitrum Bridge for Arbitrum↔Base transfers"], 3)

q("The Jovian upgrade introduced a minimum base fee. Which benefit does it NOT provide?",
  ["Faster transaction inclusion",
   "More predictable fees",
   "Spam prevention",
   "Lower L1 posting costs"], 3)

q("Which stage of finality is NOT appropriate for a user withdrawing assets from Base to Ethereum?",
  ["Flashblock Inclusion",
   "L2 Block Inclusion",
   "L1 Batch Inclusion",
   "L1 Batch Finality"], 3)

q("Which is NOT a correct statement about Base's block gas limit?",
  ["It is 400M gas per L2 block",
   "Flashblocks use the full 400M budget",
   "It applies to the L2 blocks produced by the sequencer",
   "It is 400M gas per transaction"], 3)

q("Which of the following is NOT a characteristic of Flashblock Inclusion?",
  ["Takes approximately 200ms",
   "Transaction is included in a preconfirmation block",
   "Under 0.001% reorg probability",
   "Requires the transaction to be posted to L1 first"], 3)

q("Which of the following is NOT a method on the GasPriceOracle?",
  ["getL1Fee(bytes)",
   "getL1FeeUpperBound(uint256)",
   "blobBaseFee()",
   "getL2BaseFee()"], 3)

q("Which of the following is NOT a correct fee characteristic of Base?",
  ["Every transaction has an L2 execution fee and an L1 security fee",
   "The L1 security fee is typically higher than the L2 execution fee",
   "The L1 security fee varies with L1 congestion",
   "The L2 execution fee is always higher than the L1 security fee"], 3)

q("Which is NOT an intended benefit of the minimum base fee on Base?",
  ["Faster tx inclusion",
   "More predictable fees",
   "Spam prevention",
   "Elimination of the L1 security fee"], 3)

q("Which of the following is NOT a bridge or protocol available on Base?",
  ["Base Bridge for L1↔L2 transfers",
   "Solana Bridge for Solana↔Base transfers",
   "CCTP for native USDC transfers",
   "zkSync Bridge for zkSync↔Base transfers"], 3)

q("Which statement about Base finality is FALSE?",
  ["Regular L2 transactions do NOT need to wait 7 days",
   "Withdrawals from Base to Ethereum must wait 7 days",
   "There are four stages of finality for L2 transactions",
   "All Base transactions require a 7-day wait to be considered final"], 3)

q("Which of the following is NOT a valid GasPriceOracle method?",
  ["getL1Fee",
   "getL1FeeUpperBound",
   "l1BaseFee",
   "estimateL1Fee"], 3)

q("What is NOT a factor in determining the L1 security fee on Base?",
  ["L1 congestion",
   "Ethereum base fee",
   "Transaction data size",
   "The number of Base validators online"], 3)

# --- More index 0, 2, 3 targeting ---
q("The Flashblock Inclusion stage of finality provides:",
  ["The fastest possible preconfirmation at ~200ms with very low reorg risk",
   "The highest security guarantee of any stage",
   "A guarantee the transaction will never reorg",
   "Finality equivalent to L1 settlement"], 0)

q("Base's block time of 2 seconds means the network produces approximately:",
  ["30 blocks per minute",
   "5 blocks per minute",
   "60 blocks per minute",
   "120 blocks per minute"], 0)

q("Which is NOT a characteristic of the four-stage finality model on Base?",
  ["Each stage provides increasing security",
   "All transactions must pass through all four stages",
   "Reorg probability decreases at each stage",
   "Regular L2 transactions progress through stages from ~200ms to ~20m"], 1)

q("The relationship between Base and Ethereum for the L1 security fee is that:",
  ["Base users pay an estimated cost to publish their transaction data on Ethereum",
   "Base is a fork of Ethereum so there are no L1 fees",
   "Ethereum pays Base a subsidy for each transaction",
   "L1 fees are waived for Base users"], 0)

q("What BEST describes the Fault Proof system on Base?",
  ["A mechanism that allows challenges to invalid L2 state transitions within a 7-day window",
   "A system that automatically rejects all withdrawals",
   "A software tool for proving Solidity code correctness",
   "A validator that double-checks every L2 transaction before inclusion"], 0)

q("The Base Bridge was built using Optimism's standard bridge contracts. This benefits Base because:",
  ["It leverages well-audited and battle-tested bridge infrastructure",
   "It allows Base and Optimism to share a single bridge",
   "It means Base cannot customize its bridge logic",
   "It requires Optimism to process all Base withdrawals"], 0)

q("If a Base block reaches capacity (400M gas) and stays full for 18 consecutive blocks, what happens to the base fee?",
  ["The base fee doubles (increases by ~4% each block for 18 blocks)",
   "The base fee stays the same",
   "The base fee decreases to encourage more usage",
   "The base fee is reset to the minimum"], 0)

q("Which of the following is NOT true about withdrawal transactions on Base?",
  ["They must wait 7 days to finalize",
   "They are protected by the Fault Proof system",
   "They have the same finality stages as regular L2 transactions",
   "They move value from Base back to Ethereum L1"], 2)

q("The getL1FeeUpperBound method on the GasPriceOracle is useful for:",
  ["Getting a quick estimate before fully constructing a transaction, to judge affordability",
   "Calculating the exact fee for a signed transaction",
   "Estimating the L2 execution fee only",
   "Retrieving the minimum base fee"], 0)

q("EIP-1559 on Base adjusts the L2 base fee based on:",
  ["Block utilization — when blocks are above target, the base fee increases",
   "L1 gas prices — when L1 is expensive, the L2 fee adjusts",
   "Validator voting — validators decide the fee each block",
   "User tips — the base fee is the median of all tips received"], 0)

q("Which of the following is NOT affected by the Jovian upgrade's minimum base fee?",
  ["Transaction inclusion speed",
   "Fee predictability",
   "Spam resistance",
   "The 7-day withdrawal period"], 3)

q("The Solana Bridge for Base enables:",
  ["Asset transfers between Solana and Base",
   "L1 Ethereum to Base deposits",
   "Base to Arbitrum transfers",
   "Optimism to Base transfers"], 0)

q("When blocks are full on Base, the EIP-1559 mechanism responds by:",
  ["Increasing the base fee up to 4% per block until demand subsides or the target is met",
   "Reducing the block time to fit more transactions",
   "Pausing non-essential transactions",
   "Splitting blocks into smaller Flashblocks"], 0)

q("Which of the following is NOT part of Base's fee model?",
  ["L2 execution fee (paid to L2 validators/sequencer)",
   "L1 security fee (estimated L1 posting cost)",
   "Minimum base fee (5,000,000 wei)",
   "Validator staking fee (paid to L1 validators)"], 3)

q("The 64 L1 block threshold for L1 Batch Finality corresponds to approximately:",
  ["20 minutes on Ethereum at 12-second block times",
   "2 minutes on Ethereum",
   "7 days on Ethereum",
   "200ms on Ethereum"], 0)

# --- Final balancing batch ---
q("Which of the following correctly links the finality stage with its time?",
  ["Flashblock Inclusion ~200ms, L2 Block Inclusion ~2s, L1 Batch Inclusion ~2m, L1 Batch Finality ~20m",
   "Flashblock Inclusion ~2s, L2 Block Inclusion ~200ms, L1 Batch Inclusion ~20m, L1 Batch Finality ~2m",
   "Flashblock Inclusion ~20m, L2 Block Inclusion ~2m, L1 Batch Inclusion ~2s, L1 Batch Finality ~200ms",
   "Flashblock Inclusion ~2m, L2 Block Inclusion ~20m, L1 Batch Inclusion ~200ms, L1 Batch Finality ~2s"], 0)

q("Which is NOT a factor considered when the GasPriceOracle calculates the L1 fee?",
  ["The current L1 base fee",
   "The scalar values (baseFeeScalar, blobBaseFeeScalar)",
   "The transaction data or blob data",
   "The L2 priority fee paid by the user"], 3)

q("A withdrawal from Base to Ethereum requires the 7-day challenge period because:",
  ["The Fault Proof system needs time to detect any invalid state transitions before funds are released",
   "The Ethereum L1 takes 7 days to confirm L2 block data",
   "The Base sequencer produces one block every 7 days for withdrawals",
   "CCTP requires all USDC transfers to wait 7 days"], 0)

q("The EIP-1559 elasticity mechanism on Base (Elasticity = 6, Denominator = 125) means that a block at full 400M gas would:",
  ["Increase the base fee by at most 4% in the next block since the target is exceeded",
   "Decrease the base fee by 50% since the block is too full",
   "Have no effect on the base fee",
   "Reset the base fee to the minimum"], 0)

q("Which of the following is NOT a difference between regular L2 transactions and withdrawal transactions on Base?",
  ["Regular L2 transactions finalize in minutes; withdrawals take 7 days",
   "Regular L2 transactions have four stages of finality; withdrawals have a different process",
   "Regular L2 transactions use the L2 EIP-1559 fee mechanism; withdrawals use a separate fee schedule",
   "Regular L2 transactions can be seen instantly in the user's wallet; withdrawals require waiting"], 2)

q("The Solana Bridge, Base Bridge, and CCTP are all examples of:",
  ["Cross-chain transfer infrastructure available on Base",
   "L1 Ethereum protocols",
   "Base-native DEX platforms",
   "EIP-1559 fee mechanisms"], 0)

q("Which is a valid way for a developer to estimate the L1 security fee component of a Base transaction?",
  ["Calling getL1FeeUpperBound with a gas limit estimate before the tx is built",
   "Taking the L2 gas limit and multiplying by the L2 base fee",
   "Checking the Base Bridge contract for fee schedules",
   "Using the eth_estimateGas RPC method"], 0)

q("Flashblock Inclusion's 'Under 0.001% reorg probability' means the chance of a reorg is:",
  ["Extremely low — less than 1 in 100,000",
   "Moderate — about 1 in 1,000",
   "High — about 1 in 100",
   "Certain — every Flashblock eventually reorgs"], 0)

q("The Fault Proof system's 7-day challenge period is a security feature that:",
  ["Protects bridged funds by allowing invalid withdrawals to be disputed before finalization",
   "Slows down the bridge to reduce network congestion",
   "Ensures the sequencer has enough time to batch all withdrawals",
   "Charges users interest for the duration of the wait"], 0)

q("Which of the following is NOT a valid statement about Base's EIP-1559 parameters?",
  ["Elasticity Multiplier = 6",
   "Base Fee Change Denominator = 125",
   "Max base fee increase per block = 4%",
   "Minimum base fee = 0.5 gwei"], 3)

q("What makes the L1 security fee on Base variable?",
  ["It depends on L1 congestion — when Ethereum gas is expensive, posting data costs more",
   "It is voted on by Base token holders every block",
   "It depends on how many validators are online",
   "It is set by the Base sequencer based on profitability targets"], 0)

q("The 2-second block time on Base compared to Ethereum's 12-second block time means:",
  ["Base can produce 6 blocks for every 1 Ethereum block",
   "Base produces 12 blocks for every 1 Ethereum block",
   "Base is faster but produces smaller blocks",
   "Base blocks contain fewer transactions than Ethereum blocks"], 0)

# --- Final index-3 and index-2 balancing ---
q("Which of the following is NOT a valid comparison between Flashblock Inclusion and L2 Block Inclusion?",
  ["Flashblock is ~200ms; L2 Block is ~2s",
   "Flashblock is a sequencer preconfirmation; L2 Block is distributed to validators",
   "Flashblock has under 0.001% reorg risk; L2 Block has near 0% reorg risk",
   "Flashblock requires L1 posting; L2 Block does not"], 3)

q("The EIP-1559 target gas per block on Base of ~60-70M is designed to:",
  ["Maintain stable base fee levels at typical usage while allowing bursts up to 400M",
   "Ensure blocks are never more than 70M gas",
   "Force some transactions to wait for future blocks",
   "Match Ethereum's 30M gas target exactly"], 0)

q("Which is NOT a valid statement about the GasPriceOracle?",
  ["It is a predeploy at 0x420000000000000000000000000000000000000F",
   "It provides 6 methods for fee estimation",
   "It can estimate both L1 and L2 fees",
   "It returns the current ETH/USD price for fee conversion"], 3)

q("The Fault Proof system on Base operates during the 7-day withdrawal window by:",
  ["Allowing anyone to challenge the validity of a withdrawal, triggering a dispute game",
   "Automatically rejecting all withdrawals above $10,000",
   "Requiring multi-sig approval for every withdrawal",
   "Running automated checks every hour"], 0)

q("The L2 execution fee on Base adjusts dynamically using EIP-1559. What is the purpose of this adjustment?",
  ["To match L2 demand — fees rise when blocks are full and fall when they are not",
   "To keep fees exactly the same for every transaction",
   "To always charge the maximum possible fee",
   "To match L1 gas prices exactly"], 0)

q("Which of the following is NOT a correct application of the Base Bridge?",
  ["Depositing ETH from L1 Ethereum to Base (~2 min finality)",
   "Withdrawing USDC from Base to L1 Ethereum (7-day challenge period)",
   "Transferring USDC from Solana to Base",
   "Swapping tokens on a Base DEX"], 3)

q("The 400M gas block limit on Base with a 2-second block time provides:",
  ["High throughput capacity with room for demand spikes",
   "Exactly the same throughput as Ethereum",
   "Lower throughput than most L2s",
   "Enough space for one complex transaction per block"], 0)

q("The 'minimum base fee' introduced by the Jovian upgrade means:",
  ["The L2 base fee cannot go below 5,000,000 wei, preventing spam and ensuring reliable inclusion",
   "All transactions must pay at least $1 in fees",
   "The L1 security fee has a minimum of 5,000,000 wei",
   "The base fee is fixed at 5,000,000 wei and never changes"], 0)

q("A Base transaction at the Flashblock Inclusion stage (200ms) has a reorg probability described as:",
  ["Under 0.001%",
   "Under 0.01%",
   "Under 0.1%",
   "Under 1%"], 0)

q("The difference between getL1Fee and getL1FeeUpperBound on the GasPriceOracle is:",
  ["getL1FeeUpperBound gives a quick upper estimate; getL1Fee gives the exact fee for a fully RLP-encoded tx",
   "getL1Fee is faster; getL1FeeUpperBound is more accurate",
   "getL1Fee works for L2 fees; getL1FeeUpperBound works for L1 fees",
   "They are the same method with different names"], 0)

q("Which is NOT a true statement about Base's relationship with Ethereum?",
  ["Base posts transaction batches to Ethereum for data availability",
   "An Ethereum L1 reorg can cause a reorg on Base",
   "Base uses Ethereum for its security via L1 batch publication",
   "Base withdrawals complete in ~2 minutes like deposits"], 3)

q("A Base user wants to minimize transaction costs. Which strategy would help?",
  ["Submitting transactions when L1 gas prices are low to reduce the L1 security fee",
   "Using a different wallet that charges lower fees",
   "Always sending large amounts per transaction",
   "Submitting transactions during peak L2 hours for faster inclusion"], 0)

q("When a withdrawal from Base to Ethereum completes the 7-day challenge period without any valid challenges:",
  ["The withdrawal is considered final and the funds are released on L1",
   "The withdrawal must wait another 7 days",
   "The withdrawal is automatically cancelled",
   "The user must restart the withdrawal process"], 0)

# ======================================================================
# FINAL: Shuffle and write
# ======================================================================

# Shuffle questions for variety
random.shuffle(questions)

# Check distribution and adjust if needed
dist = Counter(q['correctIndex'] for q in questions)
print(f"Before balancing: {dict(sorted(dist.items()))}")

# Assign sequential IDs
out = {
    "meta": {
        "ecosystem": "Base",
        "batchId": "base-2026-07-11-batch2",
        "generatedAt": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totalQuizzes": len(questions),
        "questionsPerSession": 5
    },
    "quizzes": [
        {"id": i, **{k: v for k, v in q.items() if k != 'id'}}
        for i, q in enumerate(questions)
    ]
}

output_path = "/home/elmardi/Documents/Web3/quizonchain/data/quizzes-base-batch2.json"
with open(output_path, 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

final_dist = Counter(q['correctIndex'] for q in out['quizzes'])
print(f"Total: {len(out['quizzes'])} questions")
print(f"Final correctIndex distribution: {dict(sorted(final_dist.items()))}")
print(f"Output written to: {output_path}")
