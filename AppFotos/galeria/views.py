import os
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from AppFotos import settings
from .models import Foto, Tarea, Nota
from .forms import NotaForm, FotoForm, TareaForm


def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'html/home.html', {'tareas': tareas})

from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm  # Asegúrate de importar correctamente TareaForm desde forms.py

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')  # Redirige a la lista de tareas después de crear la nueva tarea
    else:
        form = TareaForm()
    
    return render(request, 'html/crear_modulo.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea, Nota, Foto
from .forms import NotaForm, FotoForm

def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    notas = tarea.notas.all()

    if request.method == 'POST':
        nota_form = NotaForm(request.POST)
        foto_form = FotoForm(request.POST, request.FILES)

        if nota_form.is_valid():
            # Guardar la nota asociada a la tarea
            nota = nota_form.save(commit=False)
            nota.tarea = tarea
            nota.save()

            # Guardar las fotos asociadas a la nota
            fotos = request.FILES.getlist('imagenes')
            for foto in fotos:
                Foto.objects.create(nota=nota, imagen=foto)

            return redirect('detalle_tarea', tarea_id=tarea_id)
    else:
        nota_form = NotaForm()
        foto_form = FotoForm()

    return render(request, 'html/detalle_tarea.html', {
        'tarea': tarea,
        'notas': notas,
        'nota_form': nota_form,
        'foto_form': foto_form,
    })



def descargar_fotos_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)

    # Crear un archivo ZIP en memoria
    zip_filename = f'fotos_nota_{nota_id}.zip'
    zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)

    import zipfile
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for foto in nota.fotos.all():
            foto_path = foto.imagen.path
            zipf.write(foto_path, os.path.basename(foto_path))

    # Crear una respuesta HTTP para descargar el archivo ZIP
    response = HttpResponse(open(zip_path, 'rb'), content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'

    # Eliminar el archivo ZIP temporal después de descargarlo
    os.remove(zip_path)

    return response