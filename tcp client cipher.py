import socket
import json

with socket.socket() as ns:
    ns.connect(('127.0.0.1',5555))
    msg = {"func" : "dec" , "data": "srowhnvvq", "key":3 }
    msgjson = json.dumps(msg)
    ns.send(msgjson.encode())
    resp = ns.recv(256).decode()
    print(resp)

