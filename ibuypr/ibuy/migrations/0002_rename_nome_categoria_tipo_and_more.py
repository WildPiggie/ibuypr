# Generated by Django 4.0.4 on 2022-04-27 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibuy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nome',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='categoria_fk',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='nome_imagem',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='utilizador_fk',
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='ibuy.categoria'),
        ),
    ]
