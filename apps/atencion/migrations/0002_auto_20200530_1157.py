# Generated by Django 3.0.6 on 2020-05-30 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fichas',
            unique_together={('ci', 'fecha')},
        ),
    ]