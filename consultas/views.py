from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsultaForm
from .models import Consulta
from django.db.models import Count
from django.db.models.functions import TruncMonth
""" from django.template.loader import render_to_string """
""" from weasyprint import HTML
from django.http import HttpResponse
import openpyxl
from django.http import HttpResponse """


#medico
from .forms import MedicoForm
from .models import Medico

#paciente
from .forms import PacienteForm
from .models import Paciente




# Listar consultas
def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/listar_consultas.html', {'consultas': consultas})

# Criar consulta
def criar_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'consultas/formulario_consultas.html', {'form': form, 'titulo': 'Nova Consulta'})

# Editar consulta
def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == "POST":
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consultas/formulario_consultas.html', {'form': form, 'titulo': 'Editar Consulta'})

# Deletar consulta
def deletar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == "POST":
        consulta.delete()
        return redirect('listar_consultas')
    return render(request, 'consultas/deletar_consulta.html', {'consulta': consulta})


def detalhes_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    return render(request, 'consultas/detalhes_consulta.html', {'consulta': consulta})


def dashboard(request):
    # Número de consultas por médico
    consultas_por_medico = Consulta.objects.values('medico__nome').annotate(total=Count('id')).order_by('-total')

    # Número de consultas por mês
    consultas_por_mes = Consulta.objects.annotate(mes=TruncMonth('data_horario')).values('mes').annotate(total=Count('id')).order_by('mes')

    return render(request, 'consultas/dashboard.html', {
        'consultas_por_medico': consultas_por_medico,
        'consultas_por_mes': consultas_por_mes,
    })

""" 

def exportar_pdf(request):
    consultas = Consulta.objects.all()
    html = render_to_string('consultas/relatorio_consultas.html', {'consultas': consultas})
    pdf = HTML(string=html).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="consultas.pdf"'
    return response



def exportar_excel(request):
    consultas = Consulta.objects.all()
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Consultas"

    # Cabeçalhos
    sheet.append(["ID", "Médico", "Paciente", "Data e Hora", "Descrição"])

    # Dados
    for consulta in consultas:
        sheet.append([consulta.id, consulta.medico.nome, consulta.paciente.nome, consulta.data_horario, consulta.descricao])

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="consultas.xlsx"'
    workbook.save(response)
    return response """


#views para medico: 
# Criar um novo médico
def criar_medico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm()
    return render(request, 'consultas/formulario.html', 
        {'form': form, 
        'titulo': 'Novo Médico',
        'tipo': 'Medico'})

# Listar todos os médicos
def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'consultas/listar.html', {
        'lista': medicos,  # Alterado para usar 'lista'
        'titulo': 'Lista de Médicos',
        'editar_url': 'editar_medico',
        'deletar_url': 'deletar_medico',
        'criar_url': 'criar_medico',
        'tipo': 'Médico',  # Passa o tipo para o botão "Novo"
    })

# Atualizar um médico
def editar_medico(request, medico_id):
    medico = Medico.objects.get(id=medico_id)
    if request.method == "POST":
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'consultas/formulario.html', {'form': form, 'titulo': 'Editar Médico'})

# Deletar um médico
def deletar_medico(request, medico_id):
    medico = Medico.objects.get(id=medico_id)
    if request.method == "POST":
        medico.delete()
        return redirect('listar_medicos')
    return render(request, 'consultas/deletar.html', {'medico': medico, 'titulo': 'Deletar Médico'})



def criar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'consultas/formulario.html', {'form': form, 'titulo': 'Novo Paciente'})

# Listar todos os paciente
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'consultas/listar.html', {
        'lista': pacientes,  # Alterado para usar 'lista'
        'titulo': 'Lista de Pacientes',
        'editar_url': 'editar_paciente',
        'deletar_url': 'deletar_paciente',
        'criar_url': 'criar_paciente',
        'tipo': 'Paciente',  # Passa o tipo para o botão "Novo"
    })

# Atualizar um paciente
def editar_paciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'consultas/formulario.html', {'form': form, 'titulo': 'Editar paciente'})

# Deletar um paciente
def deletar_paciente(request, Paciente_id):
    paciente = Paciente.objects.get(id=Paciente_id)
    if request.method == "POST":
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'consultas/deletar.html', {'Paciente': paciente, 'titulo': 'Deletar paciente'})