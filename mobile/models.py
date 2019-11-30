from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Mobil(models.Model):
    """информация о телефонах"""

    """модели"""
    SAM = 'Samsung'
    ALK = 'Alkatel'
    ASE = 'Aser'
    AMI = 'Amigo'
    AMO = 'Amoi'
    APL = 'IPhone'
    ASU = 'Asus'
    BBR = 'BlackBerry'
    BVI = 'BlackView'
    BLU = 'BLU'
    BQ = 'BQ'
    CAT = 'CAT'
    CAP = 'Caterpillar'
    COO = 'Coolpad'
    CUB = 'Cubot'
    DOO = 'Doogee'
    DOR = 'Doro'
    EST = 'Estar'
    ELE = 'Elephone'
    GIG = 'Gigabyte'
    GET = 'Getnord'
    GOO = 'Google'
    HTC = 'HTC'
    HP = 'HP'
    HOM = 'HomTom'
    KAZ = 'Kazam'
    MYP = 'MyPhone'
    NOU = 'Nous'
    ONE = 'OnePlus'
    OUK = 'Oukitel'
    PRE = 'Prestigio'
    ZTE = 'ZTE'
    ZOP = 'Zopo'
    HUA = 'Huawei'
    LEN = 'Lenovo'
    SON = 'Sony'
    LG = 'LG'
    MEI = 'Meizu'
    XIA = 'Xiaomi'
    MIR = 'Microsoft'
    NOK = 'Nokia'
    OTH = '------->'

    """неисправности"""
    LCD = 'lcd'
    DIN = 'speaker'
    BUZ = 'buzzer'
    KOD = 'kod'
    AKK = 'akkaunt'
    MIC = 'microphone'
    WIF = 'wi_fi'
    PRO = 'programm'
    HEN = 'hands_free'
    N_C = 'not_charging'
    WET = 'wet'
    SIM = 'sim'
    NTO1 = 'не вкл'
    NTO2 = 'не вкл, мокрый'
    NTO3 = 'не вкл,падал'
    LCT = 'lcd/touch'
    TOU = 'touch'
    LANG = 'languige'
    UNLO = 'unlock'
    FLEX = 'flex'
    CASE = 'case'


    """состояние"""
    NVD = 'no visible defects'
    DLT = 'damaded_LCD/Touch'
    DCS = 'damaded_case'
    DBC = "damaded_back_cover"

    """статус"""
    REP = 'Ремонт'
    REP_COM = 'Рем.завершен'
    TEL_TA = 'Забран'
    BRAND = ((APL,'IPhone'),(SAM,'Samsung'),(HUA,'Huawei'),(MEI,'Meizu'),(XIA,'Xiaomi'),(NOK,'Nokia'),(MIR,'Microsoft'),
        (PRE,'Prestigio'),(SON,'Sony'),(ALK,'Alcatel'),(ASU,'Asus'),(ASE,'Aser'),(AMI,'Amigo'),(AMO,'Amoi'),
        (BVI,'BlackView'),(BLU,'BLU'),(BQ,'BQ'),(BBR,'BlackBerry'),(CAT,'CAT'),(CAP,'Caterpillar'),(COO,'Coolpad'),
        (CUB,'Cubot'),(DOO,'Doogee'),(DOR,'Doro'),(ELE,'Elephone'),(EST,'Estar'),(GIG,'Gigabyte'),(GET,'Getnord'),
        (GOO,'Google'),(HTC,'HTC'),(HOM,'HomTom'),(HP,'HP'),(KAZ,'Kazam'),(LEN,'Lenovo'),(LG,'Lg'),(MYP,'MyPhone'),
        (NOU,'Nous'),(ONE,'OnePlus'),(OUK,'Oukitel'),(ZOP,'Zopo'),(ZTE,'ZTE'),(OTH,'------->'))
    DEFECT = ((PRO,'Programm'),(LANG,'Язык'),(UNLO,'Отвязка'),(KOD,'Код'),(AKK,'Аккаунт'),(LCT,'LCD/Touch'),(LCD,'LCD'),
        (TOU,'Touch'),(NTO1,'Не вкл'),(NTO2,'Не вкл, Мокрый'),(NTO3,'Не вкл, Падал'),(N_C,'Не заряж'),(DIN,'Динамик'),
        (BUZ,'Зуммер'),(MIC,'Микрофон'),(HEN,'Hands_Free'),(WIF,'Wi-Fi'),(WET,'Мокрый'),(SIM,'Sim'),(FLEX,'шлейф'),
        (CASE,'корпус'),(OTH,'------->'))
    STATUS = ((REP,'ремонт'),(REP_COM,'ремонт_завершён'),(TEL_TA,'забран'))
    STATE = ((NVD,'Нет видимых дефектов'),(DLT,'Повреждён экран/тоучскрин'),(DCS,'Повреждён корпус'),
        (DBC,'Повреждена задняя крышка'))
    
    
    number_reg = models.IntegerField(default=0)
    number_sticker = models.CharField(max_length=5)
    model_tel = models.CharField(max_length=20,choices=BRAND)
    model_1_tel = models.CharField(max_length=20)
    kod_tel = models.CharField(max_length=20,default='*')
    price = models.CharField(max_length=5)
    imei = models.CharField(max_length=20)
    number_tel = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    date_end = models.CharField(max_length=12,default='*')
    date_take_away = models.CharField(max_length=12,default='*')
    state = models.CharField(max_length=20,choices=STATE)
    status = models.CharField(max_length=20,choices=STATUS,default=REP)
#    defect_tel = MultiSelectField(choices=DEFECT)
    defect = models.CharField(max_length=30,default='*')
    defect_tel = models.CharField(max_length=20,choices=DEFECT)
    defect_1_tel = models.CharField(max_length=20,choices=DEFECT,default='*')
    comment = models.CharField(max_length=200,default='*')
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.number_reg


