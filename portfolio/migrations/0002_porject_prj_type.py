# Generated by Django 3.0.7 on 2020-06-28 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='porject',
            name='prj_type',
            field=models.CharField(choices=[('mobile', 'Mobile'), ('web', 'Web'), ('upcomming', 'Upcomming')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
