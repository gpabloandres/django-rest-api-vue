# Generated by Django 4.2.1 on 2023-06-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_plan_team_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_status',
            field=models.CharField(choices=[('active', 'Active'), ('cancelled', 'Cancelled')], default='active', max_length=20),
        ),
    ]
