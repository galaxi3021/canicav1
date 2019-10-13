from django.db import models

# Create your models here.
class Motivo_Ingreso(models.Model):
    """Model definition for Motivo_Ingreso."""

    # TODO: Define fields here
    nombre_motivo = models.CharField(max_length=60)
    descripcion=models.TextField()
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Motivo_Ingreso."""

        verbose_name = 'Motivo de Ingreso'
        verbose_name_plural = 'Motivo de Ingresos'

    def __str__(self):
        return self.nombre_motivo

class Idioma(models.Model):
    """Model definition for Idioma."""

    # TODO: Define fields here
    nombre_idioma = models.CharField(max_length=60)
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Idioma."""

        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return self.nombre_idioma

class Enfermedad(models.Model):
    """Model definition for Enfermedad."""

    # TODO: Define fields here
    nombre_enfermedad = models.CharField(max_length=60)
    descripcion=models.TextField()
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Enfermedad."""

        verbose_name = 'Enfermedad'
        verbose_name_plural = 'Enfermedads'

    def __str__(self):
        return self.nombre_enfermedad

class Nivel_Nutricion(models.Model):
    """Model definition for Nivel_Nutricion."""

    # TODO: Define fields here
    nivel = models.CharField(max_length=60)
    descripcion=models.TextField()
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Nivel_Nutricion."""

        verbose_name = 'Nivel de Nutricion'
        verbose_name_plural = 'Nivel de Nutricion'

    def __str__(self):
        return self.nivel

class Etnia(models.Model):
    """Model definition for Etnia."""

    # TODO: Define fields here
    nombre_etnia = models.CharField(max_length=60)
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Etnia."""

        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'

    def __str__(self):
        return self.nombre_etnia

class Fuente_Estre(models.Model):
    """Model definition for Fuente_Estre."""

    # TODO: Define fields here
    nombre_fuente = models.CharField(max_length=60)
    descripcion=models.TextField()
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Fuente_Estre."""

        verbose_name = 'Fuente de Estres'
        verbose_name_plural = 'Fuente de Estres'

    def __str__(self):
        return self.nombre_fuente

class Relacion_Familia(models.Model):
    """Model definition for Relacion_Familia."""

    # TODO: Define fields here
    tipo_relacion = models.CharField(max_length=60)

    class Meta:
        """Meta definition for Relacion_Familia."""

        verbose_name = 'Relación Familiar'
        verbose_name_plural = 'Relación Familiar'

    def __str__(self):
        return self.tipo_relacion

#################### Modelos para el registro biopsicosocial #############
class Nino(models.Model):
    """Model definition for Nino."""

    # TODO: Define fields here
    fecha_evaluacion = models.DateField()
    nombre_nino = models.CharField(max_length=60)
    apellido_nino = models.CharField(max_length=60)
    image = models.ImageField(upload_to="img")
    cui = models.CharField(max_length=60)
    masculino = 'mas'
    femenino = 'fem'
    opciones = [
        (masculino, 'Masculino'),
        (femenino, 'Femenino'),
    ]
    sexo = models.CharField(
        max_length=3,
        choices=opciones,
        default=masculino,
    )




    #sexo = models.CharField(max_length=3)
    grado_educativo=models.CharField(max_length=30,null=True)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=60)
    lugar_residencia = models.CharField(max_length=60)
    motivo_ingreso=models.ForeignKey(Motivo_Ingreso,on_delete=models.PROTECT)
    ocupacion = models.CharField(max_length=60,null=True)
    religion = models.CharField(max_length=30,null=True)
    idioma=models.ForeignKey(Idioma,on_delete=models.PROTECT)
    etnia=models.ForeignKey(Etnia,on_delete=models.PROTECT)
    nombre_madre = models.CharField(max_length=100)
    nombre_padre = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Nino."""

        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'

    def __str__(self):
        return self.nombre_nino

class Area_Dental(models.Model):
    """Model definition for Area_Dental."""

    # TODO: Define fields here
    nino=models.ForeignKey(Nino,on_delete=models.PROTECT)
    diagnostico = models.TextField()
    intervencion=models.TextField()
    proxima_cita=models.DateField()
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Area_Dental."""

        verbose_name = 'Area Dental'
        verbose_name_plural = 'Area Dental'

    

class Area_Social(models.Model):
    """Model definition for Area_Social."""

    # TODO: Define fields here
    nino=models.ForeignKey(Nino,on_delete=models.PROTECT)
    rol_familiar=models.TextField(null=True)
    relacion_familiar=models.ForeignKey(Relacion_Familia,on_delete=models.PROTECT)
    fuente_estres=models.ForeignKey(Fuente_Estre,on_delete=models.PROTECT)
    visitas_autorizadas=models.BooleanField()
    recurso_familiar=models.CharField(max_length=60,null=True)


    class Meta:
        """Meta definition for Area_Social."""

        verbose_name = 'Area Social'
        verbose_name_plural = 'Area Social'

    

class Area_Psicologica(models.Model):
    """Model definition for Area_Psicologica."""

    # TODO: Define fields here
    nino=models.ForeignKey(Nino,on_delete=models.CASCADE)
    estado_emocional=models.TextField(null=True)
    aspecto_clinico=models.TextField(null=True)
    percepcion_situacion_desproteccion=models.BooleanField()
    percepcion_calidad_vida=models.BooleanField()
    percepcion_temores_actuales=models.TextField(null=True)
    percepcion_temores_futuros=models.TextField(null=True)
    enfermedad=models.ForeignKey(Enfermedad,on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Area_Psicologica."""

        verbose_name = 'Area Psicologica'
        verbose_name_plural = 'Area Psicologica'

    

class Area_Medica(models.Model):
    """Model definition for Area_Medica."""

    # TODO: Define fields here
    nino=models.ForeignKey(Nino,on_delete=models.CASCADE)
    peso=models.IntegerField()
    altura=models.FloatField()
    presencia_piojos=models.BooleanField()
    presencia_acaros=models.BooleanField()
    programa_vacunacion=models.BooleanField()
    examen_sangre=models.BooleanField()
    examne_orina=models.BooleanField()
    estado_piel=models.TextField()
    nivel_nutricion=models.ForeignKey(Nivel_Nutricion,on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Area_Medica."""

        verbose_name = 'Area Medica'
        verbose_name_plural = 'Area Medica'

    def __str__(self):
        return str (self.nino) + "" + str (self.peso) + "" + str (self.altura)


class Noticia(models.Model):
    """Model definition for Noticia."""

    # TODO: Define fields here
    titulo_noticia=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to="img")
    fecha_publicacion=models.DateField()
    descripcion=models.TextField()


    class Meta:
        """Meta definition for Noticia."""

        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo_noticia+" "+ str (self.fecha_publicacion)

    



        




