from kullanici import Kullanici
from personel import Personel
from admin import Admin
import os

kullanici1 = Kullanici()

islem = 0

while True:

    print("######### Ana Menü #########")

    print("İşlemler:")
    print("1-) Giriş Yap")
    print("2-) Kayıt Ol")
    print("3-) Sistemi Kapat")
    try:
        if 0 <= islem <= 3: 

            islem = int(input("Lütfen bir işlem seçiniz: "))
        else:
            print("❌ Tanımsız işlem!")
            islem = int(input("Lütfen geçerli bir işlem seçiniz: "))
    
    except ValueError:
        print("❌ Lütfen işlem yapmak için bir 1-3 arası bir rakam seçiniz")


    if islem == 1:
        print("######### Giriş Menü #########")
        print("İşlemler:")
        print("a-) Giriş Yap")
        print("b-) Şifremi Unuttum")
        print("c-) Ana Menüye Dön")
        
        while True:

            print("######### Giriş Menü #########")
            print("İşlemler:")
            print("a-) Giriş Yap")
            print("b-) Şifremi Unuttum")
            print("c-) Ana Menüye Dön")

            giris_islem = input("Lütfen bir işlem seçiniz: ")
            
            if giris_islem == "a" or giris_islem == "A":
                # giris_sonuc = []   #_girisYap() metodunda return ederken iki değer return ediyoruz iki değeri de kullanabilmek için liste yapısı kullandık.
                # giris_sonuc = kullanici1._girisYap()
                sayac = 3
                
                oturum_acilmis_kullanici_adi = None

                while sayac > 0:
                    print(f"\n--- Giriş Denemesi ({sayac} hakkınız var)---")
                    
                    giris_basari, ad, rol = kullanici1._girisYap()

                    if giris_basari == True:
                        oturum_acilmis_kullanici_adi = ad

                        if rol == "Admin":
                            kullanici1 = Admin() #*Kullanıcıyı admin nesnesi haline getirdik.
                            print("👑 Yönetici Paneli Yüklendi.")
                        
                        else:
                            kullanici1 = Personel() #*Kullanıcıyı personel nesnesi haline getirdik.
                            print("👷 Personel Paneli Yüklendi.")

                        print("\n ✅ Giriş Başarılı!")
                        break  #Giriş işlemi başarılı olduğu için sayaç döngüsünden çıkar.

                    else:
                        sayac -= 1
                        if sayac > 0:
                            print(f"Hatalı Giriş, Kalan Giriş Hakkı: {sayac}")
                            
                        else:
                            print("❌ Giriş hakkınız kalmadı. Ana Menüye dönülüyor.")

                if oturum_acilmis_kullanici_adi:

                    while True:
                        
                            #? Çalışma paneli kullanıcının rolüne göre değişecek bir panel olacaktır eğer kullanıcı çalışansa ve çalışma paneline basarsa farklı bir arayüzle karşılaşacak adminse farklı bir arayüzle karşılaşacak.

                            #TODO: Oturum Menüsündeki "Çalışma Paneli" seçeneğini kullanıcının rolüne göre biçimlendir.
                            print("######### Oturum Menüsü #########")
                            print("İşlemler:")
                            print("a-) Hesap Bilgilerini Güncelle")
                            print("b-) Çalışma Paneli")
                            print("c-) Hesaptan Çıkış Yap")
                            
                            giris_islem_alt = input("Lütfen bir işlem seçiniz: ")
                            
                            if giris_islem_alt == "a" or giris_islem_alt == "A":
                                yeni_ad = kullanici1._hesapGuncelleme(oturum_acilmis_kullanici_adi)
                                oturum_acilmis_kullanici_adi = yeni_ad

                            elif giris_islem_alt == "b" or giris_islem_alt == "B":
                                
                                if isinstance(kullanici1, Admin):
                                    while True:
                                        print("\n#### Admin Paneli #####")
                                        print("1-) Personel Ekle")
                                        print("2-) Personel Sil")
                                        print("3-) Personel Görüntüle")
                                        print("4-) Mesai Kayıtlarını Görüntüle")
                                        print("5-) İzin Taleplerini Onayla/Reddet")
                                        print("6-) İzin Taleplerini Görüntüle")
                                        print("7-) Personel İzin Hakkı Görüntüle")
                                        print("8-) Geri Dön")

                                        try:
                                            admin_islem = int(input("İşlem Seçiniz: "))

                                        except ValueError:
                                            print("❌ Hatalı giriş! Lütfen bir sayı giriniz.")
                                            continue
                                            
                                        if 1<= admin_islem <= 8:
                                            if admin_islem == 1:
                                                kullanici1._personelEkle()

                                            elif admin_islem == 2:
                                                kullanici1._personelSil()
                                                
                                            elif admin_islem == 3:
                                                kullanici1._personelGoruntule()
                                                
                                            elif admin_islem == 4:
                                                kullanici1._mesaiKaydiGoruntule()
                                                
                                            elif admin_islem == 5:
                                                kullanici1._izinOnayla()
                                                
                                            elif admin_islem == 6:
                                                veriler = kullanici1._provizyonIzinleriOku()
                                                kullanici1._izinTalepGoruntule(veriler)

                                            elif admin_islem == 7:
                                                kullanici1._izinHakkiGoruntuleme()

                                            elif admin_islem == 8:
                                                break
                                            
                                elif isinstance(kullanici1, Personel):
                                    print("\n#### Personel Paneli #####")
                                    
                                    print("k-) Mesai Girişi Yap")
                                    print("L-) Mesai Çıkışı Yap")
                                    print("t-) İzin Talep Et")
                                    print("r-) Penelden Çık")
                                
                                    giris_islem_personel = input("Lütfen işlem seçin: ")

                                    if giris_islem_personel == "k" or giris_islem_personel == "K":
                                        kullanici1.mesaiGirisYap(oturum_acilmis_kullanici_adi)

                                    elif giris_islem_personel == "l" or giris_islem_personel == "L":
                                        # print("\nMesai çıkışı yapılıyor...")
                                        # print("✅ Mesai çıkış saati sisteme kaydedildi.")

                                        #! Metot tam çalışmıyor.
                                        kullanici1.mesaiCikisYap(oturum_acilmis_kullanici_adi)
                                        
                                    elif giris_islem_personel == "t" or giris_islem_personel == "T":
                                        # print("\n ❌ İzin talebi foksiyonu etkin değil (çok yakında)")
                                        # print(f"Kalan İzin Hakkınız: {kullanici1.izinHakki} gün")
                                        
                                        kullanici1.izinTalepEt(oturum_acilmis_kullanici_adi)
                                    
                                    elif giris_islem_personel == "r" or giris_islem_personel == "R":
                                        break

                            elif giris_islem_alt == "c" or giris_islem_alt == "C":
                                print("\nOturum kapatılıyor...")
                                oturum_acilmis_kullanici_adi = None
                                break

                            else:
                                print("❌ Tanımsız işlem!")

            elif giris_islem == "b" or giris_islem == "B":
                kullanici1.sifremiUnuttum()
                break

            elif giris_islem == "c" or giris_islem == "C":
                break

    elif islem == 2:
        kullanici1.kayitOl()
    
    elif islem == 3:
        print("Sistem Kapatılıyor...")
        break
    