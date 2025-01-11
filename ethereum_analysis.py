from requests import get
from matplotlib import pyplot as plt
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
#create an account on etherscan.io and get your API key:etherscan.io
API_KEY = os.getenv("API_KEY")
#you can also use Infura to get the transaction details: infura.io
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")


BASE_URL = "https://api.etherscan.io/api"
ETHER_VAL = 10**18

def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}"
    for key, value in kwargs.items():
        url += f"&{key}={value}"
    return url

def get_account_balance(address):
    balance_url = make_api_url("account", "balancemulti", address, tag="latest", apikey=API_KEY)
    response = get(balance_url)
    data = response.json()
    balance = int(data["result"][0]["balance"]) / ETHER_VAL
    return balance

def get_transaction_details(tx_hash):
    tx_url = f"{BASE_URL}?module=proxy&action=eth_getTransactionByHash&txhash={tx_hash}&apikey={API_KEY}"
    response = get(tx_url)
    tx_data = response.json()

    if "result" in tx_data and tx_data["result"]:
        return tx_data["result"]
    else:
        raise ValueError(f"Transaction details not found for {tx_hash}")

def get_external_transactions(address):
    transaction_url = make_api_url("account", "txlist", address, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc", apikey=API_KEY)
    response = get(transaction_url)
    data = response.json()["result"]

    internal_tx_url = make_api_url("account", "txlistinternal", address, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc", apikey=API_KEY)
    response2 = get(internal_tx_url)
    data2 = response2.json()["result"]

    data.extend(data2)
    data.sort(key=lambda x: int(x['timeStamp']))

    current_balance = 0
    balances = []
    times = []

    for tx in data:
        if "gasPrice" in tx:
            gas_cost = int(tx["gasUsed"]) * int(tx["gasPrice"]) / ETHER_VAL
        else:
            tx_hash = tx["hash"]
            parent_tx = get_transaction_details(tx_hash)
            gas_price_wei = int(parent_tx["gasPrice"], 16)  
            gas_cost = int(tx["gasUsed"]) * gas_price_wei / ETHER_VAL

        from_addr = tx["from"]
        to = tx["to"]
        value = int(tx["value"]) / ETHER_VAL
        time_stamp = datetime.fromtimestamp(int(tx["timeStamp"]))

        money_in = to.lower() == address.lower()
        money_out = from_addr.lower() == address.lower()

        if money_in:
            current_balance += value
        elif money_out:
            current_balance -= value + gas_cost

        balances.append(current_balance)
        times.append(time_stamp)

    return current_balance, times, balances
    


    
######## Evaluate Score ########

def calculate_closeness_score(real_balance, calculated_balance):

    if real_balance == 0:  
        return 0 if calculated_balance != 0 else 1
    score = 1 - abs(real_balance - calculated_balance) / abs(real_balance)
    return max(0, score)  



######## Ethereum address to analyze: ########

ADDRESS = "0x2B6eD29A95753C3Ad948348e3e7b1A251080Ffb9"


real_balance = get_account_balance(ADDRESS)
print(f"Account Balance: {real_balance} ETH")


calculated_balance = get_external_transactions(ADDRESS)[0]
print(f"Calculated Balance: {calculated_balance} ETH")


print(f"Closeness Score: {calculate_closeness_score(real_balance, calculated_balance)}")


times = get_external_transactions(ADDRESS)[1]
balances = get_external_transactions(ADDRESS)[2]


plt.plot(times, balances)
plt.xlabel("Time")
plt.ylabel("Balance (ETH)")
plt.title("Ethereum Balance Over Time")
plt.show()