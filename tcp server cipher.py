import socket # memanggil modul
import json

class Caesar:   # membuat kelas Caesar, untuk mengenkripsi
    def __init__(self, text, shift):  
        self.text = text # membentuk variabel
        self.shift = shift
    def encipher(self):   # menambahkan method untuk mengenkripsi
        results = ''
        for char in self.text: # proses enkripsi
            if char.isupper():
                results += chr((ord(char) + self.shift - 65) % 26 + 65)
            elif char.islower():
                results += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                results += char
        self.ciphertext = results
        return self.ciphertext # mengembalikan hasil enkripsi
    def decipher(self):   # menambahkan method untuk mendekripsi
        results = ''
        for char in self.text: # proses dekripsi
            if char.isupper():
                results += chr((ord(char) - self.shift - 65) % 26 + 65)
            elif char.islower():
                results += chr((ord(char) - self.shift - 97) % 26 + 97)
            else:
                results += char
        self.plaintext = results
        return self.plaintext # mengembalikan hasil dekripsi



with socket.socket() as ns: # memanggil socket sebagai ns
    ns.bind(('127.0.0.1',5555)) # melakukan bind server
    ns.listen() # menunggu koneksi
    con,addr=ns.accept() # menerima koneksi

    while True: # memulai program interaktif
        req = json.loads(con.recv(256)) # menerima request dari client
        obj = Caesar(req["data"], req["key"]) # mengambil data
        if req["func"] == "enc":    # kondisi if untuk menentukan enkripsi atau dekripsi
            resp = obj.encipher()   # memanggil method enkripsi
            proc = "enciphered"
        elif req["func"] == "dec":
            resp = obj.decipher()   # memanggil method dekripsi
            proc = "deciphered"
        else:
            resp = "error"  # jika masukan tidak valid
            proc = "invalid input"
        con.send(resp.encode()) # mengirim hasil kepada client
        print("sent:",req["data"])  # mencetak data pada layar
        print(proc,":",resp)    # mencetak data pada layar


