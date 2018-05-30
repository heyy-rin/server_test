# import socket
#
# server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_sock.bind(('172.30.1.1', 8585)) #서버의 아이피와 포트 지정
# server_sock.listen(0) # 클라이언트의 연결요청 기다림
#
# client_sock , addr = server_sock.accept() # 연결 요청을 받음
#
# data = client_sock.recv(65535) # 클라이언트의 데이터를 가져옴
# print("recieve Data : ", data.decode())
#     #client_sock.send(data)


import socket
import cv2
import numpy

#socket 수신 버퍼를 읽어서 반환하는 함수
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

#수신에 사용될 내 ip와 내 port번호
TCP_IP = '172.30.1.1'
TCP_PORT = 5001

#TCP소켓 열고 수신 대기
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
conn, addr = s.accept() # socket과 client주소

#String형의 이미지를 수신받아서 이미지로 변환 하고 화면에 출력
length = recvall(conn,16)

#길이 16의 데이터를 먼저 수신하는 것은 여기에 이미지의 길이를 먼저 받아서 이미지를 받을 때 편리하려고 하는 것이다.
stringData = recvall(conn, int(length))
#print("string length", length.decode())

data = numpy.fromstring(stringData, dtype='uint8')
s.close()
decimg=cv2.imdecode(data,1)
cv2.imshow('SERVER',decimg)
cv2.waitKey(0)
cv2.destroyAllWindows()