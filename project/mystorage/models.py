from django.db import models
from django.conf import settings

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)  # user에 맞게 정해지도록 설정
    title = models.CharField(max_length=30)
    body = models.TextField()

class Album(models.Model):  # 사진
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length=100)

class Files(models.Model):  # 글
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    myfile = models.FileField(blank = False, null = False, upload_to="files")
    desc = models.CharField(max_length=100)