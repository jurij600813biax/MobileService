from django import forms
from .models import Post, Settings_common
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['post_message','text_message']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings_common
        fields = ['message_send_start','message_send_finish','number_reg_letter','number_reg_start','details_visible']

