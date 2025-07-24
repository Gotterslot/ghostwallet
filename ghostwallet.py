import requests
import time

ETHERSCAN_API = "https://api.etherscan.io/api"


class GhostWalletScanner:
    def __init__(self, api_key: str, verbose: bool = False):
        self.api_key = api_key
        self.verbose = verbose

    def log(self, msg):
        if self.verbose:
            print(msg)

    def get_transactions(self, address: str):
        self.log(f"Fetching transactions for {address}...")
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "asc",
            "apikey": self.api_key,
        }
        response = requests.get(ETHERSCAN_API, params=params)
        data = response.json()
        if data["status"] != "1":
            self.log(f"No transactions found or error: {data.get('message')}")
            return []
        return data["result"]

    def get_balance(self, address: str):
        params = {
            "module": "account",
            "action": "balance",
            "address": address,
            "tag": "latest",
            "apikey": self.api_key,
        }
        response = requests.get(ETHERSCAN_API, params=params)
        data = response.json()
        return int(data["result"]) / 1e18  # ETH

    def is_ghost_wallet(self, address: str):
        txs = self.get_transactions(address)
        if not txs:
            return False  # нет истории
        received = any(tx["to"].lower() == address.lower() for tx in txs)
        balance = self.get_balance(address)
        return received and balance == 0

    def scan_list(self, addresses):
        ghost_wallets = []
        for addr in addresses:
            try:
                if self.is_ghost_wallet(addr):
                    ghost_wallets.append(addr)
                    self.log(f"👻 Ghost wallet found: {addr}")
                else:
                    self.log(f"✓ {addr} is not a ghost wallet.")
                time.sleep(0.25)  # API rate limit
            except Exception as e:
                self.log(f"Error scanning {addr}: {e}")
        return ghost_wallets
