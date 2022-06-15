class batsulmasail:
    def batsulmasail():
        global deskripsimasalah
        global jawaban 
        print ("\n----------------------- batsulmasail -----------------------")
        print ("deskripsi masalah")
        print ("jawaban")
        print ("1. makruh")
        print ("2. haram")
        print ("3. mubah")
        nomor=int(input("masukan pilihan: "))
        jawaban=int(input("jawaban : "))

        if nomor==1:
            deskripsimasalah=jawaban
            print (jawaban,"batsulmasail ", deskripsimasalah)
            deskripsimasalah=("batsulmasail")
        elif nomor==2:
            deskripsimasalah=jawaban
            print (jawaban,"makruh", deskripsimasalah)
            deskripsimasalah=("batsulmasail")
        elif nomor==3:
            deskripsimasalah=jawaban
            print (jawaban,"haram ", deskripsimasalah)
            posko=("batsulmasail")
        else:
            print("pilihan tidak ada, silahkan masukan lagi!!!")
            batsulmasail()

    batsulmasail()
    jawaban=deskripsimasalah 

  

    