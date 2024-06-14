from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    numero = models.IntegerField
    
    def __str__(self):
        return f'{self.nome}, {self.cpf}' 
    
class Curso (models.Model):
    
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, default='B')
     
    def __str__(self):
        return f'{self.descricao}'