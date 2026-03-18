import smtplib
from email.message import EmailMessage
import ssl

class EmailService:
    """
    E-posta gönderme işlemlerinden sorumlu servis sınıfı.
    """
    
    # E-POSTA AYARLARI (Kendi bilgilerinizle değiştirin!)
    GONDEREN_EPOSTA = "wearbaseds@gmail.com"
    GONDEREN_SİFRE = "cynjkansrmfanemx"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    @staticmethod
    def gonder(alici_eposta, konu, icerik):
        try:
            # Eposta içeriğini oluşturma:
            mesaj = EmailMessage()
            mesaj['From'] = EmailService.GONDEREN_EPOSTA
            mesaj['To'] = alici_eposta
            mesaj['Subject'] = konu
            mesaj.set_content(icerik)

            # Güvenli Bağlantı kullanarak SMTP sunucusuna bağlanma:
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(EmailService.SMTP_SERVER, EmailService.SMTP_PORT, context=context) as server:
                server.login(EmailService.GONDEREN_EPOSTA, EmailService.GONDEREN_SİFRE)
                server.sendmail(EmailService.GONDEREN_EPOSTA, alici_eposta, mesaj.as_string())
            
            return True
        
        except smtplib.SMTPAuthenticationError:
            print("❌ Eposta gönderme hatası: SMTP kimlik doğrulaması başarısız. Uygulama şifrenizi kontrol edin.")
            return False
        except Exception as e:
            print(f"❌ Eposta gönderirken beklenmeyen bir hata oluştu: {e}")
            return False