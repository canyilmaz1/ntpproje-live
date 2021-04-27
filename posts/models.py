from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Başlık')
    body = RichTextField(verbose_name='Metin')
    date= models.DateField( auto_now_add=True, verbose_name='Tarih')
    author= models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
        verbose_name='Yazar')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    


