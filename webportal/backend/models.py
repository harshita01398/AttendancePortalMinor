from django.db import models

# Database models

class Info(models.Model):
    SubCode = models.CharField(max_length=200)
    SubName = models.CharField(max_length=200)
    TCode = models.CharField(max_length=200)
    TeacherName = models.CharField(max_length=200)
    Dept = models.CharField(max_length=200)

    def __str__(self):
        return self.SubCode

class Record(models.Model):
    SubCode = models.CharField(max_length=200)
    Date = models.DateField(auto_now_add=True)
    Img = models.ImageField(upload_to='images/')
    Xls = models.FileField(upload_to='output/',blank=True)

    def __str__(self):
        return self.Img.url

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title