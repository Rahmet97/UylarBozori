# Generated by Django 3.1 on 2020-09-12 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics')),
                ('user', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('upload_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Viloyatlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viloyat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tumanlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('viloyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uybozor.viloyatlar')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('remaining_inf', models.TextField()),
                ('description', models.TextField()),
                ('announce_type', models.CharField(max_length=20)),
                ('announce_view', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=10)),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('img3', models.ImageField(upload_to='pics')),
                ('img4', models.ImageField(upload_to='pics')),
                ('img5', models.ImageField(upload_to='pics')),
                ('price', models.FloatField()),
                ('is_paid', models.BooleanField(default=True)),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('tuman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uybozor.tumanlar')),
                ('viloyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uybozor.viloyatlar')),
            ],
        ),
    ]