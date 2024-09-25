# Generated by Django 5.1.1 on 2024-09-15 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libary', '0003_collection_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='collection',
            name='year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='libary.genre'),
        ),
    ]
