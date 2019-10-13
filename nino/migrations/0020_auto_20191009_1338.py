# Generated by Django 2.0.13 on 2019-10-09 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0019_auto_20191009_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area_dental',
            options={'verbose_name': 'Area_Dental', 'verbose_name_plural': 'Area Dental'},
        ),
        migrations.AlterModelOptions(
            name='area_medica',
            options={'verbose_name': 'Area_Medica', 'verbose_name_plural': 'Area Medica'},
        ),
        migrations.AlterModelOptions(
            name='area_psicologica',
            options={'verbose_name': 'Area_Psicologica', 'verbose_name_plural': 'Area Psicologica'},
        ),
        migrations.AlterModelOptions(
            name='area_social',
            options={'verbose_name': 'Area_Social', 'verbose_name_plural': 'Area Social'},
        ),
        migrations.AlterModelOptions(
            name='fuente_estre',
            options={'verbose_name': 'Fuente_Estre', 'verbose_name_plural': 'Fuente de Estres'},
        ),
        migrations.AlterModelOptions(
            name='motivo_ingreso',
            options={'verbose_name': 'Motivo de Ingreso', 'verbose_name_plural': 'Motivo de Ingresos'},
        ),
        migrations.AlterModelOptions(
            name='nivel_nutricion',
            options={'verbose_name': 'Nivel_Nutricion', 'verbose_name_plural': 'Nivel de Nutricions'},
        ),
        migrations.AlterModelOptions(
            name='relacion_familia',
            options={'verbose_name': 'Relacion_Familia', 'verbose_name_plural': 'Relacion Familiar'},
        ),
        migrations.AlterField(
            model_name='area_medica',
            name='nivel_nutricion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nino.Nivel_Nutricion'),
        ),
        migrations.AlterField(
            model_name='nino',
            name='motivo_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Motivo_Ingreso'),
        ),
    ]
