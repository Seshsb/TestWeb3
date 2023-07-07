from typing import Union, Dict

from web3 import Web3
from web3.middleware import geth_poa_middleware

from config import MUMBAI_MATIC_TEST_URL, WALLET_ADDRESS, PRIVATE_KEY
from utils import delete_exp


class Transaction:
    def __init__(self, url: str, w_address: str, private_key: str):
        self.web3 = Web3(Web3.HTTPProvider(url))
        self.wallet_address = w_address
        self.private_key = private_key

    @staticmethod
    def _build_transaction(web3: Web3, from_address: str, to_address: str, amount: Union[int, float], *args) \
            -> Dict[str, Union[str, int]]:

        gas_price = web3.eth.gas_price
        gas = 2500000
        nonce = web3.eth.get_transaction_count(from_address)
        txn = {
            'chainId': web3.eth.chain_id,
            'from': from_address,
            'to': to_address,
            'value': int(Web3.to_wei(amount, 'ether')),
            'nonce': nonce,
            'gasPrice': gas_price,
            'gas': gas
        }
        return txn

    def send_transaction(self, to_address: str, amount: Union[int, float]):
        transaction = self._build_transaction(web3=self.web3, from_address=self.wallet_address,
                                              to_address=to_address, amount=amount)
        sign_transaction = self.web3.eth.account.sign_transaction(transaction, self.private_key)
        transaction_send = self.web3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        hex_transaction = transaction_send.hex()
        return self.web3.eth.get_transaction(hex_transaction)


tnx = Transaction(MUMBAI_MATIC_TEST_URL, WALLET_ADDRESS, PRIVATE_KEY)
print(tnx.send_transaction('0x4Ba760E5361cf7c9031698ea6dF979a9e989e869', 0.333))
