from django import forms
from .models import Mobil
from django.forms import ModelForm,MultipleChoiceField


class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields=['number_sticker','model_tel','model_1_tel','imei','number_tel','state','price','defect',
            'defect_tel','kod_tel','comment','email_client']
        labels = {'number_sticker':'Стикер','model_tel':'Модель(бренд)','model_1_tel':'Модель','imei':'IMEI',
            'number_tel':'Номер телефона','state':'Состояние','price':'Цена','defect':'Дефект(дополнение)',
            'defect_tel':'Дефект','kod_tel':'Код телефона','comment':'Комментарии','email_client':'EMAIL' }
        help_texts = {'model_tel':'если нет в списке, укажите ------->',
            'model_1_tel':('а здесь введите полное наименование'),
            'defect_tel':'если нет в списке, укажите ------->','defect':'а здесь введите неисправность'}

class EditForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields=['number_sticker','model_tel','model_1_tel','imei','number_tel','state','price',
            'defect_tel','defect','kod_tel','status','date_end','date_take_away','number_reg','comment','email_client']
        labels = {'number_sticker':'Стикер','model_tel':'Модель(бренд)','model_1_tel':'Модель','imei':'IMEI',
            'number_tel':'Номер телефона','state':'Состояние','price':'Цена','defect':'Дефект(дополнение)',
            'defect_tel':'Дефект','kod_tel':'Код телефона','comment':'Комментарии','number_reg':'Регистр.номер',
            'status':'Статус','date_end':'Дата завершения ремонта','date_take_away':'Забран(дата)',
            'email_client':'EMAIL'}


