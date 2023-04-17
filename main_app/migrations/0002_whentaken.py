# Generated by Django 4.2 on 2023-04-17 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhenTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('med', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.med')),
            ],
        ),
    ]
