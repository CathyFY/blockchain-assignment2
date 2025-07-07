import hashlib
import os

def myhash(m):
    #Generate random nonce
    nonce = os.urandom(16).hex()
    #Generate hex digest
    to_hash = (nonce + m).encode('utf-8')
    h_hex = hashlib.sha256(to_hash).hexdigest()
    return nonce, h_hex
