import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Contacto

# Branding y personalización del espacio de Django Admin
admin.site.site_header = "Administración de Agenda de Contactos"
admin.site.site_title = "Agenda de Contactos"
admin.site.index_title = "Panel de Gestión de Contactos"


class ProveedorCorreoFilter(admin.SimpleListFilter):
    """Filtro personalizado en Django Admin para segmentar contactos por dominio de correo."""
    title = "proveedor de correo"
    parameter_name = "proveedor_correo"

    def lookups(self, request, model_admin):
        return (
            ("gmail", "Gmail"),
            ("outlook", "Outlook / Hotmail"),
            ("inacap", "INACAP"),
            ("otro", "Otros dominios"),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == "gmail":
            return queryset.filter(correo__icontains="@gmail")
        if val == "outlook":
            return queryset.filter(correo__icontains="@outlook") | queryset.filter(correo__icontains="@hotmail")
        if val == "inacap":
            return queryset.filter(correo__icontains="@inacap")
        if val == "otro":
            return (
                queryset.exclude(correo__icontains="@gmail")
                .exclude(correo__icontains="@outlook")
                .exclude(correo__icontains="@hotmail")
                .exclude(correo__icontains="@inacap")
            )
        return queryset


@admin.action(description="Exportar contactos seleccionados a CSV")
def exportar_contactos_csv(modeladmin, request, queryset):
    """Retorna los contactos seleccionados como archivo CSV descargable."""
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="contactos.csv"'

    # Añadir BOM para compatibilidad con Excel
    response.write("\ufeff".encode("utf-8"))

    writer = csv.writer(response)
    writer.writerow(("Nombre", "Teléfono", "Correo Electrónico", "Dirección"))

    for contacto in queryset.iterator():
        writer.writerow(
            (
                contacto.nombre,
                contacto.telefono,
                contacto.correo,
                contacto.direccion,
            )
        )

    return response


class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "correo", "direccion")
    search_fields = ("nombre", "correo")
    list_filter = (ProveedorCorreoFilter,)
    actions = (exportar_contactos_csv,)
    ordering = ("nombre",)
    list_per_page = 15


admin.site.register(Contacto, ContactoAdmin)
