import socket
import json

with socket.socket() as ns:
    ns.connect(('127.0.0.1',5555))
#    msg = {"func" : "dec" , "data": "srowhnvvq", "key":3 }
    
    while True:
        msg = {}
        msg["func"] = input("Enkripsi atau dekripsi? (enc) (dec): ")

        while True:
            try:
                msg["key"] = int(input("Masukkan shift key: "))
                break
            except ValueError:
                print("Ooops, masukann tolong masukkan angka.")
                
        msg["data"] = input("Masukkan pesan: ")
        msgjson = json.dumps(msg)
        ns.send(msgjson.encode())
        resp = ns.recv(256).decode()
        print("Encrypted:", resp)

