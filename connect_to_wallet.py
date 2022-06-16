from terra_sdk.client.lcd import LCDClient
from terra_sdk.key.mnemonic import MnemonicKey

terra = LCDClient(chain_id="phoenix-1", url="https://phoenix-lcd.terra.dev")
wallet_mnemonic = "mountain cancel buddy wood borrow copper stomach hurdle indoor item climb surprise flat tag abandon butter rare build neither ensure act absent ill truck"
mnemonic_key = MnemonicKey(mnemonic=wallet_mnemonic)
wallet = terra.wallet(mnemonic_key)
print(wallet.key.acc_address)
