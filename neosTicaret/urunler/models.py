from django.db import models

# Create your models here.

class Urun(models.Model):
    resim = models.FileField(upload_to='urunler/', null=True, blank=True, verbose_name='Ürün Resmi')
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(max_length=400)
    fiyat = models.IntegerField()

    def __str__(self):
        return self.isim