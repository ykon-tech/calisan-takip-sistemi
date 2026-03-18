**Tarih:** 29.12.2025

**Saat:** 01.41



**Güncelleyen: Yiğit Kaan Akdeniz**



-------------------------------- **Güncelleme Notları** ---------------------------------------------------------------





📂 **Mesai Takip Otomasyonu - Geliştirici Günlüğü**

**Proje:** Nesne Tabanlı Personel \& Mesai Takip Sistemi

**Dil:** Python

**Mimari:** OOP (Nesne Tabanlı Programlama) \& Dosya Tabanlı Veritabanı (TXT)



📅 **Faz 1:** Temel Mimari ve Güvenlik (Auth \& Core)

Projenin temelleri atıldı. Tek bir dosya üzerinde temel sınıf yapıları kurgulandı.



OOP Temeli: Kullanici ana sınıfı ve ondan türeyen Personel ile Admin sınıfları oluşturuldu.



Veri Kalıcılığı: Kullanıcı verilerinin JSON formatına benzer bir yapıda kullanici\_verileri.txt dosyasına kaydedilmesi sağlandı.



Güvenlik:



Şifre sıfırlama için smtplib ile e-posta gönderme sistemi entegre edildi.



Kayıt esnasında Regex ile katı veri doğrulama kuralları (şifre karmaşıklığı, e-posta formatı vb.) getirildi.



📅 **Faz 2:** Personel Modülü (Mesai ve Puanlama)

Çalışanların mesai hareketlerini ve performanslarını takip eden algoritmalar yazıldı.



Mesai Takibi: mesaiGirisYap ve mesaiCikisYap metotları ile anlık zaman damgaları PersonelMesai.txt dosyasına işlendi.



Hata Ayıklama (Bug Fix): Mesai çıkışı sırasında dosya okurken oluşan string parçalama (split) hataları giderildi, try-except blokları güçlendirildi.



Puanlama Sistemi: Çalışılan saate göre (normal mesai vs. fazla mesai) dinamik puan hesaplayan algoritma kuruldu.





📅 **Faz 3:** İzin Yönetimi ve Veri Ayrıştırma (Separation of Concerns)

Dosya yapısındaki karışıklık giderildi ve iş kuralları sıkılaştırıldı.



Dosya Ayrıştırma: Mesai ve İzin kayıtları aynı dosyada karışıklık yaratıyordu. İzin işlemleri PersonelIzin.txt dosyasına taşındı.



İş Kuralları (Business Logic):



14 Gün Kuralı: Son izinden sonra 14 gün geçmeden yeni talep oluşturulması engellendi.



Çift Kayıt Kontrolü: Aynı gün içinde mükerrer talep oluşturulması engellendi.



Admin Onayı: "Provizyon" (Beklemede) durumundaki izinlerin Admin tarafından onaylanması/reddedilmesi sağlandı. Büyük/küçük harf duyarlılığı hatası giderildi.





📅 **Faz 4:** Admin Paneli ve Karar Mekanizması

Sistem sadece "Kişi" odaklı olmaktan çıkarılıp "Organizasyon" odaklı hale getirildi.



Departman Sınıfı: Departman sınıfı aktif hale getirildi. Her departman kendi personel listesini tutabilir hale geldi.



Atama Mantığı: Admin'in sıfırdan personel yaratması yerine, sistemde kayıtlı olan "Atanmamış" personelleri departmanlara ataması mantığına geçildi.



Gelişmiş Filtreleme: Kullanıcı listeleme işlemleri "Genel (Karma)" ve "Departman Bazlı" olarak ikiye ayrıldı.





📅 **Faz 5:** Departman Entegrasyonu ve Refactoring (OOP Derinleşmesi)

Kod satırları arttıkça tek dosyada çalışmak zorlaştı. Proje parçalara bölündü.



Dosya Bölümlendirme:



main.py: Sadece menü ve akış kontrolü.



kullanici.py: Temel sınıf (Base Class).



personel.py: Personel operasyonları.



admin.py: Yönetim operasyonları.



departman.py: Departman nesnesi ve mantığı.



Sonuç: Kodun okunabilirliği arttı, main.py sadeleşti.





📅 **Faz 6:** Servis Mimarisi ve Temizlik (Final Touch)

Kod tekrarını önlemek ve Kullanici sınıfını şişirmemek için yardımcı işlemler servislere dönüştürüldü.



Validation Servisi (utils.py): E-posta, şifre ve telefon doğrulama (Regex) işlemleri Validator adlı statik bir sınıfa taşındı. Artık her yerden çağrılabilir durumda.



E-Posta Servisi (email\_service.py): SMTP ayarları ve mail gönderme mantığı Kullanici sınıfından çıkarılıp EmailService sınıfına aktarıldı.



Temiz Kod: Ana sınıflar artık sadece kendi işlerine (Business Logic) odaklanıyor, doğrulama ve bildirim işlerini bu servislere devrediyor.





🚀 **Sonuç**

Şu an elimizde; bakımı kolay, modüler, hatalardan arındırılmış, veri tutarlılığı sağlayan ve gerçek dünya senaryolarına uygun katmanlı bir mimariye sahip OOP prensiplerini olabildiğince kullanmış bir konsol tabanlı mesai takip otomasyonu var.

