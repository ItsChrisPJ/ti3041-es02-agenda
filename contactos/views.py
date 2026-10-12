from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Contacto
from .forms import ContactoForm


def contacto_list(request):
    """Lista todos los contactos con soporte de búsqueda y paginación."""
    query = request.GET.get('q', '').strip()
    if query:
        contactos_qs = Contacto.objects.filter(
            Q(nombre__icontains=query) | Q(correo__icontains=query)
        ).order_by('nombre')
    else:
        contactos_qs = Contacto.objects.all().order_by('nombre')

    # Paginación: 5 contactos por página
    paginator = Paginator(contactos_qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'contactos/contacto_list.html', {
        'page_obj': page_obj,
        'contactos': page_obj,
        'query': query,
        'total_count': contactos_qs.count(),
    })


def contacto_create(request):
    """Crea un nuevo contacto con validaciones y mensajes flash."""
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()
            messages.success(request, f'El contacto "{contacto.nombre}" fue creado exitosamente.')
            return redirect('contacto_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ContactoForm()

    return render(request, 'contactos/contacto_form.html', {
        'form': form,
        'titulo': 'Nuevo Contacto',
        'boton_texto': 'Guardar Contacto',
    })


def contacto_update(request, pk):
    """Edita un contacto existente con validación."""
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            contacto = form.save()
            messages.success(request, f'El contacto "{contacto.nombre}" fue actualizado correctamente.')
            return redirect('contacto_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ContactoForm(instance=contacto)

    return render(request, 'contactos/contacto_form.html', {
        'form': form,
        'contacto': contacto,
        'titulo': f'Editar Contacto: {contacto.nombre}',
        'boton_texto': 'Actualizar Cambios',
    })


def contacto_delete(request, pk):
    """Elimina un contacto con confirmación previa."""
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        nombre = contacto.nombre
        contacto.delete()
        messages.warning(request, f'El contacto "{nombre}" ha sido eliminado.')
        return redirect('contacto_list')

    return render(request, 'contactos/contacto_confirm_delete.html', {
        'contacto': contacto
    })
