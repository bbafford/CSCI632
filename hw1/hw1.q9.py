def encode(ch):
    return ord(ch)-ord('A')

def decode(num):
    return chr(num + ord('A'))

def encrypt(x, a, b):
    x = encode(x)
    y = (a*x + b) % 26
    y =  decode(y)
    return y

def inverse(a):
    for b in range(1, 26):
        if (a*b) %26 == 1:
            return b
    return 0 # This should not happen

def decrypt(y, a, b):
    y = encode(y)
    inverse_a = inverse(a)
    x = inverse_a*(y-b) % 26
    x = decode(x)
    return x

def main():
    # Encrypt 'C' with k = (15, 12)
    ciphertext = encrypt('C', 15, 12)
    print("C is encrypted to", ciphertext)

    # Decrypt 'S' with k = (7, 20)
    plaintext = decrypt('S', 7, 20)
    print("S is decrypted to", plaintext)

if __name__ == '__main__':
    main()