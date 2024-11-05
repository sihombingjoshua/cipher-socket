import socket
import json

class Caesar:
    def __init__(self, plain, shift):
        self.plaintext = plain
        self.shift = shift
    def cipher(self):
        results = ''
        for char in self.plaintext:
            if char.isupper():
                results += chr((ord(char) + self.shift - 65) % 26 + 65)
            elif char.islower():
                results += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                results += char
        self.ciphertext = results
        return self.ciphertext

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ns:
    ns.bind(('127.0.0.1', 7777))
    data, addr=ns.recvfrom(256)
    datadump = json.loads(data)
    cipher1 = Caesar(datadump['data'], datadump['key'])
    print("Plaintext : " +cipher1.plaintext)
    print("Ciphertext : "+cipher1.cipher())
    ns.sendto(cipher1.cipher().encode(), addr)

    i = 1
    while True:
        data, addr=ns.recvfrom(256)
        datadump = json.loads(data)
        if datadump['data'] == 'exit':
            break
        cipher1 = Caesar(datadump['data'], datadump['key'])
        print("[",i,"]Plaintext : " +cipher1.plaintext)
        print("[",i,"]Ciphertext : "+cipher1.cipher())
        ns.sendto(cipher1.cipher().encode(), addr)
        i += 1
