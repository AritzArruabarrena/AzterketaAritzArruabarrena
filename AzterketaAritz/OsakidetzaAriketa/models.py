from django.db import models
from django.utils import timezone
# Create your models here.
class Medikua(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=125)
    jaiotze_data = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"Medikuaren izena: {self.izena}, abizena: {self.abizena}eta jaiotze_data: {self.jaiotze_data}"
    
class Paziente(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=125)
    jaiotze_data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Pazientearen izena: {self.izena} , abizena: {self.abizena} eta jaiotze_data: {self.jaiotze_data}"

class Zitak(models.Model):
    id = models.AutoField(primary_key=True)
    hasiera_data = models.DateTimeField(default=timezone.now)
    bukaera_data = models.DateTimeField(default=timezone.now)
    mediku_id = models.ForeignKey(Medikua,on_delete=models.CASCADE)
    paziente_id = models.ForeignKey(Paziente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Zitak: Hasiera-data: {self.hasiera_data}, bukaera-data: {self.bukaera_data}, Medikuaren izen abizenak: {self.mediku_id.izena} {self.mediku_id.abizena} eta Pazientearen izen abizenak: {self.paziente_id.izena} {self.paziente_id.abizena}"