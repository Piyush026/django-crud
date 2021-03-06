# Generated by Django 3.0.2 on 2020-01-14 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('emp_code', models.CharField(max_length=10)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_registration.Position')),
            ],
        ),
    ]
