from django import forms
from .models import Post, Settings_common, Send_message
from django.forms import ModelForm, Textarea

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['post_message','text_message']
        widgets = {'text_message': Textarea(attrs={'cols': 30, 'rows': 7})}

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings_common
        fields = ['message_send_start','message_send_finish','number_reg_letter','number_reg_start','details_visible',
                  'free_set','contact_number']
        labels = {'message_send_start':'Время начала рассылки','message_send_finish':'Время завершения рассылки',
                  'free_set':'Разрешить отправку сообщений','details_visible':'Показать каталог деталей всем',
                  'number_reg_letter':'Буквенная часть номера регистрации',
                  'number_reg_start':'Начальное цифровое значение','contact_number':'Номер для контакта'}

class Send_messageForm(forms.ModelForm):
    class Meta:
        model = Send_message
        fields = ['send_message_text']
        labels = {'send_message_text': 'текст сообщения'}
        widgets = {'send_message_text': Textarea(attrs={'cols': 30, 'rows': 5})}