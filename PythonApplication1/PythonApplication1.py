##iki noktanýn oklit mesafesini hesaplayan fonksiyon
def oklitMesafesi(m1,m2):
    oklid = 0
    
    for k in range(len(m1)):
        oklid += (m1[k]- m2[k])*(m1[k]- m2[k])
    oklid **= (1/2)
    return oklid

##verilerin hazýrlandýðý ve oklitMesafesi fonksiyonunun çaðrýldýðý yer 
matris = [-1, 2]#matris=[x1,y1,z1] üç boyutlu bir nokta demektir.
matris1 = [-1, 4]
sonuc = oklitMesafesi(matris,matris1)
print(sonuc)