# Generated by Django 4.2.5 on 2023-10-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Цена')),
                ('image', models.ImageField(max_length=256, upload_to='', verbose_name='URL изображения')),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
                ('lte_exists', models.BooleanField(verbose_name='Наличие LTE')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
    ]
