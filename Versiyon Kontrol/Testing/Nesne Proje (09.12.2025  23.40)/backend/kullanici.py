import random
import os
import smtplib
from email.message import EmailMessage
import ssl
import re


class Kullanici(object):
    def __init__(self, __id="02240201169", kullaniciAdi="ÇalışanAbi44", __sifre="123456", __adSoyad="Mustafa Gül", eposta="mustafagul@gmail.com", telno="+90 537 823 45 61"):
        self.__id = __id
        self.kullaniciAdi = kullaniciAdi
        self. __sifre = __sifre
        self.__adSoyad = __adSoyad
        self.eposta = eposta
        self.telno = telno
    
    ####### Claasa ait Metotlar #######

    def _girisYap(self):
        
        #TODO: Kullanıcının rolüne (Admin/Çalışan) göre giriş yapabilmeli bu mekanizmayı geliştir.

        KLASOR_ADI = "Nesne Tabanlı Programlama Projesi/Proje/data_sets"
        DOSYA_YOLU = os.path.join(KLASOR_ADI,'kullanici_verileri.txt')
        giris_kullanici_adi = input("Kullanıcı Adı: ").strip()
        giris_sifre = input("Şifre: ").strip()

        try:
            with open(DOSYA_YOLU, "r",encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
                kullanici_bulundu = False

                for i,satir in enumerate(tum_satirlar):
                    satir = satir.strip()
                    
                    if satir.startswith("Kullanici Adı ="):
                        kayitli_kullanici_adi = satir.split("=",1)[1].strip()

                        if kayitli_kullanici_adi == giris_kullanici_adi:

                            if i + 1 < len(tum_satirlar):
                                sifre_satiri = tum_satirlar[i+1].strip()

                                if sifre_satiri.startswith("Şifre ="):
                                    kayitli_sifre = sifre_satiri.split("=",1)[1].strip()

                                    if kayitli_sifre == giris_sifre:
                                        kullanici_bulundu = True
                                        print(f"\n ✅ Giriş Başarılı! Hoş geldiniz, {giris_kullanici_adi}.")
                                        return kullanici_bulundu

                                        break
                if not kullanici_bulundu:
                    print("\n ❌ Giriş Başarısız. Kullanıcı adı veya şifre hatalı.")
                    return kullanici_bulundu
        except FileNotFoundError:
            print(f"\n❌ Kayıtlı kullanıcı bulunamadı. Lütfen önce kayıt işlemi yaptırınız.")
        
        except Exception as e:
            print(f"\n❌ Giriş yaparken bir hata oluştu: {e}")

    def _cikisYap(self):
        print("Çıkış Yapılıyor...")
        print("\n✅ Sistemden Başarıyla Çıkış Yapıldı.")

    
        



    def kayitOl(self):
        

        ##############* Doğrulama Mekanizma Metotları ##############

        def epostaDogrula(self,eposta):
            #E-posta doğrulama mekanizması.
            eposta_deseni = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            return re.fullmatch(eposta_deseni,eposta)
    
    
        def sifreGuvenlikKontrol(self,sifre):
            #Şifre güvenliği mekanizması.

            if len(sifre) < 8:
                return "Şifre en az 8 karakter uzunluğunda olmalıdır."
            if not re.search(r"[A-z]",sifre):
                return "Şifre en az bir büyük garf içermelidir."
            if not re.search(r"[a-z]",sifre):
                return "Şifre en az bir küçük harf içermelidir."
            if re.search(r"[ö,ü,ç,ğ,İ,ı,Ö,Ü,Ç,Ğ]",sifre):
                return "Şifre Türkçe karakterler içeremez."
            if not re.search(r"[0-9]",sifre):
                return "Şifre en az bir rakam içermelidir."
        
            return None #Hata yok.
    

        def telnoDogrula(self,telno):
            #Telefon numarasına ait güvenlik mekanizması.
            telno = telno.replace(" ","").replace("-","0") #Boşluk ve tireler temizlenir.
            if not telno.isdigit():
                return "Telefon numarası sadece rakamlardan oluşmalıdır."
            if len(telno) < 10 or len(telno) > 11:
                return "Telefon numarası 10 veya 11 haneli olmalıdır."
            
            return None #Hata yok.


        

        ########* Kontrol Mekanizmaları ########
        if not self.kullaniciAdi or not self.__sifre or not self.__adSoyad or not self.eposta or not self.telno:
            print("\n ❌ Kullanıcı adı ve şifre gibi bilgiler boş bırakılamaz veya sadece boşluklardan oluşamaz.")

            return -1
        
        
        temp_data = {}
        #Kullanıcı Adı Kontrol Mekanizması
        while True:
            kullanici_adi = input("Kullanıcı Adınızı Giriniz: ").strip()

            if not kullanici_adi:
                print("\n ❌ Kullanıcı adı boş bırakılamaz.")
                continue #Döngünün başına döner.

            if ' ' in kullanici_adi:
                print("\n ❌ Kullanıcı adı boşluk içeremez.")
                continue
            
            if re.search(r"[ö,ü,ç,ğ,İ,ı,Ö,Ü,Ç,Ğ]",kullanici_adi):
                 print("Şifre Türkçe karakterler içeremez.")
                 continue
            
            if len(kullanici_adi) < 8:
                print("\nKullanıcı adı minumum 8 karakterli olabilir.")
                continue

            if len(kullanici_adi) >= 16:
                print("\nKullanıcı adı maksimum 16 karakterli olabilir.")
                continue

            if not re.search(r"[A-Z]",kullanici_adi):
                print("\nKullanıcı adı en az bir büyük harf içermelidir.")
                continue
            
            if not re.search(r"[a-z]",kullanici_adi):
                print("\nKullanıcı adı en az bir küçük harf içermelidir.")
                continue
                


            #Tüm kontrollerden geçip data sets de ilgili değişkeni güncelledi.
            temp_data['kullaniciAdi'] = kullanici_adi
            break
        
        #Şifre Kontrol Mekanizması
        while True:
            sifre = input("Şifrenizi Giriniz: ").strip()

            if not sifre:
                print("\n ❌ Şifre boş bırakılamaz.")
                continue

            sifre_hata = sifreGuvenlikKontrol(self,sifre)
            if sifre_hata:
                print(f"\n❌ Şifre Hatası: {sifre_hata}")
                continue

            temp_data['sifre'] = sifre
            break

        #İsim Soyisim Kontrol Mekanizması
        while True:
            adSoyad = input("Adınızı Soyadınızı Giriniz: ").strip()

            if not adSoyad:
                print("\n ❌ Ad Soyad alanı boş bırakılamaz.")
                continue

            if not re.search(r"[a-z]",sifre):
                return "\nŞifre en az bir küçük harf içermelidir."
            if re.search(r"[ö,ü,ç,ğ,İ,ı,Ö,Ü,Ç,Ğ]",sifre):
                return "\nŞifre Türkçe karakterler içeremez."
            if not re.search(r"[0-9]",sifre):
                return "\nŞifre en az bir rakam içermelidir."
            
            temp_data['adSoyad'] = adSoyad
            break

        #E-posta Kontrol Mekanizması
        while True:
            eposta = input("E-postanızı Giriniz: ").strip()

            if not eposta:
                print("\n❌ E-posta boş bırakılamaz.")
                continue

            if not epostaDogrula(self,eposta):
                print("\n❌ Geçersiz e-posta formatı. Lütfen doğru e-posta formatı girin.")
                continue

            temp_data['eposta'] = eposta
            break
        
        #Telefon Numarası Kontrol Mekanizması
        while True:
            telno = input("Telefon Numaranızı Giriniz: ").strip()

            if not telno:
                print("\n ❌ Telefon Numarası boş bırakılamaz.")
                continue

            telno_hata = telnoDogrula(self,telno)
            if telno_hata:
                print(f"\n❌ Telefon Numarası Hatası: {telno_hata}")
                continue

            temp_data['telno'] = telno
            break
        
        #Kontrol edilerek alınan verilerin yazdırma işlemi yapılmadan önce ilgili değişkenlere atanması.
        self.__id = random.randint(1,1000)
        self.kullaniciAdi = temp_data["kullaniciAdi"]
        self.__sifre = temp_data["sifre"]
        self.__adSoyad = temp_data["adSoyad"]
        self.eposta = temp_data['eposta']
        self.telno = temp_data['telno']

        #! Kullanıcının ayrışabilmesi için rol bilgisi tutulması gerekmektedir şuanda data sets de rol bilgisi tutulmuyor!

        #TODO: data sets e rol bilgileri de eklenecek.

        KLASOR_ADI = "data_sets"
        DOSYA_YOLU = os.path.join(KLASOR_ADI,'kullanici_verileri.txt')
        if not os.path.exists(KLASOR_ADI):
            os.makedirs(KLASOR_ADI)
            print(f"Klasör Oluşturuldu: {KLASOR_ADI}")

        try:
            with open("Nesne Tabanlı Programlama Projesi/Proje/data_sets/kullanici_verileri.txt", "a", encoding="utf-8") as dosya:
                
                dosya.write("{\n")
                dosya.write(f"Kullanıcı Id = {self.__id}\n")
                dosya.write(f"Kullanici Adı = {self.kullaniciAdi}\n")
                dosya.write(f"Şifre = {self.__sifre} \n")
                dosya.write(f"İsim Soyisim = {self.__adSoyad}\n")
                dosya.write(f"Eposta = {self.eposta}\n")
                dosya.write(f"Telefon Numarası = {self.telno}\n")
                dosya.write("}\n")
            
            print(f"\n✅ Veriler başarıyla kaydedildi.")
        
        except IOError:
            print("❌ Dosya yazdırılamadı.")

    #!Hesap Güncelleme metodu daha tam fonksiyonel çalışmıyor!
    def _hesapGuncelleme(self):
        KLASOR_ADI = "Nesne Tabanlı Programlama Projesi/Proje/data_sets"
        DOSYA_YOLU = os.path.join(KLASOR_ADI,'kullanici_verileri.txt')
        kullanici_adi = input("Kullanıcı adınızı giriniz: ").strip()
        
        try:
            with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines
                kullanici_bulundu = False

                for i,satir in enumerate(tum_satirlar):
                    satir = satir.strip()
                    
                    if satir.startswith("Kullanici Adı ="):
                        kayitli_kullanici_adi = satir.split("=",1)[1].strip()

                        if kayitli_kullanici_adi == kullanici_adi:
                            guncel_kullanici_adi = input("Yeni kullanıcı adınızı giriniz: ").split()
                            kayitli_kullanici_adi = guncel_kullanici_adi
                            kullanici_bulundu = True

                            if satir.startswith("Şifre ="):
                                kayitli_kullanici_sifre = satir.split("=",1)[1].strip()
                                guncel_kullanici_sifre = input("Yeni şifrenizi giriniz: ").split()
                                kayitli_kullanici_sifre = guncel_kullanici_sifre
                                break
        except:
            if not kullanici_bulundu:
                    print("\n ❌ Giriş Başarısız. Kullanıcı adı veya şifre hatalı.")



    def epostaGonder(self,alici_eposta,guvenlik_kodu):

        # E-POSTA AYARLARI (Kendi bilgilerinizle değiştirin!)
        
        GONDEREN_EPOSTA = "wearbaseds@gmail.com"
        GONDEREN_SİFRE = "cynjkansrmfanemx"
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 465

        try:
            #Eposta içeriğini oluşturma:
            
            mesaj = EmailMessage()
            mesaj['From'] = GONDEREN_EPOSTA
            mesaj['To'] = alici_eposta
            mesaj['Subject'] = "Mesai Takip Otomasyonu - Şifre Sıfırlama Kodu"

            govde = f"""
            Şifre sıfırlama talebiniz alınmıştır.
            Lütfen aşağıdaki kodu uygulamaya girerek işlemi tamamlayınız:

            Güvenlik Kodu: {guvenlik_kodu}

            Bu kodu kimseyle paylaşmayın.
            """
            mesaj.set_content(govde)

            #Güvenli Bağlantı kullanarak SMTP sunucusuna bağlanma:

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT,context=context) as server:
                server.login(GONDEREN_EPOSTA,GONDEREN_SİFRE)
                server.sendmail(GONDEREN_EPOSTA,alici_eposta,mesaj.as_string())
            
            return True
        
        except smtplib.SMTPAuthenticationError:
            print("❌ Eposta gönderme hatası: SMTP kimlik doğrulaması başarısız. Uygulama şifrenizi kontrol edin.")
            return False
        except Exception as e:
            print("❌ Eposta gönderirken beklenmeyen bir hata oluştu {e}")
            return False
            



    def sifremiUnuttum(self):
        
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')

        print("\n ---- Şifre Sıfırlama İşlemi ----")
        
        girilen_eposta = input("Kayıtlı Eposta adresinizi giriniz: ").strip()

        try:
            with open(DOSYA_YOLU,'r', encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
            
            kayitli_kullanici_index = -1   #Eposta satırının indeksini tutar.
            kullanici_adi = None

            for i,satir in enumerate(tum_satirlar):
                satir_stripped = satir.strip()

                if satir_stripped.startswith("Eposta ="):
                    kayitli_eposta = satir_stripped.split("=", 1)[1].strip()

                    if kayitli_eposta == girilen_eposta:
                        kayitli_kullanici_index = i    #Eposta satırının indeksini kaydet.

                        if i - 3 >= 0 and tum_satirlar[i-3].strip().startswith("Kullanıcı Adı ="):
                            kullanici_adi = tum_satirlar[i-3].split("=",1)[1].strip()
                            break
            
            if kayitli_kullanici_index == -1:
                print("\n ❌ Bu eposta adresiyle kayıtlı kullanıcı bulunamadı.")
                return
            
            #Güvenlik Kodu Oluşturma ve Gönderme
            guvenlik_kodu = str(random.randint(100000, 999999))

            print(f"\n ⏳ {girilen_eposta} adresine güvenlik kodu gönderiliyor...")

            #epostaGonder() metodunun çağrılması
            gonderme_sonucu = self.epostaGonder(girilen_eposta,guvenlik_kodu)

            if not gonderme_sonucu:
                print("❌ Güvenlik kodu gönderilemedi. Lütfen ayarlarınızı kontrol edin.")
                return
            
            print("✅ Güvenlik kodu başarıyla gönderildi. Lütfen eposta kutunuzu kontrol edin.")

            #Güvenlik kodunun doğrulanması
            #?Kullanıcı bir defa güvenlik kodunu yanlış girdiğinde üç defa daha girme hakkı olmalı eğer üç defa yanlış girerse o zaman şifre sıfırlama işlemi iptal edilmeli bu fikri yapmayı bir düşün.
            girilen_kod = input("E-postanıza gelen güvenlik kodunu giriniz: ").strip()

            if girilen_kod != guvenlik_kodu:
                print("\n ❌ Güvenlik kodu hatalı. Şifre sıfırlama işlemi iptal edildi.")
                return
            
            #Yeni şifre girişi.
            
            while True:
                yeni_sifre1 = input("Yeni Şifreniz: ").strip()
                yeni_sifre2 = input("Yeni Şifreniz (Tekrar): ").strip()

                #Şifre kontrolü yapılıyor.

                if not yeni_sifre1 or len(yeni_sifre1) < 4:
                    print("❌ Şifre boş olamaz ve en az 4 karakter olmalıldır.")
                    continue

                if yeni_sifre1 != yeni_sifre2:
                    print("❌ Şifreler eşleşmiyor. Lütfen tekrar deneyin.")
                
                else:
                    break    #Şifre eşleşti döngüden çıkılıyor.
                
            # 6. Şifre Güncelleme İşlemi (Dosyaya Yazma)
        
            # Şifre satırının indisini bulma (E-posta satırının 2 satır yukarısı varsayılır)
            # Sizin kayıt formatınıza göre bu indisi (kayitli_kullanici_index - X) KONTROL EDİN!

            sifre_satir_index = kayitli_kullanici_index - 2

            #Satırın şifre satırı olup olmadığı kontrol etme.
            if sifre_satir_index >= 0 and tum_satirlar[sifre_satir_index].strip().startswith("Şifre ="):

                #Eski şifrenin üzerine yeni şifreyi yazma.
                tum_satirlar[sifre_satir_index] = f"Şifre = {yeni_sifre1}\n"

                #Değiştirilmiş tüm satırları dosyaya baştan yazma.
                with open(DOSYA_YOLU, 'w',encoding="utf-8") as dosya:
                    dosya.writelines(tum_satirlar)
                
                print(f"\n✅ Tebrikler! Şifreniz başarıyla güncellendi, {kullanici_adi}.")
            
            else:
                print("\n❌ Şifre satırı bulunamadı. Dosya formatında hata oluştu.")
    
        
        except FileNotFoundError:
            print(f"\n ❌ Kayıt dosyası bulunamadı: {DOSYA_YOLU}")

        except Exception as e:
            print(f"\n ❌ Şifre sıfırlama sırasında beklenmeyen bir hata oluştu: {e}")





    ####### Getter Setter Metotları #######

    @property
    def idGetSet(self):               #id attribute için getter metodu.
        return self.__id
    
    @idGetSet.setter                  #id attribute için setter metodu.
    def idGetSet(self,newId):
        if not newId:
            raise ValueError("Id değeri boş olamaz.")
        self.__id = newId


    @property
    def sifreGetSet(self):          #sifre attribute için getter metodu.
        return self.__sifre
    
    @sifreGetSet.setter             #sifre attribute için setter metodu.
    def sifreGetSet(self,yeni_sifre):
        if not yeni_sifre:
            raise ValueError("yeni şifre değeri boş olamaz.")
        self.__sifre = yeni_sifre

    
    @property
    def adSoyadGetSet(self):        #adSoyad attribute için getter metodu.
        return self.__adSoyad
    
    @adSoyadGetSet.setter           #adSoyad attribute için setter metodu.
    def adSoyadGetSet(self,yeni_isim):
        if not yeni_isim:
            raise ValueError("İsim soyisim değeri boş olamaz.")
        self.__adSoyad = yeni_isim




kullanici1 = Kullanici("02240201169","ÇalışkanKafa44","123456","Murat Korkmaz","muratkorkmaz@gmail.com","+90 579 632 11 21")



class Personel(Kullanici):      #Kullanici sınıfından kalıtım yoluyla türetilen Personel sınıfı.
    def __init__(self, id="02240201169", kullaniciAdi="ÇılgınÇalışan44", sifre="123456", adSoyad="Mustafa Gül", eposta="mustafagul@gmail.com", telno="+90 579 431 52 38", mesaiSaati=8, izinHakki=5):
        super().__init__(id,kullaniciAdi,sifre,adSoyad,eposta,telno)
        self.mesaiSaati = mesaiSaati
        self.izinHakki = izinHakki

        ####### Claasa ait Metotlar #######

    def mesaiGirisYap(self):
        pass

    def mesaiCikisYap(self):
        pass

    def izinTalepEt(self):
        pass

    def dosyaEkle(self):
        pass
        


personel1 = Personel("09:00","5")

print(personel1.adSoyadGetSet)
        

class Admin(Kullanici):
    def __init__(self,personelMesaiSaati,personelIzinHakki):
        self.personelMesaiSaati = personelMesaiSaati
        self.personelIzinHakki = personelIzinHakki

        ####### Claasa ait Metotlar #######
    
    def _personelEkle(self):
        pass

    def _personelSil(self):
        pass

    def _personelGoruntule(self):
        pass

    def _mesaiKaydiGoruntule(self):
        pass

    def _izinOnayla(self):
        pass

    def _izinTalepGoruntule(self):
        pass

    def _izinHakkiGoruntuleme(self):
        pass
