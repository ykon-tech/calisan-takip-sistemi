import re

class Validator:
    """
    Sistem genelinde kullanılan doğrulama (validation) işlemlerini yürüten yardımcı sınıf.
    Statik metotlar içerir, nesne oluşturulmasına gerek yoktur.
    """

    @staticmethod
    def epostaDogrula(eposta):
        # E-posta doğrulama mekanizması.
        eposta_deseni = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.fullmatch(eposta_deseni, eposta)

    @staticmethod
    def sifreGuvenlikKontrol(sifre):
        # Şifre güvenliği mekanizması.
        if len(sifre) < 8:
            return "Şifre en az 8 karakter uzunluğunda olmalıdır."
        if not re.search(r"[A-z]", sifre):
            return "Şifre en az bir büyük harf içermelidir."
        if not re.search(r"[a-z]", sifre):
            return "Şifre en az bir küçük harf içermelidir."
        if re.search(r"[ö,ü,ç,ğ,İ,ı,Ö,Ü,Ç,Ğ]", sifre):
            return "Şifre Türkçe karakterler içeremez."
        if not re.search(r"[0-9]", sifre):
            return "Şifre en az bir rakam içermelidir."
        
        return None  # Hata yok.

    @staticmethod
    def telnoDogrula(telno):
        # Telefon numarasına ait güvenlik mekanizması.
        telno = telno.replace(" ", "").replace("-", "0")  # Boşluk ve tireler temizlenir.
        if not telno.isdigit():
            return "Telefon numarası sadece rakamlardan oluşmalıdır."
        if len(telno) < 10 or len(telno) > 11:
            return "Telefon numarası 10 veya 11 haneli olmalıdır."
        
        return None  # Hata yok.