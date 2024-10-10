# Cryptography
Cryptography program of the Systems Analysis and Development course

## 🗂️ Classes Overview

This project includes the following functions:

- **encrypt(message)**: 
  - Encrypts the given message using a randomized key for letters and numbers.
  - Returns a tuple containing the encrypted message, the alphabetic key, and the numeric key.
  
- **decipher(encrypted_message, decipher_alpha, decipher_number)**: 
  - Decrypts the given encrypted message using the provided keys.
  - Returns the original, deciphered message.

### Usage

1. Call the `encrypt()` function with the message you want to encrypt. 
2. Store the returned tuple to retrieve the encrypted message and keys.
3. Call the `decipher()` function with the encrypted message and keys to retrieve the original message.
