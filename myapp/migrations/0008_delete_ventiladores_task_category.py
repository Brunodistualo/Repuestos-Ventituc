# Generated by Django 5.0 on 2023-12-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_ventiladores'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ventiladores',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]