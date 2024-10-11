from django.forms import ModelForm
from cliente.models import Cliente

# Create the form class.
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "email", "celular", "telefone_fixo"]