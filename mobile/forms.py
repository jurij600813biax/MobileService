from django import forms
from .models import Mobil
from django.forms import ModelForm,MultipleChoiceField


class MobilForm(forms.ModelForm):

    class Meta:
        model = Mobil
        fields=['number_sticker','model_tel','model_1_tel','imei','number_tel','state','price','defect',
            'defect_tel','kod_tel','comment']
        labels = {'':''}
        help_texts = {'model_tel':'если нет в списке, укажите ------->','model_1_tel':('а здесь введите полное наименование'),
            'defect_tel':'если нет в списке, укажите ------->','defect':'а здесь введите неисправность'}

class EditForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields=['number_sticker','model_tel','model_1_tel','imei','number_tel','state','price',
            'defect_tel','defect','kod_tel','status','date_end','date_take_away','number_reg','comment']


