from dotenv import load_dotenv
import os

load_dotenv()

MUMBAI_MATIC_TEST_URL = os.environ.get('MUMBAI_MATIC_TEST_URL')
WALLET_ADDRESS = os.environ.get('WALLET_ADDRESS')
MNEMONIC = os.environ.get('MNEMONIC')
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
