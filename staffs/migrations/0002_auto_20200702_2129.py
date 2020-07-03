# Generated by Django 3.0.8 on 2020-07-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='tz',
            field=models.CharField(choices=[('Africa/Abidjan', 'Africa/Abidjan'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Kolkata', 'Asia/Kolkata')], default='Asia/Kolkata', max_length=50),
        ),
    ]
