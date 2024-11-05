import socket
import json
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ns:
    a = {'data' : 'PoltekSSN', 'key' : 3}
    ajson = json.dumps(a)
    ns.sendto(ajson.encode(), ('127.0.0.1', 7777))
    data, addr=ns.recvfrom(256)
    print(data.decode())

    shift = int(input("shift?: "))

    while True:
        b = {}
        plaintxt = input("plaintxt: ")
        if plaintxt == 'exit':
            b['data'] = plaintxt
            b['key'] = shift
            ajson = json.dumps(b)
            ns.sendto(ajson.encode(), ('127.0.0.1', 7777))
            break
        b['data'] = plaintxt
        b['key'] = shift
        ajson = json.dumps(b)
        ns.sendto(ajson.encode(), ('127.0.0.1', 7777))
        data, addr=ns.recvfrom(256)
        print("ciphertext:", data.decode())


