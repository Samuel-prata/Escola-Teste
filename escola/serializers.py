from rest_framework import serializers
from escola.models import Aluno, Curso

#Transformando os dados em objetos serializados

#Esse arquivo também pode servir como um filtro para o que será mostrado como resposta da API

class AlunoSerializer (serializers.ModelSerializer):
    
    #Escolhendo o que quer serializar
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento']
        
class CursoSerializer (serializers.ModelSerializer):
    #Serializando tudo da classe Curso
    class Meta:
        model = Curso
        fields = '__all__'