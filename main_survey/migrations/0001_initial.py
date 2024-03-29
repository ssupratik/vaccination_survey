# Generated by Django 2.2.23 on 2021-05-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_title', models.CharField(max_length=5)),
                ('full_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(max_length=50)),
                ('id_proof', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=12)),
                ('id_proof_no', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=50)),
                ('block', models.CharField(max_length=50)),
                ('vaccination_status', models.CharField(max_length=5)),
                ('date_of_second_dose', models.DateField(max_length=50)),
                ('registration_id', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
    ]
