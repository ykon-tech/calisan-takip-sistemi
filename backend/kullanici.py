import random
import os
import re
# Yeni servisler import edildi
from utils import Validator
from email_service import EmailService

class Kullanici(object):
    def __init__(self, __id="02240201169", kullaniciAdi="ÇalışanAbi44", __sifre="123456", __adSoyad="Mustafa Gül", eposta="mustafagul@gmail.com", telno="+90 537 823 45 61", kullaniciRolu="Seçilmedi"):
        self.__id = __id
        self.kullaniciAdi = kullaniciAdi
        self. __sifre = __sifre
        self.__adSoyad = __adSoyad
        self.eposta = eposta
        self.telno = telno
        self.kullaniciRolu = kullaniciRolu

    ####### Class'a ait Metotlar #######

    def _girisYap(self):
        KLASOR_ADI = "Nesne Tabanlı Programlama Projesi/Proje/data_sets"
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')
        giris_kullanici_adi = input("Kullanıcı Adı: ").strip()
        giris_sifre = input("Şifre: ").strip()

        try:
            with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
                kullanici_bulundu = False

                for i, satir in enumerate(tum_satirlar):
                    satir = satir.strip()
                    
                    if satir.startswith("Kullanici Adı ="):
                        kayitli_kullanici_adi = satir.split("=", 1)[1].strip()

                        if kayitli_kullanici_adi == giris_kullanici_adi:
                            if i + 1 < len(tum_satirlar):
                                sifre_satiri = tum_satirlar[i+1].strip()
                                if sifre_satiri.startswith("Şifre ="):
                                    kayitli_sifre = sifre_satiri.split("=", 1)[1].strip()

                                    if kayitli_sifre == giris_sifre:
                                        bulanan_rol = "Çalışan"  # Varsayılan rol
                                        for k in range(1, 10):
                                            if i + k < len(tum_satirlar):
                                                rol_satiri = tum_satirlar[i+k].strip()
                                                if rol_satiri.startswith("Rol ="):
                                                    bulanan_rol = rol_satiri.split("=", 1)[1].strip()
                                                    break

                                        kullanici_bulundu = True
                                        print(f"\n ✅ Giriş Başarılı! Hoş geldiniz, {giris_kullanici_adi}.")
                                        return kullanici_bulundu, giris_kullanici_adi, bulanan_rol
                                        break
                if not kullanici_bulundu:
                    print("\n ❌ Giriş Başarısız. Kullanıcı adı veya şifre hatalı.")
                    return False, None, None
        except FileNotFoundError:
            print(f"\n❌ Kayıtlı kullanıcı bulunamadı. Lütfen önce kayıt işlemi yaptırınız.")
            return False, None, None
        except Exception as e:
            print(f"\n❌ Giriş yaparken bir hata oluştu: {e}")
            return False, None, None

    def _cikisYap(self):
        print("Çıkış Yapılıyor...")
        print("\n✅ Sistemden Başarıyla Çıkış Yapıldı.")

    def kayitOl(self):
        
        # Kontrol Mekanizmaları
        if not self.kullaniciAdi or not self.__sifre or not self.__adSoyad or not self.eposta or not self.telno:
            print("\n ❌ Kullanıcı adı ve şifre gibi bilgiler boş bırakılamaz veya sadece boşluklardan oluşamaz.")
            return -1
        
        temp_data = {}
        
        # Kullanıcı Adı Kontrol
        while True:
            kullanici_adi = input("Kullanıcı Adınızı Giriniz: ").strip()

            if not kullanici_adi:
                print("\n ❌ Kullanıcı adı boş bırakılamaz.")
                continue 

            if ' ' in kullanici_adi:
                print("\n ❌ Kullanıcı adı boşluk içeremez.")
                continue
            
            if re.search(r"[ö,ü,ç,ğ,İ,ı,Ö,Ü,Ç,Ğ]", kullanici_adi):
                 print("Kullanıcı adı Türkçe karakterler içeremez.")
                 continue
            
            if len(kullanici_adi) < 8:
                print("\nKullanıcı adı minumum 8 karakterli olabilir.")
                continue

            if len(kullanici_adi) >= 16:
                print("\nKullanıcı adı maksimum 16 karakterli olabilir.")
                continue

            if not re.search(r"[A-Z]", kullanici_adi):
                print("\nKullanıcı adı en az bir büyük harf içermelidir.")
                continue
            
            if not re.search(r"[a-z]", kullanici_adi):
                print("\nKullanıcı adı en az bir küçük harf içermelidir.")
                continue
                
            temp_data['kullaniciAdi'] = kullanici_adi
            break
        
        # Şifre Kontrol - ARTIK SERVİS KULLANIYOR
        while True:
            sifre = input("Şifrenizi Giriniz: ").strip()
            if not sifre:
                print("\n ❌ Şifre boş bırakılamaz.")
                continue

            # ! Servis Çağrısı
            sifre_hata = Validator.sifreGuvenlikKontrol(sifre)
            if sifre_hata:
                print(f"\n❌ Şifre Hatası: {sifre_hata}")
                continue

            temp_data['sifre'] = sifre
            break

        # İsim Soyisim Kontrol
        while True:
            adSoyad = input("Adınızı Soyadınızı Giriniz: ").strip()
            if not adSoyad:
                print("\n ❌ Ad Soyad alanı boş bırakılamaz.")
                continue
            
            temp_data['adSoyad'] = adSoyad
            break

        # E-posta Kontrol - ARTIK SERVİS KULLANIYOR
        while True:
            eposta = input("E-postanızı Giriniz: ").strip()
            if not eposta:
                print("\n❌ E-posta boş bırakılamaz.")
                continue

            # ! Servis Çağrısı
            if not Validator.epostaDogrula(eposta):
                print("\n❌ Geçersiz e-posta formatı. Lütfen doğru e-posta formatı girin.")
                continue

            temp_data['eposta'] = eposta
            break
        
        # Telefon Numarası Kontrol - ARTIK SERVİS KULLANIYOR
        while True:
            telno = input("Telefon Numaranızı Giriniz: ").strip()
            if not telno:
                print("\n ❌ Telefon Numarası boş bırakılamaz.")
                continue

            # ! Servis Çağrısı
            telno_hata = Validator.telnoDogrula(telno)
            if telno_hata:
                print(f"\n❌ Telefon Numarası Hatası: {telno_hata}")
                continue

            temp_data['telno'] = telno
            break

        # Rol bilgisi kontrol
        print("\n#####Roller#####")
        print("1- Admin")
        print("2- Çalışan")

        kullaniciRol = input("Lütfen rolünüzü seçiniz: ").strip()
        while True:
            print("#####Roller#####")
            print("1- Admin")
            print("2- Çalışan")

            if kullaniciRol == "1":
                self.kullaniciRolu = "Admin"
                break
            elif kullaniciRol == "2":
                self.kullaniciRolu = "Çalışan"
                break
            else:
                print("❌ Herhangi bir rol seçilemedi.")
                kullaniciRol = input("Lütfen rolünüzü seçiniz: ").strip()
                if kullaniciRol == "1" or kullaniciRol == "2":
                    continue
                
        
        self.__id = random.randint(1, 1000)
        self.kullaniciAdi = temp_data["kullaniciAdi"]
        self.__sifre = temp_data["sifre"]
        self.__adSoyad = temp_data["adSoyad"]
        self.eposta = temp_data['eposta']
        self.telno = temp_data['telno']

        KLASOR_ADI = "data_sets"
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')
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
                dosya.write(f"Rol = {self.kullaniciRolu}\n")
                dosya.write("}\n")
            
            print(f"\n✅ Veriler başarıyla kaydedildi.")
        except IOError:
            print("❌ Dosya yazdırılamadı.")

    def _hesapGuncelleme(self, eski_kullanici_adi):
        KLASOR_ADI = "Nesne Tabanlı Programlama Projesi/Proje/data_sets"
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')
        
        print(f"\n ---- Hesap Bilgileri Güncelleme {eski_kullanici_adi} ---")

        while True:
            yeni_kullanici_adi = input("Yeni Kullanıcı Adınızı Giriniz: ").strip()

            if not yeni_kullanici_adi:
                yeni_kullanici_adi = eski_kullanici_adi
                print("\nKullanıcı adı değiştirilmedi.")
                break

            if ' ' in yeni_kullanici_adi:
                print("\n ❌ Kullanıcı adı boşluk içeremez.")
                continue
            
            if re.search(r"[ö,ü,ç,ğ,İ,ı,Ö,Ü,Ç,Ğ]", yeni_kullanici_adi):
                 print("Kullanıcı adı Türkçe karakterler içeremez.")
                 continue
            
            if len(yeni_kullanici_adi) < 8:
                print("\nKullanıcı adı minumum 8 karakterli olabilir.")
                continue

            if len(yeni_kullanici_adi) >= 16:
                print("\nKullanıcı adı maksimum 16 karakterli olabilir.")
                continue

            if not re.search(r"[A-Z]", yeni_kullanici_adi):
                print("\nKullanıcı adı en az bir büyük harf içermelidir.")
                continue
            
            if not re.search(r"[a-z]", yeni_kullanici_adi):
                print("\nKullanıcı adı en az bir küçük harf içermelidir.")
                continue

            break

        while True:
            yeni_eposta = input("Yeni E-posta Adresinizi Giriniz: ").strip()

            if not yeni_eposta:
                yeni_eposta = None
                print("E-posta adresi değiştirilmedi.")
                break

            # ! Servis Çağrısı
            if not Validator.epostaDogrula(yeni_eposta):
                print("\n❌ Geçersiz e-posta formatı. Lütfen doğru e-posta formatı girin.")
                continue

            break

        if yeni_kullanici_adi == eski_kullanici_adi and yeni_eposta is None:
            print("\n ℹ️ Hiçbir bilgi gğncellenmedi. İşlem iptal edildi.")
            return

        try:
            with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
                guncelleme_yapildi = False

                for i, satir in enumerate(tum_satirlar):
                    satir_stripped = satir.strip()
                    if satir_stripped.startswith("Kullanici Adı ="):
                        kayitli_kullanici_adi = satir_stripped.split("=", 1)[1].strip()

                        if kayitli_kullanici_adi == eski_kullanici_adi:
                            if yeni_kullanici_adi != eski_kullanici_adi:
                                tum_satirlar[i] = f"Kullanıcı Adı = {yeni_kullanici_adi}\n"
                                guncelleme_yapildi = True

                            eposta_index = i + 3
                            if yeni_eposta is not None and eposta_index < len(tum_satirlar):
                                if tum_satirlar[eposta_index].strip().startswith("Eposta ="):
                                    tum_satirlar[eposta_index] = f"Eposta = {yeni_eposta}\n"
                                    guncelleme_yapildi = True
                            break

                if guncelleme_yapildi:
                    with open(DOSYA_YOLU, 'w', encoding="utf-8") as dosya:
                        dosya.writelines(tum_satirlar)
                    print(f"\n ✅ Hesap bilgileri başarıyla güncellendi.")

                    if yeni_kullanici_adi != eski_kullanici_adi:
                        return yeni_kullanici_adi
                    else:
                        return eski_kullanici_adi
                else:
                    print("\n ℹ️ Güncellenecek kayıt bulunamadı.")
                    return eski_kullanici_adi
        except FileNotFoundError:
            print(f"\n ❌ Kayıt dosyası bulunumadı: {DOSYA_YOLU}")
            return eski_kullanici_adi
        except Exception as e:
            print(f"\n ❌ Güncelleme sırasında beklenmeyen bir hata oluştu {e}")
            return eski_kullanici_adi

    def sifremiUnuttum(self):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')

        print("\n ---- Şifre Sıfırlama İşlemi ----")
        girilen_eposta = input("Kayıtlı Eposta adresinizi giriniz: ").strip()

        try:
            with open(DOSYA_YOLU, 'r', encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
            
            kayitli_kullanici_index = -1
            kullanici_adi = None

            for i, satir in enumerate(tum_satirlar):
                satir_stripped = satir.strip()
                if satir_stripped.startswith("Eposta ="):
                    kayitli_eposta = satir_stripped.split("=", 1)[1].strip()
                    if kayitli_eposta == girilen_eposta:
                        kayitli_kullanici_index = i
                        if i - 3 >= 0 and tum_satirlar[i-3].strip().startswith("Kullanıcı Adı ="):
                            kullanici_adi = tum_satirlar[i-3].split("=", 1)[1].strip()
                            break
            
            if kayitli_kullanici_index == -1:
                print("\n ❌ Bu eposta adresiyle kayıtlı kullanıcı bulunamadı.")
                return
            
            guvenlik_kodu = str(random.randint(100000, 999999))
            print(f"\n ⏳ {girilen_eposta} adresine güvenlik kodu gönderiliyor...")

            # ! Servis Çağrısı - Eposta Gönderme
            konu = "Mesai Takip Otomasyonu - Şifre Sıfırlama Kodu"
            govde = f"""
            Şifre sıfırlama talebiniz alınmıştır.
            Lütfen aşağıdaki kodu uygulamaya girerek işlemi tamamlayınız:

            Güvenlik Kodu: {guvenlik_kodu}

            Bu kodu kimseyle paylaşmayın.
            """
            
            gonderme_sonucu = EmailService.gonder(girilen_eposta, konu, govde)

            if not gonderme_sonucu:
                print("❌ Güvenlik kodu gönderilemedi. Lütfen ayarlarınızı kontrol edin.")
                return
            
            print("✅ Güvenlik kodu başarıyla gönderildi. Lütfen eposta kutunuzu kontrol edin.")

            sayac = 3
            while sayac > 0:
                girilen_kod = input("E-postanıza gelen güvenlik kodunu giriniz: ").strip()
                if girilen_kod == guvenlik_kodu:
                    break
                sayac -= 1
                print(f"\n❌ Hatalı giriş yaptınız, kalan giriş hakkı: {sayac}")
                
            if girilen_kod != guvenlik_kodu:
                print("\n ❌ Güvenlik kodu hatalı. Şifre sıfırlama işlemi iptal edildi.")
                return
            
            while True:
                yeni_sifre1 = input("Yeni Şifreniz: ").strip()
                yeni_sifre2 = input("Yeni Şifreniz (Tekrar): ").strip()

                if not yeni_sifre1 or len(yeni_sifre1) < 4:
                    print("❌ Şifre boş olamaz ve en az 4 karakter olmalıldır.")
                    continue

                if yeni_sifre1 != yeni_sifre2:
                    print("❌ Şifreler eşleşmiyor. Lütfen tekrar deneyin.")
                else:
                    break
            
            sifre_satir_index = kayitli_kullanici_index - 2
            if sifre_satir_index >= 0 and tum_satirlar[sifre_satir_index].strip().startswith("Şifre ="):
                tum_satirlar[sifre_satir_index] = f"Şifre = {yeni_sifre1}\n"
                with open(DOSYA_YOLU, 'w', encoding="utf-8") as dosya:
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
    def idGetSet(self):
        return self.__id
    
    @idGetSet.setter
    def idGetSet(self, newId):
        if not newId:
            raise ValueError("Id değeri boş olamaz.")
        self.__id = newId

    @property
    def sifreGetSet(self):
        return self.__sifre
    
    @sifreGetSet.setter
    def sifreGetSet(self, yeni_sifre):
        if not yeni_sifre:
            raise ValueError("yeni şifre değeri boş olamaz.")
        self.__sifre = yeni_sifre

    @property
    def adSoyadGetSet(self):
        return self.__adSoyad
    
    @adSoyadGetSet.setter
    def adSoyadGetSet(self, yeni_isim):
        if not yeni_isim:
            raise ValueError("İsim soyisim değeri boş olamaz.")
        self.__adSoyad = yeni_isim