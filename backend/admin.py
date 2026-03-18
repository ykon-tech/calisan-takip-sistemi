import os
from datetime import datetime
from kullanici import Kullanici
from departman import Departman

class Admin(Kullanici):
    def __init__(self, personelMesaiSaati=8, personelIzinHakki=5):
        self.personelMesaiSaati = personelMesaiSaati
        self.personelIzinHakki = personelIzinHakki
        self.departmanlar = [
            Departman("Yazılım", 101),
            Departman("İnsan Kaynakları", 102),
            Departman("Muhasebe", 103),
            Departman("Satış", 104),
            Departman("Yönetim", 105)
        ]

    ####### Claasa ait Metotlar #######
    
    def _tumKullanicilariGetir(self):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')
        kullanicilar = []
        if not os.path.exists(DOSYA_YOLU):
            return []
        try:
            with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
                icerik = dosya.read()
                bloklar = icerik.split("}")
                for blok in bloklar:
                    if "{" in blok:
                        temiz_blok = blok.split("{")[1]
                        satirlar = temiz_blok.strip().split("\n")
                        kullanici_data = {}
                        kullanici_data['raw_blok'] = blok + "}\n"
                        for satir in satirlar:
                            if "=" in satir:
                                key, val = satir.split("=", 1)
                                kullanici_data[key.strip()] = val.strip()
                        if 'Kullanici Adı' in kullanici_data:
                            kullanicilar.append(kullanici_data)
                return kullanicilar
        except Exception as e:
            print(f"Veri okuma hatası: {e}")
            return []
            
    def _departmanSec(self):
        print("\n--- Departmanlar ---")
        departmanlar = ["Yazılım", "İnsan Kaynakları", "Muhasebe", "Satış", "Yönetim"]
        for i, dep in enumerate(departmanlar, 1):
            print(f"{i}- {dep}")
        while True:
            try:
                secim = int(input("Departman Seçiniz: "))
                if 1 <= secim <= len(departmanlar):
                    return departmanlar[secim-1]
                print("Geçersiz seçim.")
            except ValueError:
                print("Lütfen sayı giriniz.")

    def _personelEkle(self):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')
        while True:
            print("\n#### 👔 Departman Atama Paneli ####")
            print("1-) Çalışanı Departmana Ata/Değiştir")
            print("2-) Departman Listelerini Gör")
            print("3-) Geri Dön")
            secim = input("Seçiminiz: ")
            if secim == "2":
                self._personelGoruntule(mod="departman")
                continue
            elif secim == "3":
                break
            elif secim == "1":
                target_user = input("Departmana atanacak personelin Kullanıcı Adı: ").strip()
                kullanicilar = self._tumKullanicilariGetir()
                bulunan_kullanici = None
                for k in kullanicilar:
                    if k.get('Kullanici Adı') == target_user:
                        bulunan_kullanici = k
                        break
                if not bulunan_kullanici:
                    print("❌ Bu kullanıcı adına sahip  bir personel bulunamadı.")
                    continue
                print(f"\nSeçilen Personel: {bulunan_kullanici.get('İsim Soyisim')} (Şu anki Dept: {bulunan_kullanici.get('Departman', 'Yok')})")
                print("\n--- Hedef Departman ---")
                for i, dep in enumerate(self.departmanlar, 1):
                    print(f"{i}- {dep.departmanAdi}")
                try:
                    dep_secim = int(input("Departman Numarası Seçiniz: "))
                    if 1 <= dep_secim <= len(self.departmanlar):
                        secilen_dept_adi = self.departmanlar[dep_secim-1].departmanAdi
                    else:
                        print("Geçersiz seçim.")
                        continue
                except ValueError:
                    print("❌ Sayı giriniz.")
                    continue
                try:
                    with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
                        satirlar = dosya.readlines()
                    yeni_satirlar = []
                    user_blogunun_icinde = False
                    degisilik_yapildi = False
                    for satir in satirlar:
                        if f"Kullanici Adı = {target_user}" in satir:
                            user_blogunun_icinde = True
                        if user_blogunun_icinde and "}" in satir:
                            user_blogunun_icinde = False
                        if user_blogunun_icinde and satir.strip().startswith("Departman="):
                            yeni_satirlar.append(f"Departman= {secilen_dept_adi}\n")
                            degisilik_yapildi = True
                        elif user_blogunun_icinde and "}" in satir.strip() and not degisilik_yapildi:
                            yeni_satirlar.append(f"Departman = {secilen_dept_adi}\n")
                            yeni_satirlar.append(satir)
                            degisilik_yapildi = True
                            user_blogunun_icinde = False
                        else:
                            yeni_satirlar.append(satir)
                    with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
                        icerik = dosya.read()
                    bloklar = icerik.split("}")
                    final_icerik = ""
                    for blok in bloklar:
                        if f"Kullanici Adı = {target_user}" in blok:
                            satirlar = blok.strip().split("\n")
                            yeni_blok_satirlar = []
                            dept_var_mi = False
                            for s in satirlar:
                                if s.strip() == "{":
                                    yeni_blok_satirlar.append(s)
                                    continue
                                if s.strip().startswith("Departman ="):
                                    yeni_blok_satirlar.append(f"Departman = {secilen_dept_adi}")
                                    dept_var_mi = True
                                else:
                                    yeni_blok_satirlar.append(s)
                            if not dept_var_mi:
                                yeni_blok_satirlar.append(f"Departman = {secilen_dept_adi}")
                            final_icerik += "\n".join(yeni_blok_satirlar) + "\n}\n"
                        else:
                            if blok.strip():
                                final_icerik += blok + "}"
                    with open(DOSYA_YOLU, "w", encoding="utf-8") as dosya:
                        dosya.write(final_icerik)
                    print(f"\n ✅ {target_user} başarıyla {secilen_dept_adi} departmanına atandı.")
                except Exception as e:
                    print(f"Hata: {e}")
                            
    def _personelSil(self):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU = os.path.join(KLASOR_ADI, 'kullanici_verileri.txt')
        while True:
            print("\n### Departmandan Çalışan Çıkarma Paneli ###")
            print("1-) Çalışanı Departmandan Çıkar")
            print("2-) Departmandaki Çalışanları Gör")
            print("3-) Geri Dön")
            secim = input("Seçiminiz: ")
            if secim == "2":
                self._personelGoruntule(mod="departman")
                continue
            elif secim == "3":
                break
            elif secim == "1":
                target_user = input("Departmandan çıkarılacak personel kullanıcı adı: ")
                try:
                    with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
                        icerik = dosya.read()
                    bloklar = icerik.split("}")
                    final_icerik = ""
                    kullanici_bulundu = False
                    for blok in bloklar:
                        if f"Kullanici Adı = {target_user}" in blok:
                            kullanici_bulundu = True
                            satirlar = blok.strip().split("\n")
                            yeni_blok_satirlar = []
                            for s in satirlar:
                                if s.strip().startswith("Departman ="):
                                    yeni_blok_satirlar.append(f"Departman = Atanmamış")
                                else:
                                    yeni_blok_satirlar.append(s)
                            final_icerik += "\n".join(yeni_blok_satirlar) + "\n}\n"
                        else:
                            if blok.strip():
                                final_icerik += blok + "}"
                    if kullanici_bulundu:
                        with open(DOSYA_YOLU, "w", encoding="utf-8") as dosya:
                            dosya.write(final_icerik)
                        print(f"\n ✅ {target_user} departmandan çıkarıldı (Atanmamış yapıldı).")
                    else:
                        print("❌ Kullanıcı bulunamadı.")
                except Exception as e:
                    print(f"Hata {e}")

    def _personelGoruntule(self, mod="genel"):
        tum_kullanicilar = self._tumKullanicilariGetir()
        for dep in self.departmanlar:
            dep.personel_listesi = []
            for k in tum_kullanicilar:
                if k.get('Departman') == dep.departmanAdi:
                    dep._uyeEkle(k.get('Kullanici Adı'))
        filtrelenmis_liste = []
        baslik = ""
        if mod == "genel":
            filtrelenmis_liste = tum_kullanicilar
            baslik = "TÜM PERSONEL LİSTESİ (Karma)"
        elif mod == "departman":
            print("\n--- Mevcut Departmanlar ---")
            for i, dep in enumerate(self.departmanlar, 1):
                print(f"{i}- {dep.departmanAdi} (Mevcut Üye: {len(dep.uyeGoruntule())})")
            try:
                secim = int(input("Görüntülemek istediğiniz departman no: "))
                if 1 <= secim <= len(self.departmanlar):
                    secilen_dept_nesnesi = self.departmanlar[secim-1]
                    baslik = f"{secilen_dept_nesnesi.departmanAdi.upper()} DEPARTMANI"
                    uye_isimleri = secilen_dept_nesnesi.uyeGoruntule()
                    for k in tum_kullanicilar:
                        if k.get('Kullanici Adı') in uye_isimleri:
                            filtrelenmis_liste.append(k)
                else:
                    print("Geçersiz seçim.")
                    return
            except Exception as e:
                print(f"Hatalı giriş. {e}")
                return
        print(f"\n#### 👥 {baslik} ####")
        print("-" * 110)
        print(f"| {'Kullanıcı Adı':<20} | {'Ad Soyad':<20} | {'Departman':<18} | {'Rol':<10} | {'Telefon':<15} |")
        print("-" * 110)
        if not filtrelenmis_liste:
            print(f"| {'Kayıt Bulunamadı':<106}|")
        else:
            for k in filtrelenmis_liste:
                dept = k.get("Departman", "Atanmamış")
                print(f"| {k.get('Kullanici Adı', '-'):<20} | {k.get('İsim Soyisim', '-'):<20} | {dept:<18} | {k.get('Rol', '-'):<10} | {k.get('Telefon Numarası', '-'):<15} |")
        print("-" * 110)
        
    def _mesaiKaydiGoruntule(self):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelMesai.txt')
        print("\n#### 📅 Personel Mesai Kayıtları ####")
        if not os.path.exists(DOSYA_YOLU_MESAI):
            print("❌ Henüz mesai kaydı bulunmamaktadır.")
            return
        print("-" * 85)
        print(f"| {'Tarih':<12} | {'Kullanıcı Adı':<20} | {'Giriş':<10} | {'Çıkış':<10} | {'Durum':<12} |")
        print("-" * 85)
        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if "GIRIS=" in satir and "USER=" in satir:
                        data = {}
                        parts = satir.strip().split("|")
                        for p in parts:
                            if "=" in p:
                                key, value = p.split("=", 1)
                                data[key.strip()] = value.strip()
                        tarih = data.get("DATE", "-")
                        user = data.get("USER", "-")
                        giris = data.get("GIRIS", "-")
                        cikis = data.get("CIKIS", "-")
                        durum = "🔴 İçerde" if cikis == "Yok" else "🟢 Tamamlandı"
                        print(f"| {tarih:<12} | {user:<20} | {giris:<10} | {cikis:<10} | {durum:<12} |")
            print("-" * 85)
        except Exception as e:
            print(f"Okuma hatası: {e}")

    def _provizyonIzinleriOku(self):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelIzin.txt')
        provizyon_listesi = []
        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    if "IZIN_MIKTARI=" in satir and "DURUM=Provizyon" in satir:
                        data = {}
                        parts = satir.strip().split("|")
                        for part in parts:
                            part = part.strip()
                            if "=" in part:
                                key, value = part.split("=", 1)
                                data[key.strip()] = value.strip()
                        try:
                            miktar = int(data.get('IZIN_MIKTARI', 0))
                        except ValueError:
                            miktar = 0
                        try:
                            puan = float(data.get('PUAN', 0.0))
                        except ValueError:
                            puan = 0.0
                        provizyon_listesi.append({
                            'key': data.get('KEY'),
                            'kullanici_adi': data.get('USER'),
                            'tarih': data.get('TARIH'),
                            'miktar': miktar,
                            'puan': puan,
                            'satir': satir
                        })
        except FileNotFoundError:
            print(f"\n ❌ Kayıt dosyası bulunamadı: {DOSYA_YOLU_MESAI}")
        return provizyon_listesi

    def _izinOnayla(self):
        provizyon_listesi = self._provizyonIzinleriOku()
        if not self._izinTalepGoruntule(provizyon_listesi):
            self._kontrolcuCalistir(provizyon_listesi)
            return
        print("\n#### ✍️ İzin Taleplerini Değerlendirme ####")
        print("Admin: 'y' (Onayla), 'n' (Reddet), 'q' (Çıkış)")
        islemler = []
        for i, talep in enumerate(provizyon_listesi):
            kullanici_adi = talep['kullanici_adi']
            miktar = talep['miktar']
            while True:
                karar = input(f"{i+1}. {kullanici_adi} {miktar} gün -> Kararınız [y/n/q]").strip().lower()
                if karar == 'y':
                    islemler.append((i, "Onay"))
                    print(f"✅ {kullanici_adi} izni ONAYLANDI (Admin)")
                    break
                elif karar == 'n':
                    islemler.append((i, "Ret"))
                    print(f"❌ {kullanici_adi} izni REDDEDİLDİ (Admin)")
                    break
                elif karar == 'q':
                    print("\n Admin değerlendirilmesi sonlandırıldı.")
                    break
                else:
                    print("❌ Geçersiz giriş işlemi.")
            if karar == 'q':
                break
        if islemler:
            self._izinKayitlariniGuncelle(provizyon_listesi, islemler)
            self._kontrolcuCalistir(provizyon_listesi)

    def _izinKayitlariniGuncelle(self, provizyon_listesi, islemler_listesi):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelIzin.txt')
        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
                yeni_satirlar = []
                guncellenen_keyler = {provizyon_listesi[i[0]]['key']: i[1] for i in islemler_listesi}
                for satir in tum_satirlar:
                    satir_yazildi = False
                    if "DURUM=Provizyon" in satir and "IZIN_MIKTARI=" in satir:
                        for key, karar in guncellenen_keyler.items():
                            if key in satir:
                                yeni_durum = "Onay" if karar == "Onay" else "Ret"
                                guncellenmis_satir = satir.replace("DURUM=Provizyon", f"DURUM={yeni_durum} (Admin)")
                                yeni_satirlar.append(guncellenmis_satir)
                                satir_yazildi = True
                                break
                        if not satir_yazildi:
                            yeni_satirlar.append(satir)
                    else:
                        yeni_satirlar.append(satir)
                    with open(DOSYA_YOLU_MESAI, "w", encoding="utf-8") as dosya:
                        dosya.writelines(yeni_satirlar)
                    print("\n ✅ Admin kararları dosyaya kaydedildi.")
        except Exception as e:
            print(f"\n ❌ Dosya güncelleme sırasında beklenmeyen bir hata oldu: {e}")
    
    def _kontrolcuCalistir(self, tum_provizyonlar):
        simdi = datetime.now()
        degerlendirilmeyen_talepler = [t for t in tum_provizyonlar if 'Provizyon' in t['satir']]
        if not degerlendirilmeyen_talepler:
            print("ℹ️ Kontrolcü: Değerlendirilmeyen talep yok.")
            return
        if simdi.hour == 0 and simdi.minute == 0:
            print("\n ### Otomatik Kontrolcü Sistemi Devrede ###")
        elif simdi.day != datetime.strptime(degerlendirilmeyen_talepler[0]['tarih'], "%d-%m-%Y").day:
            print("\n ### Otomatik Kontrolcü Sistemi Devrede ###")
        else:
            print("ℹ️ Kontrolcü: Henüz yeni güne geçilmedi veya saat 00:00 değil, bekleniyor.")
            return
        islemler = []
        for i, talep in enumerate(degerlendirilmeyen_talepler):
            puan = talep['puan']
            miktar = talep['miktar']
            kullanici_adi = talep['kullanici_adi']
            karar = "Red"
            ek_izin = 0
            if puan >= 1375.00:
                karar = "Onay"
            if 3575.00 <= puan <= 3850.00:
                ek_izin = 2
                print(f"🌟 Kontrolcü: {kullanici_adi} ({puan:.2f} Puan) -> +2 Gün Ek İzin Kazandı.")
            elif 4950.00 <= puan <= 5500.00:
                ek_izin = 5
                print(f"✨ Kontrolcü: {kullanici_adi} ({puan:.2f} Puan) -> +5 Gün Ek İzin Kazandı.")
            print(f"Kontrolcü Kararı: {kullanici_adi} - {karar}")
            self._kontrolcuDosyaGuncelle(talep['satir'], karar, ek_izin)
        print("✅ Otomatik Kontrolcü sistemi tamamlandı.")
    
    def _kontrolcuDosyaGuncelle(self, eski_satir, karar, ek_izin):
        KLASOR_ADI = os.path.join("Nesne Tabanlı Programlama Projesi", "Proje", "data_sets")
        DOSYA_YOLU_MESAI = os.path.join(KLASOR_ADI, 'PersonelMesai.txt')
        try:
            with open(DOSYA_YOLU_MESAI, "r", encoding="utf-8") as dosya:
                tum_satirlar = dosya.readlines()
            yeni_satirlar = []
            for satir in tum_satirlar:
                if satir.strip() == eski_satir.strip():
                    yeni_durum_satiri = eski_satir.replace("DURUM=Provizyon", f"DURUM={karar} (Kontrolcü) | EK_IZIN={ek_izin}")
                    yeni_satirlar.append(yeni_durum_satiri)
                else:
                    yeni_satirlar.append(satir)
            with open(DOSYA_YOLU_MESAI, "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_satirlar)
        except Exception as e:
            print(f"\n ❌ Kontrolcü dosya güncelleme hatası: {e}")

    def _izinTalepGoruntule(self, provizyon_listesi):
        if not provizyon_listesi:
            print("\n ℹ️ Görüntülenecek provizyon durumunda izin talebi bulunamadı.")
            return False
        print("\n#### 📜 Provizyondaki İzin Talepleri ####")
        print("-" * 70)
        print(f"| {'ID (KEY)':<25} | {'K. Adı':<15} | {'Puan':<6} | {'Miktar':<6} |")
        print("-" * 70)
        for talep in provizyon_listesi:
            key_kisa = talep['key'][:20] + "..." if len(talep['key']) > 23 else talep['key']
            print(f"| {key_kisa:<25} | {talep['kullanici_adi']:<15} | {talep['puan']:<6.2f} | {talep['miktar']:<6} |")
        print("-" * 70)
        return True

