# Generated by Django 3.0.5 on 2020-05-20 07:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.UUIDField(default=uuid.UUID('67b80684-678f-411d-ba26-3f0dcb4cf75a'), primary_key=True, serialize=False),
        ),
    ]
