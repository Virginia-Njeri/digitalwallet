# Generated by Django 4.1 on 2022-09-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_customer_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='nationality',
            field=models.CharField(choices=[('Kenyan', 'Kenyan'), ('Tanzanian', 'Tanzanian'), ('Rwandees', 'Rwandees')], max_length=15, null=True),
        ),
    ]
