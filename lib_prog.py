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
            1 : "+" ,
            2 : "-" ,
            3 : "*" ,
            4 : "/" ,
        }
        return switcher.get ( argument , "+" )

    def calc ( self, angka1 , operator , angka2 ) :
        if (operator==1):
            hasil = angka1 + angka2
        elif (operator==2) : 
            hasil = angka1 - angka2 
        elif (operator==3) :
            hasil = angka1 * angka2 
        elif (operator==4) :
            hasil = angka1 / angka2 
        else :
            hasil = angka1 + angka2
        return hasil


    def get_question_answer ( self ):
        operator = random.randint ( 1,4 )
        if (operator==4) :
            angka1 = random.randint ( 10,99 )
            angka2 = random.randint ( 1,10 )
        else :
            angka1 = random.randint ( 0,99 )
            angka2 = random.randint ( 0,99 )        
        self.start_time = datetime.now()
        self.question = self.start_time.strftime("%H:%M:%S") + " " + str(angka1) + " " + self.operator_matematika(operator) + " " + str(angka2)
        self.answer = self.calc ( angka1 , operator , angka2 )

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