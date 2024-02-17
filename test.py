## How to import the module:

PLAIN_TEXT      = 'sujit' # plain text
LENGTH          = 32      # length of hash 
ITERATIONS      = 100000  # number of iterations
TOKEN_BYTES     = 16      # 16 bytes (128 bits) is a common size for salts

## Plain Text Encrypt : 
from text_encrypt_decrypt.text_encrypt_decrypt import encrypt_plain_text

encrypted_plain_text, key = encrypt_plain_text(PLAIN_TEXT, LENGTH, TOKEN_BYTES, ITERATIONS)

print("Encrypted plain_text:", encrypted_plain_text)

print("Encrypted Key:", key)

## Decrypt Encrypted Plain Text : 
from text_encrypt_decrypt.text_encrypt_decrypt import decrypt_plain_text

decrypted_plain_text = decrypt_plain_text(encrypted_plain_text, key)

print("Decrypted plain_text:", decrypted_plain_text)