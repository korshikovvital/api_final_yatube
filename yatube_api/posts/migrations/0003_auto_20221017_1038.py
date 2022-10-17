# Generated by Django 2.2.16 on 2022-10-17 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20221017_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default='dcfe', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описания'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]