# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:07:08 2020
Program client, yang menerima kalimat dari keyboard, mengirimkannya ke 
server; kemudian client menerima pesan dari server dan mencetaknya ke layar
@author: elisatih
"""

import socket
HOST = 'localhost'
PORTSERVER = 12345

# """ gunakan SOCK_DGRAM untuk UDP """
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
test = "Test".encode()
s.sendto(test,(HOST,PORTSERVER))

question = s.recv(1024)
print("Question : ", question.decode())

answer = input("Jawaban : ")
message = answer.encode("UTF-8")

s.sendto(message,(HOST,PORTSERVER))

answerStatus = s.recv(1024)
print("Status jawaban : ", answerStatus.decode())

s.close()
