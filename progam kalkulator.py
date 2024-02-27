class Kalkulator:
    def plus(self,a,b):
        hasil = a+b
        print(f"Hasil Dari {a}+{b} Adalah {hasil}\n")
    def mines(self,a,b):
        hasil = a-b
        print(f"Hasil Dari {a}-{b} Adalah {hasil}\n")
    def kali(self,a,b):
        hasil = a*b
        print(f"Hasil Dari {a}x{b} Adalah {hasil}\n")
    def bagi(self,a,b):
        if b == 0:
            print("ERORR! TIDAK BISA DI BAGI 0")
        else:
            hasil = a/b 
            print(f"Hasil Dari {a}:{b} Adalah {hasil}\n")
            
cal = Kalkulator()
    
while True:
    print('='*7, "APLIKASI HITUNG", '='*7, "\n1.Perhitungan Baru\n2.Exit")
    s1 = int(input("Masukan Pilihan (1/2):"))
    if s1 == 1:
        print('='*8, "MASUKAN NILAI",  '='*8)
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua:"))
        print('='*8, "METODE HITUNG", '='*8, "\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Exit")
        o = str(input("Masukan Operasi yang anda pilih:"))
        if o == '1':
            cal.plus(a,b)
        elif o == '2':
            cal.mines(a,b)
        elif o == '3':
            cal.kali(a,b)
        elif o == '4':
            cal.bagi(a,b)
        elif o == '5':
            print("TERIMAKASIH")
            break
        else:
            print("PILIHAN ANDA TIDAK ADA!!")
            break
    elif s1 == 2:
        print("TERIMAKASIH")
        break
    else:
        print("ERORR!")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    