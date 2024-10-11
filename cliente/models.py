from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    celular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telefone_fixo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')
    
    
    def _srt_(self) -> str:
        return self.nome