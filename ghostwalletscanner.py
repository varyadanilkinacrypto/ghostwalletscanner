import time
from datetime import datetime, timedelta

from web3 import Web3

class GhostWalletScanner:
    def __init__(self, provider_url, min_balance_eth=1.0, inactivity_days=365):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.min_balance_wei = self.w3.to_wei(min_balance_eth, 'ether')
        self.inactivity_cutoff = int(time.time()) - inactivity_days * 86400

    def is_address_active(self, address):
        tx_count = self.w3.eth.get_transaction_count(address)
        return tx_count > 0

    def get_last_tx_timestamp(self, address):
        try:
            # Get internal txs via Etherscan (or your preferred method)
            # Here, we're simulating a method stub – for real-world usage,
            # you'd need a third-party indexer API or archive node
            return None
        except:
            return None

    def is_ghost_wallet(self, address):
        if not self.w3.is_address(address):
            return False

        balance = self.w3.eth.get_balance(address)
        if balance < self.min_balance_wei:
            return False

        # Here, we assume using external APIs or archive node
        last_tx = self.get_last_tx_timestamp(address)
        if last_tx is None:
            return False

        return last_tx < self.inactivity_cutoff

    def scan_addresses(self, address_list):
        ghosts = []
        for addr in address_list:
            print(f"Scanning {addr}...")
            try:
                if self.is_ghost_wallet(addr):
                    ghosts.append(addr)
            except Exception as e:
                print(f"Error with {addr}: {e}")
        return ghosts
