from django.shortcuts import render, redirect
from .forms import NotaForm

error_data = {'error_message': 'the format data is not valid or the id already exists'}

def Home(request):
	return render(request, 'api/index.html')

def CrearNota(request):
	if request.method == 'POST':
		nota_form = NotaForm(request.POST)
		if nota_form.is_valid():
			nota_form.save()
			return redirect('index')
		else:
			return render(request, 'api/data_error.html', error_data)
	else:
		nota_form = NotaForm()
		return render(request, 'api/crear_entidad.html', {'entidad_form': nota_form})

def VerNotas(request):
	if request.method == 'GET':
