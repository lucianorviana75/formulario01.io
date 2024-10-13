from django.shortcuts import render,redirect
from cliente.forms import ClienteForm
from cliente.models import Cliente

# Create your views here.
def cliente(request):
    data ={}
    data['db'] = Cliente.objects.all()
    return render(request,'index.html' ,data)

def formulario(request):
    data ={}
    data['form'] = ClienteForm()
    return render(request,'form.html' ,data)

def create(request):
    form = ClienteForm(request.POST or None)#recebe o resultado do post do formulario.
    if form. is_valid():#verificar se esta tudo certinho no formulario
        form.save()#Salvarno banco de dados
        return redirect('cliente')#retornar par pagina inicial
    
def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)    
       
       
def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'form.html', data)    
               
def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('cliente')   
    
def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('cliente')     