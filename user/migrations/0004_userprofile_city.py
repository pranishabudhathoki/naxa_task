# Generated by Django 3.1 on 2022-05-04 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='user.city'),
            preserve_default=False,
        ),
    ]
