# Generated by Django 2.2.5 on 2019-10-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20191004_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='react',
            field=models.CharField(choices=[('noreact', 'No React'), ('like', 'Like'), ('dislike', 'Dislike')], max_length=10, verbose_name=''),
        ),
    ]
