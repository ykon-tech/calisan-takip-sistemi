# 📂 Mesai Takip Otomasyonu (Employee & Overtime Tracking System)

Bu proje, bir organizasyon içerisindeki personellerin mesai giriş-çıkışlarını, performans puanlarını ve izin taleplerini yönetmek amacıyla geliştirilmiş, **Nesne Tabanlı Programlama (OOP)** prensiplerini temel alan konsol tabanlı bir otomasyon sistemidir.

## 🚀 Öne Çıkan Özellikler

* **Çift Rol Desteği:** Sistem, `Admin` ve `Personel` olmak üzere iki farklı kullanıcı tipine göre dinamik arayüz sunar.
* **Gelişmiş Güvenlik & Doğrulama:**
    * **Regex** tabanlı e-posta, şifre ve telefon numarası doğrulaması (Validator Servisi).
    * **SMTP Entegrasyonu:** Şifremi unuttum işlemleri için e-posta yoluyla güvenlik kodu gönderimi.
* **Dinamik Puanlama Algoritması:** Çalışılan süreye göre (8 saat üzeri fazla mesai dahil) personellere otomatik performans puanı atanır.
* **İzin Yönetim Sistemi:**
    * **14 Gün Kuralı:** Son izin talebinin üzerinden 14 gün geçmeden yeni talep oluşturulması engellenir.
    * **Otomatik Kontrolcü:** Puanı 1375.00 eşiğini aşan personelin izni sistem tarafından onaylanabilir ve yüksek puanlılara ek izin tanımlanır.
* **Departman Yönetimi:** Personellerin Yazılım, Muhasebe gibi spesifik departmanlara atanması ve yönetimi.

---

## 🛠 Teknik Mimari

Proje, **Separation of Concerns (Sorumlulukların Ayrılması)** prensibine uygun olarak modüllere bölünmüştür:

| Modül | Açıklama |
| :--- | :--- |
| `main.py` | Uygulamanın giriş noktası ve menü akış kontrolü. |
| `kullanici.py` | Temel sınıf (Base Class); kayıt, giriş ve şifre sıfırlama işlemlerini içerir. |
| `personel.py` | `Kullanici` sınıfından türetilmiştir; mesai ve izin talebi operasyonlarını yönetir. |
| `admin.py` | `Kullanici` sınıfından türetilmiştir; personel atama, onay ve kayıt görüntüleme yetkilerini içerir. |
| `departman.py` | Departman nesnelerini ve üye listelerini yöneten sınıf. |
| `email_service.py` | SMTP protokolü ile e-posta gönderiminden sorumlu bağımsız servis. |
| `utils.py` | Regex kontrollerini yürüten statik `Validator` sınıfı. |

---

## 📊 Veri Yönetimi

Sistem, veri kalıcılığı için yapılandırılmış `.txt` dosyalarını veritabanı olarak kullanmaktadır:
* `kullanici_verileri.txt`: Kullanıcı kimlik, şifre, iletişim ve rol bilgileri.
* `PersonelMesai.txt`: Tarih ve zaman damgalı giriş-çıkış kayıtları.
* `PersonelIzin.txt`: İzin miktarı, puan ve provizyon (onay) durumları.

---

## 📝 Gelişim Süreci (Changelog)

Proje, sistematik olarak 6 ana fazda geliştirilmiştir:
1.  **Faz 1:** Temel Mimari, Kalıtım ve Regex doğrulamaları.
2.  **Faz 2:** Personel modülü ve dinamik puan hesaplama.
3.  **Faz 3:** İzin yönetimi ve iş kurallarının (14 gün kuralı vb.) sıkılaştırılması.
4.  **Faz 4:** Departman sınıfının aktifleştirilmesi ve organizasyonel filtreleme.
5.  **Faz 5:** Kodun modüllere ayrıştırılması (Refactoring).
6.  **Faz 6:** Servis mimarisine geçiş (Validator & Email Service ayrımı).

---

## 👤 Geliştirici
**Yiğit Kaan Akdeniz | Buğra Demir**
* Bilgisayar Mühendisliği 2. Sınıf Öğrencisi

---
**Bu proje, Nesne Tabanlı Programlama (NTP) prensiplerini uygulamalı olarak göstermek amacıyla hazırlanmıştır.**
