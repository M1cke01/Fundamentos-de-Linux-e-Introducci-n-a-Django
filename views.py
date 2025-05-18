import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre


def home(request):
    persona = Persona("Miguel", 23)
    curso = Curso("Fundamentos de Linux")

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + "Probando" + "Hola, me llamo Miguel",
        "python_ver": os.environ["PYTHON_VERSION"] + "Más cambios",
        "nombre_persona": persona.nombre,
        "nombre_curso": curso.nombre,
    }

    return render(request, "pages/home.html", context)
