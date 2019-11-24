from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Mobil(models.Model):
    """информация о телефонах"""

    """модели"""
    SAM = 'Samsung'
    ALK = 'Alkatel'
    APL = 'IPhone'
    ASU = 'Asus'
    BBR = 'BlackBerry'
    COO = 'Coolpad'
    CUB = 'Cubot'
    DOO = 'Doogee'
    DOR = 'Doro'
    EST = 'Estar'
    GET = 'Getnord'
    GOO = 'Google'
    HTC = 'HTC'
    MYP = 'MyPhone'
    NOU = 'Nous'
    PRE = 'Prestigio'
    ZTE = 'ZTE'
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


    """состояние"""
    NVD = 'no visible defects'
    DLT = 'damaded_LCD/Touch'
    DCS = 'damaded_case'
    DBC = "damaded_back_cover"

    """статус"""
    REP = 'repair'
    REP_COM = 'rep_com'
    TEL_TA = 'tel_take_away'
    TITLE = ((APL,'IPhone'),(SAM,'Samsung'),(HUA,'Huawei'),(MEI,'Meizu'),(XIA,'Xiaomi'),(NOK,'Nokia'),(MIR,'Microsoft'),
        (SON,'Sony'),(ALK,'Alcatel'),(ASU,'Asus'),(BBR,'BlackBerry'),(COO,'Coolpad'),(CUB,'Cubot'),(DOO,'Doogee'),
        (DOR,'Doro'),(EST,'Estar'),(GET,'Getnord'),(GOO,'Google'),(HTC,'HTC'),(LEN,'Lenovo'),(LG,'Lg'),(MYP,'MyPhone'),
        (NOU,'Nous'),(ZTE,'ZTE'),(OTH,'------->'))
    DEFECT = ((PRO,'Programm'),(KOD,'Код'),(AKK,'Аккаунт'),(LCT,'LCD/Touch'),(LCD,'LCD'),(TOU,'Touch'),(NTO1,'Не вкл'),
        (NTO2,'Не вкл, Мокрый'),(NTO3,'Не вкл, Падал'),(N_C,'Не заряж'),(DIN,'Speaker'),(BUZ,'Buzzer'),
        (MIC,'Microphone'),(HEN,'Hands_Free'),(WIF,'Wi-Fi'),(WET,'Мокрый'),(SIM,'Sim'),(OTH,'------->'))
    STATUS = ((REP,'ремонт'),(REP_COM,'ремонт_завершён'),(TEL_TA,'забран'))
    STATE = ((NVD,'нет видимых дефектов'),(DLT,'повреждён экран/тоучскрин'),(DCS,'повреждён корпус'),
        (DBC,'повреждена задняя крышка'))
    
    
    number_reg = models.IntegerField(default=0)
    number_sticker = models.CharField(max_length=5)
    model_tel = models.CharField(max_length=20,choices=TITLE)
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


