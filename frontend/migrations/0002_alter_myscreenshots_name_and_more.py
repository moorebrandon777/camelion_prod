# Generated by Django 5.0.3 on 2024-03-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myscreenshots',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='myscreenshots',
            name='screenshot',
            field=models.FileField(default='d.png', upload_to='screenshots'),
        ),
    ]
