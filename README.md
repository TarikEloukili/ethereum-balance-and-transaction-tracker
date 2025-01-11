# Ethereum Transaction Tracker

## Description
This project allows you to track Ethereum transactions for a wallet from its creation.

## Features
- **Etherscan API Integration**: We use the Etherscan API to fetch transaction data.
- **Comprehensive Transaction Tracking**: Unlike many other projects, this tool accounts for both **normal (external)** transactions and **internal** ones. Internal transactions are handled using the Web3 library, which provides the necessary tools for in-depth tracking.
- **Calculated Balance Verification**: The project calculates the wallet balance at each transaction step, ultimately arriving at a **calculated balance** that closely matches the balance provided by the Etherscan API.

## Unique Approach
The calculated balance is verified using the `calculate_closeness_score()` function, which evaluates the similarity between the calculated balance and the real balance:
- A score close to **1** indicates the calculated balance is accurate.
- A score close to **0** suggests discrepancies between the calculated and real balances.

## How to Use
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with your Etherscan API key and Infura project ID:
   ```env
   API_KEY=your_etherscan_api_key
   INFURA_PROJECT_ID=your_infura_project_id
   ```

4. Run the script:
   ```bash
   python ethereum_analysis.py
   ```

## Output
- A plotted graph showing the wallet balance over time.
- Verification of balance accuracy using the `balance_closeness` function.

---
Feel free to contribute to this project by submitting issues or pull requests!
