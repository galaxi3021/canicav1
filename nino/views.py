from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Motivo_Ingreso, Idioma, Enfermedad, Nivel_Nutricion, Etnia, Fuente_Estre, Relacion_Familia, Nino, Area_Social, Area_Psicologica, Area_Medica
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def noticias(request):
    return render(request, 'noticias.html')

def programas(request):
    return render(request, 'programas.html')

class ProductoListView(generic.ListView):
    model = Area_Medica
    template_name = "list.html"



class ProductoDetailView(generic.DetailView):
    model = Area_Medica
    template_name = "detail.html"



class ProductoCreateView(generic.CreateView):
    model = Area_Medica
    fields='__all__'
    template_name = "form.html"


class ProductoUpdateView(generic.UpdateView):
    model = Area_Medica
    fields='__all__'
    template_name = "form.html"


class ProductoDeleteView(generic.DeleteView):
    model = Area_Medica
    template_name = "delete.html"
    success_url = reverse_lazy('tienda:index')


#vistas de las facturas 

# class FacturaListView(generic.ListView):
#     model = Factura
#     template_name = "facturas-list.html"

# class FacturaDetailView(generic.DetailView):
#     model = Factura
#     template_name = "facturas-detail.html"

#     def get_context_data(self, **kwargs):
#         context = super(FacturaDetailView, self).get_context_data(**kwargs)
#         context["detalle"] = Detalle.objects.filter(factura=self.object)
#         return context


# class DetalleInLine(InlineFormSetFactory):
#     model = Detalle
#     fields = '__all__'

# class FacturaCreateView(CreateWithInlinesView):
#     model = Factura
#     inlines = [DetalleInLine]
#     fields = '__all__'
#     template_name = "facturas-form.html"


# class FacturaUpdateView(UpdateWithInlinesView):
#     model = Factura
#     inlines = [DetalleInLine]
#     fields = '__all__'
#     template_name = "facturas-form.html"


# class FacturaDeleteView(generic.DeleteView):
#     model = Factura
#     template_name = "facturas-delete.html"
#     success_url = reverse_lazy('tienda:factura-index')



