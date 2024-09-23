from django.db import models


class cric_profile(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    contry=models.CharField(max_length=100)
    about=models.TextField()


    def __str__(self) -> str:
        return (str(self.id)+" "+self.name+" "+self.contry)


# Create your models here.
