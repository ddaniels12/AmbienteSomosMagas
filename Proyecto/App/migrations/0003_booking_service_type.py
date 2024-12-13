# Generated by Django 4.2.16 on 2024-11-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_schedule_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='service_type',
            field=models.CharField(choices=[('reiki', 'Reiki'), ('tarot', 'Tarot'), ('flowers', 'Terapia de Flores')], default='reiki', max_length=10),
        ),
    ]