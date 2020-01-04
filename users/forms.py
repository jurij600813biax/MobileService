from django import forms
from .models import Price_list,Details,Handbook
from django.forms import ModelForm

class Price_listForm(forms.ModelForm):
    class Meta:
        model= Price_list
        fields = ['user_model','user_model_1','battery_type','battery_replacement','LCD_SP',
                  'LCD_orig','LCD_HQ','charging','record_1','record_2','record_3']
        labels = {'user_model':'Модель(бренд)','user_model_1':'Модель','battery_type':'Тип батареи',
                  'battery_replacement':'Замена батареи','charging':'Зарядка'}

class DetailsForm(forms.ModelForm):
    class Meta:
        model= Details
        fields = ['user_model','user_model_1','user_detail','detail_quality','detail_comment','detail_price',
                  'detail_quantity']
        labels = {'user_model': 'Модель(бренд)', 'user_model_1': 'Модель','user_detail':'Деталь','detail_quality':
                  'Качество','detail_comment':'Комментарии','detail_price':'Цена','detail_quantity':'Количество'}

class HandbookForm(forms.ModelForm):
    class Meta:
        model= Handbook
        fields = ['handbook_model','designation']
        labels = {'handbook_model':'Модель','designation':'Обозначение'}