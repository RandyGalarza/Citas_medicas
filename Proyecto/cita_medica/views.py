from django.shortcuts import render, redirect
from .models import ReservaCita,Paciente,Medico
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def inicio(request):
    citas = ReservaCita.objects.all()  # Obtén todas las citas médicas de la base de datos
    return render(request, 'inicio.html', {'citas': citas})

def registrar_paciente(request):
    if request.method == 'POST':
        p_nombre_paciente = request.POST['nombre_paciente']
        p_telefono = request.POST['telefono']
        p_email = request.POST['email']
        p_fecha_nacimiento = request.POST['fecha_nacimiento']
        p_genero = request.POST['genero']
        p_direccion = request.POST['direccion']
        p_estado = request.POST['estado']
        nuevo_paciente = Paciente(
            nombre_paciente=p_nombre_paciente,
            telefono=p_telefono,
            email=p_email,
            fecha_nacimiento=p_fecha_nacimiento,
            genero=p_genero,
            direccion=p_direccion,
            estado=p_estado,   
        )
        nuevo_paciente.save()
    paciente = Paciente.objects.all()
    return render(request, 'registrar_paciente.html', {'paciente': paciente})
@login_required
def lista_paciente(request):
    paciente = Paciente.objects.all()
    return render(request, 'lista_paciente.html', {'paciente': paciente})
@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        paciente.nombre_paciente = request.POST['nombre_paciente']
        paciente.telefono = request.POST['telefono']
        paciente.email = request.POST['email']
        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
        paciente.genero = request.POST['genero']
        paciente.direccion = request.POST['direccion']
        paciente.estado = request.POST['estado']
        paciente.save()

        return redirect('lista_paciente')  # Redirige de nuevo a la vista lista_pacientes después de la edición

    return render(request, 'editar_paciente.html', {'paciente': paciente})
@login_required
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    paciente.delete()

    return redirect('lista_paciente')
@login_required
def registrar_medico(request):
    if request.method == 'POST':
        m_nombre_medico = request.POST['nombre_medico']
        m_especialidad = request.POST['especialidad']
        m_telefono = request.POST['telefono']
        m_email = request.POST['email']
        m_genero= request.POST['genero']
        m_direccion = request.POST['direccion']
        m_estado = request.POST['estado']
        nuevo_medico = Medico(
            nombre_medico=m_nombre_medico,
            especialidad=m_especialidad,
            telefono=m_telefono,
            email=m_email,
            genero=m_genero,
            direccion=m_direccion,
            estado=m_estado,
        )
        nuevo_medico.save()

    medicos = Medico.objects.all()
    return render(request, 'registrar_medico.html', {'medicos': medicos})
@login_required
def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'lista_medicos.html', {'medicos': medicos})
@login_required
def editar_medico(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)

    if request.method == 'POST':
        medico.nombre_medico = request.POST['nombre_medico']
        medico.especialidad = request.POST['especialidad']
        medico.telefono = request.POST['telefono']
        medico.email = request.POST['email']
        medico.especialidad = request.POST['especialidad']
        medico.direccion = request.POST['direccion']
        medico.estado = request.POST['estado']
        medico.save()

        return redirect('lista_medicos') 

    return render(request, 'editar_medico.html', {'medico': medico})
@login_required
def eliminar_medico(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)
    medico.delete()

    return redirect('lista_medicos')

def reserva(request):
    if request.method == 'POST':
        p_nombre_paciente = request.POST['nombre_paciente']
        p_fecha_cita = request.POST['fecha_cita']
        p_hora_cita = request.POST['hora_cita']
        p_estado = request.POST['estado']
        p_tipo_cita = request.POST['tipo_cita']

        nueva_cita = ReservaCita(
            nombre_paciente=p_nombre_paciente,
            fecha_cita=p_fecha_cita,
            hora_cita=p_hora_cita,
            estado=p_estado,
            tipo_cita=p_tipo_cita
        )
        nueva_cita.save()  # Guarda la nueva cita en la base de datos

    citas = ReservaCita.objects.all()  # Obtén todas las citas médicas de la base de datos
    return render(request, 'reserva.html', {'citas': citas})

@login_required
def agenda(request):#incompleto
    return render(request, 'agenda.html')
@login_required
def reservas(request):
    reservas = ReservaCita.objects.all()
    return render(request, 'reservas.html', {'reservas': reservas})
@login_required
def lista_citas(request):
    citas = ReservaCita.objects.all()  
    return render(request, 'lista_citas.html', {'citas': citas})
@login_required
def editar_cita(request, reserva_id):
    reserva = get_object_or_404(ReservaCita, id=reserva_id)

    if request.method == 'POST':
        reserva.nombre_paciente = request.POST['nombre_paciente']
        reserva.fecha_cita = request.POST['fecha_cita']
        reserva.hora_cita = request.POST['hora_cita']
        reserva.estado = request.POST['estado']
        reserva.tipo_cita = request.POST['tipo_cita']
        reserva.save()

        return redirect('reserva')  # Redirige de nuevo a la vista reserva después de la edición

    return render(request, 'editar_cita.html', {'reserva': reserva})
@login_required
def eliminar_cita(request, reserva_id):
    reserva = get_object_or_404(ReservaCita, id=reserva_id)
    reserva.delete()

    return redirect('lista_citas')
def get_eventos(request):
    eventos = ReservaCita.objects.all()
    eventos_data = []
    
    for evento in eventos:
        evento_data = {
        'title': evento.nombre_paciente,
        'start': evento.fecha_cita.strftime('%Y-%m-%d') + 'T' + evento.hora_cita.strftime('%H:%M:%S'),
        'end': evento.fecha_cita.strftime('%Y-%m-%d') + 'T' + evento.hora_cita.strftime('%H:%M:%S'),
    }
        eventos_data.append(evento_data)
    
    return JsonResponse(eventos_data, safe=False)

def exit(request):
    logout(request)
    return(redirect('home'))