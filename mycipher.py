#!/usr/bin/python

import sys

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted_ascii = ord(char) + shift
            if char.islower():
                if shifted_ascii > ord('z'):
                    shifted_ascii -= 26
            elif char.isupper():
                if shifted_ascii > ord('Z'):
                    shifted_ascii -= 26
            encrypted_text += chr(shifted_ascii)
    return encrypted_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar_cipher.py <shift>")
        return

    try:
        shift = int(sys.argv[1])
    except ValueError:
        print("Shift must be an integer")
        return

    message = input().upper()  

    encoded_message = ""
    block_count = 0
    for char in message:
        if char.isalpha():  
            encoded_message += caesar_cipher(char, shift)
            block_count += 1
            if block_count == 5:  
                encoded_message += " "  
                block_count = 0


    for i in range(0, len(encoded_message), 5*5):
        print(encoded_message[i:i+5*5])

if __name__ == "__main__":
    main()

