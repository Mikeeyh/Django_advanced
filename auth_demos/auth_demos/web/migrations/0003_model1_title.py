# Generated by Django 5.0.2 on 2024-03-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_model2'),
    ]

    operations = [
        migrations.AddField(
            model_name='model1',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
