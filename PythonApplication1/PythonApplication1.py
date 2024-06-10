##iki noktan�n oklit mesafesini hesaplayan fonksiyon
def oklitMesafesi(m1,m2):
    oklid = 0
    
    for k in range(len(m1)):
        oklid += (m1[k]- m2[k])*(m1[k]- m2[k])
    oklid **= (1/2)
    return oklid

##verilerin haz�rland��� ve oklitMesafesi fonksiyonunun �a�r�ld��� yer 
matris = [-1, 2]#matris=[x1,y1,z1] �� boyutlu bir nokta demektir.
matris1 = [-1, 4]
sonuc = oklitMesafesi(matris,matris1)
print(sonuc)