# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:37:47 2020
program server UDP : yang menerima kalimat dari client dan 
mengubah huruf pada seluruh kalimat menjadi CAPITAL
@author: elisatih
"""

import socket
import lib_prog

serverPort = 12345
""" gunakan SOCK_DGRAM untuk UDP
2 baris berikut WAJIB
"""
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("",serverPort))

print("Server is ready to receive ...")
while 1:
    message, clientAddr = serverSocket.recvfrom(2048)
    #Maksimal waktu mengerjakan
    tugas = lib_prog.TugasClientServer (30)

    tugas.get_question_answer ( )
    print(tugas.get_question())

    question = tugas.get_question()
    serverSocket.sendto(question.encode(), clientAddr)
    print("Pertanyaan yang dikirim ke client: ", question)

    answerClient, clientAddr = serverSocket.recvfrom(2048)
    answerClient = answerClient.decode()
  #  answerClient = round(float(answerClient), 2)

    print("jawaban client :", answerClient)

    message = tugas.check_jawaban(answerClient)
    serverSocket.sendto(message.encode(), clientAddr)
    print("Jawaban dikirim kembali ke client : ", tugas.check_jawaban(answerClient))