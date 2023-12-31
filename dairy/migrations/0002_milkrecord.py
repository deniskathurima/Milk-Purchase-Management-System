# Generated by Django 4.2.7 on 2023-11-30 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milk_qty', models.PositiveIntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairy.register')),
            ],
        ),
    ]
