from django.contrib import admin
from .models import Motivo_Ingreso, Idioma, Enfermedad, Nivel_Nutricion, Etnia, Fuente_Estre, Relacion_Familia, Nino, Area_Social, Area_Psicologica, Area_Medica, Noticia

admin.site.register(Motivo_Ingreso)
admin.site.register(Idioma)
admin.site.register(Enfermedad)
admin.site.register(Nivel_Nutricion)
admin.site.register(Etnia)
admin.site.register(Fuente_Estre)
admin.site.register(Relacion_Familia)
admin.site.register(Nino)
admin.site.register(Area_Social)
admin.site.register(Area_Psicologica)
admin.site.register(Area_Medica)
admin.site.register(Noticia)

class NinoAdmin(admin.ModelAdmin):
    '''Admin View for Nino'''

    list_display = ('nombre_nino','apellido_nino','sexo','motivo_ingreso','fecha_nacimiento','cui','fecha_evaluacion',)
    list_filter = ('fecha_evaluacion','motivo_ingreso',)
    search_fields = ('nombre_nino',)



