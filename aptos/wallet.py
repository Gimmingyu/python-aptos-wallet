from bitcoinlib.wallets import Wallet, wallet_delete, wallet_delete_if_exists
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.keys import HDKey


class HDWallet:

    wallet: Wallet
    mnemonic: str
    _private_key: HDKey

    def __init__(self, name: str):
        self.mnemonic = Mnemonic().generate(strength=128)
        self._private_key = HDKey.from_seed(self.mnemonic, key_type="bip32")
        wallet_delete_if_exists(name)
        self.wallet = Wallet.create(name, keys=self._private_key)
        self.__str__()

    def generate_derived_wallet(self, path: str):
        pass

    def __str__(self):
        print(f'Mnemonic : {self.mnemonic}')
        print(f'Private Key : {self._private_key}')
        print(f'Wallet ID : {self.wallet.wallet_id}')
        print(f'Dictionary : {self.wallet.as_dict(True)}')

    @property
    def private_key(self):
        return self._private_key

    @private_key.setter
    def private_key(self, value):
        self._private_key = value
