# Generated by Django 3.0.8 on 2020-07-03 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(default='', max_length=2500, unique=True)),
                ('real_name', models.CharField(default='', max_length=2500, unique=True)),
                ('tz', models.CharField(choices=[('Africa/Abidjan', 'Africa/Abidjan'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Kolkata', 'Asia/Kolkata')], default='Asia/Kolkata', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LoginLogoutLog',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='staffs.Employees')),
            ],
        ),
    ]