from kullanici import Kullanici
import os

kullanici1 = Kullanici()


islem = 0

while True:

    print("######### Ana Menü #########")

    print("İşlemler:")
    print("1-) Giriş Yap")
    print("2-) Kayıt Ol")
    print("3-) Sistemi Kapat")
    
    
        
    if 0 <= islem <= 5: 

        islem = int(input("Lütfen bir işlem seçiniz: "))
    else:
        print("❌ Tanımsız işlem!")
        islem = int(input("Lütfen geçerli bir işlem seçiniz: "))


    if islem == 1:
        print("######### Giriş Menü #########")
        print("İşlemler:")
        print("a-) Giriş Yap")
        print("b-) Şifremi Unuttum")
        giris_islem = input("Lütfen bir işlem seçiniz: ")
        if giris_islem == "a" or giris_islem == "A":
            giris_sonuc = []   #_girisYap() metodunda return ederken iki değer return ediyoruz iki değeri de kullanabilmek için liste yapısı kullandık.
            giris_sonuc = kullanici1._girisYap()
            sayac = 3
            
            oturum_acilmis_kullanici_adi = None

            while True:
                if giris_sonuc[0] == True:
                    #? Kullanıcı giriş yaptıktan sonra şifremi unuttum seçeneği olması ne kadar mantıklı zaten hesap bilgilerini güncelle seçeneği üzerinden şifresini değiştirebilir kaldı ki kullanıcı hesaba giriş yapabildiyse şifresini unutmamıştır demektir. Şimdilik bu şekilde duran şifremi unuttum seçeneğinin yerine gelicek yeni özelliği düşün.

                    #TODO: Giriş Menüsündeki "şifremi unuttum" seçeneğinin yerine başka bir özellik ekle.
                    print("######### Giriş Menü #########")
                    print("İşlemler:")
                    print("a-) Hesap Bilgilerini Güncelle")
                    print("b-) Şifremi Unuttum")
                    print("c-) Hesaptan Çıkış Yap")
                    

                    oturum_acilmis_kullanici_adi = giris_sonuc[1]
                    
                    
                    if giris_sonuc[0]:

                        
                        giris_islem = input("Lütfen bir işlem seçiniz: ")
                    

                        if giris_islem == "a" or giris_islem == "A":
                            yeni_ad = kullanici1._hesapGuncelleme(oturum_acilmis_kullanici_adi)
                            oturum_acilmis_kullanici_adi = yeni_ad
                        
                            break


                        elif giris_islem == "b" or giris_islem == "B":
                            kullanici1.sifremiUnuttum()
                            break

                        elif giris_islem == "c" or giris_islem == "C":
                            kullanici1._cikisYap()
                            break

                    #! Başarısız giriş döngüsünde problem var!

                else:
                    print("Tekrar Deneyin.")
                    giris_sonuc = kullanici1._girisYap()
                    if giris_sonuc[0] == True:
                        kullanici1._girisYap()
                        break
                    sayac = sayac - 1
                    print(f"Kalan Giriş Hakkı: {sayac}")
                    if sayac == 0:
                        break


        elif giris_islem == "b" or giris_islem == "B":
            kullanici1.sifremiUnuttum()  

            
                    
        else:
            print("❌ Herhangi bir işlem seçilemedi.")

    elif islem == 2:
        kullanici1.kayitOl()
    
    elif islem == 3:
        print("Sistem Kapatılıyor...")
        break
    
     
