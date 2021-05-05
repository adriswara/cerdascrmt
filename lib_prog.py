import random
from datetime import datetime

class TugasClientServer :
    question = ""
    answer = 0
    durasiJawaban = 0
    start_time = datetime.now()
    finish_time = datetime.now()
    lamaJawaban = datetime.now()

    def __init__(self, durasi) :
        self.durasiJawaban = durasi

    def operator_matematika ( self, argument ) :
        switcher = {
            1 : "T ∧ F = F" ,
            2 : "F ∨ T = T" ,
            3 : "T ∧ (T ∧ F) = F" ,
            4 : "F ∨ (T ∧ T) = T" ,
        }
        return switcher.get ( argument , "+" )

    def calc ( self, operator ) :
        if (operator==1):
            hasil = "2"
        elif (operator==2) : 
            hasil = "1"
        elif (operator==3) :
            hasil = "2" 
        elif (operator==4) :
            hasil = "1" 
        else :
            hasil = "2"
        return hasil


    def get_question_answer ( self ):
        operator = random.randint ( 1,4 )
           
        self.start_time = datetime.now()
        self.question = self.start_time.strftime("%H:%M:%S") + " " + " " + self.operator_matematika(operator) + " " + "\n1.True" + "2.False"
        self.answer = self.calc (  operator  )

    def get_question ( self ):
        return self.question 

    def get_answer ( self ) :
        return self.answer

    def hitung_waktu ( self ) :
        self.finish_time = datetime.now()
        self.lamaJawaban = self.finish_time - self.start_time
        return self.lamaJawaban.total_seconds()

    def check_jawaban ( self, Jawab ) :
        if (Jawab!=self.answer) :
            stringJawaban = "Salah"
        else :
            stringJawaban = "Benar, waktu jawaban : " + str(self.hitung_waktu()) + " detik"
            if (self.hitung_waktu()>self.durasiJawaban) :
                stringJawaban = stringJawaban + " TERLAMBAT !!!"
        return stringJawaban