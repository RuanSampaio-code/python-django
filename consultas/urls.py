from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/nova/', views.criar_consulta, name='criar_consulta'),
    path('consultas/editar/<int:consulta_id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/deletar/<int:consulta_id>/', views.deletar_consulta, name='deletar_consulta'),
    path('consultas/<int:consulta_id>/', views.detalhes_consulta, name='detalhes_consulta'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    #path('exportar/excel/', views.exportar_excel, name='exportar_excel'),


    # CRUD para médicos
    path('medicos/', views.listar_medicos, name='listar_medicos'),
    path('medicos/novo/', views.criar_medico, name='criar_medico'),
    path('medicos/editar/<int:medico_id>/', views.editar_medico, name='editar_medico'),
    path('medicos/deletar/<int:medico_id>/', views.deletar_medico, name='deletar_medico'),


    # CRUD para paciente
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/novo/', views.criar_paciente, name='criar_paciente'),
    path('pacientes/editar/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/deletar/<int:paciente_id>/', views.deletar_paciente, name='deletar_paciente'),
]