# Generated by Django 5.0.1 on 2024-01-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
