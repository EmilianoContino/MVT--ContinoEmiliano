# Generated by Django 4.1.1 on 2022-10-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_familiar_delete_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_ingresado',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
    ]
