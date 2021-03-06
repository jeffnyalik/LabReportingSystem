# Generated by Django 3.2.7 on 2021-10-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_delete_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_fac_staff', models.BooleanField(default=False, verbose_name='Facility status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser')),
            ],
        ),
    ]
