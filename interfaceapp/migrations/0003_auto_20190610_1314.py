# Generated by Django 2.2.2 on 2019-06-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceapp', '0002_auto_20190610_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenttemp',
            name='title',
            field=models.CharField(default='default temp', max_length=200),
        ),
    ]
