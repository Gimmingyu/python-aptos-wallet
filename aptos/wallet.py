from bitcoinlib.wallets import Wallet, wallet_delete, wallet_delete_if_exists
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.keys import HDKey

# Generate a 12-word mnemonic seed
mnemonic = Mnemonic().generate(strength=128)
print("Mnemonic seed:", mnemonic)

# Create a master private key from the mnemonic seed
master_private_key = HDKey.from_seed(mnemonic, key_type="bip32")
print("Master private key:", master_private_key.wif())

# Create an HD Wallet
if wallet_delete_if_exists('MyHDWallet'):
    pass

if wallet_delete_if_exists('new wallet'):
    pass

if wallet_delete_if_exists('test'):
    pass

wallet = Wallet.create("MyHDWallet", keys=master_private_key)



# Generate addresses
number_of_addresses = 5
for i in range(number_of_addresses):
    key = wallet.get_key()
    print(f"Address {i + 1}: {key.address}")
