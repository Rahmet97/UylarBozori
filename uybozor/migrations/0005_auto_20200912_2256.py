# Generated by Django 3.1 on 2020-09-12 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uybozor', '0004_auto_20200912_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='ann_type',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ann_view',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cond',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]