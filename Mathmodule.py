import math # math modülünü dahil etme 
# fonksiyon içerisinde kullanıcıdan seçim yapmasını isteme
def my_function(num):
    
    print("yapmak istediğiniz işlemi seçin:")
    print("faktöryelini hesaplamak için 1 e basınız:")
    print("aşağı yuvarlamak için 2 ye basınız:")
    print("yukarı yuvarlamak için 3 e basınız:")
    print("karekökünü hesaplamak için 4 e basınız:")
    # kullanıcıdan Integer türünde değer alma
    choice=int(input("seçiminiz: "))                             
    if choice==1: 
        # sayının faktöryeli alınmış hali  
        print("sayının faktöryeli: ",math.factorial(int(num)))     
    elif choice ==2:
        # sayının aşağı yuvarlanmış hali
        print("sayının aşağı yuvarlanmış hali: ",math.floor(num)) 
    elif choice ==3:
        # sayının yukarı yuvarlanmış hali
        print("sayının yukarı yuvarlanmış hali: ",math.ceil(num)) 
    elif choice ==4:
        # sayının karekök alınmış hali
        print("sayının kareköklü hali: ",math.sqrt(num))          
    else:
        print("yanlış seçim tekrar giriniz:")
while True: 
    num=0.0
    # kullanıcıdan float tipte değer alma 
    num=float(input("lütfen ondalıklı (float) tipte sayı giriniz:"))
    # fonksiyon çağırma 
    my_function(num)
