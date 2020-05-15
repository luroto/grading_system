from django.contrib import admin
from .models import Profesor, Estudiante, Curso, Area, AreadeCurso, EstudiantedeCurso, Nota, Year

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Area)
admin.site.register(AreadeCurso)
admin.site.register(EstudiantedeCurso)
admin.site.register(Nota)
admin.site.register(Year)
# Register your models here.
