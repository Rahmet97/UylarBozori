# Generated by Django 3.1 on 2020-09-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uybozor', '0006_announcement_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='phone',
            field=models.CharField(default='+(998)00 000 0000', max_length=20),
            preserve_default=False,
        ),
    ]
