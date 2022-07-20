from django.db import models

# Create your models here.
class Post(models.Model):
  
    title = models.CharField(max_length= 100, verbose_name="제목")
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
    content = models.TextField(verbose_name="내용")
    interest = models.IntegerField(default=0,verbose_name="가격")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)