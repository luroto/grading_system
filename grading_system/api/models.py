from django.db import models


tipo_documentos = [('CEDULA', 'CC'), ('CEDEXT','CE'), ('PASAPORTE', 'Pasaporte'),]
tipo_documentos_estudiantes = [('CEDULA', 'CC'), ('CEDEXT','CE'), ('PASAPORTE', 'Pasaporte'), ('TI', 'TI')]

class Profesor(models.Model):
	''' 

	'''


	apellidos = models.CharField("Apellidos del profesor", max_length=50)
	nombres = models.CharField("Nombres del profesor", max_length=50)
	tipo_documento = models.CharField(choices=tipo_documentos, max_length=9)
	numero_documento = models.IntegerField("Cédula del docente",  unique=True)
	direccion = models.CharField("Teacher's address", max_length=30)
	telefono = models.CharField("Teacher's phone", max_length=10)
	creado = models.DateField()

	class Meta:
		verbose_name = 'Profesor'
		verbose_name_plural = 'Profesores'
		ordering = ['apellidos']


	def __str__(self):
		return self.apellidos + ' ' + self.nombres


class Estudiante(models.Model):
	'''

	'''
	apellidos = models.CharField("Apellidos del estudiante", max_length=50)
	nombres = models.CharField("Nombre del estudiante", max_length=50)
	tipo_documento = models.CharField(choices=tipo_documentos_estudiantes, max_length=9)
	numero_documento = models.IntegerField("Numero de documento",  unique=True)
	direccion = models.CharField("Student's address", max_length=50)
	telefono = models.CharField("Student's phone", max_length=10)
	
	class Meta:
		verbose_name = 'Estudiante'
		verbose_name_plural = 'Estudiantes'
		ordering = ['apellidos']

	def __str__(self):
		return self.apellidos + ' ' + self.nombres

class Year(models.Model):
	'''
	
	'''
	year = models.IntegerField(unique=True)
	
	
	class Meta:
		verbose_name = 'Año'
		verbose_name_plural= 'Años'

	def __str__(self):
		return str(self.year)

class Area(models.Model):
	area_name = models.CharField("Area's name", max_length=15, unique=True)
	
	class Meta:
		verbose_name = 'Área'
		verbose_name_plural = 'Áreas'

	def __str__(self):
		return self.area_name

class Curso(models.Model):
	numero_curso = models.IntegerField("Código del curso", unique=True)
	
	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'

	
	def __str__(self):
		return str(self.numero_curso)


class AreadeCurso(models.Model):
	curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE) ##Revisar
	area_id = models.ForeignKey('Area', on_delete=models.CASCADE) 
	teacher_id = models.ManyToManyField('Profesor')
	year = models.ForeignKey('Year', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Área de curso'
		verbose_name_plural = 'Áreas de curso'
		unique_together = ['curso_id', 'area_id', 'year']
	
	def __str__(self):
		return '{}, {}, {} '.format(self.year, self.curso_id, self.area_id)


class EstudiantedeCurso(models.Model):
	course_id = models.ForeignKey('Curso', on_delete=models.CASCADE)## Revisar
	student_id = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
	year = models.ForeignKey('Year', on_delete=models.CASCADE)
	

	class Meta:
		verbose_name = 'Estudiante de curso'
		verbose_name_plural = 'Estudiantes de curso'
		unique_together = ['student_id', 'year']
		ordering = ['course_id', 'year'] 

	def __str__(self):
		return '{}, {}, {}'.format(self.year, self.course_id, self.student_id)

class Nota(models.Model):
	student_id = models.ForeignKey('EstudiantedeCurso', related_name='Curso', on_delete=models.CASCADE)
	area_id = models.ForeignKey('AreadeCurso', on_delete=models.CASCADE)
	grade = models.FloatField("Nota de 0.0 a 5.0")
	grade_description = models.CharField("Documento al que corresponde la nota", max_length=120)
	creado = models.DateField("Fecha de la nota")

	class Meta:
		verbose_name = 'Nota de estudiante'
		verbose_name = 'Notas de estudiante'

	def __str__(self):
		return '{}, {}, {}, {}, {}'.format(self.student_id.year, self.student_id,  self.area_id, self.grade, self.grade_description, self.creado)
