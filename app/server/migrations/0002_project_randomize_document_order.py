# Generated by Django 2.1.7 on 2019-05-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='randomize_document_order',
            field=models.BooleanField(default=False),
        ),
    ]
