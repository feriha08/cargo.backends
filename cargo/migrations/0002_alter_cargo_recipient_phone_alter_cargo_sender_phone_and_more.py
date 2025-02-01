# Generated by Django 5.1.4 on 2024-12-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='recipient_phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='sender_phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
