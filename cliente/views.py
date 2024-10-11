from django.shortcuts import render
from cliente.forms import ClienteForm

# Create your views here.
def cliente(request):
    return render(request,'index.html')

def formulario(request):
    return render(request,'form.html')