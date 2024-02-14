from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores,name='profesores'),
    path('form-curso/', views.form_curso, name='formCurso'),
    path('form-curso-2/', views.form_curso_2, name='formCurso2'),
    path('buscar/', views.buscar, name='buscar')
]