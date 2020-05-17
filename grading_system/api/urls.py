from django.urls import path
from .views import Home, CrearProfesor, CrearEstudiante, CrearArea, CrearAnio, CrearCurso, CrearAreadeCurso, CrearEstudiantedeCurso, CrearNota

urlpatterns = [
	path('', Home, name='index'),
#	path('data_error', DataError, name='data_error'),
	path('crear_nota', CrearNota, name='CrearNota'),
	path('estudiante/<:int>/notas', VerNotas, name='VerNotas'),
]
