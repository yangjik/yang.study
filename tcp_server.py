import socket

# 이더넷 환경, tcp 통신
sock =  socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# sock.close()
SERVER_IP = '0.0.0.0'
SERVER_PORT = 5000
# tuple 형식으로
sock.bind((SERVER_IP, SERVER_PORT))

sock.listen(1)
while True:
    print("Client 대기중")
    # 연결된 소켓, ip주소 얻을수있다.
    conn, client = sock.accept()

    print('client의 ip, port : ', client)

    send_txt = bytes('hi im server', encoding='utf-8')
    conn.send(send_txt)

    client_txt = conn.recv(1024)
    print("client에서 송신한 메시지 : ", client_txt.decode(encoding='utf-8'))

    conn.close()
    
    break