from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    #Campos para alterar e editar
    list_display = ('id', 'nome', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    
    #Campo de busca
    search_fields = ('nome',)
    
    #Paginação com 20 alunos por pagina
    list_per_page = 20
    
admin.site.register(Aluno, Alunos)

class Cursos (admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    
    search_fields = ('codigo_curso',)
    
#Registro
admin.site.register(Curso, Cursos)