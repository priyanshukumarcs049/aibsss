# Generated by Django 2.1.5 on 2019-02-19 10:55

from django.db import migrations, models
import faces.models


class Migration(migrations.Migration):

    dependencies = [
        ('faces', '0003_facedetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedetail',
            name='image',
            field=models.FileField(blank=True, upload_to=faces.models.faces),
        ),
    ]
