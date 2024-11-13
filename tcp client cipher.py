import socket # memanggil modul
import json

with socket.socket() as ns: # memanggil socket sebagai ns
    ns.connect(('127.0.0.1',5555))  # membuat koneksi dengan server
    
    while True: # fungsi interaktif
        msg = {}
        msg["func"] = input("Enkripsi atau dekripsi? (enc) (dec): ")    # inputan untuk fungsi

        while True: # perulangan while, berfungsi untuk memastikan inputan shift adalah angka int
            try:
                msg["key"] = int(input("Masukkan shift key: "))
                break
            except ValueError:
                print("Ooops, masukann tolong masukkan angka.")
                
        msg["data"] = input("Masukkan pesan: ") # meminta inputan pesan
        msgjson = json.dumps(msg)   # merubah kedalam format json
        ns.send(msgjson.encode())   # mengirimkan ke server
        resp = ns.recv(256).decode()    # menerima respons dari server
        print("Result:", resp)  # menampilkan respons

