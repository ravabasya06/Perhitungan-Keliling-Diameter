def ulang():
    pi = 3.14
    
    jari2 = input("Masukkan jari jari lingkaran (kosongkan jika ingin menggunakan diameter) : ")
    if jari2:
        print((str("Jari-jari : "+str(jari2))))
        print((str("Diameter : "+str(jari2*2))))
        print((str("Keliling : "+str(jari2*2*pi))))
    elif jari2 == "":
        diameter = int(input("Masukkan diameter lingkaran : "))
        print((int(diameter/2)))
        print(diameter)
        print(pi*diameter)
    pengulangan = input("Lakukan perhitungan lagi? ya / tidak : ")
    if pengulangan == "ya":
        ulang()
    elif pengulangan == "tidak":
        print("Ok")
    else:
        print("Saya tidak mengerti perintah anda, saya akan menganggap anda menjawab tidak.")
ulang()
