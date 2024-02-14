from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Curso ,Estudiante,Profesor
from app1.forms import CursoForm,BuscarForm,EstudianteForm,ProfesorForm

# Create your views here.
def inicio(request):
    if request.method == 'POST':
        miFormulario = BuscarForm(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso.objects.filter(nombre__contains=informacion['nombre'])
            
            return render(request, "index.html", {"cursos": curso})
    else:
         miFormulario = BuscarForm()
    return render(request, 'index.html', {"formulario": miFormulario})

def cursos(request):
    if request.method == "POST":
 
            miFormulario = CursoForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "cursos.html")
    else:
            miFormulario = CursoForm()
    return render(request, "cursos.html", {"formulario": miFormulario})

def estudiantes(request):
    if request.method == "POST":
 
            miFormulario = EstudianteForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], fecha_nacimiento=informacion["fecha_nacimiento"], telefono=informacion["telefono"])
                  curso.save()
                  return render(request, "estudiantes.html")
    else:
            miFormulario = EstudianteForm()
    return render(request, "estudiantes.html", {"formulario": miFormulario})

def profesores(request):
    if request.method == "POST":
 
            miFormulario = ProfesorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"], fecha_nacimiento=informacion["fecha_nacimiento"], telefono=informacion["telefono"])
                  curso.save()
                  return render(request, "profesores.html")
    else:
            miFormulario = ProfesorForm()
    return render(request, "profesores.html", {"formulario": miFormulario})

def form_curso(request):

    if request.method == 'POST':
        curso=Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
            
        curso.save()
        return render(request,"index.html")
    return render(request,"form-curso.html")

def form_curso_2(request):
    if request.method == "POST":
 
            miFormulario = CursoForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "index.html")
    else:
            miFormulario = CursoForm()
    return render(request, "cursoFormulario.html", {"formulario": miFormulario})

def buscar(request):
    if request.method == 'POST':
        miFormulario = BuscarForm(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso.objects.filter(nombre__contains=informacion['nombre'])
            
            return render(request, "index.html", {"cursos": curso})
    else:
         miFormulario = BuscarForm()
    return render(request, 'index.html', {"formulario": miFormulario})