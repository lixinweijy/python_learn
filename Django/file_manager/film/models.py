from django.db import models

# Create your models here.
class FilmInfo(models.Model):
    fid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=20)

    def __str__(self):
        return self.fname

class PeopleInfo(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=20)
    gender=models.BooleanField()
    film=models.ForeignKey(FilmInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.uname