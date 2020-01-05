from django.db import models
from django.contrib.auth.models import User


class Price_list(models.Model):
    """Прейскурант"""
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
    BRAND = ((APL, 'IPhone'), (SAM, 'Samsung'), (HUA, 'Huawei'), (MEI, 'Meizu'), (XIA, 'Xiaomi'), (NOK, 'Nokia'),
        (MIR, 'Microsoft'),(PRE, 'Prestigio'), (SON, 'Sony'), (ALK, 'Alcatel'), (ASU, 'Asus'), (ASE, 'Aser'),
        (AMI, 'Amigo'),(AMO, 'Amoi'),(BVI, 'BlackView'), (BLU, 'BLU'), (BQ, 'BQ'), (BBR, 'BlackBerry'),
        (CAT, 'CAT'), (CAP, 'Caterpillar'),(COO, 'Coolpad'),(CUB, 'Cubot'), (DOO, 'Doogee'), (DOR, 'Doro'),
        (ELE, 'Elephone'), (EST, 'Estar'), (GIG, 'Gigabyte'),(GET, 'Getnord'),(GOO, 'Google'), (HTC, 'HTC'),
        (HOM, 'HomTom'), (HP, 'HP'), (KAZ, 'Kazam'), (LEN, 'Lenovo'), (LG, 'Lg'),(MYP, 'MyPhone'),
        (NOU, 'Nous'), (ONE, 'OnePlus'), (OUK, 'Oukitel'), (ZOP, 'Zopo'), (ZTE, 'ZTE'), (OTH, '------->'))


    user_model = models.CharField(max_length=20,choices=BRAND)
    user_model_1 = models.CharField(max_length=20)
    battery_type = models.CharField(max_length=20,default='*')
    battery_replacement = models.CharField(max_length=6,default='*')
    LCD_SP = models.CharField(max_length=6,default='*')
    LCD_orig = models.CharField(max_length=6,default='*')
    LCD_HQ =  models.CharField(max_length=6,default='*')
    charging = models.CharField(max_length=6,default='*')
    record_1 = models.CharField(max_length=20,default='*')
    record_2 = models.CharField(max_length=20,default='*')
    record_3 = models.CharField(max_length=20,default='*')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def _str_(self):
        return self.user_model

class Details(models.Model):
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

    """детали"""
    LCD_MOD = 'LCD_module'
    LCD = 'LCD'
    TOU = 'Touch'
    FLEX_CH = 'Flex_charging'
    FLEX_ON = 'Flex_ON/OFF'
    FLEX_CAM = 'Flex_camera'
    BAT = 'Battery'
    CAM_FR = 'Camera_front'
    CAM_BC = 'Camera_back'
    BC = 'Back_cover'

    """качество"""
    SP = 'SP'
    OR = 'OR'
    HQ = 'HQ'
    COPY = 'COPY'

    BRAND = ((APL, 'IPhone'), (SAM, 'Samsung'), (HUA, 'Huawei'), (MEI, 'Meizu'), (XIA, 'Xiaomi'), (NOK, 'Nokia'),
        (MIR, 'Microsoft'), (PRE, 'Prestigio'), (SON, 'Sony'), (ALK, 'Alcatel'), (ASU, 'Asus'), (ASE, 'Aser'),
        (AMI, 'Amigo'), (AMO, 'Amoi'), (BVI, 'BlackView'), (BLU, 'BLU'), (BQ, 'BQ'), (BBR, 'BlackBerry'),
        (CAT, 'CAT'), (CAP, 'Caterpillar'), (COO, 'Coolpad'), (CUB, 'Cubot'), (DOO, 'Doogee'), (DOR, 'Doro'),
        (ELE, 'Elephone'), (EST, 'Estar'), (GIG, 'Gigabyte'), (GET, 'Getnord'), (GOO, 'Google'), (HTC, 'HTC'),
        (HOM, 'HomTom'), (HP, 'HP'), (KAZ, 'Kazam'), (LEN, 'Lenovo'), (LG, 'Lg'), (MYP, 'MyPhone'),
        (NOU, 'Nous'), (ONE, 'OnePlus'), (OUK, 'Oukitel'), (ZOP, 'Zopo'), (ZTE, 'ZTE'), (OTH, '------->'))
    DETAIL = ((BAT,'Battery'),(BC,'Back_cover'),(CAM_BC,'Camera_back'),(CAM_FR,'Camera_front'),(FLEX_CH,'Flex_charging'),
        (FLEX_ON,'Flex_ON/OFF'),(FLEX_CAM,'Flex_camera'),(LCD_MOD,'LCD_module'),(LCD,'LCD'),(TOU,'Touch'))
    QUALITY = ((SP,'SP'),(OR,'OR'),(HQ,'HQ'),(COPY,'COPY'))

    user_model = models.CharField(max_length=20, choices = BRAND)
    user_model_1 = models.CharField(max_length=20)
    user_detail = models.CharField(max_length=20, choices = DETAIL)
    detail_quality = models.CharField(max_length=10,choices = QUALITY)
    detail_comment = models.CharField(max_length=20,default='*')
    detail_price = models.CharField(max_length=5)
    detail_quantity = models.CharField(max_length=5)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Handbook(models.Model):
    handbook_model = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)