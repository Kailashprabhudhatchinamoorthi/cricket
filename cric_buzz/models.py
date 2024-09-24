from django.db import models

"""cricket profile info"""
class cric_profile(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    contry=models.CharField(max_length=100)
    about=models.TextField()


    def __str__(self) -> str:
        return (str(self.id)+" "+self.name+" "+self.contry)
    

"""cricket borad info"""
class cric_board(models.Model):
    id=models.AutoField(primary_key=True)
    board_name=models.CharField(max_length=100)
    board_orgin=models.CharField(max_length=100)

"""cricket team info"""
    
class cric_teamInfo(models.Model):
    id=models.AutoField(primary_key=True)
    team_name=models.CharField(max_length=200)
    team_nameShortForm=models.CharField(max_length=200)
    team_type=models.CharField(max_length=100)
    team_board=models.ForeignKey(cric_board,related_name='taem_borad',on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return (str(self.id)+" "+self.team_nameShortForm)
    
""" cricket series info"""
class cric_series(models.Model):
    id=models.AutoField(primary_key=True)
    series_name=models.CharField(max_length=200)
    series_host=models.ForeignKey(cric_board,related_name="host_team",on_delete=models.CASCADE)
    participate_team=models.ManyToManyField(cric_teamInfo,related_name="host_team")
    

    def __str__(self) -> str:
        return (str(self.id)+" "+self.series_name)
    


# Create your models here.
