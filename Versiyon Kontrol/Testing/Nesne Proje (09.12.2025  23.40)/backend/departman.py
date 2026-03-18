class Departman(object):
    def __init__(self,departmanAdi,__departmanID):
        self.departmanAdi = departmanAdi
        self.__departmanID = __departmanID
        self.personel_listesi = []

    
    ####### Claasa ait Metotlar #######

    def _DepartmanEkle(self,personel_nesnesi):
        self.personel_listesi.append(personel_nesnesi)
        
        

    def _departmanKaldir(self):
        pass

    def _departmanGuncelle(self):
        pass

    def departmanaGit(self):
        pass

    def _uyeEkle(self):
        pass

    def _uyeKaldir(self):
        pass

    def uyeGoruntule(self):
        return self.personel_listesi



    ####### Getter Setter Metotları #######
    
    @property
    def personelIdGetSet(self):
        return self.__personelId
    
    @personelIdGetSet.setter
    def personelIdGetSet(self,yeni_personel_id):
        if not yeni_personel_id:
            raise ValueError("Yeni personel id değeri boş olamaz.")
        self.__personelId = yeni_personel_id

    

    @property
    def departmanIdGetSet(self):
        return self.__departmanID
    
    @departmanIdGetSet.setter
    def departmanIdGetSet(self,yeni_departman_id):
        if not yeni_departman_id:
            raise ValueError("Yeni departman id değeri boş olamaz.")
        self.__departmanID = yeni_departman_id