# Generated by Django 4.2.4 on 2023-08-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/checkMigrations/img'),
        ),
    ]
