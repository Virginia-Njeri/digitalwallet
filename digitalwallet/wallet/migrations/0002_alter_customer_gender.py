# Generated by Django 4.1 on 2022-09-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Female'), ('They', 'They')], max_length=40, null=True),
        ),
    ]
