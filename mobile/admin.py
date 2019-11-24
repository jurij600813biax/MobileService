from django.contrib import admin
from mobile.models import Mobil

class MobilAdmin(admin.ModelAdmin):
    list_display= ("number_reg","model_tel","imei","number_tel","date_added","defect_tel",)

admin.site.register(Mobil,MobilAdmin)
