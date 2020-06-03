# Generated by Django 3.0.5 on 2020-06-03 10:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200520_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.UUIDField(default=uuid.UUID('f9592442-006d-4a4c-a7c9-73fd77dffff1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bill',
            name='generated_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
