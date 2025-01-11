# Ethereum Transaction Tracker

## Description
This project allows you to track Ethereum transactions for a wallet from its creation.

## Features
- **Etherscan API Integration**: We use the Etherscan API to fetch transaction data.
- **Comprehensive Transaction Tracking**: Unlike many other projects, this tool accounts for both **normal (external)** transactions and **internal** ones.
- **Calculated Balance Verification**: The project calculates the wallet balance at each transaction step, ultimately arriving at a **calculated balance** that closely matches the balance provided by the Etherscan API.

The calculated balance is verified using the `calculate_closeness_score()` function, which evaluates the similarity between the calculated balance and the real balance:
- A score close to **1** indicates the calculated balance is accurate.
- A score close to **0** suggests discrepancies between the calculated and real balances.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/TarikEloukili/ethereum-balance-and-transaction-tracker.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with your Etherscan API key and Infura project ID:
   ```env
   #create an account on 'etherscan.io' and get your API key:
   API_KEY="your_etherscan_api_key"
   
   #create an account on 'infura.io' and get your API key:
   INFURA_PROJECT_ID="your_infura_project_id"
   ```

4. Run the script:
   ```bash
   python ethereum_analysis.py
   ```

## Output
- A real account's balance given by the etherscan api
- A calculated balance
- Verification of balance accuracy using the `calculate_closeness_score()` function.
- A plotted graph showing the wallet balance over time.


---
Feel free to contribute to this project by submitting issues or pull requests!
