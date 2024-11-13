import socket
import json

with socket.socket() as ns:
    ns.connect(('127.0.0.1',5555))
#    msg = {"func" : "dec" , "data": "srowhnvvq", "key":3 }
    msg = {}
    msg["func"] = input("enkripsi atau dekripsi? (enc) (dec): ")
    msg["key"] = int(input("masukkan shift key: "))
    while True:
        msg["data"] = input("masukkan pesan: ")
        msgjson = json.dumps(msg)
        ns.send(msgjson.encode())
        resp = ns.recv(256).decode()
        print("encrypted:", resp)

