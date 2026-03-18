import os
from datetime import datetime, timedelta
from kullanici import Kullanici

class Personel(Kullanici):
    def __init__(self, id="02240201169", kullaniciAdi="ÇılgınÇalışan44", sifre="123456", adSoyad="Mustafa Gül", eposta="mustafagul@gmail.com", telno="+90 579 431 52 38", mesaiSaati=8, izinHakki=30):
        super().__init__(id, kullaniciAdi, sifre, adSoyad, eposta, telno)
        self.mesaiSaati = mesaiSaati
        self.izinHakki = izinHakki

    ####### Claasa ait Metotlar #######

    def mesaiGirisYap(self, oturum_kullanici_adi):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelMesai.txt')

        if not os.path.exists(KLASOR_ADI):
            os.makedirs(KLASOR_ADI)

        simdi = datetime.now()
        giris_tarihi = simdi.strftime("%d-%m-%Y")
        giris_saati = simdi.strftime("%H:%M:%S")

        mesai_key = f"{oturum_kullanici_adi}_{giris_saati}"
        kayit_satiri = f"KEY={mesai_key} | USER={oturum_kullanici_adi} | DATE={giris_tarihi} | GIRIS={giris_saati} | CIKIS=Yok\n"

        if self._mesaiKaydiMevcutMu(mesai_key):
            print("\n Hata: Bugün için mesai girşiniz zaten yapılmış.")
            return False
        
        try:
            with open(DOSYA_YOLU_MESAI, 'a', encoding="utf-8") as dosya:
                dosya.write(kayit_satiri)
            print(f"\n ✅ Mesai Girşi Başarılı: {oturum_kullanici_adi} - {giris_saati}")
            return True
        except IOError:
            print(f"\n ❌ Dosya yazma hatası: {DOSYA_YOLU_MESAI} yolunu kondrol edin.")
            return False
        
    def _mesaiKaydiMevcutMu(self, mesai_key):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelMesai.txt')
        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if mesai_key in satir and "CIKIS=YOK" in satir:
                        return True
            return False
        except FileNotFoundError:
            return False 
        
    def mesaiCikisYap(self, oturum_kullanici_adi):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelMesai.txt')

        simdi = datetime.now()
        cikis_saati = simdi.strftime("%H:%M:%S")

        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
            
            guncellendi = False
            for i, satir in reversed(list(enumerate(tum_satirlar))):
                if f"USER={oturum_kullanici_adi}" in satir and "CIKIS=Yok" in satir:
                    try:
                        giris_zamani_str = satir.split("GIRIS=")[1].split(" |")[0].strip()
                    except:
                        continue
                    yeni_satir = satir.replace("CIKIS=Yok", f"CIKIS={cikis_saati}")
                    tum_satirlar[i] = yeni_satir
                    guncellendi = True
                    break
                
            if guncellendi:
                with open(DOSYA_YOLU_MESAI, "w", encoding="utf-8") as dosya:
                    dosya.writelines(tum_satirlar)
                    print("\n ✅ Mesai çıkış saati sisteme kaydedildi.")
                    print(f"GĞncel Toplam Puanınız: {self._guncellePuanGetir(oturum_kullanici_adi)}")
            else:
                print("\n ❌ Açık mesai kaydınız bulunmadı. Lütfen önce mesai girişi yapınız.")
        except FileNotFoundError:
            print(f"\n ❌ Kayıt dosyası bulunamadı: {DOSYA_YOLU_MESAI}")
        except Exception as e:
            print(f"\n ❌ Mesai çıkışı sırsında bir hata oluştu: {e}")

    def _guncellePuanGetir(self, oturum_kullanici_adi):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelMesai.txt')
        toplam_puan = 0.0
        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if f"USER={oturum_kullanici_adi}" in satir and "GIRIS=" in satir and "CIKIS=" in satir:
                        if "IZIN_MIKTARI=" not in satir:
                            giris_zamani_str = satir.split("GIRIS=")[1].split(" |")[0].strip()
                            cikis_zamani_str = satir.split("CIKIS=")[1].split(" |")[0].strip()
                            if cikis_zamani_str != 'Yok':
                                try:
                                    giris_saati = datetime.strptime(giris_zamani_str, "%H:%M:%S").time()
                                    cikis_saati = datetime.strptime(cikis_zamani_str, "%H:%M:%S").time()
                                    temp_date = datetime.now().date()
                                    giris_dt = datetime.combine(temp_date, giris_saati)
                                    cikis_dt = datetime.combine(temp_date, cikis_saati)
                                    if cikis_dt < giris_dt:
                                        cikis_dt += timedelta(days=1)
                                    fark = cikis_dt - giris_dt
                                    calisilan_saat = fark.total_seconds()/3600
                                    
                                    if calisilan_saat >= 5:
                                        temel_calisma_saati = min(calisilan_saat, 8)
                                        toplam_puan += temel_calisma_saati * 12.5
                                        ek_mesai_saati = max(0, calisilan_saat - 8)
                                        ek_mesai_saati = min(ek_mesai_saati, 2)
                                        toplam_puan += ek_mesai_saati * 25
                                except ValueError:
                                    continue
        except FileNotFoundError:
            return 0.0
        return round(toplam_puan, 2)
    
    def _sonIzinTarihiGetir(self, oturum_kullanici_adi, dosya_yolu):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelMesai.txt')
        son_provizyon_tarihi = None
        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                for satir in reversed(list(dosya)):
                    if f"USER={oturum_kullanici_adi}" in satir and "IZIN_MIKTARI=" in satir:
                        try:
                            tarih_str = satir.split("TARIH=")[1].split(" |")[0].strip()
                            son_provizyon_tarihi = datetime.strptime(tarih_str, "%d-%m-%Y")
                            return son_provizyon_tarihi
                        except:
                            continue
        except FileNotFoundError:
            return None
        return son_provizyon_tarihi

    def izinTalepEt(self, oturum_kullanici_adi):
        guncel_puan = self._guncellePuanGetir(oturum_kullanici_adi)
        print(f"\n ### 🌴 İzin Talep Etme ###")
        print(f"Güncel İzin Hakkınız: {self.izinHakki} gün")
        print(f"Güncel Puanınız: {guncel_puan:.2f} puan")

        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_IZIN = os.path.join(KLASOR_ADI, 'PersonelIzin.txt')

        son_izin_tarihi = self._sonIzinTarihiGetir(oturum_kullanici_adi, DOSYA_YOLU_IZIN)
        simdi = datetime.now()
        bugun_tarih = simdi.strftime("%d-%m-%Y")
        
        if self._bugunTalepVarMi(oturum_kullanici_adi, bugun_tarih, DOSYA_YOLU_IZIN):
            print(f"\n ⚠️ Uyarı: {bugun_tarih} tarihi için zaten bir izin talebiniz mevcut.")
            print("Aynı gün içinde birden fazla talep oluşturamazsınız.")
            return

        if son_izin_tarihi:
            gecen_sure = simdi - son_izin_tarihi
            if gecen_sure.days < 14:
                kalan_gun = 14 - gecen_sure.days
                print(f"\n ❌ Hata: Son izin talebinizin üzerinden 14 gün geçmeden yeni izin talebi oluşturamazsınız.")
                print(f"Kalan süre: {kalan_gun} gün.")
                return

        while True:
            try:
                talep_miktar = int(input("Talep ettiğiniz izin miktarı(gün): "))
                if talep_miktar <= 0:
                    print("❌ İzin miktarı pozitif bir sayı olmalıdır.")
                    continue
                if talep_miktar > self.izinHakki:
                    print(f"❌ Hata: Talep ettiğiniz izin miktarı ({talep_miktar} gün) kalan izin hakkınızdan ({self.izinHakki} gün) fazla olamaz.")
                    continue
                break
            except ValueError:
                print("❌ Geçerli bir sayı giriniz")

        tarih_str = bugun_tarih
        saat_str = simdi.strftime("%H:%M:%S")
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelIzin.txt')
        kayit_satiri = f"KEY=IZIN_{oturum_kullanici_adi}_{tarih_str} | USER={oturum_kullanici_adi} | TARIH={tarih_str} | SAAT={saat_str} | IZIN_MIKTARI={talep_miktar} | PUAN={guncel_puan:.2f} | DURUM=Provizyon\n"

        try:
            with open(DOSYA_YOLU_MESAI, "a", encoding="utf-8") as dosya:
                dosya.write(kayit_satiri)
                print(f"\n ✅ İzin talebiniz ({talep_miktar} gün) sisteme kaydedildi ve **PROVİZYON** durumundadır.")
                print("Onay durumunu bekleyiniz, bir günü geçen provizyon işlemlerinde hala geri dönüş olmaması durumunda genel müdürünüze haber veriniz.")
                return True
        except IOError:
            print(f"\n ❌ Dosya yazma hatası: {DOSYA_YOLU_MESAI}")
            return False
    
    def _bugunTalepVarMi(self, kullanici_adi, tarih, dosya_yolu):
        try:
            with open(dosya_yolu, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if f"USER={kullanici_adi}" in satir and f"TARIH={tarih}" in satir:
                        return True
            return False
        except FileNotFoundError:
            return False

    def dosyaEkle(self):
        pass