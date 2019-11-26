from django.db import models

# Database models


class Record(models.Model):
    Auto_increment_id = models.AutoField(primary_key=True)
    Upload_time = models.DateTimeField(auto_now_add=True)
    Img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.Img.url