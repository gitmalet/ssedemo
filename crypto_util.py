import nacl.secret
import nacl.utils

from pathlib import Path


def initialize_key(key_file: Path):
    """
    Loads the key from the given path or creates a fresh one if the file is not
    found
    Returns the key
    """
    if key_file.exists():
        with open(key_file, "rb") as f:
            key = f.read()
    else:
        key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
        # Create parent directory structure
        key_file.parent.mkdir(parents=True, exist_ok=True)
        with open(key_file, "wb") as f:
            f.write(key)
 
    if len(key) != nacl.secret.SecretBox.KEY_SIZE:
        raise ValueError(f"Key is of invalid length {len(key)} vs {nacl.secret.SecretBox.KEY_SIZE}")
    return key


def encrypt(key: bytes, plaintext: str):
    """
    Encrypts the given data string under the key
    Returns the resulting ciphertext
    """
    # We want to handle bytes in crypto operations, so encoding the input string
    # into a bytes object
    pt = plaintext.encode()

    # Create the cipher object
    box = nacl.secret.SecretBox(key)
    # The box handles nonce generation and encryption and authantication.
    # The ciphertext object already contains the nonce
    ct = box.encrypt(pt)

    return ct


def decrypt(key: bytes, ciphertext: bytes):
    """
    Decrypts the given ciphertext under the key
    Returns the resulting plaintext as a string
    """
    # Create the cipher object
    box = nacl.secret.SecretBox(key)

    # The box handles reading out the nonce, checking authentication and
    # decrypting
    pt = box.decrypt(ciphertext)

    # We return a string again because the encrypt function has a string
    # argument
    return pt.decode()