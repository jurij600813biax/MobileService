from django import forms
from .models import Price_list,Details,Handbook
from django.forms import ModelForm

class Price_listForm(forms.ModelForm):
    class Meta:
        model= Price_list
        fields = ['user_model','user_model_1','battery_type','battery_replacement','LCD_SP',
                  'LCD_orig','LCD_HQ','charging','record_1','record_2','record_3']

class DetailsForm(forms.ModelForm):
    class Meta:
        model= Details
        fields = ['user_model','user_model_1','user_detail','detail_quality','detail_comment','detail_price',
                  'detail_quantity']

class HandbookForm(forms.ModelForm):
    class Meta:
        model= Handbook
        fields = ['handbook_model','designation']
