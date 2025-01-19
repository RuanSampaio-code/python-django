from django import forms
from .models import Medico, Paciente, Consulta

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'