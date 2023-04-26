from django.contrib import admin
from authorizationSystem.models import Licenses

# Register your models here.
class LicenseAdmin(admin.ModelAdmin):
    list = ['max_user','max_active']
admin.site.register(Licenses,LicenseAdmin)