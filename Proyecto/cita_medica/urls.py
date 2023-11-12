from django.urls import path
from . import views
urlpatterns = [
    path('agenda/', views.agenda, name='agenda'),
    path('', views.inicio, name='inicio'),
    path('registrar_paciente/', views.registrar_paciente, name='registrar_paciente'),  
    path('reserva/', views.reserva, name='reserva'),
    path('lista_citas/', views.lista_citas, name='lista_citas'),
    path('eliminar_cita/<int:reserva_id>/', views.eliminar_cita, name='eliminar_cita'),
    path('editar_cita/<int:reserva_id>/', views.editar_cita, name='editar_cita'),
    path('get_eventos/', views.get_eventos, name='get_eventos'),
    path('editar_paciente/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar_paciente/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('lista_paciente/', views.lista_paciente, name='lista_paciente'),
    path('registrar_medico/', views.registrar_medico, name='registrar_medico'),
    path('lista_medicos/', views.lista_medicos, name='lista_medicos'),
    path('editar_medico/<int:medico_id>/', views.editar_medico, name='editar_medico'),
    path('eliminar_medico/<int:medico_id>/', views.eliminar_medico, name='eliminar_medico'),
    path('logout/',views.exit,name="exit")
]

