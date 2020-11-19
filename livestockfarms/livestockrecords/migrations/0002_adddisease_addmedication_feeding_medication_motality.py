# Generated by Django 3.1.3 on 2020-11-17 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livestockrecords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adddisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Addmedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('medicationType', models.CharField(choices=[('Drugs', 'Drugs'), ('Vaccination', 'Vaccination')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Motality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAdded', models.DateTimeField(auto_now_add=True, null=True)),
                ('datepurchased', models.DateField(null=True)),
                ('qty', models.IntegerField()),
                ('cause', models.TextField(null=True)),
                ('livestock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livestockrecords.livestock')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAdded', models.DateTimeField(auto_now_add=True, null=True)),
                ('datepurchased', models.DateField(null=True)),
                ('disease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livestockrecords.adddisease')),
                ('livestock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livestockrecords.livestock')),
                ('medication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livestockrecords.addmedication')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAdded', models.DateTimeField(auto_now_add=True, null=True)),
                ('datepurchased', models.DateField(null=True)),
                ('feedname', models.CharField(max_length=200, null=True)),
                ('qty', models.FloatField()),
                ('livestock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livestockrecords.livestock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
