import bitcoinlib.wallets
from bitcoinlib.wallets import wallet_delete_if_exists
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
from utils import *
from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient

# FAUCET_URL = 'https://faucet.devnet.aptoslabs.com'
FAUCET_URL = 'https://faucet.testnet.aptoslabs.com'

NODE_URL = 'https://fullnode.testnet.aptoslabs.com/v1'


# NODE_URL = 'https://fullnode.devnet.aptoslabs.com/v1'


class HDWallet:
    master: PublicKeyUtils
    mnemonic: str
    _private_key: HDKey

    """
    master : master key which is generated from mnemonic
    rest_client : client for connect with nodes
    faucet_client : client for faucet(dev,test only)
    """

    def __init__(self):
        self.mnemonic = Mnemonic(language='english').generate()
        pt = PublicKeyUtils(self.mnemonic)
        self.master = pt
        self.rest_client = RestClient(NODE_URL)

    def generate_derived_wallet(self, index: int) -> Account:
        path = f"m/44'/637'/0'/0/{index}\n"
        pt = PublicKeyUtils(self.mnemonic, path)
        return Account.load_key(pt.private_key.hex())

    def get_balance(self, address: str) -> str:
        return f"{self.rest_client.account_balance(account_address=address)}"

    def transfer(self, from_address: str, to_address: str, amount: str):
        pass
