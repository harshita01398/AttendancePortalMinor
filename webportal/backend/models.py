from django.db import models

# Database models

# class Info(models.Model):
#     SubCode = models.CharField(max_length=200)
#     SubName = models.CharField(max_length=200)
#     TCode = models.CharField(max_length=200)
#     TeacherName = models.CharField(max_length=200)
#     Dept = models.CharField(max_length=200)

#     def __str__(self):
#         return self.SubCode

class Record(models.Model):
    Auto_increment_id = models.AutoField(primary_key=True)
    Upload_time = models.DateTimeField(auto_now_add=True)
    Img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.Img.url