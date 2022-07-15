from django.db import models

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=50, verbose_name="제목")
    release = models.IntegerField(verbose_name="개봉년도")
    genre = models.CharField(max_length=50, verbose_name="장르")
    star = models.FloatField(verbose_name="별점")
    time = models.IntegerField(verbose_name="러닝타임")
    content = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=50, verbose_name="감독")
    actor = models.CharField(max_length=50, verbose_name="배우")