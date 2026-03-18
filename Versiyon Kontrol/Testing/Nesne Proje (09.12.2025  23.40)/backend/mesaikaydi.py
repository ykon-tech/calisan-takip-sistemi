class MesaiKaydi(object):
    def __init__(self,__departmanId,departmanAdi,__personelId,__personelAdSoyad,__tarih,__girisZamani,__cikisZamani,onayDurumu):
        self.__departmanId = __departmanId
        self.departmanAdi = departmanAdi
        self.__personelId = __personelId
        self.__personelAdSoyad = __personelAdSoyad
        self.__tarih = __tarih
        self.__girisZamani = __girisZamani
        self.__cikisZamani = __cikisZamani
        self.onayDurumu = onayDurumu

    
    ####### Claasa ait Metotlar #######

    def _departmanEkle(self):
        pass

    def _departmanSil(self):
        pass




    ####### Getter Setter Metotları #######


    @property
    def departmanIdGetSet(self):
        return self.__departmanId
    
    @departmanIdGetSet.setter
    def departmanIdGetSet(self,yeni_departman_id):
        if not yeni_departman_id:
            raise ValueError("Yeni departman id boş kalamaz.")
        self.__departmanId = yeni_departman_id

    @property
    def personelIdGetSet(self):
        return self.__personelId
    
    @personelIdGetSet.setter
    def personelIdGetSet(self,yeni_personel_id):
        if not yeni_personel_id:
            raise ValueError("Yeni personel id boş kalamaz.")
        self.__personelId = yeni_personel_id

    
    @property
    def personelAdSoyadGetSet(self):
        return self.__personelAdSoyad
    
    @personelAdSoyadGetSet.setter
    def personelAdSoyadGetSet(self,yeni_adSoyad):
        if not yeni_adSoyad:
            raise ValueError("Yeni isim değeri boş kalamaz.")
        self.__personelAdSoyad = yeni_adSoyad

    @property
    def tarihGetSet(self):
        return self.__tarih
    
    @tarihGetSet.setter
    def tarihGetSet(self,yeni_tarih):
        if not yeni_tarih:
            raise ValueError("Yeni tarih değeri boş kalamaz.")
        self.__tarih = yeni_tarih

    @property
    def girisZamaniGetSet(self):
        return self.__girisZamani
    
    @girisZamaniGetSet.setter
    def girisZamaniGetSet(self,yeni_giris_zamani):
        if not yeni_giris_zamani:
            raise ValueError("Yeni giriş zamani değeri boş kalamaz.")
        self.__girisZamani = yeni_giris_zamani

    
    @property
    def cikisZamaniGetSet(self):
        return self.__cikisZamani
    
    @cikisZamaniGetSet.setter
    def cikisZamaniGetSet(self,yeni_cikis_zamani):
        if not yeni_cikis_zamani:
            raise ValueError("Yeni çıkıs zamani değeri boş kalamaz.")
        self.cikisZamaniGetSet = yeni_cikis_zamani