from django.db import models
from django.contrib.auth import get_user_model
from qrtoolkit_core import models as qr_models


class MyObject(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='user_objects')

    qrcode = models.OneToOneField(to=qr_models.QRCode, related_name='myobject', on_delete=models.CASCADE)
