from web3 import Web3,HTTPProvider
from eth_account import Account
import os

def lambda_handler(event, context):
    web3 = Web3(HTTPProvider('https://ropsten.infura.io/[YOUR INFURA TOKEN]'))
    
    abi_info = '//YOUR ABI INFOMATION :string//'
    addr_info = '//YOUR CONTRACT ADDRESS//'
    test_contract=web3.eth.contract(address=web3.toChecksumAddress(addr_info),abi=abi_info)
    
    # Get Privatekey from Environment Variables
    private_key = os.environ['PRIVATE_KEY1']
    # Get Address from Privatekey
    public_address = Account.privateKeyToAccount(private_key).address
    
    txn = test_contract.functions.//FUNCTION_NAME//(//INPUTS//).buildTransaction({'gas': n,'gasPrice':web3.toWei('n', 'gwei')})
    # Add Nonce
    txn['nonce'] = web3.eth.getTransactionCount(public_address)
    
    # Sign Transaction
    signed = web3.eth.account.signTransaction(txn, private_key)
    
    # Send RawTransaction
    tx_hash = web3.eth.sendRawTransaction(signed.rawTransaction)
    
    return tx_hash
