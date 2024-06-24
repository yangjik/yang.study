import socket

IP = '0.0.0.0'
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((IP, PORT))

server_txt = sock.recv(32)
print('server 에서 송신한 메시지 : ', server_txt.decode(encoding='utf-8'))

send_txt = bytes('hi im client', encoding='utf-8')
sock.send(send_txt)

sock.close()