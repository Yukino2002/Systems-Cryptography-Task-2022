plain_text = 'the passwords stored in your database were in plaintext and completely vulnerable as such i replaced all the stored passwords with their corresponding rolling hashes using one of the primes as seventeen and the other as oneexpnineplusseven you should be able to access the website if you can generate the corresponding hash'
alphabet = 'fgbqmytczkorlehpxdsuwnvai'

cipher_text = ''

for c in plain_text:
    if c == ' ':
        cipher_text += ' '
    else:
        cipher_text += alphabet[(alphabet.find(c) + 12) % len(alphabet)]

print(cipher_text)