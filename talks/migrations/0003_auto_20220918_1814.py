# Generated by Django 2.2.28 on 2022-09-18 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0002_auto_20220918_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='actor',
            field=models.ManyToManyField(related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='talk',
            name='participants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talk', to='talks.Participants'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talk', to=settings.AUTH_USER_MODEL),
        ),
    ]
