import socket       # memanggil modul
import json
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ns:    # memanggil socket sebagai ns
    a = {'data' : 'PoltekSSN', 'key' : 3}   # data pertama yang dikirimkan
    ajson = json.dumps(a)   # merubah dalam bentuk json
    ns.sendto(ajson.encode(), ('127.0.0.1', 7777))  # mengirim kepada server
    data, addr=ns.recvfrom(256) # menunggu response server
    print("ciphertext:", data.decode())    # mencetak response server

    shift = int(input("shift?: ")) # meminta key shift terbaru

    i = 1
    while True: # memulai program interaktif
        b = {}
        plaintxt = input("["+str(i)+"]plaintxt: ")  # meminta inputan plaintext
        if plaintxt == 'exit':  # program akan berhenti jika inputan = "exit"
            b['data'] = plaintxt
            b['key'] = shift
            ajson = json.dumps(b)
            ns.sendto(ajson.encode(), ('127.0.0.1', 7777))
            break
        b['data'] = plaintxt
        b['key'] = shift
        ajson = json.dumps(b)   # merubah dalam bentuk json
        ns.sendto(ajson.encode(), ('127.0.0.1', 7777))  # mengirimkan ke server
        data, addr=ns.recvfrom(256) # mendapatkan response
        print("["+str(i)+"]ciphertext:", data.decode()) # mencetak hasil pada layar
        i += 1


