# Generated by Django 3.1 on 2020-09-12 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uybozor', '0002_remove_announcement_is_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ann_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ann_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='announce_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uybozor.ann_type'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='announce_view',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uybozor.ann_view'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uybozor.cond'),
        ),
    ]
