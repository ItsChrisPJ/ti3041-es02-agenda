from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Contacto
from .forms import ContactoForm

def contacto_list(request):
    query = request.GET.get('q', '')
    if query:
        # Busca por nombre o por correo (case-insensitive)
        contactos = Contacto.objects.filter(
            Q(nombre__icontains=query) | Q(correo__icontains=query)
        )
    else:
        contactos = Contacto.objects.all()
    
    return render(request, 'contactos/contacto_list.html', {
        'contactos': contactos,
        'query': query
    })

def contacto_create(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_list')
    else:
        form = ContactoForm()
    
    return render(request, 'contactos/contacto_form.html', {'form': form})
