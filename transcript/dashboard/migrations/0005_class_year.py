# Generated by Django 4.2.1 on 2023-05-23 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_academicyear_academicyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.year'),
            preserve_default=False,
        ),
    ]
