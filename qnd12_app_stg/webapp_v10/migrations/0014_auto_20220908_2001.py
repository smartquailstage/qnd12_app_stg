# Generated by Django 3.2.13 on 2022-09-09 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('webapp_v10', '0013_auto_20220908_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeriadeimagenes_5',
            name='logo_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo 1'),
        ),
        migrations.AddField(
            model_name='galeriadeimagenes_5',
            name='logo_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo 2'),
        ),
        migrations.AddField(
            model_name='galeriadeimagenes_5',
            name='logo_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo 3'),
        ),
        migrations.AddField(
            model_name='galeriadeimagenes_5',
            name='logo_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo 4'),
        ),
    ]