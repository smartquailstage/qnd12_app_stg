# Generated by Django 3.2.16 on 2023-02-05 01:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.forms.models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('webapp_v10', '0019_auto_20230123_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='under_contruction',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('bio', wagtail.fields.RichTextField(blank=True, verbose_name='rseña bibliografica')),
                ('banner_title4', wagtail.fields.RichTextField(blank=True, verbose_name='Titulo de galeria-1 ')),
                ('banner_title5', wagtail.fields.RichTextField(blank=True, verbose_name='Titulo de galeria-2  ')),
                ('custom_title', models.CharField(blank=True, help_text='Reescribe el  Titulo de la publicacion ', max_length=100, null=True)),
                ('consulta', wagtail.fields.RichTextField(blank=True, verbose_name='Mensaje para que nos consulten por el formulario')),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GaleriadeImagenes_under',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen Slide Banner 1')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logotipo de Juan Silva Photo')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleria_under', to='webapp_v10.under_contruction')),
                ('profile_pic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto de perfil')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
