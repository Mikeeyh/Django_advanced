# Generated by Django 5.0.3 on 2024-04-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='state',
            field=models.CharField(choices=[('Done', 'Done'), ('Not Done', 'Not Done')], default='Not Done', max_length=8),
        ),
    ]
