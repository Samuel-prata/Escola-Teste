# Resolvendo importações
from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializers import AlunoSerializer, CursoSerializer

class AlunosViewSet (viewsets.ModelViewSet):
    '''Exibindo todos os Alunos e Alunas'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer



class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer