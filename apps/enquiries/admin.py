from django.contrib import admin

# Register your models here.
from . models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):

    list_display = ["name","email","phone_number","message"]

admin.site.register(Enquiry,EnquiryAdmin)