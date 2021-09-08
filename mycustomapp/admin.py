from django.contrib import admin
from qrtoolkit_core import models as qr_models
from qrtoolkit_core.admin import QRCodeAdmin
from mycustomapp.models import MyObject

admin.site.unregister(qr_models.QRCode)


# admin.site.unregister(qr_models.ApiHit)
# admin.site.unregister(qr_models.Department)
# admin.site.unregister(qr_models.ApiCall)

@admin.register(qr_models.QRCode)
class MyQrCodeAdmin(QRCodeAdmin):
    # Here you can override the fields you want to customize
    list_display = ('title', 'get_code_url', 'get_code_image_url')


@admin.register(MyObject)
class MyObjectAdmin(admin.ModelAdmin):
    pass
