def encode(ch):
    # A -> 0, B -> 1, ..., Z -> 25
    return ord(ch) - ord('A')


def decode(num):
    # 0 -> A, 1 -> B, ..., 25 -> Z
    return chr(num + ord('A'))


def encrypt_letter(x, k):
    x = encode(x)
    y = (x + k) % 26
    y = decode(y)
    return y


def decrypt_letter(y, k):
    y = encode(y)
    x =  (y-k) %26
    x = decode(x)
    return x


def encrypt_message(plaintext, k):
    ciphertext = ""
    for x in plaintext:
        if x == ' ':
            ciphertext += x
        else:
            y = encrypt_letter(x, k)
            ciphertext += y
    return ciphertext


def decrypt_message(ciphertext, k):
    plaintext = ""
    for y in ciphertext:
        if y == ' ':
            plaintext += y
        else:
            x = decrypt_letter(y, k)
            plaintext += x
    return plaintext


def example():
    plaintext = "HOW ARE YOU DOING"
    k = 3

    ciphertext = encrypt_message(plaintext, k)
    print(ciphertext)

    plaintext = decrypt_message(ciphertext, k)
    print(plaintext)

def brute(k):
    ciphertext = "VYQVIXZ VO YVRI NZXPMZ WMDYBZ CJGY KJNDODJI VRVDO NDBIVG"


    print (k)

    plaintext = decrypt_message(ciphertext, k)
    print(plaintext)

#    ciphertext = encrypt_message(plaintext, k)
 #   print(ciphertext)


def main():
    # The following example gives you an idea of
    # how to use the encrypt and decrypt functions.
    example()

    # 1. Copy and paste the ciphertext here

    # 2. Write your code for brute-force attack to discover the key
    for k in range(0,25):
        brute(k)
if __name__ == '__main__':
    main()