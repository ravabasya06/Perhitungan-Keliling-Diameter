def ulang():
    pi = 3.14
    
    jari2 = input("Masukkan jari jari lingkaran (kosongkan jika ingin menggunakan diameter) : ")
    if jari2:
        print("Jari-jari : "+str(float(jari2)))
        print("Diameter : "+str(float(jari2)*2))
        print("Keliling : "+str(float(jari2)*2*pi))
    elif jari2 == "":
        diameter = int(input("Masukkan diameter lingkaran : "))
        print("Jari-jari : "+str(float(diameter/2)))
        print("Diameter : "+str(float(diameter)))
        print("Keliling : "+str(float(diameter*pi)))
    pengulangan = input("Lakukan perhitungan lagi? ya / tidak : ")
    if pengulangan == "ya":
        ulang()
    elif pengulangan == "tidak":
        print("Ok")
    else:
        print("Saya tidak mengerti perintah anda, saya akan menganggap anda menjawab tidak.")
ulang()
