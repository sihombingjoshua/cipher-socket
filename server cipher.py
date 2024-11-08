import socket   # memanggil modul
import json

class Caesar:   # membuat kelas Caesar, untuk mengenkripsi
    def __init__(self, plain, shift):  
        self.plaintext = plain # membentuk variabel
        self.shift = shift
    def cipher(self):   # menambahkan method untuk mengenkripsi
        results = ''
        for char in self.plaintext: # proses enkripsi
            if char.isupper():
                results += chr((ord(char) + self.shift - 65) % 26 + 65)
            elif char.islower():
                results += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                results += char
        self.ciphertext = results
        return self.ciphertext # mengembalikan hasil enkripsi

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ns: # memanggil modul socket sebagai ns
    ns.bind(('127.0.0.1', 7777))    # membind port
    data, addr=ns.recvfrom(256) # menunggu request pertama
    datadump = json.loads(data) # merubah request pertama dari json menjadi dictionary
    cipher1 = Caesar(datadump['data'], datadump['key']) # mengenkripsi data dengan membuat object
    print("Plaintext : " +cipher1.plaintext) # mencetak request pertama yaitu PoltekSSN
    print("Ciphertext : "+cipher1.cipher()) # mencetak request pertama yaitu SrowhnVVQ
    ns.sendto(cipher1.cipher().encode(), addr) # mengirimkan hasil enkripsi kepada client

    i = 1
    while True: # memulai program interaktif
        data, addr=ns.recvfrom(256) # menunggu request
        datadump = json.loads(data) # mengonversi request dari json menjadi dictionary
        if datadump['data'] == 'exit': # jika request = exit, maka program ditutup
            break
        cipher1 = Caesar(datadump['data'], datadump['key']) # mengenkripsi data dengan membuat object
        print("[",i,"]Plaintext : " +cipher1.plaintext) # mencetak plaintext
        print("[",i,"]Ciphertext : "+cipher1.cipher()) # mencetak hasil ciphertext
        ns.sendto(cipher1.cipher().encode(), addr) # mengirimkan hasil enkripsi kepada client
        i += 1
