# Generated by Django 3.2.7 on 2021-09-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('meal', 'meal'), ('drink', 'drink'), ('desert', 'desert'), ('NONE', 'NONE')], default='NONE', max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
