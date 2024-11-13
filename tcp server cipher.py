import socket
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



with socket.socket() as ns:
    ns.bind(('127.0.0.1',5555))
    ns.listen()
    con,addr=ns.accept()

    while True:
        req = json.loads(con.recv(256))
        obj = Caesar(req["data"], req["key"])
        if req["func"] == "enc":
            resp = obj.encipher()
            proc = "enciphered"
        elif req["func"] == "dec":
            resp = obj.decipher()
            proc = "deciphered"
        else:
            resp = "error"
            proc = "invalid input"
        con.send(resp.encode())
        print("sent:",req["data"])
        print(proc,":",resp)


